"""No WordPress export residue should remain in essay bodies.

Grows one assertion at a time as M1 cleanup lands (TDD: each starts red).
"""


def test_no_caption_shortcodes(essay_bodies):
    bad = [name for name, body in essay_bodies if "[caption" in body]
    assert not bad, f"[caption] shortcodes remain in: {bad}"


def test_no_pingback_comments(essays):
    """Auto-generated WordPress trackback/pingback comments (author carries the
    « separator) are not real reader comments and should be dropped."""
    bad = []
    for p, fm in essays:
        for c in (fm.get("comments") or []):
            author = str(c.get("author", ""))
            if "&laquo;" in author or "«" in author:
                bad.append(p.name)
                break
    assert not bad, f"pingback comments remain in: {bad}"
