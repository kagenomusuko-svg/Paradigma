## PARTE VI · Ciencias Sociales y Humanidades

### Capítulo 44
Ciencia política y procesos electorales
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Nivel B: deriva y amplía los instrumentos del
paradigma para el dominio de la ciencia política y los procesos electorales.
El dominio tiene una característica que lo distingue de todos los demás
capítulos de la Parte VI: la causalidad opera tanto a nivel del acto
individual —el funcionario que alteró el resultado, el algoritmo que
suprimió el discurso político de un lado— como a nivel de la estructura
sistémica —el diseño de los distritos electorales, las reglas de
financiamiento de campaña, el sistema de acceso a los medios. El
instrumento central del capítulo es el ILE (Índice de Legitimidad
Electoral) — la medida de la brecha entre los procedimientos
democráticos declarados de un proceso electoral y los procedimientos
realmente implementados.
Los instrumentos de referencia principales de este capítulo son el IIC del
cap. 35 (el IIC_político mide la congruencia entre los valores
democráticos declarados y el comportamiento observable de las
instituciones electorales), el cap. 13 (IA y algoritmos, para la
manipulación algorítmica del discurso político) y el cap. 43 (distinción
detonadora/estructura, para separar el fraude electoral individual del
diseño sistémico que lo habilita).
Si tu caso es de fraude electoral directo (manipulación de actas o votos),
ve a §1 sub-variante 1 y §5 configuración 1. Si es de manipulación de
la información durante la campaña (desinformación, Cambridge
Analytica tipo), ve a §3 y §5 configuración 2. Si es de supresión del voto
por barreras estructurales o gerrymandering, ve a §5 configuración 3.
Para la jerarquía de evidencia, ve directamente a §2.

Taxonomía General de Aplicaciones
Nota de calibración: rangos Nivel B — derivados por extensión desde
los principios del sistema. Pendientes de calibración empírica con litigios
electorales documentados.
§1 Descripción del subcampo
La ciencia política y los procesos electorales son el dominio
donde el daño producido por la manipulación del sufragio
tiene una propiedad que ningún otro dominio de la
Taxonomía comparte: el daño es simultáneamente individual
—el votante cuyo voto fue suprimido, el candidato cuya
victoria fue robada— y sistémico —la confianza en el proceso
democrático como mecanismo de legitimación del poder
político, cuya erosión produce daño a todos los miembros de
la comunidad política independientemente de su preferencia
electoral. El fraude electoral individual produce D_individual;
la erosión sistemática de la confianza en el proceso produce
D_sistémico, que puede superar al D_individual en varios
órdenes de magnitud.
La distinción central del dominio es entre tres tipos de
manipulación electoral con grafos causales distintos. La
manipulación directa del resultado: la alteración de las actas, el
relleno de urnas, la destrucción de votos. La manipulación del
proceso: el diseño de los distritos electorales, las reglas de
financiamiento de campaña, los requisitos de registro de
votantes, el acceso a los medios — el conjunto de reglas que
determinan quién puede competir y en qué condiciones. La
manipulación del entorno informativo: la desinformación
organizada, la supresión algorítmica del discurso político de
ciertos grupos, la micro-segmentación de mensajes electorales
con datos personales sin consentimiento. Cada tipo tiene un
nodo de mayor R* distinto y una distribución distinta del S
entre el actor individual y la estructura sistémica.
El ILE (Índice de Legitimidad Electoral) y el IIC_político

Taxonomía General de Aplicaciones
El ILE mide la brecha entre los procedimientos democráticos declarados de
un proceso electoral —los establecidos en la constitución, la ley electoral y los
estándares internacionales de derechos políticos— y los procedimientos
realmente implementados. ILE ∈ [0, 1]: ILE = 1 indica la implementación
completa de los procedimientos declarados; ILE = 0 indica la ausencia total
de congruencia entre lo declarado y lo implementado.
ILE = corr (procedimientos_electorales_declarados,
procedimientos_electorales_implementados)
El ILE es la aplicación del IIC (cap. 35) a las instituciones electorales: el
IIC_político de un sistema electoral mide la congruencia entre sus valores
democráticos declarados y su comportamiento observable. ILE bajo es la firma
del fraude electoral sistémico: la institución electoral declara garantizar el
sufragio libre y secreto mientras implementa procedimientos que lo
distorsionan. R*_diseñador_del_sistema sobre el D_electoral es positivo
proporcional a (1 − ILE).
Sub-variantes del dominio electoral
Sub-variante Descripción y singularidades del dominio
Fraude electoral La alteración directa del recuento de votos o de los
directo: documentos que lo registran. Es la sub-variante con
manipulación de mayor visibilidad mediática y menor R* sistémico en
actas, relleno de los sistemas democráticos consolidados: el fraude
urnas, directo a escala suficiente para alterar el resultado de
destrucción de una elección nacional requiere la participación de
votos decenas o cientos de funcionarios, lo que hace que
la S de cada funcionario individual sea moderada-alta
(cualquier otro funcionario en esa posición bajo las
mismas instrucciones habría producido el mismo
resultado) y el R* del diseñador del esquema de
fraude sea el nodo dominante.
Gerrymandering El diseño de los límites de los distritos electorales de
y manipulación manera que concentra o dispersa a los votantes de
de los distritos ciertos grupos para maximizar la ventaja electoral del
electorales partido que controla el proceso de redistribución. Es
la sub-variante de mayor S sistémica del dominio: el
gerrymandering es legal en muchos sistemas y
habitual en el sentido de que cualquier partido en la
posición del diseñador haría lo mismo. El R* del

