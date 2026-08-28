## PARTE III · Ciencias de la Salud y Biomédicas

### Capítulo 21
Epidemiología y salud pública —
causalidad a escala poblacional
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es compilación directa del cap. 6 de El cálculo de la
responsabilidad (Epidemiología y salud pública). Organiza los conceptos del
dominio en la estructura §1–§9 de la Taxonomía y añade la escala EP0–
EP8, que es la versión operativa de la escala E0–E8 para el vocabulario
epidemiológico.
El dominio tiene tres características singulares que lo distinguen de todos los
otros capítulos del libro. Primera: los nodos del grafo son tanto personas como
estructuras físicas, espacios e instituciones — la bomba de agua, el sistema de
alcantarillado, la política de cuarentena son todos nodos con R* real. Segunda:
los Hijos de Afrodita aplican únicamente a los superpropagadores con
voluntad propia — no a los nodos estructurales. Tercera: el dominio tiene
valor tanto retrospectivo (para distribuir responsabilidad) como prospectivo
(para diseñar intervenciones). Si tu prioridad es el análisis de responsabilidad
institucional, ve a §4 y §7. Para el análisis de superpropagadores, ve a §3.
Para el fraude annona epidemiológico, ve a §7. Para la prioridad de evidencia,
ve directamente a §9.
§1 Descripción del subcampo
La epidemiología es el dominio donde el daño se produce a
escala poblacional. Un brote epidémico no es el resultado de
una sola decisión individual identificable: es la consecuencia

Taxonomía General de Aplicaciones
de la interacción entre nodos de múltiples niveles —
individuos infectados, espacios de transmisión, sistemas de
vigilancia, políticas de salud pública — que contribuyen
causalmente a la escala del daño con pesos muy distintos. La
herramienta que el análisis causal aporta a la epidemiología es
exactamente la que el dominio necesita y el R₀ convencional
no provee: la distribución del peso causal entre los nodos del
grafo, que permite identificar qué intervención tiene mayor
impacto por unidad de recursos invertida.
El error más frecuente en el análisis epidemiológico — tanto
en la investigación académica como en la política pública —
es reducir el grafo al nivel individual. Cuando el análisis solo
incluye casos de personas infectadas y sus contactos, produce
un R* que sobreestima la responsabilidad causal de los casos
individuales y subestima o no detecta la responsabilidad del
sistema de salud pública. Los brotes de mayor escala en la
historia moderna tuvieron siempre nodos estructurales con R*
alto que no fueron los casos individuales. John Snow lo
demostró en 1854 sin el formalismo matemático: el nodo de
mayor R* en el cólera de Broad Street no era ninguno de los
616 muertos ni ninguno de los supervivientes — era la bomba
de agua.
El fraude annona epidemiológico: cuando el Estado tiene R* alto
y α bajo
El fraude annona epidemiológico es la forma específica del incumplimiento del
Estado en el dominio de la salud pública: el Estado tiene R* alto en el grafo
de un brote (las condiciones que no generó fueron causalmente necesarias para
que el brote alcanzara la escala que alcanzó) y su α es bajo (no las generó
estando a su alcance hacerlo).
El concepto es analíticamente poderoso porque permite distinguir entre brotes
que eran inevitables dado el estado del conocimiento y de las tecnologías
disponibles (R* del Estado bajo porque no había intervención posible) y brotes
que habrían podido ser mucho menores si el Estado hubiera generado las
condiciones que estaban a su alcance (R* del Estado alto y Δ positivo).
FA_epi = R*_Estado × D_total × (1 − α_Estado) es la medida del
fraude annona epidemiológico — la base para calcular la responsabilidad del
Estado en demandas colectivas por negligencia en la respuesta y para establecer
el presupuesto mínimo de inversión en salud pública que el sistema requiere.

