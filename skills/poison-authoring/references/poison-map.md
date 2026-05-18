# Poison Authoring Map

Use this file as the short navigation layer for poison runs.

## Primary workflow docs

- `docs/workflows/workflow-execution.md`
  - run ownership, checkpoints, routing, and closure
- `docs/workflows/status-family-workflow.md`
  - main workflow for repeated status-family work

## Secondary workflow docs

- `docs/workflows/dependency-review-workflow.md`
  - when poison logic crosses subsystem boundaries
- `docs/workflows/balance-review-workflow.md`
  - when onset, persistence, or pressure raise tuning concerns
- `docs/workflows/simulation-port-workflow.md`
  - when poison support must be expressed in the simulator
- `docs/workflows/core-sync-workflow.md`
  - when poison doctrine affects publication explanation
- `docs/workflows/authority-revision-workflow.md`
  - when poison doctrine is blocked by upstream ambiguity

## Common source clusters

- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`
- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-design/sim/`
- `Transcendence-publications/`

## Common routing patterns

- poison-family grammar and entries only -> stay in poison-authoring
- unclear antidote or cleansing doctrine -> route to `authority-revision-workflow`
- unresolved stacking or decay coupling -> route to `dependency-review-workflow`
- onset/persistence pressure concerns -> route to `balance-review-workflow`
- simulator support required -> route to `simulation-port-workflow`
- publication explanation required -> route to `core-sync-workflow`