Taxonomía General de Aplicaciones
Sub-variante Descripción y singularidades del dominio
diseñador es alto cuando la manipulación produce
resultados electorales sistemáticamente distintos de
la preferencia popular y cuando el diseño fue
idiosincrático respecto a los estándares técnicos
disponibles.
Financiamiento El financiamiento de campañas electorales con
ilegal de dinero de origen prohibido, con cantidades
campañas: el superiores a los límites legales, o sin la transparencia
dinero que requerida. El R* del financiador sobre el daño a la
distorsiona la competencia electoral es positivo proporcional a la
competencia condición causal del financiamiento sobre el
electoral resultado — la pregunta es si el candidato financiado
habría ganado sin el financiamiento ilegal. Se
conecta con el cap. 2 (PLD) para el análisis del
origen de los fondos.
Supresión del El diseño de requisitos de registro, horarios de
voto: barreras votación, accesibilidad de los centros de votación, y
estructurales procesos de verificación de identidad que producen
que impiden el disparate impact sobre grupos específicos de
ejercicio del votantes — que tienen menor tasa de ejercicio del
sufragio a sufragio como consecuencia de esas barreras, no de
ciertos grupos su preferencia. El análisis del disparate impact (test
de los 4/5 del cap. 37) se aplica a las tasas de registro
y participación electoral: si la tasa del grupo afectado
es inferior al 80% de la del grupo de referencia
controlando por las variables de acceso, hay
supresión del voto estructural.
Manipulación La desinformación organizada durante la campaña
del entorno electoral, la micro-segmentación de mensajes
informativo: electorales con datos personales obtenidos sin
desinformación, consentimiento (Cambridge Analytica tipo), y la
micro- supresión algorítmica del discurso político de ciertos
segmentación y grupos o candidatos en las plataformas digitales. Se
supresión conecta con el cap. 13 (IA y algoritmos) para el
algorítmica análisis del R* del diseñador de la métrica del
algoritmo sobre el sesgo político del contenido
promovido. El D_electoral de la desinformación
requiere establecer la brecha entre la preferencia
informada del votante y la preferencia producida por
la desinformación.
Interferencia Un Estado extranjero —o actores con respaldo
extranjera en estatal extranjero— intervino en el proceso electoral

Taxonomía General de Aplicaciones
Sub-variante Descripción y singularidades del dominio
elecciones: el de otro Estado mediante la desinformación, el
Estado exterior financiamiento de campañas, la manipulación de la
como nodo del infraestructura tecnológica del proceso electoral, o el
grafo electoral uso de sus activos de inteligencia para beneficiar a
un candidato o partido. El R* del Estado extranjero
sobre el daño a la integridad del proceso electoral es
positivo proporcional a la condición causal de la
interferencia sobre el resultado o sobre la confianza
en el proceso.
Violencia e El uso de la violencia física, la amenaza, o la
intimidación intimidación para impedir el ejercicio del sufragio de
electoral: el uso ciertos grupos, para obligar a los votantes a votar en
de la fuerza para un sentido determinado, o para disuadir a candidatos
distorsionar el de presentarse. Se conecta con el cap. 1 (derecho
sufragio penal y civil) para el D_vital de las víctimas de la
violencia electoral y con el cap. 43 (geopolítica) para
el análisis de la estructura de impunidad que hace
posible la violencia electoral sistemática.
§2 Escala de evidencia Hi0–Hi8 aplicada al
dominio electoral
La escala Hi0–Hi8 (Parte VI) se aplica en el dominio electoral
con énfasis en los documentos del proceso electoral: las actas
de escrutinio, los registros de votantes, los informes de los
observadores electorales, los análisis estadísticos de los
resultados, y los documentos del financiamiento de campaña.
La característica más relevante del dominio es la posición de
los análisis estadísticos de los resultados (Hi2): en el dominio
electoral, la estadística de los resultados puede ser la fuente
más robusta para detectar anomalías en el proceso,
especialmente cuando el fraude fue diseñado para no dejar
rastro documental directo.

Taxonomía General de Aplicaciones
Tipo de
evidencia en Descripción y ejemplos en Rango
Nivel
procesos el dominio electoral w
electorales
Hi1 Documentos Las actas de escrutinio [0.72,
primarios del originales firmadas por los 0.90]
proceso electoral representantes de los partidos
con cadena de en cada mesa de votación. Los
custodia registros de votantes con las
verificada: actas firmas de los electores que
de escrutinio, ejercieron el sufragio. Los
registros de registros contables del
votantes, financiamiento de campaña
documentos de con los comprobantes de los
financiamiento ingresos y los gastos. Las
grabaciones de las cámaras de
los centros de votación donde
se produjo la alteración. Son los
documentos Hi1 del dominio:
su existencia establece el nexo
causal con el nivel de certeza
más alto disponible.
Hi2 Análisis El análisis estadístico de los [0.62,
estadístico de los resultados electorales que 0.80]
resultados detecta anomalías
electorales con inconsistentes con los
metodología mecanismos aleatorios del
documentada + proceso: la prueba de Benford
informes de sobre la distribución de los
observadores dígitos de los resultados, el
electorales análisis de correlación entre los
internacionales resultados y las características
acreditados de las mesas de votación, el
análisis de las discontinuidades
en las series temporales del
recuento. Los informes de las
misiones de observación
electoral de la OEA, la UE o la
OSCE, que tienen acceso a los
documentos y al proceso
durante el día de la elección.
Hi3 Testimonios Las declaraciones de [0.52,
convergentes de funcionarios electorales, 0.70]
funcionarios del representantes de partidos en
proceso electoral las mesas de votación, y

Taxonomía General de Aplicaciones
Tipo de
evidencia en Descripción y ejemplos en Rango
Nivel
procesos el dominio electoral w
electorales
con personal de los centros de
corroboración votación que describen
documental consistentemente el mismo
parcial patrón de irregularidades, con
al menos un documento
institucional compatible con el
patrón descrito. La
convergencia desde múltiples
testigos con posiciones
distintas en el proceso aumenta
el peso de la arista.
Hi4 Análisis del El análisis estadístico de las [0.42,
disparate impact tasas de registro y participación 0.60]
en las tasas de electoral desagregadas por
participación grupo: si la tasa del grupo
electoral afectado por las barreras
controlando por estructurales es inferior al 80%
variables de la tasa del grupo de
socioeconómicas referencia controlando por las
variables socioeconómicas
disponibles, hay supresión del
voto estructural documentable
(Hi4). El test de los 4/5
aplicado al dominio electoral.
Hi5 Análisis La comparación entre el [0.30,
comparado de resultado electoral y las 0.50]
los resultados encuestas de opinión del
electorales con el período, las tendencias
contexto históricas del voto en ese
electoral previo y territorio, y los resultados de
las encuestas de elecciones simultáneas en
opinión del territorios comparables — que
período establece si el resultado es
estadísticamente consistente
con el contexto o si presenta
anomalías que requieren
explicación.
Hi6 Denuncias Las denuncias formales [0.16,
formales de los presentadas por los partidos o 0.34]
partidos o candidatos afectados ante la

