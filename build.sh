#!/usr/bin/env bash
# Build the codecraft.co anthology with Zensical.
#
# Pipeline: assemble the root essays into a MkDocs source tree (build/), then
# run `zensical build` to produce build/site/. The build/ dir is disposable and
# gitignored — regenerate any time. Mirrors ../tti/home/build.sh.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if [[ ! -d .venv-demo ]]; then
  python3 -m venv .venv-demo
  ./.venv-demo/bin/pip install --quiet --upgrade pip
  ./.venv-demo/bin/pip install --quiet -r requirements.txt
fi

# Assemble Jekyll-style essays -> Zensical source tree.
./.venv-demo/bin/python scripts/build_site.py

# Build the static site (plain output; Zensical's colorized logs are noisy).
cd build
NO_COLOR=1 TERM=dumb "$ROOT/.venv-demo/bin/zensical" build

echo "Built $(find site -type f | wc -l) files at build/site/"
