#!/usr/bin/env python3
"""Image-integrity gate for the essay corpus.

Scans every ``<img>`` tag in the published essays and reports each problem as a
violation record, so the M2 goal — *own 100% of images, zero external
dependencies, alt-text everywhere* — is enforceable and gives a precise
worklist instead of being spot-checked by eye.

Problems detected (one image may have several):

- ``external``      — ``src`` is an http(s) URL on any host. Not owned; can
                      break at any time, and is blocked as mixed content once
                      the site is served over HTTPS. Must be localized.
- ``malformed``     — a broken/typo URL (e.g. ``staticfliccom``).
- ``missing-local`` — ``src`` points into ``assets/`` but the file is absent.
- ``no-alt``        — the ``<img>`` has no (or empty) ``alt`` text.

Companion to ``inventory_images.py``: inventory *catalogs* every reference into
the triage manifest; this *validates* them. Use the manifest's ``disposition``
column to drive fixes (own / generate / redraw / drop), then re-run this to
confirm the corpus is clean.

Usage:
    python scripts/check_images.py              # full grouped report
    python scripts/check_images.py --check-only # exit 1 if any violations (CI)
    python scripts/check_images.py --problem external
    python scripts/check_images.py --json
"""
import argparse
import json
import os
import re
import sys

# Names that look like essays but are repo meta, not content.
META = {"README.md", "AGENTS.md", "CLAUDE.md", "ROADMAP.md", "index.md"}
# Typo/legacy hosts that never resolve.
MALFORMED_MARKERS = ("staticfliccom", "static.flickr.com")

IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
SRC_RE = re.compile(r'\bsrc="([^"]*)"', re.I)
ALT_RE = re.compile(r'\balt="([^"]*)"', re.I)


def _default_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _classify(src):
    """Return the structural problem with this src, or None if it looks ownable."""
    if any(m in src for m in MALFORMED_MARKERS):
        return "malformed"
    if re.match(r"https?://", src, re.I):
        return "external"
    if re.match(r"(\.\.?/)*assets/", src):
        return "local"           # resolved against the filesystem by the caller
    if "wp-content/uploads" in src:
        return "external"        # an un-localized WordPress upload (URL or path)
    return "malformed"           # non-http, non-asset, unrecognized shape


def _resolve_local(root, essay_name, src):
    """True if a local ``assets/`` src resolves to a real file."""
    rel = src.split("?")[0].split("#")[0].lstrip("/")
    return os.path.isfile(os.path.join(root, rel))


def check(root=None):
    """Scan the corpus under ``root`` and return a list of violation records.

    Each record: ``{essay, line, src, alt, problem}``.
    """
    root = str(root) if root is not None else _default_root()
    violations = []
    for name in sorted(os.listdir(root)):
        if not name.endswith(".md") or name in META:
            continue
        path = os.path.join(root, name)
        if not os.path.isfile(path):
            continue
        text = open(path, encoding="utf-8").read()
        for m in IMG_RE.finditer(text):
            tag = m.group(0)
            line = text.count("\n", 0, m.start()) + 1
            src_m = SRC_RE.search(tag)
            src = src_m.group(1) if src_m else ""
            alt_m = ALT_RE.search(tag)
            alt = alt_m.group(1) if alt_m else ""

            problems = []
            if not src:
                problems.append("malformed")
            else:
                kind = _classify(src)
                if kind == "local":
                    if not _resolve_local(root, name, src):
                        problems.append("missing-local")
                else:
                    problems.append(kind)  # external | malformed
            if not alt.strip():
                problems.append("no-alt")

            for problem in problems:
                violations.append({"essay": name, "line": line, "src": src,
                                   "alt": alt, "problem": problem})
    return violations


# ---- reporting -----------------------------------------------------------------

def _report(violations):
    from collections import Counter, defaultdict
    by_problem = Counter(v["problem"] for v in violations)
    essays = {v["essay"] for v in violations}
    order = ["external", "malformed", "missing-local", "no-alt"]

    lines = [f"{len(violations)} image issue(s) across {len(essays)} essay(s):"]
    for problem in order:
        n = by_problem.get(problem, 0)
        if n:
            lines.append(f"  {problem:<14} {n}")
    for problem in order:
        items = [v for v in violations if v["problem"] == problem]
        if not items:
            continue
        lines.append(f"\n## {problem} ({len(items)})")
        grouped = defaultdict(list)
        for v in items:
            grouped[v["essay"]].append(v)
        for essay in sorted(grouped):
            for v in grouped[essay]:
                lines.append(f"  {essay}:{v['line']}  {v['src'][:90]}")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check-only", action="store_true",
                    help="exit 1 if any violations (for CI)")
    ap.add_argument("--problem", choices=["external", "malformed", "missing-local", "no-alt"],
                    help="only report this problem")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args(argv)

    violations = check()
    if args.problem:
        violations = [v for v in violations if v["problem"] == args.problem]

    if args.json:
        print(json.dumps(violations, indent=2))
    else:
        print(_report(violations) if violations else "No image issues found.")

    if args.check_only and violations:
        sys.exit(1)


if __name__ == "__main__":
    main()