Taxonomía General de Aplicaciones
Tipo de
evidencia en Descripción y ejemplos en Rango
Nivel
procesos el dominio electoral w
electorales
candidatos autoridad electoral o judicial,
afectados ante la con la descripción de las
autoridad irregularidades observadas y sin
electoral corroboración documental
independiente todavía
disponible.
Hi7 Testimonios de Los testimonios de votantes [0.06,
votantes sobre sobre la presión recibida, la 0.20]
presión, intimidación, o las
intimidación o irregularidades observadas en el
irregularidades centro de votación, sin
sin corroboración documental ni
corroboración testimonial independiente.
documental
Hi8 Alegaciones de Las afirmaciones sobre fraude [0.02,
fraude o o manipulación electoral sin 0.12]
manipulación sin ningún respaldo documental,
evidencia estadístico o testimonial
documental ni verificable.
estadística
Hi0 Análisis Hi2 que Análisis estadístico Hi2 que w =
establece establece que los resultados 0.00
positivamente la electorales son consistentes
ausencia de con el contexto electoral previo
anomalías en el y las distribuciones esperadas, y
proceso análisis Hi1 que establece que
los documentos del proceso
son coherentes y completos.
La prueba de Benford y el análisis estadístico como Hi2
en el dominio electoral
La distribución de Benford establece que, en conjuntos de datos de origen
natural, los primeros dígitos no tienen distribución uniforme: el dígito 1
aparece como primer dígito el 30% de las veces, el 2 el 17%, y así
sucesivamente de forma logarítmica. Los resultados electorales legítimos
tienden a seguir la distribución de Benford; las alteraciones sistemáticas
del recuento producen desviaciones estadísticamente significativas de esa

Taxonomía General de Aplicaciones
distribución. Cuando el análisis estadístico detecta una desviación
significativa (p < 0.05), establece un patrón de anomalía que requiere
explicación — no prueba el fraude, pero desplaza la carga de la prueba
hacia quien debe explicar la anomalía.
La posición del análisis estadístico en la escala Hi2 refleja que es el
instrumento más potente disponible en muchos contextos electorales
donde el acceso a los documentos primarios es limitado — pero que
requiere el análisis metodológico riguroso por experto en estadística
electoral para alcanzar ese nivel de certeza. Una aplicación incorrecta de
la prueba de Benford (en elecciones con distritos pequeños donde la
distribución no aplica) produce resultados Hi6 o Hi7, no Hi2.
§3 El ILE, el IIC_político y los Hijos del actor
electoral
El IIC_político de un sistema electoral o de una institución
electoral es la aplicación del IIC del cap. 35 a la dimensión
política: mide la congruencia entre los valores democráticos
declarados de la institución —la garantía del sufragio libre,
secreto, universal e igualitario— y su comportamiento
observable en el diseño y la administración del proceso
electoral. El IIC_político bajo produce el mismo daño que el
IIC bajo en cualquier otra dimensión: erosiona la confianza en
la institución, produce selección adversa de los candidatos y
los participantes, y genera el ciclo de deslegitimación que
debilita el sistema democrático como mecanismo de
resolución pacífica de los conflictos políticos.
Hijo Firma
del Qué documenta
Fuente R*
actor informa l en el
típica resultante
electo para S dominio
ral electoral
Antero S bajo [0.05– Correos y Correos R*_actor
s 0.28]. El comunicacio internos del pleno sobre
actor diseñó nes internas equipo de el
deliberadam que campaña o D_electoral
ente el muestran el del partido. . El Anteros

Taxonomía General de Aplicaciones
Hijo Firma
del Qué documenta
Fuente R*
actor informa l en el
típica resultante
electo para S dominio
ral electoral
esquema de propósito Documento electoral es
manipulació deliberado s del la base para
n electoral de la proceso de la
— el diseño manipulació diseño de los responsabili
de los n. Datos que distritos o dad civil y
distritos para muestran el los potencialm
maximizar la conocimient requisitos de ente penal
ventaja o del efecto registro. por el daño
electoral, el discriminato Análisis del a la
sistema de rio antes de efecto integridad
requisitos de la discriminato del proceso.
registro que implementa rio
excluye ción del disponible
sistemáticam diseño. en el
ente al grupo Decisiones período.
protegido, el que
esquema de rechazan
financiamien alternativas
to ilegal, la menos
campaña de manipulador
desinformaci as
ón. El disponibles
resultado sin
dependía de justificación
ese actor documentad
específico a.
porque el
diseño tenía
rasgos
idiosincrátic
os que
cualquier
otro actor en
esa posición
no habría
necesariame
nte
replicado.
Potós S moderado- Diseño de Comparació R*_actor
alto [0.40– los distritos n con los moderado
0.68]. El o los sistemas de con S
actor siguió requisitos de otros moderado-

Taxonomía General de Aplicaciones
Hijo Firma
del Qué documenta
Fuente R*
actor informa l en el
típica resultante
electo para S dominio
ral electoral
las prácticas registro estados o alto. El
del sistema coherente jurisdiccione Potós
político del con el s del mismo establece
período — el estándar del período. que la
gerrymander sistema Análisis del reforma
ing que político del estándar del debe ser
todos los período. sistema sistémica —
partidos Ausencia de político para cambiar las
practican señales de el tipo de reglas que
cuando propósito decisión hacen
tienen la discriminato analizada. racional el
oportunidad, rio gerrymande
los requisitos idiosincrátic ring — más
de registro o. que
que son el Comparació individual.
estándar n con las
histórico del prácticas de
sistema, las otros actores
prácticas de en
financiamien posiciones
to que son equivalentes
habituales en que
el sector — muestran el
sin que sus mismo
decisiones patrón.
específicas
fueran
idiosincrática
s respecto al
estándar del
período. El
daño fue
producido
por prácticas
habituales
del sistema.
Fobos S moderado Comunicaci Comunicaci R*_actor
[0.30–0.55]. ones ones moderado.
El actor internas internas del El Fobos
adoptó donde el equipo de desplaza
prácticas de actor campaña o parte del R*
manipulació expresa del partido. hacia el

