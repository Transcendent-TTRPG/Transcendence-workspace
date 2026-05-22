# Naghii Runtime Closure Pass

Date: `2026-05-19`

Owner workflow:
- `simulation-port-workflow`

Linked workflows:
- `balance-review-workflow`
- `workflow-execution`

Scope:
- close the eight already-published novice Naghii Techniques to
  `runtime_supported`
- do not reopen authored effect text or core/card surface unless runtime work
  reveals a contradiction

## Techniques Covered

- `cerrar_la_linea`
- `clavar_el_paso`
- `recuperar_la_distancia`
- `anudar_el_paso`
- `robar_el_angulo`
- `marcar_la_lectura`
- `nublar_la_senal`
- `doblar_el_tiro`

## Runtime Work Added

### Reactive execution path

- added `as_reaction` support to `ActivationIntent`
- allowed reactive Techniques to execute off-turn instead of only as leftmost
  activations
- routed reactive Technique execution through timing-sensitive reaction gating
- charged reaction cost honestly through `spend_timeline_cost(..., as_reaction=True)`

### Procedural-state closure

- extended procedural states with fiction-event expiry support
- allowed authored cleanup / mark-clear / movement / concealment style exits to
  become runtime-visible instead of remaining pure notes

### Technique-specific closures

- `Cerrar la Línea`
  - now resolves as a real reactive spear exchange
- `Anudar el Paso`
  - now installs `clean_separation_denied`
- `Robar el Ángulo`
  - now resolves exchange + local reposition + `read_spoiled`
- `Marcar la Lectura`
  - now installs `read_marked` with fiction-event cleanup
- `Nublar la Señal`
  - now installs `signal_blurred` as bounded next-answer residue
- `Doblar el Tiro`
  - now resolves as a bounded indirect-surface ranged exchange

### Supporting runtime note

- added a simulator-local fallback weapon profile for `marking_dart_launcher`
  so the seeded Naghii projection profile can execute offense honestly inside
  the reduced sim catalog

## Validation

Executed:

```bash
PYTHONPATH=Transcendence-design/sim .venv/bin/python -m pytest Transcendence-design/sim/tests/test_activations_runtime.py
PYTHONPATH=Transcendence-design/sim .venv/bin/python -m pytest Transcendence-design/sim/tests
```

Results:

- `test_activations_runtime.py`: `20 passed`
- full `sim/tests`: `113 passed`

## Closure State

- all 8 novice Naghii seed Techniques are now `runtime_supported`
- Naghii still remains `policy_exercisable: 0`
- next real closure step is not more runtime scaffolding, but:
  - policy selection
  - scenario exposure
  - question-ready balance evaluation
