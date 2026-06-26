---
name: "species-cosmology-localization"
description: "Use when a corebook species entry must be revised so its cosmology reflects species-local belief rather than chapter-12 objective metaphysics. Audits epistemology drift, maps which chapter-12 phenomena the species would actually interpret, defines species-native terminology only where justified, and integrates that vocabulary into the prose."
---

# Species Cosmology Localization

Use this skill when revising a species entry in:

- `Transcendence-publications/core-books/transcendence-corebook/06-species/es/`

The goal is not to redesign the species or rewrite the whole entry. The goal is to make the species speak from its own cosmology rather than from the objective metaphysical voice of chapter 12.

This skill is for the exact kind of pass where:

- chapter 12 contains the player/narrator truth
- the species should not sound like it has read chapter 12
- the species may still be describing real chapter-12 phenomena
- those phenomena should be filtered through species-local belief, ritual, language, and error

The output is:

1. A brief audit of cosmology drift
2. A species-specific concept map for chapter-12 phenomena
3. Species-native terminology only where it makes sense
4. A revised species entry with objective-metaphysics leakage removed
5. A closure check on whether the species actually needed a taxonomy at all

If, after the revision pass, you want a separate closure review focused only on
narrative quality and cosmological integration, use:

- `references/narrative-audit-prompt.md`

This is especially useful as a second-pass audit when the species is already
close to finished and you want to validate whether it still sounds too clean,
too explanatory, too taxonomic, or too much like narrator truth instead of a
living civilization.

Important correction:

- `vestigios` and `vínculos` are both **objects**
- they are not places
- a place may be charged, permeable, old, sacred, dangerous, or responsive without
  therefore being a `vínculo`
- species may blur object-behavior and place-behavior in their belief systems, but
  the reviser must not confuse the chapter-12 ontology

---

## When to use this skill

Use `$species-cosmology-localization` when:

- a species entry in chapter 06 sounds too much like chapter 12
- the species needs its own interpretation of `vestigios`, `vínculos`, `primordiales`, or `aflicciones`
- the cosmology section needs to be rewritten in species-local voice
- the species already has strong identity, but weak internal metaphysical vocabulary
- a species needs the same kind of start-to-finish pass that was done for `Naghii`

Do not use this skill when:

- the species concept itself is unclear or broken from the ground up
- the task is to create a full species entry from a design doc
- the task is only mechanical stats synchronization
- the task is only a broad audit across many species with no intention to revise one species deeply

In those cases, route first through:

- `species-design`
- `species-corebook-authoring`
- `species-pass-audit`

---

## Core principle

Chapter 12 is the truth of the setting.

Species entries are not.

A species entry should describe:

- what that species notices
- what that species believes is happening
- what that species gets right
- what that species gets wrong
- what vocabulary that species uses for recurring phenomena

Do not remove real metaphysical phenomena from the species if their civilization would clearly encounter them.

Do remove chapter-12 explanatory voice from the prose.

The species does not need to interpret every chapter-12 category equally. Only localize what their cosmology would plausibly encounter, care about, and build institutions around.

Also remember:

- chapter-12 categories are narrator truth
- species-local categories are usually built from **lived use**, ritual handling,
  intergenerational memory, and misinterpretation
- a species may encounter the same object-category for generations and still never
  distinguish `vestigio` from `vínculo` as separate concepts

## Civilization baseline note

When reasoning about what a species could plausibly know, do **not** map the
setting too literally to human historical Bronze Age or antiquity.

The species of this world are often operating at a **B.C.-like** civilizational
stage, but that is only an analogy of social scale, institutional fragility, and
limits of formalized knowledge.

It is **not** a literal human Bronze Age baseline.

Important differences:

- Tauma is real and shapes the world even when species do not understand it
- ruins of older civilizations survive as real cultural pressure, not just myth
- later-born civilizations may model institutions, symbols, or aspirations after
  ruins they do not truly understand
- those ruins are not only fear sources or sacred leftovers; they can also serve
  as inspiration, aspiration, imitation, or civilizational reference for later
  species
- parts of the world's technology are living, biological, or hybrid rather than
  inert mechanical systems
- some inherited technologies include living organisms, reactive matter, or
  half-understood biological functions, so "technology level" cannot be judged
  by human industrial analogies alone
- preindustrial does not mean intellectually naive
- ritual knowledge, long memory, embodied practice, and inherited caution may
  produce extremely sophisticated interpretations without producing scientific
  chapter-12 truth

So when asking “would this species know this?”, do not ask:

- “would a human Bronze Age culture know this?”

