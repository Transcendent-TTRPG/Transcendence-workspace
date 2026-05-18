---
name: "status-family-authoring"
description: "Use when authoring, revising, normalizing, or auditing a repeated status family such as infections, poisons, elixirs, trap packages, or similar grouped entries. Follow the status-family workflow instead of treating each entry as an isolated artifact."
---

# Status Family Authoring

Use this skill when the work is about a repeated family of related entries that should share grammar, taxonomy, doctrine, and simulator surfaces.

This skill is not for a single Technique-sized artifact unless that artifact is only one member of a broader family that must be authored coherently.

## When to use this skill

Use `$status-family-authoring` when the task is to:

- design or revise a whole family of infections
- design or revise a whole family of poisons
- design or revise a whole family of elixirs
- design or revise trap packages or another repeated applied-status family
- normalize a family so entries inherit shared doctrine instead of repeating it
- define grammar, tiers, resolution model, and closure rules for a family
- review whether a family is coherent across authority, simulation, and publication

Do not use this skill as the primary owner when:

- the task is one isolated Technique
- the task is one isolated simulator port
- the task is a pure species audit
- the task is a purely upstream rule rewrite with no active family scope

In those cases, route first through:

- `technique-workflow`
- `simulation-port-workflow`
- `species-audit-workflow`
- `authority-revision-workflow`

## Required workflow discipline

Every family run must be grounded in the family workflow layer.

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

Treat each family run as a run with an owner workflow, a named family, and explicit shared doctrine plus entry-level consequences.

### 1. Define the family boundary

Before authoring entries, decide what belongs to the family and what does not.

Examples:

- which entries count as infections
- which entries count as poisons
- whether a trap package is one family or multiple subfamilies
- whether a mixed set really shares one grammar

Do not start by drafting entries if the family boundary is still fuzzy.

### 2. Establish shared grammar before individual entries

The family should define:

- taxonomy
- application model
- roll surfaces
- severity structure
- duration / expiry logic
- cleansing / treatment / release logic
- inheritance vs per-entry override rules

Only after that should individual entries be authored or normalized.

### 3. Separate family doctrine from entry payload

Do not duplicate family-level rules inside every entry unless the workflow has established that the redundancy is necessary.

Keep explicit the difference between:

- what all entries inherit
- what some subclasses inherit
- what one entry overrides

### 4. Route cross-workflow issues correctly

Examples:

- if the family exposes unclear upstream doctrine, route to `authority-revision-workflow`
- if the family depends on unresolved subsystem coupling, route through `dependency-review-workflow`
- if the family needs simulator normalization, route to `simulation-port-workflow`
- if the family affects published explanation, route to `core-sync-workflow`
- if the work narrows down to one Technique only, route to `technique-workflow`

### 5. Close the family with structure, not only entries

A family run is not complete because some entries were added.

Close only when you can state:

- family boundary
- shared grammar
- inheritance model
- entry inventory
- unresolved exceptions
- simulator/publication implications

## What to produce in a good family run

A strong family run should leave behind:

- explicit family boundary
- shared doctrinal grammar
- normalized entry structure
- clear inheritance rules
- classification of exceptions
- downstream simulator/publication implications

At minimum, capture:

- family scope
- taxonomy
- shared application and resolution model
- duration / expiry model
- recovery or treatment model
- inheritance rules
- per-entry override rules
- balance risks or tiering concerns
- simulator implications
- publication implications
- pending exceptions
- change impact

## Quality rules

- Do not treat a family as only a list of entries.
- Prefer shared grammar over repeated prose.
- Keep family-level doctrine and per-entry payloads clearly separated.
- If the family depends on another subsystem that is still unstable, say so explicitly.
- Do not call the family "normalized" if its entries still rely on inconsistent structures or naming.
- Keep simulator implications explicit; families tend to hide repeated runtime work.
- Be careful with exceptions: too many exceptions usually mean the family boundary is wrong.

## Suggested family sequence

In many runs, this order works well:

1. read family workflow docs and current authority
2. define family scope and taxonomy
3. define shared grammar and inheritance model
4. normalize or author individual entries
5. assess simulator and publication implications
6. classify blockers and exceptions
7. close with explicit family status and next steps

## Reference map

Use these local references first:

- `references/family-map.md`
- `references/family-checks.md`

Then open the actual project documents named there.
