---
name: "poison-authoring"
description: "Use when authoring, revising, normalizing, or auditing poison entries or poison-family doctrine. Follow the status-family workflow and poison-specific closure rules instead of treating poisons like isolated status entries."
---

# Poison Authoring

Use this skill when the work is specifically about poisons as a family or about one poison entry that must stay consistent with poison-family doctrine.

This skill inherits the family-oriented mindset of `status-family-authoring`, but narrows it to poison logic: delivery method, onset, dose, persistence, countermeasures, cleansing, and resistance surfaces.

## When to use this skill

Use `$poison-authoring` when the task is to:

- create one or more poisons
- revise poison-family doctrine
- normalize legacy poisons to a shared structure
- define poison vectors, dose logic, or countermeasure logic
- review whether poison entries actually inherit the same grammar
- prepare poisons for simulation or publication routing

Do not use this skill as the primary owner when:

- the work is really broader status-family foundation work
- the work is about infections, elixirs, or trap packages rather than poisons
- the task is a general authority rewrite not scoped to poisons
- the task is only simulator porting after authority is already stable

In those cases, route first through:

- `status-family-workflow`
- `authority-revision-workflow`
- `simulation-port-workflow`

## Required workflow discipline

Every poison run must stay grounded in the family workflow layer and poison-specific closure criteria.

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

Treat each poison run as a run with a named poison scope, explicit family inheritance, and a clear toxic life cycle from delivery to neutralization.

### 1. Define poison boundary and delivery method

Before writing details, decide:

- what counts as a poison in this family
- what delivery methods apply
- what does not count as poison

Do not start by naming symptoms if the delivery model and family boundary are still fuzzy.

### 2. Establish poison grammar before entry prose

Each poison or poison family should make explicit:

- delivery / application model
- family or type
- dose or exposure logic
- onset timing
- severity logic
- persistence or decay
- resistance / recovery surfaces
- antidote, treatment, or cleansing logic
- release or neutralization conditions

Do not let one-off flavor text hide these fields.

### 3. Separate poison doctrine from its downstream effects

Keep clear the difference between:

- what defines the poison itself
- what the poison delivers or triggers
- what counts as escalation or stacking
- what treatment can actually change

If a downstream state belongs to a broader ailment or another subsystem, say so explicitly instead of stuffing every consequence into the poison entry.

### 4. Route cross-workflow issues correctly

Examples:

- if antidote or cleansing logic depends on unclear medical doctrine, route to `authority-revision-workflow`
- if poison stacking or decay depends on unresolved subsystem coupling, route through `dependency-review-workflow`
- if poison pressure or onset seems miscosted or too oppressive, route through `balance-review-workflow`
- if poison support must be simulated, route to `simulation-port-workflow`
- if poison explanation must appear in publication, route to `core-sync-workflow`

### 5. Close with toxic life-cycle clarity, not just evocative wording

A poison run is not complete because the fiction sounds sharp.

Close only when you can state:

- poison boundary
- delivery model
- dose / onset / persistence logic
- antidote / cleansing logic
- neutralization or release logic
- inheritance vs entry overrides

## What to produce in a good poison run

A strong poison run should leave behind:

- poison-family boundary
- explicit delivery and onset model
- consistent antidote and cleansing logic
- inheritance clarity across entries
- downstream simulator/publication implications

At minimum, capture:

- poison scope
- delivery or exposure model
- poison family or taxonomy
- dose logic
- onset timing
- severity structure
- persistence / decay logic
- resistance or recovery surface
- antidote / cleansing surface
- neutralization conditions
- simulator implications
- publication implications
- pending exceptions
- change impact

## Quality rules

- Do not reduce poisons to flavor plus damage or a penalty.
- Keep delivery, onset, persistence, and antidote logic explicit.
- Do not confuse a poison with all the states it may trigger downstream.
- Prefer shared poison grammar over bespoke one-off formatting.
- If antidote or cleansing logic is not clear, do not pretend the entry is closed.
- Be careful with onset and persistence; poisons can create very sharp tempo swings.
- Keep simulator implications explicit, especially for dose, decay, and treatment hooks.

## Suggested poison sequence

In many runs, this order works well:

1. read family workflow docs and current poison authority
2. define poison boundary and delivery model
3. define shared poison grammar
4. author or normalize entries
5. assess antidote, persistence, and neutralization logic
6. assess simulator and publication implications
7. close with poison-family status and pending exceptions

## Reference map

Use these local references first:

- `references/poison-map.md`
- `references/poison-checks.md`

Then open the actual project documents named there.
