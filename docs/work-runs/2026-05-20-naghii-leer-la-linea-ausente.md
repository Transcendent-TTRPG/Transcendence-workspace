# Naghii — Leer la Línea Ausente: Sim Port

`2026-05-20` · species: naghii · work_type: technique_authoring

## Purpose

Port `Leer la Línea Ausente` from `authored_example` in authority to `sim_defined`
in the simulation layer. The authority text (both `techniques.md` and `techniques.yaml`)
was already complete. This pass wired the sim data, cost question, scenario, and profile
so the technique has a defined simulation surface.

## What was done

### Sim data added

- `sim/data/techniques/naghii.yaml`: added `leer_la_linea_ausente` entry
  - `origin: Interpretacion` (Spanish without accent, consistent with `Percepcion`, `Sigilo` pattern)
  - `roll: family: specialization, competency: Interpretacion, opposed_by: null`
  - `effects: []` — information output is Narrator-side, no mechanical sim state
  - `duration_model: immediate`
  - classification: `data_only`

### Profile created

- `naghii_novice_archive_reader` in `sim/data/species/naghii_profiles.yaml`
  - `Interpretacion: rank: novice, level: 1`
  - Characteristics: `Astucia: 2, Sabiduría: 2`
  - Weapon: `kusari_fundo` (secondary to the technique's function)

### Scenario created

- `sim/scenarios/skirmish/naghii_archive_pattern_read.yaml`
  - Conditions: `incomplete_or_suspicious_pattern_present`, `absence_evidence_observable_in_scene`, `no_active_masking_or_deliberate_staging`
  - Default (uncontested) read — staging-opposed surface is a future extension

### Cost question defined

- `sim/questions/technique_value/naghii_leer_la_linea_ausente_cost.yaml`
  - Comparison: `leer_la_linea_ausente` vs `leer_el_calor_del_paso` (both R=3 / A=1 information reads)
  - Key question: timing viability — does R=3 leave enough ATB space to act on the absence category?

## Validation

- `validate_techniques.py`: 0 errors, 0 warnings — 74 canonical, 21 sim techniques checked

## Sim framing

| Field | Value |
| --- | --- |
| Runtime gap | `data_only` |
| Porting state | `sim_defined` |
| Runtime note | Interpretacion specialization roll resolves through existing path; all technique_value=0 because output is Narrator-side |
| Opposition gap | Deliberate-staging opposition not modeled — contextual masking matchup needs Interpretacion-opposed-by-staging surface (future `small_runtime_extension`) |

## Balance reads

### Confirmed

- `Leer la Línea Ausente` at R=3/A=1: structurally identical to `Leer el Calor del Paso` (R=3, guaranteed success, information only, no opposition in default case)
- The precondition `incomplete_or_suspicious_pattern_present` is the binding constraint justifying the Quick band
- Cost applies only during ATB — in exploration, this resolves as a normal Interpretation action with no ATB overhead

### Note

The staging-opposed surface (when another creature deliberately falsified the absence) is the technique's only meaningful opposition mechanic. Until that surface is modeled, the sim will show `resolution_rate = 1.0` unconditionally — consistent with the design intent for the default case.

## Acceptance closure

| Check | State |
| --- | --- |
| authority_updated | not_applicable — authority already complete |
| yaml_updated | not_applicable — techniques.yaml already complete |
| sim_defined_or_gap_classified | ✓ sim_defined |
| runtime_supported_or_gap_classified | ✓ data_only — no runtime support needed for default case |
| minimum_cost_question_defined | ✓ naghii_leer_la_linea_ausente_cost.yaml |
| coverage_updated | ✓ (naghii now at 15 techniques in sim data) |
| core_sync_done_or_not_needed | not_needed this pass |

## Pending items

- Staging-opposition surface: `Interpretacion opposed_by masking_or_staging` — needs contextual masking matchup mechanic
- `naghii_novice_archive_reader` has no `Intelecto` characteristic (the associated characteristic for Interpretacion); modifier will be 0 in sim until a profile with Intelecto is defined or characteristic mapping is extended
