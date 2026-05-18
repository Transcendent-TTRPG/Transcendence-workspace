# Core Sync Workflow

This document defines the canonical workflow for synchronizing rules and
content changes from design authority into the corebook publication layer.

Its job is not to make every design change immediately rewrite publication. Its
job is to determine:
- whether a change actually requires publication sync
- what kind of publication sync is required
- which language files must move together
- how to avoid redundancy and terminology drift

## Purpose

Use this workflow when:
- a system rule changes in authority
- a Technique or family of Techniques changes in a way the corebook reflects
- a terminology decision affects publication wording
- a design clarification makes the current corebook misleading
- publication and authority appear to have diverged

## Relationship to authority

Authority remains in:
- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`

The corebook is a publication artifact. It explains, teaches, and presents the
rules, but it does not own them.

Therefore the publication layer must not drift into becoming a second rules
authority.

When a discrepancy appears:
1. verify authority first
2. decide whether the discrepancy is:
   - editorial only
   - terminology only
   - explanatory only
   - mechanically misleading
3. sync the publication layer accordingly

## Required layers

Every core-sync pass should rely on:
- the `Knowledge Layer`
- the relevant design authority
- current publication files
- explicit editorial and dependency review

## Core lenses

### `continuity_lens`
Checks:
- whether the publication still matches the current authority
- whether previous sync decisions are still valid
- whether terminology remains stable across ES and EN

### `dependency_lens`
Checks:
- what sections of the corebook depend on the changed rule
- whether the change affects actions, ATB, ailments, concealment, wounds, or other linked chapters
- whether more than one file must move together

### `editorial_lens`
Checks:
- clarity
- readability
- redundancy
- instructional quality
- whether explanation can remain high-level instead of duplicating full authority text

### `system_lens`
Checks:
- whether the publication wording still describes the mechanic honestly
- whether a “small wording issue” is actually hiding a mechanical mismatch

### `translation_lens`
Checks:
- parity between ES and EN
- whether one language was updated but the other was not
- whether key terms are still mapped consistently

## Sync outcome classifications

Every pass should classify the publication need explicitly:

- `no_sync_needed`
- `editorial_cleanup`
- `terminology_sync`
- `localized_section_update`
- `multi_section_mechanical_sync`
- `authority_blocked`

### Meanings

#### `no_sync_needed`
The authority changed in a way that does not affect the corebook’s current
claims or teaching value.

#### `editorial_cleanup`
The mechanic is still accurate, but wording, structure, or readability should
improve.

#### `terminology_sync`
The main issue is vocabulary consistency, cross-language parity, or naming.

#### `localized_section_update`
One bounded section needs direct content changes.

#### `multi_section_mechanical_sync`
The change touches multiple linked sections and must be treated as a coordinated
publication pass.

#### `authority_blocked`
Authority is not yet stable enough to sync cleanly. Publication should wait.

## Phase order

## Phase 0. Intake

Inputs:
- authority change or suspected divergence
- target publication surface
- language scope
- purpose of the sync

Outputs:
- sync work card
- suspected impact area
- source files to inspect

## Phase 1. Authority Confirmation

Primary lenses:
- `system_lens`
- `continuity_lens`

Questions:
- What is the current authority claim?
- Did the underlying rule actually change?
- Is the publication wrong, incomplete, redundant, or just stylistically weak?

Outputs:
- authority baseline
- publication mismatch summary
- initial sync outcome classification

## Phase 2. Publication Surface Mapping

Primary lenses:
- `dependency_lens`
- `translation_lens`

Questions:
- Which publication files talk about this rule?
- Which chapters inherit or reference the same concept?
- Does the issue affect both ES and EN?
- Is the mismatch local or distributed?

Outputs:
- file map
- language map
- linked-section map

Examples of likely linked surfaces:
- actions
- conflict and combat
- wounds and damage
- concealment
- environmental conditions
- technique chapters

## Phase 3. Sync Decision

Primary lenses:
- `editorial_lens`
- `system_lens`

Questions:
- Does the corebook need direct rule wording changes?
- Can the issue be solved by trimming duplication and pointing back to inherited doctrine?
- Is the publication over-explaining a rule that should stay in authority?
- Is the publication under-explaining a player-facing concept that needs clearer teaching?

Outputs:
- final sync outcome classification
- scope decision:
  - no update
  - one-file update
  - paired ES/EN update
  - multi-section update
  - blocked pending authority

## Phase 4. Editorial Strategy

Primary lens:
- `editorial_lens`

Questions:
- What is the simplest correct explanation?
- What should be summarized instead of restated fully?
- What should inherit doctrine from another chapter instead of repeating it?
- What terms need to stay identical across chapters?

Outputs:
- editorial plan
- terminology plan
- duplication-reduction plan

## Phase 5. Language Strategy

Primary lens:
- `translation_lens`

Questions:
- Are both languages being updated now?
- If not, is that delay acceptable or does it create drift?
- What term pairs must stay locked?

Outputs:
- ES/EN sync plan
- explicit note if one language is intentionally deferred

Default expectation:
- if a mechanical explanation changes, both ES and EN should move together unless a deliberate temporary exception is recorded

## Phase 6. Integration

Execute the actual publication updates.

Typical tasks:
- update ES file
- update EN file
- update chapter README notes if relevant
- update migration or project-admin notes if the change is structural

Also update:
- workflow or knowledge records if terminology or sync doctrine changed

## Phase 7. Validation

Validation may include:
- authority comparison
- terminology consistency pass
- ES/EN parity pass
- chapter-local readability pass
- linked-section consistency pass

Outputs:
- validated sync
- explicit unresolved issues if not fully closed

## Phase 8. Acceptance Closure

Suggested closure checklist:
- `authority_confirmed`
- `publication_scope_mapped`
- `sync_classified`
- `es_updated` or `not_needed`
- `en_updated` or `not_needed`
- `linked_sections_checked`
- `terminology_checked`
- `pending_items_explicit`

## Phase 9. Change Impact Record

Every core-sync pass should record:
- authority source touched
- publication files changed
- terminology decisions introduced or reinforced
- whether the change was editorial, mechanical, or both
- whether any language or chapter remains pending

## Good outputs

A good core-sync pass leaves behind:
- publication that teaches the right rule
- no hidden ES/EN drift
- less duplication where possible
- clearer linkage between authority and publication

## Bad outputs

A bad core-sync pass leaves behind:
- publication wording that silently contradicts authority
- one language updated and the other forgotten
- full rule duplication where a concise inherited explanation would be better
- publication text inventing mechanics that authority never stabilized

## Relationship to other workflows

This workflow complements:
- [Technique Workflow](./technique-workflow.md)
- [Simulation Port Workflow](./simulation-port-workflow.md)

The technique workflow governs the full artifact lifecycle.
The simulation-port workflow governs simulator coverage.
This core-sync workflow governs the publication branch and its relationship to
authority. 
