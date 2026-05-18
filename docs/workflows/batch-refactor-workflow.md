# Batch Refactor Workflow

This document defines the canonical workflow for large, multi-artifact refactor
passes in Transcendence.

Its purpose is to support work that is too broad for a single isolated
artifact workflow, but still needs to remain disciplined and auditable.

Typical examples:
- retroactive species simulator backfill
- family-wide doctrine cleanup
- migrating many Techniques away from duplicated ailment text
- standardizing a procedural state family across multiple species
- reclassifying many files after an authority revision

## Purpose

Use this workflow when:
- the same kind of change must be applied across many artifacts
- a refactor spans authority, simulator, and sometimes publication
- a repeated inconsistency has accumulated over time
- the project needs a systematic migration, not a one-off edit

This workflow is about sequencing, grouping, and closure discipline.

## Relationship to other workflows

This workflow does not replace the more focused workflows.

Instead, it coordinates them at scale.

Inside one batch refactor you may still need:
- authority revision
- dependency review
- technique passes
- simulation-port passes
- core sync passes
- species audits

The batch workflow exists so these do not happen as untracked scattered edits.

## Required layers

Every batch refactor should rely on:
- the `Knowledge Layer`
- explicit grouping logic
- explicit dependency and coverage tracking
- clear migration criteria

## Core lenses

### `dependency_lens`
Checks:
- which changes are blocked by the same upstream dependency
- which artifacts must move together
- where the batch should be split into sub-batches

### `continuity_lens`
Checks:
- whether the refactor is preserving intended meaning
- whether earlier migrated entries still match later ones
- whether the migration rule is staying consistent

### `simulation_lens`
Checks:
- whether simulator coverage is being represented honestly during the migration
- whether the batch is improving shared runtime surfaces rather than adding one-off hacks

### `editorial_lens`
Checks:
- whether repeated wording is being cleaned consistently
- whether publication sync debt is being created or reduced

### `balance_lens`
Checks:
- whether the migration accidentally changes pressure, cost, or tactical shape
- whether the refactor is purely structural or functionally significant

### `species_lens`
Checks:
- whether species identity remains intact across many migrated entries
- whether the batch is flattening distinct species voices unintentionally

## Batch outcome classifications

Every batch refactor should end with one primary outcome:

- `completed`
- `partially_completed`
- `blocked_by_dependency`
- `re-scoped`

### Meanings

#### `completed`
The targeted migration rule was applied consistently across the intended batch.

#### `partially_completed`
Part of the batch closed, but part remains explicitly pending.

#### `blocked_by_dependency`
The batch cannot continue honestly until another rule family or subsystem is stabilized.

#### `re-scoped`
The original batch definition was too broad or badly shaped and had to be split or narrowed.

## Phase order

## Phase 0. Intake

Inputs:
- the migration or cleanup goal
- the artifact population it may affect
- reason the batch exists now

Outputs:
- batch work card
- intended migration rule
- initial artifact universe

## Phase 1. Refactor Rule Definition

Primary lenses:
- `system_lens`
- `continuity_lens`

Questions:
- What exact transformation is being applied?
- What should remain unchanged?
- What counts as in-scope?
- What counts as out-of-scope?

Outputs:
- refactor rule
- invariant list
- in-scope / out-of-scope definition

This phase is critical. Without it, a batch becomes a drifting collection of
similar-but-not-identical edits.

## Phase 2. Population Mapping

Primary lenses:
- `dependency_lens`
- `continuity_lens`

Questions:
- Which artifacts are candidates?
- Which are definitely affected?
- Which only look similar but should stay out?
- Which groups share the same blocker or migration path?

Outputs:
- candidate inventory
- affected inventory
- grouped batch map

## Phase 3. Dependency and Blocker Review

Primary lenses:
- `dependency_lens`
- `simulation_lens`
- `editorial_lens`

Questions:
- What shared blockers affect the batch?
- Which artifacts can migrate now?
- Which must wait for authority or runtime work?
- Should the batch be split into phases?

Outputs:
- blocker map
- immediate batch
- deferred batch
- sub-batch structure if needed

## Phase 4. Sequencing Plan

Primary lenses:
- `dependency_lens`
- `species_lens`
- `simulation_lens`

Questions:
- In what order should grouped artifacts move?
- Should the refactor proceed:
  - by species
  - by subsystem
  - by state family
  - by runtime surface
- What order minimizes rework and ambiguity?

Outputs:
- batch sequence
- sequencing rationale

## Phase 5. Pilot Slice

Before changing the whole population, run a small representative slice.

Questions:
- Does the migration rule behave as expected on a small set?
- Are there hidden exceptions?
- Is the current batch definition too broad?

Outputs:
- pilot result
- adjusted migration rule if needed

This phase helps prevent large noisy rework later.

## Phase 6. Batch Integration

Execute the refactor across the current in-scope slice.

Possible surfaces:
- authority docs
- authority data
- simulator data
- runtime
- publication docs
- coverage or state registries

The key requirement is consistency with the batch rule, not speed.

## Phase 7. Validation

Validation may include:
- consistency checks across the migrated set
- loader or runtime checks
- simulator scenario or question checks
- wording consistency review
- species identity review

Outputs:
- validated migrated slice
- exception list

## Phase 8. Residual Exception Review

Primary lenses:
- `dependency_lens`
- `continuity_lens`

Questions:
- Which artifacts still do not fit the batch rule?
- Are they valid exceptions?
- Or are they signs the migration rule needs refinement?

Outputs:
- explicit exception list
- valid exception notes
- unresolved anomaly list

## Phase 9. Coverage and State Update

Update the appropriate tracking surfaces:
- coverage records
- project state
- porting plans
- audit notes
- migration notes

Outputs:
- refreshed state records

## Phase 10. Acceptance Closure

A batch refactor should only be considered closed when:
- the migration rule was explicit
- the affected population was mapped
- the migrated slice was validated
- exceptions were recorded
- deferred work was explicit

Suggested closure checklist:
- `refactor_rule_recorded`
- `population_mapped`
- `blockers_classified`
- `pilot_completed`
- `batch_slice_integrated`
- `validation_done`
- `exceptions_recorded`
- `state_updated`
- `pending_items_explicit`

## Phase 11. Change Impact Record

Every batch refactor should record:
- migration rule
- artifact population touched
- blockers encountered
- exceptions discovered
- what future work became easier or newly necessary

## Good outputs

A good batch refactor leaves behind:
- fewer repeated inconsistencies
- a more uniform artifact population
- clearer tracking
- less hidden drift across files

## Bad outputs

A bad batch refactor leaves behind:
- many similar edits with no explicit migration rule
- half-migrated populations with no exception log
- hidden blockers that were ignored rather than classified
- a new layer of inconsistency introduced by the refactor itself

## Relationship to other workflows

This workflow complements:
- [Authority Revision Workflow](./authority-revision-workflow.md)
- [Dependency Review Workflow](./dependency-review-workflow.md)
- [Balance Review Workflow](./balance-review-workflow.md)
- [Status Family Workflow](./status-family-workflow.md)
- [Technique Workflow](./technique-workflow.md)
- [Simulation Port Workflow](./simulation-port-workflow.md)
- [Species Audit Workflow](./species-audit-workflow.md)

Use this workflow when the work unit is a coordinated migration or cleanup
across many artifacts rather than one local artifact pass. 
