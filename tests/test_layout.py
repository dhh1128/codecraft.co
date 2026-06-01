"""The essay layout renders reader comments as a collapsed appendix.

Per the 'anthology, not a blog' goal, comments live in a <details> element
that is closed by default, so each essay reads clean and the original
discussion is one click away.
"""
import re


def _comments_block(root):
    html = (root / "_layouts" / "default.html").read_text(encoding="utf-8")
    m = re.search(r"\{%\s*if page\.comments\s*%\}(.*?)\{%\s*endif\s*%\}", html, re.S)
    assert m, "no `{% if page.comments %}` block in default.html"
    return m.group(1)


def test_comments_in_collapsed_details(root):
    block = _comments_block(root)
    assert "<details" in block and "</details>" in block, "comments not wrapped in <details>"
    assert "<summary" in block, "a collapsed appendix needs a <summary>"
    assert "<details open" not in block, "comments <details> must be collapsed by default"


def test_comment_loop_inside_details(root):
    block = _comments_block(root)
    assert re.search(r"<details[^>]*>.*for comment in page\.comments.*</details>", block, re.S), \
        "the comment loop must live inside the <details> element"
