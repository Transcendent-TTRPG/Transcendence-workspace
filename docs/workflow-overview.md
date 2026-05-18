# Workflow Overview

This folder describes how Transcendence production work should be structured
across design, simulation, and publication.

The goal is not to automate judgment away. The goal is to reduce ambiguity,
repetition, and hidden dependencies by separating responsibilities clearly.

## Layers

### `Knowledge Layer`

Purpose:
- preserve doctrine
- preserve canonical decisions
- preserve source-of-truth mappings
- support retrieval by domain
- track coverage and project state

Primary homes:
- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-design/knowledge_access/`

This layer does not author Techniques or other game artifacts directly. It
exists so every later layer works from cleaner memory and better context.

### `Artifact Skills Layer`

Purpose:
- encode repeatable production procedures by artifact type
- reduce improvisation in repetitive work
- define minimum structure, required updates, and non-negotiable checks

Examples:
- `technique-authoring`
- `technique-porting-to-sim`
- `corebook-sync`
- `species-pass-audit`
- future family skills such as `infection-authoring` or `poison-authoring`

Current local skill index:
- [`skills/README.md`](../skills/README.md)

### `Role / Lens Layer`

Purpose:
- review work through explicit perspectives instead of mixing every concern at
  once

Core lenses:
- `species_lens`
- `system_lens`
- `dependency_lens`
- `balance_lens`
- `simulation_lens`
- `editorial_lens`
- `continuity_lens`

These lenses may be implemented as:
- checklists
- prompts
- subagent roles when the task is large enough to justify separation

### `Workflow Layer`

Purpose:
- define the canonical phase order for each artifact type
- make outputs, validation, and closure explicit

This layer is the main coordinator. It should remain procedural and auditable,
not magical.

### `Execution Layer`

Purpose:
- make workflows runnable by agents instead of merely readable by humans
- force explicit checkpoints
- provide reusable work cards and closure gates

Primary homes:
- `docs/workflows/workflow-execution.md`
- `docs/workcards/`

## Current workflow documents

- [Workflow Execution](./workflows/workflow-execution.md)
- [Authority Revision Workflow](./workflows/authority-revision-workflow.md)
- [Batch Refactor Workflow](./workflows/batch-refactor-workflow.md)
- [Balance Review Workflow](./workflows/balance-review-workflow.md)
- [Dependency Review Workflow](./workflows/dependency-review-workflow.md)
- [Status Family Workflow](./workflows/status-family-workflow.md)
- [Technique Workflow](./workflows/technique-workflow.md)
- [Technique Play Surface Workflow](./workflows/technique-play-surface-workflow.md)
- [Simulation Port Workflow](./workflows/simulation-port-workflow.md)
- [Core Sync Workflow](./workflows/core-sync-workflow.md)
- [Species Audit Workflow](./workflows/species-audit-workflow.md)

## Current work card templates

- [Work Card README](./workcards/README.md)
- [Technique Work Card Template](./workcards/technique-workcard-template.md)
- [Simulation Port Work Card Template](./workcards/simulation-port-workcard-template.md)
- [Species Audit Work Card Template](./workcards/species-audit-workcard-template.md)

## Design principle

The system should prefer:
- clear phase outputs over vague “done enough” states
- explicit dependency mapping over hidden cross-file assumptions
- acceptance criteria over informal completion
- change impact records over memory-by-chat
