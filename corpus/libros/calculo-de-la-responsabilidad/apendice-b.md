APÉNDICE B
Calibración de los pesos W
del grafo causal
Guía práctica para asignar valores numéricos a las aristas del
grafo en los 18 dominios del libro
Tabla universal de evidencia · Matrices por dominio ·
Calibración en expediente real · Casos de prueba
Este apéndice cierra la brecha entre la estructura del grafo
causal (qué nodos incluir y cómo conectarlos, que los
capítulos del libro explican) y el valor numérico de cada
arista (qué número asignar a ese peso, que hasta aquí
quedaba implícito). A lo largo del libro, cada arista w
aparece con un valor específico —w(UCC→resultado) =
0.80, w(ex-gerente→fraude) = 0.00, w(Princip→cascada) =
0.40— sin que en ningún momento se explicara el criterio
que produjo ese número en lugar de cualquier otro. Este
apéndice hace ese criterio explícito, verificable y replicable.
La calibración de W es un proceso de dos pasos que este
apéndice desarrolla en orden: primero la dirección de la
arista (qué tipo de relación causal representa), luego su
intensidad (qué valor numérico justifica la evidencia
disponible). Los dos pasos son independientes: la dirección
es una decisión sobre la estructura del grafo; la intensidad
es una estimación sobre la fuerza de esa relación causal.

El Cálculo de la Responsabilidad · Apéndices
§1. Los dos pasos de la
calibración: dirección e
intensidad
1.1 Paso 1: la dirección de la arista
Antes de asignar ningún número, es necesario determinar el
tipo de relación causal que la arista representa. El tipo
determina el rango de valores posibles y las fuentes de
evidencia relevantes. Hay cuatro tipos de arista en el grafo
causal:
Tipo Descripción Ejemplo del Rango w
libro habitual
Arista A realizó la O-ring → fallo 0.65 – 0.95
directa acción que del Challenger. según
produjo Subordinadas evidencia (E1-
directamente → acceso al E2)
el resultado en expediente.
B.
Arista A creó las UCC diseñó la 0.45 – 0.85
estructural condiciones tecnología → depende del
bajo las cuales UCIL operó la grado de
B pudo causar planta. habilitación
el resultado. A Institución
no causó diseñó el rol →
directamente subordinadas
sino que accedieron.
habilitó la
causa.
Arista de A tenía la Regulador no 0.15 – 0.55
omisión capacidad de inspeccionó la depende del
impedir el planta de deber y la
resultado y no Bhopal. capacidad
lo hizo. La Gobierno indio

El Cálculo de la Responsabilidad · Apéndices
inacción es no inspeccionó
causalmente condiciones de
relevante. seguridad.
Arista A no tuvo Ex-gerente → 0.00
nula (w = posición fraude en el acreditado
0) causal en el Caso Eje (w = positivamente
resultado. La 0 porque la
ausencia de arista no está
arista es una documentada).
afirmación
positiva que
requiere
evidencia.
Regla de calibración: La pregunta de dirección: "Si este
nodo no hubiera existido o no hubiera actuado como actuó,
¿habría ocurrido el resultado con la misma probabilidad?" Si la
respuesta es sí, la arista es nula. Si es no, la arista existe y su
tipo determina el rango de su intensidad.
1.2 Paso 2: la intensidad de la arista
La intensidad w ∈ [0, 1] es una función de la fuerza de la
evidencia que documenta la relación causal. A mayor
calidad y cantidad de evidencia, mayor w. El criterio no es
subjetivo: se corresponde con tipos de evidencia que tienen
estándares verificables en cada dominio.
La escala de colores del apéndice usa el mismo código en
todas las tablas:
Rango Nivel Descripción general
w
0.75 – Muy alto Evidencia documental directa o
0.95 mecanismo técnico peritado. El
resultado habría sido muy

El Cálculo de la Responsabilidad · Apéndices
significativamente diferente sin este
nodo.
0.55 – Alto Testimonio convergente con
0.74 corroboración documental, o
correlación estadística fuerte
controlada.
0.35 – Moderado Inferencia razonada por posición
0.54 estructural, o testimonio
parcialmente corroborado.
0.15 – Bajo Correlación sin mecanismo
0.34 documentado, o testimonio único
con contexto consistente.
0.05 – Muy bajo Dicho único sin corroboración. El
0.14 resultado puede calcularse pero debe
presentarse como rango.
0.00 Nulo Ausencia de arista acreditada
documentado positivamente. No es simplemente la
ausencia de evidencia: es evidencia
de la ausencia.

El Cálculo de la Responsabilidad · Apéndices
§2. La tabla universal de tipos
de evidencia con rangos
Esta tabla es el instrumento central del apéndice. Define los
nueve tipos de evidencia que el sistema reconoce, el rango
de w que justifica cada uno, y el criterio concreto de uso.
Los ejemplos son todos del libro.
Tipo de Rango Certeza Criterio de uso y
evidencia w ejemplos del libro
E1 — 0.75– Alta Contrato que diseñó el
Documento 0.95 estándar defectuoso.
directo que Correo que instruyó la
muestra la acción. Registro digital
acción del de acceso. Acta de
nodo sobre el resolución de un
resultado consejo. Código de
software auditado.
Casos: UCC/UCIL
(contratos de
seguridad), Caso Eje
(registro digital de las
subordinadas).
E2 — 0.70– Alta Informe pericial que
Mecanismo 0.90 establece la cadena fallo
causal físico o → daño. Autopsia.
técnico Análisis de fallo de
documentado ingeniería. Estudio
pericialmente epidemiológico con
modelo causal. Casos:
O-ring del Challenger
(NASA), dispersión del
MIC en Bhopal.
E3 — 0.55– Media-alta Varios testigos
Testimonio 0.75 independientes
múltiple coinciden y hay al
convergente menos un documento
con respaldo corroborante, aunque

