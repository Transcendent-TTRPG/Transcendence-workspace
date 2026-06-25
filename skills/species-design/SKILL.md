---
name: "species-design"
description: "Use when designing a new species from scratch or redesigning an existing concept. Covers the full pre-design-doc discussion: biological base, cultural anchor, Tauma relationship, cross-species positioning, civilizational concept, and horror. Output is a confirmed concept ready to be formalized into a species design doc."
---

# Species Design

Use this skill when the task is to design or redesign a species — before any design
doc exists or when an existing concept needs fundamental revision.

This skill governs the discussion phase. Its output is a confirmed design concept
clear enough to write a species design doc from. It does not write the design doc
itself, the corebook entry, or the technique seeds.

---

## When to use this skill

Use `$species-design` when:

- a species is being designed from scratch (no design doc exists)
- an existing species concept is considered "floja" or fundamentally unclear
- a provisional entry in `species-concept-index.md` needs to be developed into a
  full design concept

Do not use this skill when:

- the design concept is already confirmed and a design doc needs to be written
  → proceed directly to the 10-layer template in
  `docs/canon/species/species-template.md`
- the task is to convert an existing design doc into a corebook entry
  → use `species-corebook-authoring`
- the task is to re-localize an already-authored chapter-06 species entry away
  from chapter-12 explanatory voice
  → use `species-cosmology-localization`

---

## Required context — load before any discussion begins

Load in this order. Do not skip any item.

### 1. Setting foundations
Read `docs/canon/world-foundations.md` in full.

This document defines the survival premise, the Tauma as fundamental physics,
the human era, how life re-emerged, the mortal/Anomalía/playable-species
distinction, bio-organic technology, and human ruins. Every species design must
be internally consistent with these foundations.

Critical rules to hold during the entire discussion:

- **No species can manipulate the Tauma directly.** What looks like Tauma
  interaction is always: biological sensitivity to the physical signatures
  Tauma-saturation produces, empirical observation of Tauma effects, cultural
  interpretation of Primordial events, or use of vestigos/vínculos (where the
  entity uses the creature, not the reverse).
- **Settlements are refuges, not power centers.** Civilizational concepts must
  survive contact with a world where survival is the constant state.
- **Biological life expectancy ≠ actual life expectancy.** Culture, theology,
  and institutions reflect this gap.
- **Mortal animals and Anomalías exist as distinct categories.** The evolutionary
  lines that produced playable species did not branch back — no mortal
  counterparts exist for playable species' animal bases.

### 2. Species concept index
Read `docs/canon/species/species-concept-index.md` in full.

This document contains: all 20 species (confirmed, in-progress, provisional) with
their animal base, cultural anchor, core concept, Tauma relationship, and
cross-species friction; and the pantheon framework section.

Use this during non-overlap analysis. No two species should occupy the same
conceptual space. Cross-species friction must be specific and bidirectional.

### 3. Limbo and Tauma mechanics
Read in this order:
- `docs/system/tauma-cosmology.md`
- `docs/system/limbo-entities.md`
- `docs/system/limbo-manifestations.md`

These documents define: the gradient mechanism, how Primordials form and what
they are, the three manifestation types (ambient flow, vestigio, vínculo), and
the four entity levels (Fragmento, Entidad, Soberano, Abismal). The Tauma
relationship section of every species design must be consistent with these
documents.

### 4. Materials
Read `docs/system/materials-and-fabrication.md` §Living Materials and
§Material state.

Relevant for species that interact with umbral materials or whose biology
involves Tauma-reactive tissue. Not required in detail for every species — skim
and load fully only if the species concept has a materials-adjacent angle.

### 5. Existing species docs (situational)
If the new species is closely related to or likely to conflict with a confirmed
species, read that species' design doc from `docs/canon/species/` before the
discussion begins. Priority: any species flagged in the concept index as having
specific friction with the new species.

---

## Execution pattern

### Phase 1 — Biological base

Identify the animal and filter its traits through a single question:

> *What persists regardless of intelligence level or bipedalism?*

**Keep:** temperamental traits (solitary, territorial, hierarchy-oriented),
neurological traits (sensory emphasis, reactivity patterns), anatomical traits
that change function but not nature in a bipedal intelligent form (a horn is still
a horn; thick skin is still thick skin).

**Discard:** capability-dependent behaviors that only make sense without
intelligence or hands (mud-wallowing for thermoregulation, migration driven by
inability to plan, etc.). An intelligent bipedal version of this animal has
access to tools, planning, and social learning — behaviors that depend on lacking
those things don't survive the translation.

Produce: a list of the biological traits that will be load-bearing for the
design.

### Phase 2 — Cultural and mythological anchor

Every species needs a real cultural or mythological tradition as its anchor — not
just the animal. The anchor provides the lens through which the species is
filtered into a civilization.

The anchor must be:
- **Real** — a specific culture, mythology, or historical tradition, not an
  invented analog
- **Resonant with the animal base** — the tradition should feel like it was
  always waiting for this animal
- **Generative** — it should open new design questions, not close them

Ask: what does this tradition give the species that the animal base alone
doesn't? What tensions does the combination of animal + anchor create?

### Phase 3 — Tauma relationship

Define how this species experiences, encounters, or is shaped by the Tauma.

