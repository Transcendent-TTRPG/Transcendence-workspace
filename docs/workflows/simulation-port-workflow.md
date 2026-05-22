# Simulation Port Workflow

This document defines the canonical workflow for porting authored game content
into the simulation lab.

It is primarily written for Techniques, but its structure is also useful for
other simulator-facing artifacts such as infections, poisons, trap packages,
and future status families.

The purpose of this workflow is not just to create `sim/data` entries. Its
purpose is to make simulation coverage explicit, classify runtime gaps
correctly, and keep simulator work aligned with authority and doctrine.

It should also make one thing operationally explicit:

- `sim_defined` is not enough for serious balance review
- a Technique should normally reach `runtime_supported` before it is treated as
  a complete balance subject rather than a doctrinal estimate
- a Technique should normally define at least one saved balance question before
  it is treated as fully validated rather than merely executable

## Purpose

Use this workflow when:
- porting an authored Technique into `sim/data`
- deciding whether a Technique is already simulable
- extending runtime to support a currently-authored effect
- moving a Technique from `authored` toward `question_ready`
- auditing whether current simulator coverage is honest

Do NOT use this workflow as owner when the run must also produce publication
artifacts (corebook entry, technique card). In that case use
`technique-workflow` as owner with `simulation-port-workflow` linked.
This workflow is sim-only. Publication is out of its scope.

## Relationship to authority

The simulator does not own the rules.

