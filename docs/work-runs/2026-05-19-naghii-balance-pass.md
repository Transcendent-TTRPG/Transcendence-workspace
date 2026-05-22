# Naghii Novice Balance Pass

Date: `2026-05-19`

Owner workflow:
- `balance-review-workflow`

Linked workflows:
- `simulation-port-workflow`

Scope:
- review `Rhythm` and `Attrition` for the eight already-published novice
  Naghii Techniques
- do not reopen effect text, fantasy, or final player-facing surfaces unless a
  true contradiction appears
- use the now-complete `runtime_supported` set as the basis for a first real
  doctrinal balance pass

## Techniques Reviewed

- `Cerrar la Línea`
- `Recuperar la Distancia`
- `Clavar el Paso`
- `Anudar el Paso`
- `Robar el Ángulo`
- `Marcar la Lectura`
- `Nublar la Señal`
- `Doblar el Tiro`

## Canonical References Used

- `Transcendence-design/docs/adr/combat-atb-rhythm-costs.md`
- `Transcendence-design/sim/reports/technique-balance-matrix.md`

## Read

### Spear ladder

- `Cerrar la Línea` → `4 / 1`
- `Recuperar la Distancia` → `5 / 1`
- `Clavar el Paso` → `5 / 2`

This reads internally coherent:

- narrow reactive lane punish
- attack plus clean one-meter reset
- committed forward entry with heavier fatigue burden

No rebalance recommended at this stage.

### Flexible weapons

- `Anudar el Paso` → `4 / 1`
- `Robar el Ángulo` → `4 / 1`

Current read:

- `Anudar el Paso` still looks fair because the runtime only denies clean
  separation; it does not become full hold or immobilization
- `Robar el Ángulo` is the sharper candidate for future underpricing because it
  steals local position and spoils the target's next direct answer

No immediate rebalance, but `Robar el Ángulo` should be one of the first saved
questions.

### Ranged weapons

- `Doblar el Tiro` → `4 / 1`
- `Marcar la Lectura` → `4 / 1`
- `Nublar la Señal` → `4 / 1`

Current read:

- `Doblar el Tiro` looks acceptable while the novice geometry stays bounded to
  one declared rebound surface
- `Marcar la Lectura` looks plausible because it preserves readability without
  directly converting into damage or a broad static buff
- `Nublar la Señal` is the most likely efficient ranged utility because one
  spoiled sensory answer can swing tempo harder than its raw cost suggests

No immediate rebalance, but `Nublar la Señal` should be in the first wave of
saved questions.

## Provisional Verdict

### Looks coherent now

- `Cerrar la Línea`
- `Recuperar la Distancia`
- `Clavar el Paso`
- `Anudar el Paso`
- `Doblar el Tiro`

### Coherent but worth routine confirmation

- `Marcar la Lectura`

### Highest-priority balance questions

- `Robar el Ángulo`
- `Nublar la Señal`

## Important note

This pass is a real runtime-backed doctrinal read, not a final numeric proof.

The next meaningful closure step is:

- saved questions
- repeated scenario exposure
- then only rebalance if the measured value drifts past the current doctrinal
  read
