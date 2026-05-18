---
name: "species-pass-audit"
description: "Use when a species pass must be audited across authority, identity, simulation coverage, runtime blockers, publication drift, or prioritized backlog. Follow the species-audit workflow instead of reviewing species content ad hoc."
---

# Species Pass Audit

Use this skill when the task is to assess the state of a species pass as a whole rather than only author or port a single artifact.

This skill is for cross-cutting review: identity, authored inventory, mechanical spread, simulator coverage, blockers, and backlog. It is not the primary owner for creating a Technique or porting a single Technique unless the audit intentionally routes into those workflows.

## When to use this skill

Use `$species-pass-audit` when the user asks for things like:

- audit a species pass end to end
- count authored vs sim-ready content for a species
- identify weak or redundant Techniques in a species
- assess simulation coverage for a species
- decide what backlog should be prioritized next for a species
- verify whether a species pass is actually "closed"
- review identity drift across a species set

Do not use this skill as the primary owner when:

- the task is to create or revise one specific Technique
- the task is to port one specific Technique to sim
- the task is to rewrite a status family
- the task is to revise an upstream rule rather than the species pass

In those cases, route first through:

- `technique-workflow`
- `simulation-port-workflow`
- `status-family-workflow`
- `authority-revision-workflow`

## Required workflow discipline

Every species audit run must be grounded in the species workflow layer.

Start with:

- `docs/workflows/workflow-execution.md`
- `docs/workflows/species-audit-workflow.md`
- `docs/workcards/species-audit-workcard-template.md`

Then open only the workflow docs the run actually needs:

- `docs/workflows/technique-workflow.md`
- `docs/workflows/simulation-port-workflow.md`
- `docs/workflows/balance-review-workflow.md`
- `docs/workflows/dependency-review-workflow.md`
- `docs/workflows/core-sync-workflow.md`
- `docs/workflows/authority-revision-workflow.md`

Use the knowledge and simulator layers directly:

- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-design/knowledge_access/`
- `Transcendence-design/sim/TECHNIQUE-PORTING-PLAN.md`
- `Transcendence-design/sim/`

## Execution pattern

Treat each species audit as a run with an owner workflow, a target species, and an explicit conclusion about readiness and next steps.

### 1. Define the scope of the audit

Before reviewing content, decide what kind of audit this is:

- identity audit
- authored inventory audit
- mechanical spread audit
- simulation coverage audit
- publication drift audit
- full pass audit

Do not blur all of them together unless the user actually wants a full pass.

### 2. Instantiate the species audit work card

Use `docs/workcards/species-audit-workcard-template.md` as the run structure.

You may instantiate it as:

- a real work card file for substantial passes
- or a strict internal checklist for smaller audits

Do not skip it. Species audits become noisy quickly without explicit sections.

### 3. Separate inventory from judgment

First establish the inventory:

- what exists in authority
- what exists in structured data
- what exists in simulation
- what exists in publication

Only after the inventory is clear should you evaluate:

- identity strength
- redundancy
- missing coverage
- balance risk
- backlog order

### 4. Route local findings to the right owner workflow

The audit can reveal problems, but it does not own every repair.

Examples:

- one Technique needs rewrite -> route to `technique-workflow`
- one Technique needs simulator support -> route to `simulation-port-workflow`
- species-wide cost pattern looks off -> route through `balance-review-workflow`
- repeated blocker depends on unclear subsystem rule -> route through `dependency-review-workflow` or `authority-revision-workflow`
- publication drift is real -> route to `core-sync-workflow`

### 5. Close with backlog and status, not just observations

A species audit is not complete because it contains good commentary.

Close only when you can state:

- what is authored
- what is closed
- what is sim-ready
- what is blocked
- what should be prioritized next

## What to produce in a good species audit run

A strong species audit should leave behind:

- a clean inventory of species artifacts
- a judgment about identity coherence
- a view of mechanical spread
- simulator coverage status
- blocker classification
- prioritized backlog

At minimum, capture:

- species scope
- authored counts
- structured data counts
- sim-defined counts
- runtime-supported counts
- policy/scenario/question coverage state when relevant
- identity strengths
- identity drifts or redundancies
- notable weak or overloaded areas
- blockers
- next recommended batch of work
- change impact if the audit updated project state

## Quality rules

- Do not confuse "many entries exist" with "the species pass is healthy."
- Audit identity separately from sheer quantity.
- Keep authored, sim-ready, and published states distinct.
- Do not hide blockers inside vague summaries; classify them explicitly.
- Prefer prioritized backlog over laundry-list dumping.
- If the audit reveals an upstream rule problem, name it as such instead of treating it like a species-local flaw.
- When comparing species, keep the comparison doctrinal rather than turning every audit into a balance verdict.

## Suggested audit sequence

In many runs, this order works well:

1. read workflow docs and species authority sources
2. inventory authored and structured artifacts
3. inventory simulator and publication state
4. evaluate identity and mechanical spread
5. classify blockers and gaps
6. route findings to owning workflows where needed
7. write prioritized backlog and closure status

## Reference map

Use these local references first:

- `references/audit-map.md`
- `references/audit-checks.md`

Then open the actual project documents named there.
