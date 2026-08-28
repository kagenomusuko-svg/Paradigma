## PARTE I · Derecho y Justicia

### Capítulo 4
Derecho ambiental —
responsabilidad por daño ecológico
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo opera con dos instrumentos de imputación que no son
intercambiables. El primero es R* convencional: se usa cuando al menos un
actor es condición necesaria del daño — si ese actor no hubiera operado, el
daño no habría ocurrido o habría sido sustancialmente menor. El segundo es
el valor de Shapley (φᵢ): se usa cuando el daño es acumulativo y ningún actor
es individualmente condición necesaria — el daño ocurre por la suma de
contribuciones que superan un umbral, no por ninguna contribución
individual. La decisión entre R* y Shapley es la primera pregunta del análisis
ambiental y determina todo lo demás. Si tu prioridad es saber cuál aplica y
qué buscar primero, ve directamente a §9.
§1 Descripción del subcampo
El derecho ambiental es el dominio donde el sistema de
imputación causal enfrenta sus límites más claros y donde su
extensión —los valores de Shapley— es más necesaria. El
daño ecológico tiene cuatro características que lo distinguen
estructuralmente de todos los demás dominios de este libro y
que determinan los instrumentos adecuados para su análisis.

Taxonomía General de Aplicaciones
Consecuencia para el
Característica Descripción
análisis causal
Difusión El daño ecológico se El grafo causal debe incluir
temporal acumula a lo largo de nodos históricos que ya no
décadas o siglos. Los operan activamente. La
efectos pueden distancia temporal entre
manifestarse mucho causa y efecto complica la
después de que la atribución causal directa y
causa dejó de operar. produce evidencia A6/A7
El contaminante para las aristas de largo
emitido en el año t plazo.
puede producir daño
documentable en t +
30.
Difusión Los contaminantes R* de un nodo emisor
espacial se dispersan por puede calcularse, aunque el
agua, aire y suelo daño ocurriera en otra
cruzando fronteras jurisdicción, pero requiere
jurisdiccionales. El modelado de la dispersión
punto de medición como evidencia pericial
del daño puede estar (A2). El análisis de
lejos del punto de dispersión es condición
emisión. El necesaria para establecer la
contaminante cruza arista entre el emisor y el
jurisdicciones por daño.
diseño del proceso
físico, no del actor.
Causalidad El daño es El postulado de la
acumulativa frecuentemente el condición necesaria (I5) no
resultado de la se cumple para ningún
acumulación de actor individual. R*
contribuciones de convencional asigna cero a
múltiples actores sin todos — resultado
que ninguno de ellos técnicamente correcto,
sea por sí solo pero jurídicamente
condición necesaria inaplicable. Aquí es donde
y suficiente. El R* falla y los valores de
umbral de daño θ se Shapley son el instrumento
supera solo cuando correcto.
las contribuciones se
suman, no con la de
ningún actor
individual.
Irreversibilidad Algunos daños ΔT_trayectoria es el
parcial ecológicos son componente dominante

Taxonomía General de Aplicaciones
Consecuencia para el
Característica Descripción
análisis causal
permanentes o del daño ecológico de largo
requieren siglos para plazo. La incertidumbre
recuperarse: sobre el horizonte
extinción de temporal de la
especies, destrucción recuperación introduce
de ecosistemas rangos amplios en el
únicos, cálculo. Para daños
contaminación de irreversibles,
acuíferos profundos. D_monetary_equiv no es
La pérdida de lo que se puede pagar: es la
biodiversidad tiene medida de la
componentes inconmensurabilidad del
irreversibles que daño con cualquier
ninguna remediación reparación finita.
puede restaurar.
La decisión central del análisis ambiental: ¿R* o Shapley?
R* convencional es correcto cuando: al menos un actor es condición necesaria
del daño — sin ese actor específico el daño no habría ocurrido o habría sido
sustancialmente menor. Ejemplos: desastre industrial con fuente identificable
única o dominante, derrame de una sola empresa en un área no contaminada
previamente, vertido que produce daño inmediato localizable.
Valores de Shapley son necesarios cuando: el daño es acumulativo y ningún
actor es individualmente condición necesaria — incluso si ese actor hubiera
eliminado completamente sus emisiones, el daño habría ocurrido de todas
formas por la suma de las demás. Ejemplos: contaminación de largo plazo
por múltiples operadores en la misma cuenca, daño climático global por
emisiones de múltiples países, contaminación difusa de acuífero por múltiples
fuentes industriales y agrícolas.
La pregunta de diagnóstico: ¿Habría ocurrido el daño sin este actor específico,
dado lo que los otros habrían emitido de todas formas? Si la respuesta es no
→ R*. Si la respuesta es sí → Shapley.
Sub-variantes del dominio
Desastre industrial puntual: una instalación específica produjo
el daño mediante un evento identificable con origen claro y
único. El grafo incluye el operador directo, la casa matriz que

Taxonomía General de Aplicaciones
diseñó la tecnología y los estándares, el regulador que autorizó
las condiciones de operación, y los factores ambientales que
determinaron la magnitud de la dispersión. R* convencional
aplica porque hay al menos un actor condición necesaria.
Contaminación crónica por fuente única: emisiones continuas
de un solo operador durante un período prolongado. Similar
al desastre industrial en estructura del grafo, pero
ΔT_trayectoria es el componente dominante del daño. R*
convencional aplica.
Contaminación acumulativa por múltiples fuentes: el daño es
el resultado de la acumulación de contribuciones de varios
operadores en el mismo ecosistema durante un período
extendido. Ningún operador es condición necesaria
individualmente. Shapley es el instrumento correcto. La
estimación de v(S) para las coaliciones parciales es el desafío
central del análisis.
Daño climático por emisiones acumuladas: el caso límite y el
más político. Ningún emisor individual —ningún país,
ninguna empresa— es condición necesaria del cambio
climático. R* convencional asigna cero a todos. Los valores de
Shapley distribuyen la responsabilidad proporcional a la
contribución marginal promedio de cada emisor sobre todas
las posibles coaliciones. Es la base técnica para el diseño de
compromisos climáticos equitativos.
Daño por omisión regulatoria: el regulador que autorizó
condiciones que el sistema no debería haber tolerado, que no
inspeccionó instalaciones de riesgo conocido, o que asentó
comunidades en zonas de riesgo documentado. El regulador
tiene arista de omisión en el grafo con R* positivo cuando su
inacción fue condición causal del daño.
Responsabilidad de casa matrices multinacionales: la empresa
que diseñó la tecnología, estableció los estándares y aprobó las
reducciones de costo que comprometieron la seguridad tiene
R* positivo, aunque opere en otra jurisdicción. La separación
jurídica entre casa matriz y filial no elimina la arista causal en
el grafo.

