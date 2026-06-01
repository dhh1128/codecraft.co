"""Prover test for scripts/check_images.py — the image-integrity gate.

check_images.check(root) returns one violation record per problem found in the
essays' <img> tags. The M2 goal is zero external dependencies, every local
image present, alt-text everywhere. These tests prove the checker classifies
correctly (on a synthetic corpus) and runs on the real corpus; the end-state
"clean corpus" assertions are xfail tripwires until M2 lands.
"""
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_images  # noqa: E402

FM = "---\ntitle: T\nitem_id: CC-000001\n---\n"


def _essay(d, name, body):
    (d / name).write_text(FM + body, encoding="utf-8")


@pytest.fixture
def mini(tmp_path):
    """A throwaway corpus root with one real local asset."""
    (tmp_path / "assets").mkdir()
    (tmp_path / "assets" / "real.jpg").write_bytes(b"\xff\xd8\xff" + b"0" * 4000)
    return tmp_path


# ---- classification (synthetic) ------------------------------------------------

def _problems(root, src):
    return {r["problem"] for r in check_images.check(root) if r["src"] == src}


def test_external_http_flagged(mini):
    _essay(mini, "a.md", '<img alt="x" src="http://example.com/p.jpg">')
    assert "external" in _problems(mini, "http://example.com/p.jpg")


def test_external_https_flagged(mini):
    _essay(mini, "a.md", '<img alt="x" src="https://example.com/p.jpg">')
    assert "external" in _problems(mini, "https://example.com/p.jpg")


def test_local_existing_asset_is_clean(mini):
    _essay(mini, "a.md", '<img alt="a tractor" src="assets/real.jpg">')
    assert check_images.check(mini) == []


def test_missing_local_flagged(mini):
    _essay(mini, "a.md", '<img alt="x" src="assets/nope.jpg">')
    assert "missing-local" in _problems(mini, "assets/nope.jpg")


def test_missing_alt_flagged(mini):
    _essay(mini, "a.md", '<img src="assets/real.jpg">')
    assert "no-alt" in _problems(mini, "assets/real.jpg")


def test_empty_alt_flagged(mini):
    _essay(mini, "a.md", '<img alt="" src="assets/real.jpg">')
    assert "no-alt" in _problems(mini, "assets/real.jpg")


def test_malformed_flagged(mini):
    _essay(mini, "a.md", '<img alt="x" src="http://farm1.staticfliccom/x.jpg">')
    probs = _problems(mini, "http://farm1.staticfliccom/x.jpg")
    assert "malformed" in probs


def test_one_image_can_have_multiple_problems(mini):
    # external AND no alt-text
    _essay(mini, "a.md", '<img alt="" src="http://example.com/p.jpg">')
    assert _problems(mini, "http://example.com/p.jpg") == {"external", "no-alt"}


def test_violation_records_carry_location(mini):
    _essay(mini, "a.md", 'intro line\n\n<img alt="" src="http://x.com/p.jpg">')
    rec = check_images.check(mini)[0]
    assert {"essay", "line", "src", "problem"} <= set(rec)
    assert rec["essay"] == "a.md" and rec["line"] >= 1


def test_meta_files_are_not_scanned(mini):
    (mini / "README.md").write_text('<img src="http://x.com/a.jpg">', encoding="utf-8")
    assert check_images.check(mini) == []


# ---- runs on the real corpus ---------------------------------------------------

def test_runs_on_corpus_and_returns_worklist():
    violations = check_images.check(ROOT)
    assert isinstance(violations, list) and violations, \
        "expected current violations — external images still exist (M2 unfinished)"
    for r in violations[:10]:
        assert {"essay", "line", "src", "problem"} <= set(r)


def test_known_wikimedia_image_flagged_external():
    violations = check_images.check(ROOT)
    assert any("upload.wikimedia.org" in r["src"] and r["problem"] == "external"
               for r in violations), \
        "the are-you-losing-enough-battles wikimedia <img> should be flagged external"


def test_every_local_image_reference_resolves():
    """A real integrity guarantee we can hold today: no broken local links."""
    missing = [r for r in check_images.check(ROOT) if r["problem"] == "missing-local"]
    assert not missing, f"local <img> src pointing at absent files: " \
                        f"{[(r['essay'], r['src']) for r in missing]}"


# ---- end-state gates (tripwires; flip to hard asserts when M2 completes) --------

@pytest.mark.xfail(strict=True, reason="M2 image ownership in progress: external refs remain")
def test_corpus_has_zero_external_or_malformed_images():
    bad = [r for r in check_images.check(ROOT)
           if r["problem"] in ("external", "malformed")]
    assert not bad


@pytest.mark.xfail(strict=True, reason="M2: alt-text not yet present on every image")
def test_every_image_has_alt_text():
    no_alt = [r for r in check_images.check(ROOT) if r["problem"] == "no-alt"]
    assert not no_alt
