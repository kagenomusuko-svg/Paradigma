## PARTE III · El análisis integrado: las tres series

### Capítulo III·3
El expediente integrado completo
Qué documentos entrega, en qué formato y para qué audiencia

### I. La arquitectura del expediente integrado
El expediente integrado consolida los resultados de las tres
series en un conjunto ordenado de documentos. No es la
yuxtaposición de tres expedientes separados: es un expediente
único con una estructura interna que permite al destinatario
acceder a cualquier nivel de detalle que su audiencia o su foro
requiera, sin por ello renunciar a la coherencia del conjunto.
El expediente integrado tiene cuatro niveles de detalle. El
nivel de resumen ejecutivo es accesible a cualquier audiencia —
formula el resultado central del análisis en lenguaje del dominio
del destinatario, sin referencias al aparato técnico del sistema. El
nivel de documentos del análisis contiene los resultados formales
de las tres series — es el nivel que el destinatario usa en el foro
adversarial o en la reunión de dirección. El nivel de sustentación
contiene la hoja de calibración y los reportes de sensibilidad — es
el nivel que resiste el escrutinio técnico externo. El nivel de
verificación contiene los registros de la verificación cruzada — es

Metrología Causal · Vol. II
el nivel que el propio mediador consulta si el expediente es
revisado con posterioridad.

### II. Los documentos del expediente integrado
Docume Nivel Contenido Audiencia
nto principal
1 · Resumen Una página. El resultado Dirección
Resumen central del análisis en tres ejecutiva,
ejecutivo párrafos: qué ocurrió junta de
integrado (estructura causal en lenguaje gobierno,
del dominio), quién responde destinatario
y en qué proporción no técnico
(distribución R* en términos
absolutos si D_total está
cuantificado), y qué se
recomienda (hipótesis de
prevención más relevantes +
componentes del ajuste
debitor si aplica). Sin fórmulas,
sin referencias al aparato
técnico.
2 · Vector Análisis Tabla con R*(base), Destinatari
R* R*(ajustado) y R*(adversarial) o principal,
comparati para cada nodo, con sus abogado
vo componentes R*_neta, α y Δ. litigante,
Columna de fuente de S y α. regulador
Análisis narrativo de la
distribución: qué dice el vector
sobre la estructura causal del
sistema analizado.
3 · Mapa Análisis Los protocolos declarados Regulador,
de brecha relevantes del nodo de diseño auditor
IIC con sus c_k. El IIC global con interno,
su cálculo. La brecha entre el

Metrología Causal · Vol. II
Docume Nivel Contenido Audiencia
nto principal
campo declarado y el real comité de
descrita en lenguaje del compliance
dominio. Aplicar solo si Serie
II está en el análisis.
4 · Ajuste Análisis Los tres componentes del Consejo de
debitor ajuste debitor (estructural, administrac
con procesal, reparatorio) con sus ión,
cronogra plazos verificables. Aplicar directivo
ma solo si Serie II está en el responsable
análisis. , regulador
5 · Análisis El nivel A/B/C/D con el Tribunal,
Declaraci enunciado formal completo. árbitro,
ón de El valor exacto de ρ(θ) que lo regulador,
robustez sustenta. Aplicar solo si Serie foro
III está en el análisis. adversarial
6 · Hoja Sustentac La hoja de calibración Experto
de ión adversarial con todas las contrario,
calibració adiciones de Series II y III: revisor
n nodo de diseño identificado, técnico,
(consolida protocolos declarados con apelación
da) c_k, rangos adversariales con
sus fuentes admisibles. Es el
documento técnico completo
que sustenta todos los
resultados del expediente.
7 · Sustentac La función ρ(θ) con los puntos Experto
Reporte ión de quiebre identificados y su contrario,
de interpretación. El mapa de tribunal
sensibilida estabilidad del ranking sobre el técnico,
d hipercubo. Aplicar solo si revisión
Serie III está en el análisis. académica
8 · Verificaci Las cuatro consistencias C1– Revisión
Registro ón C4 con su resultado interna del
de (consistente/diagnosticado/c expediente,

Metrología Causal · Vol. II
Docume Nivel Contenido Audiencia
nto principal
verificació orregido). Las correcciones auditoría de
n cruzada aplicadas con su trazabilidad. calidad del
La incertidumbre residual análisis
documentada si la hay.

### III. Qué documentos entrega cada combinación
de series
No todas las combinaciones de series producen todos los
documentos. La tabla siguiente especifica qué documentos forman
el expediente según la combinación activada. Los documentos
marcados como obligatorios deben estar presentes para que el
expediente sea válido. Los marcados como condicionales se
incluyen solo si la operación que los produce se activó.
Document Solo Serie Series Series Series
o I I+II I+III I+II+III
1 · Resumen Obligatori Obligatori Obligatorio Obligatori
ejecutivo o o o
2 · Vector Solo R*(base) y R*(base) y Los tres
R* R*(base) R*(ajustad R*(adversaria vectores
comparativ o) l)
o
3 · Mapa de No aplica Obligatori No aplica Obligatori
brecha IIC o o
4 · Ajuste No aplica Obligatori No aplica Obligatori
debitor o o

