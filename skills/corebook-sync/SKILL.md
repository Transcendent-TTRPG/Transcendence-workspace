---
name: "corebook-sync"
description: "Use when authority-side system changes must be synchronized into corebook publication files, section mappings, ES/EN copies, or publication-facing explanatory text. Follow the core-sync workflow instead of editing publication chapters ad hoc."
---

# Corebook Sync

Use this skill when a rules, authority, species, technique, or subsystem change must be synchronized into publication-facing corebook material.

This skill does not own upstream system design. It assumes the authority side is stable enough to sync, or it names the exact reason publication work should pause.

## When to use this skill

Use `$corebook-sync` when the task is to:

- reflect authority changes in corebook chapters
- update ES and EN publication text after system changes
- revise explanatory rules text without creating a second authority
- map authority changes to affected publication sections
- close publication drift after technique, ailment, ATB, or subsystem updates
- determine whether publication sync is required at all

Do not use this skill as the primary owner when:

- the rule itself is still unresolved in authority
- the Technique or subsystem still needs authoring closure first
- the task is simulator coverage rather than publication sync
- the task is a broad editorial rewrite unrelated to authority synchronization

In those cases, route first through:

- `authority-revision-workflow`
- `technique-workflow`
- `simulation-port-workflow`
- another publication workflow if one later owns broader editorial work

## Required workflow discipline

Every publication sync run must be grounded in the project sync workflow layer.

Start with:

- `docs/workflows/workflow-execution.md`
- `docs/workflows/core-sync-workflow.md`

Then open only the workflow docs the run actually needs:

- `docs/workflows/technique-workflow.md`
- `docs/workflows/authority-revision-workflow.md`
- `docs/workflows/dependency-review-workflow.md`
- `docs/workflows/species-audit-workflow.md`

Read authority and publication sources directly:

- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`
- `Transcendence-publications/`

Use the knowledge layer when the sync depends on recent decisions:

- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-design/knowledge_access/`

## Execution pattern

Treat each publication sync as a run with an owner workflow, a source authority change, and explicit publication closure.

### 1. Confirm publication sync is actually required

Before touching publication files, decide whether the authority change has:

- mechanical impact
- explanatory impact
- terminology impact
- section-level impact
- language-level impact

If the answer is no, record `not_needed` instead of editing for the sake of symmetry.

### 2. Identify the source authority and the target publication surface

Map:

- source authority files
- affected corebook sections
- affected language files
- whether the sync is system-facing, example-facing, glossary-facing, or species-facing

Do not start editing prose before the mapping is explicit.

### 3. Preserve authority ownership

Publication text explains the system. It does not redefine it.

During sync:

- inherit authority decisions
- clarify and reorganize when needed
- do not create a second canonical rule payload in corebook prose

If publication needs a change that would alter authority semantics, stop and route upstream instead.

### 4. Sync by section and by language

Do not assume ES and EN drift can be fixed by editing only one side.

For each affected section, decide:

- ES requires update
- EN requires update
- both require update
- one side is intentionally deferred, with reason

### 5. Route when the run crosses boundaries

Examples:

- if the authority is still unstable, route to `authority-revision-workflow`
- if the underlying Technique is not closed, route to `technique-workflow`
- if the change was discovered during a species audit, route or return to `species-audit-workflow`
- if the sync reveals a dependency conflict across chapters, route through `dependency-review-workflow`

### 6. Close with publication status, not just edited paragraphs

A sync run is not complete because a section "reads better."

Close only when you can state:

- source authority used
- affected publication sections
- ES status
- EN status
- whether sync was required
- whether publication now matches authority
- pending drift, if any

## What to produce in a good corebook sync run

A strong sync run should leave behind:

- explicit mapping from authority change to publication surfaces
- publication prose aligned to authority without duplicating ownership
- ES/EN status clarity
- explicit residual drift if any remains
- change impact that future agents can recover

At minimum, capture:

- source authority
- affected publication sections
- impact class
- sync needed or not needed
- ES update status
- EN update status
- terminology changes
- examples or explanatory text touched
- validation of consistency against authority
- pending items
- change impact

## Quality rules

- Do not let publication files become a second source of truth.
- Do not silently update one language and assume the other is implied.
- Prefer clarity and compression over re-copying full authority payloads into the corebook.
- If a sync depends on unresolved doctrine, stop and say so.
- If a section needs only terminology alignment, keep the change narrow.
- If publication currently disagrees with authority, name the conflict explicitly.
- Keep section mapping explicit so future audits can recover what changed and why.

## Suggested sync sequence

In many runs, this order works well:

1. read sync workflow docs and authority source
2. identify affected publication sections and languages
3. classify the sync type
4. update publication text narrowly
5. review terminology and inherited explanations
6. validate against authority
7. record ES/EN status and impact

## Reference map

Use these local references first:

- `references/sync-map.md`
- `references/closure-checks.md`

Then open the actual project documents named there.
