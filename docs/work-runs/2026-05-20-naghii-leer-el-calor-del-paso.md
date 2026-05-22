# Naghii — Leer el Calor del Paso Backfill

Date: `2026-05-20`

Owner workflow:
- `technique-workflow`

Linked workflows:
- `simulation-port-workflow`

Scope:
- full backfill for `Leer el Calor del Paso` (Naghii Perception utility technique)
- design authority correction (rhythm_cost 4 → 3)
- sim YAML entry, corebook entry, technique card, glossary, porting plan, sim questions

## Technique Summary

| Field | Value |
| --- | --- |
| Name | Leer el Calor del Paso |
| Name (EN) | Read the Heat of the Step |
| Origin | Percepción |
| Category | Utility |
| Type | Active |
| Rhythm | 3 |
| Attrition | 1 |
| Range | Sensorial |
| Area | Single creature or trace |
| Duration | Instant |
| Roll | T.P. (Percepción technique check) |
| Save | Contextual (only if target actively masking) |

## Cost Correction

The design authority YAML had `rhythm_cost: 4` but the techniques.md table and the cost_note both specified R=3. The structured field was corrected to `rhythm_cost: 3`. This follows the same cost_note arbitration rule established for Plantar la Guardia: cost_note prose wins when the structured field is inconsistent with documented reasoning.

## Sim Classification

**`runtime_supported`** — data_only path.

The Percepcion specialization roll resolves through the existing `_resolve_specialization_opposed` path with `roll.family = "specialization"`, `roll.competency = "Percepcion"`, `roll.opposed_by = null`. The engine handles Percepcion via the specializations-catalog mapping (`Percepcion` → `Sabiduría` characteristic). No exchange effects needed. Effects list is empty — information output is Narrator-side and has no mechanical sim state.

### Known limitation

Contextual masking opposition (target actively masking → Sigilo check vs. Percepcion) is not modeled. The sim treats all reads as uncontested. This means the technique always succeeds when triggered, which is acceptable for baseline cost and timing questions but limits the depth of information-quality questions.

## Files Changed

### Design authority
- `Transcendence-design/data/system/techniques.yaml` — rhythm_cost corrected 4 → 3

### Sim
- `Transcendence-design/sim/data/techniques/naghii.yaml` — added `leer_el_calor_del_paso` entry
- `Transcendence-design/sim/data/species/naghii_profiles.yaml` — added technique to `naghii_novice_projection_scout`
- `Transcendence-design/sim/TECHNIQUE-PORTING-PLAN.md` — Naghii sim_defined 12→13, runtime_supported 10→11; added row to Naghii ported set table
- `Transcendence-design/sim/questions/technique_value/naghii_leer_el_calor_del_paso_cost.yaml`
- `Transcendence-design/sim/questions/technique_value/naghii_leer_el_calor_del_paso_read_window.yaml`

### Publications
- `Transcendence-publications/core-books/transcendence-corebook/09-techniques/es/14-leer-el-calor-del-paso.md`
- `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/naghii/leer-el-calor-del-paso.html`
- `Transcendence-publications/canon/glossary.md` — added Leer el Calor del Paso entry

## Sim Questions Registered

1. `naghii_leer_el_calor_del_paso_cost` — Is R=3/A=1 viable in ATB? Does spending R=3 leave a useful window to act on the information before the target's next activation?
2. `naghii_leer_el_calor_del_paso_read_window` — How often does the technique fire before the target acts? What is the typical information window?

## Notes on Non-Weapon Techniques

This is the first Naghii Perception technique ported. Key difference from weapon techniques:
- No weapon exchange, no zone, no target_slot required for the roll
- Roll resolves through `_resolve_specialization_opposed` with any competency, not just weapon competencies
- Effects list is empty — the "output" is a narrative truth from the Narrator, not a mechanical state
- Policy use is limited until a `creature_state_marker` procedural state is added (future small_runtime_extension), which would let policies act on the information

For cost/timing questions, the technique is immediately testable. For questions about information value vs. masking, contextual masking opposition needs a separate runtime surface.
