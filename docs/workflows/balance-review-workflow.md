# Balance Review Workflow

This document defines the canonical workflow for reviewing balance questions in
Transcendence.

Its purpose is not to turn the project into a purely statistical design loop.
Its purpose is to combine:
- doctrine
- system logic
- scenario reasoning
- and simulation evidence

so that cost, pressure, tempo, counterplay, and tactical value can be judged
more explicitly.

## Purpose

Use this workflow when:
- a Technique, family, species pass, or subsystem looks overpowered, weak, or unclear
- costs feel suspicious relative to similar entries
- a simulator result needs to be interpreted rather than just reported
- a design question explicitly asks whether something is oppressive, too weak, or priced wrongly
- a revision may change tempo, survivability, control, or pressure

Examples:
- whether a `Rhythm 0 / Attrition 2` reaction is worth its cost
- whether a concealment Technique is too reliable under typical conditions
- whether a species is too concentrated around one winning line
- whether an ailment lasts too long relative to its setup cost

## Relationship to authority and simulation

Balance review does not replace authority.
Balance review also does not treat simulation output as self-justifying truth.

Instead:
- authority defines intended behavior
- simulation gives repeatable evidence under explicit assumptions
- balance review interprets both together

## Cost arbitration rule

When simulation produces a validated cost that contradicts the prose `cost_note`
in `techniques.yaml`, the simulation-validated cost wins.

Concretely:

- the structured `rhythm_cost` / `attrition_cost` fields in the YAML are the
  binding record
- `cost_note` is explanatory prose and must be updated to match the validated
  numeric fields after any balance review that changes or confirms a cost
- do not leave a `cost_note` that states a cost different from the structured
  fields — that is a documentation error, not a design ambiguity

When a balance review confirms a cost without changing it, the `cost_note`
should be updated to say the cost was validated by simulation, not just asserted.

When a balance review changes a cost, both the structured field and the
`cost_note` must be updated together in the same pass.

If a balance question exposes a real contradiction in authority, it should be
routed into:
- [Authority Revision Workflow](./authority-revision-workflow.md)

If the balance question cannot be answered honestly because simulator coverage is
too thin, it should be routed into:
- [Simulation Port Workflow](./simulation-port-workflow.md)

If a Technique does not yet have its saved minimum cost question, the review
should normally stay preliminary and route toward question authoring instead of
pretending full balance validation already exists.

## Required layers

Every balance review should rely on:
- the `Knowledge Layer`
- current authority
- relevant sibling artifacts for comparison
- simulator evidence if available
- explicit assumptions
- and, for Technique-level closure, the saved minimum cost question when it
  exists

For `Rhythm` and `Attrition` specifically, the review should anchor itself to:

- [ADR — ATB Base Rhythm Costs](../../Transcendence-design/docs/adr/combat-atb-rhythm-costs.md)

The review must distinguish clearly between:

- the **canonical system spectrum**
- and the **currently observed simulator cluster**

It should not treat a temporary cluster of ported Techniques as if it were the
entire system's true baseline.

## Core lenses

### `balance_lens`
Checks:
- cost
- pressure
- frequency of impact
- boundedness
- counterplay
- payoff relative to setup
- whether the artifact belongs in a broader canonical cost band even if the
  current simulator subset clusters elsewhere

### `system_lens`
Checks:
- whether the artifact behaves as intended mechanically
- whether the review is really about balance or actually about a rules mismatch

### `species_lens`
Checks:
- whether the power profile is appropriate for the species identity
- whether a proposed nerf or buff would flatten species distinctiveness

### `simulation_lens`
Checks:
- what evidence exists
- what assumptions the evidence depends on
- what the simulator is not yet modeling

### `dependency_lens`
Checks:
- whether the balance issue is local
- whether it is caused by another subsystem
- whether the right fix belongs somewhere else

### `continuity_lens`
Checks:
- sibling comparisons
- previous passes
- earlier decisions about the same family or species

## Review outcome classifications

Every balance review should end with one primary outcome:

- `balanced_enough`
- `monitor`
- `adjust_locally`
- `adjust_systemically`
- `insufficient_evidence`

### Meanings

#### `balanced_enough`
Current evidence and doctrine do not justify changing the artifact now.

#### `monitor`
There is a plausible concern, but not enough to justify a revision yet.

#### `adjust_locally`
The issue appears local to the artifact or small family under review.

Examples:
- Rhythm or Attrition tweak
- duration adjustment
- narrowing or widening a restriction

#### `adjust_systemically`
The balance issue seems to come from a broader rule family or subsystem.

Examples:
- concealment baseline too generous
- recovery thresholds too soft
- ATB timing assumptions distorting a whole class of effects

#### `insufficient_evidence`
The question is real, but the project does not yet have enough authority
clarity, simulator coverage, or scenario evidence to answer it responsibly.

This should also be the normal outcome when:

- the Technique still lacks its minimum saved cost question
- or a clearly necessary derived question is still missing

## Evidence classes

Balance review should distinguish evidence sources clearly.

### `doctrinal_evidence`
- role comparison
- intended species identity
- intended tactical niche
- structural restriction analysis