Taxonomía General de Aplicaciones
Sub-variantes del dominio
Análisis de brotes con fuente ambiental identificable (Tipo
Snow): el nodo de mayor R* es un factor ambiental o de
infraestructura — bomba de agua contaminada, sistema de
ventilación deficiente, agua potable sin tratamiento. El grafo
tiene estructura relativamente simple con un nodo dominante
identificable mediante la variación espacial de los casos. Es el
dominio más favorable para el análisis causal retrospectivo
porque el contrafáctico es claro: sin ese nodo específico, el
brote habría sido radicalmente menor.
Análisis de pandemias con estructura causal compleja (Tipo
COVID-19): el grafo incluye nodos en múltiples escalas
(molecular, individual, comunitario, nacional, global) y el R*
está distribuido entre múltiples nodos con incertidumbre. El
análisis debe seleccionar los nodos más relevantes para la
pregunta específica. Su mayor valor es distinguir los nodos con
Δ positivo significativo (incumplimiento real del sistema) de
los nodos donde la incertidumbre genuina del momento de las
decisiones limita la atribución de responsabilidad.
Análisis de superpropagadores: el análisis de los nodos
individuales de alta transmisión. El instrumento central es el
índice de sustituibilidad S del superpropagador: si S es alto
(cualquier persona con la misma carga viral en ese mismo
entorno habría transmitido igual), la intervención correcta es
sobre el entorno, no sobre la persona. Si S es bajo (las
características idiosincráticas del superpropagador — su
posición en la red de contactos, su actividad laboral, su nivel
de exposición — fueron causalmente determinantes), hay más
base para la intervención individual.
Análisis de equidad en la respuesta: la distribución del daño del
brote entre grupos sociales está determinada no solo por la
biología del patógeno sino por las condiciones estructurales
que determinan la exposición, el acceso al tratamiento y la
capacidad de aislamiento. El análisis de los nodos estructurales
(condiciones de trabajo, acceso a cobertura de aislamiento,

Taxonomía General de Aplicaciones
densidad habitacional, acceso a sistemas de salud de calidad)
establece qué factores amplifican el daño en los grupos más
vulnerables y cuál es el R* del diseñador de esas condiciones
en la distribución desigual del daño.
Evaluación de intervenciones de salud pública: el uso
prospectivo del análisis causal para establecer qué intervención
tiene mayor impacto por unidad de recursos:
Impacto_intervención_i ∝ R*_i × (1 − S_i). La intervención
sobre el nodo de mayor R* × (1−S) — el nodo de mayor
necesidad causal idiosincrática — produce el mayor impacto
en la reducción del brote por unidad de recursos invertida.
§2 Escala de evidencia EP0–EP8 ·
Epidemiología y salud pública
La escala EP0–EP8 traduce la jerarquía general E0–E8 al
vocabulario epidemiológico. Su característica más relevante es
la posición central de la secuenciación genómica del patógeno
(EP1) y del análisis de brote con variación espacial y temporal
(EP2) — los instrumentos que en epidemiología cumplen el
rol que la documentación jurídica cumple en los dominios del
derecho. La compilación directa de El cálculo de la
responsabilidad cap. 6 calibra los rangos empíricamente desde
la práctica epidemiológica.
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio
evidencia w
epidemiológico
EP1 Evidencia Secuenciación genómica que [0.74,
genómica y de vincula directamente las 0.92]
laboratorio cepas de los casos en una
directa del cadena de transmisión; datos
patógeno y la de carga viral documentados
transmisión por laboratorio; cultivos del
patógeno que establecen la
fuente ambiental; análisis de
biología molecular que
establece el mecanismo de

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio
evidencia w
epidemiológico
transmisión. Es el
instrumento más directo
para establecer quién
transmitió a quién con
certeza molecular.
EP2 Estudio Estudio de brote con [0.65,
epidemiológico variación espacial y temporal 0.85]
con análisis que establece el nodo
causal robusto ambiental de mayor R*
(análogo al método de John
Snow); análisis multivariado
que controla por factores
confusos para aislar la
contribución causal de un
nodo específico; estudio de
cohorte con seguimiento que
establece el efecto de una
intervención de salud pública
sobre la tasa de transmisión
secundaria; modelamiento
epidemiológico con
estimación de R* por nodo
con intervalos de confianza.
EP3 Rastreo de Cadena de transmisión [0.48,
contactos reconstruida mediante 0.66]
documentado rastreo activo de contactos,
con con al menos corroboración
corroboración genómica parcial de los
de laboratorio eslabones clave. En brotes
con múltiples
superpropagadores: el
análisis de clúster que
identifica los nodos de mayor
transmisión secundaria con
datos de rastreo consistentes
entre investigadores.
EP4 Análisis Análisis de la distribución [0.38,
estadístico del espacial y temporal de los 0.58]
patrón de casos casos que establece la
con control de asociación entre el nodo
confusos analizado y la escala del
brote, con control por las

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio
evidencia w
epidemiológico
características demográficas
y socioeconómicas de la
población afectada; análisis
de regresión que establece el
impacto de una política de
salud pública sobre las tasas
de incidencia controlando
por la evolución temporal del
brote.
EP5 Análisis de la Documentación de la [0.28,
capacidad de cronología de las decisiones 0.48]
respuesta de salud pública — cuándo
institucional y se activó la alerta, cuándo se
cronología de implementaron las medidas
decisiones de contención, cuándo se
comunicó el riesgo — versus
la cronología del brote, que
establece si las decisiones
fueron causalmente
tempranas o tardías respecto
al momento de mayor
impacto posible.
EP6 Inferencia desde El sistema de salud pública [0.18,
la estructura del tenía la posición 0.38]
sistema de salud institucional, los recursos y
pública y el los instrumentos para haber
estado del actuado de manera que
conocimiento habría reducido el daño,
dado el estado del
conocimiento disponible al
momento de las decisiones.
Sin documentación directa
de las decisiones específicas.
EP7 Correlación El evento o la decisión [0.07,
temporal entre el coincide temporalmente con 0.24]
evento o la el cambio en la tasa de
decisión y el transmisión sin análisis que
cambio en la tasa establezca la cadena causal
de transmisión versus factores confusos.
EP8 Fuente única o Un solo caso documentado o [0.04,
evidencia un testimonio sin 0.16]

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio
evidencia w
epidemiológico
anecdótica sin corroboración
corroboración epidemiológica sistemática.
epidemiológica
EP0 Ausencia Análisis EP2 que establece w =
documentada de que el resultado del brote 0.00
posición causal habría sido el mismo sin el
del nodo en la nodo analizado dado el
escala del brote estado del sistema de
transmisión — el nodo era
causalmente irrelevante para
la escala del daño, o las
acciones del actor
institucional ya
implementaban las mejores
prácticas disponibles en el
estado del arte del momento.
R₀ versus R*: instrumentos complementarios para
preguntas distintas
R₀ (número básico de reproducción) y R* (vector de peso causal) son
instrumentos complementarios, no sustitutos. R₀ mide el número promedio de
infecciones secundarias en una población totalmente susceptible — es un
escalar que describe la dinámica global del brote. R* distribuye el peso causal
del brote entre los nodos del grafo — es un vector que establece cuáles nodos
son causalmente críticos y cuáles son reemplazables.
R₀ alto con R* concentrado en pocos nodos (como en el cólera de 1854 con la
bomba de Broad Street) sugiere que intervenir en esos nodos reducirá el brote
eficientemente. R₀ alto con R* distribuido (como en COVID-19 con múltiples
nodos en múltiples escalas) sugiere que se necesita intervención en múltiples
frentes simultáneamente. La correlación entre superpropagación (patrón
80/20 documentado en muchos patógenos) y R* concentrado es directa: un
parámetro de dispersión k pequeño en la distribución del número de infecciones
secundarias corresponde a R* concentrado en pocos nodos.

Taxonomía General de Aplicaciones
§3 Firmas documentales por Hijo · Solo
aplica a superpropagadores con voluntad
propia
En el dominio epidemiológico, los Hijos de Afrodita tienen un
alcance más restringido que en todos los demás capítulos del
libro: aplican exclusivamente a los superpropagadores
identificados con voluntad propia. No se calculan para los
nodos estructurales (el sistema de agua, la ventilación del
espacio, la política de cuarentena) porque esos nodos no
tienen disposición de voluntad individual. No aplican tampoco
a la OMS como institución ni al Estado como nodo normativo
en el análisis del brote a escala poblacional — esos nodos
tienen R* real, α mensurable y Δ calculable, pero sus Hijos
pertenecen al análisis de gobierno corporativo de sus
directivos (cap. 13) o al análisis de responsabilidad individual
(cap. 1).
La distinción más importante que los Hijos aportan al análisis
epidemiológico es entre el superpropagador que actuó desde
Fobos (miedo a reportar, miedo a perder el empleo si se aísla,
miedo al estigma) y el que actuó desde Anteros (negación
deliberada de las medidas de protección) o Deimos (parálisis
ante la incertidumbre sobre si estaba realmente infectado).
Esta distinción cambia radicalmente la política de intervención
recomendada.
Mapa de Hijos de los superpropagadores y sus
implicaciones para la política de salud pública
Qué α Error
Hijo Política
describe predicho frecuente
dominant de
en el si la de
e del intervenc
contexto intervenc respuesta
superprop ión
epidemiol ión es institucio
agador correcta
ógico adecuada nal
Fobos El Eliminar Alto si se Sancionar
superprop las eliminan al

Taxonomía General de Aplicaciones
Qué α Error
Hijo Política
describe predicho frecuente
dominant de
en el si la de
e del intervenc
contexto intervenc respuesta
superprop ión
epidemiol ión es institucio
agador correcta
ógico adecuada nal
agador barreras al las superprop
transmitió aislamient barreras agador
porque o: subsidio estructural individual
tenía de días es al mente en
miedo a las perdidos, aislamient lugar de
consecuen protecció o. El α abordar el
cias de n del sube nodo
aislarse: empleo, cuando el estructural
perder el provisión Fobos (condicion
empleo o de disminuye es
el ingreso, alojamient , no laborales)
el estigma o de cuando la que
de ser aislamient sanción determinó
identificad o para aumenta. su
o como quienes no conducta.
caso pueden Esto
positivo, aislarse en produce el
las casa, resultado
consecuen equipo de más
cias protecció injusto y el
laborales n menos
del adecuado, eficaz:
aislamient canales de penaliza a
o. No reporte quien
quiso anónimos. tenía
transmitir: La sanción menos
no pudo al opciones.
dejar de superprop
hacerlo agador
dadas las con Fobos
condicione dominant
s e refuerza
estructural el Fobos y
es que el reduce el α
sistema no futuro.
cambió. El
trabajador
esencial sin
cobertura
de días
perdidos es
el caso