El Cálculo de la Responsabilidad · Apéndices
documental no capture la acción
parcial directa. Casos:
directivos de Morton
Thiokol que recuerdan
la misma reunión con el
mismo contenido.
E4 — 0.50– Media R² > 0.60 en regresión
Correlación 0.70 controlada por las
estadística covariables principales.
controlada Casos: Informe
(estudios Coleman
longitudinales, (R*_entorno_familiar ≈
regresión) 52% a partir de
regresión múltiple),
Redlining (correlación
entre mapas HOLC y
tasas de denegación).
E5 — 0.35– Media- Un solo testigo que
Testimonio 0.55 baja describe la acción del
único con nodo, con al menos un
respaldo documento que es
documental consistente, aunque no
parcial la pruebe directamente.
Casos: testimonios
internos sobre la
cultura de VW antes del
Dieselgate.
E6 — 0.25– Baja- El nodo tenía la
Inferencia 0.45 media posición, los recursos y
razonada por los incentivos para la
posición acción imputada,
estructural del aunque no haya
nodo documentación directa.
La acción es la más
plausible dado el diseño
del sistema. Casos:
gobierno indio en
Bhopal (incentivos a
bajar costos sin
documentación de
instrucción directa).

El Cálculo de la Responsabilidad · Apéndices
E7 — 0.10– Baja Proximidad temporal o
Correlación 0.30 espacial entre la acción
temporal o del nodo y el resultado,
espacial sin sin evidencia del
mecanismo mecanismo de
documentado transmisión. Casos:
hecho 2 del Caso Eje
(acceso al expediente +
fraude dos días
después, sin arista
documentada). USAR
CON NOTACIÓN
EXPLÍCITA.
E8 — Dicho 0.05– Muy baja Un solo testimonio sin
único sin 0.15 ningún corroborante
respaldo de documental, físico ni
ningún tipo estadístico. Casos:
hecho 1 del Caso Eje
(dicho de las
subordinadas de que el
gerente instruyó, sin
respaldo). El sistema
puede calcular R* con
este peso pero el
resultado debe
presentarse como
rango, no como valor
puntual.
E0 — Arista 0.00 Acreditada Se acredita
nula positivamente que el
documentada nodo NO fue
(w = 0 condición del resultado.
explícito) El tipo de arista que el
Caso Eje usa para la
arista ex-gerente →
fraude. Requiere
evidencia de la
ausencia: registros que
muestren que la
información no salió
del sistema, que el nodo
no tenía acceso, etc.

El Cálculo de la Responsabilidad · Apéndices
⚠ La asignación de w NO es un proceso subjetivo libre. Es
una estimación fundamentada en el tipo de evidencia
disponible, con el rango que ese tipo de evidencia justifica. Si
el analista no puede identificar el tipo de evidencia que sustenta
cada arista de su grafo, esa arista no debería estar en el grafo.
Cuando hay múltiples fuentes de distintos tipos: Si para
una misma arista hay tanto evidencia de tipo E1 (documento) como E3
(testimonio convergente), el w se asigna al tipo de mayor calidad (E1 en
este caso). Si hay evidencia de tipos distintos que apuntan en direcciones
opuestas (una fuente dice w alto, otra dice w bajo), se aplica el
procedimiento del §4 de contradicción de fuentes.

El Cálculo de la Responsabilidad · Apéndices
§3. Las matrices de
calibración por dominio
Cada dominio del libro tiene una combinación característica
de tipos de evidencia disponibles, nodos típicos del grafo, y
rangos ajustados por las convenciones probatorias o
metodológicas del campo. Esta sección compila esa
información dominio por dominio.
Para cada dominio se presenta: (a) los nodos típicos del
grafo, (b) el tipo de evidencia dominante, (c) los rangos
específicos de cada arista, y (d) los valores usados en los
casos del libro como referencia verificable.
3.1 Derecho penal y civil (Capítulo 1)
Arista típica Rango Tipo de Nota de calibración
w evidencia
Autor 0.75– E1/E2 Requiere nexo causal
material → 0.92 documentado entre el
resultado acto del autor y el daño.
dañino La autoría material es el
tipo de arista de mayor w
del sistema penal.
Autor 0.60– E1/E3 Comunicación de la
intelectual → 0.85 instrucción (correo,
autor material grabación) → E1.
Testimonio convergente
de los receptores → E3.
Diseñador 0.50– E2/E4 La arista estructural más
del sistema 0.78 importante del Cap.1.
→ autor Ejemplo: el empleador
material que diseñó condiciones
inseguras.

