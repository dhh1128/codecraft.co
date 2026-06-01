# scripts/

The durable maintenance & polish toolkit for the essay collection. Each script
should be **idempotent**, support a **`--check-only`** mode (so CI can assert the
goal without mutating files), and log clearly.

Every quality goal pairs a fixer here with a prover test in [`../tests`](../tests).
See the M7 table in [../ROADMAP.md](../ROADMAP.md) for the planned scripts:

- `validate_frontmatter.py` — metadata completeness & schema validity
- `inventory_images.py` / `apply_image_triage.py` — image ownership workflow
- `check_links.py`, `check_images.py`, `check_crossrefs.py`, `check_citations.py`
- `assign_ids.py` — permanent item-ID assignment
- `generate_index.py` — categorized table of contents
- `check_seo.py`, `build_pdfs.py`, `lint_wordpress.py`

Reference implementations for several of these exist in `../../papers/scripts/`
(`generate_index.py`, `pandoc.py`, `check_requirements.py`) and should be ported
and adapted, not reinvented.

> Note: `../tools/` holds **legacy one-shot migration scripts** from the original
> WordPress conversion. Do not extend them; new tooling lives here.
