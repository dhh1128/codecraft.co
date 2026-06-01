#!/usr/bin/env python3
"""Assign permanent item-ids and write tags into essay frontmatter.

Item-id format: ``CC-YYMMOO`` (e.g. ``CC-120826``) where YY/MM come from the
essay's original publication ``date`` and OO is a 2-digit ordinal within that
month, ordered by (date, slug) for determinism. No category segment — tags
carry topic, and tags are not part of the id (so they can be revised freely
without disturbing ids). Coexists with the ../papers archive under the shared
``CC`` namespace: papers always carry a 3-letter middle segment, essays never
do.

Tags and series come from ``scripts/tags.yml`` (controlled vocabulary, 1+ per
essay). Frontmatter is edited surgically: only ``item_id``/``tags``/``series``
lines are inserted or replaced, after the ``slug:`` line; everything else
(comments, redirect_from, ...) is left byte-for-byte intact.

Idempotent. ``--check-only`` reports drift without writing (exit 1 if stale).
"""
import argparse
import datetime
import glob
import os
import re
import sys

import yaml

META_FILES = {"README.md", "AGENTS.md", "CLAUDE.md", "ROADMAP.md", "index.md"}
MANAGED = ("item_id:", "tags:", "series:")
HERE = os.path.dirname(os.path.abspath(__file__))


def essay_files():
    return [f for f in sorted(glob.glob("*.md")) if f not in META_FILES]


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("no parseable frontmatter")
    return yaml.safe_load(m.group(1)) or {}


def compute_ids(files):
    """Return {file: CC-YYMMOO}, ordinal within (year, month) by (date, slug)."""
    rows = []
    for f in files:
        fm = frontmatter(open(f, encoding="utf-8").read())
        d = fm.get("date")
        if not isinstance(d, datetime.date):
            raise ValueError(f"{f}: missing/!date frontmatter date: {d!r}")
        rows.append((d, fm.get("slug", f[:-3]), f))
    ids = {}
    by_month = {}
    for d, slug, f in rows:
        by_month.setdefault((d.year, d.month), []).append((d, slug, f))
    for key, lst in by_month.items():
        for i, (d, slug, f) in enumerate(sorted(lst), start=1):
            ids[f] = f"CC-{d:%y%m}{i:02d}"
    return ids


def render_managed(item_id, tags, series):
    lines = [f"item_id: {item_id}", "tags: [" + ", ".join(tags) + "]"]
    if series:
        lines.append(f'series: "{series}"')
    return lines


def apply_to_text(text, item_id, tags, series):
    lines = text.split("\n")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    fm = [l for l in lines[1:end] if not l.startswith(MANAGED)]
    insert = next((i + 1 for i, l in enumerate(fm) if l.startswith("slug:")), len(fm))
    fm = fm[:insert] + render_managed(item_id, tags, series) + fm[insert:]
    return "\n".join([lines[0]] + fm + lines[end:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()

    tags_path = os.path.join(HERE, "tags.yml")
    tagmap = yaml.safe_load(open(tags_path, encoding="utf-8"))

    files = essay_files()
    ids = compute_ids(files)

    # ids must be unique
    seen = {}
    for f, i in ids.items():
        if i in seen:
            sys.exit(f"DUPLICATE id {i}: {seen[i]} and {f}")
        seen[i] = f

    stale = 0
    for f in files:
        slug = f[:-3]
        entry = tagmap.get(slug)
        if not entry or not entry.get("tags"):
            sys.exit(f"{f}: no tags in tags.yml")
        text = open(f, encoding="utf-8").read()
        new = apply_to_text(text, ids[f], entry["tags"], entry.get("series"))
        if new != text:
            stale += 1
            print(("WOULD SET" if args.check_only else "SET"), f, "->", ids[f],
                  entry["tags"], entry.get("series") or "")
            if not args.check_only:
                open(f, "w", encoding="utf-8").write(new)
    print(f"\n{len(files)} essays, {len(set(ids.values()))} unique ids; {stale} changed.")
    if args.check_only and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
