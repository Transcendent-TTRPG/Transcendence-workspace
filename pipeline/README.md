# Transcendence Editorial Pipeline

This directory contains the infrastructure for producing prose that sounds human, remains canonically consistent, and can be maintained across a bilingual TTRPG corebook and novel line.

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
| `scripts/editorial-check.sh` | Run the standard editorial QA pass |
| `workflow.md` | Official working sequence for publications files |
| `manifest.json` | Generated — searchable index of all publications files |

## Quick start

```bash
# Create local virtual environment once
python3 -m venv .venv
.venv/bin/pip install pyyaml

# Scan publications and build manifest
.venv/bin/python pipeline/scripts/index.py --repo-path Transcendence-publications

# Find missing frontmatter (dry run)
.venv/bin/python pipeline/scripts/index.py --repo-path Transcendence-publications --dry-run

# Add missing frontmatter automatically
.venv/bin/python pipeline/scripts/index.py --repo-path Transcendence-publications --fix

# Find related files before editing a combat chapter
.venv/bin/python pipeline/scripts/index.py \
  --repo-path Transcendence-publications \
  --search '{"tags": ["combat", "atb"], "chapter": 10, "language": "es"}'

# Run the standard editorial QA pass
./pipeline/scripts/editorial-check.sh

# Or, if using make
make editorial-check
```

## Metadata model

- `type` identifies the publication container: `corebook`, `novel`, `supplement`, `canon`, `template`, `admin`, `design`
- `content_kind` identifies the editorial function inside that container: `introduction`, `rules`, `lore`, `narrative`, `reference`, `template`, `admin`
- `writing_mode` identifies the dominant writing mode of the file
- `section_modes` is optional and exists for mixed files where specific sections intentionally diverge from the dominant mode
- Legacy values such as `type: rules` and `type: introduction` are still normalized by the indexer, but they should be migrated over time

## Workflow for prose tasks

See `SKILLS.md` for the full workflow. The short version:

1. Run search to find related files
2. Read: `canon/style-guide.md` + `canon/glossary.md` + `canon/voice-samples.md`
3. Read the target file + related files
4. Edit following the constraints in SKILLS.md §prose-editor

See also: `pipeline/workflow.md`

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
| Frontmatter on existing files | Enforced — validation passes with mandatory corebook metadata |