Taxonomía General de Aplicaciones
Qué α Error
Hijo Política
describe predicho frecuente
dominant de
en el si la de
e del intervenc
contexto intervenc respuesta
superprop ión
epidemiol ión es institucio
agador correcta
ógico adecuada nal
paradigmát
ico.
Deimos El Acceso Alto si se Culpabiliz
superprop fácil y provee el ar al
agador no rápido a marco superprop
reconoció diagnóstic informativ agador
sus o. o y de por
síntomas Comunica acceso. El ignorancia
como ción clara Deimos es cuando el
infección, sobre la más sistema no
no síntomas y reformabl había
entendía el protocolo e de las generado
protocolo de acción. disposicio el acceso
de Reducción nes: al
aislamient de las desaparec diagnóstic
o, no tenía barreras e con la o ni la
acceso al de acceso provisión comunica
diagnóstic al sistema de ción clara.
o necesario de salud. estructura El
para El adecuada. Deimos
confirmar Deimos se del
si debía transform superprop
aislarse. a en agador
No hubo Harmonía tiene un Δ
transgresió cuando se del Estado
n provee el como
deliberada: marco que espejo: el
hubo faltó. Estado no
ausencia generó las
del marco condicion
que habría es que
permitido habrían
actuar convertid
diferente. o al
Deimos
en
Harmonía
.
Potós El Normas Moderado Tratar el
superprop de grupo -alto con Potós

Taxonomía General de Aplicaciones
Qué α Error
Hijo Política
describe predicho frecuente
dominant de
en el si la de
e del intervenc
contexto intervenc respuesta
superprop ión
epidemiol ión es institucio
agador correcta
ógico adecuada nal
agador que hacen intervenci como
siguió las que el ones de Anteros e
normas aislamient norma imponer
sociales y o y la social. El sanciones
los protecció Potós que
comporta n sean el responde alienan a la
mientos comporta al campo comunida
previos a la miento cultural d y
pandemia esperado más que a reducen la
sin integrar socialmen las cooperaci
la te, no la sanciones ón futura.
informació excepción. individual O tratar el
n nueva Los es. Potós
sobre el incentivos como
riesgo. La positivos Deimos e
inercia para la ignorar
comporta cooperaci que la
mental ón son persona sí
determinó más tenía
la eficaces informaci
conducta: que las ón
asistió al sanciones. disponible
evento La — solo
social, comunica que el
siguió con ción que campo
su rutina, reformula social no
no las la había
actualizó medidas integrado.
su como
comporta norma de
miento grupo
porque el reduce el
campo Potós.
cultural de
su entorno
social
tampoco
había
actualizado
.

Taxonomía General de Aplicaciones
Qué α Error
Hijo Política
describe predicho frecuente
dominant de
en el si la de
e del intervenc
contexto intervenc respuesta
superprop ión
epidemiol ión es institucio
agador correcta
ógico adecuada nal
Anteros El Normas Bajo sin Tratar el
superprop de pares cambio Anteros
agador dentro del del como el
rechazó grupo contexto problema
activament social del identitario dominant
e las superprop . El e de la
medidas de agador Anteros es respuesta
protección que hacen la cuando en
— que la disposició realidad es
negación cooperaci n más la minoría
deliberada ón sea la resistente de los
del uso de norma del a las casos. La
equipo de grupo. intervenci sobre-
protección Framing ones atención
, de las directas. institucion
resistencia medidas al al
activa al como Anteros
aislamient afirmació produce
o, difusión n de la narrativas
intencional autonomía de guerra
de individual cultural
desinform y de la que
ación responsab refuerzan
sobre el ilidad la
brote. comunitar identidad
Minoría de ia. Evitar negacionis
los casos, la ta y
pero alta confronta amplían su
visibilidad. ción impacto
La institucion social.
confrontac al directa.
ión directa La
de las reducción
institucion del
es refuerza Anteros
la requiere
identidad transform
del ación del
Anteros: lo sesgo
hace más identitario
visible y , no

Taxonomía General de Aplicaciones
Qué α Error
Hijo Política
describe predicho frecuente
dominant de
en el si la de
e del intervenc
contexto intervenc respuesta
superprop ión
epidemiol ión es institucio
agador correcta
ógico adecuada nal
más presión
resolutivo. directa.
Harmonía El Reconoce Alto Culpabiliz
superprop r y (0.70– ar
agador reforzar 1.00). Este retroactiva
cooperó públicame superprop mente a
activament nte la agador quien
e con todas cooperaci maximizó cooperó
las ón. Las su α dado de buena
medidas políticas el fe, pero
disponible que tratan conocimie transmitió
s: se aisló igualment nto por
en cuanto e a quien disponible razones
identificó cooperó y . fuera de su
síntomas, a quien no control
notificó desincenti (carga
exhaustiva van la viral pre-
mente sus cooperaci sintomátic
contactos, ón futura. a, periodo
cooperó El de
con el reconocim incubació
rastreo, iento de la n). Esto
usó el Harmonía destruye la
equipo de tiene valor confianza
protección de norma en el
adecuado. social: sistema de
Puede aun muestra salud
así haber que el pública y
transmitid comporta reduce la
o por carga miento cooperaci
viral cooperativ ón futura.
excepciona o es el que
lmente alta la
o por comunida
transmisió d valora.
n pre-
sintomátic
a
inevitable.

Taxonomía General de Aplicaciones
El principio de equidad epidemiológica basado en los
Hijos
Una política de salud pública justa distingue entre el superpropagador que
transmitió desde Fobos (las condiciones estructurales le impidieron actuar de
otro modo) y el que lo hizo desde Anteros (eligió actuar contra las medidas).
Ambos tienen el mismo R*, pero sus Δ son diferentes: el que actuó desde
Fobos tiene Δ positivo porque el sistema de salud pública no generó las
condiciones para que pudiera aislarse — eso es fraude annona del Estado
hacia el trabajador que perdería el empleo si se aislaba. El que actuó desde
Anteros tiene Δ positivo por elección propia. La política de intervención debe
ser estructuralmente distinta en cada caso: el primero requiere reforma del
sistema; el segundo requiere reforma del contexto identitario de su comunidad.
§4 ¿Qué cuenta como asunción (α) en el
dominio epidemiológico?
α en el dominio epidemiológico tiene dos niveles de aplicación
con lógicas distintas. El α individual mide lo que el
superpropagador con voluntad hizo para interrumpir las
cadenas de transmisión que dependían de él. El α
institucional/estatal mide lo que el sistema de salud pública
generó — las condiciones materiales que habrían reducido la
transmisión — proporcional a su R* y a su capacidad.
El α institucional es estructural: no son acciones individuales sino
condiciones que se generan o no se generan
El α del Estado en un brote no es un comunicado de prensa ni una declaración
de emergencia: son las condiciones materiales de posibilidad que el Estado
generó o no generó. El sistema de vigilancia epidemiológica activo antes del
brote, la capacidad hospitalaria con reserva suficiente, el acceso a diagnóstico
para toda la población, la cobertura de subsidio de días perdidos para
trabajadores esenciales, la infraestructura de agua potable y saneamiento —
esas son las condiciones cuya ausencia produce Δ positivo del Estado y cuya
presencia constituye α institucional.
FA_epi = R*_Estado × D_total × (1 − α_Estado). Este monto es la
base para calcular la responsabilidad del Estado en demandas colectivas por
negligencia en la respuesta pandémica. También es la base para establecer el
presupuesto mínimo de inversión en salud pública que el sistema requiere:

