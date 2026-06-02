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
2. `Transcendence-design/data/system/natural-attack-forms.yaml` — register the species in each attack form it uses; add a `species_profile_expressions` entry if its expression differs from the generic
3. `Transcendence-design/docs/canon/species/index.md` — add the species to the roster table
4. `Transcendence-design/docs/canon/species/species-development-status.md` — add a layer-by-layer assessment

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

This section is the bridge to the publications stat block. It must include:

- **Competency affinities** — which skill trees this species naturally justifies; use names from `specializations-catalog.yaml`
- **Natural attack logic** — which forms, what combat role, how species-specific expression differs from the generic
- **Arsenal fit** — likely weapon categories beyond natural attacks
- **Candidate Características** — which 3 attributes get +1
- **Candidate Herencia** — the one complex or penalty trait: what condition triggers it, what effect, determined by whom
- **Candidate Legado** — scaling traits: how many, what they scale with, what skill or roll type
- **Technique implications** — what the species' Technique body should emphasize and what it should avoid

All values in §9 are candidates. Final stat block values are authored in the publications file.

### Completion checklist

- [ ] All 10 sections present
- [ ] §9 includes explicit Características/Herencia/Legado candidates
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