Taxonomía General de Aplicaciones
§2 Escala de evidencia A0–A8 · Dominio
ambiental
La escala A0–A8 es la traducción de la jerarquía general E0–
E8 al vocabulario del daño ecológico. Los rangos w reflejan la
estructura epistémica específica del dominio: la evidencia
científico-técnica (peritajes de dispersión, análisis
ecotoxicológicos, modelado hidrológico) ocupa un lugar
prominente y puede superar en utilidad a la documentación
corporativa directa. Nivel A — rangos derivados por
extensión desde los principios del sistema y la práctica del
litigio ambiental; pendientes de calibración empírica formal.
Tipo de Descripción y ejemplos en Rango
Nivel
evidencia el dominio ambiental w
A1 Documento Permisos de emisión con [0.74,
corporativo o especificaciones que vinculan 0.92]
regulatorio al operador, actas de
directo inspección que documentan
el incumplimiento, correos
internos donde se tomó la
decisión de reducir los
estándares de seguridad,
registros de monitoreo oficial
que muestran la superación
de límites permisibles con
conocimiento del operador.
A2 Peritaje Análisis forense de [0.68,
científico- contaminación con trazado 0.87]
técnico de de la fuente, modelado de
dispersión y dispersión de contaminantes
atribución (hidrogeológico, atmosférico,
sedimentológico), análisis
ecotoxicológico que
establece la relación dosis-
respuesta, peritaje
epidemiológico que establece
la correlación entre
exposición y daño en salud.
Es frecuentemente el
instrumento principal en el
dominio ambiental.

Taxonomía General de Aplicaciones
Tipo de Descripción y ejemplos en Rango
Nivel
evidencia el dominio ambiental w
A3 Monitoreo Registros de monitoreo de [0.50,
ambiental oficial calidad del agua, suelo o aire 0.68]
convergente de autoridades ambientales
con análisis que muestran el patrón de
pericial contaminación, convergentes
con al menos un análisis
pericial que los vincula
causalmente a la fuente. El
patrón de monitoreo en el
tiempo establece la
trayectoria de la
contaminación.
A4 Correlación Análisis estadístico que [0.38,
estadística muestra correlación 0.58]
controlada en significativa entre el patrón
datos de de operación del emisor y el
monitoreo patrón de contaminación en
el ecosistema receptor,
controlando por fuentes
alternativas conocidas. La
cadena causal directa no está
probada pero la correlación
es sólida y los factores de
confusión están controlados.
A5 Testimonios Testimonios de miembros de [0.28,
convergentes de las comunidades afectadas 0.48]
comunidades sobre cambios observables
afectadas con en el ecosistema
corroboración (desaparición de especies,
parcial cambio de color del agua,
olores, enfermedades) que
son convergentes entre sí y
tienen al menos un elemento
documental consistente
aunque no prueba directa del
vínculo causal.
A6 Inferencia El nodo tenía la posición [0.18,
estructural por operativa, la autoridad y el 0.38]
posición en el conocimiento técnico para
sistema saber que sus emisiones o sus
productivo o estándares producirían el
regulatorio daño, sin documentación
directa de la decisión

Taxonomía General de Aplicaciones
Tipo de Descripción y ejemplos en Rango
Nivel
evidencia el dominio ambiental w
específica. Aplicable cuando
la empresa destruyó registros
o cuando el regulador nunca
documentó la omisión.
A7 Correlación La proximidad geográfica [0.07,
espacio- entre el emisor y el daño 0.24]
temporal sin sugiere causalidad, pero sin
modelado de evidencia del mecanismo de
dispersión dispersión ni de la cadena
físico-química. La empresa
está en el área, el daño está en
el área, pero el vínculo causal
no está modelado.
A8 Estimación sin Única fuente sin respaldo [0.04,
corroboración técnico ni monitoreo 0.16]
técnica corroborante. Solo se usa
cuando no hay nada más y el
contexto hace plausible la
versión.
A0 Ausencia Modelado de dispersión que w =
documentada de demuestra que el 0.00
conexión causal contaminante del nodo no
llegó al punto de daño bajo
ningún escenario de
condiciones ambientales
razonables. Análisis que
muestra que el nodo no
operaba en el período del
daño.
La jerarquía del peritaje científico en el dominio ambiental
En el dominio ambiental, la evidencia A2 (peritaje científico-
técnico) frecuentemente supera en importancia operativa a la
A1 (documentación corporativa directa) porque el vínculo
causal entre la emisión y el daño es un hecho físico que el
peritaje reconstruye independientemente de la documentación
que el actor haya producido o destruido. Un análisis
hidrogeológico que establece que el contaminante del nodo X

Taxonomía General de Aplicaciones
llegó al punto de daño Y bajo las condiciones ambientales del
período relevante es evidencia más sólida que la ausencia de
documentación interna del nodo — que puede deberse
precisamente a que la documentación fue eliminada.
Cuando A2 contradice a A1 — el peritaje no confirma lo que
los registros del operador declaran — se aplica la regla de
prioridad del cap. U·2 con desplazamiento hacia el extremo
conservador del rango A1. La contradicción es señal de
investigación adicional, no de resolución automática a favor de
la documentación corporativa.
§3 Firmas documentales por Hijo e
información para S
En el dominio ambiental, los Hijos de Afrodita informan S del
actor específico — cuánto de su comportamiento era
idiosincrático versus determinado por el marco regulatorio y
económico en el que operaba. La distinción más relevante es
entre Fobos (el operador actuó bajo un sistema de incentivos
económicos que determinó el comportamiento: cualquier
empresa en la misma posición habría actuado igual) y Anteros
(el operador tomó decisiones específicas que excedían lo que
el marco económico e incluso el marco regulatorio de su sector
determinaban). S alto implica que el problema es del marco
normativo, no de ese operador específico; S bajo implica que
las prácticas idiosincráticas del operador eran la condición
causal determinante.
§3.1 Hijos de legibilidad alta en el dominio ambiental

