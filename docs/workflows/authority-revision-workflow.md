# Authority Revision Workflow

This document defines the canonical workflow for revising rule authority in
Transcendence.

Use this workflow when the core problem is not merely:
- wording
- simulation coverage
- or publication sync

Instead, use it when the rule itself, its taxonomy, or its subsystem boundary
needs to change or be clarified.

## Purpose

Use this workflow when:
- a rule concept is ambiguous
- two authority files imply different things
- a subsystem boundary is unclear
- a doctrinal category needs to be revised
- a design contradiction has been discovered
- simulator or publication work is blocked by unstable authority

Examples:
- clarifying whether something is an ailment, a procedural state, or a concealment state
- revising how `Hidden` relates to concealment
- redefining a roll family or recovery route
- separating player wounds from creature zone damage

## Relationship to knowledge governance

This workflow should be read together with:
- `Transcendence-design/docs/knowledge/GOVERNANCE.md`

Authority revision is the highest-cost workflow in this set because it can
change downstream assumptions across:
- authority text
- authority data
- simulator abstractions
- publication wording
- knowledge registries

Therefore a revision should not be treated as a casual local edit when it
changes doctrine, taxonomy, or ownership boundaries.

## Required layers

Every authority revision should rely on:
- Tier 1 authority files
- Tier 2 architectural or doctrinal records when relevant
- the `Knowledge Layer`
- explicit dependency and continuity review

## Core lenses

### `system_lens`
Checks:
- what the rule currently claims
- what mechanic or taxonomy is really under question
- whether the proposed revision stays coherent with the wider system

### `dependency_lens`
Checks:
- what other subsystems depend on the rule
- what artifacts will require updates if the revision is accepted
- whether the revision would break current simulator or publication assumptions

### `continuity_lens`
Checks:
- prior decisions
- prior wording
- whether the revision is a true change or just a clearer statement of what was already intended

### `balance_lens`
Checks:
- whether the revision materially changes cost, pressure, survivability, or counterplay
- whether the change has practical downstream balance implications

### `simulation_lens`
Checks:
- what abstractions, normalized data, or runtime surfaces would be invalidated or improved
- whether the simulator is exposing a genuine authority weakness or merely a simulator limitation

### `editorial_lens`
Checks:
- whether the revision creates publication debt
- whether a simpler doctrinal statement is possible
- whether the revised rule can be explained consistently without duplication

## Revision outcome classifications

Every authority revision should end with one of these primary outcomes:

- `clarification_only`
- `taxonomy_revision`
- `mechanical_revision`
- `boundary_revision`
- `deferred_pending_evidence`

### Meanings

#### `clarification_only`
The intended rule was already stable. The work mainly clarifies wording,
terminology, or explicitness.

#### `taxonomy_revision`
The rule is reclassified or reorganized without necessarily changing its
mechanical outcome.

Examples:
- moving something out of ailments and into another state family
- redefining whether a concept belongs to concealment, wounds, or procedural state handling

#### `mechanical_revision`
The actual behavior changes.

Examples:
- changing how a roll is made
- changing duration or recovery structure
- changing what a state does

#### `boundary_revision`
The main change is to subsystem ownership or interface boundaries.

Examples:
- redefining whether publication should explain something directly
- redefining where simulator normalization should source a concept from
- separating player and creature damage models

#### `deferred_pending_evidence`
The issue is real, but the project is not yet ready to revise authority safely.

This should be explicit and justified, not left vague.

## Phase order

## Phase 0. Intake

Inputs:
- the rule or contradiction under review
- reason the issue was surfaced
- current blocker or risk

Outputs:
- revision work card
- target concept list
- mandatory source set

## Phase 1. Authority Baseline

Primary lenses:
- `system_lens`
- `continuity_lens`

Questions:
- What do the current authority files say?
- Where is the conflict or ambiguity?
- Which statements are canonical and which are explanatory?
- Is the problem real or only apparent?

Outputs:
- baseline summary
- contradiction or ambiguity note
- source file map

## Phase 2. Dependency Mapping

Primary lens:
- `dependency_lens`

