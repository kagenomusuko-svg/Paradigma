## PARTE II · CIENCIAS DE LA SALUD

### Capítulo 6
Epidemiología
Más allá del R₀: el peso causal de transmisión y el nodo que hace
posible el brote
§1. El problema
En el otoño de 1854, el barrio de Soho en Londres vivió
uno de los brotes de cólera más intensos de la historia de la
ciudad. En diez días murieron más de quinientas personas
en un área de pocos cientos de metros cuadrados. El origen
de los brotes de cólera era entonces un misterio: la teoría
dominante sostenía que la enfermedad se transmitía por el
aire contaminado —el "miasma"— y los médicos y
funcionarios de salud pública actuaban en consecuencia,
aireando habitaciones y quemando ropa.
John Snow, un anestesiólogo que había estudiado brotes
anteriores de cólera en Londres, tenía una hipótesis
diferente: la enfermedad se transmitía por el agua. Para
demostrarla, hizo algo que en términos de este sistema
describimos como construir el primer grafo causal empírico
de la historia de la epidemiología. Mapeó cada caso de
muerte en el barrio sobre un plano, identificó las fuentes de
agua de la zona, y observó un patrón inequívoco: la mayoría
de las muertes se concentraban alrededor de una bomba de

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
agua específica en Broad Street. Persuadió a las autoridades
de retirar la manivela de esa bomba. El brote cesó.
Lo que Snow hizo, sin llamarlo así, fue identificar el nodo
con mayor peso causal de transmisión en el grafo del brote:
la bomba de Broad Street. No identificó al paciente cero,
no calculó ninguna tasa de reproducción, no modeló la
dinámica poblacional. Identificó el nodo sin el cual el brote
no habría alcanzado esa escala. Eso es exactamente lo que
R* mide en el dominio epidemiológico.
Ciento setenta años después, en diciembre de 2019, un
brote de neumonía atípica en Wuhan, China, comenzó a
escalar. En los meses siguientes se convertiría en la
pandemia de COVID-19, que al finalizar 2023 había
causado más de veinte millones de muertes en exceso según
las estimaciones más conservadoras. El debate sobre la
responsabilidad causal del brote —los mercados de
animales vivos, los sistemas de alerta temprana que tardaron
en activarse, las decisiones de los primeros días que
permitieron la diseminación internacional— es uno de los
más políticamente cargados de la historia reciente de la
salud pública. Y es exactamente el tipo de debate que el
cálculo de la responsabilidad causal puede despolitizar: no
asignando culpas morales, sino distribuyendo pesos
causales sobre la base de evidencia documentada.
1.1 La diferencia entre R₀ y R*: correlación
versus causalidad
La epidemiología tiene ya una herramienta para medir la
capacidad de transmisión de un patógeno: el número básico
de reproducción R₀. Es uno de los indicadores más
importantes de la salud pública y ha sido central en la
respuesta a todas las pandemias modernas. R₀ mide, en
promedio, cuántas personas secundarias infecta una

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
persona primaria en una población completamente
susceptible.
Concepto epidemiológico: R₀ = número básico de
reproducción. Mide cuántas personas secundarias infecta en
promedio una persona primaria. R₀ > 1: el brote crece. R₀ < 1:
el brote se extingue. R₀ = 1: el brote es endémico estable. Es
un promedio poblacional, no una medida de la contribución
causal de nodos específicos.
R₀ es una medida correlacional: describe el comportamiento
promedio del patógeno en una población dada. No dice
nada sobre qué nodos específicos del sistema de
transmisión son causalmente necesarios para que el brote
ocurra a esa escala. No distingue entre una persona que
infectó a 50 personas en un evento superspreader y 49
personas que no infectaron a nadie. No identifica las
condiciones estructurales —sistemas de agua, ventilación
de espacios, densidad habitacional, acceso a atención
médica— que hacen posible que R₀ sea alto en ese contexto
específico.
R* causal en epidemiología hace algo diferente: distribuye
el peso causal de transmisión entre todos los nodos del
sistema epidemiológico —personas, espacios, condiciones
estructurales, políticas de salud pública— en proporción a
cuánto dependía el brote de cada nodo específico. Es la
pregunta: sin este nodo (esta persona, este mercado, este
sistema de agua, esta política de cuarentena), ¿habría
alcanzado el brote esta escala?
Dimensión R₀ (correlacional) R* causal (este
sistema)
Qué mide Promedio de Fracción del brote
infecciones causalmente
secundarias por atribuible a cada
caso primario en nodo específico del

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
población sistema de
susceptible. transmisión.
Nivel de análisis Poblacional. Un Nodal. Un vector de
solo número para pesos para cada
todo el brote. actor, espacio o
condición
estructural.
Información base Número de casos Grafo de influencias
secundarios por causales con pesos
caso primario. estimados por
Requiere evidencia
seguimiento de epidemiológica.
contactos.
¿Distingue Solo Directamente: el
superpropagadores? indirectamente, superpropagador es
como anomalías el nodo con R* bajo
estadísticas que S (su S es bajo: su
elevan la varianza contribución fue
del número de idiosincrática).
reproducción.
¿Identifica nodos No. R₀ es Sí. El sistema de
estructurales? propiedades del agua, la ventilación
patógeno-huésped, del espacio, la
no del sistema de política de
condiciones. cuarentena pueden
ser nodos con R*
alto.
Uso principal Modelar la Identificar los nodos
dinámica del brote, de intervención con
calcular umbrales mayor impacto,
de vacunación, distribuir
estimar velocidad responsabilidad entre
de expansión. actores del sistema
de salud pública.
Las dos herramientas no compiten: son complementarias.
R₀ dice qué tan rápido crece el brote. R* dice dónde
intervenir para frenarlo con mayor eficacia. La
epidemiología moderna usa R₀; el cálculo de la

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
responsabilidad añade R* como instrumento adicional que
responde preguntas que R₀ no puede responder.
1.2 Los superpropagadores como nodos con
S bajo
El fenómeno del superpropagador es uno de los más
documentados y menos formalizados de la epidemiología
moderna. En muchos brotes, la distribución del número de
infecciones secundarias no sigue una curva normal: es
altamente asimétrica. El 80% de las infecciones es causado
por el 20% de los casos —o incluso por el 10% o el 5%,
dependiendo del patógeno y el contexto. Esto es lo que la
literatura llama el principio 80/20 o la regla de Lloyd-Smith.
En términos del sistema de imputación causal, los
superpropagadores son nodos con R* alto y S bajo. R* alto:
sin ellos específicamente, el brote no habría alcanzado esa
escala en ese momento. S bajo: su contribución no era la de
cualquier persona infectada —dependía de sus
características idiosincráticas: el lugar donde estaban, las
personas con las que interactuaban, la carga viral específica
que tenían, sus condiciones de trabajo que los ponían en
contacto con muchas personas.
Esta distinción entre R* alto y S bajo es operativamente
importante para la salud pública: los superpropagadores no
son "personas culpables" de transmitir más. Son personas
cuya posición en el grafo de contactos, cuyas condiciones
de trabajo o vivienda, y cuya situación inmunológica en ese
momento específico los colocaron en una posición de alta
necesidad causal para el brote. La intervención no es
castigarlos: es identificarlos para interrumpir las cadenas
que dependen de su posición.
Superpropagador (definición ontológica): Nodo del
grafo epidemiológico con R* significativamente mayor al
promedio y S bajo. R* alto indica que el brote dependía

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
causalmente de ese nodo en mayor medida que del
promedio de casos. S bajo indica que esa dependencia no
era genérica (cualquier infectado en esa posición) sino
específica de las características de ese nodo en ese
momento: su carga viral, su red de contactos, sus
condiciones ambientales.
1.3 El fraude annona del Estado en salud
pública
En el sistema ontológico de la colección, el contrato fiscal
establece que el Estado recibe las libertades del soberano
(impuestos, obediencia, legitimidad) y debe generar las
condiciones materiales de posibilidad para que el ciudadano
pueda desplegar su eutaxia utópica. Las condiciones de
salud pública —agua potable, sistemas de vigilancia
epidemiológica, infraestructura hospitalaria, acceso a
medicamentos— son condiciones materiales de posibilidad
de primer orden.
Cuando el Estado tiene R* alto en el grafo de un brote
epidemiológico —cuando las condiciones que no generó
fueron causalmente necesarias para que el brote alcanzara
la escala que alcanzó— y su α es bajo (no reconoció su
posición causal, no reformó sus sistemas, no compensó a
las víctimas), hay fraude annona epidemiológico. El Estado
recibió el capital de los ciudadanos y no generó las
condiciones que habría podido generar y que habrían
reducido la transmisión.
Este concepto es analíticamente poderoso porque permite
distinguir entre brotes que eran inevitables dado el estado
del conocimiento y de las tecnologías disponibles (R* del
Estado bajo porque no había intervención posible) y brotes
que habrían podido ser mucho menores si el Estado hubiera
generado las condiciones que estaban a su alcance (R* del
Estado alto y Δ positivo porque las condiciones existían,
pero no se generaron o se generaron tardíamente).

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología

