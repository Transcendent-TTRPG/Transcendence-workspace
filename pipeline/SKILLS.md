# Editorial Skills

This file defines the three editorial skills available in the Transcendence pipeline. Each skill specifies what context to load, what the task goal is, and what constraints apply.

Skills are not Claude Code slash commands — they are documented workflows. Follow them manually or reference them when delegating a task.

---

## prose-editor

**Purpose:** Write or rewrite prose so it matches the Transcendence voice and does not read as AI-generated.
**When to use:** Any time corebook chapters or light novel sections need to be written, revised, or polished.

### Mandatory context (load before starting)

1. `Transcendence-publications/canon/style-guide.md`
2. `Transcendence-publications/canon/glossary.md`
3. `Transcendence-publications/canon/voice-samples.md`
4. `Transcendence-publications/canon/text-modes.md`
5. `Transcendence-publications/canon/corebook-writing-checklist.md` when working on corebook files
6. The target file
7. 2–5 related files (use `pipeline/scripts/index.py --search` to find them)

### Constraints

- Match the rhythm and vocabulary documented in `style-guide.md`
- Choose the passage mode explicitly using `canon/text-modes.md` before drafting
- Use only terminology from `glossary.md` for system concepts
- Avoid every pattern listed in `style-guide.md §AI-patterns-to-avoid`
- Do not introduce new canonical terms without first checking `glossary.md`
- Prose must be in the correct language (ES / EN) — do not mix
- Each narrative paragraph must be anchored in one primary sensory channel — do not distribute attention across unrelated inputs
- In horror-facing or Limbo-facing passages, every narrative paragraph must present a perceivable anomaly; do not describe causes or explanations
- In ordinary fiction passages, every narrative paragraph must still carry a perceivable point of tension, change, pressure, or consequence
- Narrative and rules text must be separated explicitly — rules first, then example or flavor text; do not blend them
- When writing rules text, introduce mechanical concepts by contrast ("not X, but Y") followed by a consequence chain; close with a short declarative statement of the trade-off
- Corebook files should not advance past `review` unless `canon/corebook-writing-checklist.md` passes

### How to invoke

```bash
# Find related files before editing
python3 pipeline/scripts/index.py \
  --repo-path Transcendence-publications \
  --search '{"tags": ["combat", "atb"], "chapter": 10, "language": "es"}'

# Then read: style-guide + glossary + voice-samples + target + returned files
# Then edit the target file
```

---

## rule-clarifier

**Purpose:** Make mechanical text unambiguous, structured, and testable without a rules lawyer.
**When to use:** Whenever a rules passage is unclear, has edge cases unaddressed, or contradicts design docs.

### Mandatory context (load before starting)

1. `Transcendence-publications/canon/glossary.md`
2. The target file
3. Relevant ADR(s) from `Transcendence-design/docs/adr/`
4. Relevant YAML from `Transcendence-design/data/system/`

### Constraints

- Every rule must either include an example or reference one explicitly
- No ambiguous pronouns ("it", "they") in mechanical text — always specify the subject
- Numbers (costs, thresholds, formulas) must match the values in `Transcendence-design/data/system/`
- Edge cases must be addressed inline or explicitly deferred to an open question in the relevant ADR
- Do not invent new mechanical values — defer to design docs

### Checklist before marking a rules section as complete

- [ ] Formula matches `data/system/` YAML
- [ ] All canonical terms spelled as in `glossary.md`
- [ ] No contradictions with relevant ADR
- [ ] At least one example exists (inline or linked)
- [ ] Edge cases are stated or deferred

---

## continuity-checker

**Purpose:** Validate that a file is canonically consistent across the repository before marking it final.
**When to use:** Before changing `status` to `final` or `canonical: true` in frontmatter.

### Mandatory context (load before starting)

1. `Transcendence-publications/canon/glossary.md`
2. `Transcendence-publications/canon/world-facts.md`
3. The target file
4. Related files from manifest (same chapter, same tags)
5. Relevant YAML from `Transcendence-design/data/system/`

### Checklist

- [ ] All proper nouns match `glossary.md` spelling and capitalization exactly
- [ ] Numerical values match `Transcendence-design/data/system/` files
- [ ] Internal cross-references point to files that exist
- [ ] No contradictions with files marked `canonical: true`
- [ ] Bilingual pair (ES/EN) is consistent with each other
- [ ] Tags in frontmatter are accurate and complete
- [ ] `related` field in frontmatter lists the actual related files

### World-facts checks

Run these checks explicitly whenever the file touches setting, atmosphere, cosmology, extranatural phenomena, religion, or in-world explanation:

- [ ] The text does not treat **the Limbo** and **the Void** as synonyms
- [ ] Neutral narration does not present theological interpretation as mechanical certainty
- [ ] Ordinary viewpoints do not perceive the Limbo directly unless the file establishes a valid reason
- [ ] **Tauma** is not described as creating phenomena from nothing; it transforms, modifies, or amplifies what exists
- [ ] Extranatural conditions are described by origin, not merely by intensity or spectacle
- [ ] Subtle extranatural effects are allowed; visible contradiction is not treated as mandatory in every case

