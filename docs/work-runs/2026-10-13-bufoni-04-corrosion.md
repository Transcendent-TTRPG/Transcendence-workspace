# Cuarta técnica Bufoni — Corrosión, discusión de intención

## Header

- `work_id`: `2026-10-13-bufoni-04-corrosion`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`: technique-play-surface-workflow; revisión de dependencias de aplicación/retirada; portado de simulación diferido.
- `artifact_type`: `technique`
- `status`: `authored`; entrada aprobada e integrada; simulación, balance experimental y revisión visual pendientes.

## Scope

- `species`: Bufoni como origen cultural, no requisito racial.
- `technique_id`: 165; nombre ES La mancha que vuelve, EN The Returning Stain.
- `goal`: discutir una sola técnica del siguiente perfil, después de 162–164.
- `current_state`: el creador aprueba la entrada completa («sí, está muy bien»). Core ES/EN, tarjeta y plancha, YAML, referencia humana, catálogo, glosario y README integrados. Comprobaciones locales aprobadas; no afirmar soporte runtime ni cierre experimental.
- `out_of_scope`: cambios globales a venenos o técnicas anteriores, portado de simulación, personajes y concesiones a Seku.

## Mandatory sources

- authority docs/data: definición de Corrosion en `weapon-technique-profiles.md`/`.yaml`; registros de ese perfil en `techniques.yaml`; familia Poison y vías de administración en `ailments.yaml`.
- seeds/canon: capítulo 6 ES `14-bufoni.md`, como identidad principal; canon de diseño del pase como contexto complementario. No existe semilla Bufoni separada; no inventar escuelas o doctrinas confirmadas.
- knowledge references: workflows de ejecución, técnicas y presentación; template de ficha; skills de autoría/presentación, routing y checkpoints del pase.
- simulation references: no portado ni inspección para esta dirección conceptual.
- publication references: Corrosión publicada 8, 52 y 140, contrastada con sus variantes YAML; comparación funcional cruzada con 7, 106, 110, 128 y técnicas previas del pase; capítulo 11 ES, Venenos completo.

## Phase checkpoints

### Revisión de intención — 2026-10-14

- Propuesta ambiental descartada expresamente por el creador: «eso suena más como a una trampa, porque ni siquiera se hace como en combate».
- Dirección sustitutiva aceptada: «sí, es una reacción específicamente hacia eso, está interesante». El acuerdo cubre intención y momento, no un mecanismo completo.
- Propuesta mecánica pendiente: declarar la reacción durante la limpieza, resolver esa limpieza normalmente y después intentar una nueva aplicación sobre la misma criatura, dentro del mismo intercambio. No cancelar genéricamente Interactuar ni dejar una promesa para una acción posterior.
- Acuerdo posterior del creador: «sí me parece bien» a la separación entre residuos externos y afecciones internas y al procedimiento presentado de limpieza normal, T.A./T.D., fuente material conocida, requisitos/resistencias originales, sin daño ni agravamiento/acumulación. Las precisiones siguientes todavía se proponen, no se presumen aprobadas.
- Acuerdo final del creador: «sí» a La mancha que vuelve, Novato, Ritmo 3/Desgaste 2, limpieza por aliados sin cambiar el blanco, ajustes/resistencias originales, cobro de esta reacción sin duplicar la activación de origen y una intervención por acción de limpieza. Autoriza preparar la entrada completa para revisar, no supone aprobación anticipada de su redacción.
- Revisión de redacción cerrada por el creador: «sí, está muy bien» a la entrada completa presentada. Integración de autoría el 2026-10-14, sin asignación a personajes ni portado runtime.

### Phase 0. Intake

- `scope_recorded`: una por vez; primero discusión.
- `main_question`: expresar el conocimiento químico y territorial Bufoni sin repetir obstrucción sensorial, negación de tratamiento o deterioro defensivo.
- Acceso del pase: lengua con Torsión, Interrupción, Impredecible y Corrosión; armadura/resistencias entrenadas no fijadas. No atribuir universalmente Sigilo/Nadar/Saltar como competencias por tener un legado asociado.

### Phase 1. Species Framing

- `fantasy`: observar el intento enemigo de librarse de una sustancia para volver a aplicarla durante esa intervención de combate.
- `world_origin`: conocimiento empírico de secreciones y de las respuestas de una criatura a la contaminación; paciencia y lectura del momento, no exclusivamente infiltración.
- Biología como punto de partida, no requisito: el método debe poder usarse con arma fabricada y un agente real compatible. No exigir el efecto intrínseco de Lengua ni entregar automáticamente el veneno del linaje.
- `why_not_base_action`: permiso reactivo acotado a la retirada de un residuo externo; no requiere esperar a la activación propia para una nueva aplicación. No concede aplicación gratuita ni garantiza contacto.
- `interaction_surfaces`: limpieza declarada, residuo químico externo, alcance del arma, aplicación material nueva, defensa y consecuencias de la sustancia.
- No Tauma, corrosión mágica, veneno creado de la nada, inmunidad aliada, detección negada ni anulación de Piel Permeable.

### Phase 2. Mechanical Framing

- `category`: Reactivo - Utilidad, perfil Corrosión; sin T.I. ni herencia de efectos naturales. Palabras clave omite Hereda/No Hereda por ser utilidad.
- `roll_model`: T.A. contra T.D. de la criatura que tenía el residuo, después de resolver la limpieza; conservar penalizadores específicos de la aplicación original y cualquier T.R. correspondiente. Empate/fallo no reaplica. No usar la contaminación ya retirada para penalizar esta defensa.
- `competency_source`: arma con Corrosión, Novato o superior, material disponible y procedimiento conocido. Si el efecto procede de una técnica, el practicante debe conocerla y cumplir sus requisitos; no copiar capacidades de otra criatura.
- `effect_model`: nueva aplicación del mismo residuo químico externo sobre la misma criatura y punto, sin reejecutar daños u otros resultados de la técnica de origen. La limpieza original conserva costes y resultados; fallo de la reacción no deshace la limpieza. Si la limpieza falla, no duplica la penalización existente ni empeora automáticamente severidad.
- `duration_model`: reacción inmediata; persistencia del residuo renovado y retirada según su definición original. No crear duración propia ni hacer el residuo imposible de limpiar.
- `restrictions`: solo retirada deliberada de un residuo químico externo con reglas de aplicación/retirada definidas; excluir tratamiento de veneno interno, infección, lesión, reparación de daño material y eliminación ambiental pasiva. No cualquier Alteración, no dosis infinitas ni transferencia automática de efectos naturales; un intento por practicante/acción de retirada, no cadena a la reaplicación.

### Phase 3. Dependency Framing

- `upstream_dependencies`: agente/procedimiento de aplicación y retirada definidos; requisitos originales (incluidos kits y manejo seguro cuando corresponda), exposición real y T.R. si existe, material disponible, persistencia externa y competencia del practicante. Kit de Venenos no se impone universalmente a residuos que usan otro kit. No asumir fórmula, ruta o cantidad de dosis inexistentes.
- El marco general admite inoculación, ingestión, inhalación y contacto; los cinco Venenos del catálogo ES consultado y sus registros estructurados requieren inoculación. Entorpecido/Escaldado/Erosionado/Saturado/Inhibido no se vuelven automáticamente venenos cutáneos por esta técnica.
- Usar un agente de contacto requeriría una definición compatible previa o una ampliación acotada revisada expresamente; no introducirla en silencio.
- `downstream_dependencies`: futuras entrada ES/EN, tarjeta, YAML, referencia humana y, si se necesita, definición reutilizable de residuo/exposición; solamente después de aprobación.
- `blockers`: no impide registrar el permiso de autoría, que hereda procedimientos definidos en vez de crear un catálogo químico. Nublar la Señal ofrece un caso publicado concreto. Aplicaciones futuras sin definición material/exposición/retirada no se presumen compatibles; 52/140 no se reparan ni se admiten automáticamente.
- `linked_files`: fuentes anteriores, sin modificación.

### Phase 4. Balance Framing

- `cost_sanity_note`: doctrina y tabla maestra completas leídas. `Ritmo 3 / Desgaste 2`, Novato, aprobado para autoría. Ritmo por una intervención física breve con timing estrecho y sin daño; Desgaste por renovar una degradación que puede afectar múltiples intercambios, no por la palabra Permanente. Comparación principal 8 (`4/2`), secundaria 162 (`4/1`, cancelación sin residuo) y 164 (`2/1`, intervención informativa estrecha). No se afirma balance experimental probado.
- `sibling_comparison_note`:
  - 8 Nublar la Señal, Naghii: aplicación precisa a canal sensorial; residuo que degrada ese canal y se limpia mediante Interactuar/entorno. Versión publicada y YAML difieren en extensión/alteraciones; ambas revisadas.
  - 52 Ensuciar la Herida, Zarnag: impacto que dificulta Medicina hasta preparar/limpiar la herida. Variante estructurada describe contacto sucio, no nueva infección automática.
  - 140 La Capa Que Cede, Vesper: impacto más reducción de defensa por residuo. El YAML incluye retirada mediante Interactuar/fin de encuentro, que la prosa omite; no asumir otra técnica idéntica para cubrir esa discrepancia.
- Cruce funcional: 7 ya marca y rastrea; 106 entrega veneno reactivo mediante aguijón y recepción de golpe; 110 crea una red territorial que detecta/atrapa; 128 lee contaminación y mejora resistencia. No usar sus salidas como novedad ni disfrazar una trampa completa de Corrosión.
- `pressure_note`: puede presionar repetidamente la limpieza, pero cada intento necesita alcance, material, coste y una aplicación acertada. Proponer una intervención por practicante y acción de limpieza, sin cadena reactiva a la propia reaplicación. Pendiente de acuerdo y coste.
- `counterplay_note`: defenderse de la aplicación, salir del alcance antes de limpiar, retirar el agente mediante el entorno o neutralizarlo según su regla; precisar limpieza por un aliado sin cambiar el blanco de la nueva aplicación.

Precomprobación de armas naturales con Corrosión:

| Arma | Disparador y efecto |
| --- | --- |
| Kha-Naghii Mordisco | Margen 3 y T.R. Veneno fallida: reducción de Tenacidad. |
| Saa-Naghii Aliento Astral | T.R. Veneno fallida por 3 o más: daño recurrente. |
| Zarnag Mordisco | Margen 3 y T.R. Infecciones fallida: infección que aumenta Ritmo. |
| Chelicer Aguijón | Margen 3 y T.R. Veneno fallida: reducción de Agilidad. |
| Arakhel Mordisco | Margen 3 y T.R. Veneno fallida: Paralizado. |
| Bufoni Lengua | T.A. > T.D. y T.R. Veneno fallida: veneno del linaje. |
| Soricin Colmillos Surcados | Margen 3 y T.R. Venenos fallida: Entorpecido. |
| Yacani Bilis | T.A. > T.D. y T.R. Veneno fallida: Erosionado. |

El residuo no hereda indiscriminadamente estos efectos ni sus vías. Hereda Efectos se decidirá tras fijar categoría/impacto: utilidad omite etiqueta; ataque sin T.I. usa No Hereda Efectos; un impacto completo exige revisar todas las combinaciones.

### Phase 5. Simulation Framing

- `runtime_gap_classification`: `new_state_family`, por residuo externo tipado y procedencia/material/punto/procedimiento; además requiere una ventana reactiva ordenada de retirada y reaplicación. El soporte procedural genérico y su variante antigua de 8 no implementan este contrato publicado.
- `porting_state_target`: registro de diseño `authored`; sin datos, handler, políticas ni coverage de simulación nuevos.
- `scenario_seed_note`: limpieza propia/por aliado, limpieza exitosa/fallida, contacto acertado/fallido/empate, nueva defensa sin el residuo retirado, restricciones de la aplicación original, T.R. cuando corresponde, dosis agotada, fuera de alcance, retirada ambiental y tratamiento interno excluidos, intento repetido sin acumulación.
- `question_seed_note`: pendiente de efecto/coste. Comparar permiso reactivo con la aplicación activa correspondiente y examinar si una secuencia de limpieza/reaplicación deja contrajuego real. Guardar pregunta mínima de coste antes de afirmar balance.

Pregunta mínima de coste guardada para el borrador (sin ejecución ni portado):

- ¿A `3/2`, comparado con `4/2`, la renovación reactiva de Nublar la Señal puede hacer que limpiar dentro del alcance sea sistemáticamente inútil, o conservan valor la nueva T.D., el penalizador de aplicación, la disponibilidad de dosis y el coste ATB del practicante? Comparar con volver a aplicar activamente el residuo y con limpiar fuera del alcance; incluir acierto, fallo y empate. Revisar por separado efectos residuales futuros antes de asumir que este coste sirve para todos.

### Precisiones aceptadas — entrada pendiente de revisión

- Nombre aprobado: **La mancha que vuelve**, ID 165.
- Cobro aprobado: pagar esta reacción, no además la activación completa de la técnica de origen; esa fuente aporta el procedimiento residual y sus requisitos, no una segunda técnica con todos sus resultados.
- Novato, Reactivo - Utilidad, Corrosión; alcance del arma, una criatura, resolución instantánea, T.A., sin T.I. La persistencia pertenece al residuo de origen, no a una nueva Postura.
- Declaración antes de que se resuelva una retirada deliberada. Una intervención por practicante y acción de retirada; no reaccionar a la propia reaplicación.
- Si un aliado limpia, el blanco sigue siendo la criatura sobre la que estaba el residuo, y debe poder alcanzarse con el arma en el momento de la nueva aplicación.
- Seleccionar el mismo residuo químico externo que se intenta quitar; conocer su procedimiento y disponer de sustancia, dosis, arma y kits que ese procedimiento exige. Conocer una técnica no permite copiar un residuo de otra naturaleza ni sus daños/resultados ajenos a la aplicación externa.
- Resolver la retirada y luego la aplicación con las condiciones actuales. No usar las penalizaciones de un residuo eliminado contra esta nueva defensa. Conservar los ajustes específicos de la aplicación (por ejemplo, el −2 de Nublar la Señal), T.R. y severidad de su procedimiento de origen; esta reacción no aporta una gravedad por separado.
- Empate/fallo de T.A. no reaplica. Una aplicación acertada sigue siendo resistible cuando la sustancia lo exige. No acumular capas/penalizaciones si el residuo anterior no se retiró; no empeorar automáticamente gravedad.
- Consumo y fallo material según el procedimiento original, no recuperar la dosis retirada ni inventar consumo universal todavía ausente. Ambos participantes conservan los costes de sus acciones.
- Caso admisible concreto verificado: residuo sensorial de 8. No dar por admitidas 52 (tejidos destrozados) ni 140 (prosa ES sin residuo/retirada explícitos); no corregir esas fuentes en este run.

### Entrada completa aprobada — copia de la revisión

#### La mancha que vuelve

**Reactivo - Utilidad · Rango Novato**

*La piel apenas alcanza a quedar limpia.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | — | 3 | 2 |

**Requisitos**

- Competencia Novato o superior con el arma utilizada.
- Arma con perfil Corrosión.
- Procedimiento conocido de aplicación del residuo, con sus requisitos y material disponible para una nueva aplicación. Si procede de una técnica, debes conocerla.

**Palabras clave:** Corrosión.

**Efecto**

Cuando una criatura declare una acción para retirar un residuo químico externo de un objetivo dentro del alcance de tu arma, puedes declarar esta técnica antes de que esa acción se resuelva. El objetivo puede limpiarse o recibir ayuda de otra criatura.

Resuelve primero la retirada normalmente. Después realiza una T.A. contra la T.D. del objetivo para volver a aplicar el mismo residuo sobre el mismo punto afectado. Debes poder alcanzarlo y cumplir los requisitos de aplicación en ese momento. Conserva los modificadores específicos del procedimiento original; un residuo ya retirado no penaliza esta nueva defensa.

Si tu T.A. no supera su T.D., no reaplicas el residuo. Si la supera, resuelve la nueva aplicación con las resistencias y efectos residuales del procedimiento original. Su severidad, persistencia, consumo y retirada se rigen por ese procedimiento; no copias la competencia de quien realizó la aplicación anterior.

Esta técnica no inflige daño ni aplica el efecto del arma. Si el residuo anterior permanece, no acumulas sus penalizaciones ni aumentas automáticamente su severidad. Pagas el coste de esta reacción, no además la activación de la técnica de origen. La acción de retirada conserva sus costes y resultado aunque falles al reaplicar.

Solo puedes intentar esta técnica una vez por acción de retirada. No puedes utilizarla contra tratamientos de venenos internos, infecciones o heridas, reparaciones de daño material ni retiradas causadas únicamente por el entorno.

**Ejemplo**

Conoces Nublar la Señal y dispones de su Kit de Munición y material para otra aplicación. Un enemigo intenta limpiar el residuo de su canal visual mediante Interactuar. Declaras La mancha que vuelve y resuelves primero su limpieza. Después haces tu T.A. con el penalizador de −2 que exige Nublar la Señal. Si superas su T.D., aplicas de nuevo el residuo sobre ese canal con la severidad correspondiente a tu propia competencia. Si empatas o fallas, no reaplicas nada. Si su limpieza retiró el residuo, ya no está Cegado por esa aplicación anterior al defenderse.

Nota de revisión: Instantáneo describe el permiso reactivo y su resolución inmediata; el residuo conserva su duración original. Salvación no fija una T.R. universal porque depende del procedimiento de aplicación. La T.D. enfrentada queda explícita en el efecto, como en 162–164.

### Phase 6. Editorial Framing

- `authority_cleanup_note`: ID 165 añadido; los 140 registros previos y los demás metadatos YAML se conservan semánticamente. Ninguna regla global de venenos, técnica anterior o simulación se modifica.
- `terminology_note`: nombre aprobado registrado ES/EN en glosario; no nuevo estado de juego. Contacto diferido/peligro localizado se descartan como intención de esta técnica.
- `core_sync_note`: Core ES idéntico a la entrada aprobada, par EN con la misma regla y ejemplo; tarjeta condensada sin cambiar sus requisitos ni resultados. Plancha incorpora la quinta tarjeta Bufoni y conserva las cuatro anteriores.

## Integration

- `files_changed`: esta ficha; Core ES/EN 165; tarjeta individual y plancha Bufoni; `data/system/techniques.yaml`; `docs/system/technique-la-mancha-que-vuelve.md`, `techniques.md` y `technique-surface-catalog.md`; glosario y README ES.
- `generated_index_note`: `pipeline/manifest.json` ya estaba modificado antes del pase. El comando editorial `--validate` lo regeneró automáticamente con los archivos nuevos (303 archivos, 609 errores, 221 advertencias); se informó al creador. No restaurar desde HEAD ni sobrescribir cambios previos para ocultarlo. No reparación del indexer en este pase.
- `sim_updated`: no. `core_updated`: sí. `knowledge_updated`: no registro adicional en knowledge; glosario/referencias de técnicas actualizados.

## Validation

- `roll_integrity`, `exchange_integrity`, `ailment_integrity`, `atb_integrity`, `dependency_integrity`: `pass` de definición/consistencia estática, no ejecución de combate. T.A./T.D. estrictas, procedimiento/resistencias originales, sin impacto ni cambio de administración, costes y orden de retirada conservados.
- `surface_integrity`, `publication_consistency`: `pass` de texto y estructura; ES coincide con lo aprobado, par EN coherente, tarjeta/plancha idénticas, referencias reales y campos numéricos correctos. Revisión visual de overflow, fuentes e impresión `blocked`, sin eludir la denegación previa de navegación local.
- `critical_break_integrity`: `not_applicable`, sin daño ni ruptura.
- `loader_validation`: `pass` de YAML central/campos requeridos/ID único; no implica carga o soporte en simulador.
- `balance_sanity`: `pass` provisional de comparación y pregunta mínima guardada; no cierre experimental.
- `simulation_integrity`, `scenario_validation`, `question_validation`: `blocked` para ejecución; contrato/gap y semillas definidos, sin portado ni experimento.
- Conservación: excluyendo 165, SHA-256 semántico del YAML completo coincide con el previo: `d736620c81eee430e1312b5821341b65f67b7d9489c78bfe4432e943c031c031`. Las cuatro tarjetas previas en plancha conservan sus hashes byte por byte.
- Validador global de técnicas: 141 registros centrales/21 sim, mismos 66 errores previos y cero advertencias; ningún error nuevo para 165. No declarar pase global.
- Indexer editorial: 607 → 609 errores; los dos añadidos corresponden al requisito de par bilingüe limitado erróneamente a `transcendence-corebook`. Los pares reales ES/EN de 165 existen en `transcendence-techniques`; sus contenidos pasan sin avisos. No enlaces ficticios ni cambio global del pipeline.
- No-solapamiento y precheck natural completados; comparación final documentada en la referencia humana.

## Acceptance closure

- `authority_updated`, `yaml_updated`: sí. `coverage_updated`: catálogo de superficies sí, coverage runtime no.
- `sim_defined_or_gap_classified`, `runtime_supported_or_gap_classified`: sí, gap `new_state_family` documentado; no soporte declarado.
- `core_sync_done_or_not_needed`: sí.
- `pending_items_explicit`: sí; incorporación de autoría terminada, simulación/balance experimental/visual pendientes.

## Pending items

- `pending`: portado del contrato publicado y de la fuente residual concreta antes de ejecutar preguntas/escenarios; balance experimental; revisión visual autorizada de tarjeta/plancha. Discrepancias previas de 8/52/140, errores globales de metadata e indexer fuera de alcance. No asignar a Seku ni iniciar automáticamente otra técnica.

## Change impact

- `concepts_touched`: residuos químicos externos, limpieza y permiso de reaplicación reactiva desde la perspectiva Bufoni.
- `decisions_reinforced_or_created`: permiso reactivo de 165 registrado, alcance externo/material/procedimental explícito; especie como origen, no requisito; veneno no cambia de vía porque el perfil lo sugiera; una técnica por vez.
- `coverage_movement`: Corrosión pasa de 3 a 4 técnicas en el catálogo; ninguna cobertura de simulación nueva.
- `follow_up_work`: elegir con el creador el siguiente paso; no desarrollar la trampa descartada, asignar nada a Seku ni abrir otra técnica automáticamente.