§2. Página puente —
Traducción al lenguaje
epidemiológico
Esta página resume cómo se renombran las herramientas
del sistema en el contexto de la epidemiología y la salud
pública. El lector con formación epidemiológica puede
comenzar aquí sin haber leído los capítulos anteriores.
Herramienta En epidemiología Qué significa en la
se llama práctica de la salud
pública
Grafo causal Red de transmisión El mapa de todos los
G causal nodos (personas,
espacios, condiciones
estructurales, políticas)
que contribuyen
causalmente a que el
brote alcance su escala.
Es más amplio que la red
de contactos tradicional.
Nodo Actor Puede ser una persona
epidemiológico infectada, un espacio de
transmisión (mercado,
hospital, transporte
público), una condición
estructural (sistema de
agua, ventilación), o una
política de salud pública
(cuarentena, vigilancia,
acceso a atención).
R* (vector) Peso causal de La fracción del brote
transmisión causalmente atribuible a
cada nodo. Distinto de
R₀: R₀ mide el promedio
de infecciones

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
secundarias; R*
distribuye el peso causal
total entre los nodos del
grafo. R* del
superpropagador > R*
promedio de casos
ordinarios.
R₀ (externo) Número básico de Herramienta
reproducción epidemiológica
establecida. Mide el
promedio de infecciones
secundarias.
Correlacional. R* y R₀
son complementarios: R₀
describe la dinámica
global; R* identifica los
nodos causalmente
críticos.
S (índice) Fungibilidad del S alto: cualquier persona
nodo en la cadena en esa posición (misma
carga viral, mismo
ambiente) habría
transmitido igual. El
nodo es reemplazable en
la cadena. S bajo: la
contribución de este
nodo dependía de
características
idiosincráticas. Los
superpropagadores
tienen S bajo.
α Grado de Lo que el nodo hizo para
(coeficiente) contención: interrumpir las cadenas
aislamiento, que dependían de él: se
notificación, aisló, notificó sus
tratamiento contactos, buscó
atención, cooperó con el
rastreo. α = 1:
contención completa. α
= 0: no hizo nada para
interrumpir las cadenas.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
Δ = R* − α Déficit de La brecha entre el peso
contención: causal del nodo y su
transmisión no contención efectiva. Para
interrumpida nodos institucionales
(Estado, sistemas de
salud): Δ mide el
incumplimiento de las
obligaciones de salud
pública proporcional a la
capacidad causal.
D_total Daño en salud T_invertido (muertes y
pública morbilidad directa),
T_impedido (colapso del
sistema de salud durante
el brote, atención
pospuesta),
ΔT_trayectoria (daños de
largo plazo: secuelas
crónicas, pérdidas de
potencial de las
generaciones afectadas).
D_vital Daño en tiempo de Años de vida perdidos
vida biológica y (AVPP) + años vividos
social con discapacidad (AVD)
= AVAD (Años de Vida
Ajustados por
Discapacidad). Estándar
OMS. En el sistema:
D_vital = AVAD ×
w_ref (expresado en
unidades monetarias con
el salario de referencia
universal).
Fraude Incumplimiento del El Estado tiene R* alto
annona Estado en en el brote (las
condiciones de condiciones que no
salud pública generó eran causalmente
necesarias para la escala
del daño) y α bajo (no las
generó estando a su
alcance hacerlo). Δ del

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
Estado > 0: fraude
annona epidemiológico.
Hijos de Solo aplican a Los hijos no aplican a
Afrodita superpropagadores nodos estructurales (el
con voluntad sistema de agua, la
política de cuarentena).
Solo aplican a personas
identificadas como
superpropagadores con
voluntad propia:
¿actuaron desde Fobos
(miedo a reportar), desde
Anteros (resistencia a las
medidas), desde
Harmonía (cooperación
plena)?
Para el lector que viene del núcleo universal: Este dominio
tiene tres características singulares. Primera: los nodos incluyen tanto
personas como estructuras físicas y políticas —la bomba de agua, el
sistema de vigilancia epidemiológica, la política de cuarentena son todos
nodos con R* real. Segunda: los hijos solo aplican a superpropagadores
con voluntad propia, no a nodos estructurales. Tercera: la temporalidad
puede ser tanto retrospectiva (para distribuir responsabilidad) como
prospectiva (para diseñar intervenciones).

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
§3. Las herramientas en el
contexto epidemiológico
3.1 Cómo construir el grafo epidemiológico
causal
El grafo epidemiológico causal se construye en cuatro
niveles que van desde lo más micro (los contactos
individuales) hasta lo más macro (las condiciones
estructurales del sistema de salud pública). A diferencia de
las redes de contacto tradicionales en epidemiología —que
solo incluyen personas— el grafo causal incluye también los
nodos estructurales que determinan las condiciones bajo las
cuales los contactos producen transmisión.
Nivel Tipo de Función Fuente de
nodo causal evidencia
para w
Individual Persona Transmite el Rastreo de
infectada / patógeno contactos,
superpropaga directamente. secuenciaci
dor. R* alto si la ón
transmisión de genómica
ese nodo fue del
causalmente patógeno
necesaria para (para
la escala del vincular
brote. cepas),
carga viral
documenta
da.
Ambiental Espacio de Amplifica o Estudios de
transmisión: reduce la ventilación,
mercado, transmisión análisis de
hospital, individual. Un clúster de
transporte, espacio mal casos por

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
vivienda. ventilado ubicación,
Sistema de convierte una comparació
agua o aire. transmisión n de tasas
ordinaria en un de ataque
evento por
superspreader espacio.
independientem
ente de la
persona.
Institucional Sistema de Detecta, Capacidad
vigilancia contiene y trata. de rastreo,
epidemiológic Su fallo tiempo de
a, hospitales, aumenta el R* respuesta
laboratorios efectivo de los desde
de nodos detección
diagnóstico, individuales hasta
autoridades porque reduce intervenció
de salud α. Su éxito lo n,
pública. disminuye. cobertura
de
diagnóstico.
Normativo/pol Políticas de Determina las Cronología
ítico cuarentena, condiciones de
cierre de bajo las cuales decisiones
fronteras, ocurre la vs.
mandatos de transmisión a cronología
uso de escala del brote,
equipo de poblacional. El estudios de
protección, nodo de mayor impacto de
campañas de R* intervencio
vacunación. frecuentemente nes,
es una política modelos
que tardó en contrafáctic
activarse o que os.
no se activó.
⚠ El error más frecuente al construir el grafo epidemiológico
es reducirlo al nivel individual (solo personas) y omitir los
nodos estructurales y normativos. Un grafo incompleto
produce un R* que sobreestima la responsabilidad causal de los
casos individuales y subestima o no detecta la responsabilidad

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
del sistema de salud pública. Los brotes de mayor escala en la
historia moderna tuvieron siempre nodos estructurales con R*
alto que no fueron los casos individuales.
3.2 R* causal versus R₀: el análisis de nodos
críticos
El procedimiento para calcular R* en el dominio
epidemiológico sigue la misma iteración de potencia de los
dominios anteriores, pero con una particularidad: la matriz
W incluye aristas de tipos muy distintos (persona-a-persona,
espacio-a-persona, política-a-espacio) que deben ser
ponderadas con evidencia epidemiológica.
La diferencia operativa más importante entre R₀ y R* se
manifiesta en el análisis de superpropagadores:
R₀ = E [número secundario de infecciones] (media
poblacional)
R* = eigenvector(W) (distribución causal entre
nodos)
En un brote donde el 80% de la transmisión fue producida
por el 20% de los casos (patrón 80/20 documentado en
SARS-CoV-1, COVID-19, sarampión y otros), R₀ puede ser
moderado (digamos 2.5) mientras que el R* de los
superpropagadores es muy alto y el R* del 80% de los casos
ordinarios es mínimo. Eso tiene consecuencias para la
intervención: una estrategia de control enfocada en los
nodos de mayor R* es más eficiente que una estrategia
uniforme.
3.3 El índice de sustituibilidad S en
epidemiología

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
En el dominio epidemiológico, S tiene una interpretación
directamente operativa para la política de salud pública:
• S alto de una persona infectada: cualquier otra persona
con la misma carga viral en el mismo entorno habría
transmitido igual. El nodo es genérico. La intervención
no debe focalizarse en esa persona sino en el entorno
que la hace transmisora (la ventilación del espacio, la
densidad de contactos, el acceso a equipo de
protección).
• S bajo de un superpropagador: las características
idiosincráticas de esa persona en ese momento (carga
viral excepcional, posición en la red de contactos,
trabajo que implica contacto intensivo) fueron
causalmente determinantes. La intervención puede
focalizarse en esa persona específica.
• S alto de un nodo estructural (sistema de agua
contaminado): cualquier sistema de agua equivalente
habría producido la misma transmisión. La
intervención no es sobre ese sistema específico sino
sobre la clase de sistemas similares.
• S bajo de un nodo normativo (política de cuarentena
tardía): la decisión específica de no activar la cuarentena
en ese momento específico fue causalmente
determinante. Otro gobierno con acceso a la misma
información y la misma capacidad podría haber actuado
diferente.
La combinación de R* y S produce la guía de intervención
más eficiente:
Impacto_intervención_i ∝ R*ᵢ × (1 − Sᵢ)
Intervenir en el nodo de mayor R* × (1 − S) produce el
mayor impacto en la reducción del brote por unidad de
recursos invertida.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
3.4 α y Δ en epidemiología: la brecha de
contención
En el dominio epidemiológico, α tiene dos niveles de
aplicación:
α individual (nodos-persona con voluntad):
Nivel de α Rango Conducta observable
individual
Sin 0.00– La persona no se aisló, no notificó
contención 0.05 contactos, continuó sus actividades
habituales a pesar de saber o sospechar
que estaba infectada.
Contención 0.06– Se aisló tarde, notificó solo algunos
parcial 0.35 contactos, buscó atención con demora.
Contención 0.36– Se aisló, notificó sus contactos
sustancial 0.70 conocidos, buscó atención. Cooperó
con el rastreo.
Contención 0.71– Aislamiento inmediato, notificación
completa 1.00 exhaustiva de contactos, cooperación
activa con la investigación
epidemiológica.
α institucional/estatal (nodos de diseño de la
respuesta):
Nivel de α Rango Conducta observable del sistema
institucional de salud pública
Sin respuesta 0.00– El sistema no detectó el brote en
0.05 tiempo útil, no activó protocolos de
contención, no informó a la
población.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
Respuesta 0.06– Detección tardía. Los protocolos se
tardía 0.30 activaron cuando el brote ya había
alcanzado escala difícil de contener.
Respuesta 0.31– Detección razonablemente oportuna
parcial 0.60 pero con brechas en la ejecución:
cobertura de rastreo insuficiente,
capacidad hospitalaria sobrepasada.
Respuesta 0.61– Detección temprana, activación de
integral 0.85 protocolos de contención, rastreo
extenso, comunicación clara,
capacidad hospitalaria protegida.
Respuesta 0.86– Todo lo anterior más transparencia
ejemplar 1.00 completa en la comunicación de la
incertidumbre, adaptación ágil de los
protocolos según la evidencia
emergente.
El déficit de contención Δ = R* − α mide la brecha entre el
peso causal del nodo y su respuesta. Para los nodos
individuales, Δ positivo indica transmisión que podría
haberse interrumpido. Para los nodos institucionales, Δ
positivo es el indicador del fraude annona epidemiológico.
3.5 El daño epidémico y su expresión en
tiempo de vida
D_epi = T_invertido + T_impedido + ΔT_trayectoria
Componente En Descripción
epidemiología
equivale a
T_invertido Muertes directas Las muertes atribuibles al
y morbilidad brote, las hospitalizaciones,
aguda las discapacidades
producidas en el período
agudo. Es el daño medido

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
directamente durante el
brote.
T_impedido Colapso del Durante un brote severo, el
sistema de salud sistema de salud no puede
y atención atender otras condiciones:
pospuesta cirugías pospuestas,
enfermedades crónicas sin
atención, detección de
cáncer retrasada. Este
componente
frecuentemente supera a
T_invertido en los brotes
más graves.
ΔT_trayectoria Secuelas de largo Las secuelas crónicas de los
plazo y pérdida sobrevivientes (COVID
generacional largo, síndrome post-viral),
el impacto en el desarrollo
infantil por interrupciones
educativas, la pérdida de
potencial de las cohortes
más afectadas.
Dimensión vital: La expresión en tiempo de vida del daño
epidemiológico usa el estándar de los Años de Vida Ajustados
por Discapacidad (AVAD) de la OMS: AVAD = AVPP (Años
de Vida Perdidos por Muerte Prematura) + AVD (Años
Vividos con Discapacidad). Convertido al sistema: D_vital_epi
= AVAD × w_ref. Esta conversión usa el w_ref universal (no
el salario del país afectado) para mantener el principio
ontológico de igualdad del tiempo de vida.
3.6 Los hijos de Afrodita en epidemiología:
solo en superpropagadores
En el dominio epidemiológico, los hijos de Afrodita tienen
un alcance más restringido que en los dominios jurídicos o
clínicos: solo aplican a los nodos superpropagadores
identificados con voluntad propia. No se calculan para los
nodos estructurales (el sistema de agua, la ventilación del

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
espacio, la política de cuarentena), porque esos nodos no
tienen disposición de voluntad.
La distinción más importante que los hijos aportan al
análisis epidemiológico es entre el superpropagador que
actuó desde Fobos (miedo a reportar, miedo a perder el
empleo si se aísla, miedo al estigma) y el que actuó desde
Anteros (negación deliberada de las medidas de protección)
o Deimos (parálisis ante la incertidumbre sobre si estaba
realmente infectado). Esta distinción cambia radicalmente
la política de intervención:
Hijo Qué describe Intervención α predicho
dominan en el de salud
te superpropagad pública
or
Fobos Transmitió Eliminar las Moderado-alto
porque tenía barreras al si se eliminan
miedo de aislamiento: las barreras. α
reportar o compensación sube cuando el
aislarse: perder por días Fobos
el empleo, el perdidos, disminuye.
estigma, las protección del
consecuencias. empleo,
No quiso comunicación
transmitir: no desestigmatizan
pudo dejar de te. El Fobos no
hacerlo dadas se resuelve con
las condiciones. multas: se
resuelve con
seguridad.
Anteros Resistencia Comunicación Bajo sin
deliberada a las que no cambio de
medidas de confronte contexto.
protección. directamente el Requiere
Rechazo activo Anteros (lo transformació
del aislamiento refuerza). En su n del sesgo
o del uso de lugar: norma identitario, no
social de pares,

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
equipo de incentivos presión
protección. positivos, directa.
framing de las
medidas como
afirmación de
autonomía.
Deimos Parálisis ante la Acceso fácil y Alto si se
incertidumbre: rápido a provee el
no sabía si diagnóstico. marco que
estaba Comunicación faltó. El
infectado, no clara sobre Deimos se
entendía los síntomas y qué transforma en
síntomas, no hacer. El Harmonía con
tenía acceso a Deimos se estructura.
diagnóstico. resuelve con
información y
acceso, no con
sanciones.
Harmoní Cooperación Reconocer y Alto (0.70–
a activa con las reforzar. La 1.00). Este
medidas. Se respuesta de superpropagad
aisló, notificó, salud pública or maximizó
cooperó con el que trata su α dado el
rastreo. igualmente a conocimiento
quien cooperó disponible.
y a quien no
desincentiva la
cooperación
futura.
El principio de equidad epidemiológica basado en los
hijos: Una política de salud pública justa distingue entre el
superpropagador que transmitió desde Fobos (las condiciones le impidieron
actuar de otro modo) y el que lo hizo desde Anteros (eligió actuar en contra
de las medidas). Ambos tienen el mismo R*, pero sus Δ son diferentes: el
primero tiene Δ positivo porque el sistema de salud pública no generó las
condiciones para que pudiera aislarse (fraude annona del Estado hacia el
trabajador que perdería el empleo si se aislaba). El segundo tiene Δ
positivo por elección propia. La política de intervención debe ser diferente
en cada caso.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología

