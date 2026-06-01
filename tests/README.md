# tests/

The pytest suite that **proves** the collection meets its publication goals.
`pytest` green is the definition of "publication-ready": no broken links, no
external images, complete and valid metadata, a fresh index, robust cross-refs
and citations, sound SEO posture, and current PDFs.

Each test corresponds to a fixer script in [`../scripts`](../scripts); see the
M7 table in [../ROADMAP.md](../ROADMAP.md). Tests should run against the whole
corpus and fail loudly with the specific essays/fields at fault.

Run locally:

```
pip install -r ../requirements.txt
pytest
```

CI runs this suite plus the `--check-only` mode of the scripts.
