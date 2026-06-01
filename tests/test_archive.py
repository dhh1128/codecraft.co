"""Guest posts by other authors are archived, not published.

Two essays were contributed by guest authors (Jesse Harris; Steve Tolman).
They live in archive/ (excluded from the Jekyll build) with authorship
recorded, must not reappear in the published corpus, and their old URLs
redirect to a relevant published page.
"""
import re

GUEST_AUTHORS = {
    "code-isnt-art": "Jesse Harris",
    "steve-jackson-lead-with-passion": "Steve Tolman",
}


def test_guest_posts_not_in_published_corpus(essay_paths):
    leaked = set(GUEST_AUTHORS) & {p.stem for p in essay_paths}
    assert not leaked, f"archived guest posts still in the published corpus: {sorted(leaked)}"


def test_guest_posts_archived_with_authorship(root):
    for slug, who in GUEST_AUTHORS.items():
        p = root / "archive" / f"{slug}.md"
        assert p.exists(), f"missing archive/{slug}.md"
        fm = re.match(r"^---\n(.*?)\n---\n", p.read_text(encoding="utf-8"), re.S).group(1)
        assert who in fm, f"archive/{slug}.md must record author {who!r}"


def test_old_urls_redirect_to_a_published_page(root):
    published = ((root / "role-models.md").read_text(encoding="utf-8") +
                (root / "what-is-good-code.md").read_text(encoding="utf-8"))
    for slug in GUEST_AUTHORS:
        assert f"/{slug}" in published, f"no redirect for old URL /{slug}"
