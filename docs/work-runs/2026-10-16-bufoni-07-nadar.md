# Séptima técnica Bufoni — El aliento reservado

## Header

- `work_id`: `2026-10-16-bufoni-07-nadar`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`: `technique-play-surface-workflow`, revisión de dependencias de exposición y Venenos.
- `artifact_type`: `technique`
- `status`: `authored`, ID 168, 2026-10-16. Integración Core ES/EN → tarjeta/hoja → YAML completa; comprobaciones focales aprobadas. Runtime, equilibrio experimental y revisión visual pendientes.

## Scope

- `species`: Bufoni como origen; no restricción racial.
- `technique_id`: 168, disponible tras comprobar máximo 167 y ausencia de entrada publicada.
- `goal`: registrar la única técnica discutida y aprobada, Core ES/EN → tarjeta/hoja → YAML.
- `current_state`: nombre, entrada completa, reacción, requisitos Nadar + Resistencia al Veneno Novato, dificultad contextual y coste 0/1 aceptados por el creador.
- `out_of_scope`: aprendizaje de Seku u otros personajes, nuevas fórmulas/venenos, revisión global del catálogo, motor de simulación, commits/push, cambios a archivos antiguos o al manifest.

## Mandatory sources

- authority docs/data: técnicas, dominios de especialización (Swimming), Agravios, costes; YAML de técnicas y Agravios.
- seeds/canon: capítulo 6 ES Bufoni; diseño complementario. La biología informa la práctica, pero no exige Lengua, linaje ni Piel Permeable.
- knowledge references: skills de autoría y superficie; workflows y workcard; registro previo de 167.
- publication: 38 Tomar la Corriente; 21 Templar el Veneno; 39 Guardar el Pulso; 115 Tórax de Forja; 128 Lo Que el Cuerpo Delata; 167 La dosis perdida; capítulos 8 y 11.
- simulation: inspección pendiente; no presumir soporte por el registro YAML.

## Phase checkpoints

### Phase 0. Intake

- `scope_recorded`: una técnica; discusión aprobada, no pase completo de especie.
- `main_question`: transferir control respiratorio de Nadar y experiencia de exposición a una reacción anterior a la entrada de veneno, sin mejorar la natación literal.
- Baseline: 143 registros centrales, máximo ID explícito 167. SHA semántico YAML completo `c89d755ff900858055ae3bac08e971ec0e521715bff35317e3f5dbb0b5e1ffc5`. Siete artículos previos conservados por hash. Manifest SHA `ef741863600b59b4116e8c011aa7c1e6f33787e64574e7e6edbdb63750225859`.

### Phase 1. Species Framing

- `fantasy`: controlar la inspiración involuntaria ante una descarga química puntual perceptible bajo presión de combate.
- `world_origin`: disciplina compatible con una cultura de compuestos peligrosos y lectura corporal; no fijar escuela, maestro o dominio nuevos.
- `why_not_base_action`: contener la respiración con preparación sigue siendo posible; la técnica permite respuesta inmediata ante una aplicación imprevista, con prueba y coste. No aumenta tiempo bajo el agua ni velocidad de Nadar.
- `interaction_surfaces`: detección previa legítima, vía de inhalación, aplicación puntual, T.E. contextual antes de la T.R., esfuerzo.
- Resistencia al Veneno es experiencia/requisito, no Alquimia, detección automática o bonificador añadido. La vulnerabilidad cutánea Bufoni permanece.

### Phase 2. Mechanical Framing

- `category`: Reactivo - Utilidad; Novato; origen híbrido Nadar + Resistencia al Veneno.
- `roll_model`: T.E. de Nadar; Narrador fija dificultad antes de tirar según rapidez/circunstancias del control respiratorio. No usar toxicidad, Naturaleza de una criatura o umbral de T.R. como sustitutos automáticos: el objetivo es el propio control, no otra criatura.
- `competency_source`: ambas competencias Novato o superior; no sumar Resistencia a la T.E. ni progresarla automáticamente mediante esa prueba.
- `effect_model`: éxito impide esa aplicación por inhalación; fallo conserva exposición y T.R. normales. Una tentativa por practicante/aplicación, antes de inhalar y antes de conocer la T.R.
- `duration_model`: Instantáneo; no protección mantenida, promesa para otra acción o reserva de aire extraordinaria.
- `restrictions`: no detección/identificación, tratamiento, otra vía, Asfixiado, exposición continua o cobertura de aplicaciones posteriores. Coste 0/1 incluso en fallo.
- Pool real de Nadar: 38 responde a desplazamiento forzado; no inhalación. La fila del catálogo que lista 36 Sellar la Presa como Nadar está desactualizada: 36 es Bastión. Corregir solo esa fila afectada.
- Cruces: 21 reduce severidad ya asentada; 39 mitiga un estado durante una acción; 115 purga tras resistencia fallida; 128 identifica contaminación; 167 neutraliza dosis externa mediante producto. Ninguna repite prevención respiratoria puntual anterior a la entrada.

### Phase 3. Dependency Framing

- `upstream_dependencies`: vías de Veneno del capítulo 11, Asfixiado, T.E., dificultad contextual, ventana reactiva ATB y experiencia de resistencias. Reutilizar esas definiciones; no crear un veneno/estado/temporizador nuevo.
- `downstream_dependencies`: entrada ES/EN, tarjeta ES, hoja 6+2, YAML, referencia, glosario, README, catálogo y pruebas de registro.
- `blockers`: ninguno para autoría aprobada; motor y revisión visual son cierres separados.
- `linked_files`: documentados al cerrar integración.

### Phase 4. Balance Framing

- `cost_sanity_note`: 0/1 aprobado. Ajuste interno sin desplazamiento/manipulación, una única salida y coste consciente aunque falle. No cobrar el origen híbrido como pasiva 0/0: aquí sí hay ejecución deliberada.
- `sibling_comparison_note`: 38 (3/1) implica gestión física de desplazamiento; 39 (0/1+) respuesta interna con mitigación variable; 115 (0/1) purga posterior biológica; 167 (3/1 + consumible) neutralización externa. Esta reacción evita una sola aplicación perceptible por una sola vía.
- `pressure_note`: puede mejorar la supervivencia frente a descargas repetidas, pero exige percepción, prueba y gasto por cada aplicación; no anula toda la acción enemiga ni la exposición continua.
- `counterplay_note`: amenaza no percibida, exposición ya ocurrida, otra vía, nube persistente, acciones/circunstancias que impidan ejecución.

### Phase 5. Simulation Framing

- `runtime_gap_classification`: `new_subsystem`. Inspeccionados modelos de Agravios y motor de técnicas/Agravios: falta una fase tipada de exposición por vía, percepción previa, evento puntual/continuo e intercepción anterior a la entrada; no basta con cargar el registro. No portado solicitado ni implementado.
- `porting_state_target`: `authored`.
- `scenario_seed_note`: éxito/fallo, amenaza imperceptible, exposición puntual/continua, vía doble, veneno previo, Asfixiado coexistente y aplicaciones posteriores.
- `question_seed_note`: ¿0/1 aporta una respuesta situacional sin desplazar de forma dominante la resistencia normal, considerando doble requisito, percepción previa, dificultad contextual y exclusión de exposición continua? Contrastar 1/1 y 0/2; medir aplicaciones intentadas/evitadas, T.R. aún necesarias, Desgaste y supervivencia. Pregunta guardada, no experimento ejecutado.
- Preguntas derivadas: ventana anterior a inhalación/T.R.; no percepción gratuita; independencia de rutas; no cura/oxígeno; una tentativa por aplicación; exposición continua no fraccionable para encadenar reacciones.

### Phase 6. Editorial Framing

- `authority_cleanup_note`: preservar el efecto aprobado literalmente; añadir ejemplo aparte, no nuevas reglas.
- `terminology_note`: El aliento reservado / The Reserved Breath; regla ES con texto de ambientación separado. Sin Hereda/No Hereda Efectos por ser Utilidad.
- `core_sync_note`: crear par ES/EN en draft, canonical:false. No modificar capítulo 11 ni inventar soporte clínico.

## Approved ES effect

Cuando percibas una exposición puntual e inminente a un veneno por inhalación, puedes reaccionar antes de inhalarlo y antes de resolver su T.R. No necesitas identificar el compuesto, pero sí percibir la amenaza.

Realiza una T.E. de Nadar. El Narrador establece la dificultad antes de la tirada según la rapidez de la exposición y las circunstancias que dificulten controlar tu respiración.

Con éxito, evitas esa aplicación por inhalación. Si fallas, la exposición se resuelve normalmente, incluida su T.R. correspondiente.

Puedes intentarlo una sola vez contra cada aplicación y pagas el Desgaste aunque falles. No evita otras vías de entrada, elimina venenos activos ni protege contra Asfixiado. No puede utilizarse contra una exposición continua ni concede protección frente a aplicaciones posteriores.

## Integration

- `files_changed`: entrada ES/EN 168; tarjeta `el-aliento-reservado.html`; hoja `imprimir-bufoni.html` (6+2); YAML central; referencia `technique-el-aliento-reservado.md`; resumen de técnicas; fila Nadar del catálogo; glosario; README ES; esta workcard; pruebas `test_reserved_breath.py` y expectativa de paginación de `test_lost_dose.py`.
- `sim_updated`: no; fuera de alcance.
- `core_updated`: sí, ES/EN en draft/canonical:false; efecto ES aprobado literal y ejemplo separado. Tarjeta conserva el mismo efecto completo, sin compresión semántica.
- `knowledge_updated`: referencia focal, glosario, resumen y fila Nadar del catálogo; sin nueva doctrina global.

## Validation

- `roll_integrity`: pass; T.E. Nadar contextual, requisito separado de Resistencia, sin T.A., T.I., T.R. añadida ni bonificador híbrido automático.
- `surface_integrity`: pass estático; efecto aprobado idéntico en ES, tarjeta y copia de impresión; traducción y campos alineados. Revisión visual blocked por restricción previa, no eludida.
- `exchange_integrity`: pass estático; antes de inhalación/T.R., una tentativa por aplicación, fallo conserva exposición y resistencia normales.
- `ailment_integrity`: pass estático; solo entrada por inhalación, sin estado nuevo, cura, Asfixiado o cobertura de fuente continua/otra vía.
- `critical_break_integrity`: not_applicable.
- `atb_integrity`: pass de autoría; reacción 0/1 aprobada, esfuerzo incluso en fallo; no nueva acción de movimiento o protección futura.
- `dependency_integrity`: pass de registro; referencias reales ES/EN, requerimientos, exposición y vías conservados. No se modifican kits, productos o capítulos de Agravios.
- `simulation_integrity`: gap clasificado new_subsystem; no soporte afirmado.
- `balance_sanity`: pass de comparación doctrinal provisional; no cierre experimental.
- `loader_validation`: focal pass; global fail heredado, 144 registros centrales/21 de simulación, mismos 66 errores y 0 advertencias; ninguno de 168. YAML previo inalterado al excluir únicamente 168.
- `scenario_validation`: not_applicable; sin runtime.
- `question_validation`: pregunta mínima y derivadas guardadas; no ejecutables sin motor.
- `publication_consistency`: pass focal estático; 41 tests de registro pasan (15 de 168, 12 de 167 y 14 de productos); ambos archivos nuevos tienen 0 errores/advertencias de contenido. Escaneo en memoria: 309 archivos, 615 errores, 220 advertencias. Los 2 errores adicionales son la limitación conocida del indexer al buscar pares bajo corebook en lugar de técnicas independientes, aunque las referencias ES/EN reales existen.

### Preservation and inherited discrepancies

- Excluir solo 168 conserva los 143 registros previos y metadatos: SHA semántico `c89d755ff900858055ae3bac08e971ec0e521715bff35317e3f5dbb0b5e1ffc5`.
- Los siete artículos previos de impresión conservan sus hashes; nueva hoja 6+2. Identidad exacta de las siete tarjetas modernas con sus copias; Golpe Sin Eco ya tenía prosa comprimida distinta en la hoja antes de este pase. Se conserva esa diferencia heredada, no se normaliza silenciosamente.
- SVG, nesting HTML, identificadores únicos y rutas CSS pasan comprobación estática. No prueba overflow, fuentes o impresión.
- El manifest conserva SHA `ef741863600b59b4116e8c011aa7c1e6f33787e64574e7e6edbdb63750225859`; no se escribió. `git diff --check` pasa en raíz, diseño y publicaciones.

## Acceptance closure

- `authority_updated`: sí; referencia focal y resumen.
- `yaml_updated`: sí, 168 con contrato de prevención respiratoria.
- `sim_defined_or_gap_classified`: gap new_subsystem, no sim_defined.
- `runtime_supported_or_gap_classified`: gap explícito; no runtime_supported.
- `coverage_updated`: sí; fila Nadar corregida para 38 y 168, otras filas sin tocar.
- `core_sync_done_or_not_needed`: sí; ES/EN, tarjeta y hoja 6+2.
- `pending_items_explicit`: runtime, equilibrio experimental y revisión visual.

## Pending items

- No se ha autorizado ni implementado simulación o aprendizaje por personajes.
- Restricción previa de acceso visual a archivos locales: no eludir con otro navegador, servidor o renderer; comprobaciones HTML estáticas no certifican impresión.
- No reparar los errores globales antiguos ni regenerar pipeline/manifest.json.

## Change impact

- `concepts_touched`: prevención puntual por inhalación; combinación de control respiratorio y experiencia al Veneno.
- `decisions_reinforced_or_created`: Nadar transfiere conocimiento; resistencia como requisito sin bonificador; reacción 0/1, no pasiva 0/0; acceso abierto.
- `coverage_movement`: una técnica nueva de Nadar, sin nueva familia de Agravios.
- `follow_up_work`: portado runtime, escenarios/preguntas y revisión visual permitida.