Metrología Causal · Vol. II
Document Solo Serie Series Series Series
o I I+II I+III I+II+III
5 · No aplica No aplica Obligatorio Obligatori
Declaración o
de robustez
6 · Hoja de Base Base + Base + Base +
calibración compliance adversarial complianc
e +
adversarial
7 · Reporte No aplica No aplica Obligatorio Obligatori
de o
sensibilidad
8 · Registro Simplificad C1 y C2 C3 y C4 C1, C2,
de o C3 y C4
verificación

### IV. El formato del expediente según el foro
Los ocho documentos del expediente integrado tienen un
contenido invariante — lo que dicen no cambia según el foro. Lo
que cambia es el orden en que se presentan, el nivel de detalle que
se pone en primer plano, y el vocabulario del dominio que se usa
en el análisis narrativo. Esta sección establece las tres
configuraciones más frecuentes.
Configuración A — Presentación ante tribunal o árbitro
Orden: Declaración (5) → Vector R* comparativo (2) →
Hoja de calibración (6) → Reporte de sensibilidad (7) →
Resumen ejecutivo (1) como apéndice para el jurado no
técnico.

Metrología Causal · Vol. II
Énfasis: la Declaración al frente porque es el documento que
el foro evalúa primero. La hoja de calibración disponible para
revisión técnica. El resumen ejecutivo como auxiliar para
audiencias mixtas.
Vocabulario: usar el vocabulario jurídico del dominio en el análisis
narrativo. R* se comunica como 'contribución causal proporcional'. S como
'estándar del sector' o 'práctica habitual'. Δ como 'brecha de diligencia
debida'.
Configuración B — Presentación ante regulador o
auditor
Orden: Resumen ejecutivo (1) → Mapa de brecha IIC (3) →
Ajuste debitor (4) → Vector R* comparativo (2) → Hoja de
calibración (6) → Registro de verificación (8).
Énfasis: el mapa de brecha IIC y el ajuste debitor al frente
porque el regulador necesita la descripción del
incumplimiento de diseño antes que la distribución de
responsabilidad. La Declaración en el expediente solo si el
foro regulatorio la requiere explícitamente.
Vocabulario: usar terminología de compliance y regulación. R* como 'peso
en la distribución del riesgo'. IIC como 'índice de cumplimiento declarado
vs. real'. Fraude annona como 'posición de responsabilidad institucional
agravada'.
Configuración C — Presentación ante consejo de
administración o dirección
Orden: Resumen ejecutivo (1) → Ajuste debitor (4) →
Vector R* comparativo (2) → Hoja de calibración (6) en
apéndice.

Metrología Causal · Vol. II
Énfasis: el resumen ejecutivo y el ajuste debitor son los
documentos centrales para la toma de decisión de un
consejo. La distribución R* informa, pero la pregunta
práctica que el consejo necesita responder es qué debe
cambiar en el diseño del sistema — eso está en el ajuste
debitor.
Vocabulario: lenguaje de gestión y gobierno corporativo. R* como
'contribución causal al resultado'. Δ como 'brecha de asunción'. El ajuste
debitor se presenta como 'plan de acciones correctivas con responsables y
plazos'.
Producto de salida · Capítulo III·3
Expediente integrado completo en la configuración de
presentación correcta para el foro del destinatario. Los ocho
documentos están presentes según la combinación de series
activas. El orden y el vocabulario reflejan la audiencia
principal.
Notas al Capítulo III·3
1 El resumen ejecutivo de una página es el documento más difícil de producir
del expediente integrado. Requiere que el mediador traduzca resultados
técnicos precisos a lenguaje accesible sin perder la precisión de la
atribución. La regla práctica: si el resumen ejecutivo puede ser
malinterpretado de una manera que cambie la acción que el destinatario
tomaría, necesita más precisión. Si añadir más precisión lo hace ilegible
para la audiencia de dirección, necesita dos versiones: una ejecutiva y
una técnica.
2 La hoja de calibración consolidada es el documento que determina si el
expediente integrado puede ser reproducido independientemente por
otro mediador con la misma evidencia. Una hoja de calibración bien
construida contiene toda la información necesaria para que un par
metodológico pueda verificar el análisis desde el principio. Esta
propiedad de reproducibilidad es la condición de que el expediente sea
un documento científico y no solo una opinión experta.

Metrología Causal · Vol. II

