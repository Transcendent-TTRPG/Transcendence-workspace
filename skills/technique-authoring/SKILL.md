---
name: "technique-authoring"
description: "Use when authoring, revising, backfilling, or closing a Technique in project authority. Follow the project workflow, phase checkpoints, dependency review, balance review, simulation framing, and closure discipline instead of editing technique files ad hoc."
---

# Technique Authoring

Use this skill when the task is to create, revise, backfill, normalize, or close one or more Techniques in project authority.

This skill is for Technique work specifically. It does not replace broader authority revision, status-family work, or simulation-port work. Instead, it anchors the technique run to the correct workflow, makes the required checkpoints explicit, and routes outward when the work crosses into other workflows.

## Postura — definition

A technique is a **Postura** if and only if all three of the following hold:

1. **Sustained state** — it has `Permanente` duration and creates an ongoing beneficial effect.
2. **Player-maintained constraint** — the player actively cedes something to keep it active. The constraint must be something the player controls, not something an external actor can simply negate.
3. **Player agency in maintenance** — the player can choose to break it voluntarily, and can actively resist being forced out of it (usually via T.R.).

A permanent bonus that expires when an external condition changes (e.g., an enemy closes distance) is **not** a Postura — the player gave up nothing and has no agency in maintaining it.

### Types

| Type | Constraint ceded | Keyword | Cost pattern |
| --- | --- | --- | --- |
| **Postura inmóvil** | Movilidad — cannot voluntarily move while active | `Postura` | Ritmo 3 (positional lock is the price) |
| **Postura móvil** | Something other than mobility (equipment state, etc.) | `Postura` | Desgaste higher — cost paid upfront without positional restriction |

### Exclusivity rule

Only **one Postura** may be active at a time, regardless of type or source (weapon, armor, natural weapon, body). Activating a new Postura ends the previous one automatically.

### Keyword

Every technique of type Postura must carry `Postura` as a keyword in both the corebook entry and the technique card.

---

## Keyword — Hereda Efectos / No Hereda Efectos

Every species has natural weapons. Each natural weapon has an **Efecto** that fires under a specific trigger condition (margin ≥ 3, critical hit, second consecutive hit, any hit, etc.). This Efecto is an intrinsic part of the weapon — not the technique.

The `Hereda Efectos` / `No Hereda Efectos` keyword controls whether the natural weapon's Efecto is eligible to trigger during a technique's execution.

### What these keywords mean

**`Hereda Efectos`** — The technique resolves as a full weapon hit with T.I. The natural weapon's Efecto can trigger alongside the technique's own effect if its trigger condition is met.

**`No Hereda Efectos`** — The technique does not produce a full weapon hit with T.I., or uses the weapon contact for control/positioning without a full hit. The natural weapon's Efecto is suppressed regardless of the weapon's trigger condition.

### Mandatory prerequisite: the Impacto check

A technique can only carry `Hereda Efectos` if its stat block shows **Impacto: T.I.** — meaning the technique resolves a full hit with damage. If Impacto is `—`, the keyword must be `No Hereda Efectos`. This is a hard gate, not a default.

| Impacto | Technique type | Keyword |
| --- | --- | --- |
| `T.I.` | Activo - Ataque or Reactivo with full hit | proceed to cross-species check below |
| `—` | any attack or reactive with no damage | `No Hereda Efectos` |
| any | Activo - Utilidad | omit keyword entirely |
| any | Pasivo - Resistencia | omit keyword entirely |

### Cross-species balance check (required when Impacto = T.I.)

Techniques are open to any character with the right weapon profile — not just the species they originate from. The keyword decision is therefore a statement about **all natural weapons that share the technique's profile**, not just the design species.