El Cálculo de la Responsabilidad · Apéndices
Cómplice → 0.35– E3/E5 Grado de participación
resultado 0.65 documentado. La
complicidad requiere
evidencia del
conocimiento previo del
resultado probable.
Encubridor 0.25– E5/E6 Más difícil de
→ ocultación 0.55 documentar. Requiere
del daño evidencia de la acción de
ocultación, no solo de su
resultado.
Dicho único 0.05– E8 CASO EJE hecho 1.
sin respaldo 0.20 Usar siempre con
→ conducta notación explícita: "w
asignado con evidencia
E8 sujeta a verificación
adicional".
Arista ex- 0.00 E0 w = 0 documentado.
gerente → No existe ninguna
fraude (Caso evidencia del
Eje) mecanismo de
transmisión.
Declaración explícita
en el expediente.
3.2 PLD y compliance (Capítulo 2)
Arista típica Rango Tipo de Nota de calibración
w evidencia
Operación 0.80– E1 El registro transaccional
inusual → 0.95 es evidencia directa. La
registro arista más sólida del
REINTE dominio.
APNFD → 0.55– E2/E3 Requiere acreditar el
lavado 0.80 conocimiento del
consumado destino probable de los
fondos o activos.

El Cálculo de la Responsabilidad · Apéndices
Institución sin 0.40– E4/E6 La ausencia de
controles → 0.65 controles se documenta
operación con la brecha entre el
indebida programa de
compliance declarado y
el implementado.
Beneficiario 0.30– E4/E6 Difícil de documentar
final → 0.60 cuando el beneficiario
estructura está detrás de capas
corporativas. Se
acredita por inferencia
estructural.
3.3 Derecho internacional y análisis histórico
(Capítulos 3 y 16)
Arista típica Rango Tipo de Nota de calibración
w evidencia
Tratado/acto 0.55– E1/E4 El documento existe
legislativo → 0.80 (E1), pero el
consecuencia mecanismo causal entre
histórica el acto y la
consecuencia histórica
requiere evidencia
estadística o
comparativa (E4).
Estructura 0.35– E4/E6 Análisis comparativo de
sistémica → 0.65 casos análogos. Sistema
evento de alianzas → WWI: w
histórico = 0.42 por
comparación con crisis
de 1905, 1908, 1911.
Detonador 0.05– E6/E7 S histórica alta. El
individual → 0.25 detonador tiene w bajo
cascada precisamente porque la
S del sistema es alta.
Princip → WWI: w =
0.15.

El Cálculo de la Responsabilidad · Apéndices
Estado sucesor 0.20– E1/E6 La continuidad jurídica
→ deuda 0.55 del Estado es E1
histórica (documentable). La
proporción del daño
heredado requiere
análisis estructural (E6).
3.4 Epidemiología y salud pública (Capítulo
6)
Arista típica Rango Tipo de Nota de
w evidencia calibración
Vector → 0.65– E2/E4 Modelo de
infección en red 0.90 transmisión
de contactos calibrado con datos
de contacto. El
número
reproductivo R₀
informa
directamente el w.
Superpropagador 0.55– E2/E4 Contacto
→ brote 0.85 documentado +
confirmación de
cepa idéntica. El
20% de los
individuos produce
el 80% de las
transmisiones en
muchas
enfermedades.
Política sanitaria 0.40– E4/E6 Estudio
deficiente → 0.65 comparativo de
exceso de mortalidad entre
mortalidad poblaciones con y
sin la política.
Diferencia
normalizada por
covariables.

El Cálculo de la Responsabilidad · Apéndices
Factor ambiental 0.35– E4 Regresión
→ incidencia 0.60 controlada por
factores confusos
conocidos. La
causalidad ambiental
requiere dosimetría
cuando es posible.
3.5 Ingeniería de sistemas y análisis de fallos
(Capítulo 12)
Arista típica Rango Tipo de Nota de
w evidencia calibración
Componente físico → 0.80– E1/E2 Informe pericial
fallo técnico 0.95 de ingeniería. El
documentado fallo del O-ring
del Challenger:
w = 0.88 (fallo
documentado
pericialmente
con el análisis
de Morton
Thiokol).
Decisión directiva → 0.65– E1/E3 El
ignorar advertencia 0.88 memorándum
técnica de Boisjoly es
E1. La decisión
de lanzar contra
el consejo
técnico está
documentada en
las actas.
Presión 0.55– E3/E6 Más difícil de
comercial/institucional 0.78 documentar.
→ decisión de lanzar Requiere
testimonios
sobre el
ambiente de la
reunión + la

El Cálculo de la Responsabilidad · Apéndices
estructura de
incentivos de los
directivos.
Diseño original 0.60– E1/E2 El diseño es un
defectuoso → fallo 0.85 documento
sistémico (E1). La
causalidad entre
diseño y fallo
requiere análisis
de ingeniería
(E2).
Regulador → 0.35– E1/E6 Los documentos
aprobación del sistema 0.60 de aprobación
defectuoso son E1. Pero la
arista entre
aprobación y
fallo requiere
demostrar que el
regulador tuvo
acceso a la
información
técnica
relevante.
3.6 Inteligencia artificial y algoritmos
(Capítulo 13)
Arista típica Rango Tipo de Nota de calibración
w evidencia
Diseñador de 0.60– E1/E4 El documento de
la métrica → 0.88 especificación de la
disparate métrica es E1. La
impact conexión entre esa
métrica y el DI
observado se demuestra
con el análisis de
sensibilidad del §6.2 del
Cap. 13.