### Reviewer prompts

Ask these before marking a lore-facing file complete:

1. Is this sentence stating a world fact, reporting a character belief, or expressing doctrine?
2. Could the viewpoint actually know or perceive what the sentence claims?
3. Does the passage accidentally collapse theology, cosmology, and mechanics into one voice?
4. If the passage explains a phenomenon, is that explanation already locked by `world-facts.md` or still open design?

---

## fiction-writer

**Purpose:** Write or revise sustained fiction for light novels, narrative supplements, or long-form in-world scenes without collapsing into exposition, sourcebook prose, or generic dramatic writing.
**When to use:** Any time the task is primarily story-facing rather than rule-facing.

### Mandatory context (load before starting)

1. `Transcendence-publications/canon/fiction-guide.md`
2. `Transcendence-publications/canon/text-modes.md`
3. `Transcendence-publications/canon/style-guide.md`
4. `Transcendence-publications/canon/voice-samples.md`
5. `Transcendence-publications/canon/glossary.md`
6. `Transcendence-publications/canon/world-facts.md`
7. The target file
8. 2–5 related files from the manifest

### Constraints

- Name the primary text mode before drafting; fiction defaults to `narrative` or `description`
- Maintain a constrained viewpoint unless omniscience is explicitly intended
- Do not use fiction to define mechanics directly
- Lore must emerge through perception, belief, pressure, dialogue, or consequence
- Dialogue must change the scene, not simply explain the setting to the reader
- If a passage touches the Limbo or extranatural phenomena, preserve the distinction between observable effect, interpretation, and world fact
- Do not let character belief silently redefine canon
- Every scene must end with change: discovery, escalation, cost, misreading, reversal, or consequence

### Scene checklist

- [ ] The viewpoint is clear
- [ ] The scene has an active pressure line
- [ ] Description serves action, tension, or consequence
- [ ] Dialogue changes the scene
- [ ] Lore is revealed indirectly unless explicit exposition is structurally justified
- [ ] The ending changes the reader's understanding or the character's situation

### Long-form checklist

- [ ] Scene order reflects escalation or recontextualization, not repetition
- [ ] Exposition is distributed rather than dumped
- [ ] Canon facts remain consistent with `world-facts.md`
- [ ] Terms remain consistent with `glossary.md`
- [ ] If bilingual versions exist, they preserve the same scene logic and canon payload

---

## species-design

**Purpose:** Define a new species in the design repository — write the 10-section narrative design doc, register natural attack forms in the system YAML, and update the index. This is the prerequisite for writing publications prose using the `species-entry` skill.
**When to use:** When starting a new species from scratch or promoting rough notes to a canonical design doc. Complete this before beginning any publications work.

### What this skill produces

There is no `species.yaml`. The design output is:

1. `Transcendence-design/docs/canon/species/<species>.md` — the 10-section narrative design doc
2. `Transcendence-design/docs/canon/species/<species>-technique-seeds.md` (skeleton) — the structural foundation for technique authoring; see §Seeds skeleton below
3. `Transcendence-design/data/system/natural-attack-forms.yaml` — register the species in each attack form it uses; add a `species_profile_expressions` entry if its expression differs from the generic
4. `Transcendence-design/docs/canon/species/index.md` — add the species to the roster table
5. `Transcendence-design/docs/canon/species/species-development-status.md` — add a layer-by-layer assessment

Note: Características, Herencia, and Legado do not have a YAML schema yet. They are defined as candidates in §9 of the design doc and authored as final values directly in the publications file. Do not create a species.yaml.

### Mandatory context (load before starting)

1. `Transcendence-design/docs/canon/species/species-template.md` — the authoring scaffold
2. `Transcendence-design/docs/canon/species/index.md` — all existing species and world context
3. All completed `docs/canon/species/*.md` files — tonal and structural reference
4. `Transcendence-design/data/system/natural-attack-forms.yaml` — check existing forms before adding new ones
5. `Transcendence-design/data/system/ailments.yaml` — check existing ailments before proposing weapon effects
6. `Transcendence-design/data/system/specializations-catalog.yaml` — check existing competency names before listing affinities
7. The rough notes for this species — primary source material
8. `Transcendence-design/docs/canon/species/species-development-status.md` — understand what "complete" means

### Section structure (mandatory, in order)

The design doc is analytical, not corebook prose. Use lists and concise paragraphs — this is not written for readers, it is written for designers.

