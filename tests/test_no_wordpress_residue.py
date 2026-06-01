"""No WordPress export residue should remain in essay bodies.

Grows one assertion at a time as M1 cleanup lands (TDD: each starts red).
"""


def test_no_caption_shortcodes(essay_bodies):
    bad = [name for name, body in essay_bodies if "[caption" in body]
    assert not bad, f"[caption] shortcodes remain in: {bad}"
