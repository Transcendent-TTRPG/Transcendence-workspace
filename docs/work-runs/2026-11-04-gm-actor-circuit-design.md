# Diseño del circuito completo GM/actores

Fecha: 2026-11-04. El creador indicó continuar con el diseño del circuito completo
y la implementación posterior por dependencias, cubriendo los seis frentes de alcance.

Se crea `Transcendence-narrative-engine/docs/gm-actor-interaction-design.md` como
propuesta para revisión. Desarrolla autoridad, entradas por rol, mensajes de
intervención, manifestación y pensamiento separados, solicitud de pruebas,
evidencia persistida antes de interpretación, confirmación atómica de consecuencias,
continuidad mutable, consultas, resúmenes, aislamiento y revisión del creador.

Precisiones: una nota privada no avanza el mundo ni revela su existencia al GM;
consultar experiencia propia no equivale a observar algo nuevo; las recuperaciones
de memoria no exponen cuadernos al GM ni usan triggers; los reintentos técnicos no
regeneran dados ya guardados. El controlador no decide una secuencia narrativa.

La revisión del código identifica una adaptación necesaria: v1 toma como tiempo
de contexto el de la última entrada del diario, también si es privada. Se documenta
separar reloj técnico y tiempo del mundo antes de integrar agentes, y verificar
que una nota no altere el contexto de otros roles. No se cambia esa lógica en
este entregable de diseño.

El orden de implementación queda vinculado a S0–S7: contratos de intervención,
continuidad mutable, contextos/consultas, moderación/pruebas, integración aislada,
ensayo sintético y entrada revisada a las Fosas. Se mantienen explícitamente
pendientes la plataforma, los límites de ejecución y la política de pausas ante
consecuencias irreversibles antes de una ejecución real.

Se actualizan enlaces y estados del plan, contrato del GM, arquitectura, README y
documentación local del Broker. Se corrigen afirmaciones antiguas de que aún no
existía ningún Broker. No se cambian código, formatos versión 1, ejemplo aprobado,
rosters, módulo o canon, ni se conectan modelos. Los detalles nuevos son propuesta,
sin declarar aprobación del creador ni cierre de S0/S1.