1. **Identity** — animal base, cultural analog, cosmicist hook, first impression, civilizational anxiety in one sentence
2. **Body** — anatomy, locomotion, natural weapons, senses, biological variants, size/weight/lifespan
3. **Culture** — social structure, authority model, worldview, central civilizational idea, what earns respect
4. **Theology and Cosmology** — relationship with Tauma and Limbo (or equivalent), sacred history, what they believe happened, what they fear
5. **Organization and Internal Variation** — community forms, internal roles, stable fault lines
6. **Daily Life and Survival** — food, childhood learning, daily fears, what old age means, what a non-elite life looks like
7. **External Relations** — geographic spread, neighbors, how others read them, recurring political position
8. **Material Expression and Language** — clothing, architecture, tools, naming patterns, ritual objects
9. **System Connections** — competency affinities, natural attack logic, arsenal fit, candidate Características/Herencia/Legado, Technique implications
10. **Player Character Hooks and Open Questions** — what a PC knows, departure reasons, what they carry, open design questions

### Horror pressure test (apply before marking complete)

- What is trying to kill, corrupt, starve, isolate, or mislead them?
- What daily habits exist because safety cannot be assumed?
- What does this species do because the world is cruel, not because it is elegant?
- Which belief may be true enough to help them and wrong enough to destroy them?

If any section implicitly assumes ordinary continuity or stable safety without explaining how it is defended or paid for, revise it.

### Registering natural attack forms

For each attack form the species uses:

1. Check if the form already exists in `natural-attack-forms.yaml` (bite, claws, tail, sting, etc.)
2. If it exists: add the species name to the `species` list
3. If the species' expression differs from the generic (different profiles, different contact logic): add a `species_profile_expressions` entry under that form
4. If the form does not exist at all: add a new entry under `forms:` using the template at the top of the file

Do not add new forms just because the attack feels different thematically. Check whether the generic form's `compatible_profiles` already cover the intended mechanics. Only add a new form if the contact logic genuinely cannot map to any existing form.

### §9 System Connections — what to define

This section is the bridge to both the publications stat block and the seeds skeleton. It must include:

- **Competency affinities** — which skill trees this species naturally justifies; use names from `specializations-catalog.yaml`
- **Natural attack logic** — which forms, what combat role, how species-specific expression differs from the generic
- **Arsenal fit** — likely weapon categories beyond natural attacks
- **Candidate Características** — which 3 attributes get +1
- **Candidate Herencia** — the one complex or penalty trait: what condition triggers it, what effect, determined by whom
- **Candidate Legado** — scaling traits: how many, what they scale with, what skill or roll type
- **Technique implications** — what the species' Technique body should emphasize and what it should avoid

All values in §9 are candidates. Final stat block values are authored in the publications file.

### The core design rule: species origin ≠ species restriction

**Techniques are not species-locked.** A technique originates from a species — from their anatomy, culture, practices, and history — but its usability is determined by the weapon profile or specialization required to execute it, not by the character's species.

Any character who wields a weapon with the required profile can execute a technique, regardless of where that technique originated. Any character with a specialization can execute a specialization technique from any species that developed it. The species origin explains *why* the technique exists and gives it its identity and thematic coherence. It does not gate who can use it.

What species origin does determine:

- The narrative and thematic framing of the technique
- The specific mechanical constraints and design pressure (what problem the technique was developed to solve)
- Which profiles and specializations are mapped to that species' techniques

What species origin does not determine:

- Who can learn or execute the technique — that is determined by having the required weapon profile or specialization

This is why techniques feel like they belong to the world rather than to a spreadsheet. A non-Zarnag character wielding a weapon with the Corrosion profile can execute a Zarnag-origin technique — the technique carries the Zarnag principle, but the profile is the mechanical key.

The test when authoring a technique: *Could this technique exist without this species?* If yes, the origin is too thin. *Could someone execute it with a different body, tool, or practice?* If no, the origin has become too species-locked. The target is the middle — a technique that carries the species' thought and history into action, but whose mechanical surface is profile- or specialization-based and therefore accessible to any character who meets that requirement.

### Seeds skeleton — what to write

The seeds skeleton is a separate file (`<species>-technique-seeds.md`) that establishes the structural foundation for technique authoring. It is derived directly from §9 of the design doc. Write it after §9 is stable.

**The seeds skeleton contains three things:**

1. **Technique lessons from the species** — a brief overview of natural attack profile mappings and cultural combat surfaces. For each natural attack form: which profiles it maps to and why. For cultural surfaces: which non-natural-weapon competencies or tools are valid expression surfaces.

2. **Initial authoring surfaces table** — a table of every surface (weapon form, natural attack, specialization) with its fit level (Core / Supporting) and a short note on why. This is the palette that technique authors work within — remember that these surfaces are accessible to any character with the right profile or specialization, not only to characters of this species.

3. **Novice pass distribution target** — how many techniques per section (attack/weapons, defense, resistance hybrids, specializations), which specializations are primary (up to 8, each gets one technique in the novice pass), and which are secondary (available for resistance hybrids, swaps, and higher-rank expansion). Include a brief note on what the pass should emphasize and what it should avoid.

**The seeds skeleton does NOT contain:**

