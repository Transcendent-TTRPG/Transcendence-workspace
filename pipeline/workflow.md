---
title: "Editorial Workflow"
type: admin
content_kind: admin
language: both
status: draft
canonical: false
tags: [workflow, editorial, qa, pipeline]
related:
  - canon/corebook-writing-checklist.md
  - canon/text-modes.md
  - canon/style-guide.md
  - canon/world-facts.md
---

# Editorial Workflow

This is the official working sequence for files in `Transcendence-publications`.

Use it as the default flow unless a file type explicitly requires something stricter.

---

## Standard flow

1. Create the file from the closest template.
2. Fill frontmatter immediately.
3. Declare `type`, `content_kind`, and `writing_mode` before drafting.
4. If the file mixes modes intentionally, declare `section_modes` for the sections that diverge from the dominant mode.
5. Add the bilingual pair if the file belongs to the `corebook`.
6. Add initial `related` paths.
7. Load the required canon files for the task.
8. Draft in the correct mode.
9. Run editorial QA.
10. Fix issues before changing status.
11. Only then move the file to `review`, `final`, or `locked`.

---

## Required context by task

### Corebook rules

- `canon/text-modes.md`
- `canon/style-guide.md`
- `canon/glossary.md`
- `canon/voice-samples.md`
- `canon/corebook-writing-checklist.md`
- relevant ADR / YAML from `Transcendence-design`

### Corebook lore or atmosphere

- `canon/text-modes.md`
- `canon/style-guide.md`
- `canon/glossary.md`
- `canon/voice-samples.md`
- `canon/world-facts.md`
- `canon/corebook-writing-checklist.md`

### Fiction / novel

- `canon/fiction-guide.md`
- `canon/text-modes.md`
- `canon/style-guide.md`
- `canon/voice-samples.md`
- `canon/glossary.md`
- `canon/world-facts.md`

---

## Status policy

### `draft`

- free to iterate
- warnings may exist
- no claim of readiness

### `review`

- must pass editorial QA with zero validation errors
- must pass style and continuity gates applicable to the file
- should not carry unresolved structural ambiguity

### `final`

- same requirements as `review`
- plus project-owner approval
- no known continuity or terminology issues

### `locked`

- reserved for canonically stable files
- requires authority source or explicit design decision
- use only when the file should constrain downstream writing

---

## Editorial QA

Run:

```bash
./pipeline/scripts/editorial-check.sh
```

Or, if using `make`:

```bash
make editorial-check
```

If the file is rules-facing, also confirm its design authorities manually before promoting status.

---

## Authority references

For any file that defines or explains mechanics, add `authority_refs` in frontmatter whenever possible.

Use it to point at the design sources that justify the prose, for example:

- `Transcendence-design/docs/adr/...`
- `Transcendence-design/docs/system/...`
- `Transcendence-design/data/system/...`

This field is especially important before a rules file moves to `review` or beyond.
