#!/usr/bin/env python3
"""Execute the image triage manifest — localize owned images.

Reads ``assets/image-triage.yml`` and, for every reference marked
``disposition: own``, localizes it: the essay's ``<img src>`` (or image
``<a href>``) is rewritten from its external URL to ``assets/<file>``. If a
local copy already exists (``local_match``), it's a pure reference rewrite; if
not, the file is downloaded into ``assets/`` first.

Only the ``own`` disposition is handled here. ``generate`` / ``redraw`` / ``drop``
are deliberately left for later passes (they need art generation or prose
reflow, not a mechanical rewrite). Rewrites are exact-string and idempotent, so
prose is never touched and re-running is safe.

After applying, re-run ``scripts/inventory_images.py`` so the manifest reflects
the now-local references.

Usage:
    python scripts/apply_image_triage.py                  # dry run (report only)
    python scripts/apply_image_triage.py --apply          # rewrite essays
    python scripts/apply_image_triage.py --apply --host codecraft.co
    python scripts/apply_image_triage.py --check-only      # exit 1 if own refs remain unlocalized
"""
import argparse
import os
import sys
import urllib.request

import yaml

META = {"README.md", "AGENTS.md", "CLAUDE.md", "ROADMAP.md", "index.md"}
UA = "Mozilla/5.0 (codecraft.co image localizer)"


def _default_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _manifest_path(root):
    return os.path.join(root, "assets", "image-triage.yml")


def load_rows(root):
    data = yaml.safe_load(open(_manifest_path(root), encoding="utf-8")) or {}
    return data.get("images", [])


def _fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
        return resp.read()


def _basename(src_or_name):
    return os.path.basename(src_or_name.split("?")[0].split("#")[0])


def localize(root, apply=False, fetch=None, hosts=None):
    """Localize every ``own`` image. Returns a list of action records.

    Each action: ``{essay, src, target, status}`` where status is one of
    ``rewritten`` | ``downloaded`` | ``unchanged`` | ``needs-decision`` | ``error``.
    ``hosts``: optional iterable of substrings; only rows whose src contains one
    are processed (e.g. ``["codecraft.co"]``).
    """
    root = str(root)
    fetch = fetch or _fetch
    actions = []
    # cache file contents so repeated essays are read/written once
    files = {}

    def _read(name):
        if name not in files:
            files[name] = open(os.path.join(root, name), encoding="utf-8").read()
        return files[name]

    for row in load_rows(root):
        if row.get("disposition") != "own":
            continue
        src = row["src"]
        if hosts and not any(h in src for h in hosts):
            continue
        essay = row["essay"]
        if essay in META or not os.path.isfile(os.path.join(root, essay)):
            continue

        local_match = row.get("local_match") or ""
        assets_dir = os.path.join(root, "assets")

        # Determine the local target filename.
        target_name = local_match or _basename(src)
        target_path = os.path.join(assets_dir, target_name)
        target_ref = f"assets/{target_name}"

        # Already canonical (src == assets/<file>): nothing to do.
        if src == target_ref:
            actions.append({"essay": essay, "src": src, "target": target_ref,
                           "status": "unchanged"})
            continue

        status = None
        if not os.path.isfile(target_path):
            # need to download
            if not src.lower().startswith(("http://", "https://")):
                actions.append({"essay": essay, "src": src, "target": target_ref,
                               "status": "needs-decision"})
                continue
            try:
                data = fetch(src)
            except Exception as e:  # noqa: BLE001
                actions.append({"essay": essay, "src": src, "target": target_ref,
                               "status": "error", "detail": str(e)})
                continue
            if apply:
                os.makedirs(assets_dir, exist_ok=True)
                with open(target_path, "wb") as fh:
                    fh.write(data)
            status = "downloaded"

        body = _read(essay)
        if src in body:
            files[essay] = body.replace(src, target_ref)
            status = status or "rewritten"
        elif target_ref in body:
            status = status or "unchanged"
        else:
            # neither the original src nor the target ref is in the essay
            status = status or "unchanged"

        actions.append({"essay": essay, "src": src, "target": target_ref,
                       "status": status})

    if apply:
        for name, content in files.items():
            with open(os.path.join(root, name), "w", encoding="utf-8") as fh:
                fh.write(content)

    return actions


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--host", action="append", dest="hosts",
                    help="only process rows whose src contains this substring (repeatable)")
    ap.add_argument("--check-only", action="store_true",
                    help="exit 1 if any 'own' image is still unlocalized")
    args = ap.parse_args(argv)

    root = _default_root()
    actions = localize(root, apply=args.apply, hosts=args.hosts)

    from collections import Counter
    counts = Counter(a["status"] for a in actions)
    verb = "Localized" if args.apply else "Would localize"
    rewritten = counts.get("rewritten", 0) + counts.get("downloaded", 0)
    print(f"{verb} {rewritten} owned image(s): {dict(counts)}")
    for a in actions:
        if a["status"] in ("needs-decision", "error"):
            print(f"  ! {a['status']}: {a['essay']}  {a['src']}  {a.get('detail','')}")

    if args.check_only:
        pending = [a for a in actions if a["status"] in ("rewritten", "downloaded",
                                                         "needs-decision", "error")]
        if pending:
            print(f"{len(pending)} owned image(s) not yet localized.")
            sys.exit(1)


if __name__ == "__main__":
    main()