Ask instead:

- “would this species, with its body, rituals, ruins, inherited technology,
  environmental exposure, and survival pressures, have built a stable belief
  about this?”

---

## Required context

Load in this order before revising anything:

1. **Target species entry**
   `Transcendence-publications/core-books/transcendence-corebook/06-species/es/<species-file>.md`

2. **Target species design doc**
   `Transcendence-design/docs/canon/species/<species>.md`

3. **Chapter 12 truth layer**
   - `Transcendence-publications/core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/01-el-limbo.md`
   - `Transcendence-publications/core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/03-vestigos.md`
   - `Transcendence-publications/core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/04-vinculos-y-aspectos.md`
   - `Transcendence-publications/core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/05-entidades.md`

4. **Species chapter intro**
   `Transcendence-publications/core-books/transcendence-corebook/06-species/es/00-las-especies.md`

5. **Reference species if useful**
   If a previous species already models this well, read it.
   Example: `14-bufoni.md` for strong species-local metaphysical language.

---

## Execution pattern

Treat this as a strict multi-phase workflow. Do not jump straight into rewriting.

### Phase 1 — Brief drift audit

Identify where the species entry leaks chapter-12 voice.

Look for language that sounds like objective metaphysics rather than local belief, for example:

- direct explanation of how Tauma flows
- direct explanation of how Limbo works
- terms like `flujo`, `canal`, `permeabilidad`, `entidad`, `manifestación`, `sistema nervioso` used as if the species knows the real mechanism
- certainty where the species should have doctrine, ritual, or observed pattern

Produce a short list of:

- lines or passages that are fine
- lines or passages that need rewriting
- why they sound too close to chapter 12

If the species has already been revised once and the goal is closure rather than
discovery, you may run the separate prompt in
`references/narrative-audit-prompt.md` after completing the workflow below.

### Phase 2 — Phenomenon map

Before inventing vocabulary, decide what the species would actually interpret.

Use this frame:

| Chapter-12 concept | Does this species encounter it? | How would they encounter it? | Does it matter enough to name? |
| --- | --- | --- | --- |
| Limbo / outer depth | yes/no | as sky, underworld, river-source, etc. | yes/no |
| Vestigios | yes/no | through relics, ruins, tools, graves, offerings, etc. | yes/no |
| Vínculos | yes/no | through chambers, rites, sovereigns, artifacts, nodes, etc. | yes/no |
| Primordiales | yes/no | as gods, presences, responses, powers, masks, etc. | yes/no |
| Aflicciones | yes/no | as marks, illness, blessing, contamination, burden, etc. | yes/no |

Important:

- Do not force all four concepts into every species
- Do not skip obvious concepts that the species' civilization clearly revolves around
- A species may need an umbrella category instead of four parallel categories
- A species may collapse several chapter-12 phenomena into one doctrinal frame
- A species may need no local term at all for one or more categories
- A species may classify objects by ritual destination, social use, or civilizational function rather than by chapter-12 metaphysical type
- A species may distinguish two manifestations only after repeated lived use, not by observation alone
- scarcity matters: vestigios and vínculos are not common-use household objects in most civilizations; they are usually rare enough that many cultures never build stable mass vocabulary around them

After this first map, ask a second layer of questions explicitly:

- Is the Limbo important to this species **as its own concept**, or is it absorbed
  into a broader idea such as sky, current, hunger, revelation, depth, or the
  other world?
- Are marked objects important to this species at all?
- If marked objects matter, does the species actually distinguish two kinds of
  object in lived use, ritual handling, or social consequence?
- If it distinguishes them, is that distinction really about `vestigio` versus
  `vínculo`, or about something else entirely such as closed/open, personal/common,
  safe/dangerous, preserving/draining, silent/responding?
- Are primordial presences important to the species as a separate idea, or do they
  only appear absorbed into another concept such as gods, navigators, faces,
  presences, judges, guides, or corrupted places?
- Are aflicciones important to the species as their own category, or are they only
  legible as marks, communion, contamination, revelation, fracture, hunger,
  blessing, or burden?

Important distinction:

- a concept can be **important**
- and yet not exist as an independent category in the species' cosmology

So always validate both:

- whether the species cares about the phenomenon
- whether the species isolates it conceptually, or instead folds it into another
  larger doctrinal frame

Also validate three more things:

- **Importance is not the same as frequency.**
  A phenomenon may be extremely rare and still shape sovereignty, ritual,
  authority, taboo, fear, or prestige. A phenomenon may also be common and never
  become a stable formal category. Do not assume scarcity means low importance,
  or recurrence means high conceptual clarity.

