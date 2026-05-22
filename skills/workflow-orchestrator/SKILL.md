---
name: "workflow-orchestrator"
description: "Use when a task must be routed through the project workflow system with explicit ownership, work-card instantiation, checkpointing, routing, and closure. This skill chooses and enforces the workflow path instead of letting artifact work begin ad hoc."
---

# Workflow Orchestrator

Use this skill when the main need is not yet "edit the artifact," but "run the right project workflow correctly."

This skill is the execution layer made operational. It does not replace artifact skills such as `technique-authoring` or `corebook-sync`. Instead, it decides which workflow owns the task, which work card structure applies, which linked workflows may be needed, and what must be true before the run can close.

## When to use this skill

Use `$workflow-orchestrator` when the user asks for work like:

- create a new Technique and do it through the full process
- revise an existing artifact but ensure the right workflow is followed
- run a species pass or audit with explicit closure
- backfill older content without skipping sim or publication implications
- determine which workflow really owns a messy cross-cutting task
- start a run that may need multiple linked workflows

This skill is especially useful when:

- ownership is unclear
- the task spans design, simulation, and publication
- the user wants discipline more than speed
- a previous run suffered from ambiguity, repetition, or missing closure

Do not use this skill when:

- workflow ownership is already obvious and the artifact skill alone is enough
- the task is tiny and already fully scoped
- the work is a trivial wording change with no workflow consequences

## Required workflow docs

Always start with:

- `docs/workflows/workflow-execution.md`
- `docs/workflow-overview.md`

Then open only the workflow docs required by the chosen owner:

- `docs/workflows/technique-workflow.md`
- `docs/workflows/simulation-port-workflow.md`
- `docs/workflows/core-sync-workflow.md`
- `docs/workflows/species-audit-workflow.md`
- `docs/workflows/status-family-workflow.md`
- `docs/workflows/authority-revision-workflow.md`
- `docs/workflows/dependency-review-workflow.md`
- `docs/workflows/balance-review-workflow.md`
- `docs/workflows/batch-refactor-workflow.md`

Use the work card templates in:

- `docs/workcards/`

Use the skill index in:

- `skills/README.md`

## Core responsibilities

This skill owns five things:

1. workflow ownership
2. work-card selection or instantiation
3. checkpoint discipline
4. routing between workflows and artifact skills
5. closure discipline

If one of these is missing, the run is not truly orchestrated.

## Execution pattern

### 1. Classify the task before touching files

Ask:

- what is the actual unit of work?
- what artifact or system is being changed?
- is this local or cross-cutting?
- is the owner obvious or ambiguous?

Then classify the task into one of the current owner workflows:

- `technique-workflow`
- `simulation-port-workflow`
- `core-sync-workflow`
- `species-audit-workflow`
- `status-family-workflow`
- `authority-revision-workflow`
- `dependency-review-workflow`
- `balance-review-workflow`
- `batch-refactor-workflow`

If no owner is yet clear, use the skill to resolve ownership first. Do not let artifact editing begin before that.

### 2. Select the owner workflow

Choose exactly one owner.

If several workflows are relevant:

- choose one owner
- record the others as linked workflows
- define the handoff or routing points

The owner workflow controls closure. Linked workflows inform, constrain, or extend the run, but do not replace ownership.

### 3. Select the work card

Use the appropriate work card template when one exists:

- `docs/workcards/technique-workcard-template.md`
- `docs/workcards/simulation-port-workcard-template.md`
- `docs/workcards/species-audit-workcard-template.md`

If there is no template for the owner workflow yet:

- use the closest existing template as a strict temporary scaffold
- explicitly note the mismatch
- avoid pretending the template problem does not exist

### 4. Select the artifact skill

Only after ownership is clear should the run select the artifact skill.

Common mappings:

- `technique-workflow` -> `technique-authoring`
- `simulation-port-workflow` -> `technique-porting-to-sim`
- `core-sync-workflow` -> `corebook-sync`
- `species-audit-workflow` -> `species-pass-audit`
- `status-family-workflow` -> `status-family-authoring`
- infection family under status-family ownership -> `infection-authoring`
- poison family under status-family ownership -> `poison-authoring`

If no current artifact skill cleanly fits:

- stay under workflow orchestration
- record the missing skill or missing specialization
- continue using the workflow docs directly

When the owner is `technique-workflow`, do not let orchestration begin from
"what current mechanics already support." The orchestrated run should preserve
the technique fantasy first, then let dependency and simulation framing decide
whether the system already supports it, needs bounded reusable expansion, or
must stop with an explicit gap classification.

### 5. Advance by checkpoints

The orchestrator should not let the run skip from:

- "I understand the task"
- directly to
- "I edited files"

Before substantial edits, ensure the owner workflow has produced its early checkpoints.

Examples:

- scope and source inventory
- species framing
- dependency map
- balance framing
- runtime-gap classification
- runtime gate result
- publication section mapping
- audit inventory

If a checkpoint is missing, either produce it or explicitly record why the run is intentionally narrow.

When a run includes simulation coverage, do not allow the work to be spoken of
as fully integrated unless the runtime gate is explicit:

- `runtime_supported`
- `runtime_partial`
- or `runtime_blocked`

If the run stops before `runtime_supported`, any balance conclusion should be
recorded as provisional rather than final.

And even after `runtime_supported`, do not let the run speak as if the
Technique were fully validated unless it also has:

- a saved minimum cost question for `Rhythm` / `Attrition`
- and any obviously necessary derived question for its main secondary surface

### 6. Route when boundaries are crossed

If the current run discovers that another workflow owns the hard part:

- record the blocker or dependency
- stop pretending the current workflow can solve it locally
- route to the correct owner

Examples:

- a Technique run exposes unstable upstream doctrine -> route to `authority-revision-workflow`
- a sim port is blocked by unresolved treatment logic -> route to `dependency-review-workflow` or `authority-revision-workflow`
- a local cleanup grows into a large migration -> route to `batch-refactor-workflow`
- a species audit reveals one concrete Technique rewrite -> route to `technique-workflow`

### 7. Enforce explicit closure

A run closes only when the owner workflow's acceptance logic is satisfied.

The orchestrator should require explicit statements for:

- owner workflow
- linked workflows
- acceptance status
- unresolved items
- downstream follow-up if needed
- change impact

Do not allow soft closure language like:

- "mostly done"
- "good enough for now"
- "we can remember the rest later"

unless the pending items are named and closure is deliberately partial.

## Quality rules

- Do not let artifact skills become an alternate informal process.
- Do not choose a workflow owner after files have already been edited unless you are repairing a bad run explicitly.
- Prefer one owner plus linked workflows over "everything owns this."
- Keep the active workflow set small and legible.
- If a work card template is missing, say so explicitly rather than silently improvising.
- Use the skill index before inventing a new skill path.
- If the run reveals a structural gap in the workflow system, record it as a system gap, not a user-memory task.

## Suggested orchestration sequence

In many runs, this order works well:

1. classify the task
2. choose the owner workflow
3. identify linked workflows
4. select the work card template
5. select the artifact skill
6. execute checkpoints in order
7. route when needed
8. enforce closure

## Reference map

Use these local references first:

- `references/owner-map.md`
- `references/closure-gates.md`

Then open the actual project workflow and skill docs named there.
