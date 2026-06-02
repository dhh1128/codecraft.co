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
FENCE_RE = re.compile(r"^(---\n)(.*?\n)(---\n)(.*)$", re.S)
AUTHOR_RE = re.compile(r"^  - author:\s*(.*)$")
PINGBACK = ("&laquo;", "«")


def _convert(m):
    lm = LEAD_RE.match(m.group(1))
    if not lm:
        return m.group(0)  # not the expected shape; leave it (will be reported)
    fig, cap = lm.group(1).strip(), lm.group(2).strip()
    inner = f"{fig}<figcaption>{cap}</figcaption>" if cap else fig
    return f"<figure>{inner}</figure>"


def _drop_empty_comments_key(text):
    """Remove a bare ``comments:`` line that has no list items left under it."""
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if lines[i].rstrip() == "comments:":
            j, has_item = i + 1, False
            while j < len(lines) and not re.match(r"^\S", lines[j]):
                if lines[j].startswith("  - "):
                    has_item = True
                    break
                j += 1
            if not has_item:
                i += 1
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def drop_pingback_comments(fm):
    """Drop comment list-items whose author carries the « pingback separator."""
    lines = fm.split("\n")
    out, i = [], 0
    while i < len(lines):
        m = AUTHOR_RE.match(lines[i])
        if m:
            j = i + 1  # consume the item's deeper-indented / blank continuation
            while j < len(lines) and (lines[j].strip() == "" or lines[j].startswith("    ")):
                j += 1
            if any(p in m.group(1) for p in PINGBACK):
                i = j
                continue
            out.extend(lines[i:j])
            i = j
            continue
        out.append(lines[i])
        i += 1
    text = _drop_empty_comments_key("\n".join(out))
    return text if text.endswith("\n") else text + "\n"


def fix_text(text):
    m = FENCE_RE.match(text)
    if not m:
        return CAPTION_RE.sub(_convert, text)
    open_f, fm, close_f, body = m.groups()
    return open_f + drop_pingback_comments(fm) + close_f + CAPTION_RE.sub(_convert, body)


BOLD_HEADING_RE = re.compile(r"^[ \t]*<(b|strong)>(.+?)</\1>[ \t]*$", re.M)
_PURE_LINK = re.compile(r"^<a\b.*</a>$", re.S | re.I)


def _bold_to_heading(m):
    inner = m.group(2).strip()
    if _PURE_LINK.match(inner):              # a lone bold link is ambiguous — leave it
        return m.group(0)
    inner = re.sub(r"</?span[^>]*>", "", inner).strip()   # drop presentational spans
    return f"## {inner}" if inner else m.group(0)


def convert_bold_headings(body):
    """Convert any line that is *entirely* one ``<b>``/``<strong>`` element into an
    ``## `` heading. In these WordPress-era essays a standalone bold line is a
    section title; mid-sentence bold and lone bold links are left alone. Body only.
    """
    return BOLD_HEADING_RE.sub(_bold_to_heading, body)


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
            caps = len(CAPTION_RE.findall(text))
            pings = sum(1 for ln in text.split("\n")
                        if AUTHOR_RE.match(ln) and any(p in ln for p in PINGBACK))
            bits = []
            if caps:
                bits.append(f"{caps} caption(s)")
            if pings:
                bits.append(f"{pings} pingback(s)")
            print(("WOULD FIX" if args.check_only else "FIXED"), f, "—", ", ".join(bits))
            if not args.check_only:
                open(f, "w", encoding="utf-8").write(new)
    if not stale:
        print("No WordPress residue found.")
    if args.check_only and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
