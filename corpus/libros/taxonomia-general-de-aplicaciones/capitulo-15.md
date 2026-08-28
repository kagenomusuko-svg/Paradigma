## PARTE II · Ciencias Económicas y Financieras

### Capítulo 15
Seguros —
fraude, responsabilidad y valoración de
siniestros
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo tiene dos singularidades estructurales respecto a todos los
anteriores. Primera: los Hijos de Afrodita no aplican a ningún nodo del
dominio asegurador — el análisis es de sistemas e instrumentos, no de
disposiciones individuales de voluntad. Segunda: aparece el Δ_B (déficit de
asunción del beneficio del siniestro) como concepto central que no había sido
necesario en los dominios anteriores con la misma precisión: describe tanto al
asegurado que obtuvo más del siniestro de lo que tenía derecho (fraude al
seguro) como a la aseguradora cuyo diseño de póliza contribuyó causalmente al
siniestro que compensó (aseguradora predatoria). Si tu prioridad es el análisis
de fraude al seguro, lee §4 y §5. Para la valoración de siniestros y la
distribución proporcional de la indemnización, ve a §7. Para la prima justa
ajustada por causalidad, ve a §4.3. Para la prioridad de evidencia, ve
directamente a §9.
§1 Descripción del subcampo
El seguro es el dominio donde el sistema de imputación causal
introduce dos conceptos que los capítulos anteriores no
habían necesitado con esta precisión. El primero es la
distinción entre el seguro como distribución del riesgo (el

Taxonomía General de Aplicaciones
siniestro es causalmente independiente del contrato: la
aseguradora no causó el daño, solo lo redistribuyó entre los
asegurados; R*_aseguradora ≈ 0) y el seguro como creación o
amplificación de riesgo (el diseño de la póliza modifica los
incentivos del asegurado de manera que aumenta la
probabilidad del siniestro; R*_aseguradora > 0). El segundo
es el Δ_B: la brecha entre el beneficio que un nodo obtuvo del
siniestro y lo que asumió de ese beneficio.
La distinción entre ambos tipos de seguro no es nominal: tiene
consecuencias sobre la prima justa, sobre la distribución de la
indemnización y sobre la responsabilidad de la aseguradora
ante el regulador. Cuando el diseño de la póliza incluye
sobrecobertura (la suma asegurada supera el valor real del
activo), incentiva al asegurado a invertir menos en prevención
— porque el costo marginal del siniestro para él es negativo.
En ese caso, la aseguradora no es solo el compensador del
daño: es un nodo con posición causal en el evento que
compensa.
Dos funciones ontológicas del seguro: distribución del riesgo
versus creación de riesgo
Seguro como distribución del riesgo: el siniestro existía como posibilidad antes
de la póliza. La aseguradora lo redistribuye entre los asegurados.
R*_aseguradora ≈ 0 en el siniestro. La prima justa es proporcional al riesgo
actuarialmente documentado.
Seguro como creación (o amplificación) de riesgo: el diseño de la póliza
modifica los incentivos del asegurado de manera que aumenta P(siniestro).
R*_aseguradora > 0. La prima no puede ser completamente justa en el
sentido actuarial porque el contrato mismo contribuye al riesgo que cubre. La
aseguradora tiene posición causal en el evento que compensa.
Analogía del salvavidas que cobra por rescate: si el salvavidas cobra más por
cada rescate que por prevenir el ahogamiento, tiene un incentivo estructural
para que haya más ahogamientos. Eso no significa que cause los ahogamientos
deliberadamente — significa que el diseño de su sistema de compensación tiene
posición causal en la probabilidad del evento que cubre. La aseguradora que
diseña una póliza con sobrecobertura tiene la misma posición: su diseño no
causa el incendio, pero crea el incentivo que hace el incendio más probable.

Taxonomía General de Aplicaciones
Sub-variantes del dominio
Valoración y ajuste de siniestros: distribución de la
indemnización entre los nodos del grafo causal del siniestro.
El ajustador de siniestros convencional calcula el daño. El
análisis causal establece además quién contribuyó causalmente
al siniestro y en qué proporción — lo que determina si la
indemnización íntegra procede o si debe reducirse en
proporción al R* del asegurado.
Fraude al seguro (Δ_B positivo del asegurado): el asegurado
obtuvo más del siniestro de lo que tenía derecho según su
posición causal y el valor real del activo. El Δ_B positivo del
asegurado es la señal formal del fraude: la diferencia entre la
indemnización recibida y el daño causalmente atribuible al
asegurado. Puede ocurrir por sobrecobertura (suma asegurada
superior al valor real), por exageración del daño (T_invertido
declarado superior al real) o por provocación del siniestro
(R*_asegurado alto con B_siniestro positivo).
Diseño predatorio de póliza (Δ_B positivo de la aseguradora):
la aseguradora diseñó el producto con características que
incentivan el siniestro — sobrecobertura sin verificación,
suscripción sin revisión adecuada, empresa como beneficiaria
sin auditoría — y obtuvo beneficio neto del diseño (primas
infladas más margen del diseño permisivo) sin asumir su
posición causal. El Δ_B de la aseguradora es la medida de ese
beneficio no asumido. No es necesariamente fraude penal,
pero sí es la descripción matemática de cómo el diseño del
producto extrajo valor a costa de las víctimas del siniestro.
Responsabilidad del diseñador del entorno de riesgo: el
propietario de un inmueble, el operador de una instalación
industrial o el empleador que diseñó las condiciones físicas
bajo las que ocurrió el siniestro. El grafo incluye a ese actor
como nodo de diseño del entorno con R* positivo, al
regulador que estableció (o no estableció) los estándares de
seguridad y a la aseguradora cuya póliza pudo haber
modificado los incentivos de prevención.

