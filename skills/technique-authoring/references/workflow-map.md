# Technique Authoring Workflow Map

Use this file as the short navigation layer for the skill. Open the target project documents only when the run needs them.

## Primary workflow docs

- `docs/workflows/workflow-execution.md`
  - how runs are owned, checkpointed, routed, and closed
- `docs/workflows/technique-workflow.md`
  - the main phase sequence for Technique work
- `docs/workcards/technique-workcard-template.md`
  - the structure to instantiate for a Technique run

## Secondary workflow docs

- `docs/workflows/dependency-review-workflow.md`
  - when the Technique is entangled with upstream or downstream systems
- `docs/workflows/balance-review-workflow.md`
  - when cost, pressure, frequency, or peer comparison need explicit review
- `docs/workflows/simulation-port-workflow.md`
  - when the task includes simulator definition, runtime support, or coverage
- `docs/workflows/core-sync-workflow.md`
  - when the task affects published explanation in ES/EN
- `docs/workflows/authority-revision-workflow.md`
  - when the Technique exposes an upstream doctrinal contradiction or taxonomy problem

## Project source clusters commonly needed

- `Transcendence-design/docs/system/`
  - Technique authority and nearby system doctrine
- `Transcendence-design/data/system/`
  - structured system definitions
- `Transcendence-design/docs/knowledge/`
  - doctrinal and governance memory
- `Transcendence-design/data/knowledge/`
  - registries, coverage, project state, source maps
- `Transcendence-design/sim/`
  - simulation architecture, schemas, runtime coverage, and technique port state

## Common routing patterns

- Technique phrasing only -> stay in `technique-workflow`
- Technique depends on unclear rule -> route to `authority-revision-workflow`
- Technique depends on linked subsystem but authority is clear -> route through `dependency-review-workflow`
- Technique needs runtime coverage -> route to `simulation-port-workflow`
- Technique changes published rules text -> route to `core-sync-workflow`
