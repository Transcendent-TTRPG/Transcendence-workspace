# Tabla Maestra — Costos de Técnicas

`2026-06-04` · actualizado `2026-07-09` · estado: `cerrado — 02–117 revalidadas`

## Propósito

Registro de referencia de los costos validados para las técnicas 02–117.
Cada fila representa un veredicto cerrado bajo la doctrina vigente.

Para la doctrina completa, bandas de referencia, y preguntas de arbitraje, ver:
`docs/workflows/technique-cost-stabilization.md`

## Marco de costos

- **`Ritmo`** = tiempo: cuánto avanza la ficha del usuario en el track ATB al ejecutar la técnica. Ritmo 0 cuando la técnica no tiene manifestación externa, movimiento, ni requisito de timing — un snap cognitivo o reactivo puramente interno. Ritmo > 0 cuando la ejecución requiere acción física, timing, o atención que desplaza la posición del usuario en el intercambio.
- **`Desgaste`** = esfuerzo: acumulación permanente de desgaste entre escenas. `Desgaste 0` solo para técnicas pasivas que el cuerpo ejecuta sin activación consciente. `Desgaste 1` = una superficie principal bien definida. `Desgaste 2` = dos ejes relevantes independientes. `Desgaste 3+` = sobreextensión real.
- Las acciones base son el piso ineficiente, no el benchmark de optimización.
- `Permanente` no es recargo por sí mismo — se cobra la cobertura efectiva y los intercambios alterados.

## Etiquetas

- `pendiente`: aún no revalidada en clean run
- `revisar R`: el principal sospechoso es `Ritmo`
- `revisar A`: el principal sospechoso es `Desgaste`
- `revisar sistémico`: el problema parece venir de una regla general
- `revisar escena`: el costo depende de distinguir exploración de presión real
- `revalidada`: ya pasó por la doctrina vigente en esta corrida

## Orden de revalidación

1. `interrupción / intercepción / desvío / control de línea`
2. `posturas`
3. `hostigamiento / perforación / impredecible / fluidez`
4. `impacto / ruptura / desgarro / imparable`
5. `escudo / evasión / armadura`
6. `especialización`
7. `resistencia híbrida`
nota: `bloque pasivo, cierre doctrinal esperado en 0/0`

## Tabla base

