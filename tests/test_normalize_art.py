"""scripts/normalize_art.py knocks the (variable) background out of generated
line-art images so they float transparently on any page color. It removes only
the *exterior, connected* background — interior light fills (e.g. a cream
service-window) must survive."""
import sys
from pathlib import Path

import pytest

pytest.importorskip("PIL")
from PIL import Image, ImageDraw  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import normalize_art as na  # noqa: E402

BG = (240, 238, 232)      # warm off-white, like the generator output
INK = (73, 23, 5)         # brand brown linework


def test_exterior_background_becomes_transparent():
    im = Image.new("RGB", (40, 40), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([14, 14, 26, 26], fill=INK)     # solid dark blob, away from edges
    out = na.knockout(im)
    assert out.mode == "RGBA"
    for corner in [(0, 0), (39, 0), (0, 39), (39, 39)]:
        assert out.getpixel(corner)[3] == 0, f"corner {corner} not transparent"
    assert out.getpixel((20, 20))[3] == 255, "the ink blob should stay opaque"


def test_enclosed_light_fill_survives():
    # A dark ring with a light (bg-colored) interior; the interior is NOT
    # connected to the outside, so it must NOT be knocked out.
    im = Image.new("RGB", (40, 40), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([10, 10, 30, 30], outline=INK, width=3)   # ring; interior stays BG color
    out = na.knockout(im)
    assert out.getpixel((0, 0))[3] == 0, "exterior should be transparent"
    assert out.getpixel((20, 20))[3] == 255, "enclosed light fill must survive"


def test_process_file_downscales_large_images(tmp_path):
    p = tmp_path / "big.png"
    im = Image.new("RGB", (2000, 1500), BG)
    ImageDraw.Draw(im).rectangle([800, 600, 1200, 900], fill=INK)
    im.save(p)
    na.process_file(str(p), max_size=1024)
    out = Image.open(p)
    assert max(out.size) == 1024          # downscaled to the cap
    assert out.size == (1024, 768)        # aspect preserved
    assert out.mode == "RGBA"
    assert out.getpixel((0, 0))[3] == 0   # still knocked out


def test_small_images_are_not_upscaled(tmp_path):
    p = tmp_path / "small.png"
    Image.new("RGB", (300, 200), BG).save(p)
    na.process_file(str(p), max_size=1024)
    assert max(Image.open(p).size) == 300


def test_process_file_writes_rgba_png(tmp_path):
    p = tmp_path / "art.png"
    im = Image.new("RGB", (20, 20), BG)
    ImageDraw.Draw(im).rectangle([7, 7, 13, 13], fill=INK)
    im.save(p)
    na.process_file(str(p))
    reopened = Image.open(p)
    assert reopened.mode == "RGBA"
    assert reopened.getpixel((0, 0))[3] == 0