### `comparative_evidence`
- sibling Techniques
- comparable actions
- same-species alternatives
- cross-species analogs

### `simulation_evidence`
- scenario results
- policy loop outcomes
- rate, tempo, attrition, survivability, and pressure metrics

### `playtest_like_evidence`
- traced scenarios
- human read-through of tactical lines
- qualitative stress tests

No single evidence class should automatically dominate all others.

## Phase order

## Phase 0. Intake

Inputs:
- focal artifact, family, species, or subsystem
- reason for review
- suspected balance issue

Outputs:
- balance review card
- main question
- required comparison set

## Phase 1. Question Framing

Primary lenses:
- `balance_lens`
- `system_lens`

Questions:
- What exactly is the concern?
- Is the concern about:
  - cost
  - reliability
  - pressure
  - survivability
  - control
  - counterplay
  - species identity distortion
- What would count as evidence either way?
- Is the concern about a true mismatch against the canonical cost spectrum, or
  only against the currently ported sample?
- Does the Technique already have its minimum saved cost question?
- Does it also need a derived question because its value depends on a special
  surface such as ailments, concealment, procedural states, reactions,
  geometry, breakage, kits, or residues?

Outputs:
- framed balance question
- explicit concern type
- evaluation criteria
- question sufficiency note

## Phase 2. Doctrinal Baseline

Primary lenses:
- `system_lens`
- `species_lens`
- `continuity_lens`

Questions:
- What is the artifact supposed to do?
- What niche is it supposed to occupy?
- What should it not be better than?
- What sibling or comparable artifacts form the correct comparison set?
- Which canonical `Rhythm` band and `Attrition` band should this artifact be
  compared against first?

Outputs:
- doctrinal baseline
- comparison set
- intended niche summary
- canonical cost-band target

## Phase 3. Evidence Inventory

Primary lenses:
- `simulation_lens`
- `dependency_lens`

Questions:
- What evidence exists today?
- Is there simulator evidence?
- Is there only doctrinal evidence?
- Is the artifact even modeled well enough to support a serious review?

Outputs:
- evidence inventory
- evidence quality note
- explicit missing-evidence list

## Phase 4. Comparative Analysis

Primary lenses:
- `balance_lens`
- `continuity_lens`

Questions:
- How does the artifact compare to siblings?
- Is it overpaying or underpaying?
- Is its payoff too broad or too narrow?
- Does it crowd out nearby options?

Outputs:
- comparative note
- likely overperform / underperform flags
- crowd-out or redundancy note

## Phase 5. Simulation Interpretation

Primary lenses:
- `simulation_lens`
- `balance_lens`

Questions:
- What do the results actually say?
- Under what assumptions?
- Is the result stable across scenarios or only in one narrow setup?
- Is the simulator under-modeling something important?

Outputs:
- interpreted simulation note
- assumption caveats
- confidence level

Important:
This phase should interpret results, not just repeat raw percentages.

## Phase 6. Cause Classification

Primary lenses:
- `dependency_lens`
- `system_lens`

Questions:
- Is the issue local?
- Is it caused by scenario assumptions?
- Is it caused by a simulator gap?
- Is it caused by a larger subsystem?

Outputs:
- cause classification
- local vs systemic judgment

## Phase 7. Recommendation

Primary lenses:
- `balance_lens`
- `species_lens`
- `system_lens`

Questions:
- Should nothing change?
- Should the artifact be monitored?
- Should it be adjusted locally?
- Should the subsystem be adjusted instead?

Outputs:
- review outcome classification
- recommended action
- non-recommended actions if relevant

## Phase 8. Downstream Routing

Route the result to the correct next workflow.

Possible routes:
- no action
- Technique revision
- authority revision
- simulation port extension
- species audit
- publication sync later if the change lands

Outputs:
- routed next step

## Phase 9. Acceptance Closure

A balance review should only be considered closed when it leaves behind:
- a clearly-framed question
- an explicit evidence basis
- an explicit conclusion
- an explicit next step or explicit no-action result

Suggested closure checklist:
- `question_framed`
- `doctrinal_baseline_recorded`
- `evidence_inventory_recorded`
- `comparison_done`
- `cause_classified`
- `outcome_classified`
- `next_step_routed`

## Phase 10. Change Impact Record

If the review changes tracking or planning records, record:
- focal artifact
- evidence used
- assumptions that mattered
- conclusion reached
- downstream work created or avoided

## Good outputs

A good balance review leaves behind:
- a real question
- explicit evidence
- explicit caveats
- a usable conclusion
- a clear route to the next action

## Bad outputs

A bad balance review leaves behind:
- gut feeling presented as conclusion
- raw simulator outputs with no interpretation
- comparisons with the wrong sibling set
- a recommendation with no stated cause

## Relationship to other workflows

This workflow complements:
- [Authority Revision Workflow](./authority-revision-workflow.md)
- [Dependency Review Workflow](./dependency-review-workflow.md)
- [Technique Workflow](./technique-workflow.md)
- [Simulation Port Workflow](./simulation-port-workflow.md)
- [Species Audit Workflow](./species-audit-workflow.md)

Use this workflow when the central question is not “how do we author or port
this?” but “is this priced, pressuring, and performing the way it should?” 
