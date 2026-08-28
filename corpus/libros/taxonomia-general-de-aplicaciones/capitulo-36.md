## PARTE V · Organizaciones y Gestión

### Capítulo 36
Gestión de proyectos — responsabilidad
en retrasos y sobrecostos
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Nivel A: deriva y amplía los instrumentos del
paradigma para el dominio de la gestión de proyectos y la responsabilidad
en retrasos y sobrecostos. El dominio tiene una característica que lo
distingue de todos los demás capítulos de la Parte V: el daño no se
produce por un evento discreto sino por la acumulación de desviaciones
desde el plan base a lo largo del ciclo de vida del proyecto. Cada decisión
tomada en los nodos de decisión críticos del proyecto —la estimación
inicial, la aprobación del alcance, la gestión de los cambios, la respuesta
ante las alertas de riesgo— tiene R* sobre el retraso o el sobrecosto final.
Si tu caso es de retraso atribuible a estimación inicial deficiente (falacia
de planificación), ve a §1 sub-variante 1 y §5 configuración 1. Si es de
sobrecosto por cambios de alcance no gestionados (scope creep), ve a §5
configuración 2. Si es de incumplimiento del contratista con plan
verificablemente alcanzable, ve a §3 y §5 configuración 3. Para la
prioridad de evidencia, ve directamente a §9.
Nota de calibración: los rangos w de la escala Gp0–Gp8 y los rangos
de α están derivados por extensión desde los principios del sistema, con
referencia a los rangos del cap. 12 (ingeniería de sistemas) para el nodo
de presión y la estructura de decisión crítica. Pendientes de calibración
empírica con datos de arbitrajes de proyectos.
§1 Descripción del subcampo

Taxonomía General de Aplicaciones
La responsabilidad en gestión de proyectos opera sobre un
daño acumulativo con múltiples nodos causales simultáneos y
temporalmente distribuidos que ningún otro capítulo de la
Taxonomía captura con la misma complejidad temporal. El
retraso y el sobrecosto de un proyecto grande no son el
resultado de una decisión única: son la consecuencia de
decenas de decisiones tomadas por actores distintos en
momentos distintos del ciclo de vida, donde cada decisión
aumentó o redujo la probabilidad de alcanzar el resultado
contratado. La imputación del retraso al contratista —el actor
más visible porque es quien no entregó— reproduce la misma
inversión causal que el sistema documentó en Volkswagen y
en Wells Fargo: el nodo más visible puede tener el menor
R*_neta.
La distinción central del dominio es entre tres causas de
retraso o sobrecosto con grafos causales distintos y
distribuciones de R* distintas. La primera es la falacia de
planificación: la estimación inicial era estructuralmente
insuficiente porque ignoró riesgos conocidos, usó datos
históricos de proyectos comparables que también tuvieron
retrasos, o fue optimizada para ganar la licitación en lugar de
reflejar el tiempo y costo reales. La segunda es el scope creep:
el alcance del proyecto creció durante la ejecución por cambios
no gestionados adecuadamente, sin la correspondiente
extensión del plazo y el presupuesto. La tercera es el
incumplimiento genuino del contratista: el plan era alcanzable
con recursos razonables y el contratista no los movilizó con la
calidad y la cantidad adecuadas.
El IPR (Índice de Perturbación del Proyecto) como
instrumento central del dominio
El IPR mide la brecha entre el rendimiento del proyecto y el plan base
verificablemente alcanzable —no el plan base contractual, que puede haber
sido fijado con falacia de planificación. IPR ∈ [0, 1]: IPR = 0 indica
rendimiento en línea con el plan alcanzable; IPR = 1 indica perturbación
máxima del plan alcanzable.

Taxonomía General de Aplicaciones
IPR = (retraso_o_sobrecosto_real −
retraso_o_sobrecosto_del_plan_alcanzable) /
retraso_o_sobrecosto_del_plan_alcanzable
El IPR tiene dos componentes: (a) la perturbación atribuible al plan base
(falacia de planificación o scope creep no gestionado), y (b) la perturbación
atribuible a la ejecución (incumplimiento del contratista respecto al plan
alcanzable). La distribución del R* entre el dueño del proyecto, el director de
proyecto y el contratista es proporcional a la fracción del IPR causalmente
atribuible a cada uno.
AD_nodo = R*_nodo × D_proyecto × (1 − α_nodo) donde
D_proyecto = costo_del_retraso + sobrecosto_directo +
daño_indirecto
Sub-variantes del dominio
Sub-variante Descripción y singularidades del dominio
Retraso por falacia El plan base del proyecto contenía estimaciones
de planificación en de plazo y costo estructuralmente insuficientes
la estimación inicial porque el dueño del proyecto o el director de
proyecto ignoraron riesgos conocidos, usaron
datos históricos de proyectos que también
tuvieron retrasos significativos, o fijaron el plan
base para ganar la licitación en lugar de reflejar el
tiempo y costo alcanzables con los recursos
disponibles. La falacia de planificación es el error
de categoría más frecuente en proyectos grandes:
el plan era optimista por diseño, no por
incompetencia del contratista. El R* del dueño
del proyecto y del director de proyecto sobre el
retraso es alto cuando el plan base irrealista era
una condición del contrato.
Sobrecosto por El alcance del proyecto creció durante la
scope creep no ejecución por cambios solicitados por el dueño
gestionado del proyecto —modificaciones de diseño,
adiciones de funcionalidad, cambios regulatorios
que el dueño no anticipó— sin la
correspondiente extensión formal del plazo y el
presupuesto. El scope creep es la causa más
frecuente de sobrecosto en proyectos de

Taxonomía General de Aplicaciones
Sub-variante Descripción y singularidades del dominio
tecnología de la información y en proyectos de
construcción con especificaciones técnicas
complejas. El R* del dueño del proyecto sobre el
sobrecosto es positivo cuando los cambios de
alcance fueron aprobados por él sin aprobación
simultánea de los recursos adicionales.
Incumplimiento El plan base era verificablemente alcanzable con
del contratista los recursos razonables del contratista — la
respecto al plan estimación era realista, el alcance estaba definido
alcanzable y no cambió significativamente — y el contratista
no movilizó los recursos en la calidad y la
cantidad necesarias, no gestionó adecuadamente
las interdependencias entre actividades, o tomó
decisiones técnicas que produjeron retrabajo
evitable. Es la sub-variante donde el
R*_contratista es dominante. Se conecta con el
cap. 12 (ingeniería de sistemas) para los proyectos
donde el incumplimiento produjo fallos de
seguridad.
Retraso por riesgo Un riesgo identificado o identificable del
materializado sin proyecto se materializó sin que el plan de
gestión de riesgo proyecto incluyera un plan de respuesta
adecuada adecuado: riesgos climáticos, riesgos regulatorios,
riesgos de disponibilidad de materiales o de
recursos especializados. El R* del director de
proyecto sobre el retraso producido por el riesgo
materializado es positivo cuando el plan de
gestión de riesgo era inadecuado respecto a los
riesgos que el estado del arte de la gestión de
proyectos requería identificar y mitigar en el
período.
Retraso por El dueño del proyecto o la dirección fijaron un
presión de plazo plazo de entrega que los análisis internos
que ignoró las mostraban como insuficiente, y presionaron para
señales de riesgo mantenerlo ignorando las alertas del director de
proyecto o del contratista. Es el patrón del
Challenger en el dominio de proyectos: la presión
para cumplir el hito produjo que las señales de
riesgo fueran ignoradas. El R* del dueño del
proyecto sobre el retraso es alto cuando la
presión de plazo fue la condición que determinó
que las señales no produjeran corrección del plan.

