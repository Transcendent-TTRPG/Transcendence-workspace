#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
VENV_PYTHON="$ROOT_DIR/.venv/bin/python"
INDEXER="$ROOT_DIR/pipeline/scripts/index.py"
PUBLICATIONS="$ROOT_DIR/Transcendence-publications"

if [ ! -x "$VENV_PYTHON" ]; then
  echo "Error: $VENV_PYTHON not found or not executable."
  echo "Create the local virtual environment first:"
  echo "  python3 -m venv .venv"
  echo "  .venv/bin/pip install pyyaml"
  exit 1
fi

exec "$VENV_PYTHON" "$INDEXER" --repo-path "$PUBLICATIONS" --validate