Taxonomía General de Aplicaciones
Hijo Firma
del Qué documenta
Fuente R*
actor informa l en el
típica resultante
electo para S dominio
ral electoral
n electoral preocupació Comparació sistema
motivado n por la n con las político que
por el miedo: práctica que prácticas del hace
el miedo a públicament oponente en racional la
perder la e defiende. el mismo escalada de
elección, el Evidencia de período. la
miedo a que que la manipulaci
el partido práctica fue ón — el
oponente adoptada equivalente
usara las como de la
mismas respuesta a presión del
herramientas prácticas mercado de
, el miedo a equivalentes capitales en
las del el C-suite
consecuenci oponente. corporativo
as de revelar Historial de .
la decisiones
desinformaci que
ón que el muestran la
equipo de escalada de
campaña la
había manipulació
diseñado. El n en
Fobos respuesta a
produce la la
manipulació manipulació
n electoral n del
deshonesta- oponente.
racional: el
actor sabe
que la
práctica es
éticamente
cuestionable
pero la
adopta
igualmente
porque el
sistema
político hace
que el costo
de no
hacerlo sea

Taxonomía General de Aplicaciones
Hijo Firma
del Qué documenta
Fuente R*
actor informa l en el
típica resultante
electo para S dominio
ral electoral
mayor que el
de hacerlo.
Deimo S alto [0.55– Ausencia de Análisis del R*_actor
s 0.82]. El análisis del estándar del bajo. El
actor disparate sistema Deimos
genuinament impact antes político del establece
e no anticipó de la período. que el daño
el efecto implementa Velocidad y fue
discriminato ción. calidad de la consecuenc
rio de la Respuesta respuesta del ia del riesgo
práctica inmediata y actor ante la sistémico.
electoral proporciona primera La reforma
adoptada, l del actor evidencia del del estándar
porque el cuando el disparate del sistema
análisis del efecto impact. político es
disparate discriminato el
impact no rio fue instrument
era el documentad o correcto.
estándar del o. Práctica
sistema coherente
político del con el
período o estándar del
porque la sistema
tecnología político del
disponible período sin
no permitía desviación
la detección idiosincrátic
de ese efecto a.
antes de la
implementac
ión. El daño
fue
consecuenci
a del riesgo
sistémico de
la práctica,
no de la
elección
deliberada
del actor.

Taxonomía General de Aplicaciones
§4 Tipos de nodo, tipos de arista y
configuraciones canónicas del dominio
Tipos de nodo en el grafo de responsabilidad electoral
R* en el grafo
Función en el
Tipo de nodo S típico de daño
grafo
electoral
Diseñador del Diseñó las Moderado-bajo R*_DSE ×
sistema reglas del [0.22–0.48] D_electoral ×
electoral proceso cuando el (1 − α_DSE).
(DSE) electoral: los diseño fue El R*_DSE
límites de los idiosincrático sobre el ILE
distritos, los — las reglas bajo incluye el
requisitos de específicas D_sistémico
registro, las producían el producido por
reglas de efecto la erosión de la
financiamiento discriminatorio confianza en el
, los que otras reglas proceso
procedimiento disponibles no electoral, no
s de recuento. habrían solo el D a los
R* positivo producido. votantes
cuando esas Moderado-alto específicos
reglas [0.48–0.70] afectados.
produjeron el cuando el
ILE bajo o el diseño seguía el
disparate estándar del
impact sistema político
documentado. del período.
Administració Administró el Alto [0.58– Fracción del
n electoral proceso 0.82] cuando R*_DSE que
(AE) electoral — el siguió el corresponde a
registro de procedimiento la ejecución
votantes, la institucional sin deficiente o a la
organización desviación desviación
del día de la idiosincrática, idiosincrática
elección, el incluyendo los del
recuento — procedimientos administrador
con la calidad deficientes respecto al
que el ILE diseñados por procedimiento
requería. R* el DSE. declarado.
positivo Moderado
cuando la [0.30–0.55]
administración cuando las
fue deficiente decisiones

Taxonomía General de Aplicaciones
R* en el grafo
Función en el
Tipo de nodo S típico de daño
grafo
electoral
respecto al idiosincráticas
estándar que el del
ILE declarado administrador
imponía, o fueron
cuando ejecutó condición del
con Anteros la fraude.
manipulación
del resultado.
Candidato o Fue el Moderado-bajo Proporcional al
partido beneficiario [0.15–0.40] conocimiento y
beneficiado del fraude o la cuando el la instrucción
(CPB) manipulación candidato o del fraude. El
electoral. R* partido diseñó candidato que
positivo o instruyó el genuinamente
cuando diseñó, fraude. Alto no conocía el
instruyó o [0.60–0.85] fraude de sus
conocía el cuando el seguidores
fraude y no lo fraude fue puede tener R*
denunció. R* producido por próximo a cero
nulo cuando actores que sobre el
genuinamente actuaban «en su D_electoral —
no conocía el beneficio» sin aunque tenga
fraude su un deber de
producido por conocimiento denuncia
terceros en su ni instrucción. cuando lo
beneficio. descubra.
Plataforma Gestionó el Moderado Fracción del
digital (PD) algoritmo que [0.35–0.60] D_electoral
determinó qué cuando la atribuible a la
contenido métrica del supresión o
político fue algoritmo era el amplificación
promovido o estándar de la algorítmica del
suprimido plataforma para discurso
durante la todo el político,
campaña contenido, con calculada desde
electoral. R* el sesgo político la diferencia
positivo como entre el alcance
cuando el consecuencia real del
diseño de la no buscada del discurso y el
métrica del diseño. alcance que
algoritmo Moderado-bajo habría tenido
produjo sesgo [0.20–0.38] con un
político cuando la

