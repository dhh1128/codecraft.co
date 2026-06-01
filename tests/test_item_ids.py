"""Permanent item-ids: well-formed, unique, and consistent with the
deterministic CC-YYMMOO assignment rule (stored == recomputed)."""
import re

import assign_ids  # from scripts/, via conftest sys.path

ID_RE = re.compile(r"^CC-\d{6}$")


def test_id_format(essays):
    bad = [(p.name, fm.get("item_id")) for p, fm in essays
           if not ID_RE.match(str(fm.get("item_id", "")))]
    assert not bad, f"malformed item_ids: {bad}"


def test_ids_unique(essays):
    ids = [fm["item_id"] for _, fm in essays]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    assert not dupes, f"duplicate item_ids: {dupes}"


def test_ids_match_deterministic_rule(essays):
    """Stored ids equal what assign_ids would compute — proves stability."""
    recomputed = assign_ids.compute_ids([str(p) for p, _ in essays])
    drift = {p.name: (fm["item_id"], recomputed[str(p)])
             for p, fm in essays if fm["item_id"] != recomputed[str(p)]}
    assert not drift, f"stored != recomputed (stored, expected): {drift}"
