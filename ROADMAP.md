# Roadmap

The project plan for turning the codecraft.co WordPress export into a curated,
professional anthology of essays. Tick items as they're completed. See
[AGENTS.md](AGENTS.md) for vision and principles.

_Created 2026-06-01._

**The funnel:** 124 essays → mechanically clean → owned images → rich metadata
→ curated to N `published` → SEO'd + cross-linked + PDF'd → M selected into a book.

**Locked decisions:** images case-by-case (own/generate/redraw/drop); comments →
collapsed appendix; prose = mechanical fixes only; public archive is itself
curated (`status: published | retired`, `book: true` subset).

---

## M0 — AI context & scaffolding
- [x] Write `AGENTS.md` (vision, principles, mechanical-only guardrail, conventions)
- [x] Add `CLAUDE.md` redirect to `AGENTS.md`
- [x] Create `ROADMAP.md` (this file)
- [x] Define the frontmatter schema → `docs/conventions.md`
- [x] Define the `CC-XXX-YYMMOO` item-id convention → `docs/conventions.md`
- [x] Scaffold `scripts/` + `tests/` + `requirements.txt`
- [ ] **BLOCKED (pending taxonomy debate):** freeze the category taxonomy
- [ ] **BLOCKED (needs taxonomy):** assign a permanent `item_id` to every essay

## M1 — De-WordPress & clean the Markdown _(mechanical only — no prose edits)_
- [ ] Convert 17 `[caption]` shortcodes to clean figure markup
- [ ] Resolve 18 `wp-content` references
- [ ] Fix malformed image URLs (`staticfliccom`, `static.flickr.com`, etc.)
- [ ] Normalize all `<img>` tags to one consistent figure convention
- [ ] Audit & repair garbled/missing post metadata (dates, titles, slugs)
- [ ] Drop pingback/trackback/spam comments; keep genuine human comments
- [ ] Move comments to a collapsed appendix (`<details>`) in `_layouts/default.html`

## M2 — Image ownership & quality
- [ ] `inventory_images.py` → `assets/image-triage.yml`
- [ ] Fill `disposition` per image (own / generate / redraw / drop)
- [ ] Establish a house visual style for AI-generated art
- [ ] `apply_image_triage.py`: localize, generate, redraw, or drop + reflow
- [ ] Record provenance/rights for every image in `assets/CREDITS.yml`
- [ ] Quality bar: min resolution, alt-text everywhere, sane file sizes
- [ ] Verify: zero external image references remain

## M3 — Metadata enrichment
- [ ] Add `category` (per frozen taxonomy) to each essay
- [ ] Add `keywords`, `abstract`, `version`, `revision_date`
- [ ] Backfill/verify original publication `date`
- [ ] Validate the whole corpus against the schema

## M3.5 — Curation gate
- [ ] Per-essay keep/retire decision; set `status: published | retired`
- [ ] Confirm retired essays are excluded from index, sitemap, and PDFs (but kept in repo)

## M4 — Navigation, cross-refs & citations
- [ ] Generate categorized, date-aware `index.md` (published only)
- [ ] Replace flat `README.md` list with the themed TOC
- [ ] Wire up cross-references between related essays
- [ ] Add series navigation (e.g. "Good Code Is…", decoupling parts, mentor profiles)
- [ ] Normalize external citations; verify each source resolves or is archived

## M5 — SEO posture
- [ ] Per-page SEO fields feed `jekyll-seo-tag` (title/description/keywords)
- [ ] JSON-LD structured data (`Article`/`BlogPosting`) in the layout
- [ ] `sitemap.xml`, canonical URLs, corrected `robots.txt`
- [ ] Open Graph + Twitter card images
- [ ] Verify **all** legacy WordPress `redirect_from` URLs still resolve
- [ ] Lighthouse/SEO audit pass

## M6 — PDF generation
- [ ] Port `pandoc.py` + LaTeX headers from `../papers`, adapted to essay metadata
- [ ] Per-essay PDF with embedded title/author/keywords/item-id
- [ ] Decide: commit PDFs vs. build as CI release artifacts

## M7 — Toolkit + pytest suite _(continuous, grows with every milestone)_
Each quality goal gets a fixer script (`--check-only` capable) and a prover test:
- [ ] `validate_frontmatter.py` ↔ test: complete, schema-valid metadata
- [ ] `check_links.py` ↔ test: no broken internal/external links
- [ ] `check_images.py` ↔ test: no external images; all local images exist + alt-text + quality
- [ ] `assign_ids.py` ↔ test: unique, well-formed, immutable `item_id`s
- [ ] `generate_index.py` ↔ test: index/TOC in sync with corpus
- [ ] `check_crossrefs.py` ↔ test: related-essay links resolve
- [ ] `check_citations.py` ↔ test: external sources well-formed + reachable/archived
- [ ] `check_seo.py` ↔ test: required SEO fields present + within length, no dupes
- [ ] `build_pdfs.py` ↔ test: a current PDF exists per published essay
- [ ] `lint_wordpress.py` ↔ test: no `[caption]`, `wp-content`, or WP residue
- [ ] CI: add `check-requirements.yml` (pytest + `--check-only`); keep scheduled link-check
- [ ] Bump CI actions off deprecated `node20` versions when touched

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