Taxonomía General de Aplicaciones
Prima justa ajustada por causalidad: la aplicación del principio
R* × (1−S) al diseño de primas. La prima actuarialmente justa
convencional refleja el riesgo de la clase. La prima ajustada por
causalidad refleja la contribución causal idiosincrática del
asegurado al riesgo: excluye la fracción del riesgo que es
estructural (S alto: cualquier asegurado en ese entorno habría
tenido el mismo siniestro) y carga solo la fracción que es
genuinamente del asegurado (S bajo, R*_asegurado × (1−S)).
Siniestros de causación múltiple acumulativa: incendios,
accidentes industriales, fenómenos climáticos extremos donde
múltiples factores contribuyen al daño sin que ninguno sea
condición necesaria y suficiente por sí solo. Cuando la
condición de la iteración de potencia no se cumple, el análisis
de valores de Shapley es el instrumento correcto para distribuir
R* entre los factores causales.
§2 Escala de evidencia S0–S8 · Dominio de
seguros
La escala S0–S8 traduce la jerarquía general E0–E8 al
vocabulario del dominio asegurador. Su característica más
relevante es la combinación del peritaje técnico del siniestro
(S2 — la cadena causal física del evento) con el análisis
actuarial del diseño de la póliza (S2 — la relación entre el
diseño y el incentivo al riesgo moral). Sin ambos, la
distribución del R* entre el asegurado, el diseñador del
entorno y la aseguradora permanece en S5/S6. Nivel A —
rangos derivados por extensión desde los principios del
sistema.
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio
evidencia w
asegurador
S1 Documento Reporte de siniestro con la [0.74,
directo del descripción del evento; 0.92]
siniestro, la póliza póliza con los términos de
cobertura, la suma

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio
evidencia w
asegurador
y el entorno de asegurada y las exclusiones;
riesgo certificación del valor del
activo en el momento de la
póliza; inspecciones de
seguridad del inmueble o
instalación antes del
siniestro; comunicaciones
entre el asegurado y la
aseguradora sobre la
valoración del activo;
registros de mantenimiento
del activo asegurado.
S2 Peritaje técnico Peritaje técnico que [0.65,
del siniestro y establece las causas físicas 0.85]
análisis actuarial del siniestro y la
del diseño de la contribución de cada factor
póliza (falla estructural, ausencia
de sistemas de supresión,
materiales inflamables) con
sus respectivos pesos
causales; análisis actuarial
que establece si la suma
asegurada correspondía al
valor real del activo y si el
diseño de la póliza generaba
incentivos al riesgo moral;
análisis del Δ_B de la
aseguradora mediante la
comparación de las primas
recaudadas, los siniestros
pagados y el efecto del
diseño sobre la
siniestralidad de la cartera.
S3 Testimonios Declaraciones de múltiples [0.48,
convergentes de testigos del evento 0.66]
testigos del (bomberos, inspectores de
siniestro con seguridad, vecinos) que
corroboración describen consistentemente
documental las condiciones en el
momento del siniestro, con
al menos un registro
técnico consistente. En
casos de fraude al seguro:

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio
evidencia w
asegurador
testimonios de
colaboradores que
describen cómo el
asegurado contribuyó al
siniestro o cómo exageró el
daño.
S4 Análisis Análisis que muestra que la [0.38,
estadístico del tasa de siniestralidad de la 0.60]
comportamiento cartera es estadísticamente
de la cartera incompatible con el riesgo
aseguradora actuarial de la clase de
activos asegurados;
comparación de la
siniestralidad de la cartera
con la de carteras
comparables del sector;
análisis del Δ_B de la
aseguradora mediante la
comparación de la
siniestralidad esperada
versus observada
controlando por las
características del diseño de
la póliza.
S5 Análisis del diseño Comparación del diseño de [0.28,
de la póliza y de la póliza con los estándares 0.48]
las condiciones del sector para ese tipo de
del entorno de activo y riesgo; análisis de
riesgo las condiciones físicas del
entorno de riesgo
(materiales, sistemas de
seguridad, protocolos)
versus los estándares
aplicables; evaluación del
historial de siniestros del
asegurado en el período
anterior a la póliza.
S6 Inferencia El asegurado, el diseñador [0.18,
estructural por del entorno o la 0.38]
posición del actor aseguradora tenía la
en el sistema de posición, la información y
riesgo el control para haber

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio
evidencia w
asegurador
modificado los factores
causales del siniestro, sin
documentación directa de
la decisión específica.
S7 Correlación El deterioro documentado [0.07,
temporal entre del activo o las decisiones 0.24]
condiciones del del asegurado coinciden
activo y siniestro temporalmente con el
sin análisis causal siniestro sin análisis técnico
que establezca la cadena
causal.
S8 Fuente única sin Un solo testimonio o [0.04,
corroboración documento sobre el 0.16]
técnica siniestro sin respaldo en
peritaje técnico ni análisis
actuarial.
S0 Ausencia Peritaje técnico que w =
documentada de establece que el siniestro 0.00
conexión causal fue producido
exclusivamente por un
factor exógeno
imprevisible (fuerza mayor)
sin ninguna contribución
causal de los actores del
grafo, o que la conducta del
asegurado no tenía posición
causal en el siniestro.
La diferencia entre la actuaría predictiva y el análisis causal
atributivo
La actuaría convencional calcula probabilidades: dada una clase de riesgo y
una historia de siniestros, ¿cuál es la probabilidad de que el siniestro ocurra?
Esa probabilidad determina la prima. El análisis causal añade una capa
diferente: dado que el siniestro ocurrió, ¿cuánto dependía causalmente de cada
factor? La diferencia entre ambas es la diferencia entre predicción (antes del
siniestro) y atribución (después del siniestro). La actuaría dice "este tipo de
activo tiene P(siniestro) = 2.3% anual". El análisis causal dice "en este
siniestro específico, el R* del propietario era 45% y el del regulador era 30%".
Ambas preguntas son necesarias y se complementan.

Taxonomía General de Aplicaciones
§3 Los Hijos de Afrodita no aplican en el
dominio asegurador
El dominio de seguros tiene una singularidad estructural que
lo distingue de todos los capítulos anteriores de la Parte I y de
los capítulos 11-14 de la Parte II: los Hijos de Afrodita no
aplican a ningún nodo del análisis. La razón es que los nodos
del grafo del siniestro son sistemas, estructuras físicas,
contratos e instrumentos — no personas con disposiciones de
voluntad en el momento del acto relevante.
Los propietarios del edificio tienen R* alto en el siniestro por
las condiciones físicas que diseñaron y mantuvieron — puertas
cerradas, ausencia de sistemas de supresión, materiales
inflamables acumulados — pero la disposición de voluntad
con la que tomaron esas decisiones es irrelevante para el
cálculo de R*. Lo que importa es si esas decisiones eran
condición causal del siniestro, no si fueron tomadas con
Anteros, Potós o Deimos.
Cuándo sí aplica el análisis de Hijos en casos relacionados con
seguros
El análisis de Hijos aplica en los dominios que se superponen con el
asegurador cuando hay responsabilidad individual del diseñador del producto
de seguros como directivo de la aseguradora (remitir al cap. 13 — gobierno
corporativo), responsabilidad penal del asegurado por fraude deliberado al
seguro (remitir al cap. 1 — derecho penal), o responsabilidad del inspector de
seguridad que no reportó deficiencias (remitir al cap. 8 — responsabilidad
médica por analogía de la omisión del perito). En todos esos casos, el análisis
de Hijos del dominio correspondiente se aplica al actor individual, y el análisis
causal del dominio de seguros distribuye el R* entre los nodos del siniestro.
S en el dominio asegurador: fungibilidad del factor de
riesgo

