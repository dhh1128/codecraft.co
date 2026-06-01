#!/usr/bin/env python3
"""Recover broken Wikimedia Commons images.

Many essays embed Wikimedia Commons images via legacy ``upload.wikimedia.org``
*thumbnail hotlink* URLs that now return HTTP 400 — Wikimedia stopped serving
those old direct-thumb links, but the underlying Commons files are still there
and (almost always) freely licensed. This tool, for each such ``<img>``:

1. resolves the Commons file via the API and checks it still exists;
2. reads its license; if the license permits **at least non-commercial
   publication** (PD / CC0 / CC-BY[-SA] / CC-BY-NC / GFDL / …), proceeds;
3. downloads a local copy (at the originally-displayed width) into ``assets/``;
4. rewrites the essay ``<img src>`` to the local file;
5. records full provenance/rights in ``assets/CREDITS.yml`` — including a
   ``book_safe`` flag (false for NC, which blocks the eventual commercial book).

Files that are gone, or whose license can't be confirmed, are left untouched and
reported for a human decision.

Usage:
    python scripts/recover_wikimedia.py            # dry run: resolve + report
    python scripts/recover_wikimedia.py --apply    # download, localize, credit
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request

import yaml

META = {"README.md", "AGENTS.md", "CLAUDE.md", "ROADMAP.md", "index.md"}
API = "https://commons.wikimedia.org/w/api.php"
UA = "codecraft.co-image-recovery/1.0 (daniel@provenant.net)"
IMG_RE = re.compile(r'<img\b[^>]*\bsrc="([^"]*upload\.wikimedia\.org[^"]*)"[^>]*>', re.I)


def _default_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---- pure helpers --------------------------------------------------------------

def commons_filename(url):
    path = urllib.parse.urlparse(url).path
    if "/thumb/" in path:
        # .../thumb/a/ab/<FILENAME>/<width>px-<rest>
        filename = path.split("/thumb/", 1)[1].split("/")[2]
    else:
        filename = path.rsplit("/", 1)[-1]
    return urllib.parse.unquote(filename)


def commons_title(url):
    return "File:" + commons_filename(url)


def requested_width(url, default=640):
    m = re.search(r"/(\d+)px-", url)
    return int(m.group(1)) if m else default


def _text(em, key):
    return re.sub(r"<[^>]+>", "", str(em.get(key, {}).get("value", ""))).strip()


def classify_license(em):
    """Decide whether an extmetadata block permits non-commercial publication.

    Commons sometimes leaves the machine-readable ``License`` field empty and
    records the license only in ``LicenseShortName`` (notably for GFDL), so we
    fall back to the short name.
    """
    code = _text(em, "License").lower()           # 'pd' | 'cc0' | 'cc-by-sa-4.0' | ...
    short = _text(em, "LicenseShortName")
    short_l = short.lower()

    is_pd = code.startswith(("pd", "cc0")) or "public domain" in short_l
    is_cc = code.startswith("cc-by") or code == "cc" or "cc-by" in short_l or \
        short_l.startswith("cc ")
    is_gfdl = code.startswith("gfdl") or "gfdl" in short_l or \
        "gnu free documentation" in short_l
    is_fal = code.startswith("fal") or "free art" in short_l
    allowed = is_pd or is_cc or is_gfdl or is_fal

    nc = "nc" in code or bool(re.search(r"(^|[ -])nc([ -]|$)", short_l))
    # GFDL is free but its full-license-text requirement makes it impractical for
    # the commercial book; treat it as publishable-but-not-book-safe.
    book_safe = allowed and not nc and not is_gfdl
    return {
        "license": short or code or "unknown",
        "code": code,
        "allowed": allowed,
        "book_safe": book_safe,
        "artist": _text(em, "Artist"),
        "credit": _text(em, "Credit"),
        "license_url": _text(em, "LicenseUrl"),
        "attribution_required": _text(em, "AttributionRequired").lower() == "true",
    }


def asset_name(filename, thumburl):
    base = filename.rsplit(".", 1)[0]
    slug = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")
    ext = os.path.splitext(urllib.parse.urlparse(thumburl).path)[1].lstrip(".").lower() or "jpg"
    return f"{slug}.{ext}"


# ---- network (injectable) ------------------------------------------------------

def _query_commons(title, width):
    params = urllib.parse.urlencode({
        "action": "query", "format": "json", "titles": title,
        "prop": "imageinfo", "iiprop": "url|extmetadata", "iiurlwidth": width})
    req = urllib.request.Request(f"{API}?{params}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    page = next(iter(data["query"]["pages"].values()))
    if "missing" in page or "imageinfo" not in page:
        return {"missing": True}
    ii = page["imageinfo"][0]
    return {"missing": False, "thumburl": ii.get("thumburl") or ii.get("url"),
            "descriptionurl": ii.get("descriptionurl", ""),
            "extmetadata": ii.get("extmetadata", {})}


def _download(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


# ---- corpus + credits ----------------------------------------------------------

def wikimedia_refs(root):
    refs = []
    for name in sorted(os.listdir(root)):
        if not name.endswith(".md") or name in META:
            continue
        path = os.path.join(root, name)
        if not os.path.isfile(path):
            continue
        text = open(path, encoding="utf-8").read()
        for m in IMG_RE.finditer(text):
            refs.append((name, m.group(1)))
    return refs


def _credits_path(root):
    return os.path.join(root, "assets", "CREDITS.yml")


def load_credits(root):
    p = _credits_path(root)
    if os.path.exists(p):
        return yaml.safe_load(open(p, encoding="utf-8")) or {"images": {}}
    return {"images": {}}


CREDITS_HEADER = (
    "# Provenance & rights for owned images in assets/.\n"
    "# Wikimedia entries written by scripts/recover_wikimedia.py.\n"
    "# book_safe is false for non-commercial (NC) licenses (blocks the KDP book).\n"
)


def _unique_name(root, name, reserved):
    base, ext = os.path.splitext(name)
    cand, i = name, 1
    while os.path.exists(os.path.join(root, "assets", cand)) or cand in reserved:
        cand = f"{base}-{i}{ext}"
        i += 1
    reserved.add(cand)
    return cand


def recover(root, apply=False, query=None, download=None, today=""):
    root = str(root)
    query = query or _query_commons
    download = download or _download
    credits = load_credits(root)
    credits.setdefault("images", {})
    actions = []
    files = {}
    reserved = set()

    def _read(name):
        if name not in files:
            files[name] = open(os.path.join(root, name), encoding="utf-8").read()
        return files[name]

    for essay, src in wikimedia_refs(root):
        title = commons_title(src)
        info = query(title, requested_width(src))
        if info.get("missing"):
            actions.append({"essay": essay, "src": src, "status": "missing"})
            continue
        lic = classify_license(info.get("extmetadata", {}))
        if not lic["allowed"]:
            actions.append({"essay": essay, "src": src, "status": "license-blocked",
                           "license": lic["license"]})
            continue

        name = _unique_name(root, asset_name(commons_filename(src), info["thumburl"]),
                            reserved)
        target_ref = f"assets/{name}"
        if apply:
            data = download(info["thumburl"])
            os.makedirs(os.path.join(root, "assets"), exist_ok=True)
            with open(os.path.join(root, "assets", name), "wb") as fh:
                fh.write(data)

        body = _read(essay)
        files[essay] = body.replace(src, target_ref)

        entry = credits["images"].get(name, {})
        entry.update({
            "source": info.get("descriptionurl", ""),
            "file_url": info["thumburl"],
            "license": lic["license"],
            "license_code": lic["code"],
            "license_url": lic["license_url"],
            "artist": lic["artist"],
            "credit": lic["credit"],
            "attribution_required": lic["attribution_required"],
            "book_safe": lic["book_safe"],
            "retrieved": entry.get("retrieved", today),
            "replaces": src,
        })
        used = set(entry.get("used_in", []))
        used.add(essay)
        entry["used_in"] = sorted(used)
        credits["images"][name] = entry

        actions.append({"essay": essay, "src": src, "status": "recovered",
                       "target": target_ref, "license": lic["license"],
                       "book_safe": lic["book_safe"]})

    if apply:
        for name, content in files.items():
            with open(os.path.join(root, name), "w", encoding="utf-8") as fh:
                fh.write(content)
        with open(_credits_path(root), "w", encoding="utf-8") as fh:
            fh.write(CREDITS_HEADER + yaml.safe_dump(credits, sort_keys=False,
                                                     allow_unicode=True, width=4096))

    return actions, credits


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="download + localize + credit")
    ap.add_argument("--today", default="", help="retrieval date to stamp (YYYY-MM-DD)")
    args = ap.parse_args(argv)

    actions, _ = recover(_default_root(), apply=args.apply, today=args.today)
    from collections import Counter
    counts = Counter(a["status"] for a in actions)
    verb = "Recovered" if args.apply else "Would recover"
    print(f"{verb}: {dict(counts)}\n")
    for a in actions:
        if a["status"] == "recovered":
            flag = "" if a.get("book_safe") else "  ⚠ NOT book-safe"
            print(f"  ✓ {a['essay']:<42} {a['license']}{flag}")
        else:
            print(f"  ! {a['status']:<16} {a['essay']:<42} {a['src'][:60]}")


if __name__ == "__main__":
    main()
