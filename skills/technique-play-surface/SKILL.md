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

For localization specifically:

- fully localize the surface to the publication language
- do not leave authority-side English profile or competency labels on Spanish
  player-facing surfaces
- map internal labels into the published language without changing the mechanic
- do not preserve authority-side roll abbreviations automatically if the
  publication surface uses localized player-facing roll names instead
- prefer complete ordinary player-facing words over layout abbreviations
- only preserve abbreviations when they are canonical rules notation the player
  is expected to know

For the **ES Type - Category field** specifically, only these values are valid on ES publication surfaces:

| Type | When to use |
| --- | --- |
| `Activo - Ataque` | Active technique whose primary resolution is a T.A. |
| `Activo - Utilidad` | Active technique with no attack roll — buffs, stances, declarations |
| `Activo - Utilidad · Postura` | Active stance that persists until broken |
| `Reactivo - Ataque` | Reactive technique whose primary PURPOSE is to attack and potentially deal damage — resolves through T.A. |
| `Reactivo - Utilidad` | Reactive technique whose primary PURPOSE is control, movement-denial, or utility — may still use T.A. if weapon-profile based |

**`Reactivo - Defensa` does NOT exist.** The Type - Category distinction is about **purpose**, not about which roll is made. A weapon-profile reactive technique that controls movement (no damage) is `Reactivo - Utilidad` even though its Tirada is `T.A.`. The defensive purpose of a technique does not create a "Defensa" category — that distinction lives only in authority-side taxonomy.

**Weapon-profile techniques always use `T.A.` in the Tirada field**, even when the technique does not deal damage. The absence of damage is shown by `Impacto: —`, not by changing Tirada to `T.E.`. Do not use `T.E.` for a weapon-profile Technique just because it lacks a damage payload.

For the **ES stat block fields** specifically, use only canonical ES values:

| Field | Valid ES values |
| --- | --- |
| `Rango` | `Personal` / `Alcance del arma` / `Xm` (e.g., `3m`) / `Rango Visual` |
| `Área` | `Tú` / `1 Criatura` / `Circular Xm` / `Cono Xm` / `Línea Xm` |
| `Duración` | **Only** `Instantáneo` or `Permanente` — no other values |
| `Tirada` | `T.A.` / `T.D.` / `T.I.` / `T.E. (X)` / `T.R. (X)` / `T.C. (X)` / `—` |
| `Salvación` | Roll that **completely negates** the effect, or `—` |
| `Impacto` | `T.I.` only when damage exists, otherwise `—` |

Key rules: `Alcance del arma` belongs in **Rango** not in **Área**. Área for a single-target weapon technique is `1 Criatura`. Sustained stances and lasting effects are `Permanente` — end conditions go in the effect text, not in Duración.

**No abbreviated stat values on player-facing surfaces.** Salvación must always be written in full — `T.R. (Alteraciones)` is required; `T.R. (Alt.)` is invalid. This is a new game: players need complete terms to understand every field without inference.

For `Flavor Text` specifically, apply the full flavor text rules in the Prose rules section below. The essential constraint: one short italic sentence, physical and dark, that evokes the tactical fantasy without explaining the rule.

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
- surface named kit families explicitly when they are real game gates
- make the cleanup path explicit when the technique creates a mark, residue,
  snag, foul, or similar state that existing rules can clear

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
- leave internal-language labels on a player-facing surface just because they
  are shorter

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

## Prose rules

These apply to all play-facing surfaces — both corebook entries and cards. They do not apply to YAML or authority docs.

### Setting tone

This is a dark survival game. Players are the weakest actors in an overwhelming world — the environment, creatures, and forces around them are old, vast, and indifferent. The setting draws from cosmicism, but the goal is not to sound like generic Lovecraft pastiche. The tone earns its darkness through physical precision and concrete detail, not through adjectives or abstraction.

This tone shapes flavor text. Effect text must remain clear and functional. But flavor text must reflect the world the technique lives in.

### Two zones

Technique surfaces have two zones that never mix — treat them like Magic: The Gathering cards:

**Flavor text** — one short italic sentence in the voice of the world. It evokes the technique's tactical fantasy without explaining the rule. It sounds physical, precise, and dark. It prefers concrete images over abstract concepts. It suggests tension, timing, consequence, body movement, material failure, perception, or intent — not the mechanic itself.

**Effect text** — the complete rule written in narrative prose, second person, present tense. The surface speaks directly to the player: "realizas", "recibes", "el objetivo". It is not an algorithm or a labeled sequence. It defines what happens, in the order it happens, with mechanical vocabulary placed in normal sentences.

The core and card share the same prose register. The difference is density only:

- **Core:** one extra sentence is allowed to clarify an edge case, spell out a timing nuance, or resolve a condition the card compresses. The standard does not change.
- **Card:** compresses where meaning survives intact. Does not change the rule — only removes what the player can infer.

### Flavor text rules

Do:

- One short italic sentence. If it needs two, cut one.
- Evoke the tactical fantasy without explaining the rule.
- Sound physical, precise, and dark.
- Prefer concrete images over abstract concepts.
- Suggest tension, timing, consequence, body movement, material failure, perception, or intent.
- Match the technique's specialization indirectly — through its transferable logic, not through literal explanation.
- Write for a world where the players are the weakest thing in it.