Taxonomía General de Aplicaciones
Aunque los Hijos no aplican, S sí aplica con su significado
habitual: mide cuánto del riesgo era idiosincrático del
asegurado versus estructural del entorno.
Perfil de S Consecuencia sobre la
del Interpretación prima y la
asegurado indemnización
S alto del Cualquier persona en las La prima diferenciada
asegurado mismas condiciones por comportamiento
(≥ 0.60) estructurales (mismo individual tiene poco
entorno físico, mismo fundamento causal. La
sector industrial, misma indemnización íntegra es
zona geográfica) habría justa porque el asegurado
tenido el mismo siniestro. no fue condición
El riesgo es de la clase o necesaria idiosincrática
del entorno, no de la del siniestro. No hay base
persona. La conducta para reducción de la
individual del asegurado indemnización por
tuvo poco poder causal conducta del asegurado.
sobre el resultado.
S bajo del Las condiciones y La prima diferenciada
asegurado decisiones específicas del por comportamiento
(< 0.35) asegurado (su observable tiene
comportamiento, sus fundamento causal. La
decisiones de indemnización puede
mantenimiento, su reducirse en proporción
gestión del riesgo al R*_asegurado ×
operativo) fueron (1−S). Base para
causalmente cláusulas de franquicia
determinantes para el proporcional al
siniestro. Otro asegurado comportamiento.
en la misma clase de
riesgo no habría tenido el
mismo resultado.
S alto del Cualquier póliza de ese La reforma regulatoria
diseño de la tipo (sobrecobertura, debe actuar sobre la clase
póliza (≥ empresa como de producto, no solo
0.60) beneficiaria, suscripción sobre la aseguradora
sin revisión médica) específica. La multa
habría creado el mismo mínima disuasoria se
incentivo al riesgo moral. calcula sobre el Δ_B de la
El problema es de la clase clase, no del caso
de producto, no del individual.
diseñador específico.

Taxonomía General de Aplicaciones
Perfil de S Consecuencia sobre la
del Interpretación prima y la
asegurado indemnización
S bajo del El diseño específico de El R*_aseguradora es
diseño de la esta póliza tenía alto. La multa mínima
póliza (< características disuasoria se calcula
0.35) idiosincráticas que otros sobre el Δ_B de la póliza
productos del mismo específica.
sector no tienen. La
sobrecobertura o los
incentivos perversos
fueron diseñados de
manera particular.
§4 ¿Qué cuenta como asunción (α) en el
dominio asegurador?
α en el dominio asegurador tiene interpretaciones distintas
según el nodo, con una característica que no se da en otros
dominios: el pago de la indemnización contractual por la
aseguradora es α de la obligación contractual, no α de la
responsabilidad causal. Cuando el diseño de la póliza
contribuyó causalmente al siniestro, la aseguradora que solo
paga la indemnización sin reconocer su posición causal tiene
α de obligación contractual ≈ 1 pero α de responsabilidad
causal ≈ 0.
α en el
Conducta que
Nodo dominio Tipo de α
sube α
asegurador
Asegurado Grado de Instalar sistemas Voluntario
implementació de supresión de antes del
n de medidas incendios. siniestro /
preventivas Mantener el Obligación
proporcionales activo en contractual
a su condiciones después
R*_asegurado óptimas. Seguir
× (1−S). α = 0: los protocolos
ninguna de seguridad.
medida Reportar

Taxonomía General de Aplicaciones
α en el
Conducta que
Nodo dominio Tipo de α
sube α
asegurador
preventiva. α = honestamente el
1: todas las siniestro sin
medidas exagerar el daño.
posibles
implementadas
dado el R*.
Diseñador del Grado de Mantener Voluntario
entorno implementació salidas de /
n de emergencia Regulatorio
condiciones de despejadas y
seguridad accesibles.
proporcionales Realizar el
al R* del mantenimiento
entorno en el de los sistemas
riesgo del de seguridad.
sector. Capacitar al
personal.
Reportar
deficiencias al
regulador.
Regulador Grado de Establecer Instituciona
implementació estándares l
n y aplicación mínimos
efectiva de adecuados al
estándares de riesgo. Realizar
seguridad inspecciones
proporcionales efectivas con
al riesgo del consecuencias.
sector. Sancionar
incumplimiento
s. Revisar el
marco
normativo ante
evidencia de
siniestralidad
sistémica.
Aseguradora Pago de la Es α de la Contractual
— obligación indemnización obligación
contractual establecida en contractual, no
la póliza. α de la
responsabilidad
causal. La

Taxonomía General de Aplicaciones
α en el
Conducta que
Nodo dominio Tipo de α
sube α
asegurador
aseguradora que
solo paga la
póliza cumple su
contrato pero
no asume su
posición causal
en el siniestro
cuando el diseño
contribuyó
causalmente.
Aseguradora Reconocimient Rediseño de la Voluntario
— o de que el suma asegurada o requerido
responsabilida diseño de la vinculada al
d causal póliza valor verificado
contribuyó al del activo.
siniestro y Implementación
reforma del de franquicias
diseño para proporcionales
eliminar el al
incentivo al R*_asegurado.
riesgo moral. Auditoría de
condiciones de
seguridad antes
de emitir la
póliza. Reforma
del sistema de
suscripción para
los activos de
alto riesgo.
§4.3 La prima justa ajustada por causalidad
PAC_i = P(siniestro) × E[D_total] × R*_asegurado_i × (1 − S_i)
+ Carga_administración
La prima actuarial convencional es Prima_conv = P(siniestro) ×
E[D_total] + Carga. Trata a todos los asegurados de la misma clase de
riesgo por igual, independientemente de su contribución causal idiosincrática
al riesgo.
La prima ajustada por causalidad (PAC) descompone el riesgo:
R*_asegurado_i × (1−S_i) es la contribución causal idiosincrática del

