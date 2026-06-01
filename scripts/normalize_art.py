#!/usr/bin/env python3
"""Knock the background out of generated line-art images → transparent PNGs.

openart.ai gives every image a slightly different solid-ish light background, so
on the site each would show a faint rectangle. This makes the art *float*: it
removes only the **exterior, connected** background (flood-filled from the four
corners), leaving interior light fills (e.g. a cream service-window) intact.
Output is RGBA PNG, so the art sits on any page color (and a future dark mode).

Pair with docs/art-style.md (prompts ask for a plain uniform light background,
which knocks out cleanest).

Usage:
    python scripts/normalize_art.py assets/naming-rose-tag.png [more.png ...]
    python scripts/normalize_art.py --from-prompts   # all art-prompts images present in assets/
"""
import argparse
import os
import sys

from PIL import Image, ImageDraw

_SENTINEL = (255, 0, 255)  # magenta — absent from the warm-brown palette


def knockout(img, thresh=60):
    """Return an RGBA copy with the exterior background made transparent."""
    rgb = img.convert("RGB")
    w, h = rgb.size
    for corner in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)):
        ImageDraw.floodfill(rgb, corner, _SENTINEL, thresh=thresh)
    rgba = rgb.convert("RGBA")
    transparent = (0, 0, 0, 0)
    rgba.putdata([transparent if p[:3] == _SENTINEL else p for p in rgba.getdata()])
    return rgba


def downscale(img, max_size=1024):
    """Shrink so the longest side is <= max_size (never upscales)."""
    w, h = img.size
    if max(w, h) <= max_size:
        return img
    scale = max_size / max(w, h)
    return img.resize((round(w * scale), round(h * scale)), Image.LANCZOS)


def process_file(path, thresh=60, max_size=1024):
    """Downscale (web size), knock out the background, save an optimized PNG."""
    with Image.open(path) as im:
        out = knockout(downscale(im, max_size), thresh=thresh)
    # always write PNG (alpha); if the source wasn't .png, switch the extension
    target = os.path.splitext(path)[0] + ".png"
    out.save(target, optimize=True)
    return target


def _from_prompts(root):
    import yaml
    data = yaml.safe_load(open(os.path.join(root, "assets", "art-prompts.yml"),
                                encoding="utf-8")) or {}
    names = [e["filename"] for e in data.get("images", [])]
    return [os.path.join(root, "assets", n) for n in names
            if os.path.isfile(os.path.join(root, "assets", n))]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="image files to process")
    ap.add_argument("--from-prompts", action="store_true",
                    help="process every art-prompts.yml image found in assets/")
    ap.add_argument("--thresh", type=int, default=60,
                    help="background colour tolerance (default 60)")
    ap.add_argument("--max-size", type=int, default=1024,
                    help="downscale longest side to this many px (default 1024)")
    args = ap.parse_args(argv)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = list(args.files)
    if args.from_prompts:
        files += _from_prompts(root)
    if not files:
        ap.error("no files given (pass paths or --from-prompts)")

    for path in files:
        before = os.path.getsize(path) if os.path.isfile(path) else 0
        target = process_file(path, thresh=args.thresh, max_size=args.max_size)
        after = os.path.getsize(target)
        print(f"  {os.path.basename(target)}: {before//1024} KB → {after//1024} KB transparent")


if __name__ == "__main__":
    main()
