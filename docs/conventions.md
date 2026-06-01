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
| `item_id` | ✓ | string | Permanent ID, `CC-YYMMOO` (see below). Assigned once, never changed. |
| `tags` | ✓ | list | One or more tags from the controlled vocabulary (see Tags below). First tag is the center of gravity. |
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

## Tags

Unlike the sister `../papers` archive (which uses mutually-exclusive
categories), essays are classified with **tags**: a controlled vocabulary where
each essay carries **one or more**. Essays genuinely span topics, so a single
category fights their nature; tags do not. Tags are deliberately *not* encoded in
the item-id, so they can be revised at any time without disturbing ids. The
authoritative per-essay mapping lives in `scripts/tags.yml`.

The vocabulary is bounded and defined (so tagging stays consistent). The **first
tag** in an essay's list is its center of gravity (useful for a primary grouping
in the index). Tags are grouped into families only for orientation:

| Family | Tag | The essay is mainly about… |
|---|---|---|
| Technical | `craft` | writing or shaping a unit of code well |
| | `systems` | how a system is structured and behaves (coupling, scale, failure, health) |
| | `languages` | a programming language's features, semantics, or design |
| Decisions | `strategy` | what to build, when, and what it costs (product, tech debt, economics, risk) |
| | `process` | how the work flows (delivery, cadence, measurement) |
| Human | `comm` | conveying meaning between people |
| | `org` | how a team or organization functions |
| Product | `ux` | the experience of those who use the software |
| Self | `learning` | the practitioner's own growth and thinking |
| Reflection | `meta` | reflection on the discipline itself (incl. what an architect is) |

**Series** are an orthogonal `series:` field for coherent multi-essay threads —
e.g. `intent` and `const-correctness` (languages), `Decoupling Interfaces`,
`Software Pain`, `Technical Debt`, `The Architect's Role`, `What Is Good Code`,
`Editors`, `Mentors`, `Reviews`, `RPCD`. A specific language such as C++ is also
treated as metadata (a finer tag), not a top-level concern.

## Item-ID convention

Each essay gets a stable, human-readable identifier:

**`CC-YYMMOO`** — for example `CC-120826`.

- `CC` — the Codecraft namespace.
- `YY` — two-digit year of original publication.
- `MM` — two-digit month of original publication.
- `OO` — two-digit ordinal within that month, ordered by (date, slug).

There is no category segment: topic is carried by `tags`, not the id. This is
deliberately simpler than the `../papers` ids (`CC-XXX-YYMMOO`). The two
collections coexist under the shared `CC` namespace and stay distinguishable
because papers ids always carry a 3-letter middle segment and essay ids never do.

The identifier is **permanent and immutable**. It refers to the conceptual work,
not to any representation (HTML, PDF) or to the filename/slug/URL. It does not
change when an essay is retagged, retired, or revised. Versioning is handled
separately via the `version` field. Git hashes or UUIDs may be recorded as
internal provenance but are never the public ID.
