# Diseño de Habilidades de Monstruos

Referencia para asignar Ritmos a las habilidades de bestias y decidir cuándo usar ciclos autónomos.

---

## Principio base

El Ritmo es el único costo operativo de un monstruo. No tiene Desgaste relevante entre escenas, no mejora con competencia, no es un recurso persistente — es el recurso que se consume en el encuentro.

Por eso el Ritmo de una habilidad de monstruo no responde a la misma pregunta que el Ritmo de una técnica de jugador. Las técnicas de jugador responden a: *¿qué tan eficiente es esto respecto a una acción base?* Las habilidades de monstruo responden a:

> **¿Cuántas veces debe poder hacer esto en un combate típico?**

---

## Paso 1 — Frecuencia esperada → rango de Ritmo

La frecuencia esperada es la pregunta de diseño primaria. Responderla define el rango de Ritmo correcto.

| Frecuencia esperada en combate | Rango de Ritmo |
| --- | :---: |
| Momento culminante — una vez, si acaso | 6–8 |
| Dos o tres veces — habilidad de impacto | 4–6 |
| Con frecuencia — herramienta principal de la criatura | 2–4 |
| Siempre que se active la condición (reacciones, triggers) | 0–2 |

Esta tabla es el punto de partida, no el veredicto final.

---

## Paso 2 — Chequeo de calidad contra técnicas de jugadores

Una vez definido el rango por frecuencia, comparar la habilidad del monstruo con la técnica de jugador más equivalente en scope. Las técnicas de jugadores son la referencia de calibración — no el benchmark de optimización, sino el ancla de valor táctico.

Referencias clave del sistema:

| Técnica | Ritmo | Qué hace |
| --- | :---: | --- |
| Cruzar la Punta | 3 | Reacción estrecha — evadir + avanzar sobre el atacante |
| Cerrar la Línea | 4 | Reacción con T.A. + detener movimiento del objetivo |
| Barrer la Orilla | 5 | Ataque activo + condición (Desequilibrado en fallo T.R.) |
| Atajar el Brote | 7 | Carga completa + ataque + ignorar bloqueo |
| Cerrar la Salida | 7 | Doble T.A. encadenada + Lacerado si ambas conectan |
| El Golpe Que Cobra | 0 | Consecuencia automática en fallo de T.D., sin elección del usuario |

Si la habilidad del monstruo tiene un scope similar a una de estas técnicas, su Ritmo debería estar cerca de ese valor — ajustado arriba si es más ancho, abajo si la frecuencia esperada es mayor.

---

## Paso 3 — Reacciones: Ritmo 0 o con costo

Las reacciones necesitan una decisión específica porque afectan directamente la posición del monstruo en el track.

**Ritmo 0 — trigger automático:**
La habilidad se dispara como consecuencia del estado de juego, sin elección activa del Narrador. El modelo es "El Golpe Que Cobra" (Ritmo 0): ocurre cuando el atacante falla la T.D. — no hay acción, es un resultado. Aplicar cuando:

- La habilidad es una consecuencia biológica/instintiva del evento
- El efecto es menor (no altera el resultado del combate por sí solo)
- El Narrador no tiene que "decidir" activarla — simplemente ocurre

**Ritmo 1–3 — elección reactiva:**
El Narrador elige activarla en respuesta a algo. El monstruo paga con su posición futura en el track. El efecto es significativo. Reaccionar tiene un costo real — es una decisión táctica, no presencia gratuita.

**Ritmo 4+:** Casi siempre demasiado para una reacción. Equivale a sacrificar la próxima activación completa. Solo si el efecto reactivo es excepcionalmente poderoso.

---

## Paso 4 — La velocidad de la criatura como límite, no como driver

El arquetipo de velocidad de la criatura no determina los valores de Ritmo — los acota por abajo y por arriba.

Una criatura descrita como veloz no debería tener su ataque principal en Ritmo 7. Una criatura pesada y lenta no debería tener ataques en Ritmo 2. Pero dentro de esos límites, la frecuencia esperada y el scope del efecto son los que fijan el valor exacto.

| Arquetipo | Límite inferior (no por debajo) | Límite superior (no por encima) |
| --- | :---: | :---: |
| Depredador rápido | 2 | 6 |
| Amenaza estándar | 3 | 7 |
| Tanque lento | 4 | 9 |

---

## Paso 5 — ¿Necesita un ciclo autónomo?

Un ciclo autónomo no compensa un Ritmo alto ni un problema de activación. Existe para una sola situación: **la criatura tiene dos comportamientos con cadencias distintas que ocurren en paralelo.**

Si el problema es que la criatura activa poco, la solución es bajar el Ritmo de sus habilidades o usar dos criaturas en lugar de una.

### Diagnóstico

| Pregunta | Si la respuesta es SÍ |
| --- | --- |
| ¿Tiene un efecto ambiental que pulsa independientemente de cuándo ataca? (veneno, esporas, calor, vibración) | Ciclo para ese efecto |
| ¿Tiene dos modos de ataque biológicamente disociados que operan en paralelo? (cuerpo frontal + cola; mandíbulas + aguijón) | Ciclo para el secundario |
| ¿Es un jefe diseñado para enfrentar al grupo completo en solitario, con Ritmo ya calibrado y aun así pasivo? | Ciclo para sostener presión |
| ¿Se regenera o invoca refuerzos en cadencia propia? | Ciclo para esa mecánica |
| ¿El problema es que activa poco? | **No** — ajustar Ritmo |
| ¿Se usa normalmente en grupos de 2 o más? | **No** — la composición compensa |

---

## Composición del encuentro como variable

Antes de ajustar Ritmos o añadir ciclos, verificar si el problema es de número de criaturas. Con todos a Ritmo similar:

| Composición | Activaciones del grupo por cada activación del monstruo |
| --- | :---: |
| 1 monstruo vs 4 jugadores | ≈ 4 |
| 2 monstruos vs 4 jugadores | ≈ 2 |
| 3 monstruos vs 4 jugadores | ≈ 1.3 |

Para criaturas de NR bajo pensadas para encuentros de grupo, dos criaturas es con frecuencia la solución más limpia.

---

## Resumen del flujo de decisión

```
1. ¿Cuántas veces debe disparar esta habilidad en combate?
   └─ Define el rango de Ritmo.

2. ¿Qué técnica de jugador tiene scope equivalente?
   └─ Usa ese Ritmo como ancla. Ajusta por scope mayor o menor.

3. ¿Es una reacción?
   └─ ¿Automática / instintiva? → Ritmo 0.
   └─ ¿Elección táctica del Narrador? → Ritmo 1–3.

4. ¿El Ritmo resultante encaja con la velocidad de la criatura?
   └─ Verificar contra los límites del arquetipo.

5. ¿La criatura siente que no hace nada en el encuentro?
   └─ Primero: ¿se puede bajar el Ritmo?
   └─ Segundo: ¿se pueden usar 2 criaturas?
   └─ Tercero: ¿hace algo en paralelo que requiera cadencia propia? → ciclo autónomo.
```
