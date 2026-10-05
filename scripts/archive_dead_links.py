#!/usr/bin/env python3
"""Replace dead external links with Wayback Machine snapshots.

Many essays cite pages that have since vanished. Per the "verify each source
resolves or is archived" goal, a dead citation is rewritten to the Internet
Archive copy closest to the essay's publication date, so the reader sees the
page as it was when the essay cited it. The original URL stays embedded in the
archive URL (``https://web.archive.org/web/<timestamp>/<original>``).

Which links are dead comes from a lychee JSON report (lychee is already the
link checker for CI, see lychee.toml), plus any link on a host known to be gone
for good (DEAD_HOSTS) — those often redirect to a 200 parking or announcement
page, so a checker counts them as alive.

Not rewritten, and reported for a human decision instead:

- links that failed with a bot-blocking status (401/403/429/999), since the
  page may well be alive — unless the host is in DEAD_HOSTS;
- links with no 200 snapshot in the archive (often a typo in the original URL).

Lookups are cached (``--cache``, saved after every lookup) because the
archive's CDX API is slow and rate-limits hard; a rerun, or a run resumed after
an interruption, only queries what it has not seen.

Usage:
    lychee --format json --output /tmp/lychee.json './**/*.md'
    python scripts/archive_dead_links.py --report /tmp/lychee.json          # dry run
    python scripts/archive_dead_links.py --report /tmp/lychee.json --apply  # rewrite
"""
import argparse
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

import yaml

META = {"README.md", "AGENTS.md", "CLAUDE.md", "ROADMAP.md", "index.md"}
CDX = "https://web.archive.org/cdx/search/cdx"
UA = "codecraft.co-link-archiver/1.0 (daniel@provenant.net)"

# Hosts that are gone for good, whatever a link checker says about them.
DEAD_HOSTS = {
    "plus.google.com",          # Google+ shut down 2019; redirects to a blog post
    "sethgodin.typepad.com",    # Typepad blog retired; redirects to a parking page
    "code.google.com",          # Google Code shut down 2016
}

# Failures that may just mean "this host refuses bots".
AMBIGUOUS_STATUS = {401, 403, 429, 999}

ARCHIVED_RE = re.compile(r"^https?://web\.archive\.org/web/\d+")


def _default_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---- pure helpers --------------------------------------------------------------

def host(url):
    return (urllib.parse.urlparse(url).hostname or "").lower()


def is_archived(url):
    return bool(ARCHIVED_RE.match(url))


def archive_url(timestamp, url):
    return f"https://web.archive.org/web/{timestamp}/{url}"


def essay_timestamp(text):
    """The essay's frontmatter date as a CDX timestamp (YYYYMMDD), or ''."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ""
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return ""
    d = str(fm.get("date", ""))
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", d)
    return "".join(m.groups()) if m else ""


def classify(url, status_code):
    """'dead' (archive it), 'ambiguous' (report only), or 'skip'."""
    if is_archived(url) or not url.startswith(("http://", "https://")):
        return "skip"
    if host(url) in DEAD_HOSTS:
        return "dead"
    if status_code in AMBIGUOUS_STATUS:
        return "ambiguous"
    return "dead"


def _url_pattern(url):
    """Match ``url`` (raw or HTML-escaped) as a whole URL not already archived.

    The lookbehind skips occurrences already inside a web.archive.org URL; the
    lookahead stops ``http://x/a`` from matching inside ``http://x/abc``.
    """
    forms = {url}
    if urllib.parse.urlparse(url).path == "/":
        forms.add(url[:-1])          # lychee reports "http://host" as "http://host/"
    forms |= {html.escape(f, quote=False) for f in forms}
    alts = "|".join(re.escape(f) for f in sorted(forms, key=len, reverse=True))
    return re.compile(r"(?<![\w/.])(?:" + alts + r")(?=[\"'\s)<>\]]|$)")


def rewrite(text, url, new_url):
    """Replace every bare occurrence of ``url`` in ``text``; return (text, n)."""
    def _sub(m):
        # keep the source's own escaping of '&'
        return new_url if m.group(0) == html.unescape(m.group(0)) else \
            html.escape(new_url, quote=False)
    return _url_pattern(url).subn(_sub, text)


def dead_links_from_report(report):
    """{essay: {url: status_code_or_None}} from a lychee JSON report."""
    out = {}
    for essay, entries in (report.get("error_map") or {}).items():
        for e in entries:
            code = (e.get("status") or {}).get("code")
            name = os.path.normpath(essay)
            out.setdefault(name, {})[e["url"]] = code
    return out


URL_RE = re.compile(r"https?://[^\s\"'<>)\]]+")


def dead_host_links(text):
    return {u for u in URL_RE.findall(html.unescape(text))
            if host(u) in DEAD_HOSTS and not is_archived(u)}


# ---- network (injectable) ------------------------------------------------------

def _cdx(params, retries=5, pause=4.0):
    """One CDX query; the first row's timestamp, or None if there are no rows."""
    req = urllib.request.Request(f"{CDX}?{urllib.parse.urlencode(params)}",
                                 headers={"User-Agent": UA})
    delay = pause
    for attempt in range(retries):
        time.sleep(pause)
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                rows = json.loads(resp.read().decode("utf-8"))
            return rows[1][0] if len(rows) > 1 else None
        except (OSError, ValueError):
            # 429, 5xx, and the HTML "temporarily offline" page all land here
            if attempt == retries - 1:
                raise
            time.sleep(delay)
            delay *= 2


