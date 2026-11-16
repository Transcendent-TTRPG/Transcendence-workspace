# Primera técnica Bufoni — La respuesta que no llega

## Header

- `work_id`: `2026-10-13-bufoni-01-aprovechamiento`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`: `technique-play-surface-workflow`; simulación pendiente.
- `artifact_type`: `technique`
- `status`: `authored`; regla aprobada, integrada y presentada; sin cierre de balance.

## Scope

- `species`: Bufoni como origen cultural, no como restricción.
- `technique_id`: 162, único en autoridad y posterior al máximo publicado 161.
- `goal`: desarrollar una sola técnica, discutirla y registrar la regla aprobada.
- `current_state`: entrada ES, pareja EN, tarjeta, hoja de impresión y autoridad sincronizadas.
- `out_of_scope`: un bloque de técnicas, cambios a venenos/especies, concesiones a Seku, motor narrativo, implementación de simulación y reparación semántica de registros antiguos.

## Mandatory sources

- Autoridad: `Transcendence-design/docs/system/techniques.md`, `technique-la-respuesta-que-no-llega.md`, `weapon-technique-profiles.md` y `atb-reference.md`.
- Datos: `Transcendence-design/data/system/techniques.yaml`, `weapon-technique-profiles.yaml`, `ailments.yaml`.
- Identidad principal: `Transcendence-publications/core-books/transcendence-corebook/06-species/es/14-bufoni.md`; contexto complementario de diseño, sin importar discrepancias como hechos nuevos.
- No existe `bufoni-technique-seeds.md`; esta técnica no sustituye un pase completo de semillas.
- Publicación: capítulo 11 ES, Venenos; técnicas 12, 28, 37, 59, 80, 148 y comparaciones cruzadas 130, 156, 157.
- Guías: `docs/workflows/workflow-execution.md`, `technique-workflow.md`, `technique-play-surface-workflow.md`, `technique-cost-stabilization.md`, `technique-cost-master-table.md`; skills de autoría/presentación; estilo, glosario y voz editorial.
- Simulación inspeccionada: `sim/engine/reactions.py`, `activations.py`, `ailments_runtime.py`, datos de agravios y lista de efectos admitidos por el validador.
- Las discrepancias del inventario por superficie no reemplazan la lectura directa de las técnicas publicadas.

## Phase checkpoints

### Phase 0. Intake

- `scope_recorded`: sí; una técnica por vez.
- `main_question`: aprovechar una limitación química existente para intervenir sobre una respuesta física concreta.
- Aprobación del creador: texto, requisito exacto, oposición y costes 4/1, 2026-10-13.
- Autorización adicional explícita: auditar y reparar la estructura YAML central conservando el contenido anterior.

### Phase 1. Species Framing

- `fantasy`: observar el retraso neuromuscular de una presa o adversario envenenado y cortar una intervención física.
- `world_origin`: práctica Bufoni; caza y preservación del Dominio también pueden producirla, no únicamente infiltración.
- Dominio, linaje, escuela, maestro y disponibilidad no fijados.
- `why_not_base_action`: concede un intento entrenado de cancelar una Reacción, incluso contra terceros; no es un ataque ordinario ni identificación del veneno.
- `interaction_surfaces`: `timing_atb`, `ailments_resistance`.
- El veneno no genera una fase adicional de preparación ni cancelación automática.

### Phase 2. Mechanical Framing

- `category`: utilidad reactiva; rango Novato con el arma.
- `roll_model`: T.A. con el arma, opuesta a T.D.; éxito estrictamente superior, empate falla.
- `competency_source`: competencia del arma con perfil Interrupción; sin requisito racial.
- `effect_model`: cancelar una Reacción completa con ataque físico o desplazamiento, declarada por objetivo al alcance, antes de empezar a resolverse. Puede responder a otra criatura.
- El objetivo conserva los costes de Ritmo y Desgaste de la Reacción cancelada.
- `duration_model`: Instantáneo.
- `restrictions`: Entorpecido activo, severidad Leve/Moderada/Grave, de cualquier fuente; un intento por Reacción declarada. No contra esta misma técnica, Acciones Activas ni T.D. ordinaria.
- No daño, T.I., efecto natural del arma ni modificación del veneno. Otros agravios, heridas y Fatiga no sustituyen Entorpecido.

### Phase 3. Dependency Framing

- `upstream_dependencies`: Entorpecido exacto, acceso al perfil, alcance, declaración de Reacción y resolución antes de sus efectos.
- `downstream_dependencies`: entrada, pareja EN, tarjeta, hoja de impresión, datos y referencia humana.
- `blockers`: error de sangría reparado con autorización; quedan 66 errores previos de metadatos y soporte de simulación no implementado.
- No se cambiaron costes, efectos ni datos previos para lograr pasar el validador.

### Phase 4. Balance Framing

- `cost_sanity_note`: Ritmo 4 / Desgaste 1 aprobados como punto de partida. Tiempo de intervención y esfuerzo acotado; no se declara balance probado.
- `sibling_comparison_note`:
  - 12/80: sustitución de defensa propia con daño y Alteración.
  - 28: defensa exitosa y contraataque.
  - 37: reacción a movimiento con Atrapado; referencia de coste condicional 4/1.
  - 59: defensa propia sustituida para cancelar y dañar.
  - 148: cancelar una técnica activa, sin daño, 3/1.
  - 157: continuidad del movimiento propio frente a una reacción, Acrobacias, 0/1.
  - 130: lectura que encarece respuestas; 156: lectura de patrón al defender.
- Diferencia funcional: apoyo químico exacto e intervención en una Reacción física que puede dirigirse contra otro. No se afirma unicidad solo por origen cultural.
- `pressure_note`: preparación previa, oportunidades dependientes de severidad, intervención sobre terceros y pérdida de costes del objetivo requieren comparación ejecutable.
- `counterplay_note`: T.D., retirada del veneno, negar alcance y usar acciones fuera del disparador.

Precomprobación de armas naturales con Interrupción (revisada antes del diseño):

| Arma | Efecto natural relevante |
| --- | --- |
| Cola Naghii | Margen 3 y resistencia fallida: Desorientado. |
| Cola Sauri | Penalizador a la defensa del objetivo. |
| Garras Zarnag | Margen 3 y resistencia fallida: Lacerado. |
| Garras Drak'kai | Margen 3: desplazamiento forzado. |
| Garras Rokhart | Margen 3: movimiento sin reacciones del objetivo. |
| Expulsión Corrosiva Formix | Margen 3 y resistencia fallida: Corroído. |
| Cuerno Ceratox | Margen 3 y resistencia fallida: Derribado y Lacerado. |
| Garras Chelicer | Margen 3 y resistencia fallida: Sobrecargado. |
| Mordisco Panin | Margen 3 y resistencia fallida: Conmocionado. |
| Lengua Bufoni | Impacto y resistencia fallida: veneno de linaje. |
| Mordisco Kesh | Margen 3 y resistencia fallida: Lacerado. |
| Bilis Yacani | Impacto y resistencia fallida: Erosionado. |

La nueva utilidad no resuelve impacto ni hereda estos efectos. No introduce la etiqueta Hereda Efectos.

### Phase 5. Simulation Framing

- `runtime_gap_classification`: `small_runtime_extension`, estimación de portado, con Entorpecido como dependencia previa no portada.
- `porting_state_target`: estado alcanzado `authored`; todavía no `sim_defined`, `runtime_supported` ni `question_ready`.
- Evidencia: `reactions.py` resuelve respuestas defensivas y sus costes; no expone una declaración interceptable por un tercero. `activations.py` omite ese hook defensivo al ejecutar una reacción.
- Se necesitan ventana pre-resolución, guardas de un intento/autointercepción, T.A. sin impacto, conservación de costes y permiso de intervención sobre terceros.
- Búsqueda en `sim`: Entorpecido no está portado. No sustituirlo por otro agravio ni afirmar que existe su cálculo de costes.
- `scenario_seed_note`: repetir con las tres severidades, veneno de otra fuente, sin veneno, veneno distinto, fuera de alcance, éxito/fallo/empate, Reacción contra tercero, T.D. ordinaria, Acción Activa y ejecución de esta misma técnica.
- `question_seed_note`: ¿4/1 se justifica frente a 148 y 157 cuando se contabiliza la preparación de Entorpecido, el acceso a terceros y los costes de la Reacción cancelada? Separar frecuencia de oportunidades, éxito, activaciones preservadas y ritmo/desgaste netos. Este planteamiento queda guardado aquí; no es aún una pregunta ejecutable ni un resultado de balance.

### Phase 6. Editorial Framing

- `authority_cleanup_note`: reparación estructural acotada; inserción única en `pilot_examples`; borrador YAML separado consolidado y eliminado, referencia humana trasladada a ruta estable.
- `terminology_note`: Entorpecido es Veneno, no Alteración ni condición genérica. EN conserva el nombre ES porque no existe traducción autorizada; se retiró la traducción provisional no sustentada.
- `core_sync_note`: pareja ES/EN en `draft`, `canonical: false`, costes y restricciones iguales; tarjeta condensada sin cambiar la regla.
- Tarjeta de 70 × 125 mm; se conservaron tamaños tipográficos y se compactaron solo espacios locales. Revisión visual pendiente: el navegador bloquea `file:`; no se intentó eludir ese bloqueo.

## Integration

- `files_changed`:
  - `Transcendence-design/data/system/techniques.yaml`.
  - `Transcendence-design/docs/system/techniques.md`, `technique-la-respuesta-que-no-llega.md`, `technique-surface-catalog.md`.
  - `Transcendence-publications/core-books/transcendence-techniques/es/162-la-respuesta-que-no-llega.md` y README ES.
  - `Transcendence-publications/core-books/transcendence-techniques/en/162-the-response-that-never-comes.md`.
  - `Transcendence-publications/technique-cards/transcendence-technique-cards/cards/es/bufoni/la-respuesta-que-no-llega.html` y `imprimir-bufoni.html`.
  - Esta ficha de trabajo.
- `sim_updated`: no.
- `core_updated`: sí, nuevas entradas de técnica; sin cambiar especie, veneno ni personaje.
- `knowledge_updated`: catálogo por superficie y referencia humana; no cierre canónico global.

## Structural audit

- Antes: ParserError en línea 13565; el validador no podía cargar el archivo.
- Reparación: 5 encabezados + 24 bloques completos realineados en la lista existente; 29 registros en total.
- Se conservaron todos los caracteres no blancos y los objetos de los 137 registros previos. No había IDs duplicados.
- SHA-256 del archivo anterior a la reparación: `5fb3190c826e20b269c20101b894f520c9116729b390d6bb10cc8162ada7c3af`.
- SHA-256 semántico previo a insertar 162 (`yaml.safe_dump(obj, sort_keys=True)`): `799bc080ad83b4135ce938a3efd5533fcd27d9e200151b9d0e2ac464526c7e34`.
- Después de insertar 162 y excluirlo del cálculo, ese mismo hash coincide: registros y metadatos anteriores preservados.
- Se mantuvieron los cambios no relacionados que ya existían en los repositorios.

## Validation

- `roll_integrity`: revisión documental; T.A. > T.D., empate falla. No prueba de ejecución.
- `surface_integrity`: revisión documental; Interrupción, competencia del arma; sin restricción de especie.
- `exchange_integrity`: revisión documental; sin impacto ni herencia. Ejecución pendiente.
- `ailment_integrity`: referencia cruzada; Entorpecido exacto, las tres severidades, cualquier fuente.
- `critical_break_integrity`: `not_applicable`; no daño ni ruptura.
- `atb_integrity`: costes y momento explícitos; retención/encadenamiento no probados en runtime.
- `dependency_integrity`: referencias editoriales y autoridad verificadas; dependencia de simulación pendiente.
- `simulation_integrity`: no ejecutada; gap identificado.
- `balance_sanity`: comparación de superficies/costes; no cierre empírico.
- `loader_validation`: YAML central parseable; registro nuevo completo para las comprobaciones del validador. Validación global sigue fallando por 66 campos faltantes previos.
- `scenario_validation`: pendiente del portado.
- `question_validation`: planteamiento guardado, pregunta ejecutable pendiente.
- `publication_consistency`: comprobación estática ES/EN/tarjeta/autoridad; revisión visual pendiente.

## Acceptance closure

- `authority_updated`: sí.
- `yaml_updated`: sí.
- `sim_defined_or_gap_classified`: gap clasificado.
- `runtime_supported_or_gap_classified`: gap clasificado; no soporte declarado.
- `coverage_updated`: no aumento de cobertura de simulación.
- `core_sync_done_or_not_needed`: entradas y tarjeta sincronizadas.
- `pending_items_explicit`: sí; formalización completada, no cierre de balance.

## Pending items

- Revisión visual de tarjeta e impresión.
- Portado de Entorpecido y ventana de intercepción de Reacciones; escenarios y pregunta de coste ejecutables.
- Revisión de los 66 errores antiguos de metadatos, solo en trabajo autorizado separado; no rellenar propósitos ni orígenes por inferencia.

## Change impact

- `concepts_touched`: nueva utilidad reactiva Bufoni; sin cambiar sistemas base ni personajes.
- `decisions_reinforced_or_created`: origen cultural distinto de requisito racial; requisito exacto distinto de hindrance genérica; preparación distinta de éxito automático.
- `coverage_movement`: entrada `authored`; ningún ascenso en simulación.
- `follow_up_work`: revisión de esta técnica y después discutir la siguiente de una en una. No asignarla a Seku por proximidad biográfica.
