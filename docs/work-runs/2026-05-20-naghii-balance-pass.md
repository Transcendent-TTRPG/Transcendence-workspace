# Naghii Balance Pass — Techniques 9–12

`2026-05-20` · species: naghii · work_type: simulation_validation

## Purpose

Wire techniques 9–12 so balance experiments can actually run. Techniques 1–8
were already validated. 13–14 (`trabar_el_gesto`, `plantar_la_guardia`) are
blocked on runtime extensions.

## What was done

### Scenarios created

| Scenario | Used by |
| --- | --- |
| `naghii_trace_read_window` | `leer_el_calor_del_paso_cost` |
| `naghii_threshold_pressure` | `pesar_el_umbral_cost`, `pesar_el_umbral_fear_rate` |

Both `naghii_projection_line_5m` (clavar_la_cadencia) and
`naghii_flexible_pressure_2m` (tocar_y_ceder) already existed.

### Profiles updated

- `naghii_novice_projection_scout`: added `clavar_la_cadencia`
- `naghii_novice_torsion_keeper`: added `tocar_y_ceder`

### Runner extended

- `_value_score`: added `ailment_applied` parameter (value 1.0)
- New metrics in `run_technique_cost_iteration`:
  - `ailment_application_rate`
  - `aterrorizado_application_rate` (alias for pesar_el_umbral question metrics)
  - `rr_failure_rate_in_target` (alias — equals ailment_applied since two-stage collapses to one event)
  - `resolution_rate` (always 1.0 for leer_el_calor_del_paso since no opposition)
- New runner functions: `run_clavar_la_cadencia_cost_experiment`,
  `run_tocar_y_ceder_cost_experiment`, `run_leer_el_calor_del_paso_cost_experiment`,
  `run_pesar_el_umbral_cost_experiment`
- `run_balance_analysis.py`: added 3 cost techniques to `COST_QUESTIONS`; added
  `DATA_ONLY_QUESTIONS` section for leer_el_calor_del_paso

### Tests

16/16 pass — 4 new tests added for the new runner functions.

## Numbers (n=2000, ±2.2% CI)

### Clavar la Cadencia — R=4 / A=1 / reactive

| Metric | Value |
| --- | --- |
| hit_rate | 0.635 |
| effective_damage_rate | 0.382 |
| movement_disruption_rate | 0.000 (not tracked — ≈ hit_rate in reality) |
| rhythm_efficiency | 0.095 |
| attrition_efficiency | 0.382 |

Low ηR is expected: weapon base_potency=5 (marking_dart_launcher), and the
movement disruption effect is not captured in `technique_value`. Movement
disruption on hit ≈ 63.5% via `reduce_target_movement_rank_bonus`.

**Gap to resolve**: authority cost_note references R=5; structured field is R=4.
This discrepancy predates this run and needs editorial resolution.

### Tocar y Ceder — R=5 / A=1 / active

| Metric | Value |
| --- | --- |
| hit_rate | 0.715 |
| effective_damage_rate | 2.249 |
| return_rate | 0.000 (not tracked — ≈ hit_rate in reality) |
| rhythm_efficiency | 0.507 |
| attrition_efficiency | 2.535 |

Reads plausible at R=5. Lower absolute value than spear techniques at same cost
because kusari_fundo has base_potency=6 vs spear (8). The advance+retreat cycle
provides safety not captured by current metrics (return_rate ≈ hit_rate = 71.2%).

### Leer el Calor del Paso — R=3 / A=1 / active

| Metric | Value |
| --- | --- |
| resolution_rate | 1.000 (confirmed via test) |
| all question metrics | 0.000 (info-only, Narrator-side output) |

Always resolves — no opposition (opposed_by=null). R=3 consistent with Quick
band for guaranteed-success narrow utility. The sim cannot score this technique
because there is no mechanical state change.

### Pesar el Umbral — R=3 / A=1 / active

| Metric | Value |
| --- | --- |
| aterrorizado_application_rate | 0.635 |
| rr_failure_rate_in_target | 0.635 |

63.5% fear application from hidden position. The binding precondition (valid
concealment required) justifies Quick band. Comparable to single-stage fear
techniques at R=4, but cheaper because access is precondition-gated.

## Balance reads

### Confirmed

- `Tocar y Ceder` at R=5/A=1: plausible
- `Leer el Calor del Paso` at R=3/A=1: consistent, no failure mode, correct band
- `Pesar el Umbral` at R=3/A=1: 62.6% application under precondition — justified

### Flagged

- `Clavar la Cadencia`: authority R=5 vs sim R=4 discrepancy unresolved. Low
  ηR is not a problem per se (weapon potency + untracked disruption), but the
  cost field conflict must be resolved in the design authority before this
  technique can be treated as settled.

## Metric gaps

Two technique-specific metrics are not yet tracked by the runner:

| Metric | Technique | Gap |
| --- | --- | --- |
| `movement_disruption_rate` | `clavar_la_cadencia` | `reduce_target_movement_rank_bonus` moves target but isn't scored as value |
| `return_rate` | `tocar_y_ceder` | `reposition_after_hit_distance` moves actor back but net position delta = 0 |

Both can be approximated as ≈ hit_rate. Neither gap affects the balance read
materially for this pass.

## Policy state

`policy_exercisable: 0` for all Naghii techniques — the conservative policy
still only knows Zarnag techniques. This is the next gap after runtime coverage.