def _query_cdx(url, timestamp):
    """A 200 snapshot of ``url`` near ``timestamp``: its timestamp, or None.

    The first snapshot on or after the essay's date, else the last one before
    it. (CDX's ``sort=closest`` would be exact, but takes ~a minute per query.)
    """
    base = {"url": url, "output": "json", "filter": "statuscode:200",
            "fl": "timestamp"}
    if not timestamp:
        return _cdx({**base, "limit": "1"})
    return (_cdx({**base, "from": timestamp, "limit": "1"})
            or _cdx({**base, "to": timestamp, "limit": "-1"}))


# ---- corpus --------------------------------------------------------------------

def essay_names(root):
    return sorted(n for n in os.listdir(root)
                  if n.endswith(".md") and n not in META
                  and os.path.isfile(os.path.join(root, n)))


def archive(root, report, apply=False, query=None, cache=None, skip=(),
            on_lookup=None):
    """Plan (and with ``apply``, perform) the rewrites; return the action list."""
    root = str(root)
    query = query or _query_cdx
    cache = {} if cache is None else cache
    dead = dead_links_from_report(report)
    actions = []

    for name in essay_names(root):
        path = os.path.join(root, name)
        text = open(path, encoding="utf-8").read()
        links = dict(dead.get(name, {}))
        for u in dead_host_links(text):
            links.setdefault(u, None)
        if not links:
            continue
        if name in skip:
            actions += [{"essay": name, "url": u, "status": "skipped-file"}
                        for u in sorted(links)]
            continue
        ts = essay_timestamp(text)
        new = text
        for url in sorted(links):
            kind = classify(url, links[url])
            if kind == "skip":
                continue
            if kind == "ambiguous":
                actions.append({"essay": name, "url": url, "status": "ambiguous",
                                "code": links[url]})
                continue
            key = f"{url} @{ts}"
            if key not in cache:
                cache[key] = query(url, ts)
                if on_lookup:
                    on_lookup(cache)
            snap = cache[key]
            if not snap:
                actions.append({"essay": name, "url": url, "status": "no-snapshot"})
                continue
            target = archive_url(snap, url)
            new, n = rewrite(new, url, target)
            actions.append({"essay": name, "url": url, "target": target,
                            "status": "archived" if n else "not-found-in-source"})
        if apply and new != text:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)
    return actions


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True, help="lychee --format json output")
    ap.add_argument("--apply", action="store_true", help="rewrite the essays")
    ap.add_argument("--cache", default=os.path.join(_default_root(), "build",
                                                    "wayback-cache.json"),
                    help="snapshot lookup cache (default: build/wayback-cache.json)")
    ap.add_argument("--skip", action="append", default=[],
                    help="essay file to leave untouched (repeatable)")
    args = ap.parse_args(argv)

    report = json.load(open(args.report, encoding="utf-8"))
    cache = {}
    if os.path.exists(args.cache):
        cache = json.load(open(args.cache, encoding="utf-8"))

    def save(c):
        os.makedirs(os.path.dirname(args.cache), exist_ok=True)
        with open(args.cache, "w", encoding="utf-8") as fh:
            json.dump(c, fh, indent=1, sort_keys=True)

    actions = archive(_default_root(), report, apply=args.apply, cache=cache,
                      skip=set(args.skip), on_lookup=save)

    from collections import Counter
    for a in actions:
        if a["status"] != "archived":
            extra = f" ({a['code']})" if a.get("code") else ""
            print(f"{a['status']:<20} {a['essay']}: {a['url']}{extra}")
    print(dict(Counter(a["status"] for a in actions)))
    if not args.apply:
        print("dry run; pass --apply to rewrite")
    return 0


if __name__ == "__main__":
    sys.exit(main())