§4. Casos resueltos
Caso A — El cólera de Broad Street, Londres (1854)
El primer grafo causal de la historia de la epidemiología
A.1 El contexto histórico
El brote de cólera de Soho en septiembre de 1854 es uno
de los eventos fundacionales de la epidemiología moderna.
No porque fuera el brote más grave de la historia —hubo
pandemias de cólera mucho más devastadoras— sino
porque fue el brote que John Snow usó para demostrar
empíricamente que el cólera no se transmitía por el aire sino
por el agua contaminada, y para desarrollar el método que
hoy llamaríamos análisis causal de red.
Snow llegó al barrio de Soho dos días después del inicio del
brote, el 3 de septiembre de 1854. Comenzó a mapear
sistemáticamente los casos de muerte sobre un plano del
barrio, señalando con un punto negro cada fallecimiento y
con un símbolo diferente cada fuente de agua. Lo que
emergió del mapa fue la primera visualización de un grafo
epidemiológico causal de la historia: los puntos negros se
agrupaban alrededor de la bomba de Broad Street con una
claridad que ninguna otra fuente de agua podía explicar.
La historia tiene un detalle que el análisis de R* captura
perfectamente: Snow observó que un grupo de trabajadores
de una cervecería cercana había tenido muy pocos casos de
cólera a pesar de trabajar a metros de la bomba. La
investigación reveló que los trabajadores bebían cerveza, no
agua. Y una monja del convento adyacente que murió de
cólera a pesar de vivir lejos del barrio había pedido que le
llevaran agua de la bomba de Broad Street porque la
encontraba especialmente fresca. Dos anomalías que

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
confirmaban la hipótesis causal con una precisión que
ningún modelo correlacional habría podido producir.
A.2 Reconstrucción del grafo causal
Nod Actor/Factor Tipo Función
o causal
N1 Bomba de Ambiental Fuente
agua de (infraestructura) centralizada
Broad Street de agua
contaminada.
Sin esta
bomba
específica, el
brote no
habría
alcanzado esa
concentración
espacial y
temporal. R*
alto, S
moderado-
bajo.
N2 Pozo negro Ambiental (sanitario) El foco de
de Broad contaminació
Street 40 n original.
Documentado
posteriorment
e: el bebé de
la familia Eley
desarrolló
cólera el 28 de
agosto, los
pañales se
lavaban y
vaciaban en el
pozo, y el
pozo estaba a
menos de un
metro de la
bomba con

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
grietas en la
mampostería.
N3 Infraestructu Estructural La ausencia de
ra sanitaria sistema de
del barrio de alcantarillado
Soho separado del
sistema de
agua potable
en ese sector.
Condición
estructural de
fondo que
hacía posible
la
contaminació
n del N1
desde N2.
N4 Autoridades Normativo/institucio Tenían la
de salud nal capacidad de
pública de instalar
Londres alcantarillado
separado (que
se haría
después del
brote como
respuesta) y
no lo habían
hecho.
Posición
causal
estructural,
con α bajo
antes del
brote.
N5 Casos Individual Los casos que
individuales generaron
de mayor más
transmisión transmisiones
secundaria secundarias en
sus hogares.
R* moderado,
S alto

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
(cualquier
caso con la
misma carga
viral habría
transmitido
similarmente).
Nf Población del Nodo final 616 muertes
barrio de en diez días
Soho en el área
inmediata. No
entra en el
cálculo de R*.
A.3 R*, S y Δ: lo que Snow vio sin los instrumentos
formales
El mapa de Snow era, sin saberlo, la primera visualización
de un grafo causal epidemiológico. Pero el vector R* hace
explícito lo que el mapa solo mostraba visualmente:
Nodo R* S α Interpretación
pre-
brote
N1 — Bomba ~48% 0.30 0.00 Nodo de transmisión
de Broad St. dominante. S
moderado-bajo: era
esta bomba
específica y no
cualquier fuente de
agua porque era la
única que accedía al
agua contaminada de
ese pozo.
N2 — Pozo ~22% 0.45 0.00 Foco de
negro Broad 40 contaminación
original. S moderado:
otro pozo en
situación similar

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
habría producido la
misma
contaminación.
N3 — ~18% 0.80 0.00 Factor estructural
Infraestructura con S alto. Cualquier
Soho barrio con la misma
falta de alcantarillado
habría tenido el
mismo riesgo.
N4 — ~8% 0.60 0.05 Posición causal real
Autoridades pero moderada. Su Δ
sanitarias = +0.08 es el
indicador del fraude
annona: tenían la
capacidad de generar
las condiciones y no
las generaron.
N5 — Casos ~4% 0.90 0.10 S muy alto. Cualquier
individuales caso en esa posición
habría transmitido
igual. El control
individual era
mínimamente eficaz.
La implicación central del análisis: el 86% del peso causal
del brote estaba en los nodos ambientales e
infraestructurales (N1, N2, N3) con nulo o mínimo α antes
del brote. El control individual (N5) tenía solo el 4% del
peso causal. Una política de salud pública enfocada en el
comportamiento individual habría sido casi ineficaz. Snow
lo entendió intuitivamente: la intervención correcta era
retirar la manivela, no aislar personas.
El índice de Justicia Estructural del sistema de salud pública
de Londres en 1854:
J = 1 − Σ|Δᵢ| = 1 − (0.48 + 0.22 + 0.18 + 0.03 + ...) ≈
0.06

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
J = 0.06 indica injusticia estructural casi máxima: los nodos
de mayor R* tenían α prácticamente nulo antes del brote.
El sistema de salud pública no había generado las
condiciones materiales de posibilidad para prevenir el daño.
Eso es el fraude annona epidemiológico cuantificado.
A.4 La lección metodológica: Snow como
epidemiólogo ontológico
Snow no calculó R₀. No modeló la dinámica SIR de la
epidemia. Lo que hizo fue construir un argumento causal:
identificó el nodo sin el cual el brote no habría ocurrido a
esa escala, estimó su peso causal mediante la variación
espacial de los casos, y verificó la hipótesis causal con las
anomalías (los trabajadores de la cervecería, la monja del
convento).
Esa estructura metodológica —construir el grafo,
identificar el nodo de mayor peso, verificar con
anomalías— es exactamente el protocolo del cálculo de la
responsabilidad causal. Snow lo hizo sin las herramientas
matemáticas formales porque su intuición epidemiológica
era suficiente para el caso simple de Broad Street: un solo
nodo dominante, evidencia espacial clara, anomalías
verificables.
Cuando el brote es más complejo —múltiples nodos de
transmisión, interacciones entre factores estructurales y
comportamentales, efectos de las políticas a múltiples
escalas— la intuición no es suficiente. Ahí es donde el
cálculo formal de R* aporta lo que la intuición no puede
garantizar: la consistencia y la reproducibilidad del análisis.
Snow y la paradoja de la evidencia: Snow presentó su análisis
al Comité de Salud Pública de Londres. El comité lo rechazó porque la
teoría del miasma seguía siendo dominante y la evidencia de Snow era
"solo un mapa". Sin embargo, aceptaron retirar la manivela de la bomba
como medida preventiva menor. El brote cedió. La interpretación causal
correcta no prevaleció por su lógica sino por su resultado. Esto ilustra un

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
límite importante del cálculo causal: el análisis puede ser correcto y no ser
adoptado si el sistema de toma de decisiones opera con criterios distintos a
la causalidad.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
Caso B — COVID-19 (2019–2023)
R* de los nodos de diseño versus la narrativa política: lo que el análisis causal
revela
B.1 El contexto y la complejidad del caso
La pandemia de COVID-19 es el caso epidemiológico más
complejo y políticamente cargado de la historia reciente. A
diferencia del cólera de 1854, donde el grafo era simple y el
nodo dominante era inequívoco, el COVID-19 tiene una
estructura causal de alta complejidad: múltiples actores en
múltiples escalas (local, nacional, internacional), decisiones
que se tomaron bajo incertidumbre genuina sobre las
características del patógeno, y una superposición de
factores estructurales preexistentes (desigualdad sanitaria,
fragmentación de los sistemas de salud) con decisiones
específicas que pudieron haberse tomado diferente.
Precisamente porque es complejo y políticamente cargado,
es donde el análisis causal aporta más valor: no para
establecer culpas morales (que el debate político ya produce
en abundancia) sino para distribuir pesos causales basados
en evidencia, distinguiendo entre lo que era inevitable dado
el conocimiento disponible y lo que habría podido ser
diferente con las capacidades existentes.
El análisis que sigue no pretende ser exhaustivo sobre la
causa del origen del virus —esa pregunta tiene
incertidumbre genuina que el sistema reconoce
honestamente. Se centra en los nodos del sistema de
respuesta cuya posición causal en la escala del daño está
mejor documentada.
B.2 El grafo causal de la escala de la pandemia
El grafo distingue entre los nodos relacionados con el
origen y los primeros días del brote (donde la incertidumbre

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
es mayor) y los nodos relacionados con la escala global que
el brote alcanzó (donde la evidencia es más robusta):
No Actor/Fact Tipo Función Certez
do or causal en la a
escala del
daño
N1 Sistemas de Normativo/in El retraso en Alta
alerta stitucional la declaración
temprana de emergencia
de la OMS internacional
y de China (anunciada el
30 de enero de
2020 cuando
el virus ya
circulaba
globalmente)
fue
causalmente
necesario para
que el brote
alcanzara
escala
pandémica
antes de que
se
implementara
n controles de
viaje.
N2 Conectivid Estructural/sis La dispersión Alta
ad aérea témico global en las
global sin primeras
controles semanas fue
tempranos posible por los
vuelos
internacionale
s antes de que
se declarara la
emergencia.
Nodo
estructural con

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
R* alto y S
moderado: la
conectividad
era el sistema,
pero los
controles
habrían
podido
modificar su
impacto.
N3 Desigualda Estructural La capacidad Alta
d en los de respuesta
sistemas de varió entre
salud países en
nacionales varios órdenes
de magnitud
según la
inversión
histórica en
salud pública.
En los países
con sistemas
debilitados,
cada caso
individual
tuvo mayor R*
efectivo por la
falta de
contención.
N4 Superpropa Individual Los eventos Alta
gadores en de
eventos de superspreadin
alta g
densidad documentados
(conferencias,
bodas,
servicios
religiosos,
instalaciones
de
procesamiento
de alimentos)
contribuyeron

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
desproporcion
adamente a la
transmisión en
las primeras
semanas.
N5 Políticas de Normativo Las Alta
comunicaci comunicacion
ón que es de varios
minimizaro gobiernos que
n el riesgo minimizaron
el riesgo en las
primeras
semanas
redujeron el α
individual al
no activar los
comportamien
tos
preventivos
cuando aún
eran más
eficaces.
N6 Condicione Estructural Para una Alta
s de trabajo fracción
que significativa de
impedían el la fuerza
aislamiento laboral
(trabajadores
esenciales sin
cobertura
social para
días perdidos),
el Fobos al
aislamiento era
real: perder el
empleo o el
ingreso era la
consecuencia.
Este nodo
amplificó la
transmisión
comunitaria.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
N7 Origen del Origen La pregunta Baja/in
virus más cierta
(zoonótico políticamente
o sensible del
laboratorio) análisis. Su R*
en la escala de
la pandemia es
real pero no es
el dominante:
el brote habría
alcanzado
escala
catastrófica
con cualquier
origen dado
N1-N6.
Nf Población Nodo final Más de 20 —
mundial millones de
muertes en
exceso (OMS,
2023). No
entra en el
cálculo de R*.
B.3 R* y la narrativa política: dónde divergen
El análisis de R* produce una distribución que diverge
significativamente de las narrativas políticas dominantes
sobre la pandemia. Esa divergencia es informativamente
valiosa:
Nodo R* α Divergencia
estimad estimad con narrativa
o o política
N1 — Sistemas ~28% 0.10 Δ = +0.18.
alerta OMS/China Narrativa
política: "China
fue responsable."

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
El análisis
muestra que N1
es el nodo de
mayor R* pero el
sistema de alerta
de la OMS (que
tardó en declarar
la emergencia)
también
comparte este
nodo. La
responsabilidad
es institucional
compartida, no
de un solo
Estado.
N2 — ~22% 0.05 Δ = +0.17.
Conectividad Narrativa: pocas
aérea referencias. El
cierre de rutas
aéreas tempranas
habría reducido
significativament
e la escala. Pero
fue un nodo
estructural que
ningún actor
individual
controló
unilateralmente.
N3 — ~18% 0.08 Δ = +0.10.
Desigualdad Narrativa:
sanitaria raramente
mencionado en
la narrativa
dominante. Es el
nodo que
muestra que la
pandemia no fue
homogénea: los
países con mayor
inversión
histórica en salud

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
pública tuvieron
menor R*
efectivo.
N4 — ~12% 0.30 Δ = -0.18.
Superpropagadore Narrativa: a
s veces usado para
culpabilizar a
individuos. El
análisis muestra
que su α
promedio fue
mayor que el
esperado en
ausencia de las
condiciones de
N6.
N5 — ~12% 0.15 Δ = +0.07.
Comunicación Narrativa:
minimizante debatido
políticamente. El
análisis muestra
que es un nodo
real pero no
dominante.
N6 — Cond. ~6% 0.20 Δ = -0.14.
trabajo (Fobos) Narrativa:
raramente
mencionado. Es
el nodo que
muestra el fraude
annona del
Estado:
trabajadores
esenciales
transmitieron
más porque el
sistema no les
dio condiciones
para aislarse.
N7 — Origen del ~2% 0.00 Δ = +0.02.
virus Narrativa:

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
políticamente
dominante. El
análisis muestra
que su R* en la
escala de la
pandemia es
mínimo: con N1-
N6 intactos, el
brote habría
alcanzado escala
catastrófica con
cualquier origen.
La conclusión más contraintuitiva del análisis: el origen del
virus (N7), que domina el debate político internacional,
tiene el menor R* de todos los nodos en la escala del daño.
No porque no importe quién creó el virus sino porque,
dado el sistema de respuesta que existía (N1-N6), el daño
habría sido comparable con cualquier origen. La pregunta
por el origen es legítima para prevenir futuros brotes, pero
es casi irrelevante para explicar por qué este brote alcanzó
la escala que alcanzó.
B.4 Los superpropagadores del COVID-19 y el
análisis de hijos
El COVID-19 mostró el patrón 80/20 de
superpropagación con inusual claridad: estudios en varios
países documentaron que entre el 10% y el 20% de los casos
fueron responsables del 80% de las infecciones secundarias.
La gran mayoría de los casos no transmitieron a nadie.
El análisis de hijos de los superpropagadores identificados
en los primeros meses del brote revela un perfil
predominante que tiene implicaciones directas para la
política de intervención:

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
Perfil del Hijo Implicación para la
superpropagador dominante intervención
COVID-19
Trabajador esencial Fobos No se aisló porque no
(atención médica, podía económicamente.
alimentos, transporte) La intervención correcta
sin cobertura social no es la sanción sino la
compensación: subsidio
de aislamiento, protección
del empleo, equipo de
protección adecuado.
Persona que no Deimos No se aisló porque no
reconoció los sabía que debía hacerlo.
síntomas como La intervención correcta
COVID-19 en las es diagnóstico accesible y
primeras semanas comunicación clara, no
culpabilización.
Persona que asistió a Potós Actuó sobre la base de la
un evento social información anterior al
creyendo que el riesgo punto de actualización. El
era bajo (información vector de voluntad seguía
incorrecta) apuntando hacia las
normas sociales previas a
la pandemia.
Negacionista activo Anteros Minoría, pero visible. La
que rechazó todas las intervención directa
medidas refuerza el Anteros. Las
normas de grupo que
hacen que la cooperación
sea la norma son más
eficaces.
El perfil dominante entre los superpropagadores no fue
Anteros (negación deliberada): fue Fobos, Deimos y Potós.
Es decir: la mayoría de los superpropagadores no eligieron
transmitir —fueron colocados por el sistema en una
posición donde transmitir era la consecuencia inevitable de
las condiciones. Eso es el fraude annona del sistema hacia
los trabajadores esenciales: el Estado necesitaba que

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
siguieran trabajando (N6 tiene α bajo porque el Estado no
generó las condiciones para que pudieran aislarse) y eso
amplificó la transmisión.
B.5 El daño del COVID-19 en tiempo de vida
Estimaciones de referencia (OMS, 2023):
• Muertes en exceso globales: 14.9–19.8 millones
(estimación OMS). Se usa 17 millones como valor
central.
• Esperanza de vida promedio perdida por muerte
prematura: ~15 años (dada la distribución por edad de
las muertes).
• Años de vida ajustados por discapacidad (AVAD)
incluyendo COVID largo y morbilidad grave:
estimados en ~280-320 millones de AVAD totales
(2020-2022).
• Salario de referencia global 2024: w_ref = $8 USD/hora
PPP.
D_vital_directo (muertes):
D_vital_directo = 17,000,000 × 15 años × 8,760 h/año
= 2.234 × 10¹² horas
D_monetary_directo ≈ $17.9 billones USD (2024)
D_vital_total incluyendo AVAD (T_impedido +
ΔT_trayectoria):
D_vital_AVAD = 300,000,000 AVAD × 8,760 h/año =
2.628 × 10¹² horas adicionales
D_monetary_AVAD ≈ $21.0 billones USD (2024)
D_vital_total:

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
D_vital_total ≈ 4.862 × 10¹² horas de vida
D_monetary_total ≈ $38.9 billones USD (2024)
Distribución del daño entre nodos responsables (AD_i =
R*ᵢ × D_total):
Nodo R* AD Quién debería asumir
(billones
USD)
N1 — Sistemas 28% $10.9B Reforma institucional de
alerta la OMS y de los sistemas
de alerta nacional. La
compensación económica
directa es menos relevante
que la reforma estructural.
N2 — 22% $8.6B Inversión en sistemas de
Conectividad control de viajes con
aérea respuesta rápida.
Protocolos de cierre de
rutas ante alertas
tempranas.
N3 — 18% $7.0B Los países con mayor R*
Desigualdad por esta causa son
sanitaria también los que menos
inversión histórica en
salud tienen. La equidad
en la distribución de
vacunas y recursos fue el
primer paso de α
institucional.
N5 — 12% $4.7B Responsabilidad de los
Comunicación gobiernos que
minimizaron el riesgo en
los primeros meses. AD
específico a cada gobierno
según su patrón de

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
comunicación
documentado.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
§5. Límites del método en
epidemiología
5.1 La incertidumbre sobre los pesos en
tiempo real
En un brote activo, los pesos del grafo son inciertos porque
la evidencia está siendo generada simultáneamente con la
toma de decisiones. Los modelos de R₀ tienen la misma
limitación: el R₀ estimado en las primeras semanas de un
brote tiene intervalos de confianza muy amplios. El cálculo
de R* en tiempo real debe incluir explícitamente esa
incertidumbre mediante rangos de pesos y análisis de
sensibilidad, no valores puntuales.
5.2 La causalidad en múltiples escalas
simultáneas
Una pandemia opera en múltiples escalas causales
simultáneamente: la escala molecular (la carga viral del
patógeno), la escala individual (el comportamiento de las
personas infectadas), la escala comunitaria (las condiciones
de vida y trabajo), la escala nacional (las políticas de salud
pública) y la escala global (los sistemas internacionales de
alerta y respuesta). El grafo completo tendría miles de
nodos. En la práctica, el análisis debe seleccionar los nodos
más relevantes para la pregunta específica que se intenta
responder.
5.3 El problema de la causalidad
contrafáctica en pandemia
El cálculo de R* requiere estimar qué habría ocurrido sin
cada nodo. En una pandemia, el contrafáctico es

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
especialmente difícil porque las intervenciones cambian el
comportamiento de los otros nodos: si N1 hubiera activado
la alerta dos semanas antes, N2 y N5 también habrían
actuado diferente. El grafo completo con dinámicas de
respuesta requiere modelos epidemiológicos más
sofisticados que el cálculo estático de R*.
5.4 Los hijos y la privacidad de los
superpropagadores
El análisis de hijos de superpropagadores identificados
plantea problemas de privacidad y estigmatización que el
análisis forense post-brote debe gestionar con cuidado. El
objetivo del análisis de hijos no es culpabilizar a los
superpropagadores sino orientar la política de intervención
hacia las causas estructurales (Fobos: condiciones de
trabajo) en lugar de hacia el comportamiento individual
(Anteros: negación deliberada). Si el análisis se usa para
identificar y sancionar a individuos, pierde su valor y
produce efectos contraproducentes.
5.5 R* no predice quién será el próximo
superpropagador
R* identifica retrospectivamente qué nodos tuvieron mayor
peso causal en el brote analizado. No predice qué nodo será
el superpropagador en el próximo brote, porque esa
posición depende de condiciones (carga viral, posición en
la red de contactos, entorno) que varían en cada caso. Lo
que el análisis de R* permite en sentido prospectivo es
identificar los tipos de nodos (trabajadores esenciales en
espacios cerrados, personas sin cobertura de aislamiento)
que tienden a tener mayor R* bajo condiciones similares, y
diseñar intervenciones estructurales para reducir ese peso
antes del próximo brote.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología

