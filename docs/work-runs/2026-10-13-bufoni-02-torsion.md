# Segunda técnica Bufoni — La fuerza prestada

## Header

- `work_id`: `2026-10-13-bufoni-02-torsion`
- `owner_workflow`: `technique-workflow`
- `linked_workflows`: `technique-play-surface-workflow`; simulación pendiente.
- `artifact_type`: `technique`
- `status`: `authored`; texto completo, nombre y coste aprobados por el creador el 2026-10-13. Sin cierre de balance ni aprobación visual.

## Scope

- `species`: Bufoni como origen cultural, no requisito.
- `technique_id`: 163; sigue al máximo publicado y central 162, sin reutilizar un ID.
- `goal`: formalizar la segunda técnica aprobada, una por vez.
- `current_state`: entrada ES, pareja EN, tarjeta, hoja de impresión, YAML y referencia humana incorporadas.
- `out_of_scope`: técnicas adicionales, reparación de registros antiguos, reglas de veneno, personajes, portado de simulación, motor narrativo y concesión a Seku.

## Mandatory sources

- Autoridad: `Transcendence-design/docs/system/techniques.md`, `weapon-technique-profiles.md`, `technique-la-fuerza-prestada.md` y datos centrales de técnicas/perfiles.
- Identidad: capítulo 6 ES, `14-bufoni.md`; canon de diseño como contexto complementario. No existe un archivo de semillas Bufoni; no se simula haber completado ese pase.
- Técnicas de Torsión publicadas: 5, 75, 79 y 138; comparaciones cruzadas 9, 12, 27, 37, 108, 111, 114, 141, 146 y 154.
- Nueve armas naturales con Torsión revisadas antes del diseño; efectos relevantes resumidos abajo.
- Guías: workflows de ejecución, técnicas, presentación y estabilización de costes; tabla maestra, template de ficha; skills de autoría y presentación.
- Publicación: estilo, glosario, modos de texto, muestras de voz, checklist editorial, estilo visual, hechos del mundo y template del capítulo.
- Simulación inspeccionada: `Transcendence-design/sim/engine/reactions.py` y `activations.py`.
- El catálogo por superficie conserva discrepancias anteriores; no sustituye la lectura del conjunto publicado. Su conciliación global está fuera de alcance.

## Phase checkpoints

### Phase 0. Intake

- `scope_recorded`: sí; una técnica por vez.
- `main_question`: aprovechar la fuerza de un ataque físico cercano para cambiar su destinatario.
- El creador aprobó alcance, oposición, conservación del golpe, límites, coste 3/1 y después nombre y entrada completa.

### Phase 1. Species Framing

- `fantasy`: sobrevivir a fuerza hostil mediante contacto flexible y proximidad, sin absorber el golpe ni igualar esa fuerza.
- `world_origin`: práctica Bufoni; sin fijar dominio, linaje, escuela, maestro o disponibilidad.
- `why_not_base_action`: permite redirigir un ataque ya declarado, incluso contra otra criatura, sin producir un contraataque propio.
- `interaction_surfaces`: `timing_atb`, `targeting_geometry`.
- No requiere lengua, veneno, anatomía Bufoni ni Tauma. Un arma fabricada compatible puede dar acceso.
- Descartado durante la discusión: restricción vocal, porque no existen componentes verbales y no resolvía una necesidad mecánica suficiente.
- Retirado: limitar la intervención a ataques contra el practicante o medirla exclusivamente hasta el cuerpo del agresor.

### Phase 2. Mechanical Framing

