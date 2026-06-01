# Roadmap

The project plan for turning the codecraft.co WordPress export into a curated,
professional anthology of essays. Tick items as they're completed. See
[AGENTS.md](AGENTS.md) for vision and principles.

_Created 2026-06-01._

**The funnel:** 124 essays → mechanically clean → owned images → rich metadata
→ curated to N `published` → SEO'd + cross-linked + PDF'd → M selected into a book.

**Locked decisions:** images case-by-case (own/generate/redraw/drop); comments →
collapsed appendix; prose = mechanical fixes only; public archive is itself
curated (`status: published | retired`, `book: true` subset); **publishing
platform = Zensical** (replaces Jekyll, decided 2026-06-01).

---

## M0 — AI context & scaffolding
- [x] Write `AGENTS.md` (vision, principles, mechanical-only guardrail, conventions)
- [x] Add `CLAUDE.md` redirect to `AGENTS.md`
- [x] Create `ROADMAP.md` (this file)
- [x] Define the frontmatter schema → `docs/conventions.md`
- [x] Define the `CC-XXX-YYMMOO` item-id convention → `docs/conventions.md`
- [x] Scaffold `scripts/` + `tests/` + `requirements.txt`
- [x] Freeze the classification: multi-valued `tags` (controlled vocab of 10), not mutually-exclusive categories — see `docs/conventions.md`
- [x] Assign a permanent `item_id` (`CC-YYMMOO`, no category segment) + `tags` to every essay — `scripts/assign_ids.py`, data in `scripts/tags.yml`

## M1 — De-WordPress & clean the Markdown _(mechanical only — no prose edits)_
- [x] Repair broken YAML frontmatter in 16 essays (mangled `---` fences; unquoted `title:`/`author:` values with colons) — `scripts/fix_frontmatter.py`. Unblocked dates/IDs.
- [x] Convert `[caption]` shortcodes to clean `<figure>` markup (19 blocks in 17 essays) — `scripts/lint_wordpress.py`, test `tests/test_no_wordpress_residue.py`
- [x] Audit & repair garbled/missing post metadata — done via the frontmatter repair + ID/date backfill above
- [x] Drop pingback/trackback comments; keep genuine human comments — `scripts/lint_wordpress.py` (245 lines across 33 essays; « marker), test `test_no_pingback_comments`
- [x] Move comments to a collapsed appendix — originally a Jekyll `<details>` in `_layouts/default.html`; superseded in M3.6 by the Zensical `??? quote` admonition. The guarantee now lives on the real build output (`tests/test_site_build.py`); the legacy `tests/test_layout.py` was retired with the Jekyll layout.
- → _Moved to M2 (entangled with the image inventory; 22/23 wp-content images already in `assets/`):_ resolve `wp-content` refs, fix malformed image URLs (`staticfliccom`, `static.flickr.com`), normalize `<img>` tags

_M1 pure items complete; remaining M1 work folded into M2._

## M2 — Image ownership & quality
- [x] `inventory_images.py` → `assets/image-triage.yml` — 157 refs catalogued (39 local, 32 wp, 84 external, 2 malformed); 70 auto-marked `own`, 87 blank to triage. Also emits a browsable `images_inventory.html` contact sheet (thumbnail/orig URL/license/local path/disposition + filters; gitignored). Test `tests/test_image_inventory.py` (6 tests).
- [~] Localize `wp-content` image refs → `assets/` via `scripts/apply_image_triage.py` (executes `own`-disposition rows: rewrite `<img src>`/`<a href>` → `assets/<file>`, downloading if no local copy; idempotent, exact-string, prose-safe). **Done: 22 `codecraft.co` owned images localized** (external `<img>` count 102→82). Remaining: the other `own` rows, the 2 malformed URLs, and the `scn-shot-2014-05-15` judgment call (URL is 404; date-exact local `screen-shot-2014-05-15-…png` is the likely match — awaiting confirmation)
- [ ] Fill `disposition` per image for the 87 blanks (own / generate / redraw / drop)
- [ ] Establish a house visual style for AI-generated art
- [~] `apply_image_triage.py` ↔ test `tests/test_apply_image_triage.py` (7 tests): `own` disposition implemented (localize + download). `generate`/`redraw`/`drop` + reflow still to do.
- [ ] Record provenance/rights for every image in `assets/CREDITS.yml`
- [ ] Quality bar: min resolution, alt-text everywhere (118 imgs currently lack alt — `check_images.py`), sane file sizes
- [ ] Verify: zero external image references remain

## M3 — Metadata enrichment
- [ ] Add `category` (per frozen taxonomy) to each essay
- [ ] Add `keywords`, `abstract`, `version`, `revision_date`
- [ ] Backfill/verify original publication `date`
- [ ] Validate the whole corpus against the schema

## M3.5 — Curation gate
- [x] Archive the 2 guest posts by other authors → `archive/` (excluded from build): `code-isnt-art` (Jesse Harris), `steve-jackson-lead-with-passion` (Steve Tolman). Authorship recorded; old URLs redirect to `what-is-good-code` / `role-models`; corpus 123 → 121. Guard test `tests/test_archive.py`.
- [ ] Per-essay keep/retire decision; set `status: published | retired`
- [ ] Confirm retired essays are excluded from index, sitemap, and PDFs (but kept in repo)