El Cálculo de la Responsabilidad · Apéndices
Dataset 0.50– E4 Comparación del DI con
histórico 0.75 dataset original vs.
sesgado → dataset debiased. La
resultado del diferencia de DI es el w
modelo de la arista dataset.
Modelo 0.05– E4 S del modelo ≈ 1.0. El w
(algoritmo) 0.15 de la arista modelo es
→ resultado bajo precisamente
sesgado porque cualquier modelo
competente habría
aprendido el mismo
patrón. COMPAS:
w(modelo→sesgo) =
0.08.
Desplegador 0.25– E1/E6 La decisión de desplegar
→ daño de 0.55 es documentable (E1). El
las decisiones grado de conocimiento
previo del sesgo (α del
desplegador) modifica el
w.
3.7 Medio ambiente y ecología (Capítulo 14)
Arista típica Rango Tipo de Nota de
w evidenci calibración
a
Operador directo → 0.70– E1/E2 Registros de
emisión documentada 0.92 producción +
análisis
ambiental
pericial. La
cantidad de
contaminante
emitida es en
principio
medible.
Casa matriz → 0.45– E1/E6 Los
estándares deficientes → 0.78 documentos
daño de aprobación

El Cálculo de la Responsabilidad · Apéndices
de estándares
son E1 (arista
casa matriz →
estándares).
La arista
estándares →
daño es E2
pericial.
Causalidad acumulativa Shaple E2/E4 USAR
(múltiples actores) y SHAPLEY.
La función
v(S) se estima
con datos
periciales de
superposición
de
contaminació
n. Chevron-
Ecuador:
φ_Texaco =
0.237 ×
D_total.
Factor 0.05– E2 S muy alta. El
meteorológico/geográfic 0.25 factor es
o → amplificación exógeno y no
controlable.
Se incluye en
el grafo para
completitud
pero no
produce AD.
3.8 Gobierno corporativo y ego colectivo
(Capítulo 11)
Arista típica Rango Tipo de Nota de calibración
w evidencia
CEO/directivo 0.72– E1/E3 Actas del consejo
→ decisión con 0.92 (E1). Correos internos

El Cálculo de la Responsabilidad · Apéndices
impacto (E1). En ausencia:
documentado testimonios
convergentes de
participantes en la
reunión (E3).
Diseño del 0.50– E1/E4 Los documentos de
sistema de 0.78 compensación son E1.
incentivos → La arista cultura →
cultura → daño daño requiere análisis
longitudinal de
comportamiento (E4).
Consejo de 0.25– E1/E6 Lo que el consejo NO
administración 0.55 hizo es más difícil de
→ omisión de documentar. Se calibra
supervisión por el deber fiduciario
documentado y la
evidencia de que la
información estaba
disponible.
IIC bajo → 0.40– E4 El IIC se calcula con
probabilidad de 0.70 datos públicos. La
colapso arista IIC → colapso
es estadística, calibrada
con el predictor
logístico del Cap. 11.
3.9 Quiebra y riesgo sistémico (Capítulo 9)
Arista típica Rango Tipo de Nota de calibración
w evidencia
Concentración 0.65– E1/E4 Estados financieros
de riesgo (ICRS) 0.88 auditados (E1). La
→ probabilidad relación
de quiebra ICRS→P(quiebra) es
el modelo predictor
calibrado del Cap. 9.
Proveedor 0.55– E1/E4 Contratos
único/cliente 0.80 documentados (E1).

El Cálculo de la Responsabilidad · Apéndices
concentrado → El análisis de
fragilidad sensibilidad de los
flujos (E4) mide la
arista.
Fallo de una 0.50– E4 El w del contagio
institución 0.75 sistémico se estima
sistémica → con modelos de
contagio correlación de activos
y análisis de red del
sistema financiero.
3.10 Score crediticio y discriminación
sistémica (Capítulo 8)
Arista típica Rango Tipo de Nota de calibración
w evidencia
Política 0.70– E1/E4 Los documentos de
institucional 0.90 política de
discriminatoria HOLC/FHA son E1.
→ dataset La correlación entre
sesgado mapas y datos de
denegación es E4.
Redlining: w = 0.82.
Dataset sesgado 0.60– E4 DI antes vs. después
→ score 0.82 del control por el
discriminatorio dataset. La arista se
mide con la diferencia
de DI entre modelo
con dataset original y
con dataset debiased.
Directivo que 0.40– E3/E6 La evidencia de que el
perpetuó el sesgo 0.65 directivo conocía el
→ daño sesgo es clave. Con
continuado conocimiento
confirmado: E3/E1
→ rango superior.
Sin él: E6 → rango
inferior.

