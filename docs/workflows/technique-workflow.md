# Technique Workflow

This document defines the canonical workflow for creating, revising, porting,
and validating Techniques across authority, simulation, and publication.

It is designed for high-context iterative work. It does not assume that every
Technique will be simulable immediately, but it does require that unresolved
gaps be classified explicitly instead of left ambiguous.

## Foundational stance

This workflow is **fantasy-first, combat-first, then system-grounded**.

A new Technique should not begin as "what can current mechanics already
support?" It should begin as:

- a species-true fantasy
- a concrete tactical moment **in ATB combat** — this is the primary design target
- a real held identity the game wants to preserve

**Combat-first rule:** New Techniques must be useful in ATB combat as their
primary case. Exploration or investigation utility is a valid secondary benefit.
If a Technique is only useful outside combat, that must be explicitly justified
in Phase 1 — it is not a default.

Only after that should the workflow ask:

- what current mechanics already support it
- what bounded system expansion it legitimately needs
- and whether any missing support is small enough to author now

This means the workflow should allow a Technique to justify new support of
reasonable scale, such as:

- kit families
- grievance-like or burden-like status layers
- ailment-family extensions
- procedural states
- cleanup / treatment paths
- or other reusable subsystem pieces of similar scope

It should **not** assume that one isolated Technique is enough justification to
invent a full new macro-mechanic by itself.

The goal is to protect variety and species identity without allowing local
Technique work to sprawl into uncontrolled system growth.

## Purpose

Use this workflow when:

- authoring a new Technique
- revising an existing Technique
- porting an authored Technique into the simulator
- syncing a Technique-related rules change into publication

Serious balance closure for a Technique should normally happen only after the
linked simulation run reaches `runtime_supported`.

Serious validation closure should also normally require at least one saved
question, not just a runtime-capable implementation.

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
- explicit note on whether the run is fantasy-led new authoring, revision, or
  backfill

## Phase 1. Species Framing

Primary lens:

- `species_lens`

**Source:** Read the corebook species entry (`06-species/es/`) — not design seeds or internal notes. Seeds drift; the corebook entry is the identity the game has committed to.

Questions:

- Does this genuinely belong to the species?
- What behavior, culture, biology, or training justifies it?
- What should it explicitly avoid doing?
- What are its primary and secondary interaction surfaces?
- What is the irreducible fantasy of the Technique before mechanical trimming?
- Is this Technique useful in ATB combat? If not, is that a deliberate, explicitly justified design choice — or has combat utility been overlooked?
- **Biological layer:** what does the body do by nature that makes this Technique *possible*?
- **Doctrinal layer:** what did the species conclude from having that body — what doctrine, philosophy, or theology makes this Technique specifically *theirs*?
- **Primary design question:** what does this species know that other species cannot know? What exclusive knowledge, sense, or experience becomes the combat action?

Outputs:

- fantasy
- world origin
- why-not-base-action
- interaction surfaces
- irreducible fantasy statement
- biological justification (body as substrate)
- doctrinal justification (species interpretation of that body) — may be brief if the Technique is primarily biological
- combat utility statement: explicit note on whether and how the Technique applies in ATB, and if it does not, a documented justification

## Phase 2. Mechanical Framing

Primary lens:

- `system_lens`
- `continuity_lens`

Questions:

- **Profile space check (mandatory before designing):** What other Techniques share this weapon profile across all species? Map each one: trigger, resolution, output. What gap in that profile's design space does this Technique fill?
- **Cross-profile overlap check:** Are there Techniques with a different profile that are functionally similar — same trigger pattern, same output pattern? A Technique can repeat an existing one even if the profiles differ. What makes this Technique's output genuinely distinct from all of them?
- What kind of Technique is it?
- What roll does it use?
- What real competency feeds it?
- Does it use an ailment, concealment, procedural state, or immediate effect?
- What is its real duration?
- What restrictions are necessary?
- How is it cleared, consumed, or expired?
- Which parts of the fantasy survive directly into system form, and which parts
  still lack support?

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
- Does the Technique justify a bounded system expansion of reusable scale?
- If support is missing, is the right response:
  - classify a gap
  - add a small reusable subsystem piece
  - or stop because the needed expansion is too large for this run?

