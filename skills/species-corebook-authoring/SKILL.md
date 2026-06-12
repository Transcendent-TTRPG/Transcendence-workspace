---
name: "species-corebook-authoring"
description: "Use when a species design document must be converted into a reader-facing corebook prose entry with mechanical stats. Follow the corebook authoring workflow instead of adapting design text directly."
---

# Species Corebook Authoring

Use this skill when the task is to write the reader-facing corebook entry for a species.

This skill converts a stable species design document into two outputs:
1. Narrative prose sections in `Transcendence-publications/core-books/transcendence-corebook/06-species/es/`
2. A mechanical stats block appended to that entry

It does not design the species, create technique seeds, or author techniques. If the design document is incomplete or has unresolved mechanical values, surface those gaps before writing.

---

## When to use this skill

Use `$species-corebook-authoring` when:

- a species design doc exists in `Transcendence-design/docs/canon/species/` and needs a corebook entry
- a corebook entry must be rewritten because the design doc changed significantly
- the mechanical stats block needs to be created or re-synchronized

Do not use this skill when:

- the species design doc does not exist (create that first)
- the task is to audit species content across the full pass → use `species-pass-audit`
- the task is to author techniques for the species → use `technique-authoring`

---

## Required context

Load in this order before writing anything:

1. **Species design doc:** `Transcendence-design/docs/canon/species/<species>.md`
2. **Style reference:** `Transcendence-publications/core-books/transcendence-corebook/06-species/es/04-drakkai.md`
3. **Editorial rules:** `Transcendence-publications/CLAUDE.md`
4. **Chapter intro:** `Transcendence-publications/core-books/transcendence-corebook/06-species/es/00-las-especies.md`

---

## Execution pattern

### Phase 1 — Design doc audit

Before writing, read the species design doc and check:

| Item | Check |
| --- | --- |
| Identity | Is the section clear enough to write narrative prose from? |
| Body / physiology | Is the physical description complete? |
| Natural weapons | Do they have T.A. / T.I. / Alcance / Daño / Durabilidad / Potencia defined? |
| Characteristic bonuses | Are the +1 allocations decided? |
| Herencia | Is the biological constraint defined as a mechanic? |
| Legados | Are the NR-scaling bonuses defined? |
| Lifespan / size / speed | Are the Datos Generales values present? |

If any item is missing, surface the gap to the user and confirm values before proceeding. Do not invent mechanical values — confirm them.

### Phase 2 — Prose sections

Write the narrative sections in ES following this structure:

| Section | What it covers |
| --- | --- |
| **El Cuerpo** | Physical form, senses, natural weapons described narratively, vulnerabilities |
| **La Cultura** | Civilization, institutions, daily rhythm, internal tensions |
| **Teología y Cosmología** | What they believe, what they know, what they don't, civilizational anxiety |
| **Organización e Identidad Interna** | Factions, roles, variation, dissenters, outcasts |
| **Vida Cotidiana** | Life cycle, daily practice, what death means to them |
| **Relaciones con el Mundo** | How other species see them, specific cross-species relationships |
| **Como Personaje Jugador** | What the character knows, doesn't know, combat identity, reasons to leave home |

#### Voice rules — mechanics

- Write as a book being read, not a design document being consulted
- No bullet lists in the narrative sections — continuous prose only
- No sub-headers within sections
- Do not use the words "interesante" or "único"
- ES throughout all sections. EN mechanical terms (T.A., T.E., ATB, NR) appear only in the stats block

#### Voice rules — narrative technique

The design document contains facts about the species. The corebook prose contains what those facts *feel like*. The difference between these two things is everything.

**Translate implications, not content.** The design doc says what the species does or believes. The prose shows what that looks like from the outside — or from the inside, in ways a reader can inhabit. "Los objetos mismos, los encuentros que no tienen categoría, las notas sobre lo que todavía no tiene respuesta" does not describe accumulation — it shows the specific texture of Drak'kai accumulation. Never summarize a trait. Find the specific thing the summary would point at and show that instead.

