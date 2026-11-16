# Primer GM conectado a Codex

Fecha: 2026-11-05.

El creador eligió la sesión actual de Codex frente a una API independiente. Se
consultó OpenAI Docs y la ayuda del CLI instalado (0.165.0). Solo se comprobó el
estado de autenticación, sin extraer claves o copiar credenciales. No había claves
de API en las variables comprobadas; no se presume una modalidad de facturación.

Se implementan `codex_transport.py`, `gm_agent.py`, pruebas de frontera y el piloto.
Codex recibe instrucciones explícitas, una vista del GM y operaciones limitadas
de consulta, preparación, incorporación local y presentación. No recibe objetos
Python, SQLite, el chat de diseño o cuadernos de protagonistas. Cada llamada es
nueva y efímera, con herramientas de acceso general desactivadas y modo de solo lectura.
Las reglas y restricciones administradas siguen vigentes. No se modifica la
configuración personal ni se cambia `HOME` o `CODEX_HOME`.

La primera conexión necesitó acceso al almacenamiento habitual de Codex fuera del
workspace; se ejecutó con la revisión de permisos del entorno. Los diagnósticos
no fatales del cliente se cuentan sin conservar texto potencialmente sensible.
Un fallo de turno o evento de herramienta nativa inesperado rechaza la salida.
Esto no se presenta como una garantía general de aislamiento del sistema operativo.

El primer piloto se detuvo por un fallo del adaptador: las referencias de consulta
no se traducían a evidencia de registro. Se corrigió y añadió cobertura; se retomó
la última presentación guardada sin pedir otra decisión al modelo ni borrar las
trazas anteriores. Después se hizo una llamada nueva para responder al jugador.

Resultado: siete respuestas reales del GM en el piloto, incluidas las del primer
intento. Dos presentaciones de 24 palabras cada una llegaron a un solo personaje.
La respuesta a la idea del silbato deja abierta su viabilidad y no la establece
como hecho. No hubo dados, acción física resuelta, recobros, progreso o campaña real.
La pregunta de jugador y su nota mental son datos controlados del ensayo, no agentes
autónomos. La nota no aparece en ninguna petición del GM; los otros actores no
reciben el intercambio y el estado se verifica al reabrir.

Artefactos privados del motor, fuera de Git:
`.local-runs/2026-11-05-gm-codex-pilot/inspection.md`, informe JSON, SQLite y carpeta
`gm-calls/` con instrucciones y peticiones/respuestas/resultados. La documentación
actualiza el avance sin declarar terminadas S4 o las herramientas de resolución.

Validación: 205 pruebas pasan en ocho conjuntos (20 del nuevo adaptador y 185
existentes), junto con la comprobación de vigencia de perfiles. El aviso previo
de conexión no cerrada del conjunto del Broker sigue apareciendo sin fallo de
pruebas. Se revisan sintaxis, enlaces, formato y las solicitudes reales guardadas.