Outputs:

- dependency map
- linked file list
- upstream blockers if present
- decision on whether the Technique can close now or must be split
- bounded-expansion decision

## Phase 4. Balance Framing

Primary lens:

- `balance_lens`

Questions:

- Is the cost aligned with sibling Techniques?
- Is this being compared against sibling Techniques rather than base actions?
- How often should the Technique matter?
- Is its value immediate, setup-based, or persistent?
- If it is persistent, is the value coming from duration itself or from how
  broad the persistent effect really is?
- Is `Attrition` pricing current-combat strain incorrectly when it should be
  pricing continuity between hostile scenes instead?
- If this is a posture, is positional anchoring already paying part of the
  price?
- How oppressive is it if it lands?
- What counterplay exists?
- Does the Technique create a "next action / next roll" memory burden that
  should be redesigned before cost is finalized?

Outputs:

- cost sanity note
- sibling comparison note
- risk note for overpricing or underpricing
- future simulation targets if needed

Important:

This phase is allowed to produce a **provisional doctrinal reading** before full
simulation support exists.

It is not the same thing as final balance closure.

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
- minimum cost-question requirement

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

The intended downstream sequence is:

1. `sim_defined`
2. `runtime_supported`
3. `policy_exercisable`
4. `scenario_tested`
5. `question_ready`
6. serious balance review closure

At minimum, `question_ready` should usually mean:

- one saved question about whether the current `Rhythm` / `Attrition` pair is
  justified
- plus any obviously necessary derived question for the Technique's main
  secondary surface

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

Validation should be treated as a formal check battery, not as a vague agent
judgment.

Each validation family should end in one of these states:

- `pass`
- `fail`
- `not_applicable`
- `blocked`

Validation families:

### `roll_integrity`

Check:

- primary roll is expressed correctly
- saving roll appears only when it is a distinct negating roll
- impact appears only when a real payload exists

### `surface_integrity`

Check:

- core and card say the same thing
- exact rules stay exact
- requirements are real game mechanisms
- keywords do not merely repeat visible fields

### `exchange_integrity`

Check when relevant:

- `A.R.`
- `D.R.`
- `I.R.`
- block
- interruption
- reposition
- denial or stop logic

### `ailment_integrity`

Check when relevant:

- ailment family is correct
- severity is correct
- application condition is correct
- recovery / expiry / clearing logic is coherent

### `critical_break_integrity`

Check when relevant:

- critical-hit dependency is explicit
- break / durability / part-loss logic is not ambiguous

### `atb_integrity`

Check when relevant:

- active / reactive / passive timing window is honest
- Rhythm / Attrition are stated correctly
- the Technique is not described as firing in a window it does not actually have

### `dependency_integrity`

Check:

- no unresolved upstream subsystem is being silently assumed
- blockers are named explicitly if they exist

### `simulation_integrity`

Check when relevant:

- simulator definition matches authority
- runtime gap classification is honest
- runtime support is real if claimed

### `balance_sanity`

Check:

- sibling comparison still holds
- cost still matches intended pressure
- counterplay remains legible

### `loader_validation`

Static check:

- run `python3 pipeline/scripts/validate_techniques.py`
- require zero errors
- warnings should be explicitly accepted or resolved, not silently ignored

### `scenario_validation`

Check when relevant:

- scenario or focused runtime slice actually exposes the Technique behavior

### `question_validation`

Check when relevant:

- saved question is runnable and meaningfully targets the Technique
- every Technique normally has one minimum cost question
- Techniques with clearly distinct secondary surfaces also name the right
  derived question family

### `publication_consistency`

Check when relevant:

- publication surfaces reflect the same final payload
- no drift exists between authority, core, and card after the pass

Card prose check (apply to every HTML card and ES core entry):

- effect section uses second person ("tú") — never "el usuario"
- no "bonus" in prose — always "bonificador"
- no YAML-style labels ("Éxito:", "Fallo:", "Dispara cuando") in card text
- no design-intent sentences ("esto convierte X en la opción más eficiente")
- no docstring or function-description tone — the card is a rule a player reads at the table

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
- `minimum_cost_question_defined` or explicit blocker
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
