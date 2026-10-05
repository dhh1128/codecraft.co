"""Prover test for scripts/archive_dead_links.py.

Rewrites dead external links (from a lychee JSON report, plus hosts known to be
gone) to the Wayback Machine snapshot closest to the essay's date. The CDX
lookup is injected so the logic is tested without the network.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import archive_dead_links as adl  # noqa: E402

ESSAY = """---
title: Example
date: 2013-03-08
---

See <a href="http://dead.example/page">this</a> and
<a href="http://dead.example/page2">that</a>, plus
<a href="http://www.example.com/q?a=1&amp;b=2">a query</a>,
<a href="https://plus.google.com/u/0/123/posts/abc">a post</a>,
<a href="http://blocked.example/x">blocked</a> and
<a href="http://typo.example/nothing">a typo</a>.
"""


def _report(urls):
    return {"error_map": {"example.md": [{"url": u, "status": {"code": c}}
                                         for u, c in urls]}}


def _corpus(tmp_path):
    (tmp_path / "example.md").write_text(ESSAY, encoding="utf-8")
    (tmp_path / "README.md").write_text("http://dead.example/page", encoding="utf-8")
    return tmp_path


def _query(snapshots, calls):
    def q(url, ts):
        calls.append((url, ts))
        return snapshots.get(url)
    return q


# ---- pure helpers --------------------------------------------------------------

def test_essay_timestamp_from_frontmatter():
    assert adl.essay_timestamp(ESSAY) == "20130308"
    assert adl.essay_timestamp("no frontmatter") == ""


def test_classify():
    assert adl.classify("http://x.example/", 404) == "dead"
    assert adl.classify("http://x.example/", None) == "dead"      # network error
    assert adl.classify("http://x.example/", 403) == "ambiguous"
    assert adl.classify("http://sethgodin.typepad.com/a", 403) == "dead"
    assert adl.classify("https://web.archive.org/web/2013/http://x/", 404) == "skip"
    assert adl.classify("mailto:a@b.c", None) == "skip"


def test_rewrite_matches_whole_url_only():
    text = '<a href="http://x.example/a">1</a> <a href="http://x.example/abc">2</a>'
    new, n = adl.rewrite(text, "http://x.example/a", "ARCH")
    assert n == 1
    assert new == '<a href="ARCH">1</a> <a href="http://x.example/abc">2</a>'


def test_rewrite_keeps_html_escaping():
    text = '<a href="http://x.example/q?a=1&amp;b=2">q</a>'
    new, n = adl.rewrite(text, "http://x.example/q?a=1&b=2",
                         adl.archive_url("2013", "http://x.example/q?a=1&b=2"))
    assert n == 1
    assert 'href="https://web.archive.org/web/2013/http://x.example/q?a=1&amp;b=2"' in new


def test_rewrite_matches_bare_host_without_slash():
    new, n = adl.rewrite('<a href="http://x.example">x</a>', "http://x.example/", "ARCH")
    assert n == 1 and new == '<a href="ARCH">x</a>'


def test_rewrite_is_idempotent():
    url = "http://x.example/a"
    once, _ = adl.rewrite(f'href="{url}"', url, adl.archive_url("2013", url))
    twice, n = adl.rewrite(once, url, adl.archive_url("2013", url))
    assert n == 0 and twice == once


# ---- end to end ----------------------------------------------------------------

def test_archive_dry_run_plans_but_does_not_write(tmp_path):
    root = _corpus(tmp_path)
    calls = []
    actions = adl.archive(root, _report([("http://dead.example/page", 404)]),
                          query=_query({"http://dead.example/page": "20130301000000"},
                                       calls))
    assert (root / "example.md").read_text(encoding="utf-8") == ESSAY
    assert {"essay": "example.md", "url": "http://dead.example/page",
            "status": "archived",
            "target": "https://web.archive.org/web/20130301000000/http://dead.example/page",
            } in actions
    assert ("http://dead.example/page", "20130308") in calls


def test_archive_apply(tmp_path):
    root = _corpus(tmp_path)
    report = _report([
        ("http://dead.example/page", 404),
        ("http://dead.example/page2", None),
        ("http://www.example.com/q?a=1&b=2", 410),
        ("http://blocked.example/x", 403),
        ("http://typo.example/nothing", None),
    ])
    snaps = {
        "http://dead.example/page": "20130301000000",
        "http://dead.example/page2": "20120101000000",
        "http://www.example.com/q?a=1&b=2": "20130101000000",
        "https://plus.google.com/u/0/123/posts/abc": "20130202000000",
    }
    calls = []
    actions = adl.archive(root, report, apply=True, query=_query(snaps, calls))
    out = (root / "example.md").read_text(encoding="utf-8")
    status = {a["url"]: a["status"] for a in actions}

    assert 'href="https://web.archive.org/web/20130301000000/http://dead.example/page"' in out
    assert 'href="https://web.archive.org/web/20120101000000/http://dead.example/page2"' in out
    assert ("https://web.archive.org/web/20130101000000/"
            "http://www.example.com/q?a=1&amp;b=2") in out
    # dead host found by scanning the source, not from the report
    assert "https://web.archive.org/web/20130202000000/https://plus.google.com/" in out
    # bot-blocked: reported, never queried, never rewritten
    assert status["http://blocked.example/x"] == "ambiguous"
    assert 'href="http://blocked.example/x"' in out
    assert all(u != "http://blocked.example/x" for u, _ in calls)
    # no snapshot: reported, left alone
    assert status["http://typo.example/nothing"] == "no-snapshot"
    assert 'href="http://typo.example/nothing"' in out
    # meta files are never touched
    assert (root / "README.md").read_text(encoding="utf-8") == "http://dead.example/page"


def test_archive_uses_cache_and_honours_skip(tmp_path):
    root = _corpus(tmp_path)
    report = _report([("http://dead.example/page", 404)])
    cache = {"http://dead.example/page @20130308": "20130301000000"}
    calls = []
    adl.archive(root, report, query=_query({}, calls), cache=cache)
    assert not [c for c in calls if c[0] == "http://dead.example/page"]

    actions = adl.archive(root, report, apply=True, query=_query({}, calls),
                          cache=cache, skip={"example.md"})
    assert (root / "example.md").read_text(encoding="utf-8") == ESSAY
    assert {a["status"] for a in actions} == {"skipped-file"}