- `category`: utilidad reactiva; rango Novato con el arma.
- `roll_model`: T.A. de Torsión > T.A. del agresor. Empate o inferior no redirigen.
- `competency_source`: competencia del arma con perfil Torsión.
- `effect_model`: cambia el destinatario de un solo ataque físico, antes de su defensa. Contacto con arma/extremidad atacante dentro del alcance del arma del practicante; nuevo destinatario en una trayectoria válida del mismo ataque.
- Sin proyectiles, áreas, aumento del alcance original ni paso a través de obstáculos.
- Con fracaso, el destinatario original conserva su defensa habitual.
- Con éxito, conservar el dado del agresor y recalcular solo modificadores dependientes del nuevo destinatario; enfrentar esa T.A. a su T.D.
- Si conecta, impacto y efectos del contacto del agresor frente a la protección real, con requisitos, márgenes y resistencias comprobados contra quien recibe el golpe.
- Sin impacto ni efectos del arma del practicante. No añadir Hereda Efectos a esta utilidad.
- `duration_model`: Instantáneo; no estado persistente.
- `restrictions`: un golpe por uso, no secuencia completa, movimientos ni ataques adicionales; un intento por practicante/ataque; un ataque redirigido con esta técnica no admite otra redirección por ella. El nuevo destinatario conserva otras reacciones permitidas.
- Ritmo 3 / Desgaste 1, también al fallar.
- No añadir exclusiones del practicante/agresor como destinatarios: gobierna la legalidad física del ataque original.

### Phase 3. Dependency Framing

- `upstream_dependencies`: alcance del contacto, geometría del ataque original, ventana previa a defensa, dado de T.A. reutilizable, modificadores dependientes del destinatario, efectos y protección del destinatario real, permisos de reacción.
- `downstream_dependencies`: core ES/EN, tarjeta, hoja de impresión, YAML y referencia humana.
- `blockers`: no bloquea la autoría; soporte de simulación y revisión visual no completados.
- No introducir nuevos agravios ni inventar metadatos de técnicas antiguas.

### Phase 4. Balance Framing

- `cost_sanity_note`: 3/1 aprobado como punto de partida, no balance probado. Intervención rápida acotada sin impacto propio ni persistencia, pero puede proteger al destinatario original y aprovechar un golpe enemigo poderoso.
- `sibling_comparison_note`: Torsión publicada detiene retirada con daño (5), reposiciona con daño (75), desarma sin daño (79) y Desequilibrado con daño (138).
- 27 Levantar el Dique, 4/1, transfiere recepción a ti; 146 El Plano Interpuesto, 3/1, cancela contra un aliado; 154 Invertir la Carga, 3/1, cancela y desplaza. 12 y 141 cancelan y contraatacan. Comparación conceptual, no prueba de exclusividad o balance.
- 9 ya modifica trayectorias/cobertura; 37 y 108 restringen con Atrapado; 111 y 114 preservan Oculto. No presentar esas salidas como huecos nuevos.
- `pressure_note`: frecuencia del tercero legal, fuerza/efectos del ataque ajeno, intervenciones sucesivas y protección original incluso si el nuevo destinatario defiende con éxito.
- `counterplay_note`: oposición de T.A., negar contacto, ausencia de trayectoria alternativa y defensa del nuevo destinatario.

Precomprobación de armas naturales con Torsión:

| Arma | Efecto natural relevante |
| --- | --- |
| Cola Naghii | Margen 3 y T.R. fallida: Desorientado. |
| Garras Zarnag | Margen 3 y T.R. fallida: Lacerado. |
| Mordisco Drak'kai | Impacto crítico: Aterrorizado sin T.R. |
| Garras Drak'kai | Margen 3: desplazamiento forzado. |
| Mordisco Formix | Margen 3 y T.R. fallida: Confundido. |
| Trompa Loxod | Margen 3 y T.R. fallida: Desequilibrado. |
| Garras Chelicer | Margen 3 y T.R. fallida: Sobrecargado. |
| Lengua Bufoni | T.A. superior a T.D. y T.R. fallida: veneno de linaje. |
| Mordisco Yacani | Margen 3: penalización a T.D. hasta fin de próxima activación. |

La utilidad no hereda esos efectos del practicante; los del agresor sí siguen las condiciones de su contacto real. Tener Torsión no convierte cualquier trayectoria en redirigible.

### Phase 5. Simulation Framing

