#!/usr/bin/env python3
"""Assemble the canonical root essays into a Zensical / MkDocs source tree.

The root-level ``*.md`` essays stay the canonical source. This script derives a
complete build tree from them (the inverse of how Jekyll consumed them in place):

    build/mkdocs.yml
    build/docs/<slug>.md                      one page per published essay
    build/docs/index.md                       anthology table of contents
    build/docs/assets/...                     images (copied from repo assets/)
    build/docs/stylesheets/extra.css          the author's fonts / colours / print rules
    build/docs/<legacy-path>/index.html       redirect stubs preserving WordPress URLs

The build tree is a disposable artifact (gitignored); regenerate any time with
``python scripts/build_site.py`` (or via ``build.sh``). Mirrors the assembler
pattern in ../tti/home/assemble.py.

Design notes:
- Reader comments live in essay frontmatter; here they are rendered as a
  collapsed admonition appended under an "Original discussion" heading (the
  Zensical equivalent of the old Jekyll <details> appendix).
- Legacy ``redirect_from`` URLs are preserved as self-contained meta-refresh
  HTML stubs rather than via the mkdocs-redirects plugin — Zensical's
  mkdocs-plugin compatibility is narrow, so we don't depend on it.
- Page frontmatter is slimmed to what MkDocs needs (title, tags); Jekyll-only
  keys (date, slug, item_id, redirect_from, raw comments) are dropped.
"""
import os
import re
import json
import shutil
import sys

import yaml

# --- taxonomy → reading-order sections (provisional; M4 refines TOC) ----------
# Grouped by each essay's FIRST tag (its centre of gravity, per conventions.md).
SECTION_ORDER = [
    ("craft", "Craft"),
    ("languages", "Languages"),
    ("systems", "Systems"),
    ("strategy", "Strategy"),
    ("process", "Process"),
    ("comm", "Communication"),
    ("org", "Organization"),
    ("ux", "User Experience"),
    ("learning", "Learning"),
    ("meta", "Reflections"),
]
SECTION_TITLE = dict(SECTION_ORDER)

SITE = dict(
    name="Codecraft",
    description="software = science + art + people",
    url="https://codecraft.co/",
    repo_url="https://github.com/dhh1128/codecraft.co",
    repo_name="dhh1128/codecraft.co",
)

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)

# A "← back" link to the TOC at the top of every essay (mirrors ../papers).
# Print-hidden via the .back-link rule in zensical-extra.css; not added to the index.
BACK_LINK = '<p class="back-link"><a href="/">&larr; back</a></p>'


def parse(path):
    """Return (frontmatter dict, body str) for an essay file."""
    text = open(path, encoding="utf-8").read()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, m.group(2)


def iter_essays(root):
    """Yield dicts for every PUBLISHED essay (has item_id, not retired)."""
    out = []
    for name in sorted(os.listdir(root)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(root, name)
        fm, body = parse(path)
        if not fm or "item_id" not in fm:
            continue  # AGENTS.md / README.md / ROADMAP.md / CLAUDE.md
        if fm.get("status") == "retired":
            continue
        slug = fm.get("slug") or name[:-3]
        out.append(dict(path=path, name=name, slug=slug, fm=fm, body=body))
    return out


def render_comments(comments):
    """Render reader comments as a collapsed admonition block."""
    lines = ["", "## Original discussion", "",
             f'??? quote "{len(comments)} comment(s)"']
    for c in comments:
        author = c.get("author", "?")
        date = c.get("date", "")
        lines.append(f"    **{author}** · {date}")
        lines.append("")
        for line in str(c.get("comment", "")).strip().split("\n"):
            lines.append(f"    {line}")
        lines.append("")
    return "\n".join(lines)


def slim_frontmatter(fm):
    """Keep only what a MkDocs page needs."""
    page = {"title": fm["title"]}
    if fm.get("tags"):
        page["tags"] = list(fm["tags"])
    return page


def page_markdown(essay):
    """Full MkDocs page text for one essay."""
    fm = essay["fm"]
    page_fm = slim_frontmatter(fm)
    out = ["---", f'title: {json.dumps(page_fm["title"])}']
    if page_fm.get("tags"):
        out.append("tags:")
        out += [f"  - {t}" for t in page_fm["tags"]]
    out += ["---", "", BACK_LINK, "", essay["body"].rstrip()]
    comments = fm.get("comments") or []
    if comments:
        out.append(render_comments(comments))
    return "\n".join(out).rstrip() + "\n"


def redirect_html(target_url):
    """A self-contained meta-refresh stub preserving a legacy URL."""
    canonical = SITE["url"].rstrip("/") + target_url
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        f"<meta http-equiv=\"refresh\" content=\"0; url={target_url}\">\n"
        f"<link rel=\"canonical\" href=\"{canonical}\">\n"
        "<title>Redirecting…</title>\n</head>\n<body>\n"
        f"<p>This page has moved to <a href=\"{target_url}\">{target_url}</a>.</p>\n"
        "</body>\n</html>\n"
    )


