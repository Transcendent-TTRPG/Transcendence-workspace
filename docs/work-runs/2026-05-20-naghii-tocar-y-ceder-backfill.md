# Technique Work Card

## Header

- `work_id`: 2026-05-20-naghii-tocar-y-ceder-backfill
- `owner_workflow`: `technique-workflow`
- `linked_workflows`: `simulation-port-workflow`
- `artifact_type`: `full_backfill`
- `status`: closed

## Scope

- `target_artifact`: Tocar y Ceder (Naghii / Flexible Weapons / Skirmish)
- `species_or_family`: Naghii
- `goal`: Full backfill — sim data, runtime, questions, corebook entry, technique card
- `current_porting_state`: `authored` → `runtime_supported` + `question_ready` + publication
- `out_of_scope`: policy wiring, scenario construction, EN publication pass

## Mandatory sources

- authority: `data/system/techniques.yaml` (Tocar y Ceder)
- sim: `sim/data/techniques/naghii.yaml`
- sim runtime: `sim/engine/activations.py`
- publications: `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/`
- publications: `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/`

## Phase checkpoints

### Phase 0. Intake
- `main_simulation_question`: Can a 1m-approach + attack + conditional 1m-return flexible weapon technique be run in sim?
- `source_set_confirmed`: yes

### Phase 1. Authority Read
- `authority_summary`: Active Flexible Weapons Skirmish attack. Approach up to 1m pre-exchange (no separate movement action). T.A. vs Defense. On success: T.I. normally + immediate reposition up to 1m in any direction with no reaction opportunity triggered. Duration instant.
- `explicit_mechanical_claims`:
  1. Active (not reactive)
  2. Approach up to 1m pre-exchange, bundled into the action
  3. T.A. (Flexible Weapons) vs T.D. (Defense)
  4. On success: T.I. + reposition up to 1m, no reaction from that reposition
  5. Return contingent on successful attack — failed attack = no return
  6. Rhythm 5 / Attrition 1
- `explicit_non_claims`:
  - Does not create persistent control
  - Does not deny target future movement
  - Does not allow approach/return beyond 1m at Novice
  - Does not trigger a reaction on the conditional return movement
- `cost_note_consistent`: yes — structured field R=5 matches cost_note prose

### Phase 2. Surface Mapping
- `surface_map`:
  - 1m pre-exchange approach → `advance_before_exchange_distance` (meters: 1) — exists
  - active weapon exchange → `weapon_exchange_primary` — exists
  - conditional 1m post-hit return → `reposition_after_hit_distance` (meters: 1) — exists
- `dependency_map`: no new dependencies — all three surfaces exist in runtime
- `provisional_gap_classification`: `data_only`

### Phase 3. Porting Decision
- `port_now_or_not`: port now
- `final_gap_classification`: `data_only`
- `split_needed`: no

### Phase 4. Data Definition
- `sim_data_strategy`: compose `advance_before_exchange_distance` (1m) + `weapon_exchange_primary` + `reposition_after_hit_distance` (1m) — same pattern as Clavar el Paso + Recuperar la Distancia combined
- `partial_port_note`: none

### Phase 5. Runtime Integration
- `runtime_changes_needed`: none — data_only
- `shared_surface_or_one_off`: n/a

### Phase 6. Editorial / Publication
- `corebook_entry`: `09-techniques/es/11-tocar-y-ceder.md`
- `technique_card`: `cards/es/naghii/tocar-y-ceder.html`
- `new_profile_term`: Escaramuza (Skirmish) — added to glossary
- `cost_note_updated`: not needed — R=5 structured and prose are consistent; flagged as doctrinal-only until sim validates

### Phase 7. Questions
- `minimum_cost_question`: Is Rhythm 5 / Attrition 1 justified for Tocar y Ceder (approach 1m + active attack + conditional 1m return)?
- `derived_question`: How much practical value does the conditional 1m return of Tocar y Ceder create vs a simple flexible weapon exchange?
- `question_ids`: `naghii_tocar_y_ceder_cost`, `naghii_tocar_y_ceder_return_value`
- `cost_is_doctrinal`: yes — R=5 authored but not yet sim-validated; cost_note to be updated after balance run

## Integration

- `files_changed`:
  - `sim/data/techniques/naghii.yaml`
  - `sim/questions/technique_value/naghii_tocar_y_ceder_cost.yaml`
  - `sim/questions/technique_value/naghii_tocar_y_ceder_return_value.yaml`
  - `09-techniques/es/11-tocar-y-ceder.md`
  - `cards/es/naghii/tocar-y-ceder.html`
  - `canon/glossary.md` (Escaramuza)
  - `sim/TECHNIQUE-PORTING-PLAN.md`
- `sim_data_updated`: yes
- `runtime_updated`: no (data_only)
- `tests_updated`: static validator passes

## Validation

- `loader_tests_done`: yes — validate_techniques.py passes
- `runtime_tests_done`: no focused test yet
- `publication_consistent`: yes — card, core, and authority all match

## Acceptance closure

- `authority_read_complete`: yes
- `surface_map_recorded`: yes
- `gap_classified`: data_only
- `sim_data_updated_or_blocked`: updated
- `runtime_updated_or_blocked`: not needed
- `publication_artifacts_created`: yes
- `coverage_state_updated`: yes
- `pending_items_explicit`: yes

## Pending items

- `balance_run`: cost_note references R=5 doctrinal; minimum cost question defined but sim run not executed
- `runtime_test`: no focused activation test yet
- `policy_exercisable`: no Naghii policy wiring yet

## Change impact

- `runtime_surfaces_touched`: none (data_only)
- `new_reusable_abstractions`: none
- `coverage_movement`: Naghii sim_defined 9→10, runtime_supported 9→10
- `follow_up_work`: Trabar el Gesto is the next authored Naghii technique (reactive utility / Interruption profile)