Taxonomía General de Aplicaciones
Sub-variante Descripción y singularidades del dominio
Se conecta directamente con el cap. 12 (ingeniería
de sistemas) para el nodo de presión.
Reclamación de El análisis de responsabilidad se produce en el
retraso y contexto de una disputa contractual entre las
sobrecosto entre partes: el dueño reclama al contratista por
partes del contrato incumplimiento, el contratista reclama al dueño
por causas de retraso que le son atribuibles. El
instrumento central es el análisis de impacto del
cronograma (schedule impact analysis) que
establece qué fracción del retraso total es
causalmente atribuible a cada parte. El grafo del
proyecto es el instrumento de arbitraje de la
reclamación.
§2 Escala de evidencia Gp0–Gp8 · Gestión de
proyectos
La escala Gp0–Gp8 traduce la jerarquía general E0–E8 al
vocabulario de la gestión de proyectos y el análisis de
responsabilidad en retrasos y sobrecostos. Su característica
más relevante es la posición del análisis del cronograma (Gp2)
— el instrumento que establece el IPR y su descomposición
entre las causas atribuibles a cada parte — y del análisis forense
del plan base (Gp2) que establece si el plan era
verificablemente alcanzable. Sin el plan base alcanzable como
referencia, el IPR no tiene base y el análisis de responsabilidad
no puede distribuir el R* entre las partes.
Descripción y ejemplos
Rango
Nivel Tipo de evidencia en el dominio de gestión
w
de proyectos
Gp1 Plan base Plan de proyecto con [0.72,
verificablemente estimaciones respaldadas 0.90]
alcanzable con datos por datos históricos de
de proyectos proyectos comparables
comparables + terminados, con análisis de
análisis forense del los factores de diferencia

Taxonomía General de Aplicaciones
Descripción y ejemplos
Rango
Nivel Tipo de evidencia en el dominio de gestión
w
de proyectos
cronograma + entre el proyecto analizado
registros de decisión y los comparables; análisis
en los nodos críticos forense del cronograma por
experto en gestión de
proyectos que establece la
evolución del retraso desde
el plan base hasta la
terminación, identificando
los eventos que lo
produjeron y el momento
en que cada actor tuvo la
primera señal de que el plan
estaba en riesgo; registros
de las decisiones tomadas
en los nodos de decisión
críticos del proyecto —
aprobación del plan base,
decisiones de cambio de
alcance, respuestas ante
alertas de riesgo.
Gp2 Análisis del Análisis pericial del [0.60,
cronograma por cronograma que establece 0.80]
experto en el IPR total y su
programación de descomposición entre las
obras + análisis de la causas atribuibles a cada
distribución de parte (método de análisis de
causas de retraso + impacto del cronograma:
comparación con time impact analysis o
proyectos de windows analysis);
referencia comparación del plan base
con el rendimiento de
proyectos comparables que
establece si la estimación
inicial era alcanzable dado
el estado del arte; análisis de
la gestión de cambios de
alcance que establece cuáles
cambios fueron aprobados
por el dueño sin ajuste
correspondiente de plazo y
presupuesto.

Taxonomía General de Aplicaciones
Descripción y ejemplos
Rango
Nivel Tipo de evidencia en el dominio de gestión
w
de proyectos
Gp3 Registros del Registros completos del [0.46,
proyecto (actas, proyecto que muestran la 0.64]
correos, informes de evolución del cronograma
avance) + análisis durante la ejecución, las
del cronograma alertas de riesgo emitidas
actualizado + por el director de proyecto
registro de cambios o el contratista, las
de alcance decisiones de respuesta del
dueño ante esas alertas, y el
historial de cambios de
alcance aprobados; análisis
del cronograma con los
datos de avance real que
establece la magnitud del
retraso en cada período y
los eventos que lo explican.
Gp4 Informes de avance Informes de avance [0.36,
del proyecto + actas periódicos que documentan 0.56]
de reuniones de el estado del cronograma y
seguimiento + el presupuesto en cada
contratos y adendas período de reporte; actas de
las reuniones de
seguimiento que muestran
las decisiones tomadas ante
las alertas de riesgo;
contratos y adendas que
documentan los cambios de
alcance aprobados y su
tratamiento en cuanto al
plazo y el presupuesto.
Gp5 Comparación entre La diferencia entre el plazo [0.26,
el plan base y el y el costo del plan base y el 0.44]
resultado sin análisis plazo y el costo real al cierre
forense del del proyecto, sin análisis
cronograma forense que establezca las
causas del diferencial y su
atribución a cada parte.
Gp6 Inferencia desde el El tipo de proyecto y el [0.14,
patrón de retrasos de sector de la industria 0.28]
la industria y el tipo permiten inferir que el plan
de proyecto base era probable que

Taxonomía General de Aplicaciones
Descripción y ejemplos
Rango
Nivel Tipo de evidencia en el dominio de gestión
w
de proyectos
subestimara el plazo real,
sin análisis del proyecto
específico.
Gp7 Correspondencia Las comunicaciones entre [0.06,
entre las partes sobre las partes muestran el 0.20]
el retraso sin análisis desacuerdo sobre las causas
del cronograma del retraso sin análisis
técnico del cronograma que
establezca la distribución
causal.
Gp8 Afirmación de una La afirmación de una de las [0.02,
parte sobre las partes del contrato sobre 0.12]
causas del retraso sin las causas del retraso sin
evidencia técnica del análisis pericial del
cronograma cronograma ni registros del
proyecto que la respalden.
Gp0 Ausencia Análisis Gp2 que establece w =
documentada de que el retraso o sobrecosto 0.00
nexo causal entre la es causalmente atribuible a
conducta del nodo factores exógenos a las
analizado y el retraso partes del contrato —
o sobrecosto eventos de fuerza mayor
documentados, cambios
regulatorios imprevisibles
— o que la parte analizada
cumplió plenamente con
sus obligaciones
contractuales y el retraso
fue producido
exclusivamente por la otra
parte.
§3 Firmas documentales por Hijo
Los Hijos de Afrodita aplican en el dominio de la gestión de
proyectos a los actores con voluntad propia: el dueño del
proyecto que aprobó el plan base y tomó las decisiones de

Taxonomía General de Aplicaciones
cambio de alcance, el director de proyecto que diseñó el plan
base y gestionó los riesgos, el contratista que ejecutó, y la
dirección que fijó los plazos bajo presión. La distinción más
relevante del dominio es entre el Fobos del director de
proyecto que fijó un plan base optimista para ganar la licitación
o complacer al dueño y el Deimos genuino del director que
subestimó el plazo en buena fe porque los datos de proyectos
comparables también eran optimistas.
§3.1 Hijos de legibilidad alta en el dominio de proyectos
Qué
Error de
informa Firma Fuente
Hijo discrimina
para S del documental típica
ción
actor
Anter S muy bajo Análisis Registros Confundir
os [0.03, 0.22]. internos que internos del con Potós
El dueño del mostraban proceso de cuando el
proyecto, el plazos y elaboración director de
director de costos del plan proyecto
proyecto o el significativam base. usó las
directivo que ente Correos de estimacione
fijó el plazo superiores al la dirección s estándar
sabía que el plan base sobre los del sector
plan era aprobado, sin objetivos del período
insuficiente que eso del plan. sin análisis
—los análisis produjera Comparaci específico
internos lo ajuste del ones de los
mostraban plan. Correos históricas riesgos del
— y donde la de proyecto
deliberadam dirección proyectos concreto. La
ente aprobó instruyó al del mismo pregunta: ¿el
un plan director de tipo en la director
optimista proyecto a organizació tenía
para ganar la reducir la n. información
licitación, estimación específica de
satisfacer al para cumplir que su
cliente, o con el proyecto
mantener la presupuesto tenía
aprobación o el plazo característic
política del requerido. as que lo
proyecto. El Comparacion hacían más
Anteros en es con difícil que el
proyectos es proyectos promedio
el patrón de similares que histórico del
los mostraban sector?