**Compress.** One concrete observable detail is worth more than three descriptive sentences. "La pregunta que los sigue no es cuándo llegará el desastre" lands because it's specific, because it reframes dread as a permanent companion rather than a future event. Always prefer the image that implies the meaning over the sentence that states it.

**Subtext is the primary instrument.** The civilizational anxiety, institutional tensions, and species horror must never be named directly. If you write "their deepest fear is X," you have killed the fear. The goal is to leave the reader with a feeling they can't fully articulate — and that feeling comes from accumulation of specific details, not from statements about what those details mean. Three words that imply the thing are worth more than a paragraph that explains it. The civilizational anxiety belongs in the Teología section, woven into the texture of what the species knows and can't yet answer — not stated as a direct fear.

**Institutions and tensions are noticed, not introduced.** Don't define an institution and then describe it. Don't say "the deepest internal tension is X." Arrive at the institution through what a traveler would observe, or what a member does without thinking, and let the reader find the shape of it. Tensions emerge from behavior, not from naming them.

**Each paragraph does one thing.** It establishes something, shifts something, or lands something. If a paragraph is doing three things, it's probably a checklist in prose clothing. Write until the paragraph has done its one thing, then stop.

**The opening paragraph earns the species.** It should put the reader inside the species — not summarize who they are. The Drak'kai entry opens with a correction ("no en archivos ni catálogos — los objetos mismos") that immediately shows something specific and unexpected. The first paragraph of a species entry should make the reader want to keep reading, not give them a description of what they're about to read.

**Do not follow the design doc's order.** The design doc is organized for completeness. The corebook prose is organized for narrative momentum. Find the thread that makes the species feel real — that thread is rarely "identity, then body, then culture" in a straight line. The sections are the destination; the route is yours to find.

#### Rhythm and structure — avoiding uniform prose

These are the specific failure patterns that make species prose feel generated rather than written. Check for all of them before considering a draft done.

**Don't announce the paragraph; enter it mid-thought.** The first sentence should be doing the thing, not introducing what you're about to say. "Escribir algo, para un Loxod, no es guardar información. Es terminar de recibirla." arrives inside the idea. "La cultura Loxod se centra en la gestión de resonancia." announces it. The second version kills curiosity before the paragraph begins.

**Vary sentence length dramatically within the same paragraph.** A long sentence followed by two of similar length creates a uniform beat that reads as mechanical. Cut short after a long sentence. Let the next run longer. The rhythm should feel unpredictable even when the prose is controlled.

**Conclusions don't anchor paragraphs.** A clean, quotable final sentence that wraps up what the paragraph was about — "El archivo es tratamiento antes que custodia." — is the most reliable tell that the prose was generated. Either bury the insight in the middle of the paragraph, or leave it unstated and let the reader arrive at it from the specifics. Paragraphs should often end on the fact itself, not on what the fact means.

**Let things be incomplete.** "se gestiona si hay forma de hacerlo" — the conditional is correct. Not everything resolves. Not everything has a point. Some statements end on the observation without telling the reader what to do with it. This is more honest and less uniform than prose that ties off every thread.

**Triple parallels are the AI rhythm tell.** Two parallel phrases can create useful tension. Three in succession — "No a apagarlo — no tiene apagado. A gestionarlo." — reads as a constructed pattern, not as a person writing. Watch for any place where the same grammatical structure repeats three or more times in a row and break it.

**Vary where the insight arrives across sections.** In one section the key idea appears in the first sentence. In the next it's buried in the third paragraph. In a third section it's implied but never stated. If every section has the same shape — setup, then implication, then landing — the entry will feel uniform even if each individual section is correct.

**Section openings shouldn't orient the reader.** The first sentence of a section should not tell the reader what the section is about. It should drop them inside something. The Teología section of the Loxod entry opens with "Lo que los Loxod saben del Tauma lo saben porque lo reciben directamente en sus propios sistemas, en condiciones documentadas, replicables" — it's already making a specific claim, not introducing that you're about to discuss theology.

#### Common failure mode

