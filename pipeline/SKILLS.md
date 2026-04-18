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
4. The target file
5. 2–5 related files (use `pipeline/scripts/index.py --search` to find them)

### Constraints

- Match the rhythm and vocabulary documented in `style-guide.md`
- Use only terminology from `glossary.md` for system concepts
- Avoid every pattern listed in `style-guide.md §AI-patterns-to-avoid`
- Do not introduce new canonical terms without first checking `glossary.md`
- Prose must be in the correct language (ES / EN) — do not mix
- Each narrative paragraph must be anchored in one primary sensory channel — do not distribute attention across unrelated inputs
- Every narrative paragraph must present a perceivable anomaly; do not describe causes or explanations
- Narrative and rules text must be separated explicitly — rules first, then example or flavor text; do not blend them
- When writing rules text, introduce mechanical concepts by contrast ("not X, but Y") followed by a consequence chain; close with a short declarative statement of the trade-off

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