Taxonomía General de Aplicaciones
Qué
Error de
informa Firma Fuente
Hijo discrimina
para S del documental típica
ción
actor
megaproyect que el plan
os públicos base era
donde el estadísticame
plan base se nte
construye improbable,
para pasar el sin que eso
filtro produjera
político, no revisión.
para reflejar
el costo y el
plazo reales.
El
isomorfismo
con el
Challenger:
la presión
política para
cumplir un
hito hace que
las señales de
riesgo sean
ignoradas
deliberadam
ente.
Potós S moderado- Plan base Datos Confundir
alto [0.42, construido históricos con Anteros
0.72]. El con datos del sector cuando el
director de históricos de sobre director
proyecto o el proyectos plazos y tenía análisis
dueño comparables costos de paramétrico
usaron los sin análisis de proyectos s o de
datos los riesgos similares. El riesgos
históricos de específicos plan base específicos
proyectos del proyecto del que
comparables concreto que proyecto. indicaban la
del sector — lo hacían más La ausencia insuficiencia
que también difícil. de un del plan y los
tenían sesgos Ausencia de registro de ignoró. Con
optimistas un registro de riesgos Deimos
sistémicos— riesgos con validado. cuando
para probabilidade genuinamen
construir el s e impactos te no había
plan base, sin estimados datos de

Taxonomía General de Aplicaciones
Qué
Error de
informa Firma Fuente
Hijo discrimina
para S del documental típica
ción
actor
ajustar por antes del proyectos
los riesgos inicio de la comparables
específicos ejecución. para la
del proyecto Uso de estimación
concreto. El estimaciones paramétrica.
Potós en análogas sin
proyectos es verificación
el sesgo de paramétrica.
planificación
sistémico del
sector: si
todos los
proyectos
del tipo se
retrasan en
promedio un
30%, el
director que
usa el
promedio
histórico sin
ajuste por los
riesgos del
proyecto
específico
reproduce el
sesgo sin
haber
tomado una
decisión
idiosincrática
de ser
optimista.
Fobo S moderado Propuestas Registros Confundir
s [0.32, 0.60]. con plazos de la con Potós
El director significativam propuesta cuando el
de proyecto ente técnica. director usó
adoptó un inferiores a Comparaci metodología
plan base los de los ón con las s de
que sabía era competidores propuestas estimación
optimista, sin de los estándar del
motivado justificación competidor sector que
por el miedo técnica de la es. Historial producen

Taxonomía General de Aplicaciones
Qué
Error de
informa Firma Fuente
Hijo discrimina
para S del documental típica
ción
actor
a perder la diferencia. de sesgo
licitación o a Correos o proyectos optimista
que el comunicacio del sistémico sin
proyecto nes que contratista. que el
fuera muestran que director
cancelado si el director era fuera
el plan consciente de consciente
realista que el plazo del sesgo
superaba el era específico
presupuesto insuficiente de su
disponible antes de propuesta.
del dueño. El presentar la
Fobos en propuesta.
proyectos Proyectos del
produce el mismo
plan base director o
deshonesto- empresa
racional: el donde el
director sabe patrón se
que el plazo repite.
es
insuficiente,
pero
propone el
que el dueño
quiere
escuchar
porque de
otro modo el
proyecto no
sería
aprobado.
Es la versión
organizacion
al de la
trampa en la
que el
contratista
entra cuando
el mercado
de
licitaciones
premia los

Taxonomía General de Aplicaciones
Qué
Error de
informa Firma Fuente
Hijo discrimina
para S del documental típica
ción
actor
planes más
optimistas.
Deim S alto [0.58, Registro de El registro Confundir
os 0.86]. El riesgos previo de riesgos con Potós
director de a la ejecución pre- cuando la
proyecto no que no incluía ejecución falta de
anticipó los el riesgo que del identificació
riesgos que materializó el proyecto. n del riesgo
materializaro retraso, con Proyectos fue
n el retraso justificación comparable consecuenci
porque de por qué s del sector a de no
genuinament ese riesgo no y su haber
e no disponía era tratamiento realizado el
de los datos identificable del mismo análisis de
para con el análisis riesgo. riesgos que
identificarlos disponible en el estado del
o porque los el período. arte del
riesgos eran Proyectos período
de un tipo comparables requería.
que el estado del sector que
del arte de la tampoco
gestión de identificaron
riesgos del el mismo
período no riesgo.
requería Respuesta
anticipar. El rápida y
Deimos transparente
genuino en ante la
proyectos: el materializació
riesgo que n del riesgo.
materializó el
retraso no
estaba en la
literatura de
riesgos del
tipo de
proyecto en
el período, o
las
característica
s del
proyecto lo
hacían

Taxonomía General de Aplicaciones
Qué
Error de
informa Firma Fuente
Hijo discrimina
para S del documental típica
ción
actor
genéricamen
te difícil de
estimar con
los datos
disponibles.
§3.2 El nodo de presión de plazo: el patrón del Challenger en
proyectos
El nodo de presión de plazo en proyectos es el equivalente funcional del
nodo de presión política en el Challenger (cap. 12): el actor que fijó un
hito de entrega inamovible bajo presión política, comercial o contractual,
ignorando las alertas del director de proyecto y del contratista sobre la
insuficiencia del plazo. La frase que define el patrón en proyectos es el
equivalente de «ponte el sombrero de gestión»: la dirección que instruye
al director de proyecto a mantener el plan, aunque los riesgos hagan su
cumplimiento improbable.
El R* del nodo de presión de plazo sobre el retraso es positivo cuando:
(a) las alertas del director de proyecto estaban documentadas y fueron
ignoradas; y (b) el incumplimiento del hito habría producido la revisión
del plan si las alertas hubieran sido atendidas. El S del nodo de presión
es moderado-bajo cuando la presión fue idiosincrática de ese directivo
específico — ningún otro directivo en esa posición habría mantenido el
plazo ante las mismas alertas.
§4 Escala de α con la tabla de acciones que
cuentan
α_dueño · α_director_de_proyecto · α_contratista: tres
nodos con lógica distinta
α_dueño mide el grado en que el dueño del proyecto generó las condiciones para
la ejecución exitosa: la definición completa del alcance antes del inicio, la