- Seed principles (the abstract conceptual seeds with `world_root`, `technique_space`, `authoring_pressure`, etc.) — those are added iteratively with designer review, one at a time, after the skeleton is approved.
- Finished technique descriptions — those go in `techniques.yaml` and the corebook ES files.

**Format reference:** See `docs/canon/species/zarnag-technique-seeds.md` for a complete example. The skeleton covers the Purpose section, Technique Lessons, and Appendix (Authoring Surfaces + Novice Pass). The numbered Seed Principles section is left empty until the iterative phase.

### Completion checklist

- [ ] All 10 sections present
- [ ] §9 includes explicit Características/Herencia/Legado candidates and Technique implications
- [ ] Seeds skeleton file created with: technique lessons, authoring surfaces table, novice pass distribution
- [ ] Seeds skeleton has no seed principles yet (those are added iteratively)
- [ ] Natural attack forms updated in `natural-attack-forms.yaml`
- [ ] Species added to `index.md` roster table
- [ ] Assessment added to `species-development-status.md`
- [ ] No new ailment names invented without checking `ailments.yaml`
- [ ] No new competency names invented without checking `specializations-catalog.yaml`
- [ ] Cosmological claims framed as species doctrine, not neutral world fact

---

## species-entry

**Purpose:** Write a species entry for the corebook following the canonical section structure, prose mode, and stat block format established by Naghii, Sauri, and Zarnag.
**When to use:** Any time a new species entry needs to be written or an existing one needs structural revision. One skill invocation = one species.

### Mandatory context (load before starting)

1. `Transcendence-publications/canon/style-guide.md`
2. `Transcendence-publications/canon/text-modes.md`
3. `Transcendence-publications/canon/voice-samples.md`
4. `Transcendence-publications/canon/glossary.md`
5. `Transcendence-publications/canon/world-facts.md`
6. `Transcendence-design/docs/canon/species/<species>.md` — design doc for this species
7. All completed species files in `06-species/es/` — structural and tonal reference
8. `Transcendence-design/data/system/ailments.yaml` — canonical ailment names and entries
9. `Transcendence-design/data/system/natural-attack-forms.yaml` — Durabilidad/Potencia baselines

### Section structure (mandatory, in this order)

Every species file must have exactly these sections in this order:

```text
[Opening] — 1–2 paragraphs, no header. Labor/ecological identity. Ends with the species' civilizational axiom (the sentence the culture uses to summarize what they do).
## El Cuerpo
## La Cultura
## Teología y Cosmología
## Organización e Identidad Interna
## Vida Cotidiana
## Relaciones con el Mundo
## Como Personaje Jugador
---
## Estadísticas de Especie
### Datos Generales
### Características
### Herencia
### Legado
### Armas Naturales
```

### Authoring posture

Write from the perspective of someone describing a people they know — not from the perspective of covering a design document. The design doc is context; the species entry is the result.

Select the 3–4 most distinctive things about the species and build the prose around those. Not every design decision needs to appear. What doesn't make it into the entry is not lost — it lives in the design doc. What does make it should be there because it is concrete, distinctive, and earns its place in the reader's understanding of the species.

The failure mode to avoid: prose that feels like a checklist of decisions made in prior conversations. Each paragraph should read as if the species exists, not as if a meeting was held about the species.

### Prose constraints (lore sections)

- **Mode:** `description` throughout all lore sections (§1–§7). Description presents a state — not events unfolding, not mechanical explanation.
- Each paragraph anchors in one primary subject: body, behavior, belief, or social function — not all four at once.
- Sentence variety is mandatory: mix short declaratives (under 12 words) with longer compound sentences. Do not write paragraphs where every sentence has the same structure or length.
- **Prohibited qualifiers:** generalmente, naturalmente, frecuentemente, considerablemente, inevitablemente, esencialmente — remove all instances.
- **Prohibited AI constructions in description mode:** "no X sino Y" as the primary rhetorical pattern; "no solo X, también Y" chains.
- Lore sections must not contain rules text, mechanical comparisons, or stat references. Move all mechanical discussion to §Como Personaje Jugador.

### World-facts constraints (theology and cosmology)

- Theological claims framed as in-world doctrine or species belief, not neutral narration stating mechanical fact.
- Do not write "el Limbo hace X" or "el Tauma causa Y" in neutral narration — that is doctrine, not world fact.
- Limbo and Void are not synonyms. Tauma transforms; it does not create from nothing.
- Species-specific theological names (gods, afterlife concepts, cosmological terms) must be added to `canon/glossary.md` with a Do-not-translate note before the file is considered complete.

### Stat block format rules

#### Datos Generales table

```text
| Longevidad | Tamaño | Estatura | Peso | Velocidad |
```

**Idiomas:** `NombreIdioma (nativo) · Común` — language name must be clearly distinct from the species name.

#### Características

`Los [Especie] obtienen \`+1\` en **X**, **Y** y **Z**.`

#### Herencia, Legado, Armas Naturales