| ID | Técnica | Actual | Fuente competencia | Dominio técnica | Familia funcional | Perfil / build | Acceso / restricción | Comparables directos | Estado clean run | Propuesta | Nota |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 02 | Cerrar la Línea | `4/1` | competencia compatible con el perfil | combate por perfil | castigo a entrada por movimiento | `Control de Línea` | origen compatible con el perfil | 10, 23, 37 | revalidada | `4/1` | compuerta clara, una sola superficie principal: daño + detener tránsito inmediato |
| 03 | Recuperar la Distancia | `5/1` | competencia compatible con el perfil | combate por perfil | spacing ofensivo | `Perforación` | origen compatible con el perfil | 04, 11 | revalidada | `5/1` | ataque estándar con reposicionamiento corto posterior; compra spacing, pero no agrega segundo eje dominante |
| 04 | Clavar el Paso | `5/1` | competencia compatible con el perfil | combate por perfil | entrada ofensiva con avance | `Perforación` | origen compatible con el perfil | 03, 11 | revalidada | `5/1` | convierte parte del movimiento en entrada ofensiva, pero sigue siendo una sola resolución principal |
| 05 | Anudar el Paso | `4/1` | competencia compatible con el perfil | combate por perfil | negación de retirada | `Torsión` | origen compatible con el perfil | 79, 75 | revalidada | `4/1` | control reactivo estrecho sobre retirada; muy fuerte en su momento exacto, pero sin daño efectivo en el texto actual ni segundo eje mayor |
| 06 | Robar el Ángulo | `4/1` | competencia compatible con el perfil | combate por perfil | robo de ángulo y penalización | `Impredecible` | origen compatible con el perfil | 73 | revalidada | `4/1` | no hace daño; compra desplazamiento angular corto y presión sobre la próxima acción del rival, bien encapsulada para `4/1` |
| 07 | Marcar la Lectura | `4/1` | competencia compatible con el perfil | combate por perfil | marcaje de ruta y localización | `Precisión` | origen compatible con el perfil | 62, 08 | revalidada | `4/1` | persistencia informativa muy útil, pero no degrada directamente defensa, daño ni acción enemiga; buen costo de seguimiento técnico |
| 08 | Nublar la Señal | `4/1` | competencia compatible con el perfil | combate por perfil | residuo sensorial y obstrucción | `Corrosión` | origen compatible con el perfil | 52, 07 | revalidada | `4/2` | penalización persistente sobre cualquier tirada, técnica o intercambio que dependa del canal afectado; la compuerta es real, pero la cobertura táctica es demasiado amplia para `Desgaste 1` |
| 09 | Doblar el Tiro | `4/1` | competencia compatible con el perfil | combate por perfil | geometría indirecta | `Desvío` | origen compatible con el perfil | 78 | revalidada | `4/1` | ataque indirecto útil, pero sigue siendo una sola resolución sin negar acción enemiga |
| 10 | Clavar la Cadencia | `4/1` | competencia compatible con el perfil | combate por perfil | castigo a movimiento declarado | `Cadencia` | origen compatible con el perfil | 02, 71 | revalidada | `4/1` | presión reactiva fuerte sobre movimiento, pero sin detención garantizada ni segundo eje mayor |
| 11 | Tocar y Ceder | `5/1` | competencia compatible con el perfil | combate por perfil | hostigamiento con ida y salida | `Hostigamiento` | origen compatible con el perfil | 56, 03, 04 | revalidada | `5/1` | ataque con entrada y salida breve atadas al acierto; muy expresiva, pero todavía de una sola superficie fuerte |
| 12 | Trabar el Gesto | `5/1` | competencia compatible con el perfil | combate por perfil | reemplazo defensivo por interrupción | `Interrupción` | origen compatible con el perfil | 59, 80, 74 | revalidada | `6/2` | reemplaza defensa, niega ataque, hace daño y puede fijar condición permanente; paquete demasiado ancho para `5/1` |
| 13 | Plantar la Guardia | `3/1` | competencia compatible con el perfil | combate por perfil | postura de guardia | `Guarda` | origen compatible con el perfil | 26, 29 | revalidada | `3/2` | `Ritmo 3` se sostiene, pero cobrar `Ritmo` extra igual al rango sobre cada acción enemiga en zona altera demasiados intercambios para `Desgaste 1` |
| 14 | Leer el Calor del Paso | `3/1` | especialización | Percepción | lectura sensorial integrada | lectura / setup | — | 16, 17, 18 | revalidada | `3/1` | lectura inmediata útil y estrecha; no crea ventaja mecánica amplia por sí sola |
| 15 | Pesar el Umbral | `4/1` | especialización | Sigilo | setup oculto que fuerza terror | setup / presión | — | 69, 68 | revalidada | `4/1` | compuerta fuerte de ocultamiento válido más estado en fallo de resistencia; buen costo de presión especializada |
| 16 | Leer la Línea Ausente | `3/1` | especialización | Interpretación | lectura de ausencia estructural | lectura | — | 14, 17, 18 | revalidada | `3/1` | información estructural muy útil pero sin conversión táctica dura inmediata |
| 17 | Medir el Ciclo | `3/1` | especialización | Astronomía | lectura de ritmo ATB | lectura / setup | — | 14, 16, 18 | revalidada | `4/1` | no solo informa: además entrega bonificador a varias salvaciones futuras de un mismo ciclo; demasiado ancho para seguir en `3` |
| 18 | Leer el Propósito | `4/1` | especialización | Arquitectura | lectura de punto vital | lectura / setup ofensivo | — | 24, 66 | revalidada | `4/1` | setup ofensivo persistente, pero con compuerta fuerte y beneficio personal, no compartido |
| 19 | Cruzar la Punta | `3/1` | competencia defensiva | evasión | respuesta a ataque de objetivo único | `Evasión` | — | 20, 57 | revalidada | `3/1` | defensa estrecha con avance corto hacia el atacante; muy encapsulada y dependiente del éxito defensivo |
| 20 | Vaciar el Blanco | `3/1` | competencia defensiva | evasión | vaciado de línea personal | `Evasión` | — | 19, 57 | revalidada | `3/2` | además de evitar el golpe, deja un bono amplio a la próxima tirada relevante contra ese enemigo; su valor diferido es demasiado bueno para `Desgaste 1` |
| 21 | Templar el Veneno | `0/0` | resistencia + especialización | híbrida de resistencia | venenos | `Tolerancia + Resistencia al Veneno` | — | 50, 51 | revalidada | `0/0` | pasiva por doctrina; expresa una capacidad ya internalizada, no una activación táctica |
| 22 | Sostener el Canal | `0/0` | resistencia + especialización | híbrida de resistencia | aflicciones | `Meditación + Resistencia a Aflicciones` | — | 49 | revalidada | `0/0` | pasiva por doctrina; expresa una capacidad ya internalizada, no una activación táctica |
| 23 | Fijar el Umbral | `5/1` | especialización | Agarre | negación de paso por contacto | control | — | 02, 05, 37 | revalidada | `5/1` | muy buena negación reactiva, pero estrictamente cuerpo a cuerpo y sin daño; buen benchmark de control por especialización |
| 24 | Marcar la Grieta | `4/1` | especialización | Arqueología | lectura de debilidad material | lectura / setup ofensivo | — | 18, 43 | revalidada | `4/2` | deja una mejora persistente a Impacto sobre una zona marcada; el valor acumulado de varios ataques pide más `Desgaste` |
| 25 | Sentar el Tercer Punto | `3/1` | especialización | Equilibrio | preservación de paso en mal terreno | estabilidad / movilidad | — | 38, 65 | revalidada | `3/1` | respuesta estrecha y muy dependiente del terreno; buen costo base mientras se cobre solo bajo presión real |
| 26 | Cerrar la Compuerta | `3/1` | competencia de escudo | escudo | postura de línea | `Control de Línea` | — | 13, 29 | revalidada | `3/2` | postura anclada correcta en `Ritmo`, pero la penalización igual al rango sobre ataques a aliados en toda la zona pide más costo o una futura estrechez textual |
| 27 | Levantar el Dique | `4/1` | competencia de escudo | escudo | protección de tercero | `Intercepción` | — | 33, 28 | revalidada | `4/1` | protección reactiva pura; cambia el punto de contacto pero no añade daño ni control garantizado |
| 28 | Romper el Caudal | `5/2` | competencia de escudo | escudo | interrupción defensiva dura | `Interrupción` | — | 12, 74 | revalidada | `5/2` | benchmark sano de defensa reemplazada + contraimpacto sin estado adicional ni doble secuencia |
| 29 | Asentar la Piedra | `3/1` | competencia de escudo | escudo | postura de punto y sostén | `Bastión` | — | 13, 26, 36 | revalidada | `3/2` | el texto publicado es muy ancho: bono pleno a `T.D.` contra enemigos visibles y a muchas `T.R.`; sin estrechar eso, `Desgaste 1` parece corto |
| 30 | Cerrar el Juicio | `5/2` | competencia compatible con el perfil | combate por perfil | ruptura declarada | `Impacto` | origen compatible con el perfil | 31, 61, 76 | revalidada | `5/1` | compra daño normal más validación de ruptura más fácil, pero sigue siendo una línea muy especializada y de una sola secuencia |
| 31 | Barrer la Orilla | `5/2` | competencia compatible con el perfil | combate por perfil | daño + derribo/desequilibrio | `Impacto` | origen compatible con el perfil | 30, 76 | revalidada | `5/2` | daño + `Desequilibrado` en fallo de resistencia; buen escalón base del perfil `Impacto` |
| 32 | Anclar el Contrapeso | `3/1` | competencia de escudo | escudo | anti-desplazamiento y anti-derribo | `Control de Línea` | — | 26, 27 | revalidada | `3/1` | respuesta estrecha, sin daño ni presión a terceros; protege apoyo y continuidad corporal nada más |
| 33 | Cerrar el Flanco | `6/2` | competencia compatible con el perfil | combate por perfil | intercepción ofensiva ampliada | `Intercepción` | requiere contacto físico alcanzable | 27, 74, 80 | revalidada | `6/2` | protege self o tercero, niega ataque y convierte en daño; benchmark sano de intercepción ofensiva amplia |
| 34 | Abrir la Vasija | `5/2` | competencia compatible con el perfil | combate por perfil | daño + laceración por apertura | `Desgarro` | origen compatible con el perfil | 54, 72 | revalidada | `5/2` | daño + `Lacerado` en una sola resolución; paquete clásico de dos ejes relevantes |
| 35 | La Corriente No Retrocede | `5/2` | competencia compatible con el perfil | combate por perfil | daño + desalojo de postura | `Imparable` | origen compatible con el perfil | 77, 55 | revalidada | `5/2` | daño + desplazamiento forzado en fallo de resistencia; sigue siendo un paquete fuerte pero acotado |
| 36 | Sellar la Presa | `4/1` | competencia compatible con el perfil | combate por perfil | bastión ofensivo con estado | `Bastión` | origen compatible con el perfil | 29, 26 | revalidada | `5/2` | ataque con daño normal más `Derribado` en fallo de resistencia; ese paquete ya vive en el escalón de dos ejes relevantes y no debería quedar por debajo de `Barrer la Orilla` |
| 37 | Devolver al Cauce | `4/1` | competencia compatible con el perfil | combate por perfil | captura de tránsito por canal | `Interrupción` | origen compatible con el perfil | 02, 10, 23 | revalidada | `4/1` | control de tránsito limpio, sin daño, con doble compuerta de éxito; muy fuerte pero bien encapsulada |
| 38 | Tomar la Corriente | `3/1` | especialización | Nadar | resistencia a arrastre y desplazamiento | anti-desplazamiento | — | 25, 41 | revalidada | `3/1` | técnica reactiva estrecha con elección entre dos salidas; muy buena, pero bien acotada por la compuerta física |
| 39 | Guardar el Pulso | `0/1+` | especialización | Tolerancia | sostener función bajo degradación corporal | continuidad corporal | — | 42, 64 | revalidada | `0/1+` | costo variable bien alineado con el grado de mitigación; su lectura sigue dependiendo de presión real, pero la estructura base es sana |
| 40 | Sellar la Grieta | `4/2` | especialización | Aplomo | oposición a técnica mental/social | contra-juego | — | 63 | revalidada | `4/2` | contra-juego reactivo con negación parcial o total de efectos condicionales; dos ejes claros de valor |
| 41 | Tomar el Resguardo | `3/1` | especialización | Supervivencia | identificar cobertura útil | lectura / setup espacial | — | 43, 65 | revalidada | `3/1` | fuerte dependencia de escena y rasgo físico real; buen costo base mientras no cree cobertura desde cero |
| 42 | Anudar la Vasija | `3/1` | especialización | Medicina | tratamiento breve y estabilización | recuperación | — | 39 | revalidada | `4/1` | estabilizar una herida y retirar agonía/penalizaciones en escena tiene demasiado peso para seguir en `3` |
| 43 | Tomar la Costura | `4/1` | especialización | Minería | lectura material | — | — | 24, 41 | revalidada | `4/2` | puede degradar cobertura o facilitar ruptura de forma persistente sobre una superficie relevante; valor acumulado mayor que una simple lectura |
| 44 | Tomar el Eco | `3/1` | especialización | Resonancia | lectura de huella o señal | lectura | — | 45, 67 | revalidada | `3/1` | lectura flexible, pero sin bonificador directo amplio salvo por la información que entrega |
| 45 | Tomar la Secuencia | `3/1` | especialización | Taumaturgia | lectura de patrón taumático | lectura | — | 44, 67 | revalidada | `4/1` | además de leer una condición de funcionamiento, deja bonificador persistente a tus `T.E.` o `T.A.` contra ese fenómeno |
| 46 | Cerrar la Coraza | `3/4` | competencia de armadura | armadura | postura de línea blindada | `Armadura pesada / intermedia` | línea cubierta declarada | 47 | revalidada | `3/3` | aquí sí hay razón para `Desgaste` alto: puede modificar muchos impactos relevantes del combate, pero `4` todavía se ve un escalón por encima de lo que el texto garantiza con claridad |
| 47 | Volver la Placa | `3/2` | competencia de armadura | armadura | corrección reactiva de impacto | `Armadura intermedia / pesada` | — | 46 | revalidada | `3/1` | compuerta muy estrecha: solo responde a golpe crítico sobre pieza funcional; protege continuidad material más que el intercambio táctico inmediato |
| 48 | Bajar el Núcleo | `0/0` | resistencia + especialización | híbrida de resistencia | exposición ambiental | `Aclimatación + Resistencia al Calor` | — | 21 | revalidada | `0/0` | pasiva por doctrina; expresa una capacidad ya internalizada, no una activación táctica |
| 49 | Nombrar el Umbral | `0/0` | resistencia + especialización | híbrida de resistencia | aflicciones | `Teología + Resistencia a Aflicciones` | — | 22 | revalidada | `0/0` | pasiva por doctrina; expresa una capacidad ya internalizada, no una activación táctica |
| 50 | Hacer Esperar la Podredumbre | `0/0` | resistencia + especialización | híbrida de resistencia | infecciones | `Tolerancia + Resistencia a Infecciones` | — | 21, 51 | revalidada | `0/0` | pasiva por doctrina; expresa una capacidad ya internalizada, no una activación táctica |
| 51 | Mantener Cerrada la Línea de Contagio | `0/0` | resistencia + especialización | híbrida de resistencia | infecciones | `Medicina + Resistencia a Infecciones` | — | 50 | revalidada | `0/0` | pasiva por doctrina; expresa una capacidad ya internalizada, no una activación táctica |
| 52 | Ensuciar la Herida | `5/1` | competencia compatible con el perfil | combate por perfil | daño + degradación de tratamiento | `Corrosión` | origen compatible con el perfil | 08, 54 | revalidada | `5/1` | persistencia estrecha sobre una herida ya abierta y orientada a tratamiento; molesta continuidad y recuperación, pero no altera tantos intercambios inmediatos como `08` |
| 53 | Reír en la Brecha | `5/1` | competencia compatible con el perfil | combate por perfil | presión de defensa futura | `Acecho` | origen compatible con el perfil | 06, 60 | revalidada | `5/2` | no hace daño, pero deja una penalización persistente a todas las `T.D.` directas del objetivo contra ti; presión sostenida demasiado eficiente para quedarse en `Desgaste 1` |
| 54 | Abrir la Costura | `5/1` | competencia compatible con el perfil | combate por perfil | daño + ignorar bloqueo | `Desgarro` | origen compatible con el perfil | 34, 61 | revalidada | `5/1` | mejora directa de conversión de daño, pero sin estado ni segunda superficie mayor |
| 55 | Atajar el Brote | `7/2` | competencia compatible con el perfil | combate por perfil | carga + ignorar bloqueo | `Embestida` | origen compatible con el perfil | 35, 77 | revalidada | `7/2` | compromiso espacial grande más conversión fuerte de daño; benchmark sano del escalón pesado |
| 56 | Robar la Orilla | `4/1` | competencia compatible con el perfil | combate por perfil | hostigamiento con reposición larga | `Hostigamiento` | origen compatible con el perfil | 11 | revalidada | `5/1` | daño normal más reposicionamiento de hasta media velocidad sin costo extra; la amplitud espacial es demasiado grande para seguir en `4` |
| 57 | Quebrar la Vuelta | `3/1` | especialización / defensa | evasión | counter-positioning | `Evasión` | — | 19, 20, 58 | revalidada | `3/1` | defensa estrecha con bonificador y cambio de ángulo en contacto cercano; muy buena, pero todavía de superficie limitada |
| 58 | Soltar la Capa Muerta | `3/1` | competencia de armadura | armadura | defensa evasiva con desprendimiento | `Armadura ligera` | — | 57, 19, 20 | revalidada | `3/1` | éxito defensivo más reposicionamiento corto a espacio válido; muy alineada con una defensa ligera reactiva |
| 59 | Cortar la Mano Tarde | `5/1` | competencia compatible con el perfil | combate por perfil | interrupción ofensiva de ejecución | `Interrupción` | origen compatible con el perfil | 12, 80 | revalidada | `5/2` | reemplaza defensa o respuesta normal, niega la acción enemiga y convierte en daño, pero no añade estado; encaja con el escalón de interrupción dura sin condición adicional |
| 60 | Encontrar la Parte Blanda | `4/2` | competencia compatible con el perfil | combate por perfil | presión de crítico sobre punto vital | `Letalidad` | origen compatible con el perfil | 53, 62 | revalidada | `4/1` | conversión letal puntual sobre una sola `T.I.` con compuerta fuerte de parte vital expuesta; muy expresiva, pero no compra persistencia ni control suficientes para `Desgaste 2` |
| 61 | Hacer Ceder el Resguardo | `4/3` | competencia compatible con el perfil | combate por perfil | ruptura de protección | `Ruptura` | origen compatible con el perfil | 30, 54 | revalidada | `4/2` | técnica estrecha y altamente especializada; sufre por `Desgaste 3` porque no compra daño + estado + control, sino anti-protección puntual |
| 62 | Darle a la Pieza Útil | `5/1` | competencia compatible con el perfil | combate por perfil | castigo a parte funcional | `Precisión` | origen compatible con el perfil | 07, 60 | revalidada | `5/2` | penalización persistente a todas las `T.A.` hechas con una parte de ataque identificable; su compuerta es real, pero el efecto altera demasiados intercambios para quedarse en `Desgaste 1` |
| 63 | Sostener la Mano Necesaria | `3/1` | especialización | Contención | sustitución de salvación de aliado o self | contra-juego / soporte | — | 40 | revalidada | `4/1` | reemplaza salvación propia o de aliado adyacente con bonificador de rango; soporte reactivo demasiado bueno para `3` |
| 64 | Tomar la Parte Útil | `0/3` | especialización | Destreza | segunda oportunidad técnica | rescate procedural | — | 39, 65 | revalidada | `0/2` | la compuerta es estrecha y no permite tercer intento; `3` parece exceso para un rescate procedural tan específico |
| 65 | Tirar la Advertencia | `2/1` | especialización | Lanzamiento | setup / movilidad | — | — | 25, 41, 64 | revalidada | `2/1` | conversión muy estrecha sobre una sola tirada futura y un punto exacto de ruta; buen uso del escalón `2` |
| 66 | Leer lo que Siguió | `3/1` | especialización | Rastreo | lectura ofensiva | — | — | 18, 24 | revalidada | `4/2` | deja un bono persistente a todas las `T.A.` o `T.E.` dirigidas a una zona legible; setup ofensivo acumulativo claro |
| 67 | Oír la Costura | `3/1` | especialización | Resonancia | lectura | — | — | 44, 45 | revalidada | `4/1` | no solo orienta la lectura: además deja bonificador persistente a `T.R.` o `T.C.` de Tenacidad contra el mismo fenómeno |
| 68 | Reír Donde Más Suena | `3/1` | especialización | Intimidación | presión / control | — | — | 15, 69 | revalidada | `4/1` | presión directa a rango sensorial con posibilidad de `Aterrorizado` sin requerir ocultamiento previo; `3` se queda corto |
| 69 | Pasar Como Parte del Fondo | `3/1` | especialización | Sigilo | movilidad / sigilo | — | — | 15, 65 | revalidada | `3/1` | cruce muy acotado por zona declarada y patrón de fondo creíble; buen costo base para sigilo técnico de paso |
| 70 | Ceder Antes del Disparo | `0/2` | especialización | Trampas | counterplay procedural | — | — | 64, 42 | revalidada | `0/1` | respuesta muy específica a trampas; buena sustitución, pero con compuerta demasiado estrecha para `Desgaste 2` |
| 71 | Cortar el Paso Dos Veces | `5/1` | competencia compatible con el perfil | combate por perfil | doble castigo a movimiento con consumible | `Volley` | requiere 2 armas arrojadizas | 10, 02 | revalidada | `6/2` | puede resolver hasta dos `T.I.` y además reducir o cancelar movimiento; el consumible y la compuerta ayudan, pero el paquete total ya vive por encima del castigo simple a tránsito |
| 72 | Cerrar la Salida | `7/2` | competencia compatible con el perfil | combate por perfil | doble ataque + `Lacerado` | `Fluidez` | origen compatible con el perfil | 73, 34 | revalidada | `7/2` | doble resolución ofensiva y condición si ambas conectan; compromiso fuerte y benchmark sano del escalón alto |
| 73 | Cobrar con la Otra | `6/2` | competencia compatible con el perfil | combate por perfil | doble ataque + `Desequilibrado` | `Impredecible` | requiere soporte lógico para segundo ataque | 72, 06 | revalidada | `6/2` | doble ataque con condición si ambas conectan; un escalón debajo de `72` se sostiene bien |
| 74 | Cierre en el Umbral | `5/2` | competencia compatible con el perfil | combate por perfil | reemplazo defensivo + `Impedido` | `Intercepción` | requiere anatomía o punto de contacto compatible | 12, 33, 80 | revalidada | `5/2` | niega ataque y puede fijar estado, pero no añade daño; se sostiene por debajo de `33` y `80` |
| 75 | El Peso Que Gira | `6/2` | competencia compatible con el perfil | combate por perfil | torsión y reposicionamiento | `Torsión` | requiere anatomía o punto de contacto compatible | 05, 79 | revalidada | `6/2` | daño más reposicionamiento preciso no resistido por separado; compra control corporal real y merece vivir arriba del escalón medio |
| 76 | La Masa Continúa | `6/2` | competencia compatible con el perfil | combate por perfil | daño + `Derribado` | `Impacto` | requiere anatomía o punto de contacto compatible | 31, 30 | revalidada | `6/2` | mismo eje que `31`, pero con una condición físicamente más dura; se sostiene un escalón arriba |
| 77 | El Cierre Que No Se Negocia | `5/2` | competencia compatible con el perfil | combate por perfil | cierre imparable e ignorar bloqueo | `Imparable` | requiere anatomía o punto de contacto compatible | 35, 55 | revalidada | `5/1` | con el texto actual compra sobre todo conversión de daño por ignorar bloqueo; no justifica `Desgaste 2` frente a `Abrir la Costura` |
| 78 | El Ángulo Que Falla | `7/2` | competencia compatible con el perfil | combate por perfil | deflexión + seguimiento natural | `Desvío` | requiere anatomía o secuencia corporal compatible | 09, 74 | revalidada | `7/2` | niega ataque, hace daño y habilita una segunda `T.A.` con compuerta anatómica real; swing reactivo mayor |
| 79 | La Vuelta Que Suelta | `5/2` | competencia compatible con el perfil | combate por perfil | desarme por torsión | `Torsión` | requiere anatomía o punto de contacto compatible | 05, 75 | revalidada | `5/2` | no hace daño, pero `Desarmado` es un control permanente muy decisivo y con requisito anatómico real; buen escalón medio-alto |
| 80 | La Base Que Falta | `6/2` | competencia compatible con el perfil | combate por perfil | interrupción de ataque + daño + estado | `Interrupción` | requiere anatomía o secuencia corporal compatible | 12, 59, 74 | revalidada | `6/2` | benchmark sano de interrupción reactiva completa: reemplazo de defensa, negación, daño y condición |