Taxonomía General de Aplicaciones
gestión de los cambios con el ajuste correspondiente de plazo y presupuesto, la
respuesta oportuna ante las alertas del director y el contratista, y la provisión
de los insumos del proyecto bajo responsabilidad del dueño (permisos, acceso
al sitio, información técnica) en los plazos del plan.
α_director_de_proyecto mide la calidad del plan base (realismo de las
estimaciones, robustez del registro de riesgos, adecuación de los márgenes de
contingencia), de la gestión del cronograma (seguimiento de la ruta crítica,
gestión de las interdependencias, respuesta ante desviaciones), y de la
comunicación de las alertas a las partes relevantes.
α_contratista mide la movilización de recursos en la calidad y la cantidad del
plan, la gestión de los subcontratistas y proveedores críticos, el rendimiento en
las actividades de la ruta crítica, y la comunicación oportuna de las alertas de
riesgo.
Nivel de α
α en el dominio
Conducta que típico en
Nodo de gestión de
sube α desempeño
proyectos
deficiente
Dueño del Alcance definido Especificacion 0.05–0.20 para
proyecto completamente es técnicas dueños que
(ND) antes del inicio completas y aprobaron
con verificadas cambios de
especificaciones antes de la alcance sin
técnicas firma del ajuste de plazo
verificadas; contrato. y presupuesto
proceso de Proceso de manera
gestión de documentado sistemática.
cambios que de gestión de 0.10–0.30 para
evalúa el impacto cambios con dueños que no
en plazo y análisis de respondieron
presupuesto impacto en en plazo a los
antes de aprobar plazo y requerimiento
cada cambio; presupuesto s de
provisión en previo a la información
plazo de los aprobación. del contratista
insumos bajo Provisión de que estaban en
responsabilidad permisos, la ruta crítica.
del dueño; acceso y
respuesta dentro documentos
del plazo técnicos dentro
contractual ante de los plazos

Taxonomía General de Aplicaciones
Nivel de α
α en el dominio
Conducta que típico en
Nodo de gestión de
sube α desempeño
proyectos
deficiente
los del plan.
requerimientos Revisión del
de información plan base
del contratista; cuando las
aceptación de la alertas del
revisión del plan director de
cuando las alertas proyecto
del director o del mostraban que
contratista lo el plan era
justificaban. inalcanzable.
Director de Plan base con Plan base 0.05–0.20 para
proyecto estimaciones aprobado con directores con
(DDP) verificadas por análisis Anteros: plan
datos de paramétrico base
proyectos documentado y construido
comparables y registro de para
análisis de riesgos riesgos con complacer al
documentado; probabilidades dueño en lugar
registro de e impactos de reflejar el
riesgos estimados. plazo
actualizado Seguimiento alcanzable.
durante la semanal de la 0.20–0.45 para
ejecución con ruta crítica con directores con
respuesta ante la informes Potós: plan sin
materialización documentados análisis de
de cada riesgo; de estado del riesgos
seguimiento cronograma. específico del
semanal de la ruta Alerta escrita al proyecto.
crítica con alerta dueño cuando 0.45–0.65 para
documentada al el cronograma directores que
dueño cuando el tenía riesgo de no emitieron
plan estaba en incumplir el alertas
riesgo; gestión de hito con plazo oportunas ante
las suficiente para las
interdependencia la corrección. desviaciones
s entre Gestión del
actividades con documentada cronograma.
acciones de los cambios
preventivas ante de alcance con
los retrasos impacto en el
potenciales. cronograma.

Taxonomía General de Aplicaciones
Nivel de α
α en el dominio
Conducta que típico en
Nodo de gestión de
sube α desempeño
proyectos
deficiente
Contratista Movilización de Movilización 0.05–0.20 para
(DC) recursos en la documentada contratistas
calidad y la del personal y que no
cantidad del plan los equipos en movilizaron
en las fechas las fechas del los recursos
comprometidas; plan. comprometid
rendimiento en Rendimiento os en las
las actividades de en la ruta crítica fechas del plan
la ruta crítica verificable sin causa
dentro de los desde los exógena
rendimientos del registros documentada.
plan; gestión de diarios de 0.20–0.45 para
subcontratistas y producción. contratistas
proveedores Informes de que
críticos con estado del gestionaron
colchones cronograma al los
adecuados para director de subcontratista
las proyecto con s críticos con
interdependencia indicadores de retrasos
s; comunicación desviación. sistémicos sin
oportuna de las Comunicación acciones
alertas de riesgo inmediata de correctoras.
con propuestas los eventos que 0.45–0.70 para
de solución; afectan el contratistas
retrabajo mínimo cronograma que no
por errores de con análisis de comunicaron
calidad. impacto y las alertas de
propuesta de riesgo en el
recuperación. plazo que
habría
permitido la
corrección.
Subcontratist El subcontratista Las mismas que Las mismas
a crítico que ejecuta para el que para el
(DSC) actividades de la contratista, contratista,
ruta crítica tiene aplicadas a las con la
R* directo sobre actividades del distinción de
el retraso cuando subcontratista que el
su específico. contratista
incumplimiento principal tiene
fue condición R* adicional
necesaria del por la gestión
retraso del

Taxonomía General de Aplicaciones
Nivel de α
α en el dominio
Conducta que típico en
Nodo de gestión de
sube α desempeño
proyectos
deficiente
proyecto. El del
análisis del R* del subcontratista.
subcontratista
sigue la misma
lógica que el del
contratista
principal, con la
distinción
adicional de que
el R* del
contratista
principal sobre el
rendimiento del
subcontratista es
positivo cuando
la selección, la
dirección y el
seguimiento del
subcontratista
fue inadecuada.
La falacia de planificación: cuando el plan base era la
causa del retraso
Nivel de realismo Descripción del plan base y su relación con
del plan base el IPR
Plan optimista por El plan base fue construido para ganar la
diseño licitación o para satisfacer el presupuesto
(Fobos/Anteros del disponible del dueño, no para reflejar el plazo y
director) costo reales. El IPR del contratista respecto a
este plan es positivo pero el R* del IPR es
mayoritariamente del director de proyecto y del
dueño que aprobaron el plan. La desviación del
contratista respecto al plan irreal no es evidencia
de incumplimiento: es evidencia de que el plan
era irreal.
Plan con sesgo El plan base fue construido con datos históricos
optimista sistémico del sector que tienen sesgo optimista sistémico
documentado — si el promedio histórico del

Taxonomía General de Aplicaciones
Nivel de realismo Descripción del plan base y su relación con
del plan base el IPR
del sector (Potós del tipo de proyecto tiene retrasos del 30%, el plan
director) que usa el promedio sin ajuste tiene sesgo
optimista sistémico. El R* del IPR es
compartido entre el director (por no ajustar por
los riesgos específicos del proyecto) y el sector
(por producir datos históricos sesgados).
Plan realista con El plan base era realista dado el análisis de
riesgos no riesgos disponible, pero un riesgo no
identificados identificable con el análisis del período se
(Deimos del materializó. El IPR del contratista respecto al
director) plan es positivo por la materialización del riesgo,
pero el R* del director es bajo porque la falta de
identificación del riesgo no fue negligente. El R*
del riesgo materializado se desplaza a los
factores exógenos.
Plan realista con El plan base era realista, el registro de riesgos
riesgos identificados identificaba los riesgos relevantes con planes de
y gestionados respuesta, y el director de proyecto ejecutó los
(Harmonía del planes de respuesta ante cada riesgo
director) materializado. El IPR del contratista respecto al
plan es positivo solo por el incumplimiento
genuino del contratista — no por la falacia de
planificación ni por los riesgos. α_director ≈
1.00.
§5 Tipos de nodo, tipos de arista y
configuraciones canónicas del dominio
Tipos de nodo en el grafo de gestión de proyectos
R* en el
Tipo de Función en el grafo de
S típico
nodo grafo retraso o
sobrecosto
Dueño del Definió el Variable: S bajo R*_ND ×
proyecto alcance, aprobó [0.08–0.30] D_proyecto ×
(ND) el plan base, cuando las (1 − α_ND).