Taxonomía General de Aplicaciones
Firma en Error de
Qué Fuente
el discrimina
Hijo informa document
expediente ción
para S al típica
ambiental frecuente
Fobo S alto [0.70, Declaracion Informes Confundir
s 0.90]. El es que sectoriales con
sistema de describen la que Anteros
incentivos decisión muestran el cuando la
económicos como estándar de empresa
y el marco inevitable la industria redujo
regulatorio dado el en el estándares
determinaro contexto período. por debajo
n el económico Comunicaci del
comportami y ones promedio
ento del regulatorio: internas del sector.
operador: "los sobre Si las
cualquier estándares presión de prácticas
empresa que el sector costos. del
con la usaba", "la Comparació operador
misma tecnología n con otras eran peores
tecnología disponible empresas que las de
disponible, en el del sector sus pares
bajo el período". bajo el bajo el
mismo Evidencia mismo mismo
marco de que el marco marco, S es
normativo y comportami normativo. moderado-
con los ento del bajo, no
mismos operador alto.
incentivos era común
de costo en el sector
habría bajo las
generado el mismas
mismo condiciones
daño. El regulatorias.
problema es Presión
del marco, documenta
no del da de costos
operador desde la
específico. casa matriz
que hacía
inviable la
alternativa
más limpia.
Deim S alto [0.75, Ausencia de Registros de Confundir
os 0.92]. La registros de inspección con
omisión del inspección del Anteros
regulador: la en períodos regulador (o cuando el

Taxonomía General de Aplicaciones
Firma en Error de
Qué Fuente
el discrimina
Hijo informa document
expediente ción
para S al típica
ambiental frecuente
agencia donde la ausencia de regulador
ambiental normativa ellos). tomó
que no los requería. Expediente decisiones
inspeccionó Aprobacion s de discrecional
, que no es rutinarias permisos es
actualizó los de permisos con su específicas
estándares sin análisis contenido que
cuando de riesgo en técnico. excedieron
tenía expedientes Comunicaci su omisión
evidencia de que ones de rutinaria —
que eran deberían organismos por
insuficiente tenerlo. técnicos al ejemplo,
s, que Silencio regulador reclasificar
procesó documental que zonas de
permisos ante alertas quedaron protección
rutinariame de sin para
nte sin organismos respuesta facilitar una
análisis de técnicos que documenta operación
riesgo. La llegaron al da. específica.
omisión era regulador. Eso es
estructural Anteros del
mente regulador
producida con S bajo.
por el
marco
institucional
del
regulador.
Anter S bajo [0.08, Documento Informes Confundir
os 0.32]. El s que técnicos Anteros
operador muestran internos con el
tomó que las que resultado
decisiones prácticas del describían del daño. El
idiosincrátic operador el riesgo hecho de
as que eran antes del que el daño
excedían lo inferiores al daño. ocurrió no
que el estándar de Correos de implica
marco la industria ingenieros o Anteros:
económico bajo las técnicos hay que
y el marco mismas objetando verificar si
regulatorio condiciones las las prácticas
del sector . Decisiones reducciones del
determinab de de estándar. operador

Taxonomía General de Aplicaciones
Firma en Error de
Qué Fuente
el discrimina
Hijo informa document
expediente ción
para S al típica
ambiental frecuente
an: reducción Datos diferían del
reducciones de costos comparativ estándar del
de costo que que los os con sector. Si no
sus propios propios empresas diferían, S
pares de ingenieros pares del es alto
sector no de la sector en el aunque el
adoptaron, empresa mismo daño fuera
eliminación objetaron. período. grave.
de sistemas Comparació
de n con pares
seguridad del sector
que sus que
competidor operaban
es con las
mantuviero mismas
n, omisión presiones
de económicas
mantenimie y no
nto que el produjeron
estándar de el mismo
la industria daño.
exigía. La
condición
causal
idiosincrátic
a del daño
fue la
decisión
específica
de ese
operador.
§3.2 Hijos de legibilidad baja en el dominio ambiental
Potós: puede aparecer cuando el operador replicó prácticas
heredadas de una gestión anterior sin cuestionarlas — la planta
que siguió operando exactamente igual que siempre, sin
actualizar sus estándares a pesar de que la evidencia científica
sobre los daños de sus emisiones había cambiado. Informa S
moderado-alto, pero es indistinguible de Deimos disfrazado

Taxonomía General de Aplicaciones
de tradición operativa. La pregunta discriminante: ¿el operador
tenía información técnica de que sus prácticas producían el
daño? Si la tenía y no actuó, puede ser Deimos. Asignar con
nota obligatoria de incertidumbre alta.
Eros: puede aparecer cuando el operador adoptó nuevas
tecnologías o procesos de manera proactiva y genuinamente
convencida de que eran más eficientes, sin anticipar que
producirían daño ambiental. La apertura hacia la innovación
era genuina, el daño no estaba en el mapa de consecuencias
del actor. Informa S moderado. Asignar con nota obligatoria
de incertidumbre alta.
§3.3 Harmonía — irrelevante para los actores
institucionales del dominio ambiental
Las empresas y los reguladores son egos colectivos, no sujetos individuales con
v_t localizable. Para los actores institucionales de este dominio, el análisis del
Hijo se aplica solo si hay un actor individual identificable — el directivo que
tomó la decisión específica, el funcionario que omitió la inspección. Para el ego
colectivo institucional, S se estima directamente por Ruta B (escala DS del
cap. U·3) desde la evidencia documental de la determinación sistémica del acto.
§4 ¿Qué cuenta como asunción (α) en el
dominio ambiental?
α en el dominio ambiental mide el grado en que el actor ha
actuado sobre su posición causal mediante acciones concretas
y verificables: remediación del daño producido, prevención de
daño futuro, modificación del sistema que lo causó. α mide
acciones, no declaraciones, compromisos sin ejecución ni
programas de imagen.
α es completamente independiente del dolo en el dominio
ambiental
Un operador que contaminó deliberadamente puede tener α alto si después
remedió proporcional a su R*. Un operador que contaminó sin intención

Taxonomía General de Aplicaciones
deliberada — porque el marco regulatorio lo permitía — puede tener α = 0
si nunca implementó ninguna medida de remediación ni prevención. Los Hijos
informan S (idiosincrasia del acto); α mide lo que el actor hizo después sobre
su posición causal.
α voluntario, forzado e impuesto en el contexto ambiental
En el dominio ambiental, α forzado e impuesto es frecuente:
las órdenes de remediación de autoridades ambientales, las
sentencias de tribunales que imponen planes de limpieza, y las
multas administrativas proporcionales al daño son α impuesto
que el método registra igual que el α voluntario. Si el operador
pagó la multa porque la autoridad ambiental se la impuso, su
α sube igual que si la hubiera pagado voluntariamente.
Acción del ¿Cuenta para
Razón Tipo de α
actor α?
Remediación Sí — α La forma más Voluntari
del suelo, agua máximo completa de α o o
o hábitat ambiental. forzado
dañado con Reconocimiento por
verificación con reparación sentencia
técnica del verificable del
resultado ecosistema.
Pago de multas Sí — bajo a α forzado Forzado /
administrativa moderado económico. Su impuesto
s nivel depende de la
proporcionales proporción de la
al daño multa respecto al
documentado AD_i = R*_i ×
D_total.
Adopción de Sí — α Reduce la Voluntari
tecnología más estructural de probabilidad del o o
limpia que prevención próximo evento. requerido
reduce La asunción por
emisiones preventiva tiene regulación
futuras valor
independiente de
la remediación.