## Nota de clean run

Las pasadas anteriores quedan fuera de los documentos activos para evitar
anclaje. Si alguna conclusión vieja merece rescatarse, deberá reingresar aquí
solo después de ser revalidada explícitamente.

## Outliers para última mirada

Estas técnicas merecen una revisión final corta antes de aplicar cambios en
masa, no porque hayan quedado pendientes, sino porque están cerca de un borde
doctrinal o porque el cambio propuesto es relativamente fuerte.

- `12 Trabar el Gesto` → `6/2`
  sube en ambos ejes; es el benchmark fuerte de interrupción reactiva

- `36 Sellar la Presa` → `5/2`
  salto grande frente al publicado; conviene confirmar que `Derribado` debe
  vivir al mismo escalón que otros paquetes de daño + condición

- `46 Cerrar la Coraza` → `3/3`
  sigue siendo una postura especial y uno de los costos de `Desgaste` más altos
  del set

- `53 Reír en la Brecha` → `5/2`
  penalización persistente a todas las `T.D.` directas contra ti; puede volverse
  opresiva si la ficción la mantiene activa con facilidad

- `62 Darle a la Pieza Útil` → `5/2`
  la persistencia sobre una parte de ataque es muy potente si la compuerta de
  visibilidad resulta común en mesa

