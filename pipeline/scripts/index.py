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

VALID_TYPES = {"corebook", "novel", "supplement", "canon", "template", "admin", "design"}
VALID_LANGUAGES = {"es", "en", "both"}
VALID_STATUSES = {"draft", "review", "final", "locked"}
VALID_CONTENT_KINDS = {"introduction", "rules", "lore", "narrative", "reference", "template", "admin"}
VALID_WRITING_MODES = {"rules", "example", "description", "narrative", "flavor", "reference"}

COREBOOK_MODE_COMPATIBILITY = {
    "rules": {"rules"},
    "introduction": {"description", "reference"},
    "reference": {"reference"},
    "narrative": {"narrative"},
    "lore": {"description", "narrative", "flavor"},
}

LEGACY_TYPE_ALIASES = {
    "introduction": ("corebook", "introduction"),
    "rules": ("corebook", "rules"),
    "light-novel": ("novel", None),
}

REQUIRED_FIELDS = ["title", "type", "language", "status", "canonical", "tags"]

FORBIDDEN_STYLE_PHRASES = [
    "In the world of Transcendence,",
    "It is important to note that",
    "Additionally,",
    "Furthermore,",
    "This means that",
    "As a result,",
    "In other words,",
]


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def read_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from markdown. Returns (metadata, body)."""
    content = content.lstrip("\ufeff")
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
    if "novels" in parts or "light-novels" in parts:
        return "novel"
    if "supplements" in parts:
        return "supplement"
    if "templates" in parts:
        return "template"
    return "admin"


def infer_content_kind(filepath: Path, repo_root: Path) -> str | None:
    file_type = infer_type(filepath, repo_root)
    parts = filepath.relative_to(repo_root).parts

    if file_type == "template":
        return "template"
    if file_type == "admin":
        return "admin"
    if file_type == "corebook":
        if any(part.startswith("02-introduction") for part in parts):
            return "introduction"
        return "rules"
    return None


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
        "content_kind": infer_content_kind(filepath, repo_root),
        "writing_mode": None,
        "language": infer_language(filepath),
        "chapter": infer_chapter(filepath, repo_root),
        "section": infer_section(filepath),
        "status": "draft",
        "canonical": file_type == "canon",
        "tags": [],
        "related": [],
        "authority_refs": [],
        "section_modes": [],
        "last-edited": str(date.today()),
    }


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_frontmatter(fm: dict, filepath: Path, repo_root: Path) -> list[str]:
    """Return list of validation error strings for this file's frontmatter."""
    errors = []
    rel = str(filepath.relative_to(repo_root))

    normalized_type = fm.get("type")
    if normalized_type in LEGACY_TYPE_ALIASES:
        normalized_type = LEGACY_TYPE_ALIASES[normalized_type][0]

    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"{rel}: missing required field '{field}'")

    if normalized_type and normalized_type not in VALID_TYPES:
        errors.append(f"{rel}: invalid type '{fm['type']}' (valid: {VALID_TYPES})")

    if fm.get("language") and fm["language"] not in VALID_LANGUAGES:
        errors.append(f"{rel}: invalid language '{fm['language']}' (valid: {VALID_LANGUAGES})")

    if fm.get("status") and fm["status"] not in VALID_STATUSES:
        errors.append(f"{rel}: invalid status '{fm['status']}' (valid: {VALID_STATUSES})")

    if fm.get("content_kind") and fm["content_kind"] not in VALID_CONTENT_KINDS:
        errors.append(
            f"{rel}: invalid content_kind '{fm['content_kind']}' "
            f"(valid: {VALID_CONTENT_KINDS})"
        )

    if fm.get("writing_mode") and fm["writing_mode"] not in VALID_WRITING_MODES:
        errors.append(
            f"{rel}: invalid writing_mode '{fm['writing_mode']}' "
            f"(valid: {VALID_WRITING_MODES})"
        )

    if "section_modes" in fm and not isinstance(fm["section_modes"], list):
        errors.append(f"{rel}: 'section_modes' must be a list")
    elif "section_modes" in fm and isinstance(fm["section_modes"], list):
        for idx, section_mode in enumerate(fm["section_modes"], start=1):
            if not isinstance(section_mode, dict):
                errors.append(f"{rel}: section_modes entry #{idx} must be an object")
                continue
            heading = section_mode.get("heading")
            mode = section_mode.get("writing_mode")
            if not isinstance(heading, str) or not heading.strip():
                errors.append(f"{rel}: section_modes entry #{idx} must include a non-empty 'heading'")
            if mode not in VALID_WRITING_MODES:
                errors.append(
                    f"{rel}: section_modes entry #{idx} has invalid writing_mode "
                    f"'{mode}' (valid: {VALID_WRITING_MODES})"
                )

    if "related" in fm and not isinstance(fm["related"], list):
        errors.append(f"{rel}: 'related' must be a list")
    elif "related" in fm and isinstance(fm["related"], list):
        for related_path in fm["related"]:
            if not isinstance(related_path, str):
                errors.append(f"{rel}: related entry must be a string path")
                continue
            if not (repo_root / related_path).exists():
                errors.append(f"{rel}: related path does not exist '{related_path}'")

    if "authority_refs" in fm and not isinstance(fm["authority_refs"], list):
        errors.append(f"{rel}: 'authority_refs' must be a list")
    elif "authority_refs" in fm and isinstance(fm["authority_refs"], list):
        for authority_ref in fm["authority_refs"]:
            if not isinstance(authority_ref, str):
                errors.append(f"{rel}: authority_refs entry must be a string path")
                continue
            if authority_ref.startswith("Transcendence-design/"):
                workspace_root = repo_root.parent
                if not (workspace_root / authority_ref).exists():
                    errors.append(f"{rel}: authority ref does not exist '{authority_ref}'")
            elif not (repo_root / authority_ref).exists():
                errors.append(f"{rel}: authority ref does not exist '{authority_ref}'")

    if "tags" in fm and not isinstance(fm["tags"], list):
        errors.append(f"{rel}: 'tags' must be a list")

    language = fm.get("language")
    related = fm.get("related") if isinstance(fm.get("related"), list) else []
    is_corebook_file = normalized_type == "corebook" and "core-books" in filepath.relative_to(repo_root).parts

    if is_corebook_file and language in {"es", "en"}:
        if "content_kind" not in fm:
            errors.append(f"{rel}: corebook file must declare 'content_kind'")
        if "writing_mode" not in fm:
            errors.append(f"{rel}: corebook file must declare 'writing_mode'")
        content_kind = fm.get("content_kind")
        writing_mode = fm.get("writing_mode")
        if (
            content_kind in COREBOOK_MODE_COMPATIBILITY
            and writing_mode in VALID_WRITING_MODES
            and writing_mode not in COREBOOK_MODE_COMPATIBILITY[content_kind]
        ):
            allowed = sorted(COREBOOK_MODE_COMPATIBILITY[content_kind])
            errors.append(
                f"{rel}: writing_mode '{writing_mode}' is not allowed for "
                f"content_kind '{content_kind}' (allowed: {allowed})"
            )
        counterpart_language = "es" if language == "en" else "en"
        has_bilingual_pair = any(
            isinstance(path, str)
            and path.startswith("core-books/transcendence-corebook/")
            and f"/{counterpart_language}/" in path
            for path in related
        )
        if not has_bilingual_pair:
            errors.append(
                f"{rel}: corebook file in '{language}' must include a related entry "
                f"to its '{counterpart_language}' bilingual pair"
            )

    return errors