Taxonomía General de Aplicaciones
R* en el
Tipo de Función en el grafo de
S típico
nodo grafo retraso o
sobrecosto
gestionó los decisiones que El R*_ND
cambios y produjeron el sobre el scope
proveyó los retraso fueron creep es
insumos del idiosincráticas del proporcional a
proyecto bajo su dueño específico. la fracción del
responsabilidad. S moderado-alto retraso
R* positivo sobre [0.42–0.68] causalmente
el retraso cuando el scope atribuible a los
atribuible al creep era el patrón cambios de
scope creep no de la organización alcance no
gestionado, a los en todos sus compensados
insumos no proyectos. con ajuste de
provistos en plazo y
plazo y a la presupuesto.
presión de plazo
que ignoró las
alertas del
director.
Director Diseñó el plan S alto [0.55–0.82] R*_DDP ×
de base, gestionó el cuando la falacia D_proyecto ×
proyecto cronograma y los de planificación (1 − α_DDP).
(DDP) riesgos, y era el patrón del El R*_DDP
comunicó las sector (cualquier sobre la falacia
alertas. R* director habría de
positivo sobre el construido el planificación
retraso atribuible mismo plan). S es
a la falacia de bajo [0.05–0.30] proporcional a
planificación cuando el plan fue la fracción del
(plan base construido IPR atribuible
irrealista), a la deliberadamente al plan base
gestión optimista para irreal — la
inadecuada de los ganar la licitación. diferencia
riesgos entre el plan
identificables, y a base
la falta de alertas contractual y
oportunas. el plan
alcanzable.
Contratista Ejecutó el Variable: S alto R*_DC ×
(DC) proyecto [0.55–0.80] D_proyecto ×
movilizando los cuando el (1 − α_DC).
recursos incumplimiento El R*_DC se
comprometidos y fue sistémico del calcula

Taxonomía General de Aplicaciones
R* en el
Tipo de Función en el grafo de
S típico
nodo grafo retraso o
sobrecosto
gestionando los sector para ese respecto al
subcontratistas. tipo de proyecto plan
R* positivo sobre (cualquier alcanzable, no
el retraso contratista en esas al plan base
atribuible al condiciones contractual. Si
incumplimiento habría tenido el el plan base
del contratista mismo era irreal,
respecto al plan incumplimiento). R*_DC sobre
alcanzable — no S bajo [0.08–0.35] el retraso
respecto al plan cuando el respecto al
base irreal. incumplimiento plan base es
fue idiosincrático bajo.
del contratista
específico.
Nodo de El directivo que S bajo-moderado Fracción del
presión de fijó el hito [0.15–0.42] D_proyecto
plazo inamovible bajo cuando la presión atribuible al
(NPP) presión política o fue idiosincrática retraso que
comercial, de ese directivo. S habría sido
ignorando las moderado-alto evitable si la
alertas del [0.45–0.68] presión de
director de cuando la presión plazo hubiera
proyecto y del de plazo era el permitido
contratista. R* patrón sistémico atender las
positivo sobre el de la alertas y
retraso organización. revisar el plan.
producido
después del
momento en que
las alertas habrían
permitido la
corrección si
hubieran sido
atendidas.
Factores Los eventos N/A — no son La fracción
exógenos fuera del control actores con del
(NE) de todas las voluntad. D_proyecto
partes: fuerza no atribuible a
mayor, cambios ninguna parte
regulatorios reduce el
imprevisibles, D_atribuible
condiciones del que se

Taxonomía General de Aplicaciones
R* en el
Tipo de Función en el grafo de
S típico
nodo grafo retraso o
sobrecosto
sitio radicalmente distribuye
distintas a las entre los
reveladas en los nodos con R*
estudios de suelo. positivo.
No tienen R* en
sentido de
responsabilidad,
pero su
materialización
determina la
fracción del IPR
que no es
atribuible a
ninguna de las
partes.
Configuraciones canónicas del dominio
Configuración 1 — Retraso por falacia de planificación: el
contratista que no causó el retraso del plan irreal
ND (dueño que fijó el presupuesto y el plazo que el proyecto políticamente
tenía que cumplir, sin análisis de la factibilidad: Anteros si sabía que el plan
era insuficiente; Potós si usó el promedio del sector sin análisis específico) +
DDP (director de proyecto que construyó el plan base para cumplir el
presupuesto y el plazo del dueño en lugar de reflejar el tiempo y costo reales:
Fobos si fue para ganar la licitación; Potós si siguió las metodologías estándar
del sector) + DC (contratista que ejecutó con los recursos del plan base y
produjo el retraso respecto al plan irreal: Deimos porque no identificó que el
plan era irreal antes de firmar el contrato) → Retraso del proyecto respecto
al plan base irreal
El instrumento central: el análisis comparativo del plan base con proyectos
comparables terminados establece si el plan era verificablemente alcanzable.
Si el promedio histórico del tipo de proyecto en el sector tenía retrasos del 30%,
y el plan base no incluía un margen de contingencia para ese riesgo sistémico,
el plan era optimista por diseño y el R* del retraso respecto al plan base es
del DDP y del ND — no del DC.

Taxonomía General de Aplicaciones
Configuración 2 — Sobrecosto por scope creep: el dueño que
aprobó cambios sin ajuste de recursos
ND (dueño que aprobó cambios de alcance durante la ejecución —cambios
de diseño, adiciones de funcionalidad, cambios de especificaciones técnicas—
sin el ajuste correspondiente de plazo y presupuesto: Potós si la gestión sin
ajuste era el patrón de la organización; Anteros si el dueño conocía que los
cambios requerían ajuste y deliberadamente no lo tramitó para evitar la
revisión del presupuesto aprobado) + DC (contratista que ejecutó los cambios
aprobados sin el presupuesto adicional, generando sobrecosto no gestionado)
→ Sobrecosto atribuible al scope creep del ND
El análisis de responsabilidad distingue entre los cambios de alcance
aprobados explícitamente por el dueño (R*_ND positivo sobre el sobrecosto
derivado), los cambios de alcance implícitos en las especificaciones originales
que el contratista debía haber anticipado (R*_DC positivo), y los cambios
derivados de errores de diseño del proyecto que no eran obligación del
contratista prever (R*_DDP positivo por el plan con errores de diseño).
Configuración 3 — Incumplimiento genuino del contratista
con plan verificablemente alcanzable
DC (contratista con plan verificablemente alcanzable que no movilizó los
recursos comprometidos: Anteros si la no movilización fue deliberada —el
contratista asignó los recursos a un proyecto más rentable—; Potós si siguió
las prácticas del sector que sistemáticamente subcontratan en exceso; Deimos
si el rendimiento de los recursos fue genuinamente inferior al esperado por
causas no previsibles) + DDP (director de proyecto con Harmonía: alertas
oportunas, seguimiento de la ruta crítica, acciones correctoras propuestas) →
Retraso atribuible al incumplimiento del DC respecto al plan alcanzable
En esta configuración, la prueba del R*_DC es la comparación entre el
rendimiento real de los recursos movilizados por el DC y el rendimiento del
plan alcanzable. Si el DC movilizó 60% de los recursos comprometidos y el
rendimiento de esos recursos era el planificado, el retraso es atribuible a la
movilización insuficiente, no al rendimiento de los recursos. El análisis del
cronograma en ventanas (windows analysis) establece cuánto del retraso