Taxonomía General de Aplicaciones
R* en el grafo
Función en el
Tipo de nodo S típico de daño
grafo
electoral
sistemático — métrica fue algoritmo
cuando la diseñada con neutral.
definición de conocimiento
«contenido del sesgo
relevante» o político que
«contenido producía.
seguro»
producía
disparate
impact sobre el
discurso de
ciertos
partidos o
candidatos.
Actor Un Estado o Moderado-bajo R*_AEX ×
extranjero actor con [0.20–0.45] D_electoral ×
(AEX) respaldo cuando la (1 − α_AEX).
estatal interferencia El α del actor
extranjero fue extranjero en el
intervino en el idiosincrática dominio
proceso de ese actor electoral es
electoral. R* extranjero próximo a cero
positivo específico en la mayoría
proporcional a (campañas de de los casos: la
la condición desinformación interferencia
causal de la diseñadas electoral es una
interferencia específicamente acción que rara
sobre el , hackeo de la vez produce
resultado o infraestructura reconocimient
sobre la electoral). Alto o de la
confianza en el [0.55–0.78] responsabilidad
proceso. cuando la .
interferencia
aprovechó
vulnerabilidade
s estructurales
del sistema de
información
electoral que
cualquier actor
extranjero bien
equipado
podría haber
explotado.

Taxonomía General de Aplicaciones
Configuraciones canónicas del dominio
Configuración 1 — Fraude electoral directo: el
diseñador del esquema de fraude como nodo dominante
DSE / CPB (actor con Anteros documentado que diseñó el esquema de
fraude: la instrucción de alterar las actas, el relleno de urnas en los centros de
votación controlados por el partido, la destrucción de votos del oponente — S
bajo [0.05–0.22] porque el diseño fue idiosincrático de ese actor) + AE
(administradores electorales que ejecutaron el esquema con S moderado-alto
[0.50–0.72]: cualquier funcionario bajo las mismas instrucciones y
consecuencias habría producido el mismo resultado — Fobos dominante en
la mayoría de los casos) → ILE bajo documentado con análisis Hi1/Hi2
→ D_electoral_directo = diferencial de votos alterados × w_democrático
El D_electoral_directo del fraude tiene dos componentes: el D a los
candidatos y partidos afectados (el diferencial de resultado atribuible al fraude)
y el D_sistémico a la confianza en el proceso (que puede superar al
D_directo). AD_DSE = R*_DSE × D_total × (1 − α_DSE). El
análisis del J del proceso post-fraude: cuando el sistema de consecuencias del
fraude electoral tiene J bajo, la señal es que el fraude seguirá produciéndose.
Configuración 2 — Manipulación del entorno
informativo: Cambridge Analytica (tipo)
Diseñador de la métrica del sistema de micro-segmentación (con Anteros
documentado: definió «perfil psicográfico objetivo» usando datos personales
obtenidos sin consentimiento para maximizar el impacto electoral del mensaje
— S bajo [0.10–0.28] porque el uso específico de los datos sin
consentimiento para la segmentación electoral era idiosincrático) +
Plataforma que cedió los datos sin el consentimiento de los usuarios (con Potós:
siguió las prácticas del sector del período sin verificar el uso final — S
moderado-alto [0.45–0.65]) + Campaña que contrató el servicio (con Fobos:
sabía que los métodos eran éticamente cuestionables pero los usó porque el
oponente podría usarlos igualmente — S moderado [0.32–0.52]) → Micro-
segmentación de mensajes electorales a ~87 millones de perfiles →
D_electoral = diferencial en las preferencias de los votantes afectados
atribuible a la desinformación

Taxonomía General de Aplicaciones
La aplicación del cap. 13 (IA y algoritmos) al dominio electoral: el diseñador
de la métrica tiene R* dominante porque la decisión de definir «objetivo del
mensaje» usando los perfiles psicográficos obtenidos sin consentimiento fue la
condición normativa del sistema. S del equipo técnico ≈ 1.0: cualquier equipo
técnico competente habría producido el mismo resultado con la misma métrica
y el mismo dataset. Cambiar el equipo técnico no habría cambiado el sesgo.
La reforma correcta: la regulación de la métrica (qué datos pueden usarse
para la segmentación electoral y con qué consentimiento), no la sustitución del
equipo técnico.
Configuración 3 — Supresión del voto y
gerrymandering: el diseño estructural como nodo
dominante
DSE (partido que controlaba el proceso de redistribución de distritos, con
Anteros documentado: el análisis racial de la distribución de votantes fue
usado explícitamente para diseñar los distritos de manera que diluyera el
poder electoral del grupo protegido — S moderado-bajo [0.22–0.40] cuando
el diseño produjo un disparate impact idiosincrático respecto a los estándares
técnicos alternativos disponibles) + DSE (legislatura que aprobó los
requisitos de registro o identificación que producen disparate impact sobre el
grupo protegido, con Potós en muchos casos: siguió el estándar del sistema
político del período — S moderado-alto [0.48–0.68]) → Tasa de
participación electoral del grupo protegido inferior al 80% de la tasa del grupo
de referencia (test de los 4/5) → D_electoral = valor del sufragio suprimido
× número de votantes afectados
El análisis de la supresión del voto requiere distinguir la supresión
idiosincrática (S bajo, Anteros dominante, reforma individual posible) de la
supresión estructural (S alto, Potós dominante, reforma sistémica necesaria).
Cuando el gerrymandering o los requisitos de registro eran el estándar del
sistema político, la reforma individual del actor específico no resuelve el
problema — la reforma de las reglas del juego es el instrumento correcto. El
IAS_electoral mide en qué medida las reformas post-escándalo actuaron sobre
el nodo estructural de mayor R*.

