# Conventions

Canonical definitions for this repository. Referenced by [AGENTS.md](../AGENTS.md).

## Frontmatter schema

Every essay is a Markdown file whose YAML frontmatter carries the fields below.
"Required" means CI (`scripts/validate_frontmatter.py`) will eventually enforce it.

| Field | Req | Type | Notes |
|---|---|---|---|
| `title` | ✓ | string | Display title. |
| `date` | ✓ | date | **Original** publication date (ISO 8601, date only). Drives ID ordinal and sort. |
| `slug` | ✓ | string | URL slug; equals the filename without `.md`. |
| `item_id` | ✓ | string | Permanent ID, `CC-XXX-YYMMOO` (see below). Assigned once, never changed. |
| `category` | ✓ | string | One of the frozen taxonomy categories (see Taxonomy below). |
| `status` | ✓ | enum | `published` or `retired`. Retired essays stay in the repo but are excluded from index/sitemap/PDFs. |
| `keywords` | ✓ | list/string | For SEO and PDF metadata. |
| `abstract` | ✓ | string | One-paragraph summary; feeds meta description and PDF subject. |
| `version` | ✓ | int | Bump on substantive revision. Defaults to 1. |
| `revision_date` | ✓ | date | Date of last substantive revision. |
| `redirect_from` | — | list | Legacy WordPress URLs. **Never remove** — carries SEO equity. |
| `book` | — | bool | `true` if selected for the print/Kindle book. |
| `series` | — | string | Name of a multi-part series, if any. |
| `comments` | — | list | Original reader comments (author/date/comment). Rendered as a collapsed appendix. |

Notes:
- The body must **not** repeat the title or abstract; the layout renders those.
- Mechanical-only editing rule applies to all body content (see AGENTS.md).

## Taxonomy

Every essay belongs to exactly one category. The category name is plain and
single-word; its code (first three characters, uppercased — with one documented
exception) forms the `XXX` segment of the item-id.

| Category | Code | Scope |
|---|---|---|
| Craft | `CRA` | What makes code good: quality attributes, simplicity, naming, comments. |
| Architecture | `ARC` | System design, risk, resilience, scaling, decoupling, the architect's role. |
| Languages | `LAN` | Programming-language design and mechanics. |
| People | `PEO` | Working with humans: influence, politics, courage, communication. |
| Learning | `LEA` | Personal growth, mental models, getting better; absorbs book reviews and mentor profiles. |
| UX | `UXD` | User experience and usability, incl. the Role-Play-Centered Design (RPCD) work. |
| Meta | `MET` | Why one writes, retrospectives, and personal reflection on the craft. |

Notes:
- **UX** is the one code exception: the name has two letters, so its code is
  `UXD` rather than a three-letter truncation.
- **Series.** Some coherent multi-essay threads are marked with a `series:`
  field rather than their own category:
  - `series: intent` — the language-design arc in **Languages** (Lacunas → Marks
    → Markedness → Deixis → Pointing).
  - `series: Mentors` — the "Name: lesson" profile essays in **Learning**.

## Item-ID convention

Each essay gets a stable, human-readable identifier:

**`CC-XXX-YYMMOO`** — for example `CC-CRA-120826`.

- `CC` — the Codecraft namespace.
- `XXX` — the category code from the Taxonomy table above (e.g. `CRA`, `ARC`,
  `LAN`, `PEO`, `LEA`, `UXD`, `MET`).
- `YY` — two-digit year of original publication.
- `MM` — two-digit month of original publication.
- `OO` — two-digit ordinal disambiguating items within that year/category.

The identifier is **permanent and immutable**. It refers to the conceptual work,
not to any representation (HTML, PDF) or to the filename/slug/URL. It does not
change when an essay is recategorized, retired, or revised. Versioning is handled
separately via the `version` field. Git hashes or UUIDs may be recorded as
internal provenance but are never the public ID.

This convention mirrors the sister `../papers` archive
(`.item-id-convention.md`) so the two collections are consistent.