El Cálculo de la Responsabilidad · Apéndices
3.11 Seguros y actuaría (Capítulo 10)
Arista típica Rango Tipo de Nota de calibración
w evidencia
Empleador → 0.65– E1/E2 La arista estructural
condición de 0.88 más importante del
riesgo → dominio. Los
siniestro estándares
documentados del
lugar de trabajo son
E1. El nexo con el
siniestro es E2 pericial.
Diseño del 0.55– E1 El contrato es un
contrato → 0.78 documento (E1). El
exclusión análisis actuarial del
injustificada del sesgo entre riesgo real
riesgo y cobertura provista es
E4.
Asegurado → 0.15– E2/E4 La contribución causal
riesgo propio 0.45 del asegurado al
(contribución siniestro es la PAC
causal) (Prima Actuarial Justa).
S alta del asegurado →
w bajo.
3.12 Educación y evaluación docente
(Capítulo 15)
Arista típica Rango Tipo de Nota de calibración
w evidencia
Entorno 0.65– E4 Datos longitudinales
familiar → 0.85 controlados por
resultado covariables. El Informe
educativo Coleman produce w =

El Cálculo de la Responsabilidad · Apéndices
0.72 con R² > 0.65 en
regresión múltiple.
Docente → 0.20– E4 Valor agregado docente
resultado 0.40 calibrado por entorno. El
educativo rango es intencionalmente
(efecto modesto: refleja que
VAM) R*_docente ≈ 10-15%
según la evidencia
acumulada desde
Coleman.
Escuela 0.15– E4 El efecto de la escuela
como 0.35 como institución (sin el
institución docente individual) es
→ resultado pequeño según la
evidencia. La excepción:
liderazgo directivo de alta
calidad puede alcanzar w
= 0.45.
Política 0.10– E4/E6 Efecto difuso y de largo
educativa → 0.30 plazo. Se estima con
estructura estudios de reforma
del sistema educativa natural
→ resultado (variaciones exógenas en
la política).
3.13 Deportes y valor de contribución
(Capítulo 17)
Arista típica Rango Tipo de Nota de calibración
w evidencia
Jugador 0.35– E4 El rango moderado refleja
estrella → 0.65 que, en equipos de
resultado calidad, la S del jugador
(R*_B) estrella es moderada
(Brasil ganó sin Pelé en
1962). El w se calibra con
la diferencia de P(victoria)

El Cálculo de la Responsabilidad · Apéndices
en períodos de ausencia
documentada.
Sistema 0.30– E4 Análisis de rendimiento
táctico → 0.55 bajo distintas
resultado del formaciones. El efecto del
equipo sistema es real pero
requiere varios partidos
para estimarse con
precisión.
Entrenador 0.25– E4 Comparación de
→ resultado 0.50 rendimiento
del equipo antes/después del cambio
de entrenador con calidad
del rival controlada.
Factor azar 0.10– Residual El residual no explicado
(fútbol) 0.25 por los otros nodos. En
fútbol es mayor que en
baloncesto o béisbol por
la menor densidad de
scoring.
3.14 Literatura y análisis narrativo (Capítulo
18)
Arista Rango Tipo de evidencia Nota de
típica w calibración
Nodo 0.55– Textual El análisis textual de
narrativo 0.85 la causalidad
de diseño narrativa es el
→ equivalente literario
evento de la evidencia
central documental. La
pregunta: "¿Sin este
personaje/decisión,
el evento habría
ocurrido en el
mundo del relato?"

El Cálculo de la Responsabilidad · Apéndices
Tywin → Boda
Roja: w = 0.78.
Personaje 0.30– Textual Walder Frey →
ejecutor 0.55 Boda Roja: w =
(visible) 0.55. La ejecución es
→ visible pero la S del
evento ejecutor es
moderada: otro
señor con los
mismos agravios
habría podido actuar
igual bajo las mismas
condiciones.
Hijos del N/A Análisis de hijos Los hijos no son
personaje aristas del grafo: son
→ el análisis de la
decisión disposición de
en el voluntad del
relato personaje en cada
nodo de decisión. Se
aplica el módulo 4
del Apéndice B.
Autor 0.60– Textual/intertextual El w del autor como
como 0.90 nodo de segundo
meta- nivel refleja qué tan
nodo → idiosincrático era el
diseño diseño: Dostoievski
del arco diseñó el arco
Anteros→Harmonía
con S baja (pocos
autores habrían
construido ese arco
específico con esa
precisión).

