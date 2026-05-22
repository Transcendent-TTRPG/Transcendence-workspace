---
name: "technique-porting-to-sim"
description: "Use when an authored Technique must be translated into simulator definitions, runtime surfaces, policy coverage, scenario coverage, or explicit runtime-gap status. Follow the simulation-port workflow instead of patching sim files ad hoc."
---

# Technique Porting to Sim

Use this skill when the user wants an authored Technique to become simulator-aware, simulator-defined, or explicitly classified in simulator coverage.

This skill does not own upstream Technique authoring. It assumes the Technique already has enough authority clarity to be ported, or it names the exact reason that the port is blocked.

## When to use this skill

Use `$technique-porting-to-sim` when the task is to:

- port an authored Technique into `Transcendence-design/sim/`
- decide whether a Technique reuses existing runtime or needs new support
- classify simulation readiness for a Technique
- add simulator data definitions for a Technique
- extend runtime only as much as the Technique actually needs
- define policy/scenario/question coverage for a Technique
- update technique coverage state after simulator work

Do not use this skill as the primary owner when:

- the Technique itself is still mechanically ambiguous in authority
- the task is really authoring or revising the Technique text first
- the task is a broad species audit
- the task is a status-family subsystem build rather than a Technique port

In those cases, route first through:

- `technique-workflow`
- `authority-revision-workflow`
- `species-audit-workflow`
- `status-family-workflow`

## Required workflow discipline

Every simulator port run must be grounded in the simulation workflow layer.

Start with:

- `docs/workflows/workflow-execution.md`
- `docs/workflows/simulation-port-workflow.md`
- `docs/workcards/simulation-port-workcard-template.md`

Then open only the workflow docs the run actually needs:

- `docs/workflows/dependency-review-workflow.md`
- `docs/workflows/balance-review-workflow.md`
- `docs/workflows/technique-workflow.md`
- `docs/workflows/authority-revision-workflow.md`

Read project simulator context before extending runtime:

- `Transcendence-design/sim/README.md`
- `Transcendence-design/sim/ARCHITECTURE.md`
- `Transcendence-design/sim/DOMAIN-MODEL.md`
- `Transcendence-design/sim/DATA-SCHEMAS.md`
- `Transcendence-design/sim/TECHNIQUE-PORTING-PLAN.md`

Use the knowledge layer and simulator coverage state instead of relying on memory:

- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-design/knowledge_access/`

## Execution pattern

Treat each simulator port as a run with an owner workflow, a target Technique, and explicit coverage outcomes.

### 1. Confirm the Technique is port-ready

Before touching `sim/`, verify that authority is stable enough.

If the port is blocked by unclear rule ownership, missing dependency resolution, or unresolved Technique semantics, stop calling it a simulator task and route back to the correct owner workflow.

### 2. Instantiate the simulation-port work card

Use `docs/workcards/simulation-port-workcard-template.md` as the run structure.

You may instantiate it as:

- a real work card file for substantial runs
- or a strict internal checkpoint list for small ports

Do not skip it. Porting without coverage bookkeeping causes silent drift.

### 3. Decide reuse before extension

Always ask, in this order:

1. can the Technique be expressed with existing simulator definitions only?
2. can it use existing runtime with a small resolver extension?
3. does it need a new procedural family or state family?
4. does it need a new subsystem?
5. is the port blocked by authority ambiguity?

Do not create new runtime surfaces until the simpler answers are clearly insufficient.

### 4. Separate definition work from runtime work

Most ports cross two distinct layers:

- declarative simulator definition
- runtime support

Do not blur them.

Typical declarative targets:

- `Transcendence-design/sim/data/techniques/*.yaml`
- `Transcendence-design/sim/data/actions/*.yaml`
- `Transcendence-design/sim/data/ailments/*.yaml`
- `Transcendence-design/sim/data/species/*.yaml`
- `Transcendence-design/sim/questions/`
- `Transcendence-design/sim/scenarios/`

Typical runtime targets:

- `Transcendence-design/sim/engine/`
- `Transcendence-design/sim/models/`
- `Transcendence-design/sim/loaders/`
- `Transcendence-design/sim/policies/`
- `Transcendence-design/sim/experiments/`

### 5. Route when the run crosses boundaries

Do not fake local completion when the port really changes another layer.

Examples:

- if a port exposes an upstream doctrinal contradiction, route to `authority-revision-workflow`
- if the Technique itself still needs authoring closure, route to `technique-workflow`
- if runtime reuse depends on unresolved subsystem coupling, route through `dependency-review-workflow`
- if the port forces a meaningful cost/power reinterpretation, route through `balance-review-workflow`

### 6. Close with coverage state, not just passing tests

The run is not complete just because the code loads.

You must leave behind explicit statements of:

- `sim_defined`
- `runtime_supported`
- `policy_exercisable`
- `scenario_tested`
- `question_ready`

If one or more are false, record the exact gap instead of implying completeness.

For `question_ready`, the minimum honest expectation is usually:

- one saved question about whether the current `Rhythm` / `Attrition` pair is
  justified

And when the Technique leans on a clear secondary surface, also:

- one derived question for that surface or an explicit recorded gap

## Runtime gap language

Use only the formal simulator gap classes:

- `data_only`
- `small_runtime_extension`
- `new_state_family`
- `new_subsystem`
- `authority_blocked`

Choose the smallest honest class.

## What to produce in a good simulator port run

A strong port run should leave behind:

- a clear mapping from authored Technique to simulator surfaces
- updated simulator data definitions
- minimal, justified runtime changes
- policy/scenario/question implications
- updated coverage state
- explicit blockers if the port is incomplete

At minimum, capture:

- source Technique
- declared simulator surfaces
- reuse vs extension decision
- runtime gap classification
- touched simulator files
- policy coverage status
- scenario coverage status
- question coverage status
- minimum cost question
- derived question set
- validation status
- impact on coverage trackers

## Quality rules

- Do not invent simulator semantics that the authority does not support.
- Do not call a Technique "runtime supported" if it still depends on hand-waved procedural behavior.
- Prefer existing ailment, concealment, reaction, exchange, ATB, and procedural-state surfaces before creating a new one.
- Keep declarative data and runtime semantics aligned; do not hide missing runtime in YAML.
- If a port is blocked by authority, record `authority_blocked` instead of patching around the ambiguity.
- If a Technique is data-defined but not policy- or scenario-exercisable, say that explicitly.
- Do not call a Technique fully validated if it has runtime support but no
  saved cost question yet.
- If the Technique's value depends on ailments, concealment, procedural states,
  reactions, geometry, breakage, kits, or residues, inspect whether that
  surface also deserves its own question.
- Extend runtime narrowly; do not perform opportunistic subsystem redesigns during a local Technique port unless the workflow has explicitly shifted.

## Suggested port sequence

In many runs, this order works well:

1. read simulation workflow docs and authority sources
2. inspect current runtime surfaces and nearby Techniques
3. classify the runtime gap
4. update simulator data definitions
5. extend runtime only if required
6. update policies, scenarios, and questions
7. validate loaders, runtime, and coverage
8. record acceptance and impact

## Reference map

Use these local references as your first navigation layer:

- `references/port-map.md`
- `references/coverage-checks.md`

Then open the actual project documents named there.
