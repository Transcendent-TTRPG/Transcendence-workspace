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