- **Who inside the species actually knows this?**
  Do not flatten a whole civilization into one epistemic layer. Ask whether the
  knowledge belongs to:
  - common people
  - a priesthood, scholar caste, or funerary order
  - rulers, lineages, or ritual specialists
  - scouts, workers, or field practitioners
  - rumor, taboo, fragment, or half-understood inheritance

  The answer should shape the prose. A species entry may describe a civilizational
  belief that most individuals only know in diluted, distorted, or practical form.

- **What is doctrine, and what is merely practice?**
  A species may have weak theory but strong handling habits. It may know what to
  fear, seal, carry, burn, preserve, or test without having a clean metaphysical
  explanation for why. Always separate:
  - what the species believes
  - what the species does
  - what seems to work even when the species does not know why

### Phase 2.5 — Creature experience map

Before designing terminology, translate chapter-12 truth into what a **single
creature** actually experiences.

Do this from the user's side of the object, not from the narrator's taxonomy.

Ask:

- what does first contact feel like?
- what changes before the object can even be used?
- what does the creature think is happening while the object is still undiscovered?
- what difference, if any, is perceptible between one kind of object and another?
- what costs are experienced as perception, burden, exhaustion, obsession, calling,
  revelation, contamination, etc.?

Use the chapter-12 discovery model explicitly:

- undiscovered objects do nothing intentionally
- first meaningful contact creates a **Leve Aflicción** in the linked sense
- clues arrive through that Aflicción
- understanding must be built before intentional use exists
- the object's real category may remain unknown even after use begins

Translate each category into lived experience:

- **Vestigo**
  Usually experienced as an object that, once discovered, can be used and tends to
  intensify perception through repeated use. The user may notice that it “opens”
  something, “clarifies” something, or leaves marks of perception behind.

- **Vínculo**
  Usually experienced as an object that, once discovered, responds more heavily to
  use and begins to **charge**, **drain**, **weigh on**, or **reorganize** the
  portador. The user may not know it will never run out. What they may know is that
  it exacts a different kind of cost.

- **Primordial / entity-presence**
  Usually not experienced as “I have identified a primordial.” More often it is
  lived as a place that responds, a presence that insists, a force behind repeated
  signs, a sacred or hostile attention, or something that sustains conditions beyond
  normal explanation.

- **Aflicción**
  Usually not lived as a chapter-12 diagnostic term. It is experienced as sensory
  distortion, burden, revelation, contamination, blessing, calling, hunger,
  communion, pressure, or some other culturally framed change in how the world is
  being perceived.

Do not assume species distinguish `vestigio` and `vínculo` just because chapter 12
does. Distinguish them only if the civilization would plausibly notice a stable,
repeatable difference in lived cost or institutional handling.

### Phase 3 — Taxonomy design

Only after the phenomenon map is clear, define species-local terminology.

The best terms are not one-to-one translations of chapter 12.

They should instead reflect:

- the species' cosmology
- its institutions
- its sensory world
- its ritual logic
- its fear

Good taxonomy usually gives one term for each category that matters:

- local equivalent of `vestigios`
- local equivalent of `vínculos`
- local equivalent of `primordiales`
- local equivalent of `aflicciones`

But only create terms that the species would actually need.

Valid outcomes include:

- a full four-part local taxonomy
- only one or two named categories
- one totalizing category that absorbs several chapter-12 phenomena
- one practical split that matters only inside the species' own institutions
- explicit decision that this species does not maintain stable cosmological vocabulary of its own
- explicit decision that this species collapses `vestigios` and `vínculos` into one
  practical category because its members do not experience the distinction as
  culturally important

Check for internal coherence:

- the terms should feel like one system
- the terms should reinforce each other semantically
- the terms should sound like they come from the same civilization

Example pattern:

- object that preserves a mark
- object/chamber that responds
- presence behind the response
- mark left on the reader

Counter-example pattern:

- inventing a term for `aflicciones` when the civilization would treat them as
  part of blessing, revelation, contamination, or exposure rather than as a
  separate category
- inventing a `primordiales` term when the species only really knows one god,
  one sky, one current, one verdict, or one devouring principle
- forcing a vestigio/vínculo split when the species would only notice the
  difference through cost of use, long-term consequence, or community role
- forcing a species to distinguish `vestigio` and `vínculo` when:
  - the objects are too rare for stable comparative use
  - the civilization mostly inherits such objects from outsiders
  - the species uses them ritually rather than operationally
  - the only perceptible difference is “this one leaves me seeing more” versus
    “this one leaves me spent”

