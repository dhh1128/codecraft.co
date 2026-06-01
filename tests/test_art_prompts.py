"""assets/art-prompts.yml holds one ready-to-paste openart.ai prompt per Flickr
image we'll replace with owned editorial-line art. This proves the file stays
well-formed and consistent (every prompt carries the shared house-style suffix).
See docs/art-style.md."""
import yaml


def _prompts(root):
    return yaml.safe_load((root / "assets" / "art-prompts.yml").read_text(encoding="utf-8"))


def test_loads_with_style_and_negative(root):
    d = _prompts(root)
    assert d.get("style_suffix") and d.get("negative_prompt")
    assert isinstance(d.get("images"), list) and d["images"]


def test_every_entry_is_well_formed(root):
    d = _prompts(root)
    suffix = d["style_suffix"]
    problems = {}
    for e in d["images"]:
        for field in ("essay", "replaces", "concept", "filename", "prompt", "status"):
            if not e.get(field):
                problems[e.get("filename", "?")] = f"missing {field}"
        if e.get("prompt") and not e["prompt"].endswith(suffix):
            problems[e.get("filename", "?")] = "prompt missing house-style suffix"
        if e.get("essay") and not (root / e["essay"]).exists():
            problems[e.get("filename", "?")] = f"essay not found: {e['essay']}"
    assert not problems, problems


def test_filenames_unique(root):
    names = [e["filename"] for e in _prompts(root)["images"]]
    dupes = {n for n in names if names.count(n) > 1}
    assert not dupes, f"duplicate target filenames: {dupes}"


def test_replaces_are_flickr_urls(root):
    bad = [e["replaces"] for e in _prompts(root)["images"]
           if "flickr" not in e["replaces"] and "staticfliccom" not in e["replaces"]]
    assert not bad, f"non-Flickr replace targets: {bad}"