Taxonomía General de Aplicaciones
§5 Preguntas que responde este capítulo
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
¿Hay ILE bajo Análisis comparativo del Declaración A con
— cuál es la proceso declarado análisis estadístico
brecha entre el (constitución, ley electoral, Hi2 convergente +
proceso estándares internacionales) documentos Hi1 del
declarado y el versus el proceso proceso. Declaración
implementado? implementado (análisis B con análisis Hi3 de
estadístico Hi2 de los observadores +
resultados, informes de análisis estadístico
observadores electorales Hi4. Declaración C
Hi2, análisis del disparate cuando el ILE debe
impact Hi4). El ILE = estimarse desde
corr(procedimientos Hi5/Hi6 sin acceso
declarados, directo al proceso.
procedimientos
implementados) establece
la base del R*_DSE sobre
el D_electoral.
¿El Hijo del Análisis de las Declaración A con
actor electoral comunicaciones internas documentos Hi1 que
es Anteros, del actor, la comparación muestran el
Fobos o con las prácticas de actores conocimiento del
Deimos — cuál en posiciones equivalentes efecto y la decisión de
es la del mismo período, y la proceder. Declaración
idiosincrasia del velocidad de respuesta ante B con análisis Hi3
daño? las primeras evidencias del comparado con el
efecto discriminatorio. El estándar del sistema
Anteros produce S bajo; el político del período.
Potós o el Fobos produce Declaración C cuando
S moderado-alto; el el Hijo debe inferirse
Deimos produce S alto. sin acceso a las
comunicaciones
internas.
¿Hay disparate Test de los 4/5 aplicado a Declaración A con
impact — el las tasas de registro y análisis Hi2 del
diseño produce participación: si la tasa del disparate impact con
supresión del grupo protegido es inferior las variables de
voto de un al 80% de la tasa del grupo control adecuadas.
grupo de referencia controlando Declaración B con
protegido? por las variables análisis Hi4 del
socioeconómicas disparate impact
disponibles, hay disparate desde los datos

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
impact prima facie. El disponibles sin el
análisis de regresión conjunto completo de
logística con las variables controles.
de control establece si el
disparate impact persiste
después de controlar por
los factores legítimos.
¿La Análisis del mecanismo Declaración B con
interferencia causal de la interferencia: análisis Hi3/Hi4 del
extranjera fue ¿la campaña de mecanismo de la
condición desinformación o el hackeo interferencia y su
necesaria del de la infraestructura relación causal con el
resultado — electoral fue condición resultado.
cuál es su R*? necesaria del resultado Declaración A con
observado o del deterioro documentos Hi1/Hi2
de la confianza en el desclasificados sobre
proceso? La comparación las operaciones del
con elecciones equivalentes actor extranjero.
sin la interferencia
establece el contrafáctico.
¿Cuál es el D_electoral = D_directo Declaración B con
D_electoral (diferencial de votos o de análisis Hi4/Hi5 del
total — participación atribuible a la D_directo desde los
incluyendo el manipulación) + datos electorales +
D_sistémico a D_sistémico (daño a la análisis del
la confianza en confianza en el proceso D_sistémico desde las
el proceso? electoral como mecanismo encuestas de
de legitimación). El confianza
D_sistémico se estima institucional del
desde el análisis del período posterior.
impacto del escándalo
sobre la participación
electoral y la confianza
institucional en el período
posterior.
§6 Traducción de D_total al dominio electoral

Taxonomía General de Aplicaciones
D_electoral = D_sufragio + D_representación +
D_sistémico_democrático
El daño en el dominio electoral tiene tres componentes con nodos causales
distintos. El D_sufragio es el daño al votante individual cuyo voto fue
suprimido, alterado, o coaccionado: el valor del sufragio individual en términos
del derecho político suprimido, calculado desde el impacto del voto suprimido
sobre el resultado final. El D_representación es el daño a la colectividad cuya
representación política fue distorsionada por el fraude o la manipulación
estructural: el diferencial entre la representación que el resultado legítimo
habría producido y la representación real. El D_sistémico_democrático es el
daño a la confianza en el sistema democrático como mecanismo de legitimación
del poder político: el costo de la erosión de la confianza institucional medido
desde el impacto sobre la participación política y la estabilidad democrática.
Fuente
En el
de
Componente dominio Cómo se cuantifica
evidenc
electoral
ia
D_sufragio El daño El valor del sufragio Análisis
(daño al al votante individual no tiene precio estadísti
derecho cuyo voto de mercado — es un co Hi2
político del fue derecho fundamental. El del
votante suprimid D_sufragio se cuantifica número
individual) o, desde el impacto del voto de votos
alterado o suprimido sobre el suprimid
coaccion resultado: si N votos os por
ado: el fueron suprimidos en un las
ejercicio distrito que se decidió por barreras
del M votos (M < N), la estructur
derecho supresión fue condición ales o el
fundame necesaria del resultado en fraude.
ntal al ese distrito. Compar
sufragio ación
libre y con la
secreto, participa
cuya ción
privación esperada
constituy sin la
e un daño manipul
al votante ación
individual desde el
con análisis

Taxonomía General de Aplicaciones
Fuente
En el
de
Componente dominio Cómo se cuantifica
evidenc
electoral
ia
independ del
encia del disparat
resultado e
final de la impact.
elección.
D_representaci El daño a D_representación = Análisis
ón (daño la diferencial de escaños × Hi2 de
colectivo a la colectivid período de distorsión × los
representación ad cuya costo estimado de la planes
política represent política adoptada con la de
distorsionada) ación representación redistrib
política distorsionada versus la ución
fue política que habría alternati
distorsio adoptado la representación vos
nada por legítima. Para el técnica
el fraude gerrymandering: el mente
o el diferencial de escaños neutrale
gerryman entre el plan de s.
dering: el redistribución manipulado Análisis
diferencia y el plan neutral del
l entre la técnicamente optimizado. resultad
distribuci o
ón de electoral
escaños o bajo los
cargos distintos
que el planes.
resultado Historial
legítimo de
habría votacion
producid es del
o y la período
distribuci para
ón real. estimar
el D de
la
represen
tación
distorsio
nada.
D_sistémico_d El daño a D_sistémico = Encuest
emocrático la caída_en_la_participación as de
(daño a la confianza _electoral × período × confianz

Taxonomía General de Aplicaciones
Fuente
En el
de
Componente dominio Cómo se cuantifica
evidenc
electoral
ia
confianza en el institucio costo_unitario_de_la_part a
sistema nal en el icipación_perdida + instituci
democrático) sistema aumento_en_la_polarizaci onal del
democrát ón × período × período
ico como costo_estimado_de_la_po anterior
mecanis larización. Estimable y
mo de desde el análisis del posterio
legitimaci impacto de escándalos r al
ón del electorales documentados escándal
poder sobre la participación o
político, electoral y las encuestas de electoral
producid confianza institucional. . Datos
o por la de
percepció participa
n de que ción
el electoral
proceso del
electoral período.
está Análisis
manipula compara
do. La do del
erosión impacto
de la de
confianza escándal
reduce la os
participac electoral
ión es
electoral similares
y en
aumenta contexto
la s
polarizaci compara
ón bles.
política,
producie
ndo un
ciclo de
deslegiti
mación
con
efectos
de largo
plazo.