def normalize_metadata(fm: dict, inferred: dict) -> tuple[dict, list[str]]:
    """Normalize metadata without forcing an immediate repo-wide migration."""
    normalized = dict(fm)
    warnings = []

    raw_type = normalized.get("type")
    if raw_type in LEGACY_TYPE_ALIASES:
        mapped_type, mapped_content_kind = LEGACY_TYPE_ALIASES[raw_type]
        normalized["type"] = mapped_type
        if mapped_content_kind and not normalized.get("content_kind"):
            normalized["content_kind"] = mapped_content_kind
        warnings.append(
            f"legacy type '{raw_type}' normalized to type '{mapped_type}'"
            + (
                f" + content_kind '{mapped_content_kind}'"
                if mapped_content_kind else ""
            )
        )

    if not normalized.get("content_kind") and inferred.get("content_kind"):
        normalized["content_kind"] = inferred["content_kind"]

    if not normalized.get("writing_mode"):
        content_kind = normalized.get("content_kind") or inferred.get("content_kind")
        if content_kind in VALID_WRITING_MODES:
            normalized["writing_mode"] = content_kind

    return normalized, warnings


def validate_content_rules(fm: dict, body: str, filepath: Path, repo_root: Path) -> tuple[list[str], list[str]]:
    """Lightweight content validation for corebook workflow enforcement."""
    errors = []
    warnings = []
    rel = str(filepath.relative_to(repo_root))

    normalized_type = fm.get("type")
    if normalized_type in LEGACY_TYPE_ALIASES:
        normalized_type = LEGACY_TYPE_ALIASES[normalized_type][0]

    status = fm.get("status", "draft")
    content_kind = fm.get("content_kind")
    authority_refs = fm.get("authority_refs") if isinstance(fm.get("authority_refs"), list) else []
    section_modes = fm.get("section_modes") if isinstance(fm.get("section_modes"), list) else []
    body_lower = body.lower()

    if normalized_type != "corebook":
        return errors, warnings

    for phrase in FORBIDDEN_STYLE_PHRASES:
        if phrase.lower() in body_lower:
            message = f"{rel}: forbidden style phrase found '{phrase}'"
            if status in {"review", "final", "locked"}:
                errors.append(message)
            else:
                warnings.append(message)

    if content_kind == "rules":
        has_example_signal = any(
            token in body_lower
            for token in ["## example", "## ejemplo", "\nexample:", "\nejemplo:", "> example", "> ejemplo"]
        )
        if not has_example_signal:
            message = f"{rel}: rules file should include or explicitly signal an example"
            if status in {"review", "final", "locked"}:
                errors.append(message)
            else:
                warnings.append(message)

        if status in {"review", "final", "locked"} and not authority_refs:
            errors.append(f"{rel}: rules file at status '{status}' must include 'authority_refs'")

    for section_mode in section_modes:
        heading = section_mode.get("heading")
        if isinstance(heading, str) and heading.strip():
            heading_pattern = re.compile(rf"^##+\s+{re.escape(heading.strip())}\s*$", re.MULTILINE)
            if not heading_pattern.search(body):
                message = f"{rel}: section_modes heading not found in body '{heading.strip()}'"
                if status in {"review", "final", "locked"}:
                    errors.append(message)
                else:
                    warnings.append(message)

    return errors, warnings


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
    all_warnings = []

    for md_file in sorted(repo_root.rglob("*.md")):
        if should_skip(md_file):
            continue

        content = md_file.read_text(encoding="utf-8-sig")
        fm, body = read_frontmatter(content)
        has_frontmatter = bool(fm)

        inferred = infer_metadata(md_file, repo_root)
        normalized_fm, warnings = normalize_metadata(fm, inferred)
        merged = {**inferred, **normalized_fm}

        # Validate
        errors = validate_frontmatter(fm, md_file, repo_root)
        content_errors, content_warnings = validate_content_rules(merged, body, md_file, repo_root)
        all_errors.extend(errors)
        all_errors.extend(content_errors)
        rel_path = str(md_file.relative_to(repo_root))
        all_warnings.extend([f"{rel_path}: {warning}" for warning in warnings])
        all_warnings.extend(content_warnings)

        # Fix missing frontmatter
        if not has_frontmatter:
            missing_fm.append(rel_path)
            if fix and not dry_run:
                md_file.write_text(write_frontmatter(inferred, content), encoding="utf-8")
                print(f"  [fixed] {rel_path}")
            elif dry_run:
                print(f"  [would fix] {rel_path}")

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
            "authority_refs": merged.get("authority_refs") or [],
            "content_kind": merged.get("content_kind"),
            "writing_mode": merged.get("writing_mode"),
            "section_modes": merged.get("section_modes") or [],
        }
        manifest_entries.append(entry)

    return {
        "generated": str(date.today()),
        "files": manifest_entries,
        "missing_frontmatter": missing_fm,
        "validation_errors": all_errors,
        "warnings": all_warnings,
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
    warnings = len(manifest.get("warnings", []))

    print(f"  {total} files scanned")
    print(f"  {missing} missing frontmatter")
    print(f"  {errors} validation errors")
    print(f"  {warnings} warnings")

    if args.validate and manifest["validation_errors"]:
        print("\nValidation errors:")
        for e in manifest["validation_errors"]:
            print(f"  {e}")

    if args.validate and manifest.get("warnings"):
        print("\nWarnings:")
        for warning in manifest["warnings"]:
            print(f"  {warning}")

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