## M3.6 — Platform migration (Jekyll → Zensical)
- [x] Decide platform: **Zensical** (MkDocs-Material successor), validated by a full-corpus build (de-risked via a 6-essay spike first)
- [x] `scripts/build_site.py` — the assembler: root essays → disposable `build/` MkDocs tree; `build.sh` wraps assemble + `zensical build`; test `tests/test_site_build.py` (8 tests)
- [x] Reader comments → collapsed `??? quote` admonition ("Original discussion"); `md_in_html`+`attr_list` render the inline `<figure>`/`<img>`; page frontmatter slimmed to title+tags
- [x] Legacy `redirect_from` URLs preserved as self-contained meta-refresh HTML stubs (no dependence on `mkdocs-redirects`; Zensical plugin-compat is narrow)
- [x] House styling ported → `assets/css/zensical-extra.css` (Barlow Condensed/Open Sans, brown palette, print-without-sidebar, mobile)
- [ ] GitHub Actions **publish** workflow: `build.sh` → GitHub Pages (pin actions to `node24`); retire Jekyll auto-build
- [ ] Provisional `build/docs/index.md` TOC + tag-grouped nav are first-pass — finalize under M4
- [ ] Clean up the 138 internal-link warnings the build surfaces (legacy `/category/…` and cross-essay links) — feeds M4/M7
- [ ] Once deploy is live, retire the legacy Jekyll files (`_config.yml`, `_layouts/`, `_includes/`, `assets/css/style.scss`)

## M4 — Navigation, cross-refs & citations
- [ ] Decide the primary TOC structure now that essays are tag-classified (no single category): e.g. a curated reading order / section set keyed off each essay's first tag, with tags as secondary "see also" nav — keep the anthology feel, avoid a blog-style tag cloud
- [ ] Generate tag-aware, date-aware `index.md` (published only)
- [ ] Replace flat `README.md` list with the themed TOC
- [ ] Wire up cross-references between related essays
- [ ] Add series navigation (e.g. "Good Code Is…", decoupling parts, mentor profiles)
- [ ] Normalize external citations; verify each source resolves or is archived

## M5 — SEO posture
- [ ] Per-page SEO fields → Zensical/Material meta (title/description/keywords) via the assembler (was `jekyll-seo-tag`)
- [ ] JSON-LD structured data (`Article`/`BlogPosting`) injected by the assembler / a Material partial
- [ ] `sitemap.xml`, canonical URLs, corrected `robots.txt`
- [ ] Open Graph + Twitter card images
- [ ] Verify **all** legacy WordPress `redirect_from` URLs still resolve
- [ ] Lighthouse/SEO audit pass

## M6 — PDF generation
- [ ] Port `pandoc.py` + LaTeX headers from `../papers`, adapted to essay metadata
- [ ] Per-essay PDF with embedded title/author/keywords/item-id
- [ ] Decide: commit PDFs vs. build as CI release artifacts

## M7 — Toolkit + pytest suite _(continuous, grows with every milestone)_
Each quality goal gets a fixer script (`--check-only` capable) and a prover test.
Live suite: `tests/` (run `pytest`) — 10 tests green covering frontmatter parse,
item-id format/uniqueness/determinism, and tag validity/coverage.
- [~] `validate_frontmatter.py` ↔ test: `tests/test_frontmatter.py` covers required-now fields (title/date/slug/item_id/tags); M3 fields (status/keywords/abstract/version/revision_date) still to enforce
- [x] `assign_ids.py` ↔ test: `tests/test_item_ids.py` + `tests/test_tags.py` — unique, well-formed, deterministic ids; controlled tags
- [x] `build_site.py` ↔ test: `tests/test_site_build.py` — assembler emits one page per published essay, slim frontmatter, comments admonition, redirect stubs, valid mkdocs.yml, styling carried over
- [ ] `check_links.py` ↔ test: no broken internal/external links
- [~] `check_images.py` ↔ test `tests/test_check_images.py`: flags external/malformed `<img>`, missing local files, and missing alt-text; `--check-only` gate + `essay:line` worklist. Current corpus: **102 external, 2 malformed, 0 missing-local, 118 no-alt**. End-state ("zero external", "alt everywhere") encoded as xfail tripwires until M2 lands. Image-quality (resolution/file-size) deferred to a Pillow pass. Wire `--check-only` into CI once the corpus is clean (it exits 1 today, so it would redden CI prematurely).
- [ ] `generate_index.py` ↔ test: index/TOC in sync with corpus
- [ ] `check_crossrefs.py` ↔ test: related-essay links resolve
- [ ] `check_citations.py` ↔ test: external sources well-formed + reachable/archived
- [ ] `check_seo.py` ↔ test: required SEO fields present + within length, no dupes
- [ ] `build_pdfs.py` ↔ test: a current PDF exists per published essay
- [ ] `lint_wordpress.py` ↔ test: no `[caption]`, `wp-content`, or WP residue
- [x] CI: `.github/workflows/ci.yml` runs pytest + the `--check-only` guards on every push/PR; status badge in README. Keep scheduled link-check.
- [x] Pin CI actions to node24 (`checkout@v6`, `setup-python@v6`; verified `setup-python@v5` is node20)

## M8 — Book (Amazon KDP)
- [ ] Define selection criteria; mark chosen essays `book: true`
- [ ] Define ordering and sections
- [ ] Pipeline: essays → manuscript → EPUB + print PDF (Pandoc)
- [ ] Front/back matter (intro, about, license, colophon)
- [ ] KDP formatting (trim size, bleed, ISBN, cover)
- [ ] Proof copy → publish

---

## Housekeeping / deferred
- [ ] Archive legacy one-shot migration scripts under `tools/migration/` (don't extend them)
- [x] Fix Dependabot alert #1: bump `lycheeverse/lychee-action` v1.10.0 → v2.8.0 (arbitrary code injection in `< 2.0.2`); also bumped `actions/checkout` v4 → v6 (node20 → node24)
- [ ] Keep the Dependabot security tab clean as standing hygiene (see AGENTS.md)
- [x] **Decision made:** migrate publishing platform Jekyll → Zensical (see M3.6; modelled on `../tti/home`)
