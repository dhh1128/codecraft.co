"""scripts/ingest_art.py wires a generated image into the site end-to-end:
copy → assets (normalized, 0644), rewrite the essay <img src>, strip the now-false
Flickr photo credit, record CREDITS, mark the prompt done, delete the download."""
import os
import stat
import sys
from pathlib import Path

import yaml
import pytest

pytest.importorskip("PIL")
from PIL import Image, ImageDraw  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import ingest_art as ia  # noqa: E402

SRC = "http://farm1.staticflickr.com/28/51430866_94b353ee35_m.jpg"


def _setup(tmp_path):
    (tmp_path / "assets").mkdir()
    (tmp_path / "essay.md").write_text(
        "---\ntitle: T\nitem_id: CC-000001\n---\n"
        f'<figure><img alt="" src="{SRC}" width="240" height="225" />'
        "<figcaption>A nice thing. Photo credit: Someone (Flickr)</figcaption></figure>\n",
        encoding="utf-8")
    (tmp_path / "assets" / "art-prompts.yml").write_text(yaml.safe_dump({
        "style_suffix": "S", "negative_prompt": "N",
        "images": [{"essay": "essay.md", "replaces": SRC, "caption": "x",
                    "concept": "a rose", "filename": "naming-rose-tag.png",
                    "prompt": "a rose, S", "status": "pending"}]}), encoding="utf-8")
    dl = tmp_path / "downloads"
    dl.mkdir()
    p = dl / "rose.png"
    im = Image.new("RGB", (1500, 1100), (240, 238, 232))
    ImageDraw.Draw(im).rectangle([600, 400, 900, 700], fill=(73, 23, 5))
    im.save(p)
    os.chmod(p, 0o777)  # emulate the Windows-download +x
    return tmp_path, dl


# ---- pure helpers --------------------------------------------------------------

def test_rewrite_src():
    out = ia.rewrite_src(f'x <img src="{SRC}"> y', SRC, "assets/r.png")
    assert 'src="assets/r.png"' in out and SRC not in out


def test_strip_flickr_credit_keeps_description():
    t = f'<img src="{SRC}"><figcaption>A nice thing. Photo credit: Someone (Flickr)</figcaption>'
    out = ia.strip_flickr_credit(t, SRC)
    assert "A nice thing." in out
    assert "Photo credit" not in out and "Flickr" not in out


def test_strip_credit_only_caption_drops_figcaption():
    t = f'<img src="{SRC}"><figcaption>photo credit: SpecialKRB (Flickr)</figcaption>'
    out = ia.strip_flickr_credit(t, SRC)
    assert "<figcaption>" not in out


def test_strip_img_dimensions():
    t = '<img title="x" src="assets/r.png" alt="" width="240" height="225" />'
    out = ia.strip_img_dimensions(t, "assets/r.png")
    assert "width=" not in out and "height=" not in out
    assert 'src="assets/r.png"' in out and 'title="x"' in out  # other attrs kept


# ---- end-to-end ----------------------------------------------------------------

def test_ingest_end_to_end(tmp_path):
    root, dl = _setup(tmp_path)
    actions = ia.ingest(str(root), {"rose.png": "naming-rose-tag.png"},
                        str(dl), today="2026-06-01")

    asset = root / "assets" / "naming-rose-tag.png"
    # 1. normalized asset: exists, RGBA, downscaled, transparent, and NOT +x
    assert asset.is_file()
    im = Image.open(asset)
    assert im.mode == "RGBA" and max(im.size) <= 1024
    assert im.getpixel((0, 0))[3] == 0
    mode = stat.S_IMODE(os.stat(asset).st_mode)
    assert not (mode & 0o111), f"asset should not be executable, got {oct(mode)}"

    # 2. essay rewritten + credit stripped
    body = (root / "essay.md").read_text(encoding="utf-8")
    assert 'src="assets/naming-rose-tag.png"' in body
    assert SRC not in body
    assert "Flickr" not in body and "A nice thing." in body
    assert "width=" not in body and "height=" not in body  # stale dims removed

    # 3. CREDITS recorded
    creds = yaml.safe_load((root / "assets" / "CREDITS.yml").read_text(encoding="utf-8"))
    e = creds["images"]["naming-rose-tag.png"]
    assert e["origin"] == "AI-generated" and e["model"] == "openart.ai"
    assert e["prompt"] == "a rose, S" and e["book_safe"] is True
    assert "essay.md" in e["used_in"]

    # 4. prompt marked done
    pr = yaml.safe_load((root / "assets" / "art-prompts.yml").read_text(encoding="utf-8"))
    assert pr["images"][0]["status"] == "done"

    # 5. source download removed
    assert not (dl / "rose.png").exists()
    assert any(a["status"] == "ingested" for a in actions)
