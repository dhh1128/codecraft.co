"""lint_wordpress.convert_bold_headings turns standalone bold lines (the
WordPress-era essays' section titles) into real ## headings, while leaving
mid-sentence bold and lone bold links alone."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import lint_wordpress as lw  # noqa: E402


def test_strong_line_becomes_h2():
    assert lw.convert_bold_headings("<strong>Diagnosis</strong>") == "## Diagnosis"


def test_b_line_becomes_h2():
    assert lw.convert_bold_headings("<b>Treatment</b>") == "## Treatment"


def test_strips_presentational_span():
    s = '<strong><span style="color:#333399;">One example of redundancy</span></strong>'
    assert lw.convert_bold_headings(s) == "## One example of redundancy"


def test_preserves_inline_emphasis():
    s = "<strong>The needs of <em>all</em> humans</strong>"
    assert lw.convert_bold_headings(s) == "## The needs of <em>all</em> humans"


def test_period_ending_heading_still_converts():
    s = "<strong>I. Thou shalt measure.</strong>"
    assert lw.convert_bold_headings(s) == "## I. Thou shalt measure."


def test_lone_bold_link_is_left_alone():
    s = '<strong><a href="http://x">System Thinking</a></strong>'
    assert lw.convert_bold_headings(s) == s


def test_midsentence_bold_is_left_alone():
    s = "<strong>Exceptions</strong> should declare their semantics."
    assert lw.convert_bold_headings(s) == s


def test_only_the_bold_line_changes_in_a_body():
    body = "an intro paragraph\n\n<strong>Section</strong>\n\nbody text here\n"
    out = lw.convert_bold_headings(body)
    assert "\n## Section\n" in out
    assert "an intro paragraph" in out and "body text here" in out