El Cálculo de la Responsabilidad · Apéndices
§4. Calibración cuando hay
contradicción entre fuentes
La situación más frecuente en los casos reales no es la
ausencia de evidencia sino la contradicción entre fuentes:
un documento apunta a w alto y un testimonio apunta a w
bajo, o dos estudios estadísticos producen estimaciones
distintas. El sistema tiene un procedimiento estándar para
ese caso.
4.1 El principio de la evidencia de mayor
calidad
Cuando hay contradicción entre fuentes de distinto tipo, el
w se asigna según la fuente de mayor tipo (menor número
en la escala E0-E8), no según el promedio. La razón es que
las evidencias de menor calidad son fuentes de ruido, no de
información adicional que promedia con la de mayor
calidad.
Situación Procedimiento Ejemplo del libro
E1 contradice Usar E1. Caso Eje: el registro
E3 (documento Documentar la digital (E1) muestra que
vs. testimonio) contradicción y su las subordinadas
resolución. accedieron al
expediente. El dicho de
que el gerente instruyó
(E8) no contradice E1
sino que lo
complementa con una
afirmación adicional no
acreditada.
E4 contradice Usar el estudio de Informe Coleman:
E4 (dos mayor calidad varias réplicas producen
metodológica. Si R*_entorno entre 40% y

El Cálculo de la Responsabilidad · Apéndices
estudios son comparables, 55%. El análisis usa el
estadísticos) presentar el rango. rango con el valor
central de 52% del
estudio original.
E3 contradice Reducir el w al Testigos de la reunión
E3 (testimonios rango E5-E6 y de Morton Thiokol que
convergentes documentar la recuerdan el contenido
que se inconsistencia. de manera distinta. El w
contradicen) de esa arista cae al rango
E5 y se presenta como
rango, no como valor
puntual.
E1 apunta a w Documentar la Caso Eje hecho 2: el
= 0 pero E6 arista nula registro digital muestra
apunta a w explícitamente y que la información no
positivo señalar que E6 es salió del sistema (E1 →
insuficiente para w = 0). La proximidad
revertirla. temporal de dos días
(E7) no revierte la arista
nula.
4.2 El procedimiento de rango cuando la
contradicción no se puede resolver
Cuando la contradicción entre fuentes es genuina y no
resoluble con el principio de la evidencia de mayor calidad,
el sistema usa el procedimiento de rango: en lugar de asignar
un valor puntual w, se asigna un intervalo [w_min, w_max]
y se calcula R* para ambos extremos del intervalo.
R*_rango = [R*(W con w_min), R*(W con w_max)]
Si los dos extremos producen el mismo nodo de mayor R*,
el resultado es robusto a la contradicción. Si producen
nodos distintos, la contradicción es sustantiva y debe
documentarse explícitamente: el análisis produce dos
distribuciones de responsabilidad que corresponden a las
dos interpretaciones de la evidencia.

El Cálculo de la Responsabilidad · Apéndices
Regla de calibración: Un análisis que asigna valores
puntuales cuando la evidencia es contradictoria es menos
honesto que uno que asigna rangos. El rango no es una señal
de debilidad metodológica: es la representación correcta de la
incertidumbre real del análisis.

El Cálculo de la Responsabilidad · Apéndices
§5. La W = 0 explícita:
cuándo se justifica y cómo se
documenta
La arista nula w = 0 es la declaración más poderosa del grafo
causal: afirma que un nodo no tiene posición causal en el
resultado. En el Caso Eje, la arista w (ex-gerente → fraude)
= 0 es la declaración que hace que el tipo penal no se
configure. Por eso requiere el estándar de documentación
más alto del apéndice.
5.1 La diferencia entre ausencia de evidencia
y evidencia de ausencia
La arista nula no es simplemente la ausencia de evidencia de
que el nodo causó el resultado. Es evidencia positiva de que
no lo causó. Esa distinción es fundamental para el análisis
en expedientes reales:
Situación Interpretación w correcto
correcta
No hay evidencia de Incertidumbre. El Rango bajo: E6-
que el nodo causó el w no puede E7, con w ∈
resultado determinarse con [0.05–0.25]. NO
la evidencia w = 0.
disponible.
Hay evidencia de La arista existe E7: w ∈ [0.10–
que el nodo actuó pero su intensidad 0.30]. Solo se usa
pero no de que esa es baja. w = 0 si hay
acción causó el evidencia del
resultado mecanismo
alternativo.

El Cálculo de la Responsabilidad · Apéndices
Hay evidencia de Arista nula E0: w = 0.
que la acción del documentada. w = Requiere
nodo no pudo haber 0 explícito. documentar la
causado el resultado evidencia de la
(alternativa ausencia, no solo
documentada) la ausencia de
evidencia.
5.2 Los cuatro tipos de evidencia que
justifican w = 0

### 1. Evidencia de la imposibilidad técnica: el nodo no tenía
acceso técnico al mecanismo de transmisión. En el
Caso Eje: si el registro digital muestra que el ex-gerente
no accedió al expediente (a diferencia del registro que
muestra que las subordinadas sí lo hicieron), esa arista
tiene w = 0 por imposibilidad técnica.

### 2. Evidencia del mecanismo alternativo: existe un
mecanismo alternativo que explica completamente el
resultado sin necesidad del nodo. En el hecho 2 del
Caso Eje: si el tercero que intentó el fraude tenía una
fuente alternativa de la información (robo de cartera,
darkweb, filtración de otra sucursal), el mecanismo
alternativo elimina la necesidad de la arista gerente →
fraude.

### 3. Evidencia de la separación temporal o espacial que
excluye el mecanismo: la distancia entre el acto del
nodo y el resultado es tan grande que ningún
mecanismo causal plausible puede conectarlos.
Requiere análisis del mecanismo específico para cada
caso.

### 4. Evidencia directa de la no-acción: un registro que
documenta positivamente que el nodo no realizó la
acción que se le imputa. El más sólido y el más
frecuentemente ausente en los expedientes reales.

El Cálculo de la Responsabilidad · Apéndices
⚠ La asignación de w = 0 sin documentación explícita es el
error más grave de calibración del grafo causal. Si el análisis usa
w = 0 para exonerar a un nodo, esa declaración debe estar tan
documentada como cualquier otra arista del grafo. Un w = 0
sin fundamento es tan injustificado como un w = 0.90 sin
evidencia.

