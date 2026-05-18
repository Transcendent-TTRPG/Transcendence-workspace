# Status Family Workflow

This document defines the canonical workflow for building or revising a status
family in Transcendence.

It is intended for repeatable families such as:
- infections
- poisons
- elixirs
- trap packages
- ailment extensions
- other grouped effect systems that share grammar, vectors, and resolution logic

Its purpose is not to handle one isolated entry. Its purpose is to establish
the shared frame that makes the entries of a family coherent.

## Purpose

Use this workflow when:
- authoring a new family of related statuses or effect packages
- revising the taxonomy or structure of an existing family
- expanding a family that should share common resolution logic
- normalizing a family for simulation coverage

Examples:
- defining how infections differ from poisons
- defining a family of elixirs with shared activation and side-effect logic
- defining trap packages that share trigger, warning, disable, and consequence surfaces

## Relationship to authority

The family authority remains in:
- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`
- and any relevant species or canon sources when the family is species-bound

This workflow exists because family work has a different shape than a single
Technique:
- taxonomy matters more
- vectors matter more
- shared grammar matters more
- simulator normalization usually needs to happen at the family level

## Required layers

Every status-family pass should rely on:
- the `Knowledge Layer`
- current authority
- explicit taxonomy decisions
- dependency and simulation review

## Core lenses

### `system_lens`
Checks:
- what kind of family this is
- how entries are applied
- how they persist
- how they clear, expire, or escalate

### `dependency_lens`
Checks:
- what subsystems the family depends on
- what shared surfaces should be defined once rather than repeated in every entry

### `balance_lens`
Checks:
- pressure profile across the family
- whether entries are too compressed or too broad
- whether setup, burden, and counterplay feel internally sane

### `simulation_lens`
Checks:
- whether the family can be normalized for sim coherently
- what shared runtime abstractions should exist
- whether one generic runtime family can cover many entries

### `editorial_lens`
Checks:
- whether the family can be explained cleanly once and inherited later
- whether entries are repeating shared doctrine unnecessarily

### `continuity_lens`
Checks:
- consistency with existing rule families
- consistency between the family’s own entries
- consistency with already-set taxonomy decisions

## Family outcome classifications

Every status-family pass should end with one primary outcome:

- `family_defined`
- `family_revised`
- `family_extended`
- `family_blocked`

### Meanings

#### `family_defined`
The family’s shared grammar and entry model now exist clearly.

#### `family_revised`
The family already existed, but its taxonomy, boundaries, or shared behavior
needed correction.

#### `family_extended`
The family base is stable and this pass mainly adds more entries within that
frame.

#### `family_blocked`
The family cannot yet close because a higher-level authority or subsystem issue
is unresolved.

## Phase order

## Phase 0. Intake

Inputs:
- target family
- reason for the pass
- whether the pass is new definition, revision, or expansion

Outputs:
- family work card
- work scope
- source set

## Phase 1. Family Framing

Primary lenses:
- `system_lens`
- `continuity_lens`

Questions:
- What kind of family is this?
- What unifies its entries?
- What should clearly not belong to this family?
- What nearby families must stay distinct from it?

Outputs:
- family definition
- family boundary note
- nearby-family distinction note

Examples:
- infection is not just “poison but slower”
- elixir is not just “buff item”
- trap package is not just “single trap entry”

## Phase 2. Taxonomy and Grammar

Primary lenses:
- `system_lens`
- `dependency_lens`

Questions:
- What are the shared fields or grammar of the family?
- What vectors exist?
- What severities, grades, or package sizes exist?
- What is inherited and what is entry-specific?

Outputs:
- family grammar
- taxonomy
- shared-field list
- entry-specific field list

This phase is where the family becomes authorable in a stable way.

## Phase 3. Resolution Model

Primary lenses:
- `system_lens`
- `balance_lens`

Questions:
- How are entries applied?
- What rolls or checks matter?
- What resists them?
- How do they persist, worsen, or clear?
- What counterplay exists?

Outputs:
- shared resolution model
- resistance / clearing model
- escalation or expiry model

## Phase 4. Dependency Mapping

Primary lenses:
- `dependency_lens`
- `simulation_lens`

Questions:
- What other subsystems does the family depend on?
- Does it rely on wounds, treatment, movement, consumables, concealment, inventory, or time pressure?
- What should be defined once at family level instead of per entry?

Outputs:
- dependency map
- family-level shared surfaces
- blocker list if present

## Phase 5. Internal Balance Review

Primary lenses:
- `balance_lens`
- `continuity_lens`

Questions:
- Are the entries internally differentiated enough?
- Are severities or grades meaningful?
- Is there too much compression or overlap inside the family?
- Is counterplay consistent?

Outputs:
- family balance note
- redundancy note
- weak band / oppressive band note

## Phase 6. Simulation Framing

Primary lenses:
- `simulation_lens`
- `dependency_lens`

Questions:
- Can the family be normalized coherently for the simulator?
- What shared runtime abstractions should exist?
- What belongs in:
  - data only
  - shared runtime layer
  - family-specific runtime
- What questions should this family eventually support?

Outputs:
- family simulation model
- runtime gap classification
- normalized data strategy

## Phase 7. Editorial Framing

Primary lenses:
- `editorial_lens`
- `continuity_lens`

Questions:
- What doctrine should be explained once at family level?
- What should be inherited by entries?
- What terminology needs to remain rigid?

Outputs:
- family-level explanatory structure
- entry-level inheritance plan
- terminology plan

## Phase 8. Integration

Execute the actual family work.

Possible tasks:
- update family authority docs
- update family authority YAML/data
- create or revise simulator-facing family data
- create or revise shared runtime hooks
- update publication-facing family explanations if needed

## Phase 9. Validation

Validation may include:
- taxonomy review
- grammar consistency review
- entry comparison review
- simulator normalization review
- selected scenario or question checks if family support already exists

Outputs:
- validated family frame
- unresolved family issues if present

## Phase 10. Acceptance Closure

A status-family pass should only be considered closed when it leaves behind:
- a clear family definition
- a clear grammar
- a clear resolution model
- explicit dependency status
- explicit simulation status

Suggested closure checklist:
- `family_definition_recorded`
- `taxonomy_recorded`
- `resolution_model_recorded`
- `dependency_map_done`
- `simulation_strategy_recorded`
- `editorial_structure_recorded`
- `pending_items_explicit`

## Phase 11. Change Impact Record

Every family pass should record:
- files changed
- taxonomy decisions made
- runtime surfaces affected
- what future entries can now inherit safely
- what still remains blocked

## Good outputs

A good status-family pass leaves behind:
- a family that can be extended without reinventing itself every time
- cleaner shared doctrine
- clearer simulator normalization paths
- less duplicated authoring work

## Bad outputs

A bad status-family pass leaves behind:
- entries that all behave differently with no family grammar
- taxonomy that overlaps nearby families badly
- family doctrine repeated inside every entry
- no shared simulation model

## Relationship to other workflows

This workflow complements:
- [Authority Revision Workflow](./authority-revision-workflow.md)
- [Dependency Review Workflow](./dependency-review-workflow.md)
- [Balance Review Workflow](./balance-review-workflow.md)
- [Simulation Port Workflow](./simulation-port-workflow.md)

Use this workflow when the unit of work is a reusable family, not a single
Technique or a single isolated status entry. 
