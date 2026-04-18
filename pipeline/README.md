# Transcendence Editorial Pipeline

This directory contains the infrastructure for producing prose that sounds human, remains canonically consistent, and can be maintained across a bilingual TTRPG corebook and light novel series.

## Why this exists

AI-assisted writing defaults to generic patterns unless it has a specific voice anchor and targeted context. This pipeline solves that by:

1. Defining what context to load for each type of task (SKILLS.md)
2. Maintaining a canonical voice and glossary (publications/canon/)
3. Making every file searchable by metadata without requiring full embeddings (scripts/index.py)

## Files

| File | Purpose |
| --- | --- |
| `SKILLS.md` | Three editorial skills: prose-editor, rule-clarifier, continuity-checker |
| `schemas/metadata.yaml` | Frontmatter schema for all .md files |
| `scripts/index.py` | Scan, validate, fix frontmatter; build manifest; search |
| `manifest.json` | Generated — searchable index of all publications files |

## Quick start

```bash
# Install dependency
pip install pyyaml

# Scan publications and build manifest
python3 pipeline/scripts/index.py --repo-path Transcendence-publications

# Find missing frontmatter (dry run)
python3 pipeline/scripts/index.py --repo-path Transcendence-publications --dry-run

# Add missing frontmatter automatically
python3 pipeline/scripts/index.py --repo-path Transcendence-publications --fix

# Find related files before editing a combat chapter
python3 pipeline/scripts/index.py \
  --repo-path Transcendence-publications \
  --search '{"tags": ["combat", "atb"], "chapter": 10, "language": "es"}'
```

## Workflow for prose tasks

See `SKILLS.md` for the full workflow. The short version:

1. Run search to find related files
2. Read: `canon/style-guide.md` + `canon/glossary.md` + `canon/voice-samples.md`
3. Read the target file + related files
4. Edit following the constraints in SKILLS.md §prose-editor

## Workflow for rules tasks

1. Read `canon/glossary.md`
2. Read the relevant ADR from `Transcendence-design/docs/adr/`
3. Cross-check values against `Transcendence-design/data/system/`
4. Edit following SKILLS.md §rule-clarifier

## Implementation status

| Component | Status |
| --- | --- |
| `SKILLS.md` | Done |
| `schemas/metadata.yaml` | Done |
| `scripts/index.py` | Done |
| `canon/style-guide.md` | Skeleton — **needs voice content from project owner** |
| `canon/glossary.md` | Skeleton — needs expansion |
| `canon/voice-samples.md` | Skeleton — **needs approved prose samples** |
| Frontmatter on existing files | Pending — run `--fix` after style-guide is complete |