El Cálculo de la Responsabilidad · Apéndices
§6. Cómo documentar la
calibración en un expediente
real
Este es el apartado más práctico del apéndice. Responde a
la pregunta: "Apliqué el sistema a mi caso, asigné los pesos
W, obtuve los R* y Δ. Ahora tengo que presentar ese
análisis ante un juez / árbitro / consejo de administración
/ regulador. ¿Cómo lo documento para que sea verificable
y defendible?"
6.1 El estándar de documentación por nivel
de foro
Foro Estándar de Qué debe documentar
presentación el analista
Proceso penal Estándar (1) Cada arista con su
probatorio de tipo de evidencia E1-E8
"más allá de duda identificado. (2) El w
razonable" para la asignado y el rango del
arista directa. El tipo de evidencia. (3) La
análisis causal fuente documental
apoya pero no específica que justifica
sustituye la prueba cada arista. (4) Las aristas
del tipo penal. nulas con su fundamento
explícito.
Litigio civil / Estándar de (1) -(4) del proceso
arbitraje "balance de penal. Adicionalmente:
probabilidades". (5) Análisis de
El análisis causal sensibilidad que muestre
puede ser que el resultado es
presentado como robusto a variaciones
peritaje experto. razonables del w. (6)
Comparación con
valores análogos usados

El Cálculo de la Responsabilidad · Apéndices
en el libro para casos
similares.
Regulatorio / El estándar varía (1) -(6) anteriores.
administrativo por regulador. En Adicionalmente: (7)
general: Descripción del método
preponderancia de de cálculo de R*
evidencia + suficiente para que el
razonabilidad del regulador lo replique
método. independientemente.
Consejo de Estándar de Versión simplificada: (1)
administración razonabilidad Grafo con los pesos
/ directorio empresarial. El visibles. (2) Tabla de R*
análisis debe ser y Δ. (3) Fuentes de cada
comprensible para peso en lenguaje
directores no ejecutivo (no técnico). El
técnicos. código Python del
Apéndice B como
respaldo.
6.2 La hoja de calibración: el documento de
trabajo que justifica la W
Para cada expediente, el analista debe producir una "hoja de
calibración" que documente cada arista del grafo. Este es el
formato estándar:
Arista Nodo w Tip Fuente Observaci
origen asigna o E documen ones y
→ do tal / limitacion
destino evidenci es
a
Ej. Caso Institució 0.80 E1 Diseño El w refleja
Eje n → del la arista
Subordin sistema estructural:
adas de acceso la
document institución
ado en el habilitó el

