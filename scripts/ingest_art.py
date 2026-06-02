#!/usr/bin/env python3
"""Ingest AI-generated art into the site, end-to-end.

Given a mapping ``{downloaded_file: canonical_filename}`` (the canonical names
come from assets/art-prompts.yml), for each image:

1. copy the download into ``assets/<canonical>``, run the normalize pass
   (transparent background, downscaled to 1024px, optimized PNG) and set 0644
   perms — Windows/WSL2 downloads arrive executable (+x), which we strip;
2. rewrite the essay's ``<img src>`` from the old Flickr URL to
   ``assets/<canonical>``, and strip the now-false "Photo credit: … (Flickr)"
   from that figure's caption;
3. record provenance in ``assets/CREDITS.yml`` (AI-generated, openart.ai, the
   prompt, owned/full rights);
4. mark the ``art-prompts.yml`` entry ``status: done`` and delete the download
   (so anything left in the downloads folder is unprocessed).

Usage:
    python scripts/ingest_art.py rose.png=naming-rose-tag.png stones.png=balance-stacked-stones.png
    python scripts/ingest_art.py --downloads ~/winhome/Downloads <pairs...>
"""
import argparse
import os
import re
import shutil
import sys

import yaml

import normalize_art

CREDITS_HEADER = (
    "# Provenance & rights for owned images in assets/.\n"
    "# Wikimedia entries written by scripts/recover_wikimedia.py;\n"
    "# AI-generated entries by scripts/ingest_art.py.\n"
    "# book_safe is false for non-commercial licenses (blocks the KDP book).\n"
)
PROMPTS_HEADER = (
    "# AI image-generation prompts — one per unowned Flickr image to replace.\n"
    "# House style: docs/art-style.md. Paste `prompt` into openart.ai with the\n"
    "# negative prompt from the style doc; save the result to assets/<filename>,\n"
    "# then run scripts/normalize_art.py to knock the background out (transparent).\n"
    "# `review: true` = concept inferred from the title; double-check it fits.\n"
)


def _default_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rewrite_src(text, old_src, new_ref):
    return text.replace(old_src, new_ref)


def strip_img_dimensions(text, ref):
    """Drop the stale width/height attrs from the <img> now pointing at ``ref``
    (they came from the old Flickr thumbnail; our art is 1024px and responsive)."""
    def _clean(m):
        return re.sub(r'\s+(?:width|height)="[^"]*"', "", m.group(0))
    return re.sub(rf'<img[^>]*\bsrc="{re.escape(ref)}"[^>]*>', _clean, text)


def strip_flickr_credit(text, img_src):
    """Remove the 'Photo/Image credit: … (Flickr)' tail from the figcaption that
    follows ``img_src``; drop the figcaption entirely if nothing else remains."""
    m = re.search(re.escape(f'src="{img_src}"'), text)
    if not m:
        return text
    fc = re.search(r"<figcaption>(.*?)</figcaption>", text[m.end():], re.S)
    if not fc:
        return text
    start, end = m.end() + fc.start(), m.end() + fc.end()
    inner = re.sub(r"\s*(?:Photo|Image)\s+credit\b.*$", "", fc.group(1),
                   flags=re.I | re.S).strip()
    replacement = f"<figcaption>{inner}</figcaption>" if inner else ""
    return text[:start] + replacement + text[end:]


def _load(path, default):
    if os.path.exists(path):
        return yaml.safe_load(open(path, encoding="utf-8")) or default
    return default


def ingest(root, mapping, downloads_dir, today=""):
    root = str(root)
    prompts_path = os.path.join(root, "assets", "art-prompts.yml")
    credits_path = os.path.join(root, "assets", "CREDITS.yml")
    prompts = _load(prompts_path, {"images": []})
    by_name = {e["filename"]: e for e in prompts.get("images", [])}
    credits = _load(credits_path, {"images": {}})
    credits.setdefault("images", {})

    essays = {}   # essay name -> text (edited cumulatively, written once)
    actions = []

    def _essay(name):
        if name not in essays:
            essays[name] = open(os.path.join(root, name), encoding="utf-8").read()
        return essays[name]

    for dl_name, canonical in mapping.items():
        entry = by_name.get(canonical)
        if entry is None:
            actions.append({"download": dl_name, "status": "no-prompt-entry"})
            continue
        src_path = os.path.join(downloads_dir, dl_name)
        if not os.path.isfile(src_path):
            actions.append({"download": dl_name, "status": "missing-download"})
            continue

        # 1. copy + normalize + strip +x
        dest = os.path.join(root, "assets", canonical)
        shutil.copyfile(src_path, dest)
        normalize_art.process_file(dest)          # transparent, 1024px, optimized
        os.chmod(dest, 0o644)

        # 2. rewrite essay <img src> + strip the false credit
        essay = entry["essay"]
        old_src = entry["replaces"]
        text = _essay(essay)
        text = strip_flickr_credit(text, old_src)
        text = rewrite_src(text, old_src, f"assets/{canonical}")
        text = strip_img_dimensions(text, f"assets/{canonical}")
        essays[essay] = text

        # 3. CREDITS
        cred = credits["images"].get(canonical, {})
        cred.update({
            "origin": "AI-generated",
            "model": "openart.ai",
            "prompt": entry.get("prompt", ""),
            "license": "Owned — AI-generated, full rights",
            "attribution_required": False,
            "book_safe": True,
            "retrieved": cred.get("retrieved", today),
            "replaces": old_src,
        })
        used = set(cred.get("used_in", []))
        used.add(essay)
        cred["used_in"] = sorted(used)
        credits["images"][canonical] = cred

        # 4. mark done
        entry["status"] = "done"
        actions.append({"download": dl_name, "canonical": canonical,
                        "essay": essay, "status": "ingested"})

    # write everything back
    for name, text in essays.items():
        with open(os.path.join(root, name), "w", encoding="utf-8") as fh:
            fh.write(text)
    with open(prompts_path, "w", encoding="utf-8") as fh:
        fh.write(PROMPTS_HEADER + yaml.safe_dump(prompts, sort_keys=False,
                                                 allow_unicode=True, width=1000))
    with open(credits_path, "w", encoding="utf-8") as fh:
        fh.write(CREDITS_HEADER + yaml.safe_dump(credits, sort_keys=False,
                                                 allow_unicode=True, width=4096))
    # delete the processed downloads last (so a failure above leaves them in place)
    for a in actions:
        if a["status"] == "ingested":
            os.remove(os.path.join(downloads_dir, a["download"]))
    return actions


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pairs", nargs="+", help="download=canonical mappings")
    ap.add_argument("--downloads", default=os.path.expanduser("~/winhome/Downloads"),
                    help="folder holding the downloaded images")
    ap.add_argument("--today", default="", help="provenance date (YYYY-MM-DD)")
    args = ap.parse_args(argv)

    mapping = {}
    for p in args.pairs:
        if "=" not in p:
            ap.error(f"bad pair {p!r} (want download.png=canonical.png)")
        dl, canon = p.split("=", 1)
        mapping[dl] = canon

    actions = ingest(_default_root(), mapping, args.downloads, today=args.today)
    for a in actions:
        if a["status"] == "ingested":
            print(f"  ✓ {a['download']} → assets/{a['canonical']}  ({a['essay']})")
        else:
            print(f"  ! {a['status']}: {a['download']}")


if __name__ == "__main__":
    main()
