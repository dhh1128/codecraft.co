"""Every essay must have parseable frontmatter with the fields populated so far.

The M3-enrichment fields (status, keywords, abstract, version, revision_date)
are intentionally NOT required yet — they are added in a later milestone.
"""
import datetime

REQUIRED_NOW = ["title", "date", "slug", "item_id", "tags"]


def test_every_essay_parses(essays):
    bad = [p.name for p, fm in essays if not isinstance(fm, dict)]
    assert not bad, f"unparseable frontmatter: {bad}"


def test_required_fields_present(essays):
    missing = {
        p.name: [k for k in REQUIRED_NOW if fm.get(k) in (None, "", [])]
        for p, fm in essays
        if [k for k in REQUIRED_NOW if fm.get(k) in (None, "", [])]
    }
    assert not missing, f"essays missing required fields: {missing}"


def test_date_is_a_real_date(essays):
    bad = [p.name for p, fm in essays if not isinstance(fm.get("date"), datetime.date)]
    assert not bad, f"date not parsed as a date: {bad}"


def test_slug_matches_filename(essays):
    bad = [p.name for p, fm in essays if fm.get("slug") != p.stem]
    assert not bad, f"slug != filename for: {bad}"