Taxonomía General de Aplicaciones
asegurado i. Si S = 0.80, el 80% del riesgo es estructural y el 20% es
idiosincrático. La prima justa refleja solo el 20%. Cuando el riesgo es
principalmente estructural (zona sísmica, sector industrial con condiciones de
trabajo peligrosas por deficiencias regulatorias), cobrar una prima alta al
asegurado equivale a imputarle la responsabilidad causal del entorno que no
creó.
Principio actuarial: el riesgo actuarialmente justo es R*_asegurado × (1−S)
× D_esperado. La prima que excede ese umbral es una transferencia del
costo del riesgo estructural al asegurado individual. Cuando esa transferencia
es sistemática para grupos históricamente excluidos de servicios o inversión
pública, hay fraude annona en el sistema de seguros: el asegurado paga por el
riesgo que no creó.
§4.4 El Δ_B: el beneficio del siniestro no asumido
Δ_B_asegurado y Δ_B_aseguradora: las dos formas del déficit de
beneficio
Δ_B_asegurado = B_siniestro_asegurado − α_asunción_causal.
Δ_B_asegurado positivo alto: el asegurado obtuvo más del siniestro de lo que
tenía derecho según su R* de contribución causal. Es la señal del fraude al
seguro. La diferencia entre la indemnización y el daño causalmente atribuible
al asegurado es el monto del enriquecimiento sin causa.
Δ_B_aseguradora = B_primas_total + B_diseño_incentivo −
α_reconocimiento_R*. Δ_B_aseguradora positivo alto: la aseguradora
obtuvo beneficio neto del diseño que incentivó el siniestro. No lo asumió. No
es necesariamente fraude en el sentido penal, pero es la descripción matemática
de cómo el diseño del producto extrajo valor a costa de las víctimas del
siniestro. La multa regulatoria proporcional debe ser al menos
Δ_B_aseguradora / P(detección) para que el sistema de incentivos rompa el
diseño predatorio.
La escala de α en el dominio asegurador

Taxonomía General de Aplicaciones
Indicadores
Rango Descripción
Nivel en el
α observable
expediente
Sin medidas 0.00 – El nodo no Sin sistemas de
preventivas / 0.05 implementó seguridad
obstrucción del ninguna medida instalados. Sin
ajuste preventiva mantenimiento
proporcional a su documentado.
R*, obstruyó el Daño declarado
proceso de ajuste excede el daño
del siniestro o real
exageró el daño documentado
declarado. por el peritaje.
Medidas 0.06 – El nodo Sistemas de
mínimas sin 0.20 implementó seguridad
proporcionalidad algunas medidas básicos
al R* de seguridad instalados. Sin
estándar de la mantenimiento
clase, sin acción actualizado.
específica Declaración
proporcional a su honesta del
R* individual en el daño sin
riesgo. acciones
preventivas
adicionales.
Medidas 0.21 – El nodo Sistemas de
parciales 0.45 implementó seguridad
proporcionales al medidas mejorados
R* preventivas que documentados.
redujeron Suma asegurada
significativamente revisada
su R* pero no lo parcialmente.
eliminaron. La Franquicia
aseguradora implementada
rediseñó pero no
parcialmente el proporcional al
producto R*.
predatorio.
Asunción activa 0.46 – El nodo está en Plan de mejoras
en proceso 0.70 proceso activo de de seguridad
implementación documentado
de medidas en ejecución.
proporcionales a Rediseño del
su R* con producto en
curso.

Taxonomía General de Aplicaciones
Indicadores
Rango Descripción
Nivel en el
α observable
expediente
seguimiento Cooperación
verificable. activa con el
regulador.
Asunción 0.71 – Las medidas Sistemas de
funcional 0.89 implementadas seguridad
son proporcionales
proporcionales a al riesgo del
la mayor parte del sector
R* del nodo. El Δ instalados y
residual es verificados.
pequeño. Suma asegurada
vinculada al
valor
verificado.
Siniestralidad
de la cartera
normalizada.
Asunción plena 0.90 – El nodo Auditoría de
1.00 implementó todas seguridad
las medidas aprobada.
proporcionales a Diseño de
su R*, eliminó el póliza
incentivo al riesgo reformado con
moral (en el caso Δ_B ≈ 0.
de la aseguradora) Cooperación
y cooperó plena
plenamente con el documentada.
regulador.
§5 Construcción del grafo típico del dominio
asegurador
Tipos de nodo en el grafo del siniestro

Taxonomía General de Aplicaciones
Función en el Ejemplo en el
Tipo S típico
grafo dominio
Diseñador El actor que Variable Los propietarios
del entorno diseñó y mantuvo [0.15–0.70] de la Triangle
de riesgo las condiciones Shirtwaist
(DE) físicas bajo las Factory que
que ocurrió el cerraron las
siniestro: el puertas de
propietario del emergencia con
inmueble, el llave y no
operador de la instalaron
instalación sistemas de
industrial, el supresión. El
empleador. Es el operador de la
nodo de mayor plataforma
R* en la mayoría petrolera que no
de los siniestros implementó los
laborales e protocolos de
industriales seguridad
cuando las requeridos. El
condiciones del propietario del
entorno eran la edificio con
causa dominante. instalaciones
eléctricas
deficientes no
mantenidas.
Asegurado El titular de la Variable El propietario
(A) póliza cuya [0.15–0.80] del vehículo
conducta o cuyas cuya conducta
decisiones de produjo el
mantenimiento y accidente. El
gestión del activo empresario
tienen posición cuyas decisiones
causal en el de gestión del
siniestro. En riesgo operativo
muchos contribuyeron al
siniestros, el siniestro
asegurado y el industrial. El
diseñador del asegurado que
entorno son el no realizó el
mismo actor. En mantenimiento
seguros de preventivo
responsabilidad, requerido.
el asegurado
causó daño a
terceros.

Taxonomía General de Aplicaciones
Función en el Ejemplo en el
Tipo S típico
grafo dominio
Regulador La autoridad Moderado- El regulador de
omisivo regulatoria que alto [0.45– edificios que no
(Reg) estableció 0.80] exigía salidas de
estándares de emergencia
seguridad accesibles en
insuficientes para edificios de
el sector o que no cierta altura. El
los hizo cumplir. regulador de la
R* positivo industria
cuando el marco química que no
normativo inspeccionó las
inadecuado fue instalaciones. El
condición regulador del
necesaria del sector financiero
siniestro a esa que no exigió
escala. due diligence de
valoración en los
productos de
seguro.
Aseguradora La entidad que Moderado La aseguradora
(As) diseñó la póliza. [0.30–0.65] que diseñó la
R* positivo para el póliza con
cuando el diseño diseño sobrecobertura
de la póliza predatorio sin verificación
modificó los específico del valor real del
incentivos del / Alto para activo. La
asegurado de la clase de aseguradora que
manera que producto emitió seguros
aumentó de vida
P(siniestro). colectivos de
Nodo causal sin empleados clave
el rol activo del sin revisión
diseñador del médica en el
entorno, pero rango de sumas
con posición relevantes.
estructural en el
incentivo al
riesgo moral.
Factor Los factores Muy alto El terremoto
ambiental físicos del [0.80–0.99] que derrumbó el
(FA) entorno que edificio. El rayo
contribuyeron al que inició el
siniestro sin ser incendio en el
controlables por bosque. La

