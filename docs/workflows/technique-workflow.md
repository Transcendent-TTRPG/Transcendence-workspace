# Technique Workflow

This document defines the canonical workflow for creating, revising, porting,
and validating Techniques across authority, simulation, and publication.

It is designed for high-context iterative work. It does not assume that every
Technique will be simulable immediately, but it does require that unresolved
gaps be classified explicitly instead of left ambiguous.

## Purpose

Use this workflow when:
- authoring a new Technique
- revising an existing Technique
- porting an authored Technique into the simulator
- syncing a Technique-related rules change into publication

## Required layers

Every Technique pass should rely on:
- the `Knowledge Layer` for doctrine, decisions, and retrieval
- the relevant artifact skill, especially `technique-authoring`
- explicit review lenses instead of informal mixed reasoning

## Core lenses

### `species_lens`
Checks:
- species identity
- discipline or habit origin
- what the Technique must not do if it is to remain species-correct

### `system_lens`
Checks:
- roll family
- competency source
- surface choice
- ailment vs concealment vs procedural vs immediate effect
- duration, clearing, expiry, and restrictions

### `dependency_lens`
Checks:
- upstream rules the Technique depends on
- downstream artifacts that must be updated together
- whether a missing subsystem blocks safe completion

### `balance_lens`
Checks:
- Rhythm / Attrition sanity
- relationship to sibling Techniques
- frequency, pressure, counterplay, and boundedness

### `simulation_lens`
Checks:
- whether the Technique already reuses existing runtime surfaces
- what new runtime work is needed if it does not
- what scenario and question it can eventually support

### `editorial_lens`
Checks:
- clarity
- inherited doctrine vs duplicated doctrine
- terminology
- publication readiness

### `continuity_lens`
Checks:
- consistency with seeds
- consistency with species set
- consistency with profiles, prior decisions, and previous passes

The `continuity_lens` should be applied lightly across the whole workflow,
especially during intake, integration, and validation.

## Phase 0. Intake

Inputs:
- species
- Technique or gap to work on
- seed if it exists
- work goal
- current simulation/publication state

Outputs:
- work card
- exact scope
- mandatory source files
- current coverage state
- main design question

## Phase 1. Species Framing

Primary lens:
- `species_lens`

Questions:
- Does this genuinely belong to the species?
- What behavior, culture, biology, or training justifies it?
- What should it explicitly avoid doing?
- What are its primary and secondary interaction surfaces?

Outputs:
- fantasy
- world origin
- why-not-base-action
- interaction surfaces

## Phase 2. Mechanical Framing

Primary lens:
- `system_lens`

Questions:
- What kind of Technique is it?
- What roll does it use?
- What real competency feeds it?
- Does it use an ailment, concealment, procedural state, or immediate effect?
- What is its real duration?
- What restrictions are necessary?
- How is it cleared, consumed, or expired?

Outputs:
- trigger
- requirements
- target / range / area
- Rhythm / Attrition
- roll model
- effect model
- duration / restrictions

## Phase 3. Dependency Framing

Primary lens:
- `dependency_lens`

Questions:
- What other subsystems does it touch?
- Does it require an upstream rule to be stable first?
- What files must move together?
- Is the work blocked by unresolved authority elsewhere?

Outputs:
- dependency map
- linked file list
- upstream blockers if present
- decision on whether the Technique can close now or must be split

## Phase 4. Balance Framing

Primary lens:
- `balance_lens`

Questions:
- Is the cost aligned with sibling Techniques?
- How often should the Technique matter?
- Is its value immediate, setup-based, or persistent?
- How oppressive is it if it lands?
- What counterplay exists?

Outputs:
- cost sanity note
- sibling comparison note
- risk note for overpricing or underpricing
- future simulation targets if needed

## Phase 5. Simulation Framing

Primary lens:
- `simulation_lens`

Questions:
- Does it reuse existing runtime surfaces?
- Is it data-only?
- Does it need a small runtime extension?
- Does it need a new procedural family?
- Does it need a new subsystem?
- Is it blocked by authority ambiguity?
- What minimal scenario would expose it?
- What saved question would eventually test it?

Outputs:
- porting state target
- runtime gap classification
- scenario seed note
- question seed note

### Runtime gap classifications

- `data_only`
- `small_runtime_extension`
- `new_state_family`
- `new_subsystem`
- `authority_blocked`

### Porting states

- `authored`
- `sim_defined`
- `runtime_supported`
- `policy_exercisable`
- `scenario_tested`
- `question_ready`

## Phase 6. Editorial Framing

Primary lens:
- `editorial_lens`

Questions:
- Is the text clear?
- Does it duplicate doctrine that should be inherited instead?
- Are the terms consistent?
- Can the core explain this cleanly?
- Is there redundancy between authority and publication?

Outputs:
- cleaned authority wording
- sync notes for publication if needed

## Phase 7. Integration

Execute the actual updates:
- update authority text
- update authority YAML
- update simulation data if applicable
- update simulation runtime if applicable
- update publication files if applicable
- update coverage / artifact state tracking
- update knowledge registries if doctrine changed

## Phase 8. Validation

Validation may include:
- doctrinal review
- loader validation
- runtime validation
- scenario test
- question test
- publication consistency pass

Output:
- either the Technique closes for this pass
- or it exits with an explicit pending list

## Phase 9. Acceptance Closure

The Technique is only “closed for now” when its status is explicit.

Suggested closure checklist:
- `authority_updated`
- `yaml_updated`
- `sim_defined` or gap classified
- `runtime_supported` or gap classified
- `coverage_updated`
- `core_sync_done` or `not_needed`
- `pending_items_explicit`

## Phase 10. Change Impact Record

Every Technique pass should leave a compact impact note.

Record:
- files changed
- concepts touched
- decisions introduced or reinforced
- coverage movement
- unresolved follow-up work

This is especially important for:
- retroactive simulator backfill
- species pass audits
- large doctrinal refactors

## Subagent guidance

Do not use subagents for every Technique automatically.

Subagents are justified when:
- the task is long
- the lenses are separable
- parallel review reduces risk or saves time

Good uses:
- authoring plus simulation plus editorial review on one complex Technique
- batch audits across a whole species
- doctrinal refactors across many Techniques

Poor uses:
- trivial wording edits
- very small isolated changes
- tasks where a single central decision dominates everything else

## Outputs expected from a good Technique pass

A good pass should leave behind:
- clearer authority
- cleaner dependency understanding
- explicit simulation state
- explicit publication state
- a real closure or a real blocker

It should not leave behind:
- vague “almost ready” status
- hidden subsystem dependencies
- duplicated doctrine
- unclassified runtime gaps
