---
name: "module-development"
description: "Use when designing or developing a campaign module — locations, scenes, encounters, NPCs, lore, pacing, or validating ideas against established system and setting rules."
---

# Skill: Module Development

Use this skill when working on any campaign module for Transcendence — designing locations, scenes, encounters, NPCs, lore entries, pacing, or validating ideas against the established system and setting.

---

## What this skill governs

- Developing and growing a campaign module document
- Validating design ideas against established system rules, setting canon, and module axioms
- Accumulating ideas and moving them from rough notes to designed content
- Consistency checking: does this element contradict something already defined?
- Scene, location, encounter, NPC, and lore design

This skill does NOT govern:
- Technique authoring (use `technique-authoring` skill)
- Species design (use `species-design` skill)
- Corebook prose (use `corebook-prose` skill)

---

## Step 1 — Load mandatory context

Always read these two documents first, before any module work:

1. `Transcendence-design/docs/modules/module-design-axioms.md`  
   The 7 design axioms. Every decision is filtered through these.

2. `Transcendence-design/docs/campaign-module-reference.md`  
   Loading reference by task type — tells you which docs to read for each design area.

Then load the specific module's master document (see Step 2).

---

## Step 2 — Load the module document

Each module lives in `Transcendence-design/docs/modules/<module-name>/`.

The module document is the central file where ideas accumulate and get formalized. Load it before adding or validating anything.

If the module document does not yet exist, create it using the structure defined in `module-design-template.md`.

---

## Step 3 — Load task-specific context

Use `campaign-module-reference.md` to identify which docs to read for the current task:

| Task | Load |
| --- | --- |
| Designing a location | Environmental conditions, cover/visibility, tauma-cosmology if relevant |
| Designing a combat encounter | Combat ADRs (architecture, ATB, readability, elite if applicable) |
| Designing a creature | creatures.md, creature-cycles.md, natural-attack-forms.md |
| Designing an NPC | species-relations.md (relevant axes), species canon doc |
| Adding taumatic/cosmic content | world-foundations.md, tauma-cosmology.md, limbo docs |
| Adding equipment or loot | equipment docs, materials-and-fabrication.md |

Do not load all docs at once. Load only what the current task needs.

---

## Step 4 — Apply the axiom filter

Before finalizing any design element, run it through the 7 axioms in `module-design-axioms.md`:

1. Is this system element organic or forced?
2. Does this scene's register fit the cadence — or is it following a pattern?
3. Is horror/hostility earning its presence?
4. Is the system complexity appropriate for the arc phase?
5. Does this location exist as a place, not a game board?
6. Is this structural beat predictable by genre convention?
7. Does this serve the arc without overfilling it?

If any answer is wrong, revise before proceeding.

---

## Step 5 — Record and accumulate

All design decisions go into the module document:

- **Settled content:** full description, validated against axioms and canon
- **Open ideas:** rough notes that haven't been developed yet
- **Pending decisions:** design questions that need resolution before the adjacent content can be finalized
- **Discarded ideas:** ideas that were explored and rejected, with a brief note on why — so they don't re-emerge

Ideas evolve in the module document — they start as rough notes, get developed, get validated, and become settled content. The module document is never "done" until the module is finished.

---

## Consistency validation checklist

Before adding any element to settled content, confirm:

| Question | Where to check |
| --- | --- |
| Does this contradict established species behavior? | `docs/canon/species/<especie>.md`, `species-relations.md` |
| Does this contradict world physics? | `docs/canon/world-foundations.md` |
| Does this break a combat system rule? | Relevant combat ADR |
| Does this system element belong to this arc phase? | Axiom 4 — progressive exposure curve |
| Does this feel like it belongs in this world, or in a different genre? | Axiom 3, Axiom 6 |
| Does this introduce a system before it's been established? | Check module's current system exposure state |

If any check fails, either revise the element or explicitly note that it is pending resolution.

---

## What NOT to do

- Do not load technique YAML or technique seeds for module work — they are for technique authoring
- Do not insert system elements to "balance the encounter types" — organic placement only
- Do not introduce taumatic or cosmic content early in the arc without checking the exposure curve
- Do not write location descriptions as tactical maps — write them as places
- Do not resolve all open threads — some are intentionally left open
