---
name: "infection-authoring"
description: "Use when authoring, revising, normalizing, or auditing infection entries or infection-family doctrine. Follow the status-family workflow and infection-specific closure rules instead of treating infections like isolated status entries."
---

# Infection Authoring

Use this skill when the work is specifically about infections as a family or about one infection entry that must be authored in a way that remains consistent with infection-family doctrine.

This skill inherits the family-oriented mindset of `status-family-authoring`, but narrows it to infection logic: vectors, exposure, progression, treatment, cleansing, persistence, and recovery.

## When to use this skill

Use `$infection-authoring` when the task is to:

- create one or more infections
- revise infection-family doctrine
- normalize legacy infections to a shared structure
- define infection tiers, vectors, treatment hooks, or cleansing logic
- review whether infection entries actually inherit the same grammar
- prepare infections for simulation or publication routing

Do not use this skill as the primary owner when:

- the work is really a broader status-family foundation task
- the work is about poisons, elixirs, or trap packages rather than infections
- the task is a general authority rewrite not scoped to infections
- the task is only simulator porting after authority is already stable

In those cases, route first through:

- `status-family-workflow`
- `authority-revision-workflow`
- `simulation-port-workflow`

## Required workflow discipline

Every infection run must stay grounded in the family workflow layer and infection-specific closure criteria.

Start with:

- `docs/workflows/workflow-execution.md`
- `docs/workflows/status-family-workflow.md`

Then open only the additional workflow docs the run actually needs:

- `docs/workflows/dependency-review-workflow.md`
- `docs/workflows/balance-review-workflow.md`
- `docs/workflows/simulation-port-workflow.md`
- `docs/workflows/core-sync-workflow.md`
- `docs/workflows/authority-revision-workflow.md`

Use the knowledge and simulator layers directly:

- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-design/knowledge_access/`
- `Transcendence-design/sim/`

## Execution pattern

Treat each infection run as a run with a named infection scope, explicit family inheritance, and a defined life cycle from exposure to resolution.

### 1. Define infection boundary and vector

Before writing details, decide:

- what counts as an infection in this family
- what vector or exposure model applies
- what does not count as infection

Do not start by naming symptoms if the underlying vector and boundary are still fuzzy.

### 2. Establish infection grammar before entry prose

Each infection or infection family should make explicit:

- exposure / acquisition model
- family or type
- severity logic
- progression logic
- onset and persistence
- recovery / resistance surfaces
- treatment or cleansing logic
- release conditions

Do not let one-off prose hide these fields.

### 3. Separate infection doctrine from symptoms or manifestations

Keep clear the difference between:

- what defines the infection itself
- what the infection causes
- what counts as progression
- what treatment can actually change

If a symptom belongs to a broader ailment or another subsystem, say so explicitly instead of stuffing everything into the infection entry.

### 4. Route cross-workflow issues correctly

Examples:

- if infection treatment depends on unclear medical doctrine, route to `authority-revision-workflow`
- if infection progression depends on unresolved subsystem coupling, route through `dependency-review-workflow`
- if infection tiers seem miscosted or too oppressive, route through `balance-review-workflow`
- if infection support must be simulated, route to `simulation-port-workflow`
- if infection explanation must appear in publication, route to `core-sync-workflow`

### 5. Close with life-cycle clarity, not just flavorful text

An infection run is not complete because the fiction sounds evocative.

Close only when you can state:

- infection boundary
- exposure model
- severity and progression logic
- treatment / cleansing logic
- release or closure logic
- inheritance vs entry overrides

## What to produce in a good infection run

A strong infection run should leave behind:

- infection-family boundary
- explicit acquisition and progression model
- consistent treatment/recovery logic
- inheritance clarity across entries
- downstream simulator/publication implications

At minimum, capture:

- infection scope
- vector or exposure model
- infection family or taxonomy
- severity structure
- progression logic
- persistence / expiry logic
- resistance or recovery surface
- treatment / cleansing surface
- release conditions
- simulator implications
- publication implications
- pending exceptions
- change impact

## Quality rules

- Do not reduce infections to flavor plus a penalty.
- Keep exposure, progression, and treatment explicit.
- Do not confuse an infection with the symptoms or states it may trigger downstream.
- Prefer shared infection grammar over bespoke one-off formatting.
- If treatment or cleansing logic is not clear, do not pretend the entry is closed.
- Be careful with persistence and escalation; infections often hide strong tempo pressure.
- Keep simulator implications explicit, especially for progression and treatment hooks.

## Suggested infection sequence

In many runs, this order works well:

1. read family workflow docs and current infection authority
2. define infection boundary and exposure model
3. define shared infection grammar
4. author or normalize entries
5. assess treatment, progression, and release logic
6. assess simulator and publication implications
7. close with infection-family status and pending exceptions

## Reference map

Use these local references first:

- `references/infection-map.md`
- `references/infection-checks.md`

Then open the actual project documents named there.
