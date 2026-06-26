---
name: "species-pipeline-orchestrator"
description: "Use when a species must be taken through the full authoring pipeline from rough notes or unstable concept to a finished chapter-06 species entry. This skill orchestrates concept design, canon-doc formalization, corebook authoring, cosmology localization, and final closure instead of treating them as unrelated steps."
---

# Species Pipeline Orchestrator

Use this skill when the real need is not just "design a species" or "rewrite one file,"
but to move a species cleanly through the full pipeline until it exists in the same shape
as the current chapter-06 entries.

This skill does not replace the species artifact skills. It coordinates them in the right
order, decides where the run should start, enforces the handoff points, and prevents the
species from getting stranded halfway between notes, canon doc, publication prose, and
species-local cosmology.

## When to use this skill

Use `$species-pipeline-orchestrator` when:

- the user has notes, discussion points, anatomy ideas, or a cultural base and wants to end
  with a real species file in chapter 06
- a species concept exists, but the team wants a disciplined start-to-finish species run
- a species was partially authored before and needs to be pushed through the remaining
  authoring stages without losing track of ownership
- the problem is "how do we take this species all the way through the current process?"

This skill is especially useful when:

- the concept phase and the publication phase have drifted apart
- people keep remembering the workflow from memory instead of from the repo
- a species is likely to need the now-standard cosmology-localization pass before closure

Do not use this skill when:

- only the concept discussion is needed and no formal authoring should begin
- only the design doc needs a small local revision
- only the chapter-06 prose needs a small local revision
- only the cosmology-localization pass is being run on an already-authored species
- the task is a cross-species audit rather than one species pipeline

In those cases, route directly to:

- `species-design`
- `species-corebook-authoring`
- `species-cosmology-localization`
- `species-pass-audit`

## Core responsibility

This skill owns the species pipeline as a run.

It decides:

1. where the species currently is
2. which species skill owns the current phase
3. what the next required handoff is
4. what must exist before the species can be considered closed for chapter 06

If those four things are not explicit, the species is not actually "in process" in a
reliable way.

## Required context

Before starting the run, load:

1. `skills/README.md`
2. the relevant species skill docs:
   - `skills/species-design/SKILL.md`
   - `skills/species-corebook-authoring/SKILL.md`
   - `skills/species-cosmology-localization/SKILL.md`
   - `skills/species-pass-audit/SKILL.md` only if closure review is needed

Then load only the species-local project files that actually exist for the target species:

- `Transcendence-design/docs/canon/species/<species>.md` if present
- `Transcendence-publications/core-books/transcendence-corebook/06-species/es/<nn>-<species>.md` if present
- any related notes or references the user explicitly points to

## Execution pattern

Treat each species run as a pipeline with explicit phase ownership.

### Phase 1 — Classify the current state

Before editing, determine which of these states the species is in:

- `notes_only`
  - rough notes, anatomy ideas, cultural anchor, no stable concept
- `concept_confirmed`
  - concept is stable enough, but no canon species doc exists yet
- `canon_only`
  - canon species doc exists, but no usable chapter-06 entry exists yet
- `corebook_draft`
  - chapter-06 entry exists, but still sounds too close to design-doc or chapter-12 voice
- `closure_pass`
  - chapter-06 entry is nearly done and needs final species-local audit

Do not begin by assuming the run starts at design. Start where the species actually is.

### Phase 2 — Choose the active owner skill

Use exactly one active owner at a time:

- `notes_only` -> `species-design`
- `concept_confirmed` -> canon species doc formalization in `Transcendence-design/docs/canon/species/`
- `canon_only` -> `species-corebook-authoring`
- `corebook_draft` -> `species-cosmology-localization`
- `closure_pass` -> `species-pass-audit` if a real closure review is needed

This skill remains the pipeline owner, but the active species skill owns the current phase.

### Phase 3 — Enforce the handoff outputs

Each phase must leave behind the artifact the next phase needs.

Required handoffs:

- after `species-design`
  - a stable species concept with animal base, cultural anchor, Tauma relationship,
    cross-species positioning, civilizational concept, and horror
- after canon formalization
  - a usable species design doc in `Transcendence-design/docs/canon/species/`
- after `species-corebook-authoring`
  - a chapter-06 species entry with prose sections and mechanical stats block
- after `species-cosmology-localization`
  - a chapter-06 entry that no longer sounds like it has read chapter 12 directly

If a handoff artifact is missing, do not pretend the next phase can proceed cleanly.

### Phase 4 — Default route for modern species entries

For the current project standard, assume this is the normal path unless the species is
already farther along:

1. `species-design`
2. canon species doc formalization
3. `species-corebook-authoring`
4. `species-cosmology-localization`
5. optional `species-pass-audit` for closure or backlog review

Important:

- the cosmology-localization pass is not an optional flavor tweak when the draft still
  speaks in chapter-12 truth voice
- the canon doc and the chapter-06 file are different artifacts with different jobs
- do not collapse them back into one step just because the species feels clear

### Phase 5 — Closure discipline

A species is not "done" for chapter 06 just because a file exists.

Before closing the run, confirm:

- the concept is stable
- the canon doc exists and matches the intended species identity
- the chapter-06 entry exists
- the prose sections feel like a real species entry rather than a design summary
- the cosmology speaks from species-local belief, ritual, practice, or fear
- the mechanical block is present and synchronized enough for the current pass

If any of those are false, close the current phase only, not the whole species pipeline.

## Quality rules

- Do not let `species-design` silently stand in for the full pipeline.
- Do not let chapter-06 drafting begin from unstable concept notes unless the run explicitly
  accepts that risk.
- Do not skip the canon-doc layer just because the prose is flowing well.
- Do not treat cosmology-localization as cosmetic; for the current prose standard, it is a
  structural phase.
- Prefer explicit state labels and handoff outputs over vague statements like "we more or
  less have the species."

## Suggested use

This skill is the right starting point when the user says things like:

- "vamos a crear esta especie desde mis apuntes"
- "tenemos la idea, llevémosla hasta el archivo final"
- "quiero que no se nos vuelva a perder el paso entre diseño y capítulo 06"
- "necesitamos el workflow completo de especies"
