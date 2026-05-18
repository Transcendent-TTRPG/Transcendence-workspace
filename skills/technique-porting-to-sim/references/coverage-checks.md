# Simulator Port Coverage Checks

Every Technique simulator port should leave recoverable coverage state.

## Definition checks

- Technique has a simulator definition or an explicit reason it does not
- relevant IDs and references are aligned with project naming
- declarative payload does not smuggle unsupported runtime semantics

## Runtime checks

- existing surface reuse was evaluated before extension
- runtime gap is classified with a formal class
- new runtime is minimal and justified

## Policy checks

- policy usage is explicit:
  - exercisable now
  - blocked for a known reason
  - intentionally deferred

## Scenario and question checks

- scenario need is stated
- question need is stated
- if absent, the reason is explicit

## Validation checks

- loader validation completed
- runtime validation completed when support claims were made
- tests added or updated when behavior changed

## Closure checks

- `sim_defined` status explicit
- `runtime_supported` status explicit
- `policy_exercisable` status explicit
- `scenario_tested` status explicit
- `question_ready` status explicit
- pending items explicit
- impact on technique coverage plan explicit