El Cálculo de la Responsabilidad · Apéndices
manual acceso, no
del lo ejecutó
usuario directament
(ref. e. Si fuera

### Anexo 3). E1 directo:
Contrato w = 0.88.
laboral de
las
subordina
das (ref.

### Anexo 1).
Ej. Caso Ex- 0.00 E0 Registro Arista nula
Eje gerente de salida documenta
→ de da. La
Fraude informaci proximidad
(hecho 2) ón: temporal de
ningún 2 días (E7)
registro es
muestra insuficiente
transmisi para
ón al revertir la
exterior evidencia
(ref. técnica. Ver
Pericial §5 de este
informáti apéndice.
ca, Anexo
7). Fraude
en estado
diferente
sin rastro
de
conexión.
Compl ... ... ... ... ...
etar por
caso
Para el expediente: La hoja de calibración debe acompañar
como anexo técnico al análisis de R*. Sin ella, el resultado
numérico es un número sin fundamento. Con ella, cada w es
una afirmación verificable que el adversario puede impugnar
con evidencia contraria — que es exactamente el tipo de debate

El Cálculo de la Responsabilidad · Apéndices
que el sistema busca producir: uno sobre los hechos, no sobre
la metodología.
6.3 Cómo responder la impugnación del w
En cualquier foro adversarial, la contraparte intentará
impugnar los valores w del grafo. Hay tres tipos de
impugnación y una respuesta estándar para cada uno:
Tipo de Argumento Respuesta estándar
impugnación típico de la
contraparte
Impugnación "El peso E3 Mostrar el criterio de
del tipo de que usó es clasificación del §2 de este
evidencia especulativo; apéndice. Señalar que el w
debería ser asignado es el rango inferior
E7." del tipo E3 (0.55), no el
superior. Ofrecer hacer el
análisis con E7 y mostrar que
el resultado cualitativo es el
mismo (análisis de
sensibilidad).
Impugnación "El w = 0.80 Presentar el análisis de
del valor es arbitrario; sensibilidad: calcular R* con
puntual debería ser w = 0.55 y con w = 0.80 y
0.55." mostrar la diferencia. Si el
nodo de mayor R* es el
mismo en ambos casos, el
argumento de la contraparte
no cambia la conclusión. Si
produce nodos distintos,
documentar el rango.
Impugnación "La ausencia La respuesta correcta: una
de la arista de evidencia arista nula requiere evidencia
nula no prueba que de la ausencia, no solo
la arista sea ausencia de evidencia (§5.1).
cero." Si la documentación incluye
evidencia positiva de la
imposibilidad técnica o del

El Cálculo de la Responsabilidad · Apéndices
mecanismo alternativo, la
impugnación no tiene base. Si
no la incluye, el w debe
subirse a E7 y documentarse
la incertidumbre.
Impugnación "El eigenvector El sistema es transparente: el
del método dominante no Apéndice A demuestra la
es el único convergencia. El Apéndice B
método para contiene el código ejecutable.
calcular R*." Ofrecer al foro ejecutar el
código con los datos del
expediente para replicar el
resultado. La replicabilidad es
la mejor defensa del método.

El Cálculo de la Responsabilidad · Apéndices
§7. Casos de prueba con
solución
Esta sección permite al lector verificar su comprensión del
sistema de calibración. Para cada caso se presenta un grafo
con los nodos y la descripción de la evidencia disponible,
pero sin los valores w. El lector asigna sus propios valores
y luego compara con la calibración del libro.
Caso de prueba 1 — Accidente laboral
Descripción:
Un trabajador de una empresa de manufactura sufre una
lesión grave al operar una máquina. Los hechos
documentados son: (a) el manual de operación de la
máquina indica que debe usarse con protección específica;
(b) el supervisor del turno no verificó que el trabajador
usara la protección al inicio del turno, lo cual está
documentado en el registro de seguridad firmado por el
supervisor; (c) el trabajador declaró que nunca recibió
capacitación formal sobre el uso de la protección; (d) el área
de RRHH tiene un registro de que el trabajador completó
el módulo de seguridad en plataforma digital, pero el
trabajador argumenta que lo completó sin haber operado
nunca la máquina real.
Nodos del grafo:
• N1 — Empresa (diseño del programa de capacitación)
• N2 — Supervisor del turno (verificación de seguridad)
• N3 — Trabajador (uso de la máquina)
• Nf — Lesión

El Cálculo de la Responsabilidad · Apéndices
Asigne w para las aristas: N1→Nf, N2→Nf, N3→Nf
Solución calibrada (valores del sistema):
Arista w Tipo Fundamento
calibrado E
N1 → Nf 0.72 E1/E6 E1: el manual existe y
(empresa → requiere protección. E6: la
lesión) evidencia de que la
capacitación real era
insuficiente (módulo digital
vs. práctica real) es una
inferencia estructural. w =
0.72 = extremo superior de
la arista estructural bien
documentada.
N2 → Nf 0.65 E1 E1 directo: el registro
(supervisor firmado por el supervisor
→ lesión) documenta que no verificó
la protección. Esta es la
arista más sólida del grafo
porque la omisión está
documentada en un registro
institucional.
N3 → Nf 0.35 E5/E6 S alta: cualquier trabajador
(trabajador sin capacitación práctica
→ lesión) habría actuado igual. La
contribución del trabajador
existe pero es la de menor
R* neto porque la S es alta y
la capacitación era
responsabilidad de N1.
R*_N1 ≈ 42% · R*_N2 ≈ 35% · R*_N3 ≈ 23%
El resultado más importante: el nodo de mayor R* es la
empresa (diseño del programa de capacitación), no el
supervisor ni el trabajador. Eso no exonera al supervisor (Δ

El Cálculo de la Responsabilidad · Apéndices
positivo si su α es bajo) pero distribuye la responsabilidad
de manera proporcional a la posición causal real.
Caso de prueba 2 — Decisión financiera con
información asimétrica
Descripción:
Un cliente de un banco contrata un producto de inversión
estructurado que resulta en pérdida del 60% del capital. Los
hechos documentados son: (a) el contrato incluye una
cláusula de riesgo en letra pequeña en la página 14 de 18;
(b) el asesor financiero firmó un formulario de idoneidad
en el que marcó que el cliente tenía "perfil de riesgo
moderado" aunque el cliente era jubilado con ingresos fijos;
(c) el asesor tenía un esquema de comisión que era el doble
para este producto que para los alternativos equivalentes;
(d) el cliente no leyó el contrato completo.
Nodos: N1 = banco (diseño del producto), N2 = asesor
(venta), N3 = esquema de incentivos, N4 = cliente
Solución calibrada:
Arista w Tipo Fundamento
calibrado E
N1 → Pérdida del 0.68 E1/E6 El diseño del
cliente producto con riesgo
no divulgado
adecuadamente
(cláusula en pág. 14
de 18) es E1 parcial.
La causalidad entre

El Cálculo de la Responsabilidad · Apéndices
ese diseño y la
pérdida requiere E6.
N3 (incentivos) 0.75 E1 El esquema de
→ N2 comisiones es un
(comportamiento documento E1. La
asesor) arista es alta porque el
incentivo doble es
una condición
estructural que
determina el
comportamiento del
asesor con alta S.
N2 → Venta 0.60 E1 El formulario de
inadecuada idoneidad mal
completado es E1
directo. El w es alto
pero la S también es
moderada (otro
asesor bajo el mismo
esquema habría
actuado igual).
N4 (cliente) → 0.18 E6 El cliente no leyó el
pérdida propia contrato. Pero la S es
altísima: la asimetría
de información era
tan marcada que
cualquier cliente
razonable habría
tomado la misma
decisión.
R*_N1 ≈ 38% · R*_N3+N2 ≈ 45% · R*_N4 ≈ 17%

El Cálculo de la Responsabilidad · Apéndices