These sections are entirely design-driven. Derive structure, scaling, and effect text from the species' design YAML — do not impose a format template. Existing species files are reference only; each species may differ.

What is consistent across all species:

- The natural weapon **stat block table** always uses: `| T.A. | T.I. | Alcance | Daño | Durabilidad | Potencia |`
- Principal and Auxiliar labels must match the YAML assignment
- Verify Dur/Pot values against `natural-attack-forms.yaml` before finalizing
- Ailment and state names must match `ailments.yaml` exactly

### Audit checklist (run after writing, from evaluator position)

Shift position: do not re-read impressionistically. Work through each check explicitly.

#### Structure

- [ ] All 9 sections present in correct order
- [ ] No rules text in lore sections §1–§7
- [ ] Opening ends with a civilizational axiom sentence

#### Prose

- [ ] No filler qualifiers: search `generalmente`, `naturalmente`, `frecuentemente`, `considerablemente`, `inevitablemente`, `esencialmente`
- [ ] No AI contrast constructions dominating any paragraph
- [ ] Sentence rhythm varies within each paragraph (not all long, not all short)
- [ ] Each paragraph has a single primary subject
- [ ] No stat-block trait names appear in bold in lore prose — mechanical traits are described as behavioral or physical facts, not named as rules constructs

#### World-facts

- [ ] Theological claims attributed to the species, not stated as neutral world fact
- [ ] Limbo/Void not conflated
- [ ] Species-specific cosmological terms added to `glossary.md`

#### Stat block

- [ ] Idiomas language name is distinct from species name
- [ ] All weapon effects use T.R. + conditional structure
- [ ] All scaling effects formatted as tables
- [ ] Ailment/state names verified against `ailments.yaml`
- [ ] Dur/Pot values verified against `natural-attack-forms.yaml`

### Template

`pipeline/templates/species-entry.md` — copy this file as a starting skeleton.

---

## mechanic-registrar

**Purpose:** Keep all design and canon files in sync whenever a mechanical concept is defined, changed, or removed.
**When to use:** Any time a new mechanic, term, formula, or design decision is introduced anywhere in the project — regardless of which file or repo it originated in.

This skill answers the question: *"I just defined something — what else needs to be updated?"*

### Change types and what they require

#### New mechanical concept (new stat, new system, new derived attribute)

Mandatory context:

1. `Transcendence-publications/canon/glossary.md`
2. The relevant `Transcendence-design/data/system/*.yaml` (if one exists for this area)
3. `Transcendence-design/docs/system/mechanics-overview.md`

Checklist:

- [ ] Term added to `canon/glossary.md` with ES term, EN equivalent, and Do-not-translate flag
- [ ] Numeric definition added to the relevant `data/system/*.yaml` (or new file created)
- [ ] Reference doc in `docs/system/` updated or created
- [ ] `docs/system/mechanics-overview.md` updated — add to the relevant system summary table and to §Ability design surfaces if it creates a new ability touchpoint
- [ ] `docs/system/index.md` updated — add row to Files table and to Key Numbers if applicable
- [ ] ADR created in `docs/adr/` if this concept required a design decision
- [ ] `Transcendence-publications/CLAUDE.md` cheat sheet updated if term is frequently used

#### Value change (cost, formula, threshold, scaling)

Mandatory context:

1. The `data/system/*.yaml` that owns the value
2. `docs/system/mechanics-overview.md`
3. Corebook files that reference the old value (use `pipeline/scripts/index.py --search` with relevant tags)

Checklist:

- [ ] Value updated in `data/system/*.yaml` — this is the authority; update here first
- [ ] Reference doc in `docs/system/` updated to match
- [ ] `docs/system/mechanics-overview.md` updated if the changed value appears in summary tables
- [ ] `docs/system/index.md` §Key Numbers updated if applicable
- [ ] All corebook files that state the old value explicitly updated
- [ ] ADR updated if the change reverses or supersedes a previous decision

#### New design decision (structural rule, interaction model, priority order)

Mandatory context:

1. Relevant existing ADR(s) from `docs/adr/` — check for conflicts
2. Relevant `data/system/*.yaml`

Checklist:

- [ ] ADR created or updated in `docs/adr/`
- [ ] Decision reflected in `data/system/*.yaml` if it has numeric consequences
- [ ] `docs/system/mechanics-overview.md` updated if decision changes ability surfaces or design principles
- [ ] Corebook files that conflict with the decision flagged for revision

#### New term appears in corebook before glossary entry exists

Checklist:

- [ ] Add term immediately to `canon/glossary.md` §Terms pending approval
- [ ] Do not use the term in additional files until it graduates from pending approval
- [ ] Once approved, move to the relevant glossary section and follow New mechanical concept checklist

### Hard rules