Questions:
- What other rules depend on this concept?
- What simulator surfaces depend on it?
- What publication sections depend on it?
- What species, Techniques, or status families rely on it?

Outputs:
- dependency map
- impacted artifact list
- risk surface list

## Phase 3. Problem Classification

Primary lenses:
- `system_lens`
- `dependency_lens`

Questions:
- Is this mainly a wording ambiguity?
- Is this a taxonomy problem?
- Is this a real mechanic problem?
- Is this a subsystem-boundary problem?

Outputs:
- revision outcome classification
- statement of what kind of change is actually needed

This phase is important because it prevents overreacting to a problem that is
editorial-only or underreacting to one that is actually mechanical.

## Phase 4. Revision Proposal

Primary lenses:
- `system_lens`
- `balance_lens`
- `simulation_lens`

Questions:
- What is the cleanest corrected rule?
- What behavior should remain unchanged?
- What behavior should change?
- What abstractions become cleaner or dirtier if this revision is accepted?

Outputs:
- proposed doctrinal rule
- explicit invariants
- explicit changed behavior list

## Phase 5. Cross-System Review

Primary lenses:
- `dependency_lens`
- `simulation_lens`
- `editorial_lens`

Questions:
- What downstream work will this require?
- Is the simulator blocked, helped, or invalidated?
- Does publication need a later sync?
- Do knowledge registries need to be updated?

Outputs:
- downstream work list
- sync implications
- registry update implications

## Phase 6. Authority Integration

Execute the actual authority changes.

Possible tasks:
- update `docs/system/*`
- update `data/system/*`
- update doctrinal notes if needed
- update cross-file references

This phase should change authority directly and intentionally.

## Phase 7. Validation

Validation may include:
- consistency re-read across linked authority files
- taxonomy sanity pass
- mechanical sanity pass
- simulator implication review
- publication implication review

Outputs:
- validated authority revision
- unresolved downstream list if not yet fully propagated

## Phase 8. Knowledge Layer Update

If the revision changes doctrine, boundaries, or stable terminology, update the
knowledge layer.

Possible updates:
- `decision-registry.yaml`
- `concept-registry.yaml`
- `source-map.yaml`
- `project-state.yaml`
- doctrine docs under `docs/knowledge/`

This phase is mandatory when the accepted revision is expected to matter again.

## Phase 9. Downstream Routing

Classify what must happen next:
- no downstream action
- simulator follow-up
- corebook sync follow-up
- species audit follow-up
- batch refactor follow-up

Outputs:
- routed follow-up tasks

## Phase 10. Acceptance Closure

An authority revision should only be considered closed when:
- the authority itself is stable again
- the outcome classification is explicit
- the affected downstream work is at least routed

Suggested closure checklist:
- `baseline_recorded`
- `dependency_map_done`
- `problem_classified`
- `authority_updated`
- `validation_done`
- `knowledge_updated_if_needed`
- `downstream_routed`
- `pending_items_explicit`

## Phase 11. Change Impact Record

Every authority revision should record:
- what changed
- what did not change
- what artifacts are now downstream of the revision
- what assumptions are no longer valid

This is especially important when the revision affects:
- taxonomy
- simulator abstractions
- publication wording
- cross-species doctrine

## Good outputs

A good authority revision leaves behind:
- a cleaner and more stable rule
- a smaller ambiguity surface
- clearer subsystem boundaries
- explicit downstream work
- updated knowledge memory

## Bad outputs

A bad authority revision leaves behind:
- “fixed” wording without resolving the underlying contradiction
- simulator or publication drift not acknowledged
- taxonomy changes with no downstream routing
- new doctrine living only in conversation

## Relationship to other workflows

This workflow complements:
- [Technique Workflow](./technique-workflow.md)
- [Simulation Port Workflow](./simulation-port-workflow.md)
- [Core Sync Workflow](./core-sync-workflow.md)
- [Species Audit Workflow](./species-audit-workflow.md)

Those workflows assume authority is stable enough to act on.
This workflow exists for the cases where that assumption is no longer safe. 
