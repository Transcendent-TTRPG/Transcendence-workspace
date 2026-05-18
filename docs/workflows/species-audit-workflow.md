# Species Audit Workflow

This document defines the canonical workflow for auditing a species pass across
authority, simulation coverage, and publication-facing coherence.

Its purpose is not only to count Techniques. Its purpose is to answer whether a
species is:
- complete enough
- internally coherent enough
- simulator-ready enough
- and development-prioritized correctly enough

## Purpose

Use this workflow when:
- reviewing a finished or partially finished species pass
- preparing retroactive simulator backfill
- checking whether a species identity is holding across its authored set
- deciding what the next species work should be
- validating whether current coverage claims are honest

## Relationship to authority

The species authority remains in:
- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`
- any relevant species canon or seed documents

An audit does not rewrite authority by itself. It evaluates the current state
of the pass and identifies:
- strengths
- gaps
- inconsistencies
- backlog order

If the audit uncovers a real design contradiction, that contradiction should be
escalated into a normal authority revision workflow.

## Required layers

Every species audit should rely on:
- the `Knowledge Layer`
- current species authority
- simulation coverage records
- porting-plan state if simulator coverage matters
- explicit review lenses instead of informal impressions

## Core lenses

### `species_lens`
Checks:
- whether the set still feels like one species
- whether the species fantasy is actually expressed through its Techniques
- whether some Techniques feel imported from another species

### `continuity_lens`
Checks:
- consistency with seeds
- consistency with prior pass decisions
- consistency between earlier and later authored Techniques

### `system_lens`
Checks:
- distribution of attack / defense / utility / pressure / hybrid roles
- use of surfaces such as ailments, concealment, procedural states, exchange, movement, or treatment
- whether the set over-relies on one mechanical move

### `balance_lens`
Checks:
- whether costs and pressure bands feel internally sane
- whether the species has obvious dead entries or dominant entries
- whether the species expresses too much or too little tactical variety

### `simulation_lens`
Checks:
- simulator coverage
- porting state distribution
- whether the current runtime supports the species honestly
- where the real blockers are

### `dependency_lens`
Checks:
- what species Techniques depend on missing rule families
- whether the species backlog is blocked by one or two missing subsystems
- whether the next work should be a Technique port or a runtime extension

### `editorial_lens`
Checks:
- whether wording is clean across the pass
- whether repeated explanations should be inherited instead
- whether publication sync pressure is accumulating around the species

## Audit outcomes

A species audit should end with explicit conclusions in at least these bands:

- `identity_status`
- `coverage_status`
- `simulation_status`
- `backlog_priority`

### Suggested status vocabulary

#### `identity_status`
- `strong`
- `mixed`
- `drifting`

#### `coverage_status`
- `complete`
- `mostly_complete`
- `partial`
- `fragmented`

#### `simulation_status`
- `well_supported`
- `partially_supported`
- `structurally_blocked`
- `mostly_unported`

#### `backlog_priority`
- `low`
- `medium`
- `high`
- `critical`

## Phase order

## Phase 0. Intake

Inputs:
- target species
- reason for audit
- whether the audit is authority-focused, simulator-focused, or full-pass

Outputs:
- audit work card
- audit scope
- mandatory sources

## Phase 1. Species Baseline

Primary lenses:
- `species_lens`
- `continuity_lens`

Questions:
- What is the species trying to be?
- What are its key habits, disciplines, and mechanical signatures?
- What prior decisions define its pass?
- What seeds or canon should the audit keep in view?

Outputs:
- species identity summary
- expected mechanical signature summary
- required source list

## Phase 2. Authority Inventory

Primary lenses:
- `continuity_lens`
- `system_lens`

Questions:
- How many Techniques are authored?
- What categories exist?
- What are the main role bands?
- What does the pass currently emphasize?
- Are there obvious omissions in its authored spread?

Outputs:
- authored inventory
- role/category inventory
- first-pass note on obvious holes

Important:
This phase is not yet about whether the Techniques are good. It is about
mapping the pass honestly before judging it.

## Phase 3. Identity Review

Primary lenses:
- `species_lens`
- `editorial_lens`

Questions:
- Do the Techniques feel like one family?
- Are there repeated themes that correctly reinforce the species?
- Are there Techniques that feel off-species or overly generic?
- Is the wording helping or obscuring species identity?

Outputs:
- identity strengths
- identity drifts
- repeated motifs
- outlier list

## Phase 4. Mechanical Spread Review

Primary lenses:
- `system_lens`
- `balance_lens`

Questions:
- Is there enough variety in what the species can do?
- Is the set too concentrated around one trick?
- Are some roles underrepresented?
- Are some Techniques suspiciously weak, redundant, or overbearing?

Outputs:
- spread analysis
- redundancy list
- weak-entry list
- dominant-entry list

## Phase 5. Simulation Coverage Review

Primary lenses:
- `simulation_lens`
- `dependency_lens`

Questions:
- How many Techniques are only authored?
- How many are `sim_defined`?
- How many are `runtime_supported`?
- How many are `policy_exercisable`?
- How many are `scenario_tested`?
- How many are `question_ready`?

Outputs:
- coverage matrix
- porting state counts
- honest simulator support assessment

## Phase 6. Runtime Blocker Review

Primary lenses:
- `dependency_lens`
- `simulation_lens`

Questions:
- What are the main missing runtime families?
- Are there one or two blockers affecting many Techniques?
- Would it be better to keep porting one Technique at a time, or unlock a subsystem first?

Outputs:
- blocker list
- grouped blocker families
- recommended runtime priorities

Examples:
- wound treatment
- procedural sensory interference
- corridor trap logic
- richer movement line semantics

## Phase 7. Publication Pressure Review

Primary lenses:
- `editorial_lens`
- `continuity_lens`

Questions:
- Is the species accumulating publication debt?
- Are some species explanations now out of sync with current authority?
- Is corebook sync needed now or later?

Outputs:
- publication pressure note
- sync candidates
- deferred sync note if applicable

## Phase 8. Backlog Prioritization

Primary lenses:
- `simulation_lens`
- `dependency_lens`
- `balance_lens`

Questions:
- What should be worked on next?
- Should the next work be:
  - direct Technique porting
  - authority cleanup
  - runtime extension
  - publication sync
- In what order should gaps close?

Outputs:
- ordered next-step list
- immediate next batch
- deferred backlog

## Phase 9. Audit Conclusion

Produce a compact conclusion covering:
- `identity_status`
- `coverage_status`
- `simulation_status`
- `backlog_priority`
- major blockers
- immediate next actions

## Phase 10. Change Impact Record

If the audit itself updates tracking documents, record:
- files changed
- counts changed
- coverage claims introduced or corrected
- newly-recognized blockers
- newly-prioritized work

## Acceptance criteria

A species audit should only be considered closed when it leaves behind:
- an explicit identity assessment
- an explicit coverage assessment
- an explicit simulation assessment
- an explicit ordered backlog
- no hidden “I think this is mostly fine” claims without support

Suggested closure checklist:
- `species_baseline_recorded`
- `authored_inventory_checked`
- `identity_review_done`
- `mechanical_spread_review_done`
- `simulation_coverage_review_done`
- `runtime_blockers_classified`
- `backlog_prioritized`
- `pending_items_explicit`

## Good outputs

A good species audit leaves behind:
- a cleaner picture of what the species is
- honest counts
- clear simulation status
- real priority order
- a better decision on whether to port, revise, or extend runtime next

## Bad outputs

A bad species audit leaves behind:
- only raw counts with no identity reading
- identity opinions with no coverage data
- vague claims that the species is “fine”
- no explicit blocker map
- no ordered next work

## Relationship to other workflows

This workflow complements:
- [Technique Workflow](./technique-workflow.md)
- [Simulation Port Workflow](./simulation-port-workflow.md)
- [Core Sync Workflow](./core-sync-workflow.md)

The technique workflow governs one artifact pass.
The simulation-port workflow governs simulator-facing coverage.
The core-sync workflow governs publication alignment.
This species-audit workflow governs the evaluation of the species set as a
whole. 
