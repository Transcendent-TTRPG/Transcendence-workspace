#!/usr/bin/env python3
"""
index.py — Editorial pipeline indexer for Transcendence-publications.

Scans all .md files, validates frontmatter, optionally adds missing metadata,
and builds a searchable manifest.json for context retrieval.

Usage:
  # Build manifest
  python3 pipeline/scripts/index.py --repo-path Transcendence-publications

  # Add missing frontmatter (dry run first, then --fix)
  python3 pipeline/scripts/index.py --repo-path Transcendence-publications --dry-run
  python3 pipeline/scripts/index.py --repo-path Transcendence-publications --fix

  # Search for related files before editing
  python3 pipeline/scripts/index.py --repo-path Transcendence-publications \\
    --search '{"tags": ["combat", "atb"], "chapter": 10, "language": "es"}'

  # Validate all frontmatter fields
  python3 pipeline/scripts/index.py --repo-path Transcendence-publications --validate
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import date

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SKIP_DIRS = {".git", "node_modules", "__pycache__", "98-layout-export", "99-release"}
SKIP_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}

VALID_TYPES = {"corebook", "light-novel", "canon", "template", "admin", "design"}
VALID_LANGUAGES = {"es", "en", "both"}
VALID_STATUSES = {"draft", "review", "final", "locked"}

REQUIRED_FIELDS = ["title", "type", "language", "status", "canonical", "tags"]


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def read_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from markdown. Returns (metadata, body)."""
    if not content.startswith("---"):
        return {}, content
    match = re.match(r"^---\n(.*?)\n---\n?", content, re.DOTALL)
    if not match:
        return {}, content
    try:
        fm = yaml.safe_load(match.group(1)) or {}
        body = content[match.end():]
        return fm, body
    except yaml.YAMLError as e:
        print(f"  YAML parse error: {e}")
        return {}, content


def write_frontmatter(fm: dict, body: str) -> str:
    """Prepend YAML frontmatter to markdown body."""
    yaml_str = yaml.dump(
        fm,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    return f"---\n{yaml_str}---\n{body}"


# ---------------------------------------------------------------------------
# Metadata inference
# ---------------------------------------------------------------------------

def infer_type(filepath: Path, repo_root: Path) -> str:
    parts = filepath.relative_to(repo_root).parts
    if "canon" in parts:
        return "canon"
    if "core-books" in parts:
        return "corebook"
    if "light-novels" in parts:
        return "light-novel"
    if "templates" in parts:
        return "template"
    return "admin"


def infer_language(filepath: Path) -> str:
    path_str = str(filepath)
    if "/es/" in path_str:
        return "es"
    if "/en/" in path_str:
        return "en"
    return "both"


def infer_chapter(filepath: Path, repo_root: Path) -> int | None:
    for part in filepath.relative_to(repo_root).parts:
        if re.match(r"^\d{2}-", part):
            return int(part[:2])
    return None


def infer_section(filepath: Path) -> str:
    return filepath.stem


def infer_metadata(filepath: Path, repo_root: Path) -> dict:
    """Build a complete metadata dict inferred from file path."""
    file_type = infer_type(filepath, repo_root)
    return {
        "title": filepath.stem.replace("-", " ").title(),
        "type": file_type,
        "language": infer_language(filepath),
        "chapter": infer_chapter(filepath, repo_root),
        "section": infer_section(filepath),
        "status": "draft",
        "canonical": file_type == "canon",
        "tags": [],
        "related": [],
        "last-edited": str(date.today()),
    }


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_frontmatter(fm: dict, filepath: Path, repo_root: Path) -> list[str]:
    """Return list of validation error strings for this file's frontmatter."""
    errors = []
    rel = str(filepath.relative_to(repo_root))

    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"{rel}: missing required field '{field}'")

    if fm.get("type") and fm["type"] not in VALID_TYPES:
        errors.append(f"{rel}: invalid type '{fm['type']}' (valid: {VALID_TYPES})")

    if fm.get("language") and fm["language"] not in VALID_LANGUAGES:
        errors.append(f"{rel}: invalid language '{fm['language']}' (valid: {VALID_LANGUAGES})")

    if fm.get("status") and fm["status"] not in VALID_STATUSES:
        errors.append(f"{rel}: invalid status '{fm['status']}' (valid: {VALID_STATUSES})")

    if "related" in fm and not isinstance(fm["related"], list):
        errors.append(f"{rel}: 'related' must be a list")

    if "tags" in fm and not isinstance(fm["tags"], list):
        errors.append(f"{rel}: 'tags' must be a list")

    return errors


# ---------------------------------------------------------------------------
# Manifest building
# ---------------------------------------------------------------------------