Taxonomía General de Aplicaciones
Función en el Ejemplo en el
Tipo S típico
grafo dominio
ningún actor: tormenta que
condiciones hundió el barco.
climáticas El
extremas, envejecimiento
actividad sísmica, natural del
degradación cableado que
natural de produjo el
materiales. S muy cortocircuito.
alto. R* bajo
porque cualquier
actor en ese
entorno habría
tenido el mismo
siniestro.
Configuraciones canónicas del grafo asegurador
Configuración 1 — Siniestro con diseñador del entorno de alto R*
(Triangle Shirtwaist)
DE (propietarios, condiciones idiosincráticas del entorno: R* ~45%, S
~0.22) + Reg (marco normativo inadecuado: R* ~30%, S ~0.65) + As
(sobrecobertura, incentivo al riesgo moral: R* ~12%) + FA (materiales
inflamables: R* ~4%) → Siniestro → Nf (146 víctimas)
AD_DE = 0.45 × D_total = $317M USD (2024). Los propietarios
pagaron efectivamente < $20,000 USD. Δ_N1 = +0.45 en toda su
magnitud. J_Triangle ≈ 0.12: injusticia estructural severa. La lección del
caso: el análisis causal no necesita el dolo para establecer el R* del propietario.
Sus decisiones de diseño del entorno eran condición necesaria del colapso a esa
escala, independientemente de si sabían o no que las puertas estaban cerradas
en ese momento.
Configuración 2 — Diseño predatorio de póliza (Δ_B de la
aseguradora)
As (diseño: suma asegurada inflada + empresa como beneficiaria +
suscripción sin revisión médica: R* ~42%, S ~0.30) + A (empresas
aseguradas que aprovecharon el diseño: R* ~30%) + Reg (omisión

Taxonomía General de Aplicaciones
regulatoria: R* ~18%) → Siniestralidad anómala → Nf (sistema de
seguros y asegurados de la cartera)
Δ_B_aseguradora = B_primas_infladas + B_margen_diseño_permisivo
− α_reconocimiento. Multa_mínima_disuasoria ≥ Δ_B / P(detección). Si
P(detección) = 0.30, la multa mínima disuasoria es ~3.3 × Δ_B —
suficientemente alta para que el valor esperado del diseño predatorio sea
negativo. Cuando la multa regulatoria < Δ_B / P(detección), la aseguradora
tiene incentivo racional para seguir diseñando productos predatorios.
Configuración 3 — Fraude al seguro por el asegurado (Δ_B
positivo del asegurado)
A (asegurado que provocó o exageró el siniestro: R* alto, S bajo) → Siniestro
declarado con B_siniestro > D_real → Indemnización recibida > Daño
causalmente atribuible al asegurado → Δ_B_asegurado > 0
Señal del fraude: Δ_B_asegurado = Indemnización_recibida −
(R*_asegurado × D_total_real). Cuando la suma asegurada supera el valor
real del activo (sobrecobertura) y el asegurado tiene posición causal en el
siniestro (R* alto, S bajo), el Δ_B es la medida del enriquecimiento sin
causa. En fraudes por provocación deliberada del siniestro, Δ_B_asegurado
≈ B_siniestro_completo porque el asegurado diseñó el evento para cobrar la
póliza.
§6 Preguntas que responde este capítulo
Nivel de
Pregunta del Instrumento que la
certeza
caso responde
posible
¿Cuál es la Grafo causal del siniestro con Declaración B
distribución de los cuatro niveles (del si el peritaje
R* entre el asegurado, del entorno, del técnico S2 es de
asegurado, el diseño regulatorio, del diseño calidad y la
diseñador del de la póliza). Peritaje técnico suma asegurada
entorno, el S2 que establece las causas versus el valor
regulador y la físicas y sus contribuciones real del activo
aseguradora en el causales. Análisis actuarial S2 está
siniestro? del diseño de la póliza. documentada
S1. Declaración
C si algún nivel
del grafo

Taxonomía General de Aplicaciones
Nivel de
Pregunta del Instrumento que la
certeza
caso responde
posible
requiere
inferencia
estructural S6.
¿La suma Comparación S1/S2 de la Declaración A
asegurada excedía suma asegurada con el valor o B si hay
el valor real del real del activo en el momento tasación
activo — hay de la póliza: tasación independiente
sobrecobertura independiente del activo contemporánea
con incentivo al versus suma declarada en la a la póliza.
riesgo moral? solicitud. Si la diferencia Declaración C
supera el umbral de variación si la tasación
actuarialmente razonable, hay contrafáctica
sobrecobertura con del activo
R*_aseguradora positivo. requiere
estimación
retrospectiva.
¿Hay Comparación S1/S2 de la Declaración B
Δ_B_asegurado indemnización recibida (o si el peritaje
positivo — señal reclamada) con el daño técnico
de fraude al causalmente atribuible al establece el
seguro? asegurado: D_real × D_real con
R*_asegurado. Si la primera precisión y el
supera significativamente la R*_asegurado
segunda, hay Δ_B_asegurado está
positivo y señal de fraude. documentado.
Declaración C
si el D_real
requiere
estimación
retrospectiva
del valor del
activo.
¿Hay Análisis S4 del Declaración B
Δ_B_aseguradora comportamiento de la cartera: si hay datos de
positivo — la comparación de la la cartera
aseguradora siniestralidad observada disponibles
obtuvo beneficio versus la esperada sin el para comparar
del diseño que incentivo del diseño. Cálculo la siniestralidad
incentivó el de B_primas_infladas + observada
siniestro? B_margen_diseño_permisivo versus la
− α_reconocimiento. actuarialmente
esperada sin el