Taxonomía General de Aplicaciones
§7 Límites del método y errores frecuentes de
aplicación
Límite 1 — El contrafáctico del resultado electoral «legítimo»
tiene incertidumbre alta. El D_electoral requiere estimar cuál
habría sido el resultado sin la manipulación — un
contrafáctico que requiere supuestos sobre el comportamiento
del votante que rara vez tienen el nivel de certeza de Hi2. El
análisis debe declarar explícitamente la incertidumbre del
contrafáctico y presentar el D_electoral como un rango.
Límite 2 — La prueba de Benford tiene limitaciones
específicas en elecciones con distritos pequeños. La
distribución de Benford aplica a conjuntos de datos
suficientemente grandes: en elecciones con distritos de pocos
cientos de votantes, la distribución esperada no es benfordiana
y el análisis puede producir falsos positivos. La aplicación de
la prueba de Benford como Hi2 requiere verificar que el
tamaño del conjunto de datos cumple los requisitos
estadísticos del test.
Límite 3 — La manipulación del entorno informativo tiene
causalidad difusa. La relación entre la desinformación o la
micro-segmentación y la preferencia electoral del votante no
es directamente observable: el votante afectado por la
desinformación puede haber llegado a la misma preferencia
por otras vías. El D_electoral de la manipulación informativa
debe presentarse con incertidumbre alta — Hi5 en la mayoría
de los casos — excepto cuando los experimentos controlados
del período establecen el efecto causal de la técnica específica
usada.
Errores frecuentes de aplicación

Taxonomía General de Aplicaciones
Por qué Consecue
Error Corrección
ocurre ncia
Concentrar el R* El R*_DSE La primera
en el ejecutor funcionario subestimad pregunta del
visible del fraude que alteró o. El análisis electoral:
ignorando al las actas o el diseñador ¿quién diseñó el
diseñador del que intimidó del esquema? ¿El
esquema a los esquema ejecutor actuó
votantes es evade la bajo instrucciones
el actor más responsabil (S alto) o tomó la
visible del idad iniciativa de
proceso. El mientras el manera
analista le ejecutor idiosincrática (S
atribuye el visible bajo)?
100% del R* asume el
sin analizar R*
quién diseñó completo
el esquema. — la
inversión
causal
clásica.
Usar alegaciones Las El análisis El análisis
de fraude (Hi8) alegaciones reproduce electoral debe
como base del de fraude las comenzar por el
análisis sin electoral son alegaciones nivel Hi2 — el
evidencia políticament del actor análisis estadístico
estadística o e frecuentes. afectado de los resultados
documental El analista sin — antes de usar
las usa como verificació los testimonios o
base del n. R* las alegaciones de
grafo sin asignado las partes. Sin Hi2
verificar con sin disponible,
análisis respaldo declarar
estadístico evidencial Declaración C con
Hi2 o adecuado. incertidumbre alta.
documentos
Hi1.
No incluir el El análisis D_electora El
D_sistémico_dem calcula el l D_sistémico_dem
ocrático en el D_sufragio subestimad ocrático debe
D_electoral y el o. El incluirse siempre
D_represent fraude que en el análisis
ación sin erosiona la electoral, aunque
considerar el confianza su cuantificación
daño a la en el tenga mayor

Taxonomía General de Aplicaciones
Por qué Consecue
Error Corrección
ocurre ncia
confianza proceso incertidumbre. La
institucional tiene erosión de la
en el sistema consecuen confianza en el
democrático cias de proceso es el D
. largo plazo más importante de
que los escándalos
superan el electorales de gran
D del escala.
episodio
específico.
Ignorar el S del El análisis R*_DSE El S del
sistema político al atribuye el sobreestim gerrymandering es
analizar el gerrymander ado. La el instrumento que
gerrymandering ing al reforma distingue la
como acto partido propuesta manipulación
individual específico se dirige a idiosincrática (S
que controló sustituir al bajo → reforma
el proceso partido individual posible)
de diseñador de la manipulación
redistribució en lugar de sistémica (S alto
n sin a cambiar → reforma de las
considerar las reglas reglas del sistema
que que hacen es el instrumento
cualquier racional el correcto).
otro partido gerrymand
en esa ering.
posición
habría
hecho lo
mismo.
§8 Guía de prioridades de recolección de
evidencia en ciencia política y procesos
electorales

Taxonomía General de Aplicaciones
La
Si tu evidencia Por qué Qué Qué buscar
incertidumbre que más funcion rango / qué
principal es... la reduce a reduce preguntar
es...
1. ¿Hay ILE Análisis El ILE Establec ¿Los
bajo — existe la estadístico bajo es la e el ILE resultados
brecha entre el Hi2 de los base de y el son
proceso resultados toda la R*_DS consistentes
declarado y el electorales responsa E con el
implementado? + bilidad (incertid contexto
informes del umbre electoral
de dominio. estructur previo y las
observado Sin al encuestas del
res establece central). período? ¿La
electorales rlo distribución
Hi2. Test primero, de los
de el análisis resultados
Benford no puede sigue los
sobre la distribuir patrones
distribuci el R* estadísticos
ón de los entre los esperados?
resultados actores. ¿Los
si el informes de
conjunto observadores
de datos identificaron
es irregularidad
suficiente es
mente documentad
grande. as?
2. ¿El diseño Test de El Establec ¿Las tasas de
produce los 4/5 en disparate e el registro y
disparate las tasas impact disparat participación
impact — hay de registro establece e impact del grupo
supresión del y la base y el tipo protegido
voto de un participaci del de son
grupo ón R*_DSE supresió inferiores al
protegido? electoral sobre la n 80% de las
desagrega supresió (idiosinc del grupo de
das por n del rática vs. referencia?
grupo + voto. Sin estructur ¿La
análisis de él, el al). diferencia
regresión análisis persiste
con no puede después de
variables distingui controlar por
de control r la baja las variables
participa socioeconóm

