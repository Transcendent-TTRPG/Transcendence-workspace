# Sexta técnica Bufoni — Alquimia, revisión y discusión

## Header

- `work_id`: `2026-10-14-bufoni-06-alquimia`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`: revisión de dependencias de compuestos/materiales y countermeasures de venenos mediante poison-authoring; soporte separado en `2026-10-14-neutralizadores-alquimicos.md`, que se define antes del registro; presentación posterior si se aprueba.
- `artifact_type`: `technique`
- `status`: `authored`, ID 167, 2026-10-15. Redacción completa aceptada por el creador e integrada Core ES/EN → tarjeta/segunda hoja → YAML. Soporte de neutralizadores registrado. Port runtime, equilibrio experimental y revisión visual no completados.

## Scope

- `species`: Bufoni como origen cultural, no requisito racial.
- `technique_id`: 167, verificado libre antes de crear las superficies.
- `goal`: revisar Alquimia y discutir una sola función concreta durante ATB.
- `current_state`: intención aceptada de neutralizar una preparación química externa antes de su entrada al organismo mediante un neutralizador compatible preparado; la técnica aporta una intervención reactiva durante el ataque, no exclusividad sobre todo tratamiento en combate.
- `out_of_scope`: fabricación instantánea, antídoto universal, cambios a venenos ajenos, portado runtime, nuevas asignaciones a Seku y reparación global de validadores. Esta incorporación sí incluye entrada, tarjeta, hoja de impresión, datos y referencias de 167.

## Mandatory sources

- authority docs: `docs/system/specialization-technique-domains.md`, gobierno de dominios y entrada Alchemy; referencias de materiales/fabricación como dependencia posterior si se concreta un reactivo.
- authority data: entrada Alquimia de `data/system/specialization-technique-domains.yaml`; pool de requisitos de Alquimia en `techniques.yaml`.
- seeds/canon: capítulo 6 ES `14-bufoni.md` completo leído de nuevo; cultura/doctrina del pase y diseño complementario previo, sin introducir omnisciencia química o nuevas capacidades innatas.
- knowledge references: skill de autoría, workflow de técnica única y template completo de work card.
- simulation references if relevant: ninguno nuevo; no inferir soporte.
- publication references if relevant: 127, 39, 128, 115, 117, 79, 61, 148; comparación con 8/52/140 y 165 del pase anterior; capítulo 10 ES `05-alquimia.md` completo, fragmentos relevantes de kits/infraestructura, capítulo 11 ES `04-venenos.md` completo. Consulta de indexer con --search, sin regenerar manifest.

## Phase checkpoints

### Phase 0. Intake

- `scope_recorded`: el creador acepta pasar a revisión/discusión de Alquimia después de 166, no diseñar un bloque ni asignar aprendizaje a Seku.
- `main_question`: qué intervención química distinta puede surgir del conocimiento empírico Bufoni durante combate.
- Pool real verificado: una técnica publicada cuyo requisito es Alquimia, 127 El Ángulo Estudiado. La fila del catálogo que lista Guardar el Pulso es vieja: 39 requiere Tolerancia. Se documenta, no se corrige todavía.

### Phase 1. Species Framing

- `fantasy`: hipótesis: impedir que una preparación química externa siga funcionando, actuando sobre esa materia antes de que sea introducida en un organismo.
- `world_origin`: seres cuya piel, firmas territoriales y práctica de caza mantienen una relación cotidiana con compuestos. Conocimiento aprendido de compatibilidad/reacción y manejo cuidadoso de sustancias; no solo espionaje.
- Piel Permeable permanece sin contrarrestar directamente: no mejorar T.R., conceder inmunidad o purgar su cuerpo. Evitar una fuente concreta no vuelve resistente a toda sustancia ni exige ser Bufoni.
- `why_not_base_action`: debe concretarse un permiso de neutralización química bajo oposición, sin quitar/destruir el arma. No solo identificar un compuesto ni limpiar un objeto propio mediante Interactuar. La operación sobre equipo enemigo necesita alcance y entrega/oposición reales antes de formalizar.
- `interaction_surfaces`: preparación química externa, compatibilidad de agente, consumo, alcance/entrega, arma todavía funcional y posibilidad de volver a aplicar una dosis nueva.

### Phase 2. Mechanical Framing

- `category`: Reactivo - Utilidad; ejecución directa y momento anterior a la defensa aceptados. No ataque con daño ni estado nuevo aprobados.
- `roll_model`: T.E. (Alquimia) enfrentada a la T.A. original del ataque; debe superarla, empate/fallo dejan el ataque sin cambios. Aplicación externa físicamente accesible a 1 m; no contacto automático ni T.A. propia en sustitución de la especialización.
- `competency_source`: Alquimia; ningún linaje, Lengua o herencia como requisito. Conocimiento del tipo de veneno y neutralizador compatible de calidad suficiente; soporte inicial de Confusión registrado.
- `effect_model`: hipótesis de una preparación externa tratada que deja de entregar su efecto químico; el arma conserva su daño normal e integridad. No disarmar ni desactivar glándulas, secreción interna/continua, rasgos innatos o energía integrada.
- `duration_model`: Instantáneo aceptado para la transformación material de una dosis, no una protección sostenida. Una dosis nueva no queda automáticamente neutralizada.
- `restrictions`: por discutir: solo materia química externa expuesta/accesible; agente compatible real y disponible; no curar venenos internos, crear sustancias de la nada, inhibir toda química del objetivo, quitar competencias o asumir contacto/identificación universal.

### Phase 3. Dependency Framing

- `upstream_dependencies`: compuesto/recubrimiento y vía definidos, reconocimiento o conocimiento previo válido, material reactivo compatible, manejo seguro/kit cuando corresponde, consumo/dosis, llegada al punto tratado y oposición del portador.
- Capítulo 10 exige Fórmula/reactivos/rango para producir compuestos y alambique/instalación fija para síntesis terminada. Kit Alquímico permite preparación de índices, no fabricar productos terminados en una acción de combate. Esta hipótesis usa materia preparada, no deroga ese límite.
- Capítulo 11 permite aplicación de venenos en armas según su vía; quitar/inactivar la preparación externa no neutraliza un Veneno ya introducido en otro cuerpo. Tratamiento interno conserva su Kit de Medicina y regla.
- Soporte registrado: `materials-and-fabrication.yaml`, `alchemy.poison_neutralizers`, incluye tres fórmulas de neutralizador de Confusión. No son un catálogo universal de compatibilidades; poseer un kit no demuestra disponer de la sustancia necesaria. El producto no concede su propio modo externo ordinario: esta técnica aporta ese permiso.
- El catálogo de fórmulas del capítulo 10 y el catálogo de venenos del capítulo 11 no están perfectamente alineados en nombres/efectos/vías; no resolver esa discrepancia heredada inventando que todos son cutáneos o que un solo agente neutraliza cualquiera.
- `downstream_dependencies`: soporte inicial registrado en `materials-and-fabrication.yaml`, `alchemy.poison_neutralizers`, y capítulo 10 ES. Entrada/card/YAML 167 incorporados tras aprobación; runtime y revisión visual quedan explícitos. No reestructurar todo Alquimia o Venenos.
- `blockers`: ninguno para autoría del alcance aprobado. Compatibilidades nuevas exigen fórmulas propias; faltan motor y revisión visual para esos cierres, no redefinir el producto o la técnica.
- `linked_files`: registro de productos en `2026-10-14-neutralizadores-alquimicos.md` y las fuentes enlazadas allí.

#### Base aceptada por el creador

- Alquimia fabrica neutralizadores previamente, específicos para un tipo de veneno y disponibles en tres calidades. No se concede un neutralizador universal por vía de administración.
- La técnica interviene sobre una preparación externa durante el ataque, antes de que entre en el organismo; conserva el ataque físico y no cura intoxicaciones anteriores.
- Medicina conserva el tratamiento del organismo ya envenenado y sus requisitos. El apéndice permite Medicina en combate o bajo amenaza: no restringir todo tratamiento ordinario a fuera de combate para justificar esta técnica.
- Corrección aceptada el 2026-10-15: el producto se define como recurso de tratamiento por tipo/calidad, no con dos modos autónomos de uso. La aplicación externa reactiva es un permiso explícito de esta técnica; no hace falta repetirlo como modo ordinario de la fórmula. Medicina y sus kits/procedimientos no se sustituyen.
- Kit, calidad/rareza del compuesto, Índice Alquímico y severidad del agravio son campos distintos. Las excepciones publicadas de cada veneno no se eliminan por una tabla general de neutralizadores.

#### Soporte acotado aceptado por el creador

- Reutilizar las calidades Común, Rara y Excepcional, sin abrir una cuarta escala ni inventar requisitos de rango/ingredientes aún.
- Cada fórmula indica un tipo de veneno compatible. Una calidad mayor cubre preparaciones de calidad igual o inferior de ese mismo tipo: Común → Común; Rara → Común/Rara; Excepcional → las tres. Regla aceptada y registrada en autoridad/publicación el 2026-10-15.
- Medir la capacidad externa sobre la preparación material y su calidad, no sobre la severidad que acabaría sufriendo un organismo. Si una fuente no define su calidad o dosis, no deducirlas de su severidad sin una regla de conversión aprobada.
- Capacidad externa aceptada: una dosis de neutralizador por una dosis externa de veneno. No extender esa relación a tratar pacientes, áreas contaminadas, cargas múltiples o mezclas sin su definición específica. El creador también acepta el consumo al intentar la reacción, aunque falle.
- Conservar la fabricación por fórmula/instalación fija. Tres fórmulas de neutralizador de Confusión con reactivos, índices, tiempos y rendimientos aprobados y registrados.
- La aplicación directa a 1 m y la T.E. enfrentada comprueban la entrega. No conceder contacto automático por poseer el material.

#### Ejecución reactiva aceptada por el creador

- Declaración antes de resolver la defensa de un ataque con un arma que lleva una dosis externa de veneno compatible y conocido. La intervención debe preceder a la entrada del veneno, no rescatar retroactivamente una T.R. fallida.
- Neutralizador preparado y listo para aplicar; no incluye buscarlo en el equipaje, fabricarlo ni identificar automáticamente un veneno desconocido.
- Alcance directo aceptado: el punto envenenado del arma atacante debe estar a 1 m o menos y ser físicamente accesible al neutralizador. No heredar el alcance de un arma propia sin definir un medio de entrega. Puede cubrir a otra criatura si cumple esa geometría; sin movimiento añadido ni proyectiles.
- Una T.E. (Alquimia) enfrentada a la T.A. original del agresor: éxito solo si la supera; fallo/empate no neutralizan. La T.A. no se vuelve a tirar ni se altera. Comparación aceptada para aplicar material sobre un arma en movimiento, no dificultad de la Naturaleza de la criatura ni una T.A. propia encubierta.
- Compatibilidad y capacidad del compuesto son requisitos, no resultados de esa tirada. La prueba comprueba la ejecución reactiva de la entrega/dosificación; no vuelve universal al reactivo ni hace innecesario su conocimiento previo.
- En ambos resultados continúa el ataque original con defensa, daño físico y demás efectos habituales; el éxito elimina únicamente la dosis externa tratada. No exige que el ataque haya acertado.
- Gasto aceptado: comprometer y consumir la dosis de neutralizador al intentar la técnica, incluso si falla; una tentativa por practicante y ataque. Coste ATB 3/1, nombre La dosis perdida y rango Novato aceptados después de esta ejecución.

### Phase 4. Balance Framing

- `cost_sanity_note`: doctrina y tabla maestra completas releídas; Ritmo 3 / Desgaste 1 aceptado por el creador, no simulado. Aplicación física reactiva ocupa tiempo, una sola superficie química, sin negar el ataque físico ni producir daño. Compatibilidad, proximidad, oposición y consumo también limitan la repetición; no cobrar duración abstracta.
- `candidate_surface`: La dosis perdida / The Lost Dose; Rango Novato; Reactivo - Utilidad; Instantáneo; parámetros y texto completo aceptados. Registrada como 167, sin afirmar equilibrio experimental.
- `cost_comparables`: 163 La fuerza prestada (3/1, cambia el destinatario sin daño propio); 117 Saturación (2/1, purga corporal condicional de una Alteración, no química externa); 165 La mancha que vuelve (3/2, reaplicación de residuo con procedimiento heredado). Nuevo efecto compra solo neutralización específica de una dosis externa, con gasto material y ataque conservado; 3/1 aceptado para autoría, no veredicto experimental de equilibrio.
- `sibling_comparison_note`: 127 El Ángulo Estudiado debilita T.R. de una criatura respecto a tus acciones mediante lectura; no actúa sobre una preparación material expuesta. No repetir penalización a resistencias.
- Cruces funcionales revisados:
  - 39 Guardar el Pulso: Tolerancia, mitigación corporal de un estado durante una acción; no Alquimia ni neutralización de equipo.
  - 128 Lo Que el Cuerpo Delata: Herboristería, detecta contaminación y mejora T.R.; no neutraliza materia externa.
  - 115 Tórax de Forja: reacción Talpan tras T.R. fallida, purga un agente respiratorio; no copiar rescate corporal.
  - 117 Saturación: Yacani elimina una Alteración física del propio organismo; no purga venenos ni cambia un arma.
  - 79 La Vuelta Que Suelta: desarma al portador; esta hipótesis deja el arma en su mano.
  - 61 Hacer Ceder el Resguardo: ruptura estructural; no confundir química externa con daño a Durabilidad.
  - 148 Reconocer el Gesto: cancela una técnica activa; esta hipótesis neutraliza materia, no toda la acción/competencia.
  - 8/52/140 y 165: deterioro sensorial/tejidos/defensa o reaplicación de residuos; aquí no se aplica otro agravio ni se exige que la víctima esté limpiándose.
- `pressure_note`: desactivar una preparación puede tener valor persistente; no valorar como si toda la ofensiva del enemigo desapareciera. Limitar dosis/cobertura y evitar agentes universales.
- `counterplay_note`: conservar daño físico del arma, impedir entrega/contacto, no exponer el preparado, incompatibilidad del reactivo, cambiar de arma o recubrir con otra dosis; resolver una vez fijado el mecanismo.

### Phase 5. Simulation Framing

- `runtime_gap_classification`: `new_subsystem` compartido con los neutralizadores: compatibilidad, inventario de dosis, consumo y tratamiento no portados. También falta integrar su intervención anterior a la exposición. La dependencia material ya está formalizada para Confusión; no mantener authority_blocked ni inferir que basta data_only.
- `porting_state_target`: `authored`; sin datos/handlers de simulación añadidos.
- `scenario_seed_note`: recubrimiento externo versus glándula/veneno interno; agente compatible/incompatible/desconocido; arma conservada y daño físico; alcance y entrega impedidos; material agotado; dosis nueva; preparación múltiple y fallo de neutralización.
- `question_seed_note`: pregunta mínima de coste registrada: ¿3/1 permite neutralizar una dosis compatible frente a seguir con defensa/resistencia ordinarias sin desplazar de forma dominante esas respuestas, considerando 1 m, oposición a la T.A., gasto también en fallo, posible protección a terceros y nueva impregnación? Contrastar sensibilidad 2/1 y 4/1. Medir intentos, éxitos, dosis gastadas, inoculaciones evitadas, daño físico recibido y desplazamiento ATB; no contar ataques enteros cancelados ni daño propio. Pendiente de normalización del soporte y escenarios/runtime para responderla.

### Phase 6. Editorial Framing

- `authority_cleanup_note`: ninguna autoridad modificada.
- `terminology_note`: neutralización de dosis externa, no tratamiento del organismo ni cancelación del ataque. Nombre aceptado La dosis perdida; soporte material aceptado en discusión, no integrado.
- `core_sync_note`: redacción completa aprobada e integrada sin cambiar su efecto; ES/EN en draft/canonical:false, tarjeta ES y hoja actualizadas. Mantener reglas existentes de Kit de Venenos/manipulación sin inmunidad a autocontaminación ni Kit de Medicina para la intervención externa. La traducción del capítulo de Alquimia es una deuda aparte ya registrada.

### Texto completo aprobado por el creador — conservado para cotejo

#### La dosis perdida

Reactivo - Utilidad · Rango Novato

*El filo llega solo.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| 1m | 1 Superficie u Objeto | Instantáneo | T.E. (Alquimia) |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | — | 3 | 1 |

Requisitos:

- Competencia Novato o superior en Alquimia.
- Una dosis de neutralizador preparada y lista para aplicar, compatible con el tipo de veneno y de calidad igual o superior a la preparación que vas a neutralizar.

Palabra clave: Alquimia.

Cuando se realice un ataque con un arma que lleve una preparación externa de veneno cuyo tipo conozcas, puedes intervenir antes de resolver la defensa. El punto envenenado del arma debe encontrarse a 1 metro o menos de ti y ser físicamente accesible al neutralizador. Puedes intervenir aunque el ataque vaya dirigido contra otra criatura. Esta técnica no permite desplazarte ni interceptar proyectiles.

Elige una dosis externa de veneno y realiza una T.E. de Alquimia enfrentada a la T.A. del atacante. Si tu resultado no supera el suyo, la preparación permanece intacta. Si lo supera, neutralizas la dosis elegida, que pierde su capacidad de envenenar.

Para esta aplicación externa utilizas Alquimia, no Medicina, y no necesitas un Kit de Medicina. No es un intento de tratamiento del organismo.

En ambos casos, el ataque conserva su T.A. y continúa con la defensa, el impacto y los demás efectos habituales. No dañas ni desarmas el arma, no neutralizas venenos que ya hayan entrado en un organismo ni desactivas glándulas o secreciones internas. Una dosis nueva aplicada al arma no queda neutralizada por este uso.

Puedes intentar esta técnica una vez contra cada ataque. Consumes una dosis de neutralizador y pagas Ritmo y Desgaste aunque falles. Las reglas de manipulación de venenos y autocontaminación siguen aplicándose.

Ejemplo: un atacante obtiene T.A. 10 con una hoja que lleva una dosis de veneno conocido. Tienes un neutralizador compatible de calidad suficiente y el punto impregnado está a menos de 1 metro. Tu T.E. de Alquimia obtiene 12: neutralizas la dosis. La hoja conserva T.A. 10 frente a la defensa de su destinatario y puede causar su daño físico, pero esa dosis no lo envenena. Con T.E. 10, el empate dejaría el veneno intacto. En ambos casos consumes el neutralizador y pagas 3/1.

Nota de revisión actualizada: existen tres fórmulas fabricables para Confusión en el soporte registrado. La redacción aprobada no inventa calidad/dosis en otras fuentes viejas ni redefine el tratamiento dentro del paciente. Incorporación 167 completada para autoría.

Revisión retomada y aprobada el 2026-10-15: excepción de aplicación respecto al tratamiento clínico del producto (Alquimia sin Medicina ni Kit de Medicina), sin eximir reglas de manipulación de venenos. Sin cambios a coste, alcance, compatibilidad o efecto. Tras aprobación, se crearon entrada ES/EN, tarjeta y registro ID 167.

## Integration

- `files_changed`: esta ficha; entrada ES `167-la-dosis-perdida.md` y EN `167-the-lost-dose.md`; tarjeta `la-dosis-perdida.html`; hoja `imprimir-bufoni.html` (segunda página); `techniques.yaml`; referencia `technique-la-dosis-perdida.md`; resumen `techniques.md`; fila Alquimia en `technique-surface-catalog.md`; README ES; glosario; pruebas `pipeline/tests/test_lost_dose.py`.
- `sim_updated`: no.
- `core_updated`: sí, ES/EN coherentes. El efecto ES coincide exactamente con este texto aprobado.
- `knowledge_updated`: referencias/glosario y catálogo local actualizados; no doctrina mundial nueva ni concepto/ADR nuevo adicional a los neutralizadores.

## Validation

- `roll_integrity`: pass, T.E. Alquimia contra T.A. original; empate/fallo no neutralizan; no T.I. ni salvación adicional.
- `surface_integrity`: pass estático/semántico, efecto ES aprobado exacto, traducción y tarjeta alineadas; fuente/impresión idénticas. Overflow, tipografías e impresión visual pendientes, sin sortear restricción previa del navegador.
- `exchange_integrity`: pass de contrato de autoría, ventana antes de defensa y ataque/daño físico conservados; no prueba de motor.
- `ailment_integrity`: pass de contrato, una dosis externa sin cura interna, inmunidad o nuevos agravios.
- `critical_break_integrity`: not_applicable, sin ruptura ni desarme.
- `atb_integrity`: pass de registro, 3/1 y dosis incluso en fallo; un intento por practicante/ataque.
- `dependency_integrity`: pass para soporte inicial de Confusión y excepciones médicas explícitas; no compatibilidad universal ni fuentes sin calidad/dosis.
- `simulation_integrity`: blocked para ejecución, gap `new_subsystem` clasificado; ningún motor/dato sim nuevo.
- `balance_sanity`: pass doctrinal/provisional por comparables y límites; no equilibrio experimental validado.
- `loader_validation`: pass focal, campos/ID/coste/contrato comprobados. Validador global fail por los mismos 66 errores previos y 0 advertencias (143 registros centrales / 21 sim); ningún error nuevo de 167.
- `scenario_validation`: blocked, semillas descritas pero no escenarios runtime ejecutados.
- `question_validation`: blocked para ejecución; pregunta mínima y familias derivadas guardadas, no experimento runnable aún.
- `publication_consistency`: pass focal ES/EN/card/print. Escaneo de solo lectura: 307 archivos, 613 errores, 220 advertencias; dos avisos nuevos son falsos fallos de pareja por prefijo corebook-only del indexer. Las dos rutas reales existen y ambas entradas tienen cero errores/advertencias de contenido. No regenerar manifest para intentar arreglarlos.

Pruebas específicas: 26 pass (12 de 167 + 14 de productos), sin afirmar simulación. Preservación pass: los 142 registros y metadatos previos, los seis artículos previos de impresión y `pipeline/manifest.json` intactos. SHA-256 semántico previo a 167: `009047aaf0a0e02cfb03ebf3a37da6073da2d9c0e80992472ba96da3169136c7`. `git diff --check` sin errores en ambos repos y workspace.

## Acceptance closure

- `authority_updated`: sí.
- `yaml_updated`: sí, 167 authored.
- `sim_defined_or_gap_classified`: gap `new_subsystem` clasificado.
- `runtime_supported_or_gap_classified`: gap clasificado, runtime no implementado.
- `coverage_updated`: sí, README ES y catálogo Alquimia. Solo esa fila obsoleta se corrige a 127 + 167.
- `core_sync_done_or_not_needed`: sí, ES/EN y tarjeta/impresión; revisión visual pendiente.
- `pending_items_explicit`: sí.

## Pending items

- `pending`: revisión visual/impresión permitida, port de inventario/dosis/intercepción y equilibrio experimental. La traducción EN del capítulo de productos es deuda independiente; la técnica ES/EN sí está registrada. No extender compatibilidades ni asignar aprendizaje a personajes sin nueva decisión.

## Change impact

- `concepts_touched`: Alquimia, dosis, preparación externa, material compatible y fuente química de amenaza.
- `decisions_reinforced_or_created`: efecto completo aprobado e incorporado como 167; permiso externo de técnica separado del producto y de Medicina, sin cambiar alcance/coste/gasto ni conceder inmunidad.
- `coverage_movement`: nueva técnica Alquimia authored; hoja Bufoni de 7 tarjetas en dos páginas (6 + 1), sin modificar las anteriores.
- `follow_up_work`: detener esta incorporación con pendientes explícitos; no avanzar a otra técnica ni asignar aprendizaje a Seku automáticamente.