Taxonomía General de Aplicaciones
α_Estado debe ser proporcional a R*_Estado para que Δ_Estado sea
próximo a cero.
α en el Nivel de α
dominio Conducta típico en
Nodo
epidemiológic que sube α respuestas
o deficientes
Superpropagad Grado de Aislamiento 0.00–0.35
or individual interrupción de inmediato cuando el
(con voluntad) las cadenas de ante síntomas. Fobos (no
transmisión: Notificación puede
aislamiento, exhaustiva de aislarse) o el
notificación de todos los Deimos (no
contactos, contactos sabe que
cooperación conocidos. debe
con el rastreo, Cooperación hacerlo) es
uso de equipo activa con el dominante.
de protección. rastreo de
contactos.
Uso
consistente
del equipo de
protección
disponible.
Sistema de Velocidad y Detección del 0.05–0.15 en
vigilancia cobertura de la brote antes de los brotes
epidemiológica detección del que alcanzara donde la
brote: tiempo transmisión detección
desde los comunitaria tardía fue el
primeros casos amplia. factor
hasta la Activación de dominante
activación de la la alerta en de la
alerta, tiempo útil escalada.
cobertura del para las
sistema de intervencione
vigilancia s de
centinela, contención.
capacidad de Capacidad de
secuenciación rastreo mayor
genómica. al 80% de los
contactos
identificados.

Taxonomía General de Aplicaciones
α en el Nivel de α
dominio Conducta típico en
Nodo
epidemiológic que sube α respuestas
o deficientes
Sistema de Capacidad de Mantenimient 0.10–0.30 en
atención médica absorción del o de reserva sistemas de
y hospitalario brote sin hospitalaria salud que
colapso: reserva activa. fueron
de camas de Provisión de sobrepasado
cuidados equipo de s por la
intensivos, protección demanda del
disponibilidad suficiente para brote.
de equipo de todos los
protección para trabajadores
trabajadores de de salud.
salud, acceso a Diagnóstico
diagnóstico accesible para
para toda la toda la
población con población con
síntomas. indicación
clínica.
Sistema de Calidad y Comunicació 0.10–0.20 en
comunicación veracidad de la n temprana y los sistemas
de riesgo comunicación honesta sobre que
del riesgo a la el riesgo y la minimizaro
población: incertidumbre n el riesgo
transparencia . en las
sobre la Instrucciones primeras
incertidumbre, claras y semanas del
claridad sobre consistentes brote.
los protocolos sobre qué
de acción, hacer.
coherencia Adaptación
entre los de los
mensajes de mensajes a
distintas distintos
autoridades. grupos de la
población.
Estado como Grado en que el Existencia de 0.05–0.25 en
diseñador de las Estado generó programas de los sistemas
condiciones las condiciones compensació que no
estructurales materiales de n por días de generaron
posibilidad que aislamiento las
habrían para condiciones
reducido la trabajadores para que los
transmisión: informales y grupos más

Taxonomía General de Aplicaciones
α en el Nivel de α
dominio Conducta típico en
Nodo
epidemiológic que sube α respuestas
o deficientes
cobertura de esenciales. vulnerables
subsidio de días Provisión de pudieran
perdidos para alojamiento aislarse.
trabajadores de aislamiento
esenciales, para quienes
acceso a no pueden
vivienda con aislarse en el
condiciones de hogar.
aislamiento, Inversión
infraestructura histórica en
de agua y infraestructur
saneamiento. a de salud
pública.
§5 Construcción del grafo epidemiológico
causal
El grafo de cuatro niveles: de lo individual a lo estructural
El grafo epidemiológico causal se construye en cuatro niveles
que van desde lo más micro (los contactos individuales) hasta
lo más macro (las condiciones estructurales del sistema de
salud pública). A diferencia de las redes de contacto
tradicionales en epidemiología — que solo incluyen personas
— el grafo causal incluye también los nodos estructurales que
determinan las condiciones bajo las cuales los contactos
producen transmisión. El error de construir el grafo solo con
personas produce un R* que sobreestima la responsabilidad
individual y subestima la responsabilidad estructural.

Taxonomía General de Aplicaciones
Fuent
Nivel Tipo e de
Función R*
del de S típico eviden
causal típico
grafo nodo cia
para w
Indivi Person Transmisi Variable Variable Rastre
dual a ón directa — bajo — alto o de
infecta del en casos en casos contact
da con patógeno. ordinario ordinario os,
caracter R* alto si s, alto en s secuen
ísticas la superpro (cualquie ciación
de alta transmisi pagadore r caso genómi
transmi ón de ese s habría ca,
sión: nodo fue transmiti carga
carga causalme do igual viral
viral nte en ese docum
excepci necesaria entorno), entada,
onal, para la bajo en análisis
posició escala del superpro de
n en la brote. S pagadore clúster
red de depende s por
contact de si esas genuinos caso
os característ índice.
(hub), icas eran
trabajo idiosincrá
con ticas (S
contact bajo:
o superpro
intensiv pagador)
o. o
genéricas
(S alto:
cualquier
caso
habría
transmitid
o igual).
Ambi Espaci Amplifica Moderad Moderad Estudi
ental o de o reduce o-alto o — el os de
transmi la cuando el espacio ventila
sión: transmisi espacio específic ción,
instalac ón es la o tiene análisis
ión individual condició caracterís de
cerrada independi n que ticas que clúster
mal entement convierte otros por
ventila e de las el caso en espacios ubicaci
da, característ no ón,

