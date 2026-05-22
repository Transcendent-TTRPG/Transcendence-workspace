# Work Run — Trabar el Gesto Backfill

## Header

- `work_id`: 2026-05-20-naghii-trabar-el-gesto-backfill
- `owner_workflow`: `technique-workflow`
- `linked_workflows`: `simulation-port-workflow`
- `artifact_type`: technique
- `status`: sim_defined / runtime_partial

## Scope

- `species`: Naghii
- `technique_id`: trabar_el_gesto
- `goal`: Full backfill — sim definition, corebook entry, technique card, glossary, questions, porting plan update
- `current_state`: authored in design authority; not yet in sim or publications
- `out_of_scope`: runtime extension implementation (deferred, classified small_runtime_extension)

## Phase checkpoints

### Phase 0. Intake

- `scope_recorded`: yes
- `main_question`: Can Trabar el Gesto be sim-defined using existing effects, and what runtime extension is needed to make it executable?

### Phase 1. Species Framing

- `fantasy`: Read the commitment arc of the enemy's weapon action; send the flexible weapon into that line before the stroke can lock in. Catch lands on arm, grip, or execution line — not to hold, but to break the moment.
- `world_origin`: Naghii archive guard threshold-denial training. Confined archive spaces without full parrying guards; catching the weapon arm or execution line before the stroke completes is a specific taught discipline.
- `why_not_base_action`: A base flexible-weapon attack strikes the target's body on the user's turn. Trabar el Gesto intercepts a weapon commitment arc on the enemy's turn and applies a disabling condition — identity is breaking the enemy's ability to complete an action, not dealing harm.
- `interaction_surfaces`: primary — reactive weapon-arc interruption; secondary — Impedido application on failed R.R., cancelling triggering action

### Phase 2. Mechanical Framing

- `category`: utility / reactive
- `roll_model`: Interruption specialization check vs weapon execution commitment; on success → Alteration R.R. against Impedido
- `competency_source`: Flexible Weapons (profile: Interruption)
- `effect_model`: utility_check_primary + apply_ailment (Impedido, rank-scaled severity)
- `duration_model`: ailment_persistence (Impedido until Enfoque recovery)
- `restrictions`: weapon-rooted actions only; credible contact line required; no movement restriction; one target

### Phase 3. Dependency Framing

- `upstream_dependencies`: Impedido ailment — not yet in sim ailments data → added in this run
- `downstream_dependencies`: none
- `blockers`: enemy_weapon_declaration_trigger_hook (ATB model); cancel_triggering_action_on_rr_failure (activation result)
- `linked_files`: sim/data/ailments/ailments.yaml, sim/data/techniques/naghii.yaml

### Phase 4. Balance Framing

- `cost_sanity_note`: R=5 / A=1. Reactive with condition output (Impedido) and triggering-action cancellation. Trigger is narrow (weapon execution only), target has R.R. window, condition is recoverable via Enfoque. +1 Rhythm vs Cerrar la Línea (R=4) is justified by condition output over pure exchange interception.
- `sibling_comparison_note`: Cerrar la Línea R=4 (reactive weapon exchange); Anudar el Paso R=4 (reactive denial procedural state). Trabar el Gesto R=5 for condition-application + action cancellation is doctrinal. Not yet sim-validated.
- `pressure_note`: Impedido prevents weapon-rooted techniques until Enfoque recovery — meaningful tempo suppression if R.R. fails.
- `counterplay_note`: Target has Alteration R.R. window; user needs credible contact line; does not function against non-weapon actions.

### Phase 5. Simulation Framing

- `runtime_gap_classification`: small_runtime_extension
- `porting_state_target`: sim_defined (data entry complete); runtime_supported blocked on extension
- `missing_components`:
  - enemy_weapon_declaration_trigger_hook — ATB loop needs a point where reactive techniques can fire before the enemy's weapon-rooted activation completes
  - cancel_triggering_action_on_rr_failure — activation result needs a flag/mechanism to cancel the source action when ailment applies
  - rank-scaled severity in apply_ailment — current apply_ailment uses fixed severity string; dynamic rank-based severity resolution not yet implemented
- `scenario_seed_note`: naghii_interruption_pressure_reach — Naghii novice vs melee aggressor in confined reach; needs trigger rate and condition landing rate exposure
- `question_seed_note`: cost question (R=5 vs R=4 reactive baseline); disruption question (action cancellation + Impedido duration value)

### Phase 6. Editorial Framing

- `authority_cleanup_note`: Design authority clean; no rewrites needed.
- `terminology_note`: Impedido (ES), Interrupción profile (ES), T.R. Alt. = Alteration Resistance Roll.
- `core_sync_note`: Corebook entry created. Glossary entry needed for Trabar el Gesto and Impedido.

## Integration

- `files_changed`:
  - `sim/data/ailments/ailments.yaml` — added Impedido ailment definition
  - `sim/data/techniques/naghii.yaml` — added trabar_el_gesto entry
  - `sim/questions/technique_value/naghii_trabar_el_gesto_cost.yaml` — created
  - `sim/questions/technique_value/naghii_trabar_el_gesto_disruption_value.yaml` — created
  - `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/12-trabar-el-gesto.md` — created
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/trabar-el-gesto.html` — created
  - `sim/TECHNIQUE-PORTING-PLAN.md` — updated counts and added entry
- `sim_updated`: yes — data entry and ailment definition; execution blocked pending small_runtime_extension
- `core_updated`: yes — corebook entry and technique card created
- `knowledge_updated`: no

## Validation

- `roll_integrity`: pass — Interruption specialization check vs weapon execution commitment is coherent
- `surface_integrity`: pass — utility surface (interruption) + ailment surface (Impedido) are correctly separated
- `exchange_integrity`: not_applicable — no weapon damage exchange
- `ailment_integrity`: pass — Impedido defined in sim ailments; rank-scaled severity documented; recovery via Enfoque correct per design authority
- `critical_break_integrity`: not_applicable
- `atb_integrity`: partial — reactive timing modeled in data; execution hook is the open gap
- `dependency_integrity`: pass — Impedido added; no other upstream blockers
- `simulation_integrity`: partial — data entry valid; static validator passes; runtime execution blocked on two engine gaps
- `balance_sanity`: pass — R=5/A=1 doctrinal and defensible; pending sim validation
- `loader_validation`: pass — validate_techniques.py passes (effect IDs are in SUPPORTED_EFFECT_IDS)
- `scenario_validation`: blocked — scenario naghii_interruption_pressure_reach not yet created
- `question_validation`: pass — two questions defined and saved
- `publication_consistency`: pass — corebook entry and card match design authority cost, trigger, and effect text

## Closure

- `owner_workflow`: technique-workflow
- `linked_workflows`: simulation-port-workflow
- `acceptance_status`: partial — sim_defined and publications complete; runtime_supported blocked on small_runtime_extension
- `unresolved_items`:
  - enemy_weapon_declaration_trigger_hook (ATB engine)
  - cancel_triggering_action_on_rr_failure (activation result model)
  - rank-scaled severity in apply_ailment
  - scenario naghii_interruption_pressure_reach (not yet created)
  - glossary entries for Trabar el Gesto and Impedido
- `downstream_follow_up`: implement small_runtime_extension before re-running porting state to runtime_supported; create scenario before question execution
- `change_impact`: Impedido is now sim-facing; any future techniques that apply Impedido can reuse the data definition