- The `data/system/*.yaml` files are the numeric authority. Update them first, then propagate to docs and prose.
- The `canon/glossary.md` is the terminology authority. A term does not exist until it is there.
- `docs/system/mechanics-overview.md` is the ability design authority. If a surface exists but is not listed there, it will be ignored when designing abilities.
- Never update only one file. Every change touches at minimum: the authority file + the reference doc + the glossary (if it introduces a term).

---

## technique-author

**Purpose:** Author one technique from conceptual idea to finished entry — iterating from free ideation through mechanical grounding to final writing. One skill invocation = one technique.
**When to use:** Any time a new technique is being developed. Do not begin with the YAML format. Begin with the idea.

### Phase 1 — Ideation (no context loading required)

The technique begins as a conversation. No mechanical constraints apply yet. The goal of this phase is to arrive at a clear conceptual picture:

- What does this technique want to do? What is the core action or principle it expresses?
- What species body, practice, or cultural knowledge produced this method?
- What problem was this developed to solve? What moment in combat or exploration does it resolve?
- Who should be able to execute it? (Which weapon profile or specialization is the key — remembering that species origin ≠ species restriction)

**Phase 1 ends when:** The idea can be stated as a concrete action with a named origin surface (a weapon profile, a specialization, or a hybrid). If the idea cannot yet be stated this precisely, keep iterating in conversation before loading any files.

### Phase 2 — Grounding (load context here)

**Mandatory context:**

1. `Transcendence-design/data/system/techniques.yaml` — taxonomy, cost model, authoring questions, required fields
2. `Transcendence-design/docs/system/technique-play-surface.md` — play-facing output format
3. `Transcendence-design/data/system/ailments.yaml` — if the technique applies any condition or state
4. `Transcendence-design/docs/system/specialization-technique-domains.md` — if the technique is specialization-rooted
5. `Transcendence-design/docs/canon/species/<species>.md` — for origin context and thematic coherence
6. `Transcendence-design/docs/canon/species/<species>-technique-seeds.md` — to confirm the technique fits the seeded surface and novice pass slot

Work through the `authoring_questions` already codified in `techniques.yaml`. The key gates before writing:

- **Competency origin:** What single competency or hybrid makes this executable? State it explicitly.
- **Non-magical cause:** What trained body control, timing, force transfer, positioning, or practiced perception explains this? (The `spectacle_rule` in techniques.yaml lists the valid sources.)
- **Mechanical change:** What named mechanic does the effect touch — an existing Ailment, a Fatigue state, a wound grade, a positional state, a cover condition, an information reveal? The effect must be traceable to a named system mechanic. Do not invent freeform effects.
- **Specialization gate:** If this is a specialization technique — name the extracted trained capability before writing the effect text. If you cannot name it, the technique is not ready.
- **Information technique gate:** If this is a reading or perception technique — what actionable truth does it reveal? A technique that only grants a passive bonus is not a technique unless it is explicitly a bounded setup technique with a clear target action, narrow trigger, and defined duration.
- **Cost:** Rhythm (anchors: 0, 3, 5, 7, 9 — intermediates allowed) and Attrition (0–3, higher for exceptional overextension). Calibrate using the cost model bands in `techniques.yaml`. Use the conservative band on first pass.

  **Cost calibration reference: other techniques, not base actions.** The game is built on competency growth. Techniques are always the most efficient expressions of competency — a character who has learned a relevant technique should never find the base action more attractive for that specific situation. Base actions are intentionally inefficient; they are the fallback for when no technique applies, not the benchmark. When evaluating whether a cost is correct, compare against existing techniques of the same type and tier in `techniques.yaml`, not against what a base action costs.

  **Attrition rule:** Attrition does not mainly price what the Technique does to the user in the current combat turn. It mainly prices how much strain and continuity pressure the Technique creates across hostile scenes and how much broad persistent leverage it buys once active.

  **Persistence rule:** Do not charge extra just because an effect is persistent. In this project, persistence is a normal system surface. Charge for coverage, repeat leverage, and how many important exchanges the effect can keep altering.

  **Posture rule:** Anchored postures should usually stay low in Rhythm unless their coverage or payoff is extreme, because being pinned to a point is already part of their cost.

  **Memory-burden rule:** Avoid authoring Techniques around "the next action", "the next roll", or similar one-use future promises. Prefer effects that resolve immediately or persist with a clear fictional end condition.

### Mechanic creation rule

If the technique requires a mechanic that does not exist yet:

1. **Check if the concept fits within an existing system.** Existing systems include: Ailments (ailments.yaml), Agravios, learning factors and specialization domains, cost/timing mechanics, Fatigue/wound grade expressions.
2. **If it fits:** Create the new instance within that system (a new Ailment entry, a new agravio type, etc.) before writing the technique. Then trigger `mechanic-registrar` to propagate it.
3. **If it requires a new system:** Do not create it inline. Flag it as a design question, note what would be needed, and redesign the technique to use existing mechanics instead. New systems are not created inside technique authoring.

### Phase 3 — Writing

**YAML entry** (`Transcendence-design/data/system/techniques.yaml`):