Taxonomía General de Aplicaciones
Nivel de
Pregunta del Instrumento que la
certeza
caso responde
posible
diseño.
Declaración C
si el efecto del
diseño sobre la
siniestralidad
debe inferirse
desde S4 sin
datos
completos de la
cartera.
¿Cuál es la prima PAC_i = P(siniestro) × Declaración B
justa ajustada por E[D_total] × R*_asegurado_i si el peritaje S2
causalidad para × (1−S_i). La estimación de establece los
este tipo de R*_asegurado_i y S_i componentes
activo? requiere el peritaje técnico S2 idiosincráticos
del perfil de riesgo y estructurales
idiosincrático del asegurado del riesgo.
versus el riesgo estructural del Declaración C
entorno. si la separación
R*_asegurado
/ R*_entorno
requiere
estimación
desde S4.
¿Cuántos Predictor de siniestros: Declaración B
siniestros t_detección = log (θ_ratio / si hay datos de
adicionales ratio_inicial) / log (1 + la cartera para
producirá el crecimiento_anomalía). Si estimar
diseño predatorio t_detección ≤ 0: el umbral ya P_diseño
antes de la fue superado — reporte versus
detección proactivo inmediato. Si P_actuarial.
regulatoria? t_detección > 0: Declaración C
N_adicionales = Cartera × si las tasas de
(P_diseño − P_actuarial) × siniestralidad
t_detección. requieren
extrapolación.
§7 Traducción de D_total al dominio
asegurador

Taxonomía General de Aplicaciones
El D_total del siniestro en el dominio asegurador tiene la
misma estructura tricomponente de todos los dominios, pero
con una característica que lo distingue: la póliza define la
cobertura — qué componentes del D_total la aseguradora se
comprometió a cubrir. La distribución de la indemnización
justa entre los nodos del grafo es proporcional a su R*, no a la
cobertura contractual de la póliza.
En el Cobertura
Notas para el
Componente dominio habitual de
análisis causal
asegurador la póliza
T_invertido El valor del Cubierto El valor del
(pérdida activo típicamente activo destruido
directa del destruido o en la debe estimarse al
siniestro) dañado (para mayoría de valor real en el
bienes las pólizas momento del
materiales), las de daños. siniestro, no al
lesiones Es el valor declarado
corporales component en la póliza si hay
directas (para e que la sobrecobertura.
seguros de póliza cubre El peritaje S2
personas), la de manera establece el
pérdida de más D_real versus la
ingresos completa. suma asegurada.
inmediata
documentada.
T_impedido Los ingresos Cubierto en Este
(interrupción perdidos pólizas de componente es
del negocio / durante el interrupción frecuentemente
recuperación) período de del negocio. subestimado en
reconstrucció No siempre la valoración
n o incluido en convencional del
recuperación, pólizas siniestro. Su
los costos de básicas de inclusión
instalaciones daños. completa en el
provisionales, D_total afecta
los contratos los AD_i de
perdidos todos los nodos
durante la con R* positivo.
interrupción,
los gastos de
recuperación
del estado

Taxonomía General de Aplicaciones
En el Cobertura
Notas para el
Componente dominio habitual de
análisis causal
asegurador la póliza
previo al
siniestro.
ΔT_trayectori Para siniestros Cubierto en Es el
a (pérdida con víctimas: seguros de componente más
permanente de la pérdida del vida y difícil de estimar
potencial) potencial de accidentes y el más
ingresos personales. frecuentemente
futuros, la Raramente excluido de las
discapacidad cubierto en indemnizaciones
permanente, la pólizas . D_vital =
reducción de básicas de ΔT_trayectoria /
la esperanza daños w_ref cuando
de vida. Para materiales. hay vidas
siniestros de afectadas. El
negocio: la caso Triangle
pérdida de produce D_vital
contratos, ≈ 88.2 millones
reputación y de horas para las
posición de 146 víctimas y
mercado que sus
no se dependientes.
recuperan
aunque el
activo sea
reconstruido.
La distribución de la indemnización justa entre los nodos del
grafo
Indemnización_justa_nodo_i = R*_i × D_total. La indemnización que la
aseguradora paga al asegurado no es Indemnización_justa_asegurado =
R*_asegurado × D_total (que podría ser menor al pago contractual si
R*_asegurado es bajo). Es la indemnización contractual — a menos que el
contrato tenga cláusulas de reducción por conducta del asegurado.
La distribución de AD_i entre los nodos del grafo establece la responsabilidad
de compensación de cada nodo en la cadena causal. En el caso Triangle:
AD_DE = 0.45 × $705M = $317M. La aseguradora pagó la póliza
íntegra ($445K en 1911 ≈ $13.8M de 2024) y cobró sus primas. Los
propietarios pagaron < $20,000 en indemnizaciones netas. La diferencia
entre el D_total calculado y lo que efectivamente asumió cada nodo es la

Taxonomía General de Aplicaciones
medida de la injusticia estructural del sistema de distribución de
responsabilidades: J_Triangle ≈ 0.12.
§8 Límites del método y errores frecuentes de
aplicación
Límites del método en el dominio asegurador
Límite 1 — Siniestros de causación múltiple acumulativa:
muchos siniestros tienen causas múltiples que contribuyen
simultáneamente sin que ninguna sea condición necesaria y
suficiente por sí sola. En esos casos, la condición de
irreductibilidad de la matriz W puede no cumplirse. El análisis
de valores de Shapley — desarrollado en la Parte IV de El
cálculo de la responsabilidad — ofrece la solución para los
siniestros de causación múltiple acumulativa.
Límite 2 — La causalidad contrafáctica en el seguro de vida: la
pregunta "¿habría muerto sin ese factor causal?" es
frecuentemente incontestable con certeza individual. La
actuaría maneja esta incertidumbre estadísticamente, pero el
análisis causal individual requiere un contrafáctico que a veces
no existe. El sistema recomienda trabajar con rangos de R* y
análisis de sensibilidad en lugar de valores puntuales.
Límite 3 — El riesgo de usar R* × (1−S) para discriminar
primas injustamente: si S no se estima correctamente y se usa
una S baja para cobrar prima alta a un asegurado cuyo riesgo
es principalmente estructural, se le imputa la responsabilidad
del entorno que no creó. El principio de prima justa ajustada
por causalidad protege contra ese error solo si la estimación de
S es precisa.
Límite 4 — El predictor de siniestros adicionales es una
estimación sobre una distribución de probabilidad, no una
certeza. Los parámetros del modelo (P_actuarial, P_diseño,
t_detección) tienen incertidumbre y deben presentarse con
análisis de sensibilidad explícito.

