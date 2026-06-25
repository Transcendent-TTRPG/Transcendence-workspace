# Skills Index

This folder contains the current project-local skills for Transcendence work.

These skills are versioned in the workspace so they can be:

- shared across agents and collaborators
- reviewed in Git
- evolved together with workflows, knowledge, and simulator surfaces

Skills here are not meant to replace design judgment. They exist to make
repeatable work more structured, less ambiguous, and easier to close cleanly.

## How to use this folder

Use this index before choosing a skill.

Each skill should have:

- a clear owning workflow or workflow family
- a defined scope
- explicit routing rules for when the task belongs elsewhere
- closure criteria that prevent "almost done" states

If a skill does not reduce real repetition or does not yet map to an active
workflow, it should not stay in the active set.

## Current set

### Execution layer

Use this first when the main problem is workflow ownership, routing, or closure
discipline rather than the artifact work itself.

- [workflow-orchestrator](./workflow-orchestrator/SKILL.md)
  - selects the owning workflow, picks the work card, routes to artifact skills, and enforces closure

### Active technique pipeline

Use these first for the current production loop around Techniques.

- [technique-authoring](./technique-authoring/SKILL.md)
  - primary skill for authoring, revising, backfilling, or closing Techniques
- [technique-play-surface](./technique-play-surface/SKILL.md)
  - primary skill for converting a stable Technique into aligned core and card play-facing surfaces
- [technique-porting-to-sim](./technique-porting-to-sim/SKILL.md)
  - primary skill for translating authored Techniques into simulator coverage
- [corebook-sync](./corebook-sync/SKILL.md)
  - primary skill for synchronizing authority changes into publication surfaces
- [corebook-prose](./corebook-prose/SKILL.md)
  - primary skill for writing or revising prose in corebook publication files — flavor text, rules text, voice passes, bilingual alignment
- [corebook-description](./corebook-description/SKILL.md)
  - primary skill for writing or revising description-mode content — species, creatures, equipment, world/faction passages, cosmic horror ambiance
- [species-pass-audit](./species-pass-audit/SKILL.md)
  - primary skill for species-wide inventory, identity, coverage, and backlog review
- [species-cosmology-localization](./species-cosmology-localization/SKILL.md)
  - primary skill for revising chapter-06 species so they speak from species-local cosmology rather than chapter-12 objective metaphysics

### Base transversal

These are broader framework skills that support repeated families or future
systems, but are not the default first pick for a simple Technique task.

- [status-family-authoring](./status-family-authoring/SKILL.md)
  - trunk skill for repeated status-like families with shared grammar and inheritance

### Family-specific extensions

These are active only when the work is really about that family, not when the
work is about Techniques in general.

- [infection-authoring](./infection-authoring/SKILL.md)
  - infection-family boundary, vector, progression, treatment, and closure
- [poison-authoring](./poison-authoring/SKILL.md)
  - poison-family delivery, onset, dose, persistence, antidote, and closure

## Suggested selection order

For current Technique-centered work, the usual order is:

1. `workflow-orchestrator` when ownership or routing is not already obvious
2. `technique-authoring`
3. `technique-play-surface` when the Technique needs final core/card form
4. `technique-porting-to-sim`
5. `corebook-sync` if publication drift is affected after surface finalization
6. `species-pass-audit` when reviewing a whole species pass

Use `status-family-authoring` only when the work is truly about a repeated
family and not just one Technique.

Use `infection-authoring` or `poison-authoring` only when the family itself is
the owning scope.

For species work, the usual order is:

1. `species-design` when the concept itself is still unstable or incomplete
2. `species-corebook-authoring` when converting a stable design doc into a chapter-06 entry
3. `species-cosmology-localization` when a chapter-06 entry leaks chapter-12 truth or needs species-local doctrine / ritual vocabulary
4. `species-pass-audit` when reviewing closure, backlog, or drift across many species

## Governance rules

- Keep the active set small.
- Prefer one strong trunk skill over many overlapping narrow ones.
- Remove or defer skills that are not part of the current production pipeline.
- If a new system is not yet active, do not keep its skill in the active set
  just because it may be useful later.
- A skill should map to real repeated work, not hypothetical future work.

## Related docs

- [Workflow Overview](../docs/workflow-overview.md)
- [Workflow Execution](../docs/workflows/workflow-execution.md)
- [Technique Workflow](../docs/workflows/technique-workflow.md)
- [Simulation Port Workflow](../docs/workflows/simulation-port-workflow.md)
- [Core Sync Workflow](../docs/workflows/core-sync-workflow.md)
- [Species Audit Workflow](../docs/workflows/species-audit-workflow.md)
- [Status Family Workflow](../docs/workflows/status-family-workflow.md)