def should_skip(filepath: Path) -> bool:
    for part in filepath.parts:
        if part in SKIP_DIRS:
            return True
    if filepath.name in SKIP_FILES:
        return True
    return False


def build_manifest(repo_root: Path, fix: bool = False, dry_run: bool = False) -> dict:
    """Scan all .md files and build a manifest. Optionally fix missing frontmatter."""
    manifest_entries = []
    missing_fm = []
    all_errors = []

    for md_file in sorted(repo_root.rglob("*.md")):
        if should_skip(md_file):
            continue

        content = md_file.read_text(encoding="utf-8")
        fm, body = read_frontmatter(content)
        has_frontmatter = bool(fm)

        inferred = infer_metadata(md_file, repo_root)
        merged = {**inferred, **fm}

        # Validate
        errors = validate_frontmatter(fm, md_file, repo_root)
        all_errors.extend(errors)

        # Fix missing frontmatter
        if not has_frontmatter:
            missing_fm.append(str(md_file.relative_to(repo_root)))
            if fix and not dry_run:
                md_file.write_text(write_frontmatter(inferred, content), encoding="utf-8")
                print(f"  [fixed] {md_file.relative_to(repo_root)}")
            elif dry_run:
                print(f"  [would fix] {md_file.relative_to(repo_root)}")

        entry = {
            "path": str(md_file.relative_to(repo_root)),
            "title": merged.get("title") or md_file.stem,
            "type": merged.get("type"),
            "language": merged.get("language"),
            "chapter": merged.get("chapter"),
            "section": merged.get("section"),
            "status": merged.get("status", "draft"),
            "canonical": bool(merged.get("canonical", False)),
            "tags": merged.get("tags") or [],
            "related": merged.get("related") or [],
        }
        manifest_entries.append(entry)

    return {
        "generated": str(date.today()),
        "files": manifest_entries,
        "missing_frontmatter": missing_fm,
        "validation_errors": all_errors,
    }


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

def search_manifest(manifest: dict, query: dict, limit: int = 5) -> list[str]:
    """
    Find relevant files from the manifest based on a query.

    Query fields (all optional):
      tags: list[str]      — files sharing any of these tags score higher
      type: str            — exact match on type
      language: str        — exact match on language
      chapter: int         — exact match on chapter
      exclude: list[str]   — file paths to exclude from results

    Returns up to `limit` file paths sorted by relevance score (descending).
    """
    query_tags = set(query.get("tags") or [])
    exclude = set(query.get("exclude") or [])
    results = []

    for entry in manifest.get("files", []):
        if entry["path"] in exclude:
            continue

        score = 0

        if query.get("type") and entry.get("type") == query["type"]:
            score += 3
        if query.get("language") and entry.get("language") == query["language"]:
            score += 2
        if query.get("chapter") is not None and entry.get("chapter") == query["chapter"]:
            score += 4
        if query_tags:
            entry_tags = set(entry.get("tags") or [])
            score += len(query_tags & entry_tags) * 2
        # Canonical files always get a boost (they are anchors)
        if entry.get("canonical"):
            score += 1

        if score > 0:
            results.append((score, entry["path"]))

    results.sort(reverse=True)
    return [path for _, path in results[:limit]]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Transcendence editorial pipeline indexer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--repo-path", required=True,
        help="Path to the Transcendence-publications directory",
    )
    parser.add_argument(
        "--fix", action="store_true",
        help="Add missing frontmatter to files that lack it",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what --fix would do without modifying files",
    )
    parser.add_argument(
        "--validate", action="store_true",
        help="Report all frontmatter validation errors",
    )
    parser.add_argument(
        "--output", default="pipeline/manifest.json",
        help="Output path for the manifest (default: pipeline/manifest.json)",
    )
    parser.add_argument(
        "--search",
        help='JSON query string, e.g. \'{"tags": ["combat"], "chapter": 10, "language": "es"}\'',
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_path).resolve()
    if not repo_root.exists():
        print(f"Error: path not found: {repo_root}")
        sys.exit(1)

    print(f"Scanning {repo_root} ...")
    manifest = build_manifest(repo_root, fix=args.fix, dry_run=args.dry_run)

    total = len(manifest["files"])
    missing = len(manifest["missing_frontmatter"])
    errors = len(manifest["validation_errors"])

    print(f"  {total} files scanned")
    print(f"  {missing} missing frontmatter")
    print(f"  {errors} validation errors")

    if args.validate and manifest["validation_errors"]:
        print("\nValidation errors:")
        for e in manifest["validation_errors"]:
            print(f"  {e}")

    if args.search:
        query = json.loads(args.search)
        results = search_manifest(manifest, query)
        print(f"\nRelevant files for query {args.search}:")
        for r in results:
            print(f"  {r}")
        return

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\nManifest written to {out_path}")


if __name__ == "__main__":
    main()