All required fields: `name`, `origin`, `world_origin`, `category`, `type`, `trigger`, `requirements`, `learning`, `target`, `range`, `area`, `duration`, `cost`, `saving_roll`, `description`, `effect`, `scaling`, `restrictions`, `tags`.

The `world_origin` block requires: `primary_front` (Species / Doctrine / Region), `source`, `seed`, `focus`, `holder`, `transmission`, `availability`.

**Corebook ES entry** (`Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/`):

Follow `technique-play-surface.md` exactly. The play-facing fields in order:

1. `Tipo - Categoría` — valid values: `Activo - Ataque`, `Activo - Utilidad`, `Activo - Utilidad · Postura`, `Reactivo - Ataque`, `Reactivo - Utilidad`
2. `Nombre`
3. `Rango de Competencia`
4. `Texto de Sabor` — one strong image or turn of thought; species-shaped; brief; not a mechanical paraphrase
5. `Rango` — valid values: `Personal`, `Alcance del arma`, `Xm`, `Rango Visual`
6. `Área` — valid values: `Tú`, `1 Criatura`, `Circular Xm`, `Cono Xm`, `Línea Xm`
7. `Duración` — valid values only: `Instantáneo` or `Permanente` (end conditions go in Efecto, not here)
8. `Tirada Principal` — `T.A.` for weapon-rooted; `T.E.` for specialization-rooted; `—` for passive/no-roll
9. `Tirada de Salvación` — only if there is a distinct negating roll separate from the primary; omit or `—` otherwise
10. `Impacto` — only if there is a direct damage payload; omit or `—` otherwise
11. `Ritmo`
12. `Desgaste`
13. `Requisitos` — real game mechanisms only (profile, equipment, tracked state, formal condition); no implied common-sense physical logic
14. `Palabras Clave`
15. `Efecto` — the full mechanical effect including end conditions for Permanente effects

### Audit checklist

- [ ] Idea stated as concrete action with named origin surface before writing began
- [ ] Non-magical cause identifiable in the effect
- [ ] Effect traces to a named existing system mechanic (Ailment, Fatigue, wound, positional state, information reveal, named bonus)
- [ ] Specialization gate passed: extracted capability named before effect text
- [ ] Information gate passed if applicable: actionable truth identified, not passive bonus
- [ ] Cost calibrated against techniques.yaml cost bands
- [ ] All required YAML fields present
- [ ] Play-surface Duración is only Instantáneo or Permanente
- [ ] Requirements are real game mechanisms, not implied physical logic
- [ ] Profile/specialization requirement used, not species restriction
- [ ] Si se creó una mecánica nueva: se ejecutó `mechanic-registrar` antes de finalizar
- [ ] El texto de ambientación es breve, concreto, moldeado por la especie, no una paráfrasis mecánica

---

## bestiary-author

**Purpose:** Diseñar adversarios y fauna para Transcendence siguiendo estrictamente las reglas anatómicas y mecánicas del sistema.
**When to use:** Siempre que se requiera crear una nueva criatura o NPC para el bestiario o un escenario.

### Mandatory context (load before starting)

1. `Transcendence-design/docs/system/mechanics-overview.md` — **Fuente Primaria de Verdad**. NUNCA asumas mecánicas. Si tienes dudas sobre un concepto, búscalo aquí primero.
2. `Transcendence-publications/core-books/transcendence-corebook/` — Busca aquí SOLO si el concepto no existe en `mechanics-overview.md`.
3. `Transcendence-publications/core-books/transcendence-corebook/14-adversaries-and-bestiary/es/06-bestiario.md` — Para referencia de formato y entradas previas.

### Creation Workflow (En orden obligatorio)

1. **Intención y Descripción:** Antes de tocar números, define qué es la criatura. ¿Qué propósito narrativo y ecológico cumple? Describe su aspecto físico y su instinto primario.
2. **NR (Nivel de Referencia):** Asigna un NR. Este valor ancla a la criatura en el ecosistema. Define la dificultad de interactuar con ella y qué Nivel de Referencia mínimo deben tener los jugadores para que sea un encuentro viable.
3. **Rol de Combate:** Selecciona el Rol (Golpeador, Protector, Soporte, Lanzador). El rol dictamina su comportamiento base y multiplicadores matemáticos posteriores.
4. **Anatomía y Zonas:** Divide la criatura en sus Zonas Anatómicas lógicas. 
   - **Regla Fundamental:** TODA zona tiene un propósito puntual en la criatura. Las zonas no son solo "blancos para golpear"; cada una aloja capacidades (defensivas, sensoriales, de movilidad u ofensivas) que se desarrollarán.
   - Al menos una zona debe ser definida como el **Núcleo** (el fallo sistémico de la bestia).