Taxonomía General de Aplicaciones
Errores frecuentes de aplicación
Por qué Consecuenci
Error Corrección
ocurre a
Confundir El analista Δ_B_asegura Distinguir
el pago de la trata el pago dora = 0 α_obligación_contr
indemnizaci de la póliza aunque la actual (pago de la
ón como α aseguradora póliza) de
contractual completo de obtuvo α_responsabilidad_
con la la beneficio causal
asunción de aseguradora neto del (reconocimiento del
la , ignorando diseño R* del diseño y
responsabili que cuando predatorio. El reforma del
dad causal el diseño de diseño producto). Son
de la la póliza predatorio componentes
aseguradora contribuyó permanece independientes.
al siniestro, sin análisis.
la
aseguradora
tiene una
responsabili
dad causal
adicional.
Atribuir el El ajustador Indemnizació AD_asegurado =
D_total del calcula el n R*_asegurado ×
siniestro al D_total y lo sobreestimad (1−S_asegurado) ×
asegurado usa a cuando D_total es el
como base directament R*_entorno o componente del
de la e como base R*_regulatori daño causalmente
indemnizaci de la o es alto. O atribuible al
ón sin indemnizaci infravalorada asegurado. Es la
estimar ón, sin cuando el base justa para la
R*_asegura establecer asegurado indemnización y
do cuánto del tiene R* bajo para las cláusulas de
siniestro era y S alto. reducción por
causalmente Decisión de conducta.
atribuible al cobertura
asegurado basada en el
versus al daño total, no
entorno o al en la
regulador. responsabilid
ad causal.

Taxonomía General de Aplicaciones
Por qué Consecuenci
Error Corrección
ocurre a
No incluir el El analista R* del El marco
regulador en construye el regulador = 0 regulatorio (o su
el grafo grafo con aunque el ausencia) tiene
cuando el solo el marco posición causal en el
marco asegurado, normativo siniestro cuando los
normativo el entorno inadecuado estándares que
fue físico y la fue condición habría requerido la
condición aseguradora necesaria del situación estaban
del siniestro , sin incluir siniestro a esa ausentes o no se
el marco escala. aplicaban. El
regulatorio regulador es un
insuficiente nodo del grafo con
como nodo R* positivo
causal. proporcional a esa
brecha.
Usar El analista Falso positivo El fraude al seguro
Δ_B_asegur detecta que de fraude requiere: (1)
ado como la cuando el Δ_B_asegurado
único indemnizaci siniestro era positivo
indicador de ón causalmente significativo; (2)
fraude sin reclamada independient R*_asegurado
verificar R* supera el e del significativo (el
y S valor real asegurado (S asegurado fue
del activo y alto) y la condición causal del
concluye sobrecobertu siniestro o lo
fraude sin ra no fue exageró); (3)
verificar si el determinante S_asegurado bajo
asegurado de la (la conducta era
era conducta del idiosincrática). Si S
condición asegurado. es alto, la
causal del sobrecobertura
siniestro. puede ser un error
actuarial, no fraude.
§9 Guía de prioridades de recolección de
evidencia
Si tu prioridad es saber qué buscar primero en un caso
asegurador, usa la tabla y el árbol que siguen. La primera
decisión siempre es identificar el análisis: valoración del
siniestro (distribución del D_total entre los nodos del grafo),

Taxonomía General de Aplicaciones
fraude del asegurado (Δ_B_asegurado positivo), o diseño
predatorio de la aseguradora (Δ_B_aseguradora positivo).
Cada análisis tiene prioridades de evidencia distintas.
Tabla de prioridades de recolección de evidencia
aseguradora
Si tu Qué
incertidu La evidencia Por qué Qué buscar /
mbre que más la funcion rango qué
principal reduce es… a reduce pregunta
es… r
1. ¿Cuál es Identificar el Cada Determin ¿La suma
el análisis eje del caso: análisis a el asegurada
principal ¿el D_total tiene instrume excede el
— está disputado instrume nto valor del
valoración o hay indicios ntos y principal activo?
, fraude de que fue evidenci y el orden ¿El
del exagerado as de asegurado
asegurado (fraude del prioritari recolecci tiene
o diseño asegurado)? as ón historial
predatori ¿La distintas. de
o? siniestralidad Confund siniestros
de la cartera es irlos anteriores
anómalamente produce ? ¿La
alta (diseño una siniestrali
predatorio)? recolecci dad de la
¿La ón cartera es
distribución ineficient comparati
del R* entre e. vamente
los nodos es la alta?
pregunta
principal
(valoración)?

### 2. Peritaje Sin el Reduce ¿Cuáles
[VALOR técnico S2 de peritaje rango de fueron las
ACIÓN] las causas técnico, R* de causas
¿Cuál es la físicas del los pesos cada físicas
distribuci siniestro: ¿qué del grafo nodo directas
ón del R* factores son (incertidu del
entre los fueron inferenci mbre siniestro?
condición as S6. empírica) ¿Cuál

Taxonomía General de Aplicaciones
Si tu Qué
incertidu La evidencia Por qué Qué buscar /
mbre que más la funcion rango qué
principal reduce es… a reduce pregunta
es… r
nodos del necesaria del Con él, habría
siniestro? evento?, alcanzan sido la
¿cuáles lo S2 y magnitud
amplificaron y permiten del
cuáles fueron Declarac siniestro
exógenos? El ión B. sin la
peritaje ausencia
establece los de
pesos w de las sistemas
aristas del de
grafo. supresión
? ¿El
marco
regulatori
o exigía
condicion
es que no
se
cumplían?

### 3. Tasación La Reduce ¿Hay
[FRAUD independiente sobrecob rango de tasación
E DEL del valor real ertura es Δ_B_aseg independi
ASEGUR del activo en el la urado ente
ADO] momento de condició (incertidu contempo
¿La suma la póliza, n mbre ránea a la
asegurada comparada necesaria empírica solicitud
correspon con la suma para el crítica) de la
de al valor asegurada Δ_B_ase póliza?
real del declarada. Si la gurado ¿Hubo
activo? diferencia es en ajuste de
significativa, fraudes la suma
hay por asegurada
sobrecobertur incendio inmediata
a y o mente
Δ_B_asegurad destrucci antes del
o potencial. ón de siniestro?
activos. ¿El valor
Sin del activo
establece asegurado
r el valor excede
real del significati
activo, el vamente

Taxonomía General de Aplicaciones
Si tu Qué
incertidu La evidencia Por qué Qué buscar /
mbre que más la funcion rango qué
principal reduce es… a reduce pregunta
es… r
análisis los valores
del comparab
fraude les del
no puede mercado?
avanzar.