Taxonomía General de Aplicaciones
Fuent
Nivel Tipo e de
Función R*
del de S típico eviden
causal típico
grafo nodo cia
para w
sistema icas de las superpro tendrían compa
de agua personas. pagador si ración
o aire Un estuviera de
compar espacio n mejor tasas
tido, mal ventilado de
transpo ventilado s o ataque
rte de puede mantenid por
alta convertir os espacio
densida una ,
d. transmisi análisis
ón de
ordinaria aerosol
en un es.
evento
superspre
ader.
Instit Sistema Detecta, Moderad Moderad Cronol
ucion de contiene y o-alto en o — los ogía de
al vigilanc trata. Su los sistemas decisio
ia fallo brotes de salud nes
epidem aumenta donde la pública versus
iológica el R* detecció con cronol
, efectivo n tardía o distinto ogía del
hospita de los la nivel de brote,
les, nodos capacida inversión capacid
laborat individual d histórica ad de
orios es porque hospitala producen rastreo,
de reduce α ria respuesta tiempo
diagnós del sobrepas s muy de
tico, sistema. ada distintas respues
autorid Su éxito fueron ta
ades de lo factores desde
salud disminuye determin detecci
pública. . Es el antes de ón
nodo la escala hasta
donde el interve
fraude nción,
annona cobert
del ura de
Estado es diagnó
más stico.
directame

Taxonomía General de Aplicaciones
Fuent
Nivel Tipo e de
Función R*
del de S típico eviden
causal típico
grafo nodo cia
para w
nte
medible.
Norm Política Determin Alto Moderad Cronol
ativo s de a las cuando o-bajo ogía de
/ cuarent condicion las cuando decisio
polític ena, es bajo las decisione las nes
o mandat cuales s decisione versus
os de ocurre la políticas s eran model
equipo transmisi crearon idiosincr os
de ón a condicio áticas del contraf
protecc escala nes que gobierno ácticos
ión, poblacion amplifica específic de la
restricci al. El ron la o; escala
ones de nodo de transmisi moderad del
movilid mayor R* ón más o-alto brote
ad, en allá de lo cuando con
campañ muchos que el cualquier activaci
as de brotes es sistema gobierno ón
vacuna una de salud bajo las tempra
ción, política podía mismas na,
subsidi que tardó absorber restriccio compa
os de en nes ración
aislami activarse institucio entre
ento, o que no nales jurisdic
comuni se activó habría ciones
cación — no un tomado con
de caso las distinta
riesgo. individual mismas s
. decisione política
s s,
estudio
s de
impact
o de las
interve
ncione
s.

Taxonomía General de Aplicaciones
El índice de sustituibilidad S en epidemiología: hacia
dónde apunta la intervención
S alto del nodo → la intervención debe ser sobre la clase, no sobre
el nodo específico
S alto de una persona infectada: cualquier persona con la misma carga viral
en el mismo entorno habría transmitido igual. La intervención no debe
focalizarse en esa persona sino en el entorno que la hace transmisora — la
ventilación del espacio, la densidad de contactos, el acceso a equipo de
protección.
S alto de un nodo estructural (sistema de agua contaminado): cualquier
sistema de agua equivalente habría producido la misma transmisión. La
intervención no es solo sobre ese sistema específico sino sobre la clase de sistemas
similares.
S bajo del superpropagador: las características idiosincráticas de esa persona
en ese momento — carga viral excepcional, posición en la red de contactos,
trabajo con contacto intensivo en espacio cerrado — fueron causalmente
determinantes. La intervención puede focalizarse en ese perfil de persona. La
combinación de R* × (1−S) produce la guía de intervención más eficiente:
Impacto_intervención_i ∝ R*_i × (1 − S_i). Intervenir en el nodo de mayor
R* × (1−S) produce el mayor impacto en la reducción del brote por unidad
de recursos invertida.
§6 Preguntas que responde este capítulo
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
¿Cuál es el nodo Construcción del grafo Declaración B si hay
de mayor R* en el epidemiológico con los análisis EP2 de
brote — el que cuatro niveles y cálculo calidad con variación
más contribuyó del eigenvector espacial y temporal.
causalmente a su dominante de la matriz Declaración A si hay
escala? de pesos W. El nodo de secuenciación EP1
mayor R* es el que, si se que establece la
hubiera intervenido, cadena de
habría producido la transmisión con
mayor reducción del precisión molecular.
brote. John Snow lo
identificó sin el
formalismo
matemático mediante la

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
variación espacial de los
casos.
¿La política de Análisis cronológico Declaración B si hay
respuesta EP2/EP5: ¿las evidencia de las
institucional fue decisiones se tomaron decisiones y de sus
causalmente cuando el sistema tenía alternativas
adecuada o hay la información y la disponibles EP5.
fraude annona capacidad para actuar Declaración C si el
epidemiológico? de manera diferente? contrafáctico de la
¿Qué habría ocurrido si activación temprana
las medidas se hubieran requiere
implementado dos modelamiento
semanas antes? FA_epi epidemiológico con
= R*_Estado × alta incertidumbre.
D_total × (1 −
α_Estado).
¿El Análisis de Hijos del Declaración B con
superpropagador superpropagador desde evidencia contextual
actuó desde la evidencia EP3/EP5 de las
Fobos epidemiológica y condiciones
(condiciones de contextual: ¿tenía estructurales del
trabajo), Deimos cobertura de días superpropagador.
(falta de perdidos para aislarse? Declaración C si el
diagnóstico) o ¿Tenía acceso a Hijo debe inferirse
Anteros (negación diagnóstico? ¿Hay sin documentación
deliberada)? evidencia de directa del caso.
comportamiento
negacionista activo? El
Hijo dominante
determina la política de
intervención.
¿Qué intervención Cálculo de R*_i × Declaración B con
tiene mayor (1−S_i) para cada nodo análisis EP2 que
impacto por candidato a establezca los R* y S
unidad de intervención. El nodo de los nodos
recursos — de mayor R* × (1−S) candidatos. El
análisis produce el mayor análisis prospectivo
prospectivo? impacto por unidad de tiene mayor
recursos. Si S del incertidumbre que el
entorno físico es alto análisis
(cualquier instalación retrospectivo.
similar produciría el
mismo resultado), la

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
intervención sobre la
clase es más eficiente
que la intervención
sobre un espacio
específico.
¿Cuánto del Distribución de R* Declaración B con
D_total del brote entre los cuatro niveles análisis EP2
es causalmente del grafo: individual, completo. La
atribuible a los ambiental, institucional, distribución de R*
nodos normativo/político. entre niveles es el
institucionales AD_institucional = análisis más
versus a los R*_institucional × disputado del
factores D_total_AVAD. El dominio porque
estructurales de D_total en unidades requiere establecer
fondo? comparables contrafácticos para
internacionalmente usa múltiples nodos
AVAD × w_ref. simultáneamente.
¿Hay desigualdad Análisis del diferencial Declaración B con
epidemiológica — de daño entre grupos análisis EP4 de la
el brote afectó sociales controlando distribución del daño
más a los grupos por las características por grupo social
más vulnerables del patógeno: ¿los controlando por la
por razones de grupos con mayor severidad de la
diseño del mortalidad o condición. El R* de
sistema? morbilidad lo son por los nodos
características estructurales
biológicas o por (condiciones
condiciones de laborales, acceso al
exposición, acceso al sistema de salud) en
tratamiento y capacidad el diferencial de daño
de aislamiento entre grupos
determinadas establece la
estructuralmente? responsabilidad del
diseñador de esas
condiciones.
§7 Traducción de D_total al dominio
epidemiológico