5. **Rasgos (Caracter y Ventaja Evolutiva):** Define los Rasgos. Los rasgos no son habilidades mágicas, son aspectos del "carácter" del NPC (instinto predatorio, respuesta al miedo, adaptación).
   - Este carácter forja su **Ventaja Evolutiva** (Ventaja de Ejecución).
   - Debe atarse a una condición de activación narrativa y orgánica.
   - El efecto otorga Ventaja de Ejecución a las tiradas válidas del sistema (ver restricciones abajo).
6. **Matemáticas de Zonas (PV y Bloqueo):** Calcula la salud y defensa de cada zona basado estrictamente en el NR, Rol, Naturaleza y Cobertura (según `02-zonas.md`).
   - **PV Base:** Zona normal = NR × 10. Núcleo = NR × 15.
   - **PV Final:** Multiplica el PV Base por el multiplicador del Rol (Golpeador ×2, Protector ×3, etc).
   - **Bloqueo Base:** NR × 2. Multiplicado por la Naturaleza (Mortal ×1, Anomalía ×1.5).
   - **Bloqueo Final:** Multiplica el Bloqueo Base por el modificador de cobertura de esa zona específica (Tejido blando ×0.5, Piel ×1, Cuero/Escamas ×1.5, Placas óseas ×2).

7. **Durabilidad de Zonas:** Calcula qué tan difícil es romper la zona con un Impacto Crítico usando el catálogo de materiales (`08-catalogo-de-materiales.md`).
   - **Fórmula:** `Durabilidad = D Base del Material × NR × Factor de Naturaleza`
   - **Factor de Naturaleza:** Mortal = 1, Anomalía = 2, Primordial = Inmune al daño físico.
8. **Potencia de Armas Naturales:** Si la zona actúa como un arma natural (garras, colmillos, cuernos), calcula su capacidad de destrucción (usada para romper blindajes en impactos críticos).
   - **Fórmula:** `Potencia = P Base del Material Ofensivo × NR × Factor de Naturaleza`
9. **Bloque de Tiradas:** Calcula los modificadores de tirada del monstruo basándote en su NR y Rol (según `01-doctrina.md`).
   - **Modificador Base:** `NR + Rango` (Rango 1 para NR 1-2, Rango 2 para NR 3-4, etc).
   - Todas las tiradas (T.A, T.D, T.I, T.C, T.R, T.E) reciben el Modificador Base. No hay penalizadores.
   - El **Rol** añade el Modificador Base *de nuevo* (es decir, lo duplica) a las tiradas fuertes de la criatura:
     - *Golpeador:* +Base a T.A y T.I (daño fijo).
     - *Protector:* +Base a T.D y T.R.
     - *Soporte:* +Base a T.E y T.C.
     - *Lanzador:* +Base a T.A (distancia) y T.E.
   - **T.I (Daño de Monstruo):** Se calcula como `(Rango)d(Dado del arma) + (NR × Grado) + Modificador`. Para armas naturales, Grado = Rango.
10. **Habilidades y Acciones:** Toda zona de combate (ofensiva/defensiva) debe tener una habilidad atada a ella. Si la zona se rompe, la habilidad se pierde.
    - Las habilidades de los NPC se estructuran sin **Desgaste**.
    - **Formato de Salida (Plantilla Maestra):** Debes formatear TODO el bloque de la criatura (Estadísticas, Zonas, Rasgos y Técnicas) siguiendo EXACTAMENTE la misma maquetación, clases HTML (`.monster-block`) y estructura de tablas Markdown que la primera entrada (Carroñero Abisal) en el archivo `14-adversaries-and-bestiary/es/06-bestiario.md`. No inventes otros formatos; usa el Carroñero como tu plantilla inquebrantable.

### Mechanical Constraints (Reglas Inquebrantables)

- **Sin "PV abstractos":** Las criaturas se dividen en Zonas. El colapso del Núcleo significa la muerte o cambio de fase. El colapso de una Zona normal neutraliza la habilidad o rasgo atado a ella.
- **PV vs Durabilidad:** PV es la salud de la zona. Durabilidad es la dureza del material (escamas, hueso). La Durabilidad sirve **exclusivamente** para evaluar si un impacto Crítico destruye la zona de un golpe (Potencia vs Durabilidad).
- **Prohibido el uso de PA (Puntos de Acción):** La economía de acciones usa el sistema de **Ritmo** (Ataque estándar, Ataque pesado, Reacción, etc).
- **Límites de la Ventaja de Ejecución:** Los Rasgos SOLO pueden otorgar Ventaja de Ejecución a estas tres tiradas:
  - **T.A. (Tirada de Ataque):** Gobierna conectar un golpe, quebrar blindaje y superar reflejos.
  - **T.D. (Tirada de Defensa):** Gobierna el instinto de preservar la vida, esquivar, bloquear o desviar.
  - **T.E. (Tirada de Especialización):** Gobierna habilidades entrenadas (trepar, rastrear, acrobacias, etc).
- **Tiradas Prohibidas:** NUNCA otorgues ventaja a T.I. (Impacto/Daño), T.C. (Característica), o T.R. (Resistencia).
