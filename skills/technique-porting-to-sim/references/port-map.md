# Technique Porting to Sim Map

Use this file as the short navigation layer for simulator-port runs.

## Primary workflow docs

- `docs/workflows/workflow-execution.md`
  - how runs are owned, checkpointed, routed, and closed
- `docs/workflows/simulation-port-workflow.md`
  - main workflow for Technique simulator ports
- `docs/workcards/simulation-port-workcard-template.md`
  - work card structure for the run

## Secondary workflow docs

- `docs/workflows/dependency-review-workflow.md`
  - when a Technique port crosses subsystem boundaries
- `docs/workflows/balance-review-workflow.md`
  - when simulator work reveals cost or pressure issues
- `docs/workflows/technique-workflow.md`
  - when authority-side Technique closure is still missing
- `docs/workflows/authority-revision-workflow.md`
  - when the port is blocked by doctrinal ambiguity

## Core simulator docs

- `Transcendence-design/sim/README.md`
- `Transcendence-design/sim/ARCHITECTURE.md`
- `Transcendence-design/sim/DOMAIN-MODEL.md`
- `Transcendence-design/sim/DATA-SCHEMAS.md`
- `Transcendence-design/sim/TECHNIQUE-PORTING-PLAN.md`

## Common simulator file clusters

- `Transcendence-design/sim/data/techniques/`
- `Transcendence-design/sim/data/actions/`
- `Transcendence-design/sim/data/ailments/`
- `Transcendence-design/sim/data/species/`
- `Transcendence-design/sim/engine/`
- `Transcendence-design/sim/loaders/`
- `Transcendence-design/sim/models/`
- `Transcendence-design/sim/policies/`
- `Transcendence-design/sim/scenarios/`
- `Transcendence-design/sim/questions/`
- `Transcendence-design/sim/tests/`

## Common routing patterns

- authority clear + runtime already exists -> stay in simulation-port
- authority clear + small resolver needed -> stay in simulation-port with `small_runtime_extension`
- procedural/state family missing -> stay in simulation-port with `new_state_family`
- subsystem absent -> stay in simulation-port with `new_subsystem`
- authority unclear -> route to `authority-revision-workflow`
- Technique itself not closed -> route to `technique-workflow`
