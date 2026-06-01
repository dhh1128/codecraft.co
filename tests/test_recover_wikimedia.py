"""Prover test for scripts/recover_wikimedia.py.

Recovers Wikimedia Commons images whose legacy hotlink URLs broke: resolves the
Commons file via the API, checks the license permits (at least) non-commercial
publication, downloads a local copy into assets/, rewrites the essay <img src>,
and records provenance/rights in assets/CREDITS.yml. Network calls (the Commons
query + the image download) are injected so the logic is tested deterministically.
"""
import sys
from pathlib import Path

import yaml
import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import recover_wikimedia as rw  # noqa: E402

THUMB = ("http://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/"
         "George_McClellan_at_National_Portrait_Gallery_IMG_4524.JPG/"
         "320px-George_McClellan_at_National_Portrait_Gallery_IMG_4524.JPG")


# ---- pure helpers --------------------------------------------------------------

def test_commons_title_from_thumb_url():
    assert rw.commons_title(THUMB) == \
        "File:George_McClellan_at_National_Portrait_Gallery_IMG_4524.JPG"


def test_commons_title_url_decodes():
    url = ("http://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/"
           "Maslow%27s_hierarchy_of_needs.png/320px-Maslow%27s_hierarchy_of_needs.png")
    assert rw.commons_title(url) == "File:Maslow's_hierarchy_of_needs.png"


def test_requested_width():
    assert rw.requested_width(THUMB) == 320
    assert rw.requested_width("http://x/commons/e/ef/Foo.jpg", default=640) == 640


def test_classify_public_domain_allowed_and_book_safe():
    em = {"License": {"value": "pd"}, "LicenseShortName": {"value": "Public domain"},
          "AttributionRequired": {"value": "false"}, "Artist": {"value": "Billy Hathorn"}}
    lic = rw.classify_license(em)
    assert lic["allowed"] and lic["book_safe"]
    assert "Public domain" in lic["license"]


def test_classify_cc_by_sa_allowed_book_safe_attribution():
    em = {"License": {"value": "cc-by-sa-4.0"},
          "LicenseShortName": {"value": "CC BY-SA 4.0"},
          "AttributionRequired": {"value": "true"}, "Artist": {"value": "<a>Jane</a>"}}
    lic = rw.classify_license(em)
    assert lic["allowed"] and lic["book_safe"]
    assert lic["attribution_required"]
    assert lic["artist"] == "Jane"  # HTML stripped


def test_classify_non_commercial_allowed_but_not_book_safe():
    em = {"License": {"value": "cc-by-nc-2.0"}, "LicenseShortName": {"value": "CC BY-NC 2.0"}}
    lic = rw.classify_license(em)
    assert lic["allowed"]
    assert not lic["book_safe"]  # NC blocks the eventual commercial book


def test_classify_gfdl_allowed_but_not_book_safe():
    # License code field is empty; the license lives in LicenseShortName.
    em = {"License": {"value": ""}, "LicenseShortName": {"value": "GFDL 1.2"},
          "UsageTerms": {"value": "GNU Free Documentation License 1.2"},
          "Artist": {"value": "fir0002"}}
    lic = rw.classify_license(em)
    assert lic["allowed"]          # GFDL is a free license — publishable
    assert not lic["book_safe"]    # but impractical (full-text requirement) for the book


def test_classify_unknown_license_not_allowed():
    lic = rw.classify_license({})
    assert not lic["allowed"]


def test_asset_name_slug_and_extension():
    name = rw.asset_name("Maslow's_hierarchy_of_needs.png",
                         "https://upload.wikimedia.org/.../320px-Maslow's_hierarchy_of_needs.png")
    assert name == "maslow-s-hierarchy-of-needs.png"


# ---- orchestration (stubbed network) -------------------------------------------

def _corpus(tmp_path, src=THUMB):
    (tmp_path / "assets").mkdir()
    (tmp_path / "a.md").write_text(
        f'---\ntitle: T\nitem_id: CC-000001\n---\n<figure><img alt="x" src="{src}"></figure>',
        encoding="utf-8")
    return tmp_path


def _pd_query(title, width):
    return {"missing": False,
            "thumburl": "https://upload.wikimedia.org/x/320px-McClellan.JPG",
            "descriptionurl": "https://commons.wikimedia.org/wiki/File:McClellan",
            "extmetadata": {"License": {"value": "pd"},
                            "LicenseShortName": {"value": "Public domain"},
                            "AttributionRequired": {"value": "false"},
                            "Artist": {"value": "Billy Hathorn"}}}


def test_recover_downloads_localizes_and_credits(tmp_path):
    root = _corpus(tmp_path)
    got = {}

    def dl(url):
        got["url"] = url
        return b"\xff\xd8\xffDATA"

    actions, credits = rw.recover(root, apply=True, query=_pd_query, download=dl,
                                  today="2026-06-01")
    # downloaded the Commons thumburl
    assert got["url"] == "https://upload.wikimedia.org/x/320px-McClellan.JPG"
    # a local asset now exists and the essay points at it
    body = (root / "a.md").read_text(encoding="utf-8")
    assert "upload.wikimedia.org" not in body
    assert 'src="assets/' in body
    asset = body.split('src="')[1].split('"')[0]            # assets/<name>
    assert (root / asset).is_file()
    # CREDITS.yml written with provenance
    creds = yaml.safe_load((root / "assets" / "CREDITS.yml").read_text(encoding="utf-8"))
    entry = creds["images"][asset.split("/", 1)[1]]
    assert entry["license"] == "Public domain"
    assert entry["source"].startswith("https://commons.wikimedia.org/")
    assert entry["book_safe"] is True
    assert "a.md" in entry["used_in"]
    assert any(a["status"] == "recovered" for a in actions)


def test_recover_dry_run_writes_nothing(tmp_path):
    root = _corpus(tmp_path)
    rw.recover(root, apply=False, query=_pd_query, download=lambda u: b"x",
               today="2026-06-01")
    assert "upload.wikimedia.org" in (root / "a.md").read_text(encoding="utf-8")
    assert not (root / "assets" / "CREDITS.yml").exists()


def test_recover_skips_missing_file(tmp_path):
    root = _corpus(tmp_path)
    actions, _ = rw.recover(root, apply=True,
                            query=lambda t, w: {"missing": True},
                            download=lambda u: b"x", today="2026-06-01")
    assert "upload.wikimedia.org" in (root / "a.md").read_text(encoding="utf-8")
    assert any(a["status"] == "missing" for a in actions)


def test_recover_skips_disallowed_license(tmp_path):
    root = _corpus(tmp_path)

    def blocked_query(t, w):
        return {"missing": False, "thumburl": "https://x/t.jpg",
                "descriptionurl": "https://commons.wikimedia.org/wiki/File:X",
                "extmetadata": {}}  # no license → not allowed

    actions, _ = rw.recover(root, apply=True, query=blocked_query,
                            download=lambda u: b"x", today="2026-06-01")
    assert "upload.wikimedia.org" in (root / "a.md").read_text(encoding="utf-8")
    assert any(a["status"] == "license-blocked" for a in actions)
