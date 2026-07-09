# Technique Play Surface Workflow

This document defines the canonical workflow for converting a Technique that is
already stable enough in authority into its **final play-facing surfaces**.

Those surfaces are:

- the **corebook-facing final technique entry**
- the **card-facing final technique entry**

Its job is not to author the Technique from scratch and not to port it into the
simulator. Its job is to transform an already-authored Technique into the
formats that players actually read at the table.

## Purpose

Use this workflow when:

- a Technique already exists in authority and needs its final player-facing form
- a Technique needs to become a real corebook entry instead of only an
  authority record
- a Technique needs a tarot-card surface aligned to the final core wording
- a Technique currently exists in design language that is too heavy, too
  internal, or too authoring-oriented for play
- core and card need to be kept semantically aligned while allowing different
  density

Do not use this workflow as the primary owner when:

- the Technique itself is still unstable in authority
- the Technique still needs upstream rule clarification
- the main problem is simulator coverage
- the main problem is publication drift after an already-finalized play surface

In those cases, route first through:

- `technique-workflow`
- `authority-revision-workflow`
- `simulation-port-workflow`
- `core-sync-workflow`

## Relationship to other layers

This workflow sits **between authority and publication artifacts**.

It assumes:

- authority lives in `Transcendence-design/docs/system/techniques.md`
- structured authority lives in `Transcendence-design/data/system/techniques.yaml`

It produces or updates:

- corebook technique entries
- technique-card source files
- technique print-sheet surfaces

This workflow does **not** make corebook and cards into new authorities.

## Required layers

Every play-surface pass should rely on:

- the `Knowledge Layer`
- the current authority Technique source
- the current card and publication surfaces
- the current technique-play-surface specification

Key references:

- `Transcendence-design/docs/system/technique-play-surface.md`
- `Transcendence-publications/core-books/transcendence-techniques/es/`
- `Transcendence-publications/technique-cards/transcendence-technique-cards/`

## Core lenses

### `species_lens`
Checks:
- whether the flavor line sounds like the species or tradition that owns the Technique
- whether the voice feels remembered, practiced, or taught instead of generically dramatic
- whether the line carries one strong image rather than diffuse abstraction

### `system_lens`
Checks:
- whether the play-facing block still states the mechanic honestly
- whether a field belongs in final surface or only in authority
- whether saving roll, impact, requirements, and effect are expressed correctly

### `editorial_lens`
Checks:
- readability
- compression quality
- player-facing clarity
- whether flavor text, requirements, and effect are legible at a glance
- whether publication language is fully localized instead of leaking authority-side English labels
- whether roll and payload notation follows the player-facing standard of the publication language
- whether ordinary player-facing words remain complete instead of being shortened for layout

### `continuity_lens`
Checks:
- whether core and card still describe the same Technique
- whether the final surface still reflects the current authority
- whether abbreviations and field order remain consistent across entries

### `dependency_lens`
Checks:
- whether the Technique depends on another unresolved subsystem to be surfaced honestly
- whether core entry and card source must move together
- whether the print sheet needs updating once the card source changes

### `balance_lens`
Checks:
- whether compression accidentally hides a real balance caveat
- whether the surface makes the cost, window, and counterplay readable enough for play

## Surface model

The canonical final play-facing structure is:

1. `Type - Category`
2. `Name`
3. `Competency Rank`
4. `Flavor Text`
5. `Range`
6. `Area`
7. `Duration`
8. `Primary Roll`
9. `Saving Roll` if applicable
10. `Impact` if applicable
11. `Rhythm`
12. `Attrition`
13. `Requirements`
14. `Keywords`
15. `Effect`

Core and card should carry the same semantic structure.

The difference should be:

- **core:** more breathing room, slightly fuller wording
- **card:** stronger compression, faster scan speed

## Phase order

## Phase 0. Intake

Inputs:

- target Technique
- current authority source
- current publication/card state
- purpose of the pass

Outputs:

- play-surface work scope
- source file list
- current surface status

Questions:

- Is the Technique stable enough in authority?
- Does a final core entry already exist?
- Does a card source already exist?
- Is this a first-surface pass or a revision pass?

## Phase 1. Authority Confirmation

Primary lenses:

- `system_lens`
- `continuity_lens`

Questions:

- What is the current authoritative Technique payload?
- Which fields are authority-only?
- Which fields should survive into the play surface?
- Does the authority still contain ambiguity that makes final play text unsafe?

Outputs:

- authority baseline
- surface-eligible field list
- explicit blocker if authority is not stable enough

## Phase 2. Surface Shaping

Primary lenses:

- `species_lens`
- `system_lens`
- `editorial_lens`

Questions:

- What should the top-line classification be in final play?
- Does the flavor text sound like a line the owning species or tradition would actually say?
- Is the flavor text carrying one strong image or one strong maxim instead of paraphrasing the effect?
- Does the flavor text avoid inflated or generic AI-sounding abstraction?
- Is the flavor text short, declarative, and physically or tactically grounded enough to be memorable at a glance?
- Which requirements are true game mechanisms and which are only authoring or common-sense constraints?
- For an `Active` Technique, is any listed requirement actually only tactical context rather than a formal gate?
- Does the Technique depend on a named kit family that must appear explicitly on the final surface?
- Which keywords add real information rather than repeating existing fields?
- Does the effect text say only what players need to resolve the Technique?
- Does the wording remain mechanically exact, without adding approximation that authority does not contain?
- Do all player-facing labels match the language of the publication surface instead of reusing internal authority terms?
- Are roll names and payload labels localized to the publication standard instead of copied from authority shorthand?
- Are ordinary player-facing words kept complete instead of being shortened for layout?
- If something remains abbreviated, is it canonical rules notation rather than ad hoc compression?
- If the Technique creates a mark, residue, snag, foul, or similar clearable state, is the cleanup path explicit and tied to `Interactuar`, `Usar Especialización`, or another real subsystem response?

Outputs:

- final field payload for core/card
- compression decisions
- abbreviation decisions for card use

Examples of valid compression:

- `Instantáneo` -> `Inst.` on card
- `1 criatura` -> `1 criat.` on card

The core version may keep the fuller wording if space allows.

Non-negotiable rule:

- compression may shorten wording
- compression may not weaken exactness
- if authority says `1 meter`, the final surface must not say `approximately 1 meter`
- flavor text may be compressed, but should not lose species voice or collapse into generic dramatic filler
- short, concrete doctrine lines are preferred over ornate metaphor
- localization may map authority labels into the publication language, but should not change the underlying mechanic
- notation may change from internal shorthand to player-facing naming, but should not change the underlying mechanic

## Phase 3. Core Surface Integration

Primary lenses:

- `editorial_lens`
- `continuity_lens`

Questions:

- Where does this Technique belong in the core section?
- Is it only an example, or is it a real entry in the technique list?
- Does the core version read like a player-facing rules object rather than a design note?

Outputs:

- updated core technique entry
- updated section README or index if needed

## Phase 4. Card Surface Integration

Primary lenses:

- `editorial_lens`
- `dependency_lens`

Questions:

- Does the card source exist as an individual file?
- Does it render as a standalone card correctly?
- Is the print-sheet surface aligned with the card source?
- Do layout abbreviations preserve meaning?

Outputs:

- updated individual card source
- updated print sheet if needed
- explicit note if the print sheet intentionally remains partial

## Phase 5. Alignment Review

Primary lenses:

- `continuity_lens`
- `system_lens`

Questions:

- Do authority, core, and card still say the same Technique?
- Did compression change the mechanic?
- Did category, requirements, or keywords drift from the agreed final surface rules?
- Did any English authority labels leak into a Spanish-facing surface, or vice versa?
- Did internal roll abbreviations leak into a surface that should use localized player-facing notation?

Outputs:

- alignment result
- explicit drift note if unresolved

## Phase 6. Validation

Validation may include:

- manual reading pass
- card preview pass
- print-sheet preview pass
- core readability pass
- cross-check against authority

Outputs:

- validated surface pair
- or explicit pending list

## Phase 7. Acceptance Closure

Suggested closure checklist:

- `authority_confirmed`
- `core_surface_created_or_updated`
- `card_surface_created_or_updated`
- `core_card_alignment_checked`
- `abbreviations_consistent`
- `pending_items_explicit`

## Phase 8. Change Impact Record

Every pass should leave a compact note of:

- authority source used
- core files changed
- card files changed
- print-sheet implications
- unresolved follow-up

## Typical output set

A strong pass should leave behind:

- one finalized core entry
- one finalized card source
- one aligned print-sheet state
- explicit note of whether the Technique is now fully surfaced or still partial

## Good execution

Good play-surface execution leaves behind:

- player-facing text instead of design-facing language
- aligned core and card semantics
- compact but honest requirements
- keywords that carry real information
- a print-ready path that does not depend on reading giant authority records

## Bad execution

Bad play-surface execution leaves behind:

- authority notes copied directly into the core
- cards that repeat internal taxonomy or pseudo-requirements
- card-only abbreviations that change meaning
- core and card saying different things