**Hold the constraint throughout this phase:** no mortal species can manipulate
the Tauma directly. The relationship must be one of the following:

- **Biological sensitivity** — their body reacts to physical signatures of
  Tauma-saturation (not to the Tauma itself), the way umbral materials do but
  biologically. The reaction is real; the mechanism is opaque to them.
- **Empirical observation** — they have accumulated data on how Tauma effects
  manifest and what patterns they follow, without understanding the underlying
  physics. They use that knowledge operationally.
- **Cultural interpretation** — their theology and ritual are responses to
  Primordial events they have experienced, interpreted through their cultural
  frame. The interpretation is theirs; the events are real.
- **Exposure and vulnerability** — their work, environment, or biology puts them
  in proximity to Tauma-saturated zones or objects, and the effects of that
  exposure have shaped their culture.
- **Vestigo/vínculo tradition** — they have systematized use of Tauma-charged
  objects, not understanding the mechanism but knowing the use patterns. The
  entities in those objects use them; not the reverse.

Define: what does the Tauma do to this species? What do they believe it is?
What does their culture do about that? What does their culture get wrong?

### Phase 4 — Cross-species positioning

Check the new species against the species-concept-index. For each confirmed and
in-progress species, ask:

- Does this new species occupy the same conceptual space?
- Is their primary relationship with the Tauma different enough to justify a
  distinct species?
- What specific friction does this species create for each relevant species, and
  why?

The friction must be **specific and mechanical** — not "they don't trust each
other" but "Ceratox horns react to Formix chemical signals in contaminated zones,
creating false positives that the Ceratox cannot override and the Formix cannot
prevent."

Produce: a friction entry for each species where the relationship is non-trivial.
Update the species-concept-index provisional entry if one exists.

### Phase 5 — Civilizational concept

Design what their society actually looks like given:
- The survival premise (refuges, not empires; the space between settlements is
  hostile; culture is survival technology)
- Their biology (solitary vs. social, territorial vs. nomadic)
- Their Tauma relationship (does their ability/vulnerability create a specific
  economic or social role?)

Ask the horror pressure test questions from `species-template.md`:
- What is trying to kill, corrupt, starve, isolate, or mislead them?
- What daily habits exist because safety cannot be assumed?
- What does this species do because the world is cruel, not because it is elegant?
- What part of their belief system may be true enough to help them and wrong
  enough to destroy them?

A civilizational concept that could exist in a stable modern world is not the
right concept. The civilization should read like a survival strategy that
developed a cultural identity, not a stable culture that happens to face
dangers.

### Phase 6 — The horror

Every species has a specific civilizational anxiety — the question at the heart
of their culture that their entire existence is organized around but that cannot
be fully answered.

The horror must be:
- **Specific** — not "they fear the dark" but "they cannot distinguish, at the
  margin, between the horn providing information and the horn controlling them"
- **Internal** — arising from what they are, not just from external threat
- **Unresolvable** — something their culture wrestles with rather than solves

The horror must never be named directly in corebook prose. It lives in the
texture of what the species does, believes, and cannot stop doing. Confirm it
here, in the design phase, so it can be woven in rather than announced.

### Phase 7 — Concept confirmation

Before declaring the concept ready to formalize:

| Checkpoint | Question |
| --- | --- |
| Biological base | Are the load-bearing traits clearly derived from animal biology? |
| Anchor | Is the cultural/mythological anchor specific and real? |
| Tauma relationship | Does it follow the no-direct-manipulation rule? |
| Non-overlap | Is the conceptual space distinct from all existing species? |
| Civilizational concept | Does it pass the survival-premise test? |
| Horror | Is it specific, internal, and unresolvable? |
| Species-concept-index | Is the entry ready to update? |

If any checkpoint fails, resolve it before proceeding to design doc.

---

## Output

At the end of this phase, produce:

1. **Updated species-concept-index entry** — Animal/Size, Anchor, Core (1–2
   sentences), Tauma, Friction. Update the file directly.

2. **Design concept summary** — A short paragraph (not the full design doc)
   capturing the confirmed concept in enough detail that the 10-layer design doc
   can be written from it without returning to this discussion.

The design doc itself follows the template at
`docs/canon/species/species-template.md`. Writing that is the next step, separate
from this skill.

---

## What this skill does not cover

- Writing the species design doc (use the 10-layer template directly)
- Writing the corebook entry (use `species-corebook-authoring`)
- Re-localizing an existing chapter-06 species whose cosmology sounds like the
  player/narrator truth layer instead of species-local belief (use
  `species-cosmology-localization`)
- Authoring technique seeds (separate authoring session after design doc exists)
- Authoring techniques (use `technique-authoring`)

---

## Reference map

| Resource | Path |
| --- | --- |
| Setting foundations | `docs/canon/world-foundations.md` |
| Species concept index | `docs/canon/species/species-concept-index.md` |
| Tauma cosmology | `docs/system/tauma-cosmology.md` |
| Limbo entities | `docs/system/limbo-entities.md` |
| Limbo manifestations | `docs/system/limbo-manifestations.md` |
| Materials | `docs/system/materials-and-fabrication.md` |
| Species template | `docs/canon/species/species-template.md` |
| Corebook authoring | `skills/species-corebook-authoring/SKILL.md` |
| Cosmology localization | `skills/species-cosmology-localization/SKILL.md` |
