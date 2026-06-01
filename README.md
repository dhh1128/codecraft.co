# Codecraft

[![CI](https://github.com/dhh1128/codecraft.co/actions/workflows/ci.yml/badge.svg)](https://github.com/dhh1128/codecraft.co/actions/workflows/ci.yml)

*software = science + art + people*

A curated anthology of essays on software architecture and the craft of
programming, by Daniel Hardman — published at
**[codecraft.co](https://codecraft.co)**.

This repository holds the essay sources (Markdown), the owned images, and a
tested Python toolkit that maintains and publishes them. The site is built with
Zensical (the actively-maintained MkDocs-Material successor).

> **New here? Read [AGENTS.md](AGENTS.md) first** — it's the single source of
> truth for vision, conventions, and how to work in this repo. The tickable
> plan is in [ROADMAP.md](ROADMAP.md); the metadata schema and ID convention
> are in [docs/conventions.md](docs/conventions.md).

## Quick start

```bash
git clone git@github.com:dhh1128/codecraft.co.git
cd codecraft.co
./build.sh            # assemble the essays + run zensical build → build/site/
```

Live preview while editing:

```bash
cd build && zensical serve     # http://127.0.0.1:8000
```

Run the test suite — it *proves* the quality goals, so `pytest` green means
publication-ready:

```bash
pip install -r requirements.txt
pytest
```

## How it's built

The root-level `*.md` files are the canonical essay sources. `build.sh` runs
`scripts/build_site.py`, an *assembler* that generates a disposable MkDocs tree
under `build/` (gitignored), then `zensical build` renders `build/site/`. The
site's table of contents is the generated `index.md` — **this README is not part
of the published site.**

## Toolkit (`scripts/`)

Every quality goal is a script plus a prover test in `tests/` (`pytest`).

| Script | Purpose |
|---|---|
| `build_site.py` | Assemble the essays into the Zensical site |
| `assign_ids.py` | Assign permanent `CC-YYMMOO` item-ids and tags |
| `fix_frontmatter.py` | Repair WordPress-export YAML frontmatter |
| `lint_wordpress.py` | Strip WordPress residue (captions, pingbacks, …) |
| `inventory_images.py` | Catalog every image into the triage manifest |
| `check_images.py` | Gate: no external/broken images; alt-text present |
| `apply_image_triage.py` | Localize owned images per the manifest |
| `recover_wikimedia.py` | Recover broken Wikimedia images + record rights |

## License

Content is licensed
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) unless
otherwise noted. Per-image rights and provenance are tracked in
[`assets/CREDITS.yml`](assets/CREDITS.yml).
