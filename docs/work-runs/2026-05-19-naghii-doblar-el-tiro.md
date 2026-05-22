# Work Run: Naghii - Doblar el Tiro

- Date: `2026-05-19`
- Owner workflow: `technique-workflow`
- Linked workflows:
  - `technique-play-surface-workflow`
  - `simulation-port-workflow`
  - `authority-revision-workflow`

## Scope

Pass `Doblar el Tiro` through authority confirmation, final player-facing surface, and initial simulation definition.

## Key decisions

- Corrected a small authority drift in profile localization:
  - `Ranged Weapons / Ricochet` now maps to `Ricochete` instead of `Sigiloso`
- Final surface keeps the Technique as:
  - `Activo - Ataque`
  - `Salvación: T.D.`
- Final requirements keep the real geometry gates:
  - `Arma con perfil Ricochete`
  - usable rebound surface
  - physically plausible indirect path

## Publication outputs

- Core entry:
  - `09-doblar-el-tiro.md`
- Card entry:
  - `cards/es/naghii/doblar-el-tiro.html`
- Print sheet:
  - `technique-cards/index.html`

## Simulation outputs

- Added `doblar_el_tiro` to:
  - `sim/data/techniques/naghii.yaml`
- Added to seed profile:
  - `sim/data/species/naghii_profiles.yaml`
- Added loader assertion:
  - `sim/tests/test_definition_loaders.py`

## Honest porting state

- `authored`
- `core done`
- `card done`
- `sim_defined`
- `runtime_supported`: `no`

## Runtime gap

`Doblar el Tiro` still needs a real indirect-geometry resolver that can:

- declare one rebound surface
- preserve final-path defense honestly
- deny only the original cover edge that the rebound line truly bypasses
- reject impossible rebound paths without pretending to be homing behavior

## Validation

- targeted loader test for the new definition
