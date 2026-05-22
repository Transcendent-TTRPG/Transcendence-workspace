# Simulation Port Work Card

## Header

- `work_id`: 2026-05-19-naghii-clavar-la-cadencia-port
- `owner_workflow`: `simulation-port-workflow`
- `linked_workflows`: `technique-workflow` (editorial gap on cost field)
- `artifact_type`: `simulation_port`
- `status`: closed

## Scope

- `target_artifact`: Clavar la Cadencia (Naghii / Ranged Weapons / Volley)
- `species_or_family`: Naghii
- `goal`: Move from `authored` to `runtime_supported` + `question_ready`
- `current_porting_state`: `authored` → `runtime_supported`
- `out_of_scope`: policy wiring, scenario construction, broader Naghii backfill

## Mandatory sources

- authority docs: `Transcendence-design/data/system/techniques.yaml` (entry: Clavar la Cadencia)
- authority data: `Transcendence-design/data/system/weapon-technique-profiles.yaml` (Volley profile)
- simulator data: `Transcendence-design/sim/data/techniques/naghii.yaml`
- simulator runtime: `Transcendence-design/sim/engine/activations.py`, `sim/engine/effects.py`
- knowledge references: `sim/TECHNIQUE-PORTING-PLAN.md`
- porting-plan references: Naghii coverage matrix

## Phase checkpoints

### Phase 0. Intake
- `main_simulation_question`: Can a reactive Volley ranged attack that reduces target movement by rank bonus meters be run in the sim?
- `source_set_confirmed`: yes

### Phase 1. Authority Read
- `authority_summary`: Reactive Ranged Weapons technique using Volley profile. Triggers when a creature within ranged line declares or begins movement (approach, withdrawal, cover change, line break). Rolls attack (Ranged Weapons) vs Defense. If connected, reduces target's remaining movement distance by 1 meter per rank bonus of the competency used.
- `explicit_mechanical_claims`:
  1. Reactive timing (interrupts declared movement before it completes)
  2. Roll: attack roll (Ranged Weapons) opposed by Defense
  3. On success: standard weapon exchange resolves normally
  4. On success: target's remaining movement is reduced by 1m per rank bonus
  5. Duration: instant — only affects the triggering movement
- `explicit_non_claims`:
  - Does not create area suppression
  - Does not attack multiple targets
  - Does not reduce speed after the triggering movement resolves
  - Does not force a hard stop unless the reduction removes all remaining distance
- `editorial_gap`: `rhythm_cost` field is `4` but `cost_note` references "Rhythm 5 / Attrition 1 is deliberate." — contradiction between structured field and explanatory note. Sim uses structured field (R=4). Needs authority resolution in a linked technique-workflow pass.

### Phase 2. Surface Mapping
- `surface_map`:
  - reactive weapon exchange → `weapon_exchange_primary` (existing)
  - as_reaction=True timing → existing reaction support
  - movement reduction (1m × rank_bonus on target) → NO existing equivalent
- `dependency_map`:
  - `weapon_exchange_primary` with reaction timing: exists, used by Cerrar la Línea
  - target position shift by rank_bonus: needs new effect handler
- `provisional_gap_classification`: `small_runtime_extension` — one new position-change effect in `activations.py`

### Phase 3. Porting Decision
- `port_now_or_not`: port now
- `final_gap_classification`: `small_runtime_extension`
- `split_needed`: no — both the reactive exchange and the movement reduction can be implemented in this run

### Phase 4. Data Definition
- `sim_data_strategy`: add entry to `sim/data/techniques/naghii.yaml` using `weapon_exchange_primary` + new `reduce_target_movement_rank_bonus` effect
- `partial_port_note`: none — full effect set is being implemented

### Phase 5. Runtime Integration
- `runtime_changes_needed`: add `reduce_target_movement_rank_bonus` handler in `_apply_post_exchange_effects` in `engine/activations.py`; add effect to exclusion set so it does not fall through to `apply_effect_definition`; add to `SUPPORTED_EFFECT_IDS` in `engine/effects.py` and `pipeline/scripts/validate_techniques.py`
- `shared_surface_or_one_off`: shared surface — `reduce_target_movement_rank_bonus` is a reusable position-change effect for any technique that disrupts a target's movement by rank bonus

