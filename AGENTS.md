# AGENTS.md — Project context for AI collaborators

> This file is the single source of truth for working in this repository.
> `CLAUDE.md`, `GEMINI.md`, etc. are thin redirects here. Read this first.
> The live, tickable task list lives in [ROADMAP.md](ROADMAP.md).
> The exact metadata schema and ID convention live in [docs/conventions.md](docs/conventions.md).

## What this repository is

A collection of ~124 essays written years ago by Daniel Hardman about software
architecture and the craft of programming. They were authored on WordPress,
exported, and converted to Markdown. They are published as a Jekyll site on
GitHub Pages at **codecraft.co** (CC BY 4.0).

The repo is mid-transformation: from a date-ordered WordPress blog export into a
**curated, professional anthology of essays**. A sister repo, `../papers`,
already exhibits the target patterns (categorized index, stable per-item IDs,
per-document PDFs, a tested Python toolkit, requirements-checking CI). Much of
the work here is porting and adapting that proven system.

## The vision (what "done" means)

1. Reads as a curated anthology, **not** a blog — categorized table of contents,
   stable per-essay IDs, no date-driven navigation.
2. Owns 100% of its images: yours, or AI-generated with full rights. **Zero
   external image dependencies.**
3. No broken links (internal or external), enforced in CI.
4. Complete, accurate, schema-valid metadata on every essay.
5. Strong Google indexing posture (structured data, sitemap, canonical URLs,
   social cards, preserved legacy redirects).
6. Robust cross-references between sibling essays and robust citation of
   external sources.
7. A PDF of every published essay; eventually a curated subset published as a
   book on Amazon KDP.
8. A **tested Python toolkit** (`scripts/`) + **pytest suite** (`tests/`) that
   *proves* every goal above. `pytest` green == publication-ready.

## Guiding principles

- **Mechanical edits only — never rewrite the author's prose.** Fix WordPress
  residue, links, images, structure, and metadata. Do **not** improve, modernize,
  rephrase, or "tighten" sentences. The only prose changes allowed are repairs to
  text that migration physically broke (truncation, doubled passages, mojibake),
  and even those should be **flagged for human review**, not silently applied.
  These are period pieces; preserve the voice.
- **Own every image.** Never reintroduce an external image URL. See the image
  workflow below.
- **IDs are permanent.** Once an essay has an `item_id`, it never changes — not
  when the filename, slug, category, or status changes. See
  [docs/conventions.md](docs/conventions.md).
- **Every quality goal is a script + a test.** When you add a capability, add the
  fixer script in `scripts/` *and* the prover test in `tests/`. CI runs the tests
  and the `--check-only` mode of the scripts.
- **Preserve legacy SEO.** The `redirect_from` entries in frontmatter map old
  WordPress URLs to current pages; they carry the site's existing search equity.
  Never drop them.
- **Surface, don't guess.** If a referenced tool, fixture, or convention is
  missing or contradicts what's described here, stop and ask — don't improvise a
  replacement.
- **Keep the repo free of Dependabot alerts.** A clean security tab is a standing
  hygiene goal, not a one-off. After any push, check
  `gh api repos/dhh1128/codecraft.co/dependabot/alerts --jq '.[] | select(.state=="open")'`;
  if anything is open, triage and fix it (bump the dependency to its first
  patched version) rather than letting it linger. When authoring or editing a
  GitHub Actions workflow, pin actions to a non-vulnerable, `node24`-runtime
  version up front so you don't create a new alert. Verify a tag's runtime with
  `curl -sL https://raw.githubusercontent.com/<org>/<action>/<tag>/action.yml | grep -E '^\s*using:'`
  (want `node24`, `composite`, or `docker` — never `node20`).

## Decisions already made (do not relitigate without the author)

- **Images:** handled case-by-case — `own` / `generate` / `redraw` / `drop`.
  Not a bulk transform. Driven by a triage manifest (see workflow).
