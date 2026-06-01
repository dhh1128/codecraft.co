"""Tags: every essay carries 1+ tags from the controlled vocabulary, and
scripts/tags.yml maps exactly the essay corpus (no gaps, no orphans)."""
import yaml

VOCAB = {"craft", "systems", "languages", "strategy", "process",
         "comm", "org", "ux", "learning", "meta"}


def test_every_essay_has_valid_tags(essays):
    problems = {}
    for p, fm in essays:
        tags = fm.get("tags") or []
        if not tags:
            problems[p.name] = "no tags"
        elif set(tags) - VOCAB:
            problems[p.name] = f"unknown tags {sorted(set(tags) - VOCAB)}"
    assert not problems, f"tag problems: {problems}"


def test_tags_yml_covers_corpus_exactly(root, essay_paths):
    tagmap = yaml.safe_load((root / "scripts" / "tags.yml").read_text(encoding="utf-8"))
    mapped = set(tagmap)
    corpus = {p.stem for p in essay_paths}
    assert mapped == corpus, (
        f"tags.yml unmapped essays: {sorted(corpus - mapped)}; "
        f"orphan slugs: {sorted(mapped - corpus)}"
    )


def test_tags_yml_matches_frontmatter(root, essays):
    tagmap = yaml.safe_load((root / "scripts" / "tags.yml").read_text(encoding="utf-8"))
    drift = {p.name: (fm.get("tags"), tagmap[p.stem]["tags"])
             for p, fm in essays if fm.get("tags") != tagmap[p.stem]["tags"]}
    assert not drift, f"frontmatter tags != tags.yml (fm, yml): {drift}"