Taxonomía General de Aplicaciones
Acción del ¿Cuenta para
Razón Tipo de α
actor α?
Plan de Sí — α Modifica el Voluntari
contingencia estructural sistema que podría o o
implementado producir el daño impuesto
con futuro.
protocolos
verificables
Compensación Sí — Asunción Voluntari
a comunidades moderado a económica directa o o
afectadas alto hacia los negociado
proporcional afectados.
al AD_i de la
empresa
Publicar un No Declaración sin —
informe de consecuencia
sostenibilidad concreta sobre la
sin modificar posición causal.
el sistema de No modifica α.
emisiones
Comprar No modifica α La compra de —
bonos de del daño bonos no modifica
carbono sin propio — la posición causal
reducir puede ser α de del emisor sobre el
emisiones compensació daño que ya
propias n sistémica produjo.
Remediación Sí — bajo α real pero Voluntari
parcial de la desproporcionado o selectivo
zona menos : el actor eligió — señal
dañada asumir la parte de alerta
mientras la más barata sin
más dañada proporcionalidad a
permanece sin R*.
tratar
La escala de α en el dominio ambiental
Rangos derivados por extensión de los principios del sistema. Pendientes
de calibración empírica.

Taxonomía General de Aplicaciones
Descripción
Rango observable en el Indicadores
Nivel
α dominio verificables
ambiental
Negación / 0.00 – El operador niega Sin pagos, sin
evasión total 0.05 su contribución al remediación, sin
daño, combate modificaciones
activamente el del sistema de
proceso emisiones, sin
ambiental y no ha reconocimiento
implementado ante la autoridad
ninguna medida ambiental.
de remediación ni Recurso activo de
prevención. El todas las
proceso resoluciones sin
regulatorio o acciones
judicial está paralelas.
activo sin
acciones
concretas.
Reconocimiento 0.06 – El operador Comunicados
nominal 0.20 reconoció públicos
formalmente su documentados.
contribución, Informes de
pero sin sostenibilidad.
consecuencia Ninguna
concreta. remediación
Declaraciones de verificable.
"compromiso Multas no
ambiental", pagadas o
informe de recurridas.
sostenibilidad,
"lamentamos el
impacto" sin
remediación.
Asunción 0.21 – El operador pagó Multas
parcial 0.45 multas o administrativas
implementó pagadas
medidas de equivalentes al
remediación 10–30% del
menores a lo que daño.
su R* indica. Hay Remediación de
acciones zonas menores o
concretas pero la más accesibles.
proporcionalidad Planes de
contingencia

Taxonomía General de Aplicaciones
Descripción
Rango observable en el Indicadores
Nivel
α dominio verificables
ambiental
está muy lejos del aprobados pero
AD_i. no
completamente
implementados.
Asunción activa 0.46 – El operador está Remediación del
en proceso 0.70 en proceso activo 40–60% del área
de remediación afectada
con acciones verificada por
concretas y peritaje. Planes
verificables. Las de remediación
acciones son aprobados y en
sustanciales ejecución con
aunque no hayan seguimiento
alcanzado la técnico.
proporcionalidad Compensaciones
completa del parciales a
AD_i. comunidades en
proceso de pago.
Asunción 0.71 – El operador ha Remediación del
funcional 0.89 asumido la mayor 70–85% del área
parte de su documentada
posición. Las con verificación
acciones de técnica.
remediación son Compensaciones
proporcionales a sustanciales
su R* aunque no pagadas a las
perfectas. comunidades
afectadas.
Modificación
verificable del
sistema de
emisiones con
datos de mejora.
Asunción plena 0.90 – El operador Remediación
1.00 asumió completa
completamente certificada por
su posición peritaje
causal. La independiente.
remediación es Compensación
proporcional a su integral a
R*, el sistema que comunidades.

Taxonomía General de Aplicaciones
Descripción
Rango observable en el Indicadores
Nivel
α dominio verificables
ambiental
produjo el daño Modificación del
fue modificado sistema de
estructuralmente emisiones con
y hay seguimiento datos verificables
verificable de de reducción
resultados sostenida.
distintos. Reconocimiento
formal de la
posición causal
ante la autoridad.
Δ y el déficit de remediación
Δ_i = R*_i − α_i (en R* convencional) o Δ_i = φᵢ − α_i (en
Shapley) mide la brecha entre la contribución causal al daño y
la remediación implementada. Δ positivo es la base técnica
para la acción de responsabilidad ambiental y para las órdenes
de remediación proporcionales. La orden de remediación
técnicamente justificada es:
Orden_remediación_proporcional_i = R*_i × (1 − S_i) ×
D_total.
La irreversibilidad y el límite de la compensación
monetaria
Algunos daños ecológicos son irreversibles: la extinción de especies, la
destrucción de ecosistemas únicos, el daño permanente a comunidades
culturalmente arraigadas en un territorio. Para estos daños,
D_monetary_equiv puede ser calculable pero la promesa de reparación
monetaria es ontológicamente vacía. El sistema reconoce honestamente este
límite: D_monetary_equiv no es lo que se debe pagar — es la medida de la
magnitud del daño. Cuando esa magnitud supera cualquier capacidad de
compensación, la fórmula cumple su función más importante, que es hacer
visible la inconmensurabilidad entre el daño y cualquier reparación finita
posible.

Taxonomía General de Aplicaciones
§5 Construcción del grafo típico del dominio
ambiental
Tipos de nodo en el grafo ambiental
Ejemplo en el
Función en el
Tipo S típico dominio
grafo
ambiental
Operador La empresa u Variable La filial que
directo organización [0.20–0.85] opera la planta
(Op) que opera la con los
fuente de estándares
contaminación. comprometidos.
Causa inmediata El operador del
del daño. R* pozo que
alto cuando es produce el
condición derrame. La
necesaria. S empresa que
mide si vierte los
cualquier otra residuos.
empresa bajo las
mismas
condiciones
habría actuado
igual.
Diseñador La empresa que Bajo- La casa matriz
/ casa diseñó la moderado que diseñó la
matriz (D) tecnología, [0.15–0.50] tecnología con
estableció los riesgo conocido.
estándares de La dirección
seguridad y corporativa que
aprobó las aprobó los
reducciones de estándares
costo. R* del rebajados. La
nodo de diseño empresa que
es comparable o estableció el
mayor que el del protocolo de
operador operación
cuando las deficiente.
decisiones de
diseño eran
condición
causal del daño.

Taxonomía General de Aplicaciones
Ejemplo en el
Función en el
Tipo S típico dominio
grafo
ambiental
Regulador El Estado que Alto [0.55– La agencia
/ gobierno autorizó la 0.85] ambiental que
(Reg) operación, no inspeccionó.
reguló las El gobierno que
condiciones de asentó
seguridad y comunidades en
tenía obligación zona de riesgo
de inspeccionar. conocido. El
R* positivo ministerio que
cuando el aprobó el
regulador permiso sin
aprobó análisis de riesgo
condiciones que adecuado.
el sistema no
debería haber
tolerado, o
cuando la
omisión de
inspección fue
condición del
daño.
Factor Las condiciones N/A — no es Dirección del
ambiental del ecosistema actor viento que
(FA) receptor que dirigió el
determinaron la contaminante
dispersión y el hacia la
impacto del comunidad.
contaminante: Corriente
dirección del subterránea que
viento, transportó el
corrientes de lixiviado.
agua, Características
características del suelo que
del suelo, facilitaron la
densidad de absorción.
población. No
tiene R* en
sentido de
responsabilidad
— no es un
actor — pero
sus condiciones
son parte del
grafo causal y

