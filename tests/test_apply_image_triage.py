"""Prover test for scripts/apply_image_triage.py.

The executor reads the triage manifest and, for images marked ``own``, localizes
them: the essay's ``<img src>`` (or image ``<a href>``) is rewritten from the
external URL to ``assets/<file>``, downloading the file first if no local copy
exists. Other dispositions are left for later passes. Rewrites are exact-string
and idempotent (never touch prose).
"""
import sys
from pathlib import Path

import yaml
import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import apply_image_triage as ait  # noqa: E402

WP = "http://codecraft.co/wp-content/uploads/2008/foo.png?w=128"


def _setup(tmp_path, rows, essay_body, local_files=("foo.png",)):
    tmp_path.mkdir(parents=True, exist_ok=True)
    (tmp_path / "assets").mkdir()
    for f in local_files:
        (tmp_path / "assets" / f).write_bytes(b"\x89PNG" + b"0" * 2000)
    (tmp_path / "a.md").write_text(
        "---\ntitle: T\nitem_id: CC-000001\n---\n" + essay_body, encoding="utf-8")
    manifest_dir = tmp_path / "assets"
    (manifest_dir / "image-triage.yml").write_text(
        yaml.safe_dump({"images": rows}), encoding="utf-8")
    return tmp_path


def _row(**kw):
    base = {"essay": "a.md", "type": "img", "kind": "wp", "host": "codecraft.co",
            "src": WP, "local_match": "foo.png", "alt": "x", "disposition": "own"}
    base.update(kw)
    return base


def test_own_image_with_local_copy_is_rewritten(tmp_path):
    root = _setup(tmp_path, [_row()], f'<img alt="x" src="{WP}">')
    actions = ait.localize(root, apply=True)
    body = (root / "a.md").read_text(encoding="utf-8")
    assert 'src="assets/foo.png"' in body
    assert "codecraft.co" not in body
    assert any(a["status"] == "rewritten" for a in actions)


def test_dry_run_does_not_modify(tmp_path):
    root = _setup(tmp_path, [_row()], f'<img alt="x" src="{WP}">')
    ait.localize(root, apply=False)
    assert WP in (root / "a.md").read_text(encoding="utf-8")


def test_idempotent(tmp_path):
    root = _setup(tmp_path, [_row()], f'<img alt="x" src="{WP}">')
    ait.localize(root, apply=True)
    actions2 = ait.localize(root, apply=True)
    body = (root / "a.md").read_text(encoding="utf-8")
    assert body.count('src="assets/foo.png"') == 1
    assert all(a["status"] != "rewritten" for a in actions2)


def test_non_own_dispositions_untouched(tmp_path):
    for disp in ("", "generate", "redraw", "drop"):
        root = _setup(tmp_path / disp.zfill(1) if disp else tmp_path / "blank",
                      [_row(disposition=disp, local_match="")],
                      f'<img alt="x" src="{WP}">')
        ait.localize(root, apply=True)
        assert WP in (root / "a.md").read_text(encoding="utf-8"), f"{disp!r} touched"


def test_prose_untouched(tmp_path):
    body = f'Some prose about codecraft.co the site.\n\n<img alt="x" src="{WP}">\n\nMore prose.'
    root = _setup(tmp_path, [_row()], body)
    ait.localize(root, apply=True)
    out = (root / "a.md").read_text(encoding="utf-8")
    assert "Some prose about codecraft.co the site." in out
    assert "More prose." in out


def test_download_when_no_local_copy(tmp_path):
    url = "http://codecraft.co/wp-content/uploads/2014/05/bar.png?w=646"
    root = _setup(tmp_path, [_row(src=url, local_match="")],
                  f'<img alt="x" src="{url}">', local_files=())
    fetched = {}

    def fake_fetch(u):
        fetched["url"] = u
        return b"\x89PNG" + b"Z" * 3000

    actions = ait.localize(root, apply=True, fetch=fake_fetch)
    assert fetched["url"] == url
    assert (root / "assets" / "bar.png").is_file()
    body = (root / "a.md").read_text(encoding="utf-8")
    assert 'src="assets/bar.png"' in body
    assert any(a["status"] == "downloaded" for a in actions)


def test_already_canonical_src_is_unchanged(tmp_path):
    # A row whose src is already assets/<file> must report 'unchanged', not 'rewritten'.
    root = _setup(tmp_path, [_row(src="assets/foo.png", local_match="foo.png")],
                  '<img alt="x" src="assets/foo.png">')
    actions = ait.localize(root, apply=True)
    assert all(a["status"] != "rewritten" for a in actions)
    assert any(a["status"] == "unchanged" for a in actions)


def test_normalizes_leading_slash_assets(tmp_path):
    # /assets/foo.png and ../assets/foo.png should normalize to assets/foo.png.
    root = _setup(tmp_path, [_row(src="/assets/foo.png", local_match="foo.png")],
                  '<img alt="x" src="/assets/foo.png">')
    ait.localize(root, apply=True)
    assert 'src="assets/foo.png"' in (root / "a.md").read_text(encoding="utf-8")


def test_link_type_href_rewritten(tmp_path):
    root = _setup(tmp_path, [_row(type="link")],
                  f'<a href="{WP}">see chart</a>')
    ait.localize(root, apply=True)
    assert 'href="assets/foo.png"' in (root / "a.md").read_text(encoding="utf-8")
