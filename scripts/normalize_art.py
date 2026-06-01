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
    px = rgba.load()
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            if (r, g, b) == _SENTINEL:
                px[x, y] = (0, 0, 0, 0)
    return rgba


def process_file(path, thresh=60):
    with Image.open(path) as im:
        out = knockout(im, thresh=thresh)
    # always write PNG (alpha); if the source wasn't .png, switch the extension
    target = os.path.splitext(path)[0] + ".png"
    out.save(target)
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
    args = ap.parse_args(argv)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = list(args.files)
    if args.from_prompts:
        files += _from_prompts(root)
    if not files:
        ap.error("no files given (pass paths or --from-prompts)")

    for path in files:
        target = process_file(path, thresh=args.thresh)
        print(f"  knocked out background → {target}")


if __name__ == "__main__":
    main()