Taxonomía General de Aplicaciones
Ejemplo en el
Función en el
Tipo S típico dominio
grafo
ambiental
determinan la
magnitud del
daño dado el
nivel de
emisión.
Comunidad El receptor del Generalmente La comunidad
afectada daño: las no aplica indígena cuyo
(Nf) personas, territorio fue
comunidades y contaminado. La
ecosistemas que población cuya
sufrieron las fuente de agua
consecuencias. fue afectada. Los
No entra en el ecosistemas
cálculo de R* acuáticos
del daño salvo dañados por el
cuando vertido.
contribuyó
causalmente —
caso inusual
dado la
asimetría de
información
entre el
operador y la
comunidad
sobre el riesgo.
Tipos de arista en el grafo ambiental
Arista directa de emisión o vertido: conecta el operador
directo con el daño mediante el proceso físico de
contaminación. Sustentada por A2 (peritaje de dispersión que
traza la huella del contaminante) o A1 (registros de emisiones
del propio operador).
Arista estructural de diseño: conecta la casa matriz con el daño
mediante los estándares, la tecnología y las decisiones de
reducción de costo que diseñó. Sustentada por A1
(documentos internos de decisión) o A4/A6 (inferencia desde

Taxonomía General de Aplicaciones
la comparación con estándares alternativos disponibles en el
período).
Arista de omisión regulatoria: conecta el regulador con el daño
mediante la inacción documentada. Requiere: (1) deber de
inspeccionar o regular documentado en normativa; (2)
evidencia de que el regulador tenía o debía tener información
del riesgo. Sin ambos elementos, la arista de omisión no tiene
sustento.
Arista de amplificación ambiental: conecta el factor ambiental
(FA) con la magnitud del daño. No tiene R* propio, pero
pondera la proporcionalidad del daño — el mismo nivel de
emisión produce daños de distinta magnitud según las
condiciones ambientales del receptor.
Configuraciones canónicas del grafo ambiental
Configuración 1 — Desastre industrial puntual (R* convencional)
D (casa matriz / estándares) → Op (operador directo / proceso de
producción) + Reg (regulador omisivo) → FA (condiciones ambientales) →
Daño en Nf
Al menos un actor — típicamente la combinación Op + D — es condición
necesaria del daño. R* convencional es el instrumento correcto. La distribución
entre D y Op depende de si el operador actuaba dentro de los estándares
aprobados por D (R* de D alto) o por debajo (R* compartido con
distribución dependiente de cuánto D sabía y no actuó).
Configuración 2 — Contaminación acumulativa por múltiples
operadores (Shapley)
Op₁ (operador 1, período t₁-t₂) + Op₂ (operador 2, período t₂-t₃) + Op₃
(fuentes difusas) → Daño acumulado en Nf
Ningún operador individual es condición necesaria: el daño habría ocurrido
de todas formas por la suma de las otras fuentes. R* convencional asigna cero
a todos — técnicamente correcto, pero jurídicamente inaplicable. Shapley
distribuye la responsabilidad proporcional a la contribución marginal

Taxonomía General de Aplicaciones
promedio de cada operador sobre todas las posibles coaliciones. La función de
valor v(S) para cada coalición se estima con los datos de monitoreo y el
modelado de dispersión.
Configuración 3 — Responsabilidad de casa matriz multinacional
D_matriz (casa matriz / diseñadora de estándares, jurisdicción A) →
Op_filial (filial operadora, jurisdicción B) → Daño en Nf (jurisdicción B)
La separación jurídica entre casa matriz y filial no elimina la arista causal.
La condición para que D_matriz tenga R* positivo: las decisiones de
D_matriz (tecnología, estándares, reducción de costos) eran condición causal
del daño — sin esas decisiones, el daño no habría ocurrido en esa forma. El
análisis de S de la filial determina cuánto de su comportamiento era
determinado por las instrucciones de D_matriz.
§6 Preguntas que responde este capítulo
Nivel de
Pregunta
Instrumento que la responde certeza
del caso
posible
¿El daño Diagnóstico previo: ¿Habría La respuesta a
tiene un ocurrido el daño sin este actor dado esta pregunta
actor lo que los otros habrían producido? diagnóstica
condición Si no → R*. Si sí → Shapley. Ver §9, determina el
necesaria o primera rama del árbol de decisión. instrumento.
es No es una
acumulativo Declaración
— R* o en sí misma
Shapley? pero
condiciona
todas las que
siguen.
¿La casa R* positivo de D_matriz si sus Declaración A
matriz tiene decisiones (tecnología, estándares, o B si hay
R* positivo reducciones de costo) eran documentos
aunque solo condición causal del daño. Arista internos A1
la filial D_matriz → daño sustentada por de las
operara la A1 (documentos internos) o A4/A6 decisiones de
instalación? (comparación con pares del sector). la casa matriz.
Declaración C

Taxonomía General de Aplicaciones
Nivel de
Pregunta
Instrumento que la responde certeza
del caso
posible
si la inferencia
es A6.
¿El Arista de omisión del regulador: Declaración A
regulador deber de inspeccionar si el deber está
que no documentado en normativa (A1) + en normativa
inspeccionó evidencia de que tenía o debía tener y la omisión
tiene R* información del riesgo (A3 o A5). Si está
significativo ambos están presentes, R* del documentada.
por su regulador es positivo. Declaración C
omisión? si el deber es
inferido o el
conocimiento
del riesgo es
indirecto.
¿Cuánto del Valores de Shapley: φᵢ = Declaración B
daño es contribución marginal promedio del si los datos de
proporcional actor i sobre todas las posibles monitoreo y el
a la coaliciones. Requiere estimación de modelado de
contribución v(S) para las coaliciones parciales. dispersión
de cada La suma Σφᵢ = D_total verifica la permiten
operador en eficiencia. estimar v(S)
un caso con buena
acumulativo precisión.
? Declaración C
si v(S) de las
coaliciones
parciales
requiere
estimaciones
contrafácticas
con alta
incertidumbre
.
¿S alto del S alto del operador (cualquier Declaración A
operador empresa bajo el mismo marco o B si la
implica que habría actuado igual) implica que el comparación
la reforma problema es del marco regulatorio, con pares del
debe ser no de ese operador específico. La sector está
normativa, orden contra el operador es justa documentada
no una pero insuficiente si el marco no con A3 o A4.
orden de cambia. Declaración C
remediación si la