def _section_key(essay):
    tags = essay["fm"].get("tags") or []
    return tags[0] if tags else "meta"


def build_nav(essays):
    """nav: grouped by first tag, sections in reading order, essays by date."""
    by_section = {}
    for e in essays:
        by_section.setdefault(_section_key(e), []).append(e)
    nav = [{"Home": "index.md"}]
    for key, title in SECTION_ORDER:
        items = by_section.get(key, [])
        if not items:
            continue
        items.sort(key=lambda e: (str(e["fm"].get("date", "")), e["slug"]))
        nav.append({title: [f"{e['slug']}.md" for e in items]})
    return nav


def build_index(essays):
    """Anthology table of contents (provisional — M4 will refine)."""
    by_section = {}
    for e in essays:
        by_section.setdefault(_section_key(e), []).append(e)
    out = [
        "# Codecraft",
        "",
        "A collection of essays on software architecture and the craft of "
        "programming, by Daniel Hardman.",
        "",
    ]
    for key, title in SECTION_ORDER:
        items = by_section.get(key, [])
        if not items:
            continue
        items.sort(key=lambda e: (str(e["fm"].get("date", "")), e["slug"]))
        out.append(f"## {title}")
        out.append("")
        for e in items:
            out.append(f"- [{e['fm']['title']}]({e['slug']}.md)")
        out.append("")
    body = "\n".join(out).rstrip()
    # Wrap in .toc-index so the homepage list spacing can be tightened in CSS
    # (md_in_html renders the Markdown inside the div).
    return f'<div class="toc-index" markdown="1">\n\n{body}\n\n</div>\n'


def build_mkdocs_config(essays):
    return {
        "site_name": SITE["name"],
        "site_description": SITE["description"],
        "site_url": SITE["url"],
        "site_author": "Daniel Hardman",
        "copyright": "Content licensed CC BY 4.0 unless otherwise noted.",
        "theme": {
            "name": "material",
            "favicon": "assets/favicon.png",
            "features": [
                "navigation.sections",
                "navigation.top",
                "navigation.indexes",
                "content.code.copy",
                "search.highlight",
                "search.suggest",
                "toc.follow",
            ],
        },
        "extra_css": ["stylesheets/extra.css"],
        "markdown_extensions": [
            "admonition",
            "pymdownx.details",
            "attr_list",
            "md_in_html",
            {"toc": {"permalink": True}},
        ],
        "plugins": ["search", "tags"],
        "nav": build_nav(essays),
    }


def assemble(root, out_dir):
    """Generate the full build tree. Returns a summary dict."""
    docs = os.path.join(out_dir, "docs")
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(docs)

    essays = iter_essays(root)

    # one page per essay
    for e in essays:
        with open(os.path.join(docs, f"{e['slug']}.md"), "w", encoding="utf-8") as fh:
            fh.write(page_markdown(e))

    # index / TOC
    with open(os.path.join(docs, "index.md"), "w", encoding="utf-8") as fh:
        fh.write(build_index(essays))

    # images and other owned assets
    src_assets = os.path.join(root, "assets")
    if os.path.isdir(src_assets):
        shutil.copytree(src_assets, os.path.join(docs, "assets"),
                        ignore=shutil.ignore_patterns("css", "*.scss", "*.yml"))

    # styling
    css_src = os.path.join(root, "assets", "css", "zensical-extra.css")
    css_dst_dir = os.path.join(docs, "stylesheets")
    os.makedirs(css_dst_dir, exist_ok=True)
    shutil.copyfile(css_src, os.path.join(css_dst_dir, "extra.css"))

    # root static files that must land at the published site root (MkDocs copies
    # non-.md files from docs/ verbatim). CNAME preserves the custom domain.
    for static in ("CNAME", "robots.txt"):
        src = os.path.join(root, static)
        if os.path.isfile(src):
            shutil.copyfile(src, os.path.join(docs, static))

    # legacy redirect stubs (preserve WordPress SEO equity)
    redirects = 0
    for e in essays:
        target = f"/{e['slug']}/"
        for legacy in e["fm"].get("redirect_from") or []:
            rel = legacy.strip().lstrip("/").rstrip("/")
            if not rel:
                continue
            stub_dir = os.path.join(docs, *rel.split("/"))
            os.makedirs(stub_dir, exist_ok=True)
            with open(os.path.join(stub_dir, "index.html"), "w", encoding="utf-8") as fh:
                fh.write(redirect_html(target))
            redirects += 1

    # mkdocs.yml
    cfg = build_mkdocs_config(essays)
    with open(os.path.join(out_dir, "mkdocs.yml"), "w", encoding="utf-8") as fh:
        yaml.safe_dump(cfg, fh, sort_keys=False, allow_unicode=True, default_flow_style=False)

    return {"essays": len(essays), "redirects": redirects, "out_dir": out_dir}


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "build")
    summary = assemble(root, out_dir)
    print(f"Assembled {summary['essays']} essays + {summary['redirects']} "
          f"redirect stubs into {summary['out_dir']}")


if __name__ == "__main__":
    main()
