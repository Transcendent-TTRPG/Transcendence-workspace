---
name: "technique-play-surface"
description: "Use when an authored Technique must be converted into aligned final play-facing surfaces for the corebook and technique cards. Follow the play-surface workflow instead of copying authority text directly into publication artifacts."
---

# Technique Play Surface

Use this skill when the task is to turn an already-authored Technique into the
formats players actually read at the table:

- a corebook-facing final technique entry
- a card-facing final technique entry

This skill does not author the Technique from scratch and does not port it into
the simulator. It transforms stable authority into final play-facing surfaces.

## When to use this skill

Use `$technique-play-surface` when the task is to:

- convert a Technique from authority into a real corebook entry
- convert a Technique into a tarot-card surface
- align core and card wording so they say the same thing
- compress authoring-heavy language into player-facing language
- replace pseudo-requirements with real game-mechanism requirements
- decide which fields survive into final play surface

Do not use this skill as the primary owner when:

- the Technique is still unstable in authority
- the task is still authoring or revising the Technique itself
- the task is simulator coverage rather than player-facing presentation
- the task is publication drift after a final play surface already exists

In those cases, route first through:

- `technique-workflow`
- `authority-revision-workflow`
- `simulation-port-workflow`
- `core-sync-workflow`

## Required workflow discipline

Every play-surface run must be grounded in the play-surface workflow layer.

Start with:

- `docs/workflows/workflow-execution.md`
- `docs/workflows/technique-play-surface-workflow.md`

Then open only the additional docs the run actually needs:

- `Transcendence-design/docs/system/technique-play-surface.md`
- `docs/workflows/technique-workflow.md`
- `docs/workflows/core-sync-workflow.md`
- `docs/workflows/authority-revision-workflow.md`
- `docs/workflows/dependency-review-workflow.md`

Read actual surfaces directly:

- `Transcendence-publications/core-books/transcendence-corebook/09-techniques/`
- `Transcendence-publications/technique-cards/transcendence-technique-cards/`

## Execution pattern

Treat each run as a transformation from one stable source into two aligned final
surfaces.

### 1. Confirm authority stability

Before writing core or card text, confirm that the Technique is stable enough
in:

- `Transcendence-design/docs/system/techniques.md`
- `Transcendence-design/data/system/techniques.yaml`

If authority is still ambiguous, stop and route back upstream. Do not finalize
surface wording around unresolved mechanics.

### 2. Build the play-facing payload

Shape the Technique into the canonical play-facing structure:

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

Do not allow authoring scaffolding to leak through unchanged.

### 3. Separate survival fields from authority-only fields

Keep only what players need in play.

Usually keep:

- operational classification
- cost
- trigger-facing requirements
- tactical surfaces
- fast effect wording

Usually remove from final surface:

- world-origin payload in full
- cost note essays
- simulator implications
- "why this is not a base action"
- authoring notes
- broad common-sense restrictions that are not real tracked mechanics

For `Active` Techniques specifically:

- do not promote ordinary tactical context into a formal `Requirements` line
- keep `Requirements` for real access or rules gates
- leave contextual use logic in trigger understanding or effect wording unless
  the system truly tracks it as a requirement

### 4. Produce both surfaces from the same semantic payload

The core and card should carry the same meaning.

The difference is density:

- **core:** more breathing room, slightly fuller wording
- **card:** stronger compression and abbreviation when needed

If the card says something materially different from the core, the run is not
closed.

### 5. Control compression explicitly

Compression is allowed only when meaning survives.

Examples:

- `Instantáneo` -> `Inst.`
- `1 criatura` -> `1 criat.`

Compression should not:

- hide a requirement
- hide a saving roll
- change target scope
- erase meaningful timing
- turn an exact rule into an approximate one

If authority is exact, the final surface must stay exact.

### 6. Keep card source and print sheet distinct

The card layer should distinguish:

- **one card per source file**
- **one or more print sheets** composed from those sources

The skill should update whichever of these are actually affected and record if
the sheet remains intentionally partial.

### 7. Close only after alignment review

A run closes only when:

- authority matches the final surface
- core matches the final surface
- card matches the final surface
- abbreviations do not change meaning

## Quality rules

- Do not copy authority text into the core verbatim if it still sounds like design prose.
- Do not let cards become shorthand that changes the Technique's real meaning.
- Do not keep fake requirements that are only common-sense scene logic.
- Do not list contextual combat pressure as a formal requirement for an `Active` Technique unless the game explicitly tracks it as one.
- Do not repeat top-line fields as keywords unless the keyword adds new system information.
- Do not let core and card diverge semantically.
- Do not add approximation language where authority is exact.
- Use final play-facing language, not pipeline language, in publication artifacts.

## Typical outputs

A strong run should leave behind:

- one finalized core entry
- one finalized individual card source
- one aligned print-sheet state
- explicit note of whether the surface pair is fully closed or still partial

## Suggested sequence

In many runs, this order works well:

1. confirm authority
2. extract the play-facing payload
3. compress and normalize requirements/keywords/effect
4. update the core entry
5. update the card source
6. update the print sheet if needed
7. run alignment review
8. record closure state

## Reference map

Use these local references first:

- `references/surface-map.md`
- `references/surface-checks.md`

Then open the actual project documents named there.