Taxonomía General de Aplicaciones
Nivel de
Pregunta
Instrumento que la responde certeza
del caso
posible
solo contra comparación
ese es inferida.
operador?
¿La compra No en el sentido de α del daño Declaración A
de bonos de propio. La compra de bonos no — la
carbono por remedia la posición causal del distinción es
el operador operador sobre el daño que ya conceptual y
modifica su produjo. α requiere acciones sobre no depende
α? la posición causal específica: de evidencia
remediación, modificación del adicional.
sistema de emisiones,
compensación a las comunidades
afectadas.
¿Cuál es la Orden_remediación_proporcional_ Depende de la
orden de i = R*_i × (1 − S_i) × D_total. La calidad de R*
remediación proporción (1 − S_i) refleja que solo y S.
técnicament la fracción idiosincrática de la Declaración A
e contribución del operador justifica si la evidencia
proporcional la orden sobre ese operador es A1/A2.
al R* del específico; la fracción S_i Declaración B
operador? corresponde al marco regulatorio o C si hay
que el conjunto del sector debe componentes
modificar. de inferencia
estructural.
§7 Traducción de D_total al dominio
ambiental
Los servicios ecosistémicos son tiempo de vida cristalizado de
las comunidades que dependen de esos ecosistemas para
subsistir. Cuando una comunidad pierde su suelo cultivable,
su fuente de agua o sus recursos pesqueros por daño
ambiental, cada año de pérdida de esos servicios es trabajo no
recompensado, subsistencia no posible y salud deteriorada.
D_vital = D_total / w_ref captura esa dimensión: el daño
ambiental siempre es también un daño a la economía del
tiempo de vida de las comunidades afectadas.

Taxonomía General de Aplicaciones
Definición
Component en el Cómo se Fuente de
e dominio mide evidencia
ambiental
T_invertido Pérdida Inventario de Registros
(daño directa en el daños médicos de la
inmediato) momento del documentados emergencia.
evento o en el con registros Inventarios
período inicial médicos y ambientales
de ambientales. antes y después
contaminació Costo de del evento.
n: muertes, atención Peritaje de
lesiones médica de daños físicos
agudas urgencia. inmediatos.
documentadas Valoración de
, destrucción activos
de activos naturales
naturales destruidos
(hábitat, suelo, usando
agua), costos métodos de
de atención costo de
médica de reemplazo.
urgencia,
pérdida
inmediata de
medios de
subsistencia de
las
comunidades.
T_impedido Pérdida de los Valoración Estudios de
(pérdida de servicios que económica de valoración de
servicios el ecosistema los servicios servicios
ecosistémicos dañado ecosistémicos ecosistémicos.
durante el proveía perdidos por Registros de
período de durante el año, producción
contaminació período en multiplicada agrícola,
n activa) que la por el período pesquera o
contaminació de turística antes y
n impidió su contaminación durante la
funcionamient activa. contaminación
o normal: agua Métodos: . Facturas de
potable no costo de alternativas
disponible, reemplazo, que las
suelo no preferencia comunidades
cultivable, revelada debieron
recursos (cuánto pagar.

Taxonomía General de Aplicaciones
Definición
Component en el Cómo se Fuente de
e dominio mide evidencia
ambiental
pesqueros no pagaron las
cosechables, comunidades
ecoturismo por
imposible. Es alternativas),
la pérdida de valoración
flujos de contingente.
servicios
durante el
período de
contaminació
n activa.
ΔT_trayectori La diferencia Modelos de Estudios
a (pérdida entre el estado recuperación epidemiológic
permanente o del ecosistema ecológica con y os
de muy largo y de las sin longitudinales.
plazo) comunidades remediación. Modelos de
si no hubiera Estudios recuperación
ocurrido el epidemiológic ecológica de
daño y el os de largo largo plazo.
estado real: plazo sobre el Censos de
pérdida diferencial de biodiversidad
permanente de esperanza de antes y después
biodiversidad, vida y de del daño con
daño morbilidad proyección de
irreversible a entre la recuperación.
ecosistemas comunidad
únicos, expuesta y una
reducción comparable sin
permanente de exposición.
la esperanza Valoración de
de vida de las la pérdida
comunidades permanente de
expuestas, biodiversidad
daño mediante
generacional disposición a
en salud. Es el pagar.
componente
dominante en
los daños de
largo plazo.

Taxonomía General de Aplicaciones
D_vital ambiental y la dualidad ontológica del daño ecológico
D_vital = D_total / w_ref convierte el daño ambiental a horas de vida de
las comunidades afectadas. Un año de pérdida de la fuente de agua de una
comunidad es el equivalente en trabajo, salud y subsistencia de N personas ×
8,760 horas × (1 − q), donde q es la fracción de las condiciones de vida que
se mantuvieron sin la fuente de agua.
Para los daños con componente de pérdida permanente de biodiversidad o de
ecosistemas únicos: D_monetary_equiv puede ser calculable pero la promesa
de reparación monetaria es ontológicamente vacía. La fórmula cumple su
función más importante — hacer visible que el daño es inconmensurable con
cualquier reparación finita posible — sin pretender que el resultado sea el
monto que se puede exigir. El monto jurídicamente exigible es proporcional
al AD_i del operador sobre la fracción del daño que es monetariamente
cuantificable.
§8 Límites del método y errores frecuentes de
aplicación
Límites del método en el dominio ambiental
Límite 1 — El postulado de la condición necesaria en
causalidad acumulativa. Cuando el daño es acumulativo y
ningún actor es individualmente condición necesaria, R*
convencional asigna cero a todos los actores — técnicamente
correcto, pero jurídicamente inaplicable. La extensión Shapley
resuelve este límite cuando la función de valor v(S) puede
estimarse con datos suficientes. Si v(S) no puede estimarse, la
Declaración es C o D.
Límite 2 — La incertidumbre en los datos de dispersión. El
cálculo de R* y de los valores de Shapley en el dominio
ambiental requiere estimar cuánto del daño observado es
atribuible a cada fuente. En daños de largo plazo, esa
atribución requiere modelos de dispersión con incertidumbre
inherente. El resultado debe siempre presentarse como un
rango, no como un valor puntual.
Límite 3 — La función de valor v(S) de las coaliciones
parciales no siempre es estimable. El cálculo de Shapley
requiere v(S) para todas las coaliciones posibles.

