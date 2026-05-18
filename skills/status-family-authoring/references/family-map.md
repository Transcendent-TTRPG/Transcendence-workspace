# Status Family Map

Use this file as the short navigation layer for family-level runs.

## Primary workflow docs

- `docs/workflows/workflow-execution.md`
  - run ownership, checkpointing, routing, and closure
- `docs/workflows/status-family-workflow.md`
  - main workflow for repeated status-family work

## Secondary workflow docs

- `docs/workflows/dependency-review-workflow.md`
  - when the family crosses subsystem boundaries
- `docs/workflows/balance-review-workflow.md`
  - when the family needs tiering or cost/pressure review
- `docs/workflows/simulation-port-workflow.md`
  - when the family needs simulator normalization or runtime support
- `docs/workflows/core-sync-workflow.md`
  - when the family affects published explanation
- `docs/workflows/authority-revision-workflow.md`
  - when the family exposes upstream doctrinal ambiguity
- `docs/workflows/technique-workflow.md`
  - when the work narrows back down to one Technique-scale artifact

## Common source clusters

- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`
- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`
- `Transcendence-design/sim/`
- `Transcendence-publications/`

## Common routing patterns

- family grammar and entries only -> stay in status-family
- upstream doctrinal ambiguity -> route to `authority-revision-workflow`
- subsystem coupling blocker -> route to `dependency-review-workflow`
- simulator normalization -> route to `simulation-port-workflow`
- publication explanation drift -> route to `core-sync-workflow`
