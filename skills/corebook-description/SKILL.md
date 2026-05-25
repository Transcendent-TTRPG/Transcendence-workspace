---
name: "corebook-description"
description: "Use when writing or revising description-mode content in the corebook — species, creatures, equipment, world/faction passages, cosmic horror ambiance, or any prose that presents observable state without defining mechanics or narrating events. Loads voice, canon context, and description-mode rules."
---

# Corebook Description

Use this skill when the task is to write or revise **description-mode** content in corebook publication files.

Description presents observable state. It answers: what does this thing, place, or being look, sound, feel, or behave like? It does not explain how it works mechanically — that is `rules` mode (`corebook-prose`). It does not unfold events — that is `narrative` mode (`fiction-guide`).

## What this skill covers

| Content type | What description does there |
| --- | --- |
| Species entries | Presents what you perceive when you encounter one — not taxonomy |
| Creature / adversary entries | Presents observable presence, behavior, and threat — not stat-block in prose |
| Equipment entries | Presents physical properties and what handling it registers — not how the mechanic works |
| World / faction passages | Presents the lived experience of presence in that context — not history or politics as exposition |
| Cosmic horror / Limbo passages | Presents perceivable consequence first, causality partially obscured |
| Chapter or section openers | Orients the reader to what kind of space they are entering — physical, not atmospheric in the abstract |

## Authoring stance

Description in Transcendence is **precise, constrained, and perceptual**.

The world is not explained. It is presented through what can be observed.

- What you see, hear, smell, or feel when you are in the presence of something — that belongs here.
- Why it is that way, what caused it, what it means cosmologically — that does not belong here unless the viewpoint can genuinely perceive it.
- What it does mechanically — that belongs in `rules` text, separated from description.

The darkness in this world earns its weight through specific physical detail, not through declaring that something is unsettling. A place is not "eerie" — the sound arrives a beat late, and the ground gives a fraction more than it should. That is description.

## When to use this skill

Use `$corebook-description` when the task is to:

- write or revise a description passage for a species, creature, or adversary entry
- write or revise a world or faction introduction
- write or revise equipment or item descriptions
- write or revise setting or environment passages in the corebook
- write or revise cosmic horror ambiance text where perceivable consequence leads
- do a voice pass on existing description that sounds clinical, abstract, or like a glossary entry

Do not use this skill when the task is primarily:

- defining how a mechanic works (use `corebook-prose`, mode: rules)
- writing or revising flavor lines in ailment/condition/technique entries (use `corebook-prose`)
- syncing authority changes to publication (use `corebook-sync`)
- writing fiction, light novel scenes, or narrative inserts (use `fiction-guide`)

## Required context

**Always load:**
- `Transcendence-publications/canon/text-modes.md` — description mode rules (what it can and cannot contain)
- `Transcendence-publications/canon/style-guide.md` — vocabulary rules, anti-patterns, sentence structure
- `Transcendence-publications/canon/voice-samples.md` — approved rhythm reference; use "scene or narrative" samples as adjacent calibration for description cadence
- `Transcendence-publications/canon/glossary.md` — canonical term list; all system terms must match exactly

**Load when relevant:**
- `Transcendence-publications/canon/world-facts.md` — when the passage touches species, factions, geography, theology, or world history; required for any passage that makes a factual claim about the setting
- `Transcendence-publications/canon/fiction-guide.md` — when description appears inside a scene or narrative passage and must serve the scene's pressure
- the target file itself
- the bilingual pair file (if the task touches one language, always check the other)

## Execution pattern

### 1. Confirm the mode is description

Before drafting, confirm the passage is presenting observable state — not defining a mechanic, not narrating events.

If a passage is doing two things at once, split it. Rules text and description text must be in separate paragraphs. Description inside a scene must serve the scene's pressure (see `fiction-guide`).

### 2. Identify the primary sensory channel

Each description passage should anchor to **one primary sensory channel**:
- visual: form, light, surface, proportion
- auditory: sound, rhythm, delay, absence
- tactile: weight, texture, resistance, temperature
- olfactory: presence, absence, contamination
- spatial/kinesthetic: distance, movement, pressure, orientation

A second sensory detail is allowed only if it reinforces the same phenomenon.

Do not distribute attention across unrelated sensory inputs in one paragraph.

### 3. Identify the contrast