Taxonomía General de Aplicaciones
D_vital_epi = AVAD × w_ref · Los Años de Vida Ajustados por
Discapacidad como unidad estándar
El daño epidemiológico se cuantifica en la unidad estándar de la OMS para
la carga de enfermedad: AVAD = AVPP (Años de Vida Perdidos por
Muerte Prematura) + AVD (Años Vividos con Discapacidad). Convertido
al sistema: D_vital_epi = AVAD × w_ref, donde w_ref es el salario de
referencia global universal (no el salario del país afectado), para mantener el
principio ontológico de igualdad del tiempo de vida. La hora de vida de un
trabajador esencial de un país de ingreso bajo que murió por COVID-19
porque el sistema no le dio condiciones para aislarse tiene el mismo valor
ontológico que la de un ciudadano de un país de ingreso alto.
La conversión D_vital = AVAD × w_ref × 8,760 horas/año transforma
los AVAD en la misma unidad de horas de vida que se usa en todos los
dominios del libro — lo que permite comparar el fraude annona
epidemiológico con el fraude annona financiero, el daño de un brote con el daño
de una catástrofe ambiental, y el costo de la inversión preventiva con el
D_total que esa inversión habría prevenido.
En el Fuente
Compon dominio Estimación en de
ente epidemioló unidades comparables evidenci
gico a
T_invertid Las muertes D_vital_T_invertido = Datos de
o (muertes atribuibles al AVPP × 8,760 h/año × mortalida
y brote w_ref. Los AVPP se d en
morbilida (AVPP) y calculan como exceso de
d aguda las (esperanza_de_vida − las
directa) hospitalizaci edad_de_muerte) para autoridad
ones, cada fallecimiento es
discapacida atribuido al brote. Para el estadística
des y COVID-19 con 17 s
morbilidad millones de muertes en nacionale
producidas exceso: ~2.23 × 10¹² s. Análisis
en el horas de vida. de AVPP
período de la
agudo del OMS y de
brote. Es el institutos
component de
e que las estadística
estadísticas s
de nacionale
mortalidad s.
registran Estudios
más de
mortalida

Taxonomía General de Aplicaciones
En el Fuente
Compon dominio Estimación en de
ente epidemioló unidades comparables evidenci
gico a
directament d por
e. todas las
causas
durante el
brote
versus
períodos
comparab
les.
T_impedi Durante un D_vital_T_impedido = Datos de
do brote severo AVD_cond_pospuestas actividad
(colapso el sistema de × 8,760 h/año × w_ref. hospitalar
del salud no Los AVD se calculan ia durante
sistema de puede usando los pesos de el brote
salud y atender discapacidad de la OMS versus
atención otras para las condiciones que períodos
pospuesta condiciones: no recibieron atención comparab
) cirugías oportuna. les.
pospuestas, Estudios
enfermedad del
es crónicas impacto
sin atención, del brote
detección de sobre las
cáncer listas de
retrasada, espera.
atención de Análisis
urgencias de la
comprometi mortalida
da. Este d por
component condicion
e es no
frecuenteme COVID
nte supera a durante el
T_invertido período
en los brotes del brote.
más graves.
ΔT_trayec Las secuelas D_vital_trayectoria = Estudios
toria crónicas de AVD_secuelas_crónicas de largo
(secuelas los × 8,760 h/año × w_ref + plazo
de largo supervivient pérdida_de_potencial_ge sobre
plazo y es (COVID neracional. Este COVID
pérdida largo, componente tiene la largo y

Taxonomía General de Aplicaciones
En el Fuente
Compon dominio Estimación en de
ente epidemioló unidades comparables evidenci
gico a
generacio síndrome mayor incertidumbre del otros
nal) post-viral, D_total y debe declararse síndrome
daño como rango con análisis s post-
orgánico de sensibilidad. virales.
persistente), Análisis
el impacto del
en el impacto
desarrollo de las
infantil por interrupci
interrupcion ones
es educativa
educativas, s sobre el
la pérdida de potencial
potencial de de
las cohortes ingresos
más de las
afectadas. cohortes
afectadas.
Estudios
de
impacto
en el
desarrollo
cognitivo
por
interrupci
ones en el
período
crítico.
Distribución del AD entre los nodos del grafo y el fraude
annona epidemiológico
AD_i = R*_i × D_total_epi · FA_epi = R*_Estado × D_total × (1
− α_Estado)
En el COVID-19 con D_total ≈ $38.9 billones USD (2024): AD_N1
(sistemas de alerta OMS/China, R* ~28%) ≈ $10.9B. AD_N2
(conectividad aérea, R* ~22%) ≈ $8.6B. AD_N3 (desigualdad sanitaria,
R* ~18%) ≈ $7.0B. AD_N5 (comunicación minimizante, R* ~12%)
≈ $4.7B. El FA_epi se aplica a los nodos institucionales/normativos bajo

Taxonomía General de Aplicaciones
control del Estado: con R*_Estado ≈ 58% (N1+N3+N5+N6) y
α_Estado ≈ 0.10, FA_epi ≈ $20.3 billones USD.
Para el cólera de Broad Street de 1854 con D_monetary_equiv ≈ $705M
USD (2024): AD_N1 (bomba, R* ~48%) ≈ $339M. AD_N4
(autoridades sanitarias, R* ~8%) ≈ $56M. J_sistema = 1 − Σ|Δ_i| ≈
0.06: injusticia estructural casi máxima. Los nodos de mayor R* (la bomba,
el pozo negro, la infraestructura) tenían α ≈ 0 antes del brote. El fraude
annona del sistema de salud pública de Londres en 1854 era masivo y
medible: el sistema había recibido el capital de los ciudadanos y no había
generado las condiciones materiales básicas (alcantarillado separado, agua
potable) que habrían evitado el brote.
§8 Límites del método y errores frecuentes de
aplicación
Límites del método en el dominio epidemiológico
Límite 1 — La incertidumbre sobre los pesos en tiempo real.
En un brote activo, los pesos del grafo son inciertos porque la
evidencia está siendo generada simultáneamente con la toma
de decisiones. Los R* estimados en las primeras semanas de
un brote tienen intervalos de confianza amplios. El análisis en
tiempo real debe incluir rangos de pesos y análisis de
sensibilidad, no valores puntuales.
Límite 2 — La causalidad en múltiples escalas simultáneas.
Una pandemia opera en múltiples escalas causales: molecular,
individual, comunitaria, nacional, global. El grafo completo
tendría miles de nodos. En la práctica, el análisis debe
seleccionar los nodos más relevantes para la pregunta
específica. La selección de los nodos incluidos en el análisis es
una decisión metodológica que debe declararse
explícitamente.
Límite 3 — El problema del contrafáctico en pandemia. Las
intervenciones cambian el comportamiento de los otros
nodos: si los sistemas de alerta hubieran actuado dos semanas
antes, los sistemas de conectividad aérea y las políticas de
comunicación también habrían actuado diferente. El grafo

