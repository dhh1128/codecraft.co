"""Shared fixtures: discover and parse the essay corpus once per session."""
import re
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))  # let tests import the toolkit

META_FILES = {"README.md", "AGENTS.md", "CLAUDE.md", "ROADMAP.md", "index.md"}


def _essay_paths():
    return sorted(p for p in ROOT.glob("*.md") if p.name not in META_FILES)


@pytest.fixture(scope="session")
def root():
    return ROOT


@pytest.fixture(scope="session")
def essay_paths():
    return _essay_paths()


@pytest.fixture(scope="session")
def essays():
    """List of (Path, frontmatter dict-or-None)."""
    out = []
    for p in _essay_paths():
        text = p.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        try:
            fm = yaml.safe_load(m.group(1)) if m else None
        except yaml.YAMLError:
            fm = None
        out.append((p, fm))
    return out
