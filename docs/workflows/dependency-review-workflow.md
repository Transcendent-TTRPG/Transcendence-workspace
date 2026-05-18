# Dependency Review Workflow

This document defines the canonical workflow for reviewing dependencies between
rules, artifacts, and runtime surfaces in Transcendence.

Its purpose is not to redesign a rule by itself. Its purpose is to determine:
- what a task really depends on
- what can safely move now
- what is blocked upstream
- what downstream artifacts must move together

This workflow is especially useful when work feels “stuck” for reasons that are
not actually local to the artifact currently being edited.

## Purpose

Use this workflow when:
- a Technique, status family, or rule seems to require more than one subsystem
- simulator work is blocked by unclear or missing upstream rules
- publication sync depends on clarifying multiple linked concepts
- a task might need to be split into smaller pieces
- a team member suspects a hidden dependency is causing repetition or rework

Examples:
- a Technique like `Ensuciar la Herida` that depends on wound treatment, `Interact`, and medicine surfaces
- a concealment revision that touches actions, state handling, and publication wording
- a trap family that depends on route logic, reactions, and scenario semantics

## Relationship to other workflows

This workflow does not replace:
- authority revision
- technique authoring
- simulation porting
- core sync

Instead, it acts as a cross-cutting diagnostic workflow.

Use it when the main question is not “what should this say?” but rather:
- “what does this actually rely on?”
- “what must change together?”
- “what should be blocked, split, or reordered?”

## Required layers

Every dependency review should rely on:
- the `Knowledge Layer`
- current authority files
- current simulator or publication surfaces if relevant
- explicit dependency and continuity review

## Core lenses

### `dependency_lens`
Checks:
- upstream dependencies
- downstream dependencies
- ownership boundaries
- hidden couplings between artifacts

### `system_lens`
Checks:
- what the focal artifact actually claims mechanically
- which parts are local and which parts belong to other rule families

### `continuity_lens`
Checks:
- whether prior decisions already settled part of the dependency question
- whether the team is rediscovering a previously-recorded dependency

### `simulation_lens`
Checks:
- whether the dependency is in authority only or also in runtime
- whether a simulator blocker is genuine or just a missing abstraction layer

### `editorial_lens`
Checks:
- whether publication files inherit the same dependency structure
- whether sync debt is being created by cross-file coupling

## Dependency outcome classifications

Every dependency review should end with one primary outcome:

- `self_contained`
- `linked_update_required`
- `upstream_blocked`
- `downstream_routing_required`
- `must_split_work`

### Meanings

#### `self_contained`
The work is mostly local. No important hidden dependency is blocking it.

#### `linked_update_required`
The work can proceed, but more than one artifact must move together.

Examples:
- authority text plus YAML
- simulator data plus runtime
- ES plus EN publication files

#### `upstream_blocked`
The focal task cannot close honestly because another rule or subsystem must be
stabilized first.

#### `downstream_routing_required`
The focal change is valid, but it creates follow-up obligations elsewhere.

#### `must_split_work`
The task is too entangled to treat as one unit. It should be divided into:
- a dependency-unlocking task
- and one or more artifact tasks downstream

## Phase order

## Phase 0. Intake

Inputs:
- focal artifact or rule
- current blocker or suspicion
- desired outcome if no dependency existed

Outputs:
- dependency review card
- focal question
- mandatory source set

## Phase 1. Local Claim Extraction

Primary lenses:
- `system_lens`
- `continuity_lens`

Questions:
- What is the focal artifact actually trying to do?
- Which claims are local to it?
- Which claims already sound like they belong to another subsystem?

Outputs:
- local claim list
- apparent non-local claim list

This phase is important because many dependency problems start with a local
artifact silently carrying another subsystem inside it.

## Phase 2. Upstream Mapping

Primary lens:
- `dependency_lens`

Questions:
- What rules or abstractions must exist first?
- Which mechanics does the focal task assume are already defined?
- Are those definitions stable, partial, or absent?

Outputs:
- upstream dependency map
- upstream stability assessment

Examples of upstream dependencies:
- treatment logic
- movement line semantics
- ailment taxonomy
- concealment state semantics
- break / durability logic

## Phase 3. Downstream Mapping

Primary lenses:
- `dependency_lens`
- `editorial_lens`
- `simulation_lens`

Questions:
- If the focal task changes, what else must change with it?
- Which simulator surfaces depend on it?
- Which publication sections depend on it?
- Which knowledge records depend on it?

Outputs:
- downstream artifact map
- linked update list

## Phase 4. Boundary Check

Primary lenses:
- `system_lens`
- `dependency_lens`

Questions:
- Does the focal artifact own this behavior?
- Or is it leaking another subsystem into itself?
- Would solving this locally create duplication or fake closure?

Outputs:
- boundary note
- ownership decision

This phase is especially important for deciding whether a task belongs to:
- authority revision
- technique workflow
- simulation porting
- core sync
- or must first become a dependency-unlocking task

## Phase 5. Review Outcome Classification

Primary lenses:
- `dependency_lens`
- `continuity_lens`

Questions:
- Is the work actually self-contained?
- Does it require linked updates?
- Is it blocked upstream?
- Does it need splitting?

Outputs:
- dependency outcome classification
- statement of why

## Phase 6. Work Routing

Primary lenses:
- `dependency_lens`
- `simulation_lens`
- `editorial_lens`

Questions:
- What workflow should own the next step?
- Should the next step be:
  - authority revision
  - technique pass
  - simulation port
  - core sync
  - species audit
  - runtime subsystem task
- In what order should those tasks happen?

Outputs:
- routed next tasks
- ordered dependency plan

## Phase 7. Validation

Validation may include:
- checking whether the mapped dependencies match current authority
- checking whether an assumed blocker is real
- checking whether the proposed split actually isolates the work cleanly

Outputs:
- validated dependency map
- revised routing if needed

## Phase 8. Acceptance Closure

A dependency review should only be considered closed when:
- the focal task’s dependencies are explicit
- blockers are explicit
- linked updates are explicit
- next workflow ownership is explicit

Suggested closure checklist:
- `local_claims_recorded`
- `upstream_dependencies_mapped`
- `downstream_dependencies_mapped`
- `boundary_decision_made`
- `outcome_classified`
- `next_work_routed`
- `pending_items_explicit`

## Phase 9. Change Impact Record

If the dependency review changes tracking or planning records, record:
- focal artifact
- dependencies identified
- blockers identified
- routing decisions
- tasks created or reprioritized

## Good outputs

A good dependency review leaves behind:
- a clearer map of what belongs where
- fewer hidden blockers
- better sequencing of work
- fewer fake local fixes

## Bad outputs

A bad dependency review leaves behind:
- generic statements that “this touches many things”
- no ownership decision
- no routing decision
- no distinction between upstream blockers and downstream obligations

## Relationship to other workflows

This workflow complements:
- [Authority Revision Workflow](./authority-revision-workflow.md)
- [Technique Workflow](./technique-workflow.md)
- [Simulation Port Workflow](./simulation-port-workflow.md)
- [Core Sync Workflow](./core-sync-workflow.md)
- [Species Audit Workflow](./species-audit-workflow.md)

It should be used when a team member needs to know what the real dependency
shape of a problem is before choosing the correct downstream workflow. 