Taxonomía General de Aplicaciones
completo con dinámicas de respuesta requiere modelos
epidemiológicos más sofisticados que el cálculo estático de R*.
Límite 4 — Los Hijos y la privacidad de los
superpropagadores. El análisis de Hijos de superpropagadores
identificados plantea problemas de privacidad y
estigmatización. El objetivo del análisis de Hijos no es
culpabilizar a los superpropagadores sino orientar la política
de intervención hacia las causas estructurales. Si el análisis se
usa para identificar y sancionar a individuos en lugar de
reformar el sistema, pierde su valor y produce efectos
contraproducentes.
Límite 5 — R* identifica retrospectivamente, no predice
prospectivamente el próximo superpropagador. R* identifica
qué nodos tuvieron mayor peso causal en el brote analizado.
No predice cuál nodo será el superpropagador en el próximo
brote, porque esa posición depende de condiciones que varían
en cada caso. Lo que permite en sentido prospectivo es
identificar los tipos de nodos que tienden a tener mayor R*
bajo condiciones similares y diseñar intervenciones
estructurales para reducir ese peso antes del próximo brote.
Errores frecuentes de aplicación
Por qué Consecuen
Error Corrección
ocurre cia
Construir el El rastreo R* El grafo causal
grafo de sobreestima completo incluye
epidemiológ contactos es do de los cuatro niveles:
ico solo con la práctica casos individual, ambiental,
personas e estándar en individuales institucional y
ignorar los epidemiolog . R* del normativo/político.
nodos ía y produce sistema de La omisión de
estructurale naturalment salud cualquier nivel
s e e un grafo pública y de produce una
institucional de personas. las distribución de R*
es condiciones incompleta y una guía
estructurale

Taxonomía General de Aplicaciones
Por qué Consecuen
Error Corrección
ocurre cia
s = 0. Las de intervención
políticas subóptima.
resultantes
se focalizan
en el
comportam
iento
individual
cuando el
mayor
potencial de
impacto
está en los
nodos
estructurale
s.
Usar el Hijo El análisis Sanción a El Hijo dominante
dominante identifica a quien tenía determina la política
del un las menores de intervención, no el
superpropa superpropa opciones nivel de sanción.
gador para gador con reales para Fobos → eliminar las
sancionarlo Fobos actuar barreras al
en lugar de dominante y diferente. aislamiento. Deimos
para diseñar el sistema Incremento → proveer el marco
la responde del Fobos que faltó. Solo
intervenció con sanción. de otros Anteros justifica la
n correcta potenciales sanción individual, y
casos que aun así la reforma del
no contexto identitario es
reportarán más eficaz que la
ni sanción directa.
cooperarán.
Reducción
del α
general del
sistema.
Atribuir La narrativa R* del nodo El análisis causal
toda la política más visible siempre distribuye R*
responsabili tiende a sobreestima entre múltiples nodos.
dad del personalizar do. R* de El nodo de origen
brote a un la causa en los nodos típicamente tiene S
único nodo el nodo más sistémicos alto (cualquier evento
visible (el visible — el (sistemas de similar en esas
"paciente caso índice, alerta, condiciones habría

Taxonomía General de Aplicaciones
Por qué Consecuen
Error Corrección
ocurre cia
cero" o el el Estado desigualdad producido resultados
Estado de donde sanitaria, similares); los nodos
origen) comenzó el conectivida estructurales tienen S
brote. d aérea) = 0 moderado-bajo y son
en la los que más podrían
narrativa cambiar el resultado
dominante. de brotes futuros.
Las
reformas
resultantes
son
ineficaces
porque
atacan el
detonador
visible (S
alto) en
lugar del
sistema que
lo amplificó
(S bajo).
No El análisis Responsabil R*_superpropagador
distinguir establece el idad _efectivo =
entre el R* R* del individual R*_intrínseco × (1 −
del superpropa sobreestima α_sistema). Cuando
superpropa gador sin da. El Δ del α_sistema es bajo (el
gador y la preguntar Estado sistema no generó las
responsabili cuánto de como condiciones de
dad del ese R* es espejo del aislamiento), el
sistema que causalmente Fobos del R*_efectivo del
lo produjo atribuible a trabajador superpropagador es
las esencial amplificado por la
condiciones permanece inacción sistémica. El
que el invisible. Δ del Estado que no
sistema no generó las
generó para condiciones de
reducirlo. aislamiento es la
medida de su
responsabilidad en la
amplificación del
R*_efectivo de los
nodos individuales.

Taxonomía General de Aplicaciones
§9 Guía de prioridades de recolección de
evidencia
Si tu prioridad es saber qué buscar primero en un análisis
epidemiológico de responsabilidad, usa la tabla y el árbol que
siguen. La primera decisión siempre es establecer si el análisis
es retrospectivo (distribución de responsabilidad en un brote
ocurrido) o prospectivo (diseño de intervenciones para el
brote en curso o para la preparación del próximo). Cada
análisis tiene prioridades de evidencia distintas.
Tabla de prioridades de recolección de evidencia en
epidemiología y salud pública
La Qué
Por
Si tu evidencia Qué buscar /
qué
incertidumbre que más rango qué
funcio
principal es… la reduce reduce pregunta
na
es… r
1. ¿El análisis es Identificar El Determ ¿El
retrospectivo el objetivo objetiv ina el análisis se
(responsabilidad del análisis: o instrum usa para
por un brote ¿se busca determi ento atribución
ocurrido) o distribuir na los principa de
prospectivo responsabi instrum l y el responsab
(diseño de lidad entre entos nivel de ilidad legal
intervenciones)? actores por priorita certeza o
un brote ya rios y el necesari institucion
ocurrido, o nivel de o al
identificar certeza (retrospec
los nodos requeri tivo), para
de mayor do. El guiar la
impacto análisis respuesta
para retrosp actual
intervenci ectivo (prospecti
ones usa EP2 vo en
durante el con tiempo
brote más real), o
activo o datos para
para la disponi preparació
preparació bles; el n

Taxonomía General de Aplicaciones
La Qué
Por
Si tu evidencia Qué buscar /
qué
incertidumbre que más rango qué
funcio
principal es… la reduce reduce pregunta
na
es… r
n del análisis preventiva
próximo? prospec (prospecti
tivo vo a largo
requiere plazo)?
rangos
y
escenari
os de
estrés.
2. [TODOS] Construcci La Estable ¿Hay
¿Cuáles son los ón del omisión ce la datos de
cuatro niveles grafo con de complet infraestruc
del grafo — está los cuatro cualqui itud del tura de
el análisis niveles: er nivel grafo salud
incluyendo los individual, produc (incerti pública
nodos ambiental, e un R* dumbre disponible
estructurales? institucion incomp empíric s
al, leto. El a (cobertura
normativo error estructu de agua
/político. más ral) potable,
¿Hay frecuen acceso a
nodos de te es saneamien
infraestruc reducir to,
tura el grafo densidad
(sistemas al nivel hospitalari
de agua, individ a)? ¿Hay
ventilación ual. Los cronología
, densidad nodos de
habitacion de decisiones
al) mayor de los
incluidos? R* en la actores
¿Hay mayoría institucion
nodos de de los ales? ¿Hay
política brotes datos de
(cronologí de condicion
a de escala es
decisiones, significa laborales y
cobertura tiva son de
del sistema estructu cobertura
de salud) rales, social de
incluidos? no los grupos