- `66 Leer lo que Siguió` → `4/2`
  varias técnicas de lectura ofensiva subieron, pero esta es la más claramente
  acumulativa

- `71 Cortar el Paso Dos Veces` → `6/2`
  paquete muy ancho aun con consumible; conviene confirmar que el costo de
  recursos materiales no ya esté pagando suficiente

- `77 El Cierre Que No Se Negocia` → `5/1`
  baja en `Desgaste`; conviene mirar una vez más si ignorar `Bloqueo` se siente
  tan puntual en mesa como en la lectura doctrinal

---

## Audit 81–117 — pasada de costos `2026-07-09`

Técnicas 81–117 (Drak'kai novatas, especializaciones Drak'kai, set de herencias).
31 técnicas validadas sin cambios. 6 outliers corregidos y aplicados.

| ID | Técnica | Anterior | Nuevo | Razón del cambio |
| --- | --- | --- | --- | --- |
| 86 | El Golpe Que Cobra | `3/1` | `0/1` | Dispara cuando ya fallaste T.D. — no hay acción del usuario, es consecuencia automática del golpe en armadura funcional. Ritmo 0 como otras técnicas de trigger-on-hit. |
| 92 | El Cuello Que Todo Lo Atraviesa | `3/2` | `3/1` | Sustitución de habilidad espacial + bono = un solo output compuesto. Desgaste 2 exige dos ejes independientes. |
| 93 | El Margen Que Quedó Abierto | `3/2` | `3/1` | Mismo patrón que #92 para habilidades sociales. Un output. |
| 107 | Adaptabilidad | `3/2` | `3/1` | Swap de especializaciones = un output. Cantidad de habilidades consolidadas no determina el Desgaste; lo determina el ancho de los outputs. |
| 108 | La Presa del Oso | `4/1` | `4/2` | T.I. + Atrapado = dos superficies relevantes. El costo por activación de mantenimiento no reduce el ancho del paquete base. |
| 117 | Saturación | `2/3` | `2/1` | Cleanse condicional de una Alteración con tirada que puede fallar = un output con compuerta real. Desgaste 3 no se sostiene para una sola superficie. |

**Casos borderline — mantenidos sin cambio:**

- `89 La Línea Que No Se Rompe` `0/2` — preservar una Postura activa bajo golpe es un output de alto impacto en el estado de juego. Desgaste 2 defensible.
- `99 Protección Natural` `0/2` — trigger amplio (cualquier herida no crítica), un output fuerte (negación completa de heridas Leve). Ritmo 0 correcto porque dispara en la ventana de reacción sin acción del usuario.
- `101 Magnetorrecepción` `3/2` — tres outputs en la misma familia sensorial (posición, sorpresa, ocultamiento). No cambiado; los tres pertenecen al mismo sentido magnético y la compuerta de T.C. es real.
- `113 Aceleración del Caos` `0/2` — movimiento físico con Ritmo 0. Defensible: reflejo biológico involuntario al recibir herida — el trigger no es una elección táctica sino una respuesta corporal automática.