- `runtime_gap_classification`: `small_runtime_extension`, estimación de portado, no soporte implementado.
- `porting_state_target`: alcanzado `authored`; no `sim_defined`, `runtime_supported` ni `question_ready`.
- Evidencia: `reactions.py` selecciona una reacción defensiva del destinatario y devuelve bono/costes. `activations.py` fija el destinatario antes del intercambio y omite el hook defensivo cuando el intento entrante es reactivo.
- Se necesitan intervención por terceros antes de defensa, geometría explícita, dado preservado/modificadores del nuevo destinatario, resolución de payload contra quien lo recibe, costes al fallar, guardas por practicante/ataque y contra redirecciones sucesivas. Admitir ataques entrantes reactivos válidos, no solo activos.
- El objeto YAML `attack_redirection` es un contrato declarativo, no un handler ejecutable.
- `scenario_seed_note`: éxito/fallo/empate; protección propia/tercero; cuerpo del agresor fuera de alcance pero contacto alcanzable; trayectorias inválidas/obstáculos; proyectiles/áreas; cambio de modificadores; nueva defensa exitosa/fallida; efecto original y sus márgenes/T.R.; no efectos propios; secuencias pagadas por golpe; intentos reiterados, cadenas de éxito y otras reacciones permitidas.
- `question_seed_note`: comparar 3/1 con 2/1 y 4/1 frente a 146 y 27, controlando oportunidades, defensa original preservada, daño realmente redirigido, efectos, reiteración y costes. Semilla guardada, no pregunta ejecutable ni resultado.

### Phase 6. Editorial Framing

- `authority_cleanup_note`: incorporación del registro 163; sin reescribir los 138 registros anteriores ni reparar sus metadatos.
- `terminology_note`: nombre aprobado registrado en el glosario; pareja EN Borrowed Force. No se cambia ninguna definición canónica previa.
- `core_sync_note`: entrada completa ES aprobada, traducción EN y ejemplo de resolución. `status: draft`, `canonical: false`.
- Tarjeta condensada sin nuevas condiciones; misma pieza en impresión. Espaciado local, sin cambiar tamaño de carta ni tipografía compartida.
- Revisión visual pendiente: el navegador rechazó el acceso local previamente. No intentar otro navegador, servidor local ni un mecanismo alternativo para sortear esa restricción. La comprobación estática no certifica ausencia de desbordamiento.

## Integration

- `files_changed`: core ES/EN 163; tarjeta Bufoni/impresión; YAML central; referencia humana y documento central; catálogo de superficie; README ES; glosario; esta ficha.
- `sim_updated`: no.
- `core_updated`: sí.
- `knowledge_updated`: término aprobado y referencias humanas; no nuevas escuelas ni biografías.
- No se concede la técnica a Seku ni se modifica otro personaje.

## Validation

- `roll_integrity`, `exchange_integrity`, `atb_integrity`, `dependency_integrity`: revisión documental de oposición, dado, efectos, ventana, alcance y costes; no prueba de runtime.
- `surface_integrity`: `pass` estático: HTML equilibrado, IDs SVG únicos, iconos/CSS referenciados existentes, artículo idéntico entre tarjeta e impresión y dos tarjetas anteriores conservadas literalmente. Revisión visual pendiente.
- `loader_validation`: YAML carga; validador global devuelve los mismos 66 errores previos y 0 advertencias, sobre 139 registros centrales y 21 de simulación. No son errores del nuevo registro.
- `publication_consistency`: `pass` enfocado: efecto ES coincide con el texto aprobado, datos y cabeceras ES/EN concuerdan, pareja bilingüe y todas las referencias existen. Revisión manual de la traducción; no se afirma equivalencia semántica probada por un motor.
- Conservación central: al excluir el nuevo registro 163, el SHA-256 semántico es `22646c6a7f90089a51f59bafcd14f527c7e6f668f995ecd44132ad77043f6119`, idéntico al previo: 138 registros y metadatos anteriores sin cambios. ID 163 único.
- Indexador editorial: 299 archivos, 32 sin frontmatter, 606 errores y 221 advertencias frente a 605 errores antes. La entrada ES nueva añade un falso positivo de pareja bilingüe: `validate_frontmatter` exige que el enlace empiece por `core-books/transcendence-corebook/`, excluyendo `core-books/transcendence-techniques/`. ES enlaza a su EN real y EN a su ES real; la comprobación enfocada confirma ambos. No se reparó el indexador ni se añadió una referencia ficticia para forzar su aprobación. El resto de validaciones de ambos archivos no da errores ni advertencias. Se usó `--search`, sin escribir el manifiesto.
- `ailment_integrity`, `critical_break_integrity`: no se crea agravio ni ruptura; efectos originales del agresor quedan sujetos a sus requisitos y protección real.
- `balance_sanity`, `simulation_integrity`, `scenario_validation`, `question_validation`: pendientes; sin runtime ni experimentos ejecutados.