Taxonomía General de Aplicaciones
La
Si tu evidencia Por qué Qué Qué buscar
incertidumbre que más funcion rango / qué
principal es... la reduce a reduce preguntar
es...
socioecon ción por icas? ¿Las
ómicas. elección barreras
del afectan
votante desproporcio
de la baja nalmente al
participa grupo
ción por protegido?
barreras
estructur
ales.
3. ¿El Hijo del Análisis El Hijo Establec ¿Hay
actor electoral comparad determin e el S del alternativas
es Anteros o o del a el S y el actor y la técnicas al
Deimos — cuál diseño instrume distribuc diseño que
es el S del con el nto ión entre producen
diseño? estándar correcto reforma menor
del de individu disparate
sistema reforma al y impact y que
político (individu sistémic estaban
del al vs. a. disponibles
período + sistémica en el
document ). período? ¿El
os Anteros actor rechazó
internos → esas
del reforma alternativas
proceso individua sin
de diseño l posible justificación
si están y documentad
disponible necesaria a? ¿Las
s. . prácticas de
Potós/D actores
eimos → equivalentes
reforma del período
sistémica son similares
de las al diseño
reglas del analizado?
juego.
4. ¿La Análisis El R* de Establec ¿La
plataforma de la la e el definición de
digital tiene R* métrica platafor R*_PD «contenido
por sesgo del ma sobre sobre la seguro» o

Taxonomía General de Aplicaciones
La
Si tu evidencia Por qué Qué Qué buscar
incertidumbre que más funcion rango / qué
principal es... la reduce a reduce preguntar
es...
algorítmico algoritmo el sesgo supresió «contenido
político — cuál de la político n relevante» de
fue la métrica? plataform es algorítm la plataforma
a: ¿cuál era proporci ica del era neutral
la onal al discurso respecto al
definición diseño político. contenido
de de la político? ¿El
«contenid métrica, análisis del
o no al disparate
relevante» modelo impact sobre
o técnico. el alcance del
«contenid El contenido
o seguro» modelo electoral de
aplicada al es S ≈ distintos
discurso 1.0 grupos está
político? (cualquie documentad
¿Esa r modelo o?
definición con la
producía misma
disparate métrica y
impact el mismo
sobre el dataset
discurso habría
de ciertos producid
grupos? o el
mismo
sesgo).
5. ¿Cuál es el Encuestas El Establec ¿Las
D_sistémico_d de D_sisté e la encuestas de
emocrático — confianza mico escala confianza
la confianza en institucion puede del institucional
el proceso fue al del dominar D_sisté cayeron
erosionada? período el mico y el después del
anterior y D_electo AD total escándalo?
posterior ral total del ¿La
al en los DSE. participación
escándalo. escándal electoral en la
Datos de os de siguiente
participaci gran elección fue
ón escala. inferior a la
electoral Sin él, el esperada?
del AD del ¿Los datos de

Taxonomía General de Aplicaciones
La
Si tu evidencia Por qué Qué Qué buscar
incertidumbre que más funcion rango / qué
principal es... la reduce a reduce preguntar
es...
período DSE es confianza en
posterior. menor el proceso
Análisis del que le electoral del
comparad correspo período
o del nde. posterior son
impacto comparables
de con los de
escándalo jurisdiccione
s s sin
electorales escándalo?
similares.
Árbol de decisión en ciencia política y procesos electorales
¿El caso es de fraude directo, manipulación informativa o
supresión estructural del voto?
│
├─ ANÁLISIS A: FRAUDE ELECTORAL DIRECTO
│ └─ PRIORIDAD 1: Análisis estadístico Hi2
+ documentos Hi1 → ILE bajo documentado
│ · Anomalía en la distribución de los
resultados → ILE positivo → R*_DSE dominante.
│ └─ PRIORIDAD 2: ¿El ejecutor actuó bajo
instrucciones (S alto) o por iniciativa (S bajo)?
│ · S alto del ejecutor → R* migra al DSE.
Fraude annona electoral.
│ └─ PRIORIDAD 3: D_electoral =
D_sufragio + D_representación + D_sistémico
├─ ANÁLISIS B: MANIPULACIÓN INFORMATIVA
│ └─ PRIORIDAD 1: ¿Cuál fue la métrica del
sistema de segmentación o desinformación?
│ · Métrica idiosincrática (S bajo) →
R*_diseñador dominante. Cap. 13 para el análisis.

Taxonomía General de Aplicaciones
│ └─ PRIORIDAD 2: ¿La plataforma cedió
datos sin consentimiento informado?
│ · Cesión de datos con Potós →
R*_plataforma moderado.
│ └─ PRIORIDAD 3: D_electoral =
diferencial de preferencias atribuible a la
desinformación (Hi5/C)
└─ ANÁLISIS C: SUPRESIÓN ESTRUCTURAL DEL
VOTO
└─ PRIORIDAD 1: Test de los 4/5 en las
tasas de participación del grupo protegido
· Tasa_grupo / Tasa_referencia < 0.80 →
disparate impact prima facie.
└─ PRIORIDAD 2: ¿El diseño fue
idiosincrático (Anteros, S bajo) o el estándar del
período (Potós, S alto)?
· S alto → reforma de las reglas del sistema. S
bajo → reforma del actor y del diseño.
└─ PRIORIDAD 3: D_electoral =
D_sufragio_suprimido +
D_representación_distorsionada
└─ Paso 2: ¿El D_sistémico_democrático es significativo —
la confianza fue erosionada?
├─ SÍ → D_total incluye D_sistémico → AD_DSE
aumenta significativamente
│ └─ AD_DSE = R*_DSE × (D_sufragio +
D_representación + D_sistémico) × (1 −
α_DSE).
└─ NO (fraude local sin impacto en la confianza general)
→ D_total = D_directo
└─ AD_DSE = R*_DSE × D_directo × (1 −
α_DSE).
— Fin del Capítulo 44 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

