---
name: "technique-authoring"
description: "Use when authoring, revising, backfilling, or closing a Technique in project authority. Follow the project workflow, phase checkpoints, dependency review, balance review, simulation framing, and closure discipline instead of editing technique files ad hoc."
---

# Technique Authoring

Use this skill when the task is to create, revise, backfill, normalize, or close one or more Techniques in project authority.

This skill is for Technique work specifically. It does not replace broader authority revision, status-family work, or simulation-port work. Instead, it anchors the technique run to the correct workflow, makes the required checkpoints explicit, and routes outward when the work crosses into other workflows.

## Authoring stance

This skill is **fantasy-first** and **combat-first**.

Do not begin new Technique work by shrinking the idea to whatever the current
mechanics or simulator already support.

Begin by preserving:

- the species-true fantasy
- the concrete tactical moment **in ATB combat** — this is the primary design target
- the held identity of the move

**Combat-first rule:** Every new Technique must be designed for ATB combat use
as its primary case. Exploration or investigation utility is a valid secondary
benefit but is not a sufficient primary use on its own. If a Technique works
only outside combat, the run must explicitly document why that is the correct
design before proceeding — it is not a default.

Then use the workflow to ground that fantasy in the system.

The right order is:

1. fantasy
2. authority
3. dependency check
4. bounded system expansion if justified
5. simulation / publication surfaces

Reasonable bounded expansions opened by a Technique may include:

- kit families
- ailment-family extensions
- grievance or burden surfaces
- procedural states
- cleanup / treatment paths
- other reusable subsystem pieces of similar scale

Do **not** treat one Technique as automatic justification for inventing an
entire large mechanic family or macro-system. If the needed support is too
large, record that explicitly instead of mutilating the fantasy or pretending
the support already exists.

## When to use this skill

Use `$technique-authoring` when the user asks for things like:

- create a new Technique
- revise an existing Technique in `techniques.md` or `techniques.yaml`
- backfill older Techniques so they match current doctrine
- clean wording, mechanics, or taxonomy for one Technique
- port a Technique through the authoring side before simulation or core sync
- audit whether a Technique is actually "closed"

Do not use this skill as the primary skill when the true owner is another workflow:

- use `authority-revision-workflow` first when the rule problem is upstream and the Technique is only a symptom
- use `status-family-workflow` first when the work is really about infections, poisons, elixirs, traps, or another repeated family
- use `species-audit-workflow` first when the user wants a full species pass rather than one Technique
- use `simulation-port-workflow` after authoring when the main task becomes simulator coverage
- use `core-sync-workflow` after authoring when the main task becomes publication synchronization

## Required workflow discipline

This skill does not allow ad hoc Technique editing. Every run must be grounded in the project workflow layer.

Start with these project documents:

- `docs/workflows/workflow-execution.md`
- `docs/workflows/technique-workflow.md`
- `docs/workcards/technique-workcard-template.md`

Then read only the additional workflow docs that the run actually needs:

- `docs/workflows/dependency-review-workflow.md`
- `docs/workflows/balance-review-workflow.md`
- `docs/workflows/simulation-port-workflow.md`
- `docs/workflows/core-sync-workflow.md`
- `docs/workflows/authority-revision-workflow.md`

Use the knowledge layer before relying on long chat history:

- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-design/knowledge_access/`

## Execution pattern

Treat each Technique task as a run with an owner workflow and explicit checkpoints.

### 1. Claim workflow ownership

Before editing, identify whether `technique-workflow` is truly the owner.

If the request is actually blocked by upstream rule ambiguity, switch ownership to `authority-revision-workflow` or run dependency review before touching authority text.

### 2. Instantiate the work card

Use `docs/workcards/technique-workcard-template.md` as the run structure.

You may instantiate it as:

- an actual work card file for substantial work
- or a strict internal checklist if the task is small

Do not skip its sections. The work card is what keeps the run from collapsing back into improvisation.

### 3. Advance by phase, not by intuition

Move through the technique workflow in order:

1. Intake
2. Species Framing
3. Mechanical Framing
4. Dependency Framing
5. Balance Framing
6. Simulation Framing
7. Editorial Framing
8. Integration
9. Validation
10. Acceptance Closure
11. Change Impact Record

Do not jump straight into file edits unless the earlier phases are already stable and recoverable from project state.

For new Technique creation, make sure the early phases preserve the original
fantasy before dependency or simulation pressure starts trimming it.

### 4. Route when the run crosses boundaries

If the Technique run exposes a real cross-workflow dependency, do not fake completion.

Examples:

- if the Technique depends on unresolved wound-treatment doctrine, route through `dependency-review-workflow`
- if the Technique needs simulator coverage, route into `simulation-port-workflow`
- if the Technique changes published explanation, route into `core-sync-workflow`
- if the Technique reveals an upstream rules contradiction, route into `authority-revision-workflow`

### 5. Close explicitly

A Technique is not "done" because the prose looks better.

Close only when you can state:

- authority status
- YAML status
- simulation status or precise gap classification
- publication sync status
- pending items, if any
- change impact

### 6. Treat validation as a formal check battery

Do not let validation collapse into "the agent thinks it looks correct."

Run validation as explicit check families and record each as:

- `pass`
- `fail`
- `not_applicable`
- `blocked`

Minimum families to consider:

- `roll_integrity`
- `surface_integrity`
- `exchange_integrity`
- `ailment_integrity`
- `critical_break_integrity`
- `atb_integrity`
- `dependency_integrity`
- `simulation_integrity`
- `balance_sanity`
- `loader_validation`
- `scenario_validation`
- `question_validation`
- `publication_consistency`

Not every Technique will use every family, but the run should explicitly mark
which ones were applicable and what their result was.

## What to produce in a good Technique run

A strong Technique run should leave behind:

- clean authority text in the right source files
- synchronized structured data when required
- explicit dependency and balance notes
- simulation framing or port status
- closure state with no vague "almost done"

At minimum, capture:

- fantasy
- irreducible fantasy statement
- world origin
- why-not-base-action
- interaction surfaces
- trigger
- requirements
- target/range/area
- rhythm/attrition
- roll model
- effect model
- duration / expiry / restrictions
- dependency map
- bounded-expansion decision
- balance sanity check
- simulation gap classification
- minimum cost question requirement
- derived question triggers if applicable
- editorial sync note
- acceptance status
- change impact

## Card prose rules

These apply to the HTML card effect section and to publication core entries. They do not apply to YAML or authority docs.

### Setting tone

This is a dark survival game. Players are the weakest actors in an overwhelming world. The setting draws from cosmicism — old, vast, indifferent forces — but the goal is not generic Lovecraft pastiche. The tone earns its darkness through physical precision and concrete detail, not through adjectives or abstraction. Flavor text must reflect this. Effect text must remain clear and functional.

### Two zones

Technique cards have two zones that never mix — treat them like Magic: The Gathering cards:

**Flavor text** — one or two lines in the voice of the world. It evokes the feeling of using the technique from inside the fiction. It never explains the mechanic. It never mentions dice, rolls, bonuses, or conditions.

**Effect text** — the complete rule written in narrative prose, second person, present tense. The card speaks directly to the player: "realizas", "recibes", "el objetivo". It is not an algorithm or a labeled sequence. It is a description of what happens, in the order it happens, with mechanical vocabulary placed in normal sentences. A bonus is written as "un bonificador igual a tu rango de X" — never as "+[rango de X]". An outcome is written as "con éxito, el objetivo..." — never as "Éxito: objetivo → Y".

Specific rules:

- **Second person only.** Write "tú" / "tu" — never "el usuario" or "the user". The card speaks directly to the player.
- **No bracket notation.** Never write `+[rango de X]` or `−[rango de X]`. Write "un bonificador igual a tu rango de X" or "una penalización igual a tu rango de X".
- **No "bonus".** Use "bonificador" in all card prose. "bonus" belongs only in YAML.
- **No YAML-style labels in prose.** "Éxito:", "Fallo:", "Dispara cuando" are internal authoring shorthand. In the card, the rule must read as continuous prose.
- **No design-intent explanations.** Never write "esto convierte X en la opción más eficiente" or "esto hace que sea más atractivo atacar al usuario". The rule produces that effect — the card does not explain it.
- **No docstring tone.** If the effect reads like a function description, rewrite it as a rule a player reads at the table. Short, present tense, no parentheticals explaining why.
- **Flavor text must be atmospheric, not descriptive.** Flavor explains the fiction, not the mechanic. "El objetivo cambia el peso para irse" is flavor. "Esta técnica dispara cuando el objetivo intenta moverse" is not.

For the full flavor text rules, effect text structure, and canonical language patterns, see `technique-play-surface` Prose rules.

## Quality rules

- Do not treat conversation memory as the primary authority when project authority exists.
- Do not rewrite ailments, concealment rules, or other inherited subsystems inside the Technique unless the workflow has established that the Technique must own that logic.
- Prefer inheritance from existing doctrine over repeating full rule payloads.
- Separate "Technique not closed because authority is ambiguous" from "Technique not closed because simulation support is missing."
- If a blocker is upstream, name it explicitly instead of forcing a local patch.
- If a Technique is ready only in authority but not in simulation, say so precisely using the project runtime-gap language.
- Do not treat a Technique as strongly validated if it still lacks its saved
  minimum cost question.
- If the Technique's value depends on ailments, concealment, procedural states,
  reactions, geometry, breakage, kits, or residues, make sure the run names the
  derived question family that should eventually test that surface.
- Keep the user informed in plain language, but do not skip workflow checkpoints internally.
- Do not summarize validation as a vibe check; validation must be recorded as explicit system checks.

## Runtime gap language

When simulation framing is relevant, classify the gap precisely:

- `data_only`
- `small_runtime_extension`
- `new_state_family`
- `new_subsystem`
- `authority_blocked`

Do not invent softer labels like "almost simulable" when one of the formal categories fits.

## Suggested file touch order

In many runs, this order works well:

1. read workflow docs and authority sources
2. inspect knowledge layer and current technique state
3. resolve dependency and balance framing
4. edit authority text
5. edit structured YAML if required
6. route into simulation or core sync only if needed
7. validate (run `python3 pipeline/scripts/validate_techniques.py` and ensure zero errors)
8. record acceptance and impact

## Reference map

Use these local references as your first map:

- `references/workflow-map.md`
- `references/checkpoints.md`

Then open the actual project workflow docs named there.