## Acceptance closure

- `authority_updated`, `yaml_updated`, `core_sync_done_or_not_needed`: sí.
- `sim_defined_or_gap_classified`, `runtime_supported_or_gap_classified`: gap clasificado, no soporte.
- `coverage_updated`: no; no crear cobertura ficticia.
- `pending_items_explicit`: sí. Autoría aprobada no significa técnica probada ni lista para impresión.

## Pending items

- Revisión visual permitida de tarjeta e impresión.
- Portado, escenarios y comparación de costes.
- Conciliación del catálogo histórico por superficie y metadatos antiguos, fuera de este alcance.
- Corregir el criterio de pareja bilingüe del indexador en un trabajo de pipeline, no como cambio oculto de esta técnica.

## Change impact

- `concepts_touched`: intervención física de Torsión sobre un ataque existente.
- `decisions_reinforced_or_created`: origen no equivale a requisito racial; el contacto, no la posición corporal del agresor, acota la intervención; no asignación automática a Seku.
- `coverage_movement`: ninguno.
- `follow_up_work`: revisar esta técnica antes de abrir otra.

## Entrada completa aprobada

Registro del texto aprobado por el creador, no autoridad paralela. La entrada mantenida para lectura está en el core ES 163. La utilidad no tiene impacto propio; los efectos conservados pertenecen al agresor.

## La fuerza prestada

### Reactivo - Utilidad

**Rango Novato**

*El golpe encuentra otra carne.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | — | 3 | 1 |

### Requisitos

- Competencia Novato o superior con el arma utilizada.
- Arma con perfil Torsión.

### Palabras clave

- Torsión

### Efecto

Cuando se declare un ataque físico contra una sola criatura, puedes intervenir antes de resolver su defensa si tu arma puede alcanzar el arma o extremidad atacante en el punto de contacto que vas a alterar. Puedes intervenir aunque el ataque no vaya dirigido contra ti. Esta técnica no puede redirigir proyectiles ni ataques de área.

Elige otra criatura que ese mismo ataque pueda alcanzar mediante una trayectoria físicamente válida, sin aumentar su alcance ni atravesar obstáculos. Realiza una T.A. con tu arma de Torsión, enfrentada a la T.A. del agresor.

Si tu T.A. no supera la del agresor, el ataque continúa contra su destinatario original, que conserva su defensa habitual.

Si la superas, el ataque se dirige contra la criatura elegida. El agresor conserva el resultado del dado de su T.A. y ajusta únicamente los modificadores que dependan del nuevo destinatario. Esa T.A. se enfrenta a la T.D. de la criatura elegida.

Si el ataque conecta, el agresor resuelve su impacto y los efectos propios del contacto contra la protección del nuevo destinatario. Sus requisitos, márgenes y resistencias se comprueban contra esa criatura. No añades impacto ni efectos de tu propia arma.

Cada uso afecta un solo ataque, no toda una secuencia ni sus movimientos o ataques adicionales. Puedes intentar esta técnica una vez contra cada ataque. Un ataque ya redirigido mediante esta misma técnica no puede volver a redirigirse con ella. El nuevo destinatario conserva sus otras reacciones permitidas.

Pagas Ritmo y Desgaste aunque la intervención falle.