Authority remains in:
- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`

The simulator consumes normalized, reduced, or staged representations of those
rules.

Therefore a porting pass must never silently invent authority.

If the authored Technique is ambiguous, the correct result is one of:
- resolve the ambiguity in authority first
- classify the port as `authority_blocked`
- split the work so that only the clearly-supported portion is ported

## Required layers

Every simulation-port pass should rely on:
- the `Knowledge Layer`
- the current technique authority
- the simulator domain model and roll model
- the porting plan and coverage state
- explicit review lenses instead of mixed ad hoc reasoning

## Core lenses

### `continuity_lens`
Checks:
- whether the Technique being ported matches current authority
- whether existing simulator seeds already cover part of the same surface
- whether previous coverage claims remain true

### `system_lens`
Checks:
- roll family
- competency source
- duration model
- clearing / consumption / expiry route
- whether the Technique is really immediate, procedural, concealment-based, or ailment-based

### `dependency_lens`
Checks:
- which simulator subsystems the Technique depends on
- whether the required upstream runtime is already present
- whether a missing subsystem blocks honest porting

### `simulation_lens`
Checks:
- what part can be represented in `sim/data`
- what part needs runtime support
- whether a policy can ever choose it meaningfully
- whether a scenario can expose it meaningfully

### `balance_lens`
Checks:
- whether the Technique’s port preserves its intended pressure profile
- whether a simplification would distort cost or tactical value too much

## Porting states

Every authored Technique should move through these states explicitly:

1. `authored`
2. `sim_defined`
3. `runtime_supported`
4. `policy_exercisable`
5. `scenario_tested`
6. `question_ready`

These are not vibes. They are coverage claims and should only be asserted when
true.

## Runtime support as a gate

For workflow purposes, `runtime_supported` is a real gate, not a soft note.

That means:

- `sim_defined` means the Technique exists in simulation-facing data
- `runtime_supported` means the engine can resolve its core behavior honestly
- strong balance review should normally happen **after** `runtime_supported`
- before that point, only provisional doctrinal cost review is safe

This keeps the project from balancing imagined behavior instead of implemented
behavior.

## Runtime gap classifications

Every porting pass should classify the current gap as exactly one primary type:

- `data_only`
- `small_runtime_extension`
- `new_state_family`
- `new_subsystem`
- `authority_blocked`

### Meanings

#### `data_only`
The engine already has everything necessary. The remaining work is:
- `sim/data` definition
- optional policy/scenario/question wiring

#### `small_runtime_extension`
The engine is almost ready, but one bounded addition is still needed.

Examples:
- one effect id
- one exchange-time modifier
- one expiry hook
- one small targeting helper

#### `new_state_family`
The Technique needs a new reusable family of states or markers.

Examples:
- wound-fouled
- signal-blurred
- read-marked
- route-spoiled

#### `new_subsystem`
The Technique depends on a larger runtime surface that does not yet exist.

Examples:
- richer treatment logic
- corridor trap logic
- shared quarantine logic
- multi-observer route contamination

#### `authority_blocked`
The authored material is not yet precise enough to port honestly.

In this case the correct action is not “fake it in sim.” The correct action is
to resolve the authority first.

## Phase order

## Phase 0. Intake

Inputs:
- target artifact
- authority file references
- current simulation coverage state
- purpose of the port

Outputs:
- port work card
- current porting state
- main simulation question
- mandatory source files

## Phase 1. Authority Read

Primary lenses:
- `continuity_lens`
- `system_lens`

Questions:
- What does the Technique actually do in authority?
- What does it not do?
- What part is immediate?
- What part persists?
- What part depends on another rule family?

Outputs:
- authority summary
- list of exact mechanical claims
- list of explicit non-claims

This phase is where false shortcuts should die early.

## Phase 2. Surface Mapping

Primary lenses:
- `system_lens`
- `dependency_lens`

Questions:
- Which simulator surfaces already exist that map to this Technique?
- Does it belong to:
  - exchange
  - ailment
  - concealment
  - reaction
  - procedural state
  - movement
  - treatment
  - trap logic
- What exact runtime components would need to be touched?

Outputs:
- surface map
- dependency map
- provisional runtime gap classification

## Phase 3. Porting Decision

Primary lenses:
- `simulation_lens`
- `balance_lens`

Questions:
- Can the Technique be ported honestly right now?
- If yes, how much of it?
- If not, what exactly blocks it?
- Would a simplification preserve or distort its intended tactical shape?

Outputs:
- one of:
  - port now
  - split port
  - block on authority
  - block on runtime
- final runtime gap classification

## Phase 4. Data Definition

This is the first execution phase.

Tasks may include:
- add or update `sim/data/techniques/*.yaml`
- bind:
  - `id`
  - `origin`
  - `rhythm`
  - `attrition`
  - `trigger`
  - `roll`
  - `effects`
  - `duration_model`
  - restrictions and notes

Questions:
- What is the minimal honest simulation-facing definition?
- What explicit note is needed if the port is partial?

Outputs:
- `sim_defined` data entry

## Phase 5. Runtime Integration

Only do the runtime work that the gap classification actually demands.

Possible work:
- add an effect id
- add an exchange modifier
- add an expiry rule
- add a procedural state family
- add a new subsystem hook

Questions:
- What is the smallest honest runtime change?
- Is the behavior reusable?
- Does this belong in a general surface or as a one-off hack?

Outputs:
- runtime support implementation
- updated runtime status

### Runtime support criteria

Do not mark a Technique as `runtime_supported` unless all of these are true:

- its core roll path resolves in engine
- its primary effect path resolves in engine
- its expiry / cleanup / consumption path is honest enough for the authored behavior
- the implementation is not a knowingly distorting placeholder
- at least one focused runtime or loader validation exists for the ported behavior

If these are not true, keep the state at:

- `sim_defined`

and keep the gap explicit.

### Runtime support outcome

Phase 5 should end in exactly one of these states:

- `runtime_supported`
- `runtime_partial`
- `runtime_blocked`

#### `runtime_supported`

The engine resolves the Technique honestly enough for downstream scenario and
balance work.

#### `runtime_partial`

Part of the Technique is real in runtime, but a meaningful portion is still
missing, distorted, or manually assumed.

This is still **not** `runtime_supported`.

#### `runtime_blocked`

The runtime gap is still too large or upstream-dependent to implement in this
run.

## Phase 6. Policy Exercise

Questions:
- Can at least one policy choose this Technique intelligibly?
- If not, is the blocker:
  - no policy support
  - no scenario support
  - no real decision condition yet

Outputs:
- `policy_exercisable` true or false
- explanation if false

Important:
Not every port needs a rich policy immediately, but the lack of policy support
should be recorded honestly.

## Phase 7. Scenario Exposure

Questions:
- Is there a meaningful scenario where this Technique can actually matter?
- Does such a scenario already exist?
- Does it need a minimal new scenario?

Outputs:
- `scenario_tested` true or false
- scenario id or scenario gap

## Phase 8. Question Definition

Questions:
- What repeatable design question does this port unlock?
- What is the **minimum cost question** this Technique must answer about
  `Rhythm` and `Attrition`?
- Is it already useful for:
  - probability
  - tempo
  - pressure
  - survivability
  - counterplay
  - comparative species testing
- Does the Technique justify additional derived questions because of its effect
  family?

Minimum rule:

- every Technique should normally leave this phase with at least one saved
  question about whether its current `Rhythm` / `Attrition` pair is justified
  relative to a meaningful reference

Typical references:

- base action baseline
- sibling Technique in the same origin
- next lighter / next heavier step in the same ladder
- a direct alternative that trades damage for control, geometry, or persistence

### Derived question triggers

If the Technique uses one of these surfaces, create or queue at least one
derived question for that surface:

- `ailments`
  - persistence, cleanup/recovery burden, activation pressure
- `concealment`
  - gain rate, detection rate, crossing success
- `procedural states`
  - persistence, cleanup path, effective burden frequency
- `reactions`
  - trigger frequency, opportunity rate, cost efficiency
- `positioning` or `geometry`
  - meter/angle swing, line recovery, path denial
- `breaking`, `zones`, or `parts`
  - disable rate, downstream tactical consequence, swinginess
- `kits`, `residues`, or consumable setup`
  - whether access friction or cleanup burden already constrains value enough

Outputs:
- `question_ready` true or false
- minimum cost question
- derived question set
- question seed or question gap

## Phase 9. Validation

Validation may include:
- loader tests
- runtime tests

Questions:
- Does the loader read the data definition correctly?
- Does the runtime behavior actually resolve as authored?
- If the Technique is still not `runtime_supported`, is that limitation stated
  explicitly?
- Does the Technique now have at least one saved cost question?
- If it opens a clearly distinct effect surface, does it also have the right
  derived question or an explicit pending gap?

Outputs:
- validation status
- runtime gate result confirmed or denied

## Phase 10. Balance Handoff

Questions:
- Has this Technique reached `runtime_supported`?
- If yes, is it ready for serious balance review?
- If not, is the next cost discussion only doctrinal / provisional?
- Does the `cost_note` in `techniques.yaml` match the structured `rhythm_cost` / `attrition_cost` fields?

Outputs:
- `ready_for_balance_review`
- or `doctrinal_only_until_runtime_supported`

Rule:

Do not treat a Technique as fully balance-review-ready just because it is
`sim_defined`.

Cost arbitration rule: when simulation validates or changes a cost, the
structured `rhythm_cost` / `attrition_cost` fields are the binding record.
The `cost_note` must be updated to match before the port is considered closed.
A `cost_note` that states a different cost than the structured fields is a
documentation error, not a design ambiguity.
- exchange tests
- policy tests
- scenario tests
- end-to-end question execution

Outputs:
- validated port
- explicit failure mode if validation fails

## Phase 10. Coverage Update

Update the relevant coverage records:
- technique coverage state
- species coverage counts
- runtime gap notes
- backlog priority if the Technique remains partially blocked

This may touch:
- simulator plan documents
- knowledge registries
- future workload notes

## Phase 11. Change Impact Record

Every porting pass should record:
- files changed
- runtime surfaces touched
- new reusable abstractions introduced
- what the Technique now proves in the simulator
- what still remains unsupported

## Acceptance criteria

A Technique port should only be considered “closed for this pass” when its
status is explicit.

Suggested closure checklist:
- `authority_read_complete`
- `surface_map_recorded`
- `gap_classified`
- `sim_data_updated` or blocked explicitly
- `runtime_updated` or blocked explicitly
- `tests_added_or_updated`
- `coverage_state_updated`
- `pending_items_explicit`

## Good outputs

A good simulation-port pass leaves behind:
- honest coverage
- explicit runtime classification
- reusable runtime abstractions when appropriate
- no fake completeness
- no hidden dependency assumptions

## Bad outputs

A bad simulation-port pass leaves behind:
- “sim-ready” claims without real runtime support
- partial ports that pretend to be complete
- one-off hacks with no declared surface
- silent authority invention
- coverage matrices that no longer match reality

## Relationship to the technique workflow

This workflow is a companion to:
- [Technique Workflow](./technique-workflow.md)

The technique workflow governs the whole artifact lifecycle.
This simulation-port workflow governs the simulator-facing branch of that
lifecycle in detail.