### 4. Peritaje El Reduce ¿Hubo
[FRAUD técnico S2 de Δ_B_ase rango de fallos de
E DEL la gurado R*_asegu mantenim
ASEGUR contribución requiere rado y S iento o
ADO] ¿El del asegurado tanto (incertidu incumpli
asegurado al siniestro: sobrecob mbre mientos
tiene ¿las decisiones ertura empírica de
posición de como y protocolo
causal en mantenimient R*_aseg ontológic s de
el o, las urado a) seguridad
siniestro condiciones positivo. por parte
— R* de operación o Si el del
alto? las acciones asegurad asegurado
directas del o tenía S ? ¿Hay
asegurado alto historial
fueron (cualquie de
condición r conductas
causal del asegurad de riesgo
siniestro? o en ese anteriores
¿Otros entorno document
asegurados en habría adas?
la misma clase tenido el ¿Otros
de riesgo mismo activos de
habrían tenido siniestro) la misma
el mismo , la clase, en
siniestro? sobrecob condicion
ertura es es
un error similares,
actuarial han
pero no tenido
fraude. siniestros
similares?

### 5. Análisis Si la Reduce ¿Cuál es la
[DISEÑ estadístico S4 siniestral rango de tasa de
O de la tasa de idad es Δ_B_aseg siniestrali
PREDAT siniestralidad estadístic uradora dad de la

Taxonomía General de Aplicaciones
Si tu Qué
incertidu La evidencia Por qué Qué buscar /
mbre que más la funcion rango qué
principal reduce es… a reduce pregunta
es… r
ORIO] de la cartera amente (incertidu cartera
¿La comparada incompa mbre comparad
siniestrali con la de tible con empírica) a con la
dad de la carteras del el perfil del sector?
cartera mismo tipo en actuarial ¿Hay
excede la el sector, de la concentra
actuarialm controlando clase de ción de
ente por las activos, siniestros
esperada? características hay una en el
de los activos señal de segmento
asegurados. que el de mayor
diseño sobrecobe
del rtura? ¿El
producto diseño del
está producto
generand tiene
o característ
incentivo icas que lo
s al distinguen
siniestro de los
más allá estándares
de lo del sector?
actuarial
mente
esperado
.

### 6. Predictor de Cuando Establece ¿La tasa
¿Cuántos siniestros: el umbral la de
siniestros comparar ya fue urgencia siniestrali
adicionale ratio_siniestral superado del dad actual
s idad_actual vs , cada reporte y supera 1.5
producirá θ_detección_r siniestro la veces la
el diseño egulatoria. Si adicional estrategia actuarialm
predatori ratio ≥ θ → el aumenta óptima ente
o antes de umbral ya fue P(investi esperada?
la superado: gación) Si sí →
detección reporte de umbral
? proactivo manera superado.
inmediato. Si no lineal. Si no →
ratio < θ → El ¿cuándo
calcular reporte se estima
t_detección y proactiv

Taxonomía General de Aplicaciones
Si tu Qué
incertidu La evidencia Por qué Qué buscar /
mbre que más la funcion rango qué
principal reduce es… a reduce pregunta
es… r
N_adicionales o es la que lo
. estrategi superará?
a óptima
para
reducir el
Δ_B
acumula
do.
7. ¿Cuál es PAC_i = La prima Establece ¿Qué
la prima P(siniestro) × ajustada la justicia porcentaje
justa E[D_total] × por de la del riesgo
ajustada R*_asegurado causalida prima y el de la clase
por _i × (1−S_i). d refleja argument es
causalidad El peritaje S2 solo el o de estructural
para el establece riesgo equidad (cualquier
activo? R*_asegurado que el actuarial asegurado
_i y S_i. asegurad en ese
Comparar con o causó. entorno lo
la prima actual La tiene)
para diferenci versus
identificar si a entre la idiosincrát
hay prima ico
transferencia actual y (depende
injusta del la PAC de las
riesgo es la decisiones
estructural al fracción del
asegurado del asegurado
individual. riesgo específico
estructur )?
al
(entorno
,
regulator
io) que
está
siendo
imputad
a
injustam
ente al
asegurad
o.

Taxonomía General de Aplicaciones
Árbol de decisión asegurador: ¿qué buscar primero?
El árbol comienza con la identificación del análisis principal,
porque valoración, fraude del asegurado y diseño predatorio
de la aseguradora tienen instrumentos y prioridades de
evidencia radicalmente distintos.
¿Cuál es el análisis principal?
├─ Análisis A: VALORACIÓN DE SINIESTROS —
distribución justa del D_total y la indemnización
│
└─ PRIORIDAD 1: Peritaje técnico S2 de las causas
físicas del siniestro.
· ¿Qué factores fueron condición necesaria del evento?
¿Cuáles lo amplificaron?
· Construir el grafo causal con los cuatro niveles
(asegurado, entorno, regulatorio, diseño de póliza).
· Indemnización_justa_i = R*_i × D_total para cada
nodo con R* positivo.
├─ Análisis B: FRAUDE DEL ASEGURADO —
Δ_B_asegurado positivo
│
├─ PRIORIDAD 1: Tasación independiente del valor
real del activo S1/S2.
· ¿La suma asegurada excede el valor real? →
Sobrecobertura.
├─ PRIORIDAD 2: Peritaje técnico S2 de la
contribución causal del asegurado.
· ¿R*_asegurado es significativo? ¿S_asegurado es bajo?
· Si sí a ambas → Δ_B_asegurado = Indemnización −
R*_asegurado × D_real. Fraude verificable.
· Si S alto → sobrecobertura sin fraude. Error actuarial
en el diseño de la póliza.

Taxonomía General de Aplicaciones
└─ Análisis C: DISEÑO PREDATORIO —
Δ_B_aseguradora positivo
├─ PRIORIDAD 1: Análisis estadístico S4 de la
siniestralidad de la cartera.
· ¿La siniestralidad excede el umbral actuarialmente
esperado para la clase?
├─ PRIORIDAD 2: Comparar ratio_actual vs
θ_detección.
· Si ratio ≥ θ → umbral superado. Reporte proactivo
inmediato.
· Si ratio < θ → calcular t_detección y
N_adicionales_esperados.
└─ PRIORIDAD 3: Calcular Δ_B_aseguradora y
multa mínima disuasoria.
· Δ_B = B_primas_infladas + B_margen_diseño −
α_reconocimiento.
· Multa_mínima = Δ_B / P(detección) para romper
el incentivo al diseño predatorio.
— Fin del Capítulo 15 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