**Design doc paraphrase:** taking the identity section of the design doc and reformatting it into complete sentences. The result reads like a checklist where each item corresponds to a section heading in the design document, and every paragraph settles into "here is the next thing about this species." The test: read the Drak'kai entry and then read the new entry. If the new one feels like a summary and the Drak'kai one feels like a world, rewrite.

### Phase 3 — Mechanical stats block

Every field requires a value. Do not leave entries blank.

#### Datos Generales

```
| Longevidad | Tamaño | Estatura | Peso | Velocidad |
```

Use values from the design doc. If Velocidad is not specified, confirm with the user — do not default silently.

**Idiomas:** `<native language name> (nativo) · Común`

#### Características

List which characteristics receive `+1`. Standard allocation is two or three. Derive from the design doc's characteristic affinity section and confirm with the user.

#### Herencia

The biological constraint — something the species cannot turn off. Usually a vulnerability or perceptual limitation arising from their physiology. One entry. Must feel like a biological reality, not a game balance adjustment.

Format model (Drak'kai):
> **Percepción Interferida** — [description of what it is biologically]. Los [Species] reciben una penalización permanente de `−X` a [specific T.E.]. Esta penalización no proviene de un estado ni de una condición — es la forma en que la especie percibe.

#### Legado

Two or three NR-scaling bonuses that reinforce the species' identity in play. Each should map to something concrete in the design doc — a biological capability, a cultural practice, or a structural advantage.

Format: `+1 por cada cuatro Niveles de Referencia a [X]`

Do not invent Legado entries that have no basis in the design doc.

#### Armas Naturales

For each natural weapon:

1. State all members who have access (usually "Todos los [Species]" or a variant group) and whether it is Principal or Auxiliar
2. Write the stat table:

```
| T.A. | T.I. | Alcance | Daño | Durabilidad | Potencia |
```

3. List profiles (2–4 from `Transcendence-design/data/system/weapon-technique-profiles.yaml`)
4. Write the effect text — the conditional that triggers on a strong T.A. margin (usually "supera la T.D. por 3 o más")
5. Include a rank-scaling severity table if the effect scales

### Phase 4 — File and frontmatter

**Frontmatter template:**

```yaml
---
title: "<Species Name>"
type: corebook
content_kind: lore
writing_mode: prose
language: es
chapter: 6
status: draft
canonical: false
tags: [species, <species-slug>, lore, <2–3 identity tags>]
authority_refs:
  - Transcendence-design/docs/canon/species/<species>.md
related:
  - core-books/transcendence-corebook/06-species/es/00-las-especies.md
---
```

**File path:** `Transcendence-publications/core-books/transcendence-corebook/06-species/es/<nn>-<species-slug>.md`

The `<nn>` number follows the existing sequence (01 naghii, 02 sauri, 03 zarnag, 04 drakkai → next is 05).

---

## Quality rules

- Prose sections must read as lore, not as design doc points reformatted into sentences
- The stats block must be consistent with `Transcendence-design/data/system/`
- Weapon profiles listed must exist in `weapon-technique-profiles.yaml`
- Legado bonuses must derive from the design doc — no invented content
- The Herencia must describe a biological reality, not a balance decision
- The civilizational anxiety must be present but never named directly
- "Como Personaje Jugador" must give a player enough to want to play this species
- The prose must not mechanically follow the design doc's section order — find the narrative thread
- Final test: read the Drak'kai entry (`04-drakkai.md`), then read this entry. If this one feels like a summary and the Drak'kai one feels like a world, rewrite

---

## Reference map

| Resource | Path |
| --- | --- |
| Species design doc | `Transcendence-design/docs/canon/species/<species>.md` |
| Style reference | `Transcendence-publications/core-books/transcendence-corebook/06-species/es/04-drakkai.md` |
| Editorial rules | `Transcendence-publications/CLAUDE.md` |
| Weapon profiles | `Transcendence-design/data/system/weapon-technique-profiles.yaml` |
| Chapter intro | `Transcendence-publications/core-books/transcendence-corebook/06-species/es/00-las-especies.md` |