Taxonomía General de Aplicaciones
ocurrió en cada período y quién tenía R* sobre las actividades retrasadas en
ese período.
§6 Preguntas que responde este capítulo
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
¿El plan base era Análisis comparativo del Declaración A si hay
verificablemente plan base con datos datos de proyectos
alcanzable — la históricos de proyectos comparables
falacia de comparables terminados terminados con
planificación del sector: ¿el plazo y el análisis estadístico del
contribuyó al costo del plan base plazo y costo real vs.
retraso? estaban dentro del rango plan base (Gp1).
histórico de proyectos de Declaración B con
complejidad equivalente? análisis pericial del
¿El registro de riesgos del plan base comparado
plan base incluía los con los datos del
riesgos que el sector sector (Gp2).
documenta Declaración C
sistemáticamente para cuando el plan
ese tipo de proyecto? La alcanzable debe
diferencia entre el plan estimarse desde los
base contractual y el plan datos disponibles sin
alcanzable estimado es la un análisis estadístico
fracción del IPR robusto de proyectos
atribuible a la falacia de comparables.
planificación.
¿El retraso fue Análisis del historial de Declaración A si hay
causado por cambios de alcance: un registro de
scope creep no ¿cuántos cambios fueron cambios de alcance
gestionado — aprobados por el dueño? documentado con la
cuál es el R* del ¿Cuáles tuvieron ajuste aprobación del dueño
dueño? correspondiente de plazo y el análisis de
y presupuesto? ¿Cuál es el impacto para cada
impacto acumulado en el cambio (Gp1).
cronograma de los Declaración B con
cambios sin ajuste? La análisis del contrato y
fracción del retraso las adendas que
atribuible al scope creep muestran los cambios
sin ajuste es el R*_ND aprobados sin ajuste

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
sobre ese componente de plazo y
del retraso. presupuesto (Gp2).
Declaración C
cuando el scope creep
debe inferirse desde
las diferencias entre el
alcance inicial y el
alcance ejecutado sin
un registro de
cambios.
¿El contratista Análisis del cronograma Declaración A con
incumplió en ventanas que establece análisis del
respecto al plan la distribución de causas cronograma en
alcanzable — del retraso período por ventanas (windows
cuál es el período: ¿en qué analysis) y registros
IPR_DC? períodos el retraso fue diarios de producción
causado por actividades del DC (Gp1).
bajo control del DC? ¿El Declaración B con
rendimiento de los análisis pericial del
recursos movilizados por cronograma y
el DC fue inferior al del registros de avance
plan alcanzable? El del proyecto (Gp2).
IPR_DC es la fracción Declaración C
del IPR total causalmente cuando el IPR_DC
atribuible al debe estimarse desde
incumplimiento del DC los informes de
respecto al plan avance sin acceso a
alcanzable. los registros diarios de
producción.
¿Hay un nodo de Análisis de las Declaración A si hay
presión de plazo comunicaciones entre el correos o actas de
— la presión nodo de presión y el reuniones donde el
produjo que las director de proyecto o el nodo de presión
alertas fueran contratista: ¿hay alertas ignoró explícitamente
ignoradas? documentadas de riesgo las alertas
al cronograma que el documentadas (Gp1).
nodo de presión ignoró? Declaración B con
¿El nodo de presión análisis del historial
instruyó al director a de comunicaciones
mantener el plan a pesar entre el nodo de
de las alertas? ¿El retraso presión y el director
habría sido evitable si las de proyecto (Gp2).
alertas hubieran Declaración C
cuando la presión de

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
producido la revisión del plazo debe inferirse
plan? desde la ausencia de
revisión del plan ante
alertas documentadas.
¿Cuál es el D_proyecto = Declaración B con
D_proyecto total costo_del_retraso + análisis del
y cómo se sobrecosto_directo + D_proyecto desde los
distribuye el AD daño_indirecto. El costo registros contables
entre los nodos? del retraso incluye los del proyecto y el
costos financieros del análisis del
capital invertido durante cronograma (Gp2).
el período adicional, los Declaración A con
ingresos perdidos acceso a los registros
durante el período de financieros
retraso y los costos completos del
contractuales de proyecto más el
penalización por retraso. análisis del
El AD_nodo = R*_nodo cronograma en
× D_proyecto × (1 − ventanas (Gp1).
α_nodo) para cada nodo
del grafo.
§7 Traducción de D_total al dominio de
gestión de proyectos
D_proyecto = D_retraso + D_sobrecosto + D_indirecto
El daño en gestión de proyectos tiene tres componentes que deben calcularse
separadamente porque tienen nodos causales distintos y contrafácticos
distintos. El D_retraso es el daño producido por el tiempo adicional de
ejecución: los costos financieros del capital invertido durante el período
adicional, los ingresos perdidos durante el período de retraso, y los costos de
las penalizaciones contractuales. El D_sobrecosto es el daño producido por el
costo superior al presupuesto del plan alcanzable — no del plan base irreal.
El D_indirecto es el daño a terceros producido por el retraso del proyecto: el
perjuicio a los beneficiarios del proyecto que no pudieron usar la
infraestructura durante el período de retraso.

Taxonomía General de Aplicaciones
En el
dominio
Fuente
de
Compo de
gestión Cómo se cuantifica
nente evidenci
de
a
proyecto
s
D_retra El daño D_retraso = Registro
so producid (días_de_retraso_respecto_al_pla s
(costo o por la n_alcanzable) × contable
del extensión (costo_diario_de_los_recursos_d s del
tiempo del plazo el_proyecto) + proyecto
adiciona de (ingresos_perdidos_por_día × (costos
l de ejecución días_de_retraso) + reales
ejecució más allá penalizaciones_contractuales. El por
n) del plan costo diario de los recursos del período).
alcanzabl proyecto se establece desde el Presupu
e: los presupuesto del plan base esto del
costos ajustado por los recursos plan
directos realmente movilizados. base.
de Contrato
mantener y
los adendas
recursos con las
del cláusulas
proyecto de
durante penalizac
el ión.
período Análisis
adicional financier
(personal o del
, equipos, capital
instalacio inmovili
nes de zado.
obra), los
costos
financier
os del
capital
inmoviliz
ado
durante
el
período
adicional,
y las

Taxonomía General de Aplicaciones
En el
dominio
Fuente
de
Compo de
gestión Cómo se cuantifica
nente evidenci
de
a
proyecto
s
penalizac
iones
contractu
ales por
incumpli
miento
del plazo.
El
contrafác
tico es el
plazo del
plan
alcanzabl
e, no el
plan base
contractu
al cuando
éste era
irreal.
D_sobr El daño D_sobrecosto = costo_real_total Registro
ecosto producid − costo_del_plan_alcanzable. El s
(exceso o por el costo del plan alcanzable se contable
de costo costo establece desde el análisis s del
sobre el total del comparativo con proyectos proyecto
presupu proyecto similares terminados. La fracción . Análisis
esto del superior atribuible al scope creep = compara
plan al costo Σ(costo_de_cada_cambio_sin_aj tivo de
alcanzab del plan uste_de_presupuesto). costos de
le) alcanzabl proyecto
e. El s
contrafác similares.
tico es el Historial
costo del de
plan cambios
alcanzabl de
e — si el alcance
plan base con su
era irreal, costo.
la
diferenci