Taxonomía General de Aplicaciones
Frecuentemente solo el daño del conjunto completo v(N) es
observable, mientras que los daños de las coaliciones parciales
deben estimarse con modelos contrafácticos. Esa estimación
tiene incertidumbre que se propaga a los valores de Shapley
calculados.
Límite 4 — La irreversibilidad y la limitación de la
compensación monetaria. Algunos daños ecológicos son
irreversibles. Para estos, D_monetary_equiv no es lo que se
puede exigir como reparación: es la medida de la magnitud del
daño. El analista que presenta D_monetary_equiv de un daño
irreversible como el monto de la pretensión jurídica está fuera
del alcance del método.
Errores frecuentes de aplicación
Por qué Consecuen
Error Corrección
ocurre cia
Usar R* El analista R* Verificar antes
convencional aplica el convencion de calcular:
cuando el daño instrumento al asigna ¿habría
es acumulativo estándar sin cero a todos ocurrido el
y ningún actor verificar si el los actores daño sin este
es condición postulado I5 se — resultado actor dado lo
necesaria cumple. jurídicamen que los otros
te inútil. El habrían
análisis producido? Si
produce sí → Shapley.
Declaración
D cuando
debería
producir
Declaración
B con
Shapley.
No incluir la El analista R* de la casa Construir el
casa matriz en sigue la matriz = 0 grafo desde el
el grafo porque estructura aunque sus resultado hacia
solo la filial jurídica de decisiones atrás.
separación de Preguntar: ¿sin

Taxonomía General de Aplicaciones
Por qué Consecuen
Error Corrección
ocurre cia
operó la entre casa tecnología y las decisiones
instalación matriz y filial estándares de la casa
sin preguntar si fueran matriz el daño
la casa matriz condición habría ocurrido
es nodo causal. causal del en esta forma?
daño. La
responsabili
dad recae
solo sobre la
filial.
No incluir el Las aristas de R* del Para cada actor
regulador en el omisión son regulador = con deber
grafo por la difíciles. El 0 aunque su documentado
dificultad de analista incluye omisión de de actuar:
probar la solo al inspección ¿tenía
omisión operador. fuera información
condición del riesgo?
del daño. El ¿Actuó? Si no
operador → incluir arista
carga con la de omisión con
totalidad del el nivel
R* que disponible y
correspond declarar su
e distribuir certeza.
entre
operador y
regulador.
Aceptar la El analista α α del daño
compra de registra el gasto sobreestima propio requiere
bonos de en bonos como do. Δ acciones sobre
carbono como acción sobre la subestimad esa posición
α del daño posición causal. o. El causal
ambiental operador no específica. Los
propio ha bonos de
remediado carbono son
su posición compensación
causal pero de otro daño
aparece con (emisiones
α propias de
moderado. CO₂), no
remediación
del daño
ecológico

Taxonomía General de Aplicaciones
Por qué Consecuen
Error Corrección
ocurre cia
directo
analizado.
Presentar El analista La D_monetary_e
D_monetary_e calcula pretensión quiv de daños
quiv del daño D_monetary_e es irreversibles es
irreversible quiv y lo usa numéricame la medida de la
como el monto directamente nte magnitud
de la como imposible ontológica del
pretensión pretensión. de satisfacer daño, no el
jurídica y puede monto exigible.
desacreditar El monto
el análisis exigible es
completo. AD_i = R*_i ×
D_cuantificabl
e sobre la
fracción
monetariament
e cuantificable.
§9 Guía de prioridades de recolección de
evidencia
La primera pregunta del análisis ambiental — ¿R* o Shapley?
— condiciona todo lo demás. El árbol de decisión comienza
aquí.
Tabla de prioridades de recolección de evidencia
ambiental
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más rango
funciona qué
principal la reduce reduce
preguntar
es… es…
1. ¿R* Evidencia Si el Determin ¿Operaban
convencio de que el modelado a el otras

Taxonomía General de Aplicaciones
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más rango
funciona qué
principal la reduce reduce
preguntar
es… es…
nal o daño muestra instrumen fuentes de
Shapley habría que el to de contaminac
— hay ocurrido (o daño imputació ión del
actores no) sin el habría n — mismo tipo
condición actor ocurrido decisión en el área?
necesaria? específico igualment fundamen ¿El daño
dado lo que e sin el tal hubiera
los otros actor → ocurrido
habrían Shapley. Si con esas
producido. muestra fuentes
Monitoreo que el solas? ¿El
ambiental daño modelado
de zonas habría sido de
comparabl sustancial dispersión
es sin ese mente puede
actor menor → correr el
(A3/A4). R* escenario
Modelos de convencio sin este
dispersión nal. actor?
de las otras
fuentes sin
la
contribució
n del actor
analizado
(A2).
2. ¿La Peritaje de Sin el Reduce ¿Existe un
arista dispersión modelo de rango de peritaje de
entre el A2: dispersión, w de la dispersión
emisor y el modelado la arista arista del
punto de hidrológico entre el principal contamina
daño , emisor y el (incertidu nte
existe — atmosféric daño es mbre específico
modelo de o o inferencia empírica) bajo las
dispersión sedimentol espacial condicione
? ógico que A7 con w s
traza la bajo ambientale
trayectoria [0.07– s del
del 0.24]. Con período?
contamina el modelo, ¿Los datos
nte desde el la arista es de
punto de A2 con w monitoreo

Taxonomía General de Aplicaciones
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más rango
funciona qué
principal la reduce reduce
preguntar
es… es…
emisión [0.68– muestran el
hasta el 0.87]. patrón de
punto de propagació
daño bajo n del
las contamina
condicione nte?
s
ambientale
s del
período.
3. ¿La casa Document La casa Reduce ¿La casa
matriz os A1 de matriz rango de matriz
tiene R* las tiene R* R* de la diseñó la
positivo decisiones positivo casa tecnología?
— de la casa cuando matriz ¿Aprobó
decisiones matriz: sus (incertidu las
de diseño tecnología decisiones mbre reduccione
y diseñada, eran empírica) s de costo
estándares estándares condición que
? establecido causal — comprome
s, sin ellas el tieron los
decisiones daño no sistemas de
de habría seguridad?
reducción ocurrido ¿Las
de costo en esa prácticas
que forma. La resultantes
comprome comparaci eran
tieron la ón con el inferiores al
seguridad. estándar estándar
Comparaci del sector del sector?
ón A4 con determina
los si las
estándares decisiones
que el eran
sector idiosincrát
usaba para icas (S
verificar bajo del
que las D_matriz)
decisiones o no.
de la casa
matriz eran
por debajo

Taxonomía General de Aplicaciones
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más rango
funciona qué
principal la reduce reduce
preguntar
es… es…
del
estándar.
4. ¿El Dos La arista Reduce ¿La
regulador elementos de rango de normativa
tiene R* simultáneo omisión R* del establecía
por s: (a) requiere regulador la
omisión normativa ambos (incertidu obligación
— deber y que elementos. mbre de
conocimie establece el Sin el empírica) inspeccion
nto deber de deber ar en el
simultáne inspeccion document período?
os? ar o regular ado, la ¿El
(A1); (b) omisión regulador
evidencia no es recibió
de que el condición alertas,
regulador causal. Sin denuncias
tenía o el o informes
debía tener conocimie técnicos
informació nto sobre el
n del riesgo document riesgo?
— alertas ado, la ¿Hay
técnicas, arista es registro de
denuncias inferida que esas
recibidas, (A6). comunicaci
informes ones
de otros llegaron?
organismos
(A3/A5).
5. ¿S del Comparaci S alto Reduce ¿Otras
operador ón A3/A4 implica rango de empresas
— las entre las que el S del del mismo
prácticas prácticas problema operador sector, bajo
eran del es del (incertidu el mismo
idiosincrát operador y marco mbre marco,
icas o el estándar regulatorio ontológic actuaron de
estándar del sector : la a) manera
del sector? bajo las reforma diferente?
mismas debe ser ¿El
condicione normativa, operador
s no solo adoptó
regulatorias contra ese reduccione