Taxonomía General de Aplicaciones
La Qué
Por
Si tu evidencia Qué buscar /
qué
incertidumbre que más rango qué
funcio
principal es… la reduce reduce pregunta
na
es… r
individ más
uales. afectados?

### 3. Análisis El Estable ¿Los casos
[RETROSPEC EP2 de la método ce el se agrupan
TIVO] ¿Cuál fue variación de John nodo de espacialm
el nodo de espacial y Snow mayor ente
mayor R* en el temporal — R* alrededor
brote — análisis de los variació (incerti de un
de la fuente casos: ¿hay n dumbre nodo
primaria? un cluster espacial empíric específico
de casos de los a crítica) ? ¿Las
que apunta casos anomalías
a un nodo con el (grupos
ambiental nodo que no se
específico ambient infectaron
(bomba de al como , grupos
agua, epicentr que sí)
instalación o — es confirman
de el la
procesami instrum hipótesis
ento, ento del nodo
evento más primario?
social)? La directo ¿La
variación y secuenciac
espacial robusto ión
con para genómica
epicentro identific EP1
claro ar el establece
sugiere R* nodo de la cadena
alto del mayor de
nodo físico R* transmisió
identificad cuando n?
o. hay una
fuente
primari
a
identific
able.

### 4. Análisis Si el Estable ¿Cuándo
[RETROSPEC cronológic sistema ce el tuvo el
TIVO] ¿Hay o EP5: tenía FA_epi sistema de

Taxonomía General de Aplicaciones
La Qué
Por
Si tu evidencia Qué buscar /
qué
incertidumbre que más rango qué
funcio
principal es… la reduce reduce pregunta
na
es… r
fraude annona comparaci informa del vigilancia
epidemiológico ón entre el ción y sistema la
— el sistema momento capacid de salud informaci
tenía la en que el ad para pública ón
capacidad de sistema actuar (incerti suficiente
actuar diferente? tuvo la antes de dumbre para
informació lo que empíric activar la
n para actuó, a y alerta?
actuar y el hay Δ normati ¿Había
momento positivo va) recursos
en que del disponible
actuó. nodo s no
¿Había instituci utilizados?
precedente onal — ¿Otros
s de brotes fraude sistemas
similares annona con
con medible capacidad
respuestas . es
más similares
tempranas respondier
? ¿Los on más
recursos temprana
disponible mente?
s permitían ¿Los
una planes de
respuesta respuesta
más rápida existentes
o más se
completa? activaron
en
tiempo?

### 5. Análisis El Hijo Reduce ¿Tenía el
[SUPERPROP contextual domina la superprop
AGADORES] del nte incertid agador
¿El superprop determi umbre trabajo
superpropagado agador: na la sobre la informal o
r transmitió ¿tenía política política sin
desde Fobos, cobertura de de cobertura
Deimos, Potós o de días interve interven de días
Anteros? perdidos nción ción perdidos?
para correcta (incerti ¿Había
aislarse . La dumbre acceso

Taxonomía General de Aplicaciones
La Qué
Por
Si tu evidencia Qué buscar /
qué
incertidumbre que más rango qué
funcio
principal es… la reduce reduce pregunta
na
es… r
(ausencia confusi ontológ gratuito y
→ Fobos ón ica) rápido a
probable)? entre diagnóstic
¿Tenía Fobos y o en su
acceso a Anteros área? ¿Hay
diagnóstic produc registros
o cuando e la de
empezó a política comporta
tener más miento
síntomas injusta negacionis
(ausencia (sancio ta activo
→ Deimos nar a document
probable)? quien ado?
¿Hay no tenía
evidencia opcione
de s) y la
comporta menos
miento eficaz.
negacionis
ta activo
(Anteros)?

### 6. Cálculo de R* × Estable ¿Los
[PROSPECTIV R*_i × (1−S) ce las superprop
O] ¿Qué (1−S_i) es el priorida agadores
intervención para cada criterio des de identificad
tiene mayor nodo de interven os tienen
impacto por candidato prioriza ción característ
unidad de a ción de (incerti icas
recursos? intervenci interve dumbre comunes
ón con los nciones empíric que
datos — el a y de permiten
disponible mismo política) identificar
s. Si S del principi la clase
nodo es o del (trabajado
alto cap. 12 res
(cualquier (insolve esenciales
persona o ncia) en
instalación aplicad espacios
similar o al cerrados,
produciría diseño instalacion
el mismo de la es con
resultado), respues ventilació

Taxonomía General de Aplicaciones
La Qué
Por
Si tu evidencia Qué buscar /
qué
incertidumbre que más rango qué
funcio
principal es… la reduce reduce pregunta
na
es… r
la ta de n
intervenci salud deficiente,
ón sobre la pública. etc.)? ¿La
clase intervenci
supera a la ón sobre
intervenci esa clase
ón sobre el es factible
nodo con los
específico. recursos
disponible
s?
Árbol de decisión en epidemiología y salud pública: ¿qué
buscar primero?
El árbol bifurca entre el análisis retrospectivo de
responsabilidad y el análisis prospectivo de diseño de
intervenciones.
¿Cuál es el análisis principal?
├─ Análisis A: RETROSPECTIVO — distribución de
responsabilidad en un brote ocurrido
│
├─ PRIORIDAD 1: Construir el grafo con los cuatro
niveles — no omitir los nodos estructurales.
· Individual, ambiental, institucional y normativo/político.
├─ PRIORIDAD 2: ¿Cuál fue el nodo de mayor R*
— variación espacial EP2 o genómica EP1?
· El método de Snow: variación espacial con epicentro claro
= nodo ambiental dominante.

Taxonomía General de Aplicaciones
├─ PRIORIDAD 3: ¿Hay fraude annona — el
sistema tuvo la capacidad de actuar diferente?
· Cronología de decisiones EP5 versus cronología del brote.
· FA_epi = R*_Estado × D_total × (1 − α_Estado).
└─ PRIORIDAD 4 (si hay superpropagadores
identificados): Hijo dominante → política de
respuesta.
· Fobos → reforma estructural. Deimos → acceso y
comunicación. Anteros → norma de pares.
└─ Análisis B: PROSPECTIVO — diseño de intervenciones
durante el brote o para preparación
└─ PRIORIDAD ÚNICA: Calcular R*_i × (1−S_i)
para cada nodo candidato a intervención.
· El nodo de mayor R* × (1−S) es el de mayor
impacto por unidad de recursos.
· S alto → intervención sobre la clase. S bajo →
intervención focalizada en el nodo.
· Hijos de los superpropagadores: la intervención correcta
depende del Hijo, no del R*.
— Fin del Capítulo 21 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

