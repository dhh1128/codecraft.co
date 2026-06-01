#!/usr/bin/env python3
"""Repair YAML frontmatter glitches left over from the WordPress export.

Two deterministic, mechanical fixes, applied only within the frontmatter block:

1. Mangled opening fence: a first line that is not ``---`` but is immediately
   followed by a ``title:`` line (the export turned ``---`` into an em-dash
   entity on a couple of files). The first line is restored to ``---``.

2. Unquoted scalars that break YAML: ``title:`` and comment ``author:`` values
   that contain ``": "`` or begin with a quote character. They are wrapped in
   double quotes, or single quotes when the value itself contains a double
   quote.

Idempotent. Use ``--check-only`` to report what would change without writing
(exit 1 if anything is stale). This is a maintenance tool, not part of the
one-shot ``tools/`` migration set.
"""
import argparse
import glob
import re
import sys

META_FILES = {"README.md", "AGENTS.md", "CLAUDE.md", "ROADMAP.md", "index.md"}
SCALAR_RE = re.compile(r"^(\s*(?:-\s+)?)(title|author):\s(.*)$")
MANGLED_FENCE_RE = re.compile(r"^\s*&mdash;\s*-\s*$")  # export turned '---' into this


def needs_quote(v):
    v = v.rstrip()
    if not v:
        return False
    if len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'")):
        return False  # already quoted
    if ": " in v or v.endswith(":") or v[0] in "\"'[]{}>|*&!%@`#":
        return True
    return False


def quote(v):
    v = v.rstrip()
    if '"' in v:
        return "'" + v.replace("'", "''") + "'"
    return '"' + v + '"'


def fix_text(text):
    lines = text.split("\n")
    if not lines:
        return text, []
    changes = []

    # Fix 1: mangled opening fence.
    if lines[0].strip() != "---" and len(lines) > 1 and lines[1].startswith("title:"):
        changes.append(f"open fence: {lines[0]!r} -> '---'")
        lines[0] = "---"

    if lines[0].strip() != "---":
        return "\n".join(lines), changes  # no frontmatter to scan

    # Fix 2: quote unsafe scalars and restore a mangled closing fence, within
    # the frontmatter block only.
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            break  # end of frontmatter
        if MANGLED_FENCE_RE.match(lines[i]):
            changes.append(f"close fence: {lines[i]!r} -> '---'")
            lines[i] = "---"
            break
        m = SCALAR_RE.match(lines[i])
        if not m:
            continue
        prefix, key, val = m.group(1), m.group(2), m.group(3)
        if needs_quote(val):
            newline = f"{prefix}{key}: {quote(val)}"
            changes.append(f"{key}: {val[:50]!r} -> quoted")
            lines[i] = newline
    return "\n".join(lines), changes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", help="files to fix (default: all root essays)")
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()

    files = args.files or [f for f in sorted(glob.glob("*.md")) if f not in META_FILES]
    stale = 0
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        new, changes = fix_text(text)
        if new != text:
            stale += 1
            tag = "WOULD FIX" if args.check_only else "FIXED"
            print(f"{tag} {f}:")
            for c in changes:
                print(f"    {c}")
            if not args.check_only:
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(new)
    if not stale:
        print("All frontmatter parses cleanly.")
    if args.check_only and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