- **Reader comments:** kept in frontmatter but rendered as a collapsed appendix
  at the end of each essay. Pure pingback/trackback/spam comments may be removed;
  genuine human comments are preserved.
- **Prose:** mechanical fixes only (see principle above).
- **Archive scope:** the public site is itself curated. Three tiers expressed in
  frontmatter `status`: cleaned → `published` → `book: true`. Retired essays stay
  in the repo and git history but are excluded from the index, sitemap, and PDFs.

## Open questions (decide when relevant, don't assume)

- **Publishing platform.** The site currently builds with **Jekyll** on GitHub
  Pages (no `Gemfile` — it uses Pages' built-in Jekyll, so there are no Ruby gem
  dependencies for Dependabot to track; the only dependency surface is the
  Actions workflows). Jekyll is blog-oriented; the author is migrating newer
  static sites to **Zensical** (an actively-maintained successor to MkDocs,
  MkDocs-API-compatible, more publication- than blog-oriented). A Zensical
  migration is under consideration for this repo — see `../tti/home` for a
  working example (`requirements.txt` pins `zensical`, `build.sh` runs
  `zensical build`, published via `.github/workflows/publish.yml`). Not decided;
  do not migrate without an explicit decision. Note this is **orthogonal** to
  dependency hygiene — the link-check action must be kept current regardless of
  the SSG.

## Repository layout

```
*.md                 essays (one file per essay; slug == filename)
index.md / README.md  table of contents (README currently a flat list; to be replaced)
assets/              owned images (target: ALL images live here)
_layouts/            Jekyll layouts (default.html renders essays + comments)
_includes/           Jekyll partials
_config.yml          Jekyll config (minimal remote theme, plugins)
scripts/             durable maintenance/polish toolkit (Python) — see scripts/README.md
tests/               pytest suite that proves the goals — see tests/README.md
docs/                conventions (frontmatter schema, item-id convention)
tools/               LEGACY one-shot migration scripts (1convert.py…). Do not
                     extend; new tooling goes in scripts/.
.github/workflows/   CI (link-check today; requirements-check to be added)
ROADMAP.md           the tickable project plan
```

## Frontmatter schema (summary)

Canonical definition in [docs/conventions.md](docs/conventions.md). In brief,
each essay's YAML frontmatter should carry: `title`, `date` (original
publication), `slug`, `redirect_from`, `item_id`, `category`, `keywords`,
`abstract`, `version`, `revision_date`, `status` (`published` | `retired`),
optional `book: true`, optional `series`, and the existing `comments` list.

## Image workflow (case-by-case)

1. `scripts/inventory_images.py` → writes `assets/image-triage.yml`: one row per
   external `<img>` (essay, line, URL, host, alt-text, alive/dead, blank
   `disposition`).
2. A human or AI fills `disposition` per image: `own` (download & localize),
   `generate` (AI replacement + prompt seed), `redraw` (→ owned diagram), or
   `drop` (remove tag, reflow prose).
3. `scripts/apply_image_triage.py` executes the manifest.
4. `assets/CREDITS.yml` records provenance/rights for every final image (origin,
   license, and generation model+prompt if AI-made).
5. Generated art follows the house style guide so the anthology stays cohesive.

## How to add or edit an essay

1. Make only mechanical/structural/metadata changes (see principles).
2. Keep frontmatter schema-valid (`scripts/validate_frontmatter.py`).
3. Never introduce external image URLs; route images through the workflow above.
4. Run `pytest` before committing; CI is the backstop.

## Conventions for AI collaborators

- Commit messages: sign off with `-s` (the author works in DCO-enforced repos).
- New/edited GitHub Actions: pin actions to their `node24`-runtime versions
  (`actions/checkout@v4` and friends default to deprecated `node20`).
- When unsure about scope, the taxonomy, or whether a change counts as "prose",
  ask rather than guess.