Good description in this setting usually presents a contrast between **expected behavior and actual behavior**:
- the expected: what the reader assumes this thing or place would be like
- the actual: what is observably different

That contrast is where the specificity of the world lives. A creature that moves the way a creature should is not described — one that does not move the way it should is.

This does not mean every passage must contain an anomaly. Ordinary creatures, ordinary equipment, ordinary places have their own specificity. But that specificity comes from concrete physical detail, not from declaring that something is "dangerous" or "mysterious".

### 4. Draft within the mode

**Shape rules:**
- Short to medium declarative sentences
- Present tense for stable observable state; past tense only when describing a trace or residue
- One phenomenon per sentence
- One sensory cluster per paragraph
- Close on what the presence of this thing does to the perceiving body — not what it means

**Voice rules:**
- Physical language over abstract descriptors: "the weight shifts forward" not "it feels unbalanced"
- Prefer verbs over adjectives: "the surface pulls" not "the surface is adhesive"
- No mood adjectives without physical grounding: not "unsettling" or "eerie" — find the physical fact that produces the feeling
- No hidden causes explained: the observer can perceive consequence, not causality
- No generic dark fantasy language: "darkness", "shadows", "ancient evil" as standalone descriptors are not allowed; earn them with specific physical detail
- No interiority unless the passage is explicitly viewpoint-bound

### 5. Content-type specific rules

**Species and creatures:**
- Open with the most immediately observable physical fact — size, movement pattern, texture, sound
- Do not open with taxonomy, etymology, or in-world classification
- Behavior is described through what can be observed, not inferred inner state
- Threat is presented through physical capability and behavior, not through declaring dangerousness
- The extranatural or anomalous should be presented as physical consequence, not explained as cause

**Equipment and items:**
- Weight, grip, surface, and what handling it registers in the body are primary
- What the item does mechanically is rules text — separate it
- If the item has a history or origin, present it through physical traces (wear, markings, material) not through narrative explanation

**World and faction passages:**
- Present the lived experience of being in that context: what a body in that place registers
- Social or political facts are presented through observable behavior and physical evidence, not through exposition
- Do not write history. Write presence — what is observable now that is shaped by what happened before.

**Cosmic horror and Limbo:**
- Perceivable consequence always leads; causality is partially or fully obscured
- Physical anomaly is the vehicle: things that do not behave as the body expects
- Do not name or explain the source of the anomaly unless the viewpoint has genuine reason to understand it
- Subtle is valid — not every Limbo passage needs full contradiction of physical law
- The absence of something expected is as valid as the presence of something wrong

### 6. Check the bilingual pair

After writing or revising one language, check that the other carries equivalent content and physical anchoring. ES and EN may differ in phrasing but must not differ in what they present or in their sensory register.

If one language is pending, mark it explicitly: `ES: pendiente` or `EN: pending`.

## Quality rules

- Do not blend description and rules in the same paragraph.
- Do not blend description and narrative in the same paragraph unless the passage is inside a scene and the fiction-guide governs it.
- Do not use "mysterious", "ancient", "unsettling", "eerie", or equivalent mood adjectives as standalone descriptors — always follow them with the physical fact that earns them, or remove them.
- Do not open a description with classification: "The X is a type of Y that..." — open with what you perceive.
- Do not explain causes. Present consequences.
- Do not write interiority for non-viewpoint creatures: not "the creature senses danger" but "it stops, turns, and does not move again for several seconds."
- All canonical terms must match `glossary.md` exactly.
- Do not write a description that could apply to any creature, place, or item in the genre — specificity is the test.
- If a passage sounds like a zoology textbook, a museum placard, or a sourcebook summary, it has failed. Rewrite from the sensory anchor.

## Rhythm reference

The approved "scene or narrative" samples in `canon/voice-samples.md` are the closest calibration for description cadence. They share the same physical anchoring, the same one-phenomenon-per-sentence discipline, and the same preference for specific anomaly over generic atmosphere.

Use them as rhythm templates, not content templates. Match sentence length pattern and sensory focus — not phrasing.

## Reference map

Load these first:

- `Transcendence-publications/canon/text-modes.md`
- `Transcendence-publications/canon/style-guide.md`
- `Transcendence-publications/canon/voice-samples.md`
- `Transcendence-publications/canon/world-facts.md`
- `Transcendence-publications/canon/glossary.md`

Then load the target file and its bilingual pair.