Taxonomía General de Aplicaciones
En el
dominio
Fuente
de
Compo de
gestión Cómo se cuantifica
nente evidenci
de
a
proyecto
s
a entre el
costo real
y el plan
base
irreal no
es
sobrecost
o
atribuible
al
contratist
a. La
fracción
del
sobrecost
o
atribuible
al scope
creep se
calcula
separada
mente del
sobrecost
o
atribuible
al
incumpli
miento
del
contratist
a.
D_indir El daño a D_indirecto = Σ Datos de
ecto los (daño_por_período × uso
(daño a beneficia períodos_de_retraso) para cada esperado
terceros rios del categoría de afectados. Para de la
por el proyecto infraestructura pública: el valor de infraestr
retraso que no la infraestructura no disponible uctura.
del pudieron estimado desde el tráfico o el uso Estudios
proyect usar la esperado × el costo unitario del de
o) infraestru perjuicio por usuario × el número impacto

Taxonomía General de Aplicaciones
En el
dominio
Fuente
de
Compo de
gestión Cómo se cuantifica
nente evidenci
de
a
proyecto
s
ctura o el de usuarios afectados × los días de económi
sistema retraso. co del
durante proyecto
el . Datos
período de costos
de por
retraso: el retraso
daño de
económi proyecto
co a los s
usuarios compara
de la bles.
infraestru Encuesta
ctura no s a los
disponibl usuarios
e, el daño afectado
a la s.
calidad
de vida
por la
indisponi
bilidad
del
servicio,
el daño a
otras
actividad
es que
dependía
n de la
terminaci
ón del
proyecto
en plazo.
Relevant
e
especialm
ente en
proyectos
de
infraestru

Taxonomía General de Aplicaciones
En el
dominio
Fuente
de
Compo de
gestión Cómo se cuantifica
nente evidenci
de
a
proyecto
s
ctura
pública.
§8 Límites del método y errores frecuentes de
aplicación
Límites del método en el dominio de gestión de proyectos
Límite 1 — El plan alcanzable tiene incertidumbre inherente.
El análisis del plan alcanzable requiere establecer qué plazo y
costo habría tenido el proyecto con la gestión adecuada y los
recursos razonables — un contrafáctico con incertidumbre
inherente que aumenta con la complejidad y la singularidad del
proyecto. Para proyectos sin comparables cercanos, la
incertidumbre del plan alcanzable puede hacer difícil
establecer si el retraso respecto al plan base era atribuible a la
falacia de planificación o al incumplimiento del contratista.
Límite 2 — El análisis del cronograma en ventanas requiere
registros completos del proyecto. El análisis que distribuye el
retraso entre las causas atribuibles a cada parte período por
período requiere el cronograma actualizado en cada período
de reporte, los registros diarios de producción, y las
comunicaciones entre las partes que documentan quién tenía
responsabilidad sobre las actividades retrasadas en cada
período. Sin esos registros, el análisis de la distribución de
causas tiene alta incertidumbre.
Límite 3 — La concurrencia de causas. En la mayoría de los
proyectos con retrasos significativos, las causas atribuibles a
cada parte son concurrentes — ocurren simultáneamente y su

Taxonomía General de Aplicaciones
efecto no es aditivo sino sinérgico. El retraso total no es la
suma del retraso atribuible al dueño más el retraso atribuible
al contratista: es el resultado de la interacción entre ambos,
donde el retraso de una parte frecuentemente produce el
retraso en cascada de la otra. El análisis de la concurrencia de
causas requiere metodologías específicas de análisis del
cronograma (modified but-for, fragnets) que el análisis
convencional no captura.
Errores frecuentes de aplicación
Error Por qué ocurre Consecuencia Corrección
Calcular el El plan base R*_DC El análisis
IPR_DC contractual es el sobreestimado debe
respecto al documento de cuando el plan establecer el
plan base referencia más base era irreal. El plan
irreal en obvio. El contratista aparece alcanzable
lugar del análisis compara como incumplidor antes de
plan el resultado real respecto a un plan calcular el
alcanzable con el plan base que nunca fue IPR_DC. Si el
sin verificar si el alcanzable. plan base era
plan base era R*_ND y irreal, el
alcanzable. R*_DDP IPR_DC se
subestimados. calcula
respecto al
plan
alcanzable, no
al plan base
contractual.
Ignorar el El sobrecosto es R*_ND El análisis del
scope visible en los subestimado sobre sobrecosto
creep registros el sobrecosto debe
como contables del atribuible al scope comenzar por
causa del contratista. La creep. La el historial de
sobrecosto causa del pretensión del cambios de
y atribuirlo sobrecosto dueño contra el alcance:
al (scope creep contratista incluye ¿cuáles fueron
contratista aprobado por el el sobrecosto que aprobados por
dueño sin ajuste el dueño mismo el dueño sin
de presupuesto) causó con los ajuste de
requiere el cambios no presupuesto?
análisis del compensados. La fracción del
historial de sobrecosto
cambios. atribuible a

Taxonomía General de Aplicaciones
Error Por qué ocurre Consecuencia Corrección
esos cambios
es R*_ND, no
R*_DC.
No El nodo de R*_nodo_presión El grafo del
analizar el presión de plazo no captado. El proyecto debe
nodo de es parte de la retraso producido incluir el nodo
presión de organización del por ignorar las de presión de
plazo dueño y se alertas de riesgo plazo como
como confunde con el bajo presión de nodo
nodo dueño del plazo queda sin independiente
causal del proyecto como nodo causal cuando hay
retraso actor único. El identificado. evidencia de
análisis no que las alertas
distingue entre del director de
las decisiones proyecto
del dueño como fueron
contratante y las ignoradas por
decisiones del un directivo
directivo que específico bajo
presionó para presión
mantener el política o
plazo. comercial.
Atribuir al El contratista es D_proyecto El análisis de la
contratista responsable del sobreestimado y distribución de
el retraso resultado del R*_DC causas del
producido proyecto y el sobreestimado por retraso debe
por retraso es su la inclusión del comenzar por
factores incumplimiento retraso exógeno identificar la
exógenos contractual. El en el análisis de fracción del
sin análisis análisis no responsabilidad. retraso
de diferencia entre atribuible a
causalidad el retraso por factores
causas exógenas exógenos —
(que reducen el fuerza mayor,
D_atribuible a cambios
las partes) y el regulatorios
retraso por imprevisibles,
causas condiciones
endógenas. del sitio
radicalmente
distintas —
que no es
atribuible a
ninguna parte.

Taxonomía General de Aplicaciones
§9 Guía de prioridades de recolección de
evidencia
La primera decisión es establecer si el plan base era
verificablemente alcanzable. Sin ese análisis previo, el análisis
de la distribución del R* entre el dueño, el director y el
contratista carece de base: el IPR_DC calculado respecto al
plan base irreal sobreestima el R* del contratista.
Tabla de prioridades de recolección de evidencia en
gestión de proyectos
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más la rango
funciona qué
principal reduce reduce
preguntar
es... es...
1. ¿El plan Datos El plan Establece ¿Cuál es el
base era históricos alcanzable la plazo y
verificable de es la referencia costo
mente proyectos referencia del IPR promedio
alcanzable? comparable correcta (incertidu de
s para mbre proyectos
terminados calcular el estructural comparabl
del sector + IPR_DC. central). es
análisis Sin él, el terminados
paramétric análisis de en el
o del plan responsabili sector? ¿El
base. Si el dad atribuye plan base
plan base al incluía
era contratista márgenes
estadística el retraso de
mente causado por contingenc
improbable el plan ia para los
dado el irreal. riesgos
historial del sistémicos
sector, hay del tipo de
falacia de proyecto?
planificació ¿Hay
n. análisis
paramétric