### Phase 6. Policy Exercise
- `policy_exercisable`: false — Naghii techniques have no policy wiring yet (0/8 policy_exercisable per porting plan)
- `policy_blocker_if_any`: no Naghii policy exists that triggers reactions on observed target movement

### Phase 7. Scenario Exposure
- `scenario_tested`: false
- `scenario_id_or_gap`: `naghii_projection_line_5m` is structurally compatible but does not explicitly declare target movement conditions. A dedicated "target movement common" variant would be needed for meaningful scenario testing.

### Phase 8. Question Definition
- `question_ready`: true
- `minimum_cost_question`: Is Rhythm 4 / Attrition 1 justified for Clavar la Cadencia, a reactive Volley ranged attack that on success also reduces the target's remaining movement by 1 meter per rank bonus?
- `cost_question_reference`: compare against Cerrar la Línea (R=4, reactive, pure exchange) and Robar el Ángulo (R=4, active, exchange + position steal)
- `derived_question_triggers`: positioning / geometry surface — movement reduction creates measurable positional swing
- `derived_questions`:
  - How much practical positional value does the rank-bonus movement reduction of Clavar la Cadencia create?
- `question_id_or_gap`: `naghii_clavar_la_cadencia_cost`, `naghii_clavar_la_cadencia_movement_disruption_value`

## Integration

- `files_changed`:
  - `sim/data/techniques/naghii.yaml` — added Clavar la Cadencia entry
  - `sim/engine/activations.py` — added `reduce_target_movement_rank_bonus` handler + exclusion
  - `sim/engine/effects.py` — added `reduce_target_movement_rank_bonus` to `SUPPORTED_EFFECT_IDS`
  - `pipeline/scripts/validate_techniques.py` — added `reduce_target_movement_rank_bonus` to `SUPPORTED_EFFECT_IDS`
  - `sim/questions/technique_value/naghii_clavar_la_cadencia_cost.yaml` — created
  - `sim/questions/technique_value/naghii_clavar_la_cadencia_movement_disruption_value.yaml` — created
  - `sim/TECHNIQUE-PORTING-PLAN.md` — updated Naghii coverage (9 → sim_defined / runtime_supported)
- `sim_data_updated`: yes
- `runtime_updated`: yes
- `tests_updated`: static validator passes; loader validation confirmed via `validate_techniques.py`

## Validation

- `loader_tests_done`: yes — `validate_techniques.py` passes with 0 errors
- `runtime_tests_done`: pending — no focused activation test for Clavar la Cadencia yet
- `policy_tests_done`: not applicable (no policy wiring)
- `scenario_checks_done`: not applicable (no scenario wiring)
- `question_checks_done`: yes — both question files created and structurally valid

## Acceptance closure

- `authority_read_complete`: yes
- `surface_map_recorded`: yes
- `gap_classified`: `small_runtime_extension` — implemented
- `sim_data_updated_or_blocked`: updated
- `runtime_updated_or_blocked`: updated
- `coverage_state_updated`: yes — porting plan updated to 9 sim_defined / 9 runtime_supported
- `pending_items_explicit`: yes

## Pending items

- `pending`:
  - `editorial_gap`: resolve R=4 vs R=5 discrepancy in `techniques.yaml` cost_note via linked technique-workflow pass
  - `policy_exercisable`: no Naghii policy yet triggers on observed target movement — needed before scenario testing
  - `runtime_test`: no focused `test_activations_runtime.py` test for Clavar la Cadencia yet
  - `balance_run`: minimum cost question is defined but simulation run not yet executed

## Change impact

- `runtime_surfaces_touched`: `reduce_target_movement_rank_bonus` — new reusable position-change effect that shifts a target backward by rank_bonus meters on a successful hit
- `new_reusable_abstractions`: `reduce_target_movement_rank_bonus` is directly reusable by any future technique that disrupts target movement by competency rank bonus
- `coverage_movement`: Naghii sim_defined 8→9, runtime_supported 8→9
- `follow_up_work`: Tocar y Ceder (Flexible / Skirmish) is the next unported Naghii technique in authored-order