Practical rule:

- if the species has not plausibly gone through repeated discovery, transfer,
  comparison of users, and institutional memory around objects, prefer a single
  umbrella term
- if the species has, ask whether its distinction would be about:
  - perceptual burden
  - psychic exhaustion
  - ritual danger
  - civic role
  - destination of the object
  rather than chapter-12 ontology itself

Language note:

- Prefer clear in-world Spanish by default
- Use real-world inherited terms only when they add meaningful cultural texture,
  remain understandable from context, and do not make the species harder to read
- If a borrowed term is less clear than a strong Spanish equivalent, prefer the
  Spanish equivalent

### Phase 4 — Rewrite the cosmology block

Rewrite `## Teología y Cosmología` first.

Keep:

- the species' identity
- civilizational anxiety
- ritual practice
- ambiguity
- doctrine and disagreement

Remove:

- objective explanatory voice
- chapter-12 system terms used as if the species understands them scientifically
- over-precise metaphysical certainty

The cosmology section should read like:

- theology
- ritual logic
- doctrine
- observed pattern
- inherited fear

It should not read like:

- system documentation
- cosmology lecture
- narrator explanation

### Phase 5 — Integrate terminology where natural

Once the cosmology section is stable, seed the new species-local terms in the rest of the entry only where they are naturally supported.

Typical insertion points:

- `La Cultura`
  for archives, relics, institutions, ritual access, sacred objects

- `Teología y Cosmología`
  for doctrinal framing and category definitions

- `Vida Cotidiana`
  for how ordinary people fear or recognize the phenomenon

- `Como Personaje Jugador`
  for what a player character knows from upbringing

Do not force every new term into every section.

### Phase 6 — Discovery sanity check

Before finalizing the rewrite, verify that the species-local cosmology is
compatible with chapter-12 discovery.

Check all of the following:

- does the rewrite accidentally imply that objects are commonly usable without
  discovery?
- does it forget that first meaningful contact creates an Aflicción route?
- does it assume people know what objects do without clue-reading, teaching, or
  transfer?
- does it make a species sound certain about object categories that, in practice,
  would only be known after repeated lived comparison?
- does it confuse the cost of `Aflicción` growth with the cost of `Eco` /
  exhaustion?

If any answer is yes, revise again before closing the species.

A good rule:

- one strong introduction
- one or two reinforcing mentions elsewhere

is usually enough.

### Phase 6 — Residual cleanup outside cosmology

After the cosmology rewrite, audit the rest of the entry for leftover chapter-12 leakage.

Typical places that still need cleanup:

- opening hook
- body section
- culture section
- cross-species relations
- player-character section
- final “what they know” lines

Keep the species-local terms, but make sure surrounding phrasing still sounds species-native.

### Phase 7 — Verification

Before closing, verify all of the following:

1. The species no longer sounds like it has read chapter 12
2. The species still clearly encounters real chapter-12 phenomena where appropriate
3. The species-local terms form a coherent internal system
4. No concept was added “just to have all four”
5. The prose still reads naturally and not like a glossary insertion

Use targeted search for residual leakage terms if helpful, such as:

- `flujo`
- `canal`
- `permeable`
- `entidad`
- `manifestación`
- `sistema nervioso`
- `cruce`

Only keep them if they truly belong to species-local language.

---

## What a good result looks like

A strong localization pass should leave the species with:

- its own metaphysical vocabulary
- its own uncertainty
- its own institutional response
- its own way of being wrong

The reader should be able to infer:

- what chapter-12 phenomenon this species is probably dealing with
- without the species ever needing to explain it in chapter-12 terms

The reader should also be able to infer when:

- the species is collapsing multiple real phenomena into one doctrine
- the species is using institutional or ritual categories instead of metaphysical ones
- the species' error is part of what makes the cosmology feel alive

---

## Quality rules

- Do not flatten a species into a disguised chapter-12 glossary
- Do not invent taxonomy for categories the species would not care about
- Do not erase real setting phenomena just because the species misunderstands them
- Prefer observed effect over metaphysical explanation
- Prefer doctrine over system language
- Prefer category systems that arise from the species' material life
- When in doubt, make the species more local, not more correct

---

## Best-fit case

This workflow is the best fit for species like `Naghii`, where:

- the civilization is deeply metaphysical
- it clearly encounters real chapter-12 phenomena
- but it should interpret them through archive, ritual, and sky rather than through objective cosmological truth

Use that same discipline for any future species:

- identify what they actually encounter
- name only what matters to them
- keep chapter 12 true
- keep chapter 06 local