Taxonomía General de Aplicaciones
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más rango
funciona qué
principal la reduce reduce
preguntar
es… es…
y operador. s de costo
económica S bajo que sus
s. Si otros implica pares no
operadores que las adoptaron?
bajo el decisiones ¿Los
mismo idiosincrát propios
marco icas del ingenieros
actuaron operador del
igual → S eran la operador
alto. Si las condición objetaron
prácticas causal las
del determina decisiones?
operador nte.
eran
inferiores al
estándar →
S
moderado-
bajo.
6. ¿v(S) de Datos de Shapley Determin ¿Hay datos
las monitoreo requiere a la de
coalicione ambiental v(S) para calidad de monitoreo
s — para por zona y cada la que
el cálculo por coalición Declaraci permitan
de período posible. Si ón en el aislar la
Shapley? que solo se análisis contribució
permitan tiene v(N) Shapley n de cada
estimar la (el daño fuente? ¿El
contribució total), modelo de
n de cada Shapley dispersión
fuente en necesita puede
ausencia de estimacion correr
las otras. es escenarios
Modelado contrafácti sin uno o
de cas. varios de
dispersión Cuanto los actores?
por fuente más ¿Hay zonas
individual precisas del
A2. sean las ecosistema
Análisis de estimacion influenciad
superposici es de v(S) as por una
ón parciales, sola fuente

Taxonomía General de Aplicaciones
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más rango
funciona qué
principal la reduce reduce
preguntar
es… es…
geográfica más que sirvan
de zonas de estrecho de
influencia es el referencia?
de cada intervalo
operador. de
confianza
de φᵢ.
7. ¿α del Verificació α mide Reduce ¿Hay
operador n técnica remediaci rango de peritaje
— qué independie ón α del independie
remediaci nte del efectiva, operador nte del
ón real ha estado de no (incertidu estado del
ocurrido? remediació compromi mbre área
n: peritaje sos ni empírica) afectada
del área planes. El después de
remediada peritaje de las medidas
versus el verificació de
área total n del remediació
afectada estado n? ¿La
(A2). post- recuperació
Registros remediaci n del
de pagos a ón es la ecosistema
comunidad fuente de es
es versus evidencia verificable
AD_i para α, no con datos
estimado. las de
Datos de declaracio monitoreo?
monitoreo nes del ¿Los pagos
post- operador. a las
remediació comunidad
n que es son
muestren proporcion
recuperació ales al
n AD_i
verificable estimado?
del
ecosistema.
Árbol de decisión ambiental: ¿qué buscar primero?

Taxonomía General de Aplicaciones
El árbol comienza con la decisión entre R* y Shapley — que
es la más importante y la que condiciona todo el análisis
posterior.
¿Cuál es tu principal incertidumbre?
├─ ¿R* o Shapley — primera decisión del análisis?
│
└─ PRIORIDAD 1: Verificar si algún actor es
condición necesaria del daño.
· Pregunta de diagnóstico: ¿Habría ocurrido el daño sin
este actor dado lo que los otros habrían producido?
· Si NO → R* convencional. Al menos un actor es
condición necesaria. Calcular R* con el grafo completo.
· Si SÍ → Shapley. El daño es acumulativo. Necesitas
estimar v(S) para las coaliciones parciales.
· Si no puedes determinarlo → buscar modelado de
dispersión A2 que corra el escenario sin el actor analizado.
├─ [R* CONVENCIONAL] ¿Sobre la arista entre el emisor
y el punto de daño?
│
└─ PRIORIDAD: Obtener peritaje de dispersión A2.
· Sin modelo de dispersión → arista A7, w en [0.07–
0.24]. Declaración C.
· Con modelo de dispersión → arista A2, w en [0.68–
0.87]. Declaración B probable.
· El modelo debe correr con las condiciones ambientales del
período del daño (dirección del viento, caudales, etc.).
├─ [R* CONVENCIONAL] ¿Sobre R* de la casa matriz —
sus decisiones eran condición causal?
│
└─ PRIORIDAD: Buscar documentos A1 de
decisiones de diseño y estándares de la casa matriz.
· ¿La casa matriz diseñó la tecnología? ¿Aprobó las
reducciones de estándar?
· Comparar con el estándar del sector A4: ¿las decisiones
de la casa matriz estaban por debajo del estándar?

Taxonomía General de Aplicaciones
· Si sí → S bajo de la casa matriz, R*_neta alto. Incluir
como nodo D en el grafo.
├─ [R* CONVENCIONAL] ¿Sobre R* del regulador por
omisión?
│
└─ PRIORIDAD: Verificar los dos elementos de la
omisión simultáneamente.
· Elemento 1 — deber: ¿La normativa establecía
obligación de inspeccionar en el período?
· Elemento 2 — conocimiento: ¿El regulador recibió
alertas, denuncias o informes técnicos sobre el riesgo?
· Si ambos → arista de omisión A1/A3. R* del
regulador significativo. Declaración A o B.
· Si solo uno → arista de omisión A6. Declaración C
para esa arista.
├─ [SHAPLEY] ¿Sobre v(S) de las coaliciones — datos para
el cálculo?
│
└─ PRIORIDAD: Buscar datos de monitoreo que
permitan aislar la contribución de cada fuente.
· ¿Hay zonas del ecosistema influenciadas por una sola
fuente que sirvan de referencia calibrada?
· ¿El modelo de dispersión puede correr escenarios sin uno o
varios actores para estimar v(S) de las coaliciones parciales?
· Si hay datos suficientes → Shapley con Declaración B.
Si las coaliciones parciales requieren estimaciones contrafácticas
con alta incertidumbre → Declaración C.
└─ ¿Sobre α del operador — qué remediación real ha
ocurrido?
└─ PRIORIDAD: Obtener peritaje independiente
del estado de remediación.
· ¿Hay verificación técnica independiente del área
remediada versus el área total afectada?
· ¿Los datos de monitoreo post-remediación muestran
recuperación verificable del ecosistema?

Taxonomía General de Aplicaciones
· ¿Los pagos a comunidades son proporcionales al
AD_i estimado (R*_i × D_total)?
· Declaraciones sin peritaje de verificación no modifican
α. α solo sube con evidencia A1/A2 de la remediación
efectiva.
— Fin del Capítulo 4 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

