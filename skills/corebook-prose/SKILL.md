---
name: "corebook-prose"
description: "Use when writing, revising, or doing a narrative voice pass on corebook publication files — flavor text, rules text, ailment entries, condition descriptions, or any prose in writing_mode: rules. Loads canon voice, style, and glossary context before drafting."
---

# Corebook Prose

Use this skill when the task is to write or revise prose in corebook publication files. This includes:

- writing flavor lines for ailment entries, conditions, or other rules content
- doing a narrative voice pass on existing entries that sound robotic or abstract
- writing rules-mode explanatory text that must be declarative and functional
- aligning ES and EN prose so both versions carry the same voice and content

This skill is for prose work specifically. It does not replace authoring decisions (use `technique-authoring`), system synchronization (use `corebook-sync`), or authority changes (use the relevant authority workflow).

## Authoring stance

This is a dark survival game. Players are the weakest actors in an overwhelming world. The setting draws from cosmicism — old, vast, indifferent forces — but earns its darkness through physical precision and concrete detail, not through adjectives or abstraction.

Prose in this game must work on two levels:

- **Rules text** must be declarative and functional. It enables decisions and removes ambiguity. Every sentence carries one mechanism or consequence. It does not explain tone; it produces it.
- **Flavor text** must be physical and sensorial. It evokes the felt experience of the state from inside the fiction. It never explains the mechanic. It never mentions dice, rolls, conditions, or game terms.

Do not let these two zones bleed into each other. If a line is doing both, split it.

## When to use this skill

Use `$corebook-prose` when the user asks for things like:

- write the flavor text for this entry
- this feels robotic — give it voice
- do a narrative pass on these ailment entries
- write the rules text for this condition
- translate this ES entry to EN maintaining the same voice
- does this entry match the established voice?
- apply the same voice pattern to the remaining entries

Do not use this skill when the task is primarily:

- changing a mechanic (route to the relevant authoring workflow)
- syncing authority changes to publication (use `corebook-sync`)
- creating a new technique (use `technique-authoring`)
- writing light novel or fiction content (use `fiction-guide` as primary reference)

## Required context

Before drafting, load these canon files:

**Always load:**
- `Transcendence-publications/canon/text-modes.md` — the approved writing modes and what each is allowed to do
- `Transcendence-publications/canon/style-guide.md` — sentence structure, density, and formatting rules
- `Transcendence-publications/canon/voice-samples.md` — the rhythm reference; use approved samples as cadence templates
- `Transcendence-publications/canon/glossary.md` — canonical term list for ES/EN pairs; all system terms must match this file

**Load when relevant:**
- `Transcendence-publications/canon/world-facts.md` — when the prose touches setting, factions, world mechanics, or named entities
- `Transcendence-publications/canon/publication-visual-style.md` — when formatting, callouts, tables, or layout is relevant
- the target file itself
- the bilingual pair file (if the task touches one language, always check the other)

Do not draft until the mode is named. Decide flavor or rules first.

## Execution pattern

### 1. Name the mode

Decide per passage:
- `flavor` — brief tonal line; does not carry mechanics; appears as italic in corebook entries
- `rules` — declarative explanation of how something works; appears as body text

If a passage is doing both, split it.

### 2. Load context

Read the canon files listed above. Read the target file. If bilingual, read both language versions.

Identify any canonical terms the passage must use. Cross-reference against `glossary.md`.

### 3. Draft in the named mode

**For flavor text:**
- one or two short sentences, maximum
- body-first: the body or a physical sensation is the grammatical subject when possible; avoid "the target" as subject where the body itself can be the subject
- physical and sensorial: what does the body feel, register, fail to do?
- contrasting or sequential structure: either two facts that tension against each other, or a sequence that moves from cause to consequence
- no adjectives stacked to build atmosphere; let the physical fact carry the weight
- no "the target [verb]s" when the body or the limb can be the subject instead
- never mention dice, rolls, conditions, bonuses, or game terms

**For rules text:**
- declarative sentences; one mechanism per sentence
- third person ("the target", "a creature", "the effect")
- use canonical system terms exactly as they appear in `glossary.md`
- no emotional framing; no atmospheric language
- formulas: write `1d10 + Characteristic + competency level + additional bonuses`, never shorthand placeholders
- competency references: always name the specific competency, never write "Resistencias" or "Bonos" alone

### 4. Check the bilingual pair

After writing or revising one language, check that the other carries equivalent content and voice. ES and EN may differ in phrasing but must not differ in information or tone register.

If one language is pending, mark it explicitly: `ES: pendiente` or `EN: pending`.

### 5. Read the result aloud

If it sounds robotic, it is not done. If it sounds abstract, it is not done. If it explains the mechanic instead of evoking the state, it is flavor drifting into rules — split it.

## Prose rules for flavor lines in rules-mode files

These apply specifically to the short italic flavor lines that open each entry in ailment, condition, and technique catalog entries.

### Voice pattern established for Alterations

The confirmed voice for Alteración/Alteration flavor lines:

- **1–2 sentences, no more**
- **Body-first:** the body, a specific muscle group, a limb, a sense, or a physical process is the subject — not "the target"
- **Physical or sensorial:** what the body registers, fails, delays, or loses — not what it "experiences" abstractly
- **Contrasting or sequential:** two facts in tension ("X arrived. Y did not follow."), or a causal chain ("X happened. The body does Y.")
- **No hollow adjectives:** not "unbearable", "horrifying", "overwhelming" — find the physical fact instead
- **No game language:** no rolls, no penalties, no conditions named

Confirmed samples (ES → EN):
- *Los músculos responden con retraso. El frío ya lleva ventaja.* → *The muscles respond late. The cold already has the lead.*
- *El golpe llegó. La claridad tardará en volver.* → *The hit landed. Clarity will take a while to return.*
- *La postura cede. El suelo gana.* → *Posture gives. The ground wins.*
- *La descarga pasó. Los músculos no terminan de creérselo.* → *The discharge passed. The muscles have not finished believing it.*
- *Moverse cuesta. La herida recuerda exactamente cuánto.* → *Moving costs. The wound remembers exactly how much.*
- *La señal llega. El cuerpo no la ejecuta.* → *The signal arrives. The body does not execute it.*
- *Demasiado a la vez. El sistema no encuentra por dónde salir.* → *Too much at once. The system cannot find a way out.*

Use these as calibration for all future flavor lines in ailment and condition entries.

## Quality rules

- Do not mix flavor and rules in the same sentence.
- Do not use "el objetivo" or "the target" as the subject of a flavor line when the body itself can be.
- Do not write placeholder language: never "Resistencias", "Bonos", "rolls y tiradas". Use specific names.
- All canonical terms must match `glossary.md` exactly — spelling and capitalization.
- Do not write an EN entry without checking the ES pair, and vice versa.
- If a flavor line sounds like a function description, rewrite it.
- If a flavor line mentions a mechanic, move that content to rules text.
- If a rules line sounds atmospheric or evocative, move that content to flavor text or cut it.
- Prefer two short sentences over one long compound sentence with conjunctions stacked.
- Do not add flavor where none existed unless the task explicitly requests it.

## Reference map

Load these first:

- `Transcendence-publications/canon/text-modes.md`
- `Transcendence-publications/canon/voice-samples.md`
- `Transcendence-publications/canon/glossary.md`

Then load the target file and its bilingual pair.
