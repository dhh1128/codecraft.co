"""Prover test for scripts/build_site.py — the Jekyll → Zensical assembler.

The assembler reads the canonical root-level essays and emits a MkDocs/Zensical
source tree (mkdocs.yml + docs/) into a build directory. These tests prove the
guarantees the migration depends on, *without* invoking the (heavy) zensical
build itself: the structural contract is what matters here.
"""
import os
import sys
import yaml
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

build_site = pytest.importorskip("build_site")


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    """Assemble the whole corpus once into a temp build dir."""
    out = tmp_path_factory.mktemp("build")
    summary = build_site.assemble(ROOT, str(out))
    return out, summary


def _published_slugs():
    slugs = []
    for name in os.listdir(ROOT):
        if not name.endswith(".md"):
            continue
        with open(os.path.join(ROOT, name), encoding="utf-8") as fh:
            text = fh.read()
        if not text.startswith("---"):
            continue
        fm = yaml.safe_load(text.split("---", 2)[1])
        if not fm or "item_id" not in fm:
            continue
        if fm.get("status") == "retired":
            continue
        slugs.append(fm.get("slug") or name[:-3])
    return slugs


def test_one_doc_per_published_essay(built):
    out, summary = built
    docs = out / "docs"
    slugs = _published_slugs()
    assert len(slugs) == 121, f"expected 121 published essays, found {len(slugs)}"
    for slug in slugs:
        assert (docs / f"{slug}.md").is_file(), f"missing doc for {slug}"
    assert summary["essays"] == len(slugs)


def test_archived_guest_posts_excluded(built):
    out, _ = built
    docs = out / "docs"
    for slug in ("code-isnt-art", "steve-jackson-lead-with-passion"):
        assert not (docs / f"{slug}.md").exists(), f"{slug} should be excluded"


def test_no_jekyll_or_wordpress_residue_in_output(built):
    out, _ = built
    docs = out / "docs"
    offenders = []
    for md in docs.glob("*.md"):
        body = md.read_text(encoding="utf-8")
        if "{%" in body or "{{" in body:  # liquid tags
            offenders.append((md.name, "liquid"))
        if "[caption" in body:
            offenders.append((md.name, "caption shortcode"))
    assert not offenders, f"residue found: {offenders[:5]}"


def test_comments_rendered_as_collapsible_admonition(built):
    out, _ = built
    docs = out / "docs"
    # what-is-good-code has a reader comment in its frontmatter.
    text = (docs / "what-is-good-code.md").read_text(encoding="utf-8")
    assert "## Original discussion" in text
    assert '??? quote' in text
    # frontmatter must NOT carry the raw comments list any more
    fm = yaml.safe_load(text.split("---", 2)[1])
    assert "comments" not in fm


def test_page_frontmatter_is_slim(built):
    out, _ = built
    docs = out / "docs"
    text = (docs / "what-is-good-code.md").read_text(encoding="utf-8")
    fm = yaml.safe_load(text.split("---", 2)[1])
    assert fm.get("title")
    # Jekyll-only keys must be gone from the page frontmatter
    for jekyll_key in ("date", "slug", "item_id", "redirect_from"):
        assert jekyll_key not in fm, f"{jekyll_key} should not leak into page frontmatter"


def test_redirect_stubs_generated(built):
    out, summary = built
    docs = out / "docs"
    # what-is-good-code redirects from /2012/08/26/what-is-good-code
    stub = docs / "2012" / "08" / "26" / "what-is-good-code" / "index.html"
    assert stub.is_file(), "legacy redirect stub missing"
    html = stub.read_text(encoding="utf-8")
    assert "http-equiv" in html.lower() and "refresh" in html.lower()
    assert "/what-is-good-code/" in html
    # every essay has redirect_from, so we expect at least 121 stubs
    assert summary["redirects"] >= 121


def test_mkdocs_yml_valid_and_complete(built):
    out, _ = built
    cfg_path = out / "mkdocs.yml"
    assert cfg_path.is_file()
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    assert cfg["theme"]["name"] == "material"
    exts = cfg["markdown_extensions"]
    ext_names = [e if isinstance(e, str) else list(e)[0] for e in exts]
    for required in ("admonition", "pymdownx.details", "attr_list", "md_in_html"):
        assert required in ext_names, f"missing markdown extension {required}"
    assert "stylesheets/extra.css" in cfg.get("extra_css", [])


def test_back_link_on_every_essay_page(built):
    out, _ = built
    docs = out / "docs"
    slugs = _published_slugs()
    for slug in slugs:
        text = (docs / f"{slug}.md").read_text(encoding="utf-8")
        body = text.split("---", 2)[2]  # after frontmatter
        assert 'class="back-link"' in body, f"{slug} missing back link"
        assert 'href="/"' in body, f"{slug} back link not pointing at root"


def test_no_back_link_on_index(built):
    out, _ = built
    index = (out / "docs" / "index.md").read_text(encoding="utf-8")
    assert "back-link" not in index, "the home/TOC page should not have a '← back' link"


def test_no_status_badges_on_the_site(built):
    """README carries the CI badge for GitHub; the published site must not."""
    out, _ = built
    index = (out / "docs" / "index.md").read_text(encoding="utf-8")
    assert "badge.svg" not in index and "/badge" not in index, \
        "status badges belong in README (GitHub view), not on the site TOC"


def test_back_link_is_print_hidden_in_css(built):
    out, _ = built
    css = (out / "docs" / "stylesheets" / "extra.css").read_text(encoding="utf-8")
    # the print block must hide the back link
    print_block = css.split("@media print", 1)[1]
    assert "back-link" in print_block


def test_root_static_files_copied_for_pages(built):
    """CNAME (custom domain) and robots.txt must reach the published site."""
    out, _ = built
    docs = out / "docs"
    cname = docs / "CNAME"
    assert cname.is_file(), "CNAME missing — deploying would break the custom domain"
    assert cname.read_text(encoding="utf-8").strip() == "codecraft.co"
    assert (docs / "robots.txt").is_file()


def test_styling_carried_over(built):
    out, _ = built
    css = (out / "docs" / "stylesheets" / "extra.css").read_text(encoding="utf-8")
    # the author's fonts and signature heading colour must be present
    assert "Barlow Condensed" in css
    assert "Open Sans" in css
    assert "#491705" in css  # heading brown
    assert "@media print" in css  # printable without sidebar