Taxonomía General de Aplicaciones
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más la rango
funciona qué
principal reduce reduce
preguntar
es... es...
o del plan
base
documenta
do?
2. ¿El Historial de El scope Establece ¿Hay un
retraso fue cambios de creep es la el R*_ND registro de
por scope alcance con causa de sobre el cambios de
creep no la R*_ND sobrecost alcance?
gestionado? aprobación más o por ¿Cuáles
del dueño y frecuente y scope cambios
el análisis más creep tuvieron
de impacto frecuentem (incertidu ajuste
para cada ente mbre del formal de
cambio. La ignorada en nodo plazo y
suma de los los análisis dueño). presupuest
cambios sin de o? ¿Cuál es
ajuste de responsabili el costo
plazo y dad de acumulado
presupuest proyectos. de los
o es el cambios
scope creep sin ajuste?
no
gestionado.
3. ¿El Análisis del El IPR_DC Establece ¿Qué
IPR_DC es cronogram establece el el R*_DC porcentaje
calculable a en R*_DC (incertidu de los
respecto al ventanas sobre el mbre del recursos
plan (Gp2) con incumplimi nodo comprome
alcanzable? los registros ento contratista tidos
de avance genuino. ). movilizó el
del Sin el DC en las
proyecto: análisis de fechas del
¿en qué ventanas, el plan? ¿El
períodos el IPR_DC rendimient
retraso fue puede o de los
causado incluir el recursos
por retraso movilizado
actividades causado por s era el
bajo el ND y el planificado
control del DDP. en las
DC? ¿El actividades

Taxonomía General de Aplicaciones
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más la rango
funciona qué
principal reduce reduce
preguntar
es... es...
rendimient de la ruta
o de los crítica? ¿El
recursos DC
movilizado comunicó
s era el alertas
planificado oportunas
? al DDP?
4. ¿Hay un Comunicac El nodo de Establece ¿Hay
nodo de iones entre presión de el R* del correos o
presión de el DDP y el plazo puede nodo de actas
plazo — las directivo ser el nodo presión donde el
alertas que de mayor (incertidu DDP
fueron presionó R* cuando mbre del alertó
ignoradas para las alertas nodo de sobre el
bajo mantener el del DDP presión). riesgo al
presión? plazo: ¿hay eran cronogram
alertas suficientes a? ¿La
documenta para la respuesta
das de corrección y del
riesgo al fueron directivo
cronogram ignoradas fue
a? ¿La deliberada mantener
respuesta mente. el plazo o
del revisar el
directivo plan? ¿Hay
fue antecedent
mantener el es de que
plazo en ese
lugar de directivo
revisar el ignoró
plan? alertas
similares
en otros
proyectos?
5. ¿Cuál es D_retraso Sin el Establece ¿Cuál es el
el (costos D_proyecto la escala costo
D_proyect directos del , el AD de del diario de
o total? período cada nodo D_proyec los
adicional + no tiene to recursos
ingresos base (incertidu del
perdidos + mbre proyecto

Taxonomía General de Aplicaciones
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más la rango
funciona qué
principal reduce reduce
preguntar
es... es...
penalizacio cuantificada empírica durante el
nes) + . del daño). período de
D_sobreco retraso?
sto (exceso ¿Cuáles
sobre el son los
plan ingresos
alcanzable) perdidos
+ por día de
D_indirect retraso?
o (daño a ¿Hay
los penalizacio
beneficiario nes
s del contractual
proyecto es por
durante el retraso?
retraso). ¿Cuál es el
daño a los
beneficiari
os del
proyecto
durante el
período de
retraso?
6. ¿El Hijo Análisis del El Hijo del Establece ¿Hay
dominante proceso de DDP el S del análisis
del director elaboración determina el DDP internos
de proyecto del plan S de la (incertidu del proceso
es Anteros, base: ¿hay falacia de mbre de
Fobos o análisis planificació ontológica elaboració
Potós — internos n y la del nodo n del plan
qué tipo de que fracción del director). base? ¿El
falacia hay? mostraban R*_DDP director
plazos que es presentó
superiores idiosincrátic estimacion
al plan base a. es distintas
aprobado? al plan base
¿El director aprobado?
tenía datos ¿Hay
de proyectos
proyectos anteriores
comparable del mismo
s que director

Taxonomía General de Aplicaciones
Si tu La
Qué
incertidu evidencia Qué
Por qué buscar /
mbre que más la rango
funciona qué
principal reduce reduce
preguntar
es... es...
indicaban la con el
insuficienci mismo
a del plan? patrón de
retraso?
Árbol de decisión en gestión de proyectos: tres pasos
¿El plan base era verificablemente alcanzable — cuál es la
referencia para el IPR?
│
├─ Plan base IRREAL (falacia de planificación
documentada) → IPR_DC respecto al plan alcanzable
│ └─ PRIORIDAD 1: ¿La falacia fue Anteros
(deliberada) o Potós (sistémica del sector)?
│ · Anteros → S_DDP bajo [0.05–0.22].
R*_DDP pleno sobre el plan irreal.
│ · Potós → S_DDP moderado-alto [0.42–
0.70]. R* compartido con el sector.
│ └─ PRIORIDAD 2: ¿El ND aprobó el plan
sabiendo que era irreal?
│ · Sí → R*_ND sobre la fracción del retraso
atribuible al plan irreal que aprobó.
│ └─ PRIORIDAD 3: ¿Hay scope creep no
gestionado — R*_ND adicional?
│ · Cambios sin ajuste de plazo y presupuesto
→ R*_ND sobre el sobrecosto del scope creep.
└─ Plan base ALCANZABLE → IPR_DC respecto al
plan base
└─ PRIORIDAD 1: ¿El DC incumplió
respecto al plan alcanzable?
· Análisis de ventanas del cronograma
establece el IPR_DC.

Taxonomía General de Aplicaciones
└─ PRIORIDAD 2: ¿Hay nodo de presión de
plazo que ignoró alertas?
· Alertas documentadas ignoradas →
R*_NPP sobre el retraso posterior a la alerta.
├─ Paso 2: ¿Cuál es la distribución del R* entre ND, DDP,
DC y NPP?
│
├─ R*_ND dominante → scope creep + plan irreal
aprobado → pretensión principal contra el dueño
│ └─ AD_ND = R*_ND × D_proyecto × (1 −
α_ND).
├─ R*_DDP dominante → falacia de planificación
idiosincrática → plan irreal por diseño del director
│ └─ AD_DDP = R*_DDP × D_proyecto × (1
− α_DDP).
└─ R*_DC dominante → incumplimiento genuino
respecto al plan alcanzable
└─ AD_DC = R*_DC × D_proyecto × (1 −
α_DC).
└─ Paso 3: ¿El D_proyecto incluye el D_indirecto a
terceros?
├─ SÍ (proyecto de infraestructura pública con
beneficiarios identificados)
│ └─ D_indirecto = daño_por_período ×
períodos_de_retraso ×
N_beneficiarios_afectados.
└─ NO (proyecto privado sin afectados externos) →
D_proyecto = D_retraso + D_sobrecosto
└─ AD_nodo = R*_nodo × (D_retraso +
D_sobrecosto) × (1 − α_nodo).
— Fin del Capítulo 36 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

