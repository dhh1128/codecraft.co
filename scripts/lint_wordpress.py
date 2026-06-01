#!/usr/bin/env python3
"""Remove WordPress export residue from essay bodies.

Currently handles:

- ``[caption ...]<a><img/></a> Caption text[/caption]`` shortcodes →
  ``<figure><a><img/></a><figcaption>Caption text</figcaption></figure>``.
  The inner image element is preserved verbatim (image-src localization and
  ``<img>`` attribute normalization are separate steps); only the shortcode
  wrapper is converted and the trailing text becomes a ``<figcaption>``.

Operates on the body only (never the frontmatter, so comment text is left
alone). Idempotent. ``--check-only`` reports without writing (exit 1 if stale).
More residue fixers will be added here over time.
"""
import argparse
import glob
import re
import sys

META_FILES = {"README.md", "AGENTS.md", "CLAUDE.md", "ROADMAP.md", "index.md"}
CAPTION_RE = re.compile(r"\[caption[^\]]*\](.*?)\[/caption\]", re.S)
LEAD_RE = re.compile(r"\s*(<a\b.*?</a>|<img\b[^>]*>)\s*(.*?)\s*$", re.S)


def _convert(m):
    lm = LEAD_RE.match(m.group(1))
    if not lm:
        return m.group(0)  # not the expected shape; leave it (will be reported)
    fig, cap = lm.group(1).strip(), lm.group(2).strip()
    inner = f"{fig}<figcaption>{cap}</figcaption>" if cap else fig
    return f"<figure>{inner}</figure>"


def fix_text(text):
    m = re.match(r"^(---\n.*?\n---\n)(.*)$", text, re.S)
    if m:
        return m.group(1) + CAPTION_RE.sub(_convert, m.group(2))
    return CAPTION_RE.sub(_convert, text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()

    files = args.files or [f for f in sorted(glob.glob("*.md")) if f not in META_FILES]
    stale = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        new = fix_text(text)
        if new != text:
            stale += 1
            n = len(CAPTION_RE.findall(text))
            print(("WOULD CONVERT" if args.check_only else "CONVERTED"), f,
                  f"({n} caption(s))")
            if not args.check_only:
                open(f, "w", encoding="utf-8").write(new)
    if not stale:
        print("No [caption] shortcodes found.")
    if args.check_only and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