Do not:

- Mention the character, player, mechanic, roll, bonus, condition, range, or action cost.
- Explain why the specialization applies.
- Use "el usuario", "el practicante", "la técnica permite", or similar phrases.
- Use generic epic fantasy language.
- Use motivational phrases.
- Over-explain.
- Make the sentence longer than needed.
- Repeat the technique name unless it creates strong rhythm.
- Use direct imperatives unless the technique's style strongly benefits from it.

Style target: short, sharp, concrete, suggestive. More like a blade mark than a paragraph.

### Effect text rules

Structure — in this order when applicable:

1. Trigger, if any — state as prose, not as a labeled field.
2. The roll — "Realiza una..."
3. Failure — "Si fallas..."
4. Success — "Con éxito..." or "Si tienes éxito..."
5. Duration or end condition if the effect persists — "La técnica termina si..."

Canonical language patterns:

- `Realiza una T.E. (X) contra...`
- `Si fallas, no ocurre nada.`
- `Con éxito, el objetivo...`
- `Este bonificador se aplica una sola vez.`
- `La técnica termina si te desplazas.`

Do:

- Be clear enough to play without asking the Narrator.
- Use "tú" when referring to the character.
- Define the trigger first, if any.
- Keep one rule idea per sentence whenever possible.
- Use consistent language across all techniques.

Do not:

- Change the mechanic unless explicitly asked.
- Add restrictions unless needed to prevent ambiguity.
- Explain design intent.
- Use programming-style language: "dispara cuando", "trigger", "fijo", "escala", "evento".
- Use "usuario" when "tú" is clearer.
- Use "bonus" — use "bonificador".
- Hide important limits in flavor text.
- Mix rule and designer commentary.

### Format rules

- **Second person only.** Write "tú" / "tu" — never "el usuario". Both surfaces speak directly to the player.
- **No bracket notation.** Never write `+[rango de X]` or `−[rango de X]`. Write "un bonificador igual a tu rango de X" or "una penalización igual a tu rango de X". For dice expressions, write "un número de dados d2 igual a tu rango de X" — not `[rango de X]d2`.
- **No "bonus".** Use "bonificador" in all play-facing prose. "bonus" belongs only in YAML.
- **No YAML-style labels in prose.** "Éxito:", "Fallo:", "Dispara cuando" are internal authoring shorthand. In the surface, the rule must read as continuous prose.
- **No design-intent explanations.** Never write "esto convierte X en la opción más eficiente". The rule produces that effect — the surface does not explain it.
- **No docstring tone.** If the effect reads like a function description, rewrite it as a rule a player reads at the table. Short, present tense, no parentheticals explaining why.

## Effect anchoring rules

Every mechanical effect on a play-facing surface must be grounded in a concrete system reference. Two distinct categories define how effects are produced:

**Specializations produce narrative effects only.** A successful T.E. (Intuición) gives contextual information the player uses to justify actions — it does not produce a mechanical bonus automatically. No technique effect should describe a specialization roll as producing a bonus, penalty, or condition unless a technique explicitly defines that outcome.

**Techniques produce both narrative context and a defined mechanical outcome.** A technique always uses T.E. of its base specialization. Whether the triggering action is a base specialization use or a technique, the roll form is the same — T.E. (Especialización). Do not distinguish between "base use" and "technique use" in play-facing text; reference only the roll category.

When a technique counters or intercepts another roll, reference the roll category rather than listing every valid specialization:

- `T.E. Mental o Social` — covers all social and mental specialization rolls: Intuición, Percepción, Engaño, Intimidación, Negociación, Liderazgo, Instinto, Resonancia, and others when the narrative context supports it
- Use specific specialization names only when the technique is narrowly scoped to one

When a counter-technique denies effects, the denied effects must map to one of:
- The narrative context itself (the read produces no usable information)
- A named conditional mechanic from a specific technique (e.g., an effect that fires only if the read succeeds)

Do not write "efectos tácticos", "ventaja narrativa", or other vague placeholders. If the denied effect has no concrete system name, the denial is just: the read produces no usable context.

## Quality rules

- Do not copy authority text into the core verbatim if it still sounds like design prose.
- Do not let cards become shorthand that changes the Technique's real meaning.
- Do not keep fake requirements that are only common-sense scene logic.
- Do not list contextual combat pressure as a formal requirement for an `Active` Technique unless the game explicitly tracks it as one.
- Do not repeat top-line fields as keywords unless the keyword adds new system information.
- Do not let core and card diverge semantically.
- Do not add approximation language where authority is exact.
- Do not let flavor text drift into generic fantasy filler or AI-sounding abstraction.
- Do make flavor text feel like it belongs to the owning species, school, or living tradition.
- Do not leak English-facing profile, competency, or rules labels into Spanish publication surfaces.
- Do not preserve internal shorthand automatically if the publication surface uses a different player-facing notation standard.
- Do not leave `A.R.`, `I.R.`, or similar internal abbreviations on a Spanish-facing surface if the book's own standard spells or names them differently.
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