§6. Profundización formal — Esta sección puede saltarse sin perder el
argumento del capítulo
§6. Profundización formal
6.1 La relación entre R₀, Re y R*
Los tres indicadores son relacionados, pero
matemáticamente distintos:
Indicador Definición formal Relación con R*
R₀ E[número de R₀ = ρ(K) donde K es la
infecciones matriz de siguiente
secundarias en generación del modelo
población epidemiológico. R₀ es un
totalmente escalar (un número). R* es un
susceptible] vector. R₀ describe la
dinámica global; R* distribuye
el peso causal entre nodos.
Re (Rt) Número efectivo de Re(t) = R₀ × S(t)/N donde
reproducción en S(t) es la fracción susceptible.
tiempo t, con Re es también un escalar. R*
inmunidad parcial captura lo que Re no puede:
de la población. cuáles nodos específicos
están aportando más a ese Re
en un momento dado.
R* causal Eigenvector R* se calcula sobre el grafo
dominante de la de influencias causales, no
matriz de pesos W sobre el modelo de dinámica
del grafo poblacional. Puede incluir
epidemiológico nodos estructurales y
causal. normativos que ninguno de
los dos anteriores incluye.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
La relación entre R₀ y R* puede expresarse
aproximadamente así: si R₀ = Σᵢ R*ᵢ × transmisibilidad_ᵢ,
entonces R₀ es una media ponderada de las contribuciones
de transmisión de todos los nodos, mientras R* es la
distribución de esas contribuciones. R₀ alto con R*
concentrado en pocos nodos sugiere que intervenir en esos
nodos reducirá R₀ eficientemente. R₀ alto con R*
distribuido sugiere que se necesita intervención en múltiples
frentes simultáneamente.
6.2 El modelo SIR con nodos heterogéneos
El modelo SIR clásico (Susceptible-Infectado-Recuperado)
es homogéneo: todos los individuos son igualmente
transmisores. Una extensión que incorpora la
heterogeneidad de R* es el modelo con distribución k del
número de infecciones secundarias:
Var(k) / E(k) >> 1 → superpropagación dominante
donde k es el número de infecciones secundarias por caso.
Lloyd-Smith et al. (2005) modelaron k como una
distribución binomial negativa con parámetro de dispersión
p. Un p pequeño (p < 0.1) indica fuerte superpropagación.
Para el COVID-19, los estimados de p estuvieron entre 0.1
y 0.3, consistentes con el patrón 80/20 observado.
En términos del grafo causal, el parámetro p está
relacionado con la varianza de R* entre nodos:
Var(R*) ∝ 1/p → p pequeño ⟺ R* concentrado en
pocos nodos
Esto formaliza la relación entre superpropagación (p
pequeño en el modelo epidemiológico) y R* concentrado
(pocos nodos con alto peso causal) en el grafo causal.

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
6.3 El cálculo del fraude annona
epidemiológico
El fraude annona epidemiológico del Estado se calcula
como:
FA_epi = R*_Estado × D_total × (1 − α_Estado)
donde R*_Estado es la suma de R* de todos los nodos
institucionales/normativos controlados por el Estado (N1,
N3, N5, N6 en el caso COVID), D_total es el daño total
del brote, y (1 − α_Estado) es la fracción no asumida.
Este monto FA_epi es la base para:
• Calcular la responsabilidad del Estado en demandas
colectivas por negligencia en la respuesta pandémica.
• Establecer el presupuesto mínimo de inversión en salud
pública que el sistema requiere para que α_Estado sea
suficiente para evitar el fraude annona en el próximo
brote.
• Comparar la respuesta de distintos países: un país con
FA_epi bajo tiene un sistema de salud pública con alta
α; uno con FA_epi alto tiene un sistema que no generó
las condiciones materiales de posibilidad para contener
el brote.
6.4 Código Python de referencia para
epidemiología
import numpy as np from scipy.stats import pearsonr def
analisis_epidemiologico(W_epi, alpha_contencion,
D_total_AVAD, w_ref=8.0, R0_observado=None):
""" Análisis de responsabilidad causal en brote epidemiológico.
W_epi: matriz de pesos del grafo epidemiológico
alpha_contencion: α por nodo (contención: aislamiento, reporte, etc.)
D_total_AVAD: AVAD totales del brote (estándar OMS) w_ref:
salario de referencia (USD/hora, default global) R0_observado: R0
del brote si disponible (para comparación) """ n = W_epi.shape[0]
# ── R* causal ── R = np.ones(n) / n for _ in range(500):
Rn = W_epi @ R; s = np.sum(Rn) if s < 1e-12: break Rn /= s

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
if np.max(np.abs(Rn - R)) < 1e-9: break R = Rn R_star = Rn
# ── S: fungibilidad del nodo en la cadena ── S = np.zeros(n) for
i in range(n): max_c = 0 for j in range(n): if j == i:
continue Wm = W_epi.copy() Wm[i,:] = np.mean(W_epi,
axis=0) Rm = np.ones(n)/n for _ in range(200):
Rm2 = Wm @ Rm; sm = np.sum(Rm2) if sm < 1e-12: break
Rm2 /= sm if np.max(np.abs(Rm2-Rm)) < 1e-6: break
Rm = Rm2 c, _ = pearsonr(R_star, Rm2) max_c =
max(max_c, abs(c)) S[i] = 1 - max_c Delta = R_star -
alpha_contencion R_neta = R_star * (1 - S) # ── Daño en tiempo
de vida (AVAD → horas) ── horas_por_AVAD = 365.25 * 24 # 1
AVAD = 1 año = 8,766 horas D_vital_horas = D_total_AVAD *
horas_por_AVAD D_monetary = D_vital_horas * w_ref # ──
Distribución del daño ── AD = R_star * D_monetary # ajuste
debitor por nodo # ── Fraude annona epidemiológico ── #
nodos_estado: índices de los nodos institucionales/normativos # Se
calcula externamente y se pasa como argumento R_star_estado =
np.sum(R_star[R_star > np.percentile(R_star, 70)]) FA_epi =
R_star_estado * D_monetary * np.mean(1 - alpha_contencion) result
= { 'R_star': R_star, 'S': S, 'Delta_contencion': Delta,
'R_neta': R_neta, 'D_vital_horas': D_vital_horas,
'D_monetary': D_monetary, 'AD_por_nodo': AD,
'fraude_annona_epi': FA_epi, 'J_sistema': float(1 -
np.sum(np.abs(Delta))), 'nodos_prioritarios': np.argsort(-R_neta)[:3],
} if R0_observado: # Consistencia aproximada: R* alto
correlacionado con R0 alto result['R0_observado'] = R0_observado
result['R_estrella_promedio'] = float(np.mean(R_star[R_star > 0]))
return result # ── Ejemplo: John Snow — Cólera Broad Street 1854
── W_snow = np.array([ [0, 0, 0, 0, 0, 0], # N1 (bomba) →
Nf [0.95, 0, 0, 0, 0, 0], # N2 (pozo) → N1 [0.70, 0.60, 0,
0, 0, 0], # N3 (infr.) → N1, N2 [0, 0, 0.80, 0, 0, 0], # N4
(autoridades) → N3 [0, 0, 0, 0, 0, 0], # N5 (casos indiv.) →
Nf [0, 0, 0, 0, 0, 0], # Nf (sumidero) ]) # Añadir aristas a Nf
W_snow[0,5]=0.90; W_snow[2,5]=0.60; W_snow[4,5]=0.85 alpha_snow
= np.array([0.00, 0.00, 0.00, 0.05, 0.10, 0.0]) # AVAD estimados para el
brote de Soho: ~800 (616 muertes × factor AVD) resultado_snow =
analisis_epidemiologico( W_snow, alpha_snow, D_total_AVAD=800,
w_ref=8.0, R0_observado=2.8 ) nodos_snow = ['N1-Bomba','N2-
Pozo','N3-Infraest.','N4-Autoridades','N5-Casos','Nf'] print("=== John
Snow — Broad Street 1854 ===") for i, (nm, rs, si, di) in enumerate(zip(
nodos_snow[:5], resultado_snow['R_star'][:5], resultado_snow['S'][:5],
resultado_snow['Delta_contencion'][:5])): flag = ' ← Snow lo
identificó' if i == 0 else '' print(f" {nm:18s} R*={rs:.3f} S={si:.2f}
Δ={di:+.3f}{flag}") D_mon = resultado_snow['D_monetary'] FA =
resultado_snow['fraude_annona_epi'] J = resultado_snow['J_sistema']
print(f"\nJ (justicia estructural): {J:.3f}") d_m = D_mon/1e6
print(f"D_monetary_equiv: {d_m:.1f} M USD (2024)") fa_m =
FA/1e6 print(f"Fraude annona epidem.: {fa_m:.1f} M USD")

El Cálculo de la Responsabilidad · Cap. 6 — Epidemiología
Miguel Hilario Olvera Aguilar
Centro Multidisciplinario Meriadock Formación y Asesoría A.C., 2026
Continúa en el Capítulo 7 — Tanatología y duelo

El Cálculo de la Responsabilidad · Cap. 7 — Tanatología y duelo