Before assigning `Hereda Efectos` to a technique with T.I., map every natural weapon with that profile and ask: does [technique effect] + [this weapon's Efecto] produce an acceptable combination?

**What to look for:**

- **Lower-threshold triggers** — most natural weapon effects require margin ≥ 3. Some fire on any hit (Bufoni Lengua, Yacani Bilis) or on critical only (Drak'kai Mordisco). Lower-threshold triggers create more reliable stacking.
- **Guaranteed effects** — some natural weapon effects bypass T.R. entirely (Drak'kai Mordisco: Aterrorizado on critical). Combined with a technique that also produces conditions, this can create two-condition hits.
- **Same condition** — if the natural weapon and the technique both produce the same Alteration (e.g., Loxod Trompa + a technique that causes Desequilibrado), they don't stack — strongest applies. Effectively neutral.
- **Stat reduction + condition stack** — veneno effects that reduce stats (reduce Tenacidad, reduce Agilidad) compound with conditions that restrict actions. Check whether the combination under the worst-case species pairing is still within acceptable power range.

**When to use `No Hereda Efectos` despite T.I.:**

If any specific species + technique combination produces a reliably broken output — meaning a player can trigger two independent conditions on most hits without exceptional luck — the technique should use `No Hereda Efectos`. The technique's own effect is the primary output; the natural weapon is suppressed by design.

**When `Hereda Efectos` is correct despite stacking potential:**

If all combinations require both a non-trivial trigger condition (margin ≥ 3 or critical) AND a T.R. failure to produce the combined effect, the stacking is acceptable. The design relies on two independent conditional gates rather than one.

### Application rule

- Every **Activo - Ataque** and **Reactivo** technique must specify the keyword. Never leave it implicit.
- **Utilidad** and **Pasivo** techniques: omit the keyword entirely — no weapon contact involved.
- The keyword goes in `## Keywords` in the corebook entry and as a `<span>` in the HTML card tag-bar.

### Where to find natural weapon data

All natural weapon stat blocks, profiles, and Efecto text live in:

```
Transcendence-publications/core-books/transcendence-corebook/06-species/es/
  01-naghii.md … 20-yacani.md
```

Each file has a `### Armas Naturales` section. Read the **Perfiles** line of every weapon block to find which species can use the technique's profile with a natural weapon, then read the **Efecto** block to understand the trigger condition and output.

---

## Non-overlap analysis — mandatory before designing

Before proposing any design, run this analysis. It has two parts. Do not skip either.

### Part 1 — same-profile technique map

Search `Transcendence-design/data/system/techniques.yaml` for every existing technique that uses the same weapon profile, regardless of species. For each one, record:

- its trigger (what condition fires the technique)
- its output (what the technique produces mechanically)
- its species origin

Map what the existing set covers, then identify the specific gap the new technique fills. If no gap exists, the design is a duplicate and must be revised before proceeding.

### Part 2 — cross-profile functional overlap

A technique can be a duplicate of an existing one even if the profiles differ. Two techniques that share the same trigger pattern **and** the same output pattern are functionally overlapping regardless of their profile.

Example: a technique that fires when an enemy moves and stops that movement overlaps with any other technique — on any profile — that also fires on enemy movement and stops it. The profile does not make them distinct.

Check the full technique set, not only same-profile entries, for this pattern.

### Gate

Only after both parts are complete should a design be proposed to the user. The non-overlap analysis is the basis for the design, not a box to check after it.

---

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

## Species framing discipline

Every new Technique run starts from the **corebook species entry**, not from design seeds or internal notes. Seeds drift; the corebook entry is what the player reads and what defines the species identity the game has committed to.

Before designing, read the corebook entry and identify two distinct layers:

**Biological layer** — what the body does by nature: anatomy, senses, metabolic traits, natural weapons, physical limits. This is what makes the Technique *possible*.

**Doctrinal layer** — what the species concluded from having that body: culture, philosophy, combat doctrine, theological reading of force. This is what makes the Technique specifically *theirs*.

A Technique that expresses only the biological layer is mechanically valid but species-generic. A Technique that expresses both layers is irreducible to another species. Techniques don't have to express both simultaneously — but the set as a whole must have both layers represented.

**Herencia principle:** when designing for a species vulnerability (herencia penalty), do not build a direct counter. The species' response is almost always lateral — they developed other capabilities that make the vulnerability matter less in practice. A vulnerability with a direct counter tells the player the species is afraid of itself. A vulnerability that is worked around tells the player the species has lived with it long enough to build a different path.

**Uniqueness rule:** for each species set, there is 1 Technique that should be indefensible outside that species — it requires the species' specific biology, lifespan, cultural history, or exclusive knowledge to be coherent. These anchor the set and distinguish it from generic profile work.

**Open access rule:** Techniques are born from species identity but are mechanically open to any character with the required weapon profile. A Technique must not depend on herencias, legados, or species-specific mechanics as mechanical requirements or outputs. A Technique must not depend on natural weapon effects (such as a specific bite effect, sting condition, or claw bonus) as its primary mechanical engine — the technique must function for a character using a crafted weapon with the same profile. Natural weapons may inform the fantasy of the technique, but the mechanic must stand on its own without them. Only 1–2 techniques in a full game set depend on natural weapons exclusively; the rest are profile-gated, not anatomy-gated.

**Primary design question:** *¿Qué sabe esta especie que otras no pueden saber?* Not what the body can do physically — what knowledge, experience, or biological sense is unavailable to any other species, and how does that become a concrete action with a real combat moment?

## Techniques vs. base specialization rolls

A base specialization roll provides narrative context — it helps the player
make decisions and know what is possible. A Technique must provide narrative
context AND a distinct concrete mechanical output on top of that. If a
Technique's output can be replicated by a good base specialization roll alone,
the Technique is not adding enough.

Test before finalizing any Technique: **what does this Technique do
mechanically that a base roll cannot do?** If the answer is only "it gives
better narrative information," revisit the effect and find a mechanic in the
existing system to anchor it to — T.A., T.D., T.I., T.E., T.R., T.C.,
ATB position, conditions, Ruptura, or access permissions.

When the mechanical consequence is implicit (e.g., safe identification without
physical contact), make it explicit in the effect text.

## Specialization domains

A specialization roll is the direct application of the skill in its literal
context. A Technique sourced from a specialization domain is not a better
version of that roll — it is an extension of the **underlying knowledge** the
specialization represents, applied to a context that is not the literal skill.

The correct question is not "how does this help with swimming?" but "what does
a swimmer know that a non-swimmer does not, and how does that apply inside
combat?"

**Full domain definitions — required reading before designing any
specialization-origin Technique:**

- `Transcendence-design/docs/system/specialization-technique-domains.md` —
  prose definitions for all 54 specializations: `fantasy_core`,
  `transferable_capabilities`, valid derived techniques, and invalid patterns
- `Transcendence-design/data/system/specialization-technique-domains.yaml` —
  structured authority version of the same data

### Domain extraction test

Before finalizing a domain-sourced Technique, confirm all three:

1. **What does this skill teach?** Not what it does, but what knowledge and
   principles it builds in the practitioner.
2. **What non-literal problem does that knowledge solve?** The Technique's
   mechanical output should answer this question.
3. **Does the Technique require that knowledge to be coherent?** If a
   character without the domain could use the same logic, the Technique is
   not domain-grounded — it is a generic mechanic wearing a specialization
   label.

### Activation roll requirement

Every specialization-origin Technique **must** include a `T.E.` of the relevant
specialization as its activation roll. This is not optional. It serves two
simultaneous functions:

- **Failure gate** — the Technique can be attempted and fail. Cost (Ritmo and
  Desgaste) is paid regardless; the effect does not occur on failure.
- **Progression trigger** — specialization competency can only advance through
  successful `T.E.` rolls. If a Technique has no activation roll, the only way
  to progress the specialization is through literal out-of-combat use, which is
  prohibitively slow.

**What the T.E. is testing:** Having the specialization means the character
already possesses the knowledge. The roll does not test "do you know X?" — it
tests "can you successfully apply that knowledge to *this specific target* under
combat pressure?" That distinction makes the roll valid even when the knowledge
itself is unambiguous.

**Standard difficulty scale — techniques targeting a creature:**

| Naturaleza | Dificultad |
| --- | --- |
| Mortal | Desafiante |
| Anomalía | Rigurosa |
| Primordial | Exigente |

Do not write the numeric value (8 + NR, 11 + NR, etc.) in the corebook entry
or card. Write only the tier name.

**Exception — reactive techniques with Ritmo 0 and scaling Desgaste:** For
techniques that fire as an internal resistance response (e.g., pushing through
a physical state, maintaining concentration under interruption), the difficulty
is contextual rather than Nature-based. Use Alteration severity
(Leve → Fundamental, Moderada → Desafiante, Grave → Rigurosa) or a Narrator-
set difficulty based on the severity of the triggering event. State this
clearly in the effect text.

---

## Cost and duration doctrine

**Required reading before setting any cost:** Read both of these docs first — they are the canonical cost reference, not memory or intuition:

- `docs/workflows/technique-cost-stabilization.md` — doctrine, bands, arbitration rules, and Ritmo/Desgaste definitions
- `docs/workflows/technique-cost-master-table.md` — the full validated table of all existing techniques with their accepted costs and comparison notes

When this skill authors or normalizes costs, use these project rules:

- compare costs against sibling Techniques, not against base actions
- base actions are fallback floor, intentionally inefficient, and are not the
  optimization benchmark for authored Techniques
- `Rhythm` = **time**: how much ATB position (ficha advancement) the technique
  costs. Any value ≥ 0. Use 0 when the technique has no external manifestation,
  no movement, and no timing requirement — a purely internal cognitive or
  reactive snap that does not occupy the ATB track. Use higher values when the
  effect requires physical execution, timing, or attention that shifts the
  user's position in the exchange.
- `Attrition` = **effort**: the permanent accumulated strain of executing under
  combat pressure. All active and reactive Techniques must carry at least
  `Attrition` 1 — doing anything while simultaneously tracking opponents,
  reading the field, and managing the body costs something permanently, even
  when the effect is fast or purely cognitive. `Attrition` 0 is only valid for
  hybrid resistance Techniques that represent things the body executes passively
  without conscious activation.
- when setting costs, ask: does this technique take **time** (Rhythm > 0), or
  only **effort** (Rhythm 0)? how much of each, and why?
- do not surcharge a Technique merely because its effect is `Permanente`
- charge for coverage, repeat leverage, and how many exchanges the effect can
  keep altering once active
- anchored postures should usually stay low in `Rhythm`; their positional lock
  is already part of the price
- avoid authoring effects that depend on "the next action", "the next roll",
  "N rounds", or similar memory burdens
- prefer effects that are either `Instantáneo` or `Permanente` with clear
  fictional end conditions
- hybrid resistance Techniques that are genuinely passive should default to
  `0/0`, because the body already knows how to do them rather than activating
  them tactically

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

### Cost review guardrails

When revising an existing Technique:

- update structured cost fields first
- then update any explanatory cost prose that still states the old values
- if the Technique's text shape no longer matches the cost doctrine, fix the
  Technique rather than forcing the cost to defend a bad structure
- if a Technique's effect relies on a one-use future promise, treat that as a
  design issue first and a cost issue second

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

**Effect text** — the complete rule written in narrative prose, second person, present tense. The card speaks directly to the player: "Realiza una T.A.", "recibes", "el objetivo realiza una T.R.". It is not an algorithm or a labeled sequence. It is a description of what happens, in the order it happens, with mechanical vocabulary placed in normal sentences. A bonus is written as "un bonificador igual a tu rango de X" — never as "+[rango de X]". An outcome is written as "con éxito, el objetivo..." — never as "Éxito: objetivo → Y".

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
3. **non-overlap analysis + Hereda Efectos pre-check** — run both mandatory pre-design steps:
   - Follow the **Non-overlap analysis** procedure (same-profile map + cross-profile functional overlap check)
   - For the technique's profile, list all natural weapons that share it (from `06-species/es/`); note trigger thresholds and output types — this becomes the **Hereda Efectos cross-species check** that runs after the design is drafted
4. resolve dependency and balance framing
5. confirm design with user (review gate before writing any output); at this point also resolve the **Hereda Efectos** keyword using the cross-species check against the drafted technique's own effect
6. write core publication entry (`transcendence-techniques/es/`)
7. write technique card (HTML, `technique-cards/.../cards/es/<species>/`)
8. edit authority YAML (`data/system/techniques.yaml`)
9. route into simulation or core sync only if needed
10. validate (run `python3 pipeline/scripts/validate_techniques.py` and ensure zero errors)
11. record acceptance and impact

## Reference map

Use these local references as your first map:

- `references/workflow-map.md`
- `references/checkpoints.md`

Then open the actual project workflow docs named there.
