## PARTE II · Ciencias Económicas y Financieras

### Capítulo 11
Crédito y sistema financiero —
fraude y colapso crediticio
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo opera con tres análisis que deben distinguirse desde el inicio. El
primero es el análisis causal del impago individual: distribución de la
responsabilidad del impago entre el deudor, el diseñador del producto crediticio,
el algoritmo y el entorno macroeconómico. El segundo es el análisis del sesgo
sistémico: cómo el nodo algorítmico transmite el daño histórico al sistema
presente, y quién tiene R* sobre ese sesgo. El tercero es el análisis del riesgo
sistémico y el colapso financiero: quién tenía mayor posición causal en el diseño
del sistema que hizo inevitable el colapso. Si tu prioridad es el análisis del
impago individual, lee §1 a §5. Para el análisis del sesgo algorítmico, ve a
§4.3. Para el colapso sistémico, ve a §4.4. Para cuantificar D_crédito, ve a
§7. Para la prioridad de evidencia, ve a §9.
§1 Descripción del subcampo
El crédito y el sistema financiero es el dominio donde el
sistema de imputación causal introduce un tipo de nodo que
no había aparecido en ningún capítulo anterior: el nodo
algorítmico / dataset, con posición causal real en el grafo, pero
sin voluntad propia, sin dolo y sin Hijos. Su R* no implica
culpabilidad del algoritmo sino posición causal que apunta
estructuralmente hacia el directivo que lo aprobó y hacia el

Taxonomía General de Aplicaciones
diseñador de la política que generó los datos con los que fue
entrenado. Esa distinción — entre el R* del nodo sin voluntad
y el R* del actor humano que lo creó o aprobó — es la
contribución conceptual central de este capítulo.
La segunda distinción fundamental es entre el impago
idiosincrático (causado principalmente por las condiciones y
conductas específicas del deudor: R*_deudor alto) y el impago
estructural (causado principalmente por el diseño del sistema
crediticio: R*_sistema > R*_deudor). Esa distinción
transforma la evaluación del riesgo crediticio de un ejercicio
de predicción estadística sobre el deudor en un análisis causal
del sistema completo que produce el impago.
El índice de causalidad del impago: R* en el sistema crediticio
R*_impago = R*_deudor + R*_dataset + R*_directivo + R*_producto
+ R*_entorno_macro + ...
Esta descomposición transforma la evaluación del riesgo crediticio. R*_deudor
es la fracción del impago causalmente atribuible a las condiciones y conducta
específicas del deudor. R*_sistema es la fracción atribuible al diseño del
producto, al sesgo del algoritmo, a la política crediticia del acreedor y al entorno
macroeconómico. Cuando R*_sistema > R*_deudor, el sistema tiene mayor
responsabilidad causal en el impago que el deudor. La acción de cobro integral
contra el deudor en ese escenario es la inversión causal clásica del sistema
financiero.
La distinción entre correlación crediticia y causalidad crediticia: el score FICO
predice el impago con correlación estadística real. Pero esa correlación no
implica causalidad en el sentido del sistema: no dice que el FICO bajo causó
el impago. Puede decir que las condiciones que produjeron un FICO bajo —
ingresos inestables, falta de historial crediticio formal, acceso solo a productos
de alto costo — son las mismas condiciones que producen el impago. Y esas
condiciones pueden tener un nodo de diseño con R* mucho mayor que el del
deudor.
Sub-variantes del dominio
Impago individual y responsabilidad crediticia: la distribución
de R* entre el deudor y el sistema en un impago específico. El

Taxonomía General de Aplicaciones
análisis determina qué fracción del impago era causalmente
atribuible al deudor (su gestión financiera, su capacidad de
servicio de la deuda, sus decisiones) y qué fracción era
atribuible al producto (tasa excesiva para el perfil del deudor,
términos irrazonables, condiciones de renegociación
inexistentes), al algoritmo de scoring (sesgo que excluyó
crédito justo), y al entorno macroeconómico.
Sesgo algorítmico y discriminación crediticia sistémica: el
algoritmo de scoring produce resultados sistemáticamente
desfavorables para grupos que, dado su perfil crediticio real,
deberían recibir condiciones equivalentes a otros grupos. El
sesgo opera a través de variables proxy que no son
discriminatorias en sí mismas pero que capturan patrones de
segregación histórica. R* del dataset y R* del directivo que
aprobó el modelo sin auditoría de equidad son los
instrumentos de imputación.
Crédito predatorio: el diseñador del producto financiero
diseñó deliberadamente condiciones que hacían inevitable el
impago para capturar el activo o generar ingresos por
comisiones y penalizaciones que superaban el costo del capital.
S_bajo del diseñador: la estructura específica del producto era
idiosincrática y deliberada. Anteros dominante. R*_sistema
alto, R*_deudor bajo.
Fraude financiero corporativo: el directivo de la institución
financiera diseñó un esquema de falsificación de información,
de ventas de productos que sabía inadecuados para el perfil del
cliente, o de ocultación de riesgos a los accionistas y
reguladores. La estructura del grafo es idéntica al fraude
corporativo del cap. 6 (competencia), aplicada al dominio
financiero.
Riesgo sistémico y colapso financiero: el diseño del sistema
financiero — los instrumentos de seguridad, las calificaciones
crediticias que no reflejaban el riesgo real, el marco de
desregulación que permitió la escala del riesgo — creó las
condiciones de un colapso que ningún actor individual podría
haber producido solo. El índice de concentración de riesgo

Taxonomía General de Aplicaciones
sistémico (ICRS) establece qué nodo del sistema tenía mayor
posición causal en el colapso.
Fraude annona crediticio estatal: el Estado diseñó un sistema
crediticio que excluía a grupos específicos del acceso al crédito
(redlining) o que no reguló la discriminación algorítmica
sistémica (inacción regulatoria), recibiendo los impuestos de
las comunidades afectadas sin generar las condiciones
materiales de posibilidad para su acumulación de patrimonio.
§2 Escala de evidencia CF0–CF8 · Dominio
crediticio y financiero
La escala CF0–CF8 traduce la jerarquía general E0–E8 al
vocabulario del crédito y el sistema financiero. Su característica
más relevante es la posición del peritaje financiero-cuantitativo
(CF2) como instrumento central del dominio — incluyendo el
análisis de disparate impact algorítmico, que transforma el
sesgo estadístico en evidencia causal. Compilación directa
desde El cálculo de la responsabilidad cap. 8 y cap. 9.
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio crediticio
evidencia w
y financiero
CF1 Documento Expediente crediticio con [0.74,
financiero o los términos del producto y 0.92]
institucional el perfil del deudor al
directo momento de la aprobación;
política interna de crédito
del acreedor; correo o acta
donde se tomó la decisión
de diseño del producto o
del algoritmo; estados
financieros de la institución
con los datos relevantes del
período; registro de
comunicaciones entre el
directivo aprobador y el
equipo que presentó
advertencias de sesgo;

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio crediticio
evidencia w
y financiero
documentación de
auditoría interna del
sistema de scoring.
CF2 Peritaje Análisis de capacidad de [0.65,
financiero- servicio de la deuda que 0.85]
cuantitativo establece si el producto era
especializado razonablemente pagable
dado el perfil del deudor;
análisis de disparate impact
que establece si el
algoritmo producía
diferencias
estadísticamente
significativas entre grupos
comparables en ingresos y
deudas; análisis de
concentración de riesgo
sistémico (ICRS) que
establece la posición causal
de cada nodo en el colapso;
valoración del D_crédito
mediante análisis de la
brecha patrimonial
generada por el sesgo o el
colapso.
CF3 Testimonios Declaraciones de deudores [0.48,
convergentes con afectados cuyas versiones 0.66]
corroboración son compatibles entre sí y
documental con al menos un registro
documental consistente;
testimonios de empleados
de la institución que
describen las prácticas de
diseño del producto o del
algoritmo; testigos del
programa de clemencia en
fraudes financieros
corporativos.
CF4 Análisis Análisis que muestra que [0.40,
estadístico del las tasas de impago, de 0.62]
comportamiento denegación de crédito o de
pérdida patrimonial del

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio crediticio
evidencia w
y financiero
del sistema grupo afectado son
crediticio estadísticamente
incompatibles con su perfil
crediticio objetivo;
comparación de tasas de
aprobación y condiciones
entre grupos con perfiles
comparables que muestra
un diferencial
estadísticamente
significativo; análisis de la
correlación entre el perfil
del algoritmo de scoring y
el patrón de segregación
residencial histórica.
CF5 Documentación Especificaciones técnicas [0.28,
estructural del del modelo de scoring o del 0.48]
algoritmo o del producto financiero que
producto con muestran variables proxy
inferencia de discriminatorias o
función condiciones diseñadas para
producir impago; estados
financieros de la institución
que muestran patrones de
comisiones y
penalizaciones
inconsistentes con un
producto diseñado para ser
pagado.
CF6 Inferencia El directivo o la institución [0.18,
estructural por tenía la posición, la 0.38]
posición en el información y el control
sistema crediticio sobre el sistema para haber
o financiero diseñado o aprobado las
condiciones que
produjeron el daño, sin
documentación directa del
acto específico de diseño o
aprobación.
CF7 Correlación El deterioro patrimonial o [0.07,
patrimonial o de la tasa de impago del grupo 0.24]
afectado correlaciona con

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de Rango
Nivel en el dominio crediticio
evidencia w
y financiero
impago sin análisis la variable o el período
causal analizado sin que haya
análisis que establezca la
cadena causal específica.
CF8 Dicho único sin Un solo testimonio o [0.04,
corroboración documento sin respaldo 0.16]
cuantitativo ni
corroboración documental.
CF0 Ausencia Análisis cuantitativo que w =
documentada de establece que las tasas de 0.00
conexión causal impago o de denegación de
crédito del grupo son
estadísticamente
consistentes con su perfil
crediticio objetivo, o que el
colapso habría ocurrido
igualmente sin la posición
causal del nodo analizado.
El análisis de disparate impact como instrumento de
traducción de CF4 a CF2
El análisis de disparate impact toma una diferencia estadística observada
(tasa de denegación 80% mayor para un grupo dado sus características
crediticias objetivas) y establece si esa diferencia es causalmente atribuible al
diseño del algoritmo o del producto. Cuando el análisis de disparate impact es
realizado por un perito especializado con metodología reproducible, la evidencia
CF4 del patrón estadístico se transforma en evidencia CF2 del mecanismo
causal. Sin el peritaje que establece el mecanismo, la diferencia estadística es
CF4 y sustenta aristas en el rango [0.40, 0.62]. Con el peritaje, la evidencia
alcanza CF2 [0.65, 0.85].
§3 Firmas documentales por Hijo e
información para S
En el dominio crediticio, los Hijos de Afrodita aplican
exclusivamente a los directivos y reguladores con poder de

Taxonomía General de Aplicaciones
decisión sobre el diseño del producto, el algoritmo o la política
crediticia. No aplican al algoritmo, al dataset, al producto
financiero como nodo sin voluntad, ni al entorno
macroeconómico. Para los nodos sin voluntad, S se estima
directamente desde la evidencia cuantitativa de la
determinación sistémica.
La distinción más relevante para la política regulatoria es entre
Potós (el directivo persistió en el sistema heredado sin
cuestionarlo — cualquier directivo en esa cultura institucional
habría actuado igual: S alto, culpa habitual, solución
regulatoria) y Anteros (el directivo defendió deliberadamente
un sistema que sabía sesgado o defectuoso: S bajo, dolo
eventual o directo, solución penal-civil).
§3.1 Hijos de legibilidad alta en el dominio crediticio
Qué Firma en Error de
Fuente
informa el discrimina
Hijo document
para S del expediente ción
al típica
directivo financiero frecuente
Anter S bajo [0.05, Comunicaci Correos Confundir
os 0.28]. El ones internos del con Potós
directivo internas que directivo. cuando el
diseñó o documenta Actas de directivo
defendió n el comités de recibió
deliberadam conocimien riesgo y alertas, pero
ente to del cumplimien las
condiciones directivo del to. desestimó
crediticias sesgo o del Documenta por creer
sesgadas, riesgo: ción de genuinamen
predatorias alertas de alertas te que el
o equidad recibidas. modelo era
fraudulenta desestimada Comparaci correcto. La
s con s por ón con pregunta
conocimien escrito, decisiones discriminan
to explícito análisis de de te: ¿el
del daño riesgo que el directivos directivo
que directivo de sabía que el
producían. recibió y no institucione sistema
La decisión actuó, s pares en el producía

Taxonomía General de Aplicaciones
Qué Firma en Error de
Fuente
informa el discrimina
Hijo document
para S del expediente ción
al típica
directivo financiero frecuente
fue presión mismo daño
genuinamen documenta período. injusto, o
te da sobre el creía que el
idiosincrátic equipo de modelo era
a: otros cumplimien técnicament
directivos to para no e válido? El
en reportar primero es
condiciones irregularida Anteros; el
similares, des. segundo
con el Decisiones puede ser
mismo que Potós.
marco excedieron
regulatorio lo que el
y los sistema de
mismos incentivos
incentivos, requería.
no habrían
producido
las mismas
condiciones
.
Potós S Ausencia de Expediente Confundir
moderado- documentac del modelo con
alto [0.45, ión de de scoring Anteros
0.80]. El análisis de con fecha cuando el
directivo equidad o de última directivo
persistió en de auditoría revisión o recibió
el uso del de riesgo en auditoría. advertencia
sistema el Política s explícitas
crediticio expediente interna de de
heredado del modelo crédito con miembros
— el o del historial de del equipo y
modelo de producto. actualizacio las
scoring, el Uso del nes. desestimó
producto modelo Documenta activamente
financiero, estándar de ción de la . Si hay
la política de la industria industria documenta
aprobación sin sobre las ción de que
— sin evaluación prácticas el directivo
cuestionarlo independien estándar del suprimió o
críticamente te. período. ignoró
ni auditarlo Resistencia advertencia
para pasiva a s de

Taxonomía General de Aplicaciones
Qué Firma en Error de
Fuente
informa el discrimina
Hijo document
para S del expediente ción
al típica
directivo financiero frecuente
detectar revisiones equidad,
sesgo o del sistema. Anteros
riesgo Documenta moderado
excesivo. ción de que es más
"Los datos el directivo preciso que
son los estaba al Potós.
datos." tanto del
"Siempre modelo
hemos pero no lo
usado este cuestionó.
modelo." La
conducta
era
deliberada
pero no
idiosincrátic
a: cualquier
directivo en
esa cultura
institucional
habría
hecho lo
mismo.
Deim S alto [0.65, Ausencia Expediente Confundir
os 0.90]. El total de de con Potós
directivo documentac aprobación cuando
genuinamen ión de del modelo había
te no evaluación o del análisis
comprendía del producto. disponibles
las algoritmo o Documenta en el sector
implicacion del ción de que el
es del producto onboarding directivo
modelo o antes de la del ignoró. Si el
del aprobación. directivo. análisis de
producto Sin alertas Comparaci disparate
financiero internas ón con el impact era
que aprobó. (que nivel una práctica
La parálisis confirmaría técnico conocida en
ante la n Potós o esperado la industria
complejidad Anteros). El del cargo. en ese
técnica del directivo período y el
sistema de aprobó el directivo no
scoring o de sistema lo aplicó,

Taxonomía General de Aplicaciones
Qué Firma en Error de
Fuente
informa el discrimina
Hijo document
para S del expediente ción
al típica
directivo financiero frecuente
la estructura siguiendo el puede ser
de riesgo del procedimie Potós
producto nto estándar (ignorancia
determinó sin análisis electiva)
la adicional. más que
aprobación. Deimos
Ausencia de (ignorancia
análisis, no genuina).
supresión
de análisis.
§3.2 El Hijo del deudor: relevante para S del deudor en el
impago idiosincrático
En el análisis del impago individual, cuando el análisis
establece que R*_deudor es significativo, los Hijos del deudor
informan la posición de v_t en el momento de las decisiones
financieras que contribuyeron al impago. Fobos del deudor:
actuó bajo presión financiera sistémica (pérdida de empleo,
emergencia médica, crisis sistémica) que determinó el impago
— S alto del deudor. Anteros del deudor: tomó decisiones
idiosincráticas que, dado su perfil y las condiciones
disponibles, otros deudores en la misma posición no habrían
tomado — S bajo del deudor. Deimos del deudor: no
comprendió completamente las condiciones del producto que
firmó — lo que puede incidir en la responsabilidad del
diseñador del producto que no proveyó información
adecuada.
§3.3 Los nodos sin voluntad no tienen Hijo — el dataset y
el producto financiero
El algoritmo de scoring, el dataset de entrenamiento, el producto financiero
estructurado y el índice de calificación crediticia son nodos causales sin voluntad
propia. No tienen Hijo, no tienen α, no pueden ser sancionados directamente.

Taxonomía General de Aplicaciones
Su R* se imputa hacia los actores humanos que los diseñaron y aprobaron: el
directivo que aprobó el algoritmo sin auditoría (R*_efectivo_directivo =
R*_directivo + R*_dataset × P (detección | auditoría)), el diseñador del
producto que estructuró las condiciones del impago, el regulador que permitió
la escala del riesgo sin intervenir.
§4 ¿Qué cuenta como asunción (α) en el
dominio crediticio?
α en el dominio crediticio mide lo que el acreedor, el directivo
o el regulador han hecho concretamente sobre su posición
causal: corrección del sesgo del algoritmo con auditoría
verificable, modificación del producto financiero para hacerlo
razonablemente pagable, compensación a los deudores
excluidos incorrectamente, reestructuración del crédito ante
choques exógenos. Para el Estado: regulación que corrige la
discriminación sistémica, programas de inclusión financiera
proporcionales al déficit histórico.
α en el dominio crediticio es completamente independiente del
dolo
Un directivo que diseñó deliberadamente condiciones predatorias puede tener
α alto si después auditó el sistema, corrigió el sesgo y compensó a los afectados.
Un directivo que replicó el modelo estándar del sector sin comprender sus
implicaciones puede tener α = 0 si nunca auditó ni corrigió el sistema una vez
informado. Los Hijos informan S; α mide lo que el actor hizo después sobre
su posición causal.
Acción del ¿Cuenta Tipo de
Razón
actor para α? α
Auditoría de Sí — α La auditoría que Voluntari
equidad del estructural detecta y corrige el o
algoritmo con alto sesgo es la asunción
corrección más valiosa en el
verificable antes dominio algorítmico:
o después del reduce
daño P(detección|auditorí

Taxonomía General de Aplicaciones
Acción del ¿Cuenta Tipo de
Razón
actor para α? α
a) que determina
R*_efectivo del
directivo.
Compensación Sí — α Asunción económica Voluntari
a los deudores económico directa de la posición o o
afectados por el proporcion causal verificable en forzado
sesgo al el expediente.
proporcional al
AD_i
Modificación Sí — α Modifica el sistema Voluntari
del producto estructural que producía el o o
para hacerlo del impago estructural. requerido
razonablemente producto
pagable dado el
perfil del
deudor
Reestructuració Sí — α de El acreedor asume Voluntari
n del crédito respuesta parte del o o
ante choque proporcion R*_entorno cuando regulatori
macroeconómic al reestructura ante o
o exógeno choques que no son
documentado imputables al
deudor.
El regulador Sí — α La regulación que Requerid
estableció regulatorio hace obligatoria la o por
estándares de auditoría es α mandato
auditoría de institucional del
equidad regulador sobre el
obligatorios déficit que permitió.
El Estado Sí — Asunción diferida de Voluntari
implementó α_diferido la posición causal o /
programas de del Estado histórica del fraude político
inclusión annona crediticio
financiera estatal. Ver cap. 3
proporcionales para el marco del
al déficit α_diferido.
histórico
Publicar un No Declaración sin —
reporte de consecuencia
responsabilidad concreta sobre la
corporativa sin

Taxonomía General de Aplicaciones
Acción del ¿Cuenta Tipo de
Razón
actor para α? α
modificar el posición causal. No
algoritmo modifica α.
§4.3 La imputación del R* del dataset al directivo
R*_efectivo del directivo en el sesgo algorítmico
R*_efectivo_directivo = R*_directivo + R*_dataset × P (detección |
auditoría)
P (detección | auditoría) es la probabilidad de que una auditoría de disparate
impact estándar habría detectado el sesgo. Para sesgos de alta magnitud
(diferencias de 80% o más en tasas de denegación controlando por perfil
crediticio), P ≈ 0.90. Eso significa que el directivo que aprobó el modelo sin
auditoría tiene responsabilidad causal efectiva del orden de R*_directivo +
0.9 × R*_dataset — la mayor parte de la posición causal del dataset le es
imputable.
Cuando el directivo realiza la auditoría y corrige el sesgo: α sube
significativamente y R*_efectivo_directivo cae a R*_directivo solo (ya no
incluye R*_dataset porque el sesgo fue detectado y corregido). La auditoría es
tanto una acción de α como una reducción del R*_efectivo futuro. Eso es la
auditoría como instrumento de α estructural.
§4.4 El índice de concentración de riesgo sistémico (ICRS)
en el colapso financiero
En el análisis de colapso financiero, el instrumento central no
es el α individual de cada actor sino el ICRS — el índice de
concentración de riesgo sistémico — que establece qué nodo
del sistema financiero tenía mayor R* sobre el colapso
colectivo. El ICRS responde la pregunta: sin este nodo
específico (esta institución, este instrumento, esta política
regulatoria), ¿habría ocurrido el colapso a esta escala?

Taxonomía General de Aplicaciones
ICRS_i = R*_i sobre el grafo de interdependencias financieras del
sistema
ICRS alto de un nodo significa que ese nodo era condición necesaria del
colapso a esa escala — ya sea porque era un puente necesario en la red de
transmisión del riesgo, porque su quiebra activaba cláusulas que producían
quiebras en cascada, o porque su existencia era condición para que otros nodos
mantuvieran su solvencia aparente.
Diferencia fundamental con el análisis de riesgo convencional: el riesgo
financiero convencional es un cálculo sobre la probabilidad de que un actor
individual incumpla sus obligaciones. El ICRS es algo diferente y más difícil:
la probabilidad de que la interconexión entre actores produzca un colapso en
cascada que ninguno de ellos habría producido individualmente. Esta
distinción no se captura con ninguna medida de riesgo convencional porque las
medidas convencionales son por definición individuales.
La escala de α en el dominio crediticio
Rango Descripción Indicadores en
Nivel
α observable el expediente
Negación / 0.00 – El acreedor o el Sin auditorías, sin
evasión total 0.05 directivo niega el correcciones del
sesgo o el daño, algoritmo, sin
combate compensaciones.
activamente el Impugnación
proceso sin activa de las
ninguna acción determinaciones
concreta de del regulador.
corrección ni
compensación.
Reconocimiento 0.06 – Reconocimiento Comunicados de
nominal 0.20 del impacto del equidad
sesgo o del daño financiera. Sin
crediticio sin auditorías
consecuencia documentadas.
concreta. Sin correcciones
Declaración de del modelo. Sin
"compromiso compensaciones.
con la equidad
financiera" sin
modificación del
sistema.

Taxonomía General de Aplicaciones
Rango Descripción Indicadores en
Nivel
α observable el expediente
Asunción 0.21 – Auditoría del Reporte de
parcial 0.45 algoritmo auditoría
realizada pero sin documentado.
corrección Correcciones
completa del menores del
sesgo, o modelo.
compensación Compensaciones
menor al AD_i documentadas del
estimado. 10–30% del
AD_i.
Asunción activa 0.46 – Auditoría con Corrección
en proceso 0.70 corrección del documentada del
modelo en algoritmo con
proceso datos
verificable y comparativos
compensaciones antes-después.
sustanciales en Compensaciones
curso. del 40–60% del
AD_i. Programa
de inclusión en
proceso.
Asunción 0.71 – El modelo fue Reducción
funcional 0.89 corregido con verificable del
datos verificables disparate impact
de reducción del post-corrección.
disparate impact Compensaciones
y las del 70–85% del
compensaciones AD_i.
son Cumplimiento
proporcionales a documentado
la mayor parte con los estándares
del daño. regulatorios de
equidad.
Asunción plena 0.90 – Corrección Reducción del
1.00 integral del disparate impact a
sistema, niveles
compensaciones estadísticamente
proporcionales al no significativos.
R* y mecanismos Compensaciones
de auditoría integrales
permanentes que documentadas.
previenen la Programa de
recurrencia. auditoría

Taxonomía General de Aplicaciones
Rango Descripción Indicadores en
Nivel
α observable el expediente
permanente con
seguimiento
verificable.
§5 Construcción del grafo típico del dominio
crediticio
Tipos de nodo en el grafo crediticio y financiero
Ejemplo
Tipo Función en el grafo S típico en el
dominio
Diseñador de El actor con poder de Variable El directivo
política / decisión sobre el [0.15– que aprobó
directivo diseño del producto 0.60] el
aprobador (D) crediticio, el algoritmo
algoritmo de scoring de scoring
o la política de sin
aprobación. Es el auditoría de
nodo humano de equidad. El
mayor R*_neta ejecutivo
cuando el sistema era que diseñó
idiosincrático. Sus el producto
Hijos informan S. La predatorio.
distinción El
Anteros/Potós/Dei regulador
mos determina si el que no
proceso es penal o estableció
regulatorio. estándares
de equidad
a pesar de
evidencia
de
disparate
impact.
Nodo El algoritmo de N/A — El
algorítmico / scoring, el dataset de no es algoritmo
dataset (NA) entrenamiento, el actor con de scoring
producto voluntad entrenado

Taxonomía General de Aplicaciones
Ejemplo
Tipo Función en el grafo S típico en el
dominio
estructurado o la con datos
calificación crediticia. históricos
Tiene posición causal de
real en el grafo sin segregación
tener voluntad. Su R* residencial.
se imputa al directivo El dataset
que lo aprobó y al de
diseñador de la hipotecas
política que generó que
los datos sesgados. reproduce
No tiene α, no puede el mapa del
ser sancionado redlining.
directamente. El modelo
de
calificación
que otorgó
AAA a
instrument
os de alto
riesgo.
Institución El banco, la fintech o Moderad El banco
financiera (IF) la institución de o-alto que
crédito que [0.40– comercializ
implementa y 0.80] ó hipotecas
comercializa el subprime a
sistema crediticio. R* deudores
positivo cuando sus con perfil
decisiones inadecuado
institucionales eran . La fintech
condición de la escala que
del daño. S informa si desplegó el
cualquier institución algoritmo
con los mismos sesgado. La
incentivos habría institución
actuado igual. que diseñó
y vendió
instrument
os de alto
riesgo
como
seguros.

Taxonomía General de Aplicaciones
Ejemplo
Tipo Función en el grafo S típico en el
dominio
Regulador La autoridad Alto La Reserva
omisivo (Reg) financiera que tenía [0.60– Federal que
información del 0.90] observó el
riesgo sistémico o del crecimient
sesgo algorítmico y o de la
no estableció los burbuja
estándares que lo hipotecaria
habrían prevenido. y no usó los
R* positivo cuando la instrument
omisión regulatoria os
fue condición de la regulatorio
continuidad del s
sistema que produjo disponibles
el daño. . La CFPB
que tardó
en
establecer
estándares
de auditoría
de equidad
algorítmica.
Entorno Los choques N/A — La crisis
macroeconómi exógenos (crisis no es financiera
co (EM) financiera, pandemia, actor de 2008. La
recesión) que pandemia
contribuyeron de
causalmente al COVID-
impago sin ser 19. El ciclo
atribuibles a ningún de tasas de
actor específico. interés que
Nodo sin voluntad hizo
que informa S del insostenibl
deudor: cuanto más es los
determinante fue el créditos
entorno, mayor es S variables.
del deudor y menor es
R*_deudor.
Deudor (Deu) El receptor del Variable El deudor
crédito y su capacidad [0.15– que
de servicio de la 0.80] incumplió
deuda. R* positivo el crédito
cuando las hipotecario
condiciones y . El cliente

Taxonomía General de Aplicaciones
Ejemplo
Tipo Función en el grafo S típico en el
dominio
conductas específicas del
del deudor eran producto
causalmente predatorio.
determinantes del El
impago. S informa solicitante
cuánto del impago era de crédito
estructural versus excluido
idiosincrático. por el
algoritmo
sesgado.
Configuraciones canónicas del grafo crediticio
Configuración 1 — Impago estructural con inversión causal
contra el deudor
D (diseñador del producto con tasa excesiva para el perfil) → IF (institución
que comercializó) → Deu (deudor con R*_deudor bajo) → Impago
La estructura clásica de la inversión causal crediticia: el sistema de cobro
intenta recuperar el 100% del AD del impago del deudor cuando R*_deudor
es menor que R*_sistema. AD_deudor = R*_deudor × (1 − S_deudor)
× D_total. Si este valor es significativamente menor que el monto reclamado
al deudor, la reclamación íntegra al deudor es jurídicamente inverosímil.
Configuración 2 — Sesgo algorítmico con nodo dataset y directivo
aprobador
Redlining histórico (N1, diseño original) → Dataset histórico (NA, nodo
sin voluntad) → Directivo aprobador (D, R*_efectivo alto) → IF
(institución, despliegue) → Deudores excluidos incorrectamente (Nf)
R*_efectivo_directivo = R*_directivo + R*_dataset × P (detección |
auditoría). El directivo no discriminó con intención, pero discriminó con
precisión estadística al aprobar sin auditar. La solución regulatoria (auditoría
obligatoria) actúa sobre el vínculo directivo-dataset reduciendo P (impacto no
detectado).

Taxonomía General de Aplicaciones
Configuración 3 — Riesgo sistémico y colapso en cascada
Marco_regulatorio_permisivo (ICRS alto como diseño) →
Institución_sistémica (ICRS alto como nodo de transmisión) →
Instrumentos_de_riesgo (NA sin voluntad) → Calificadoras_sesgadas
(ICRS moderado) → Colapso_sistémico (Nf: todo el sistema financiero y sus
usuarios)
En el análisis de colapso sistémico, el ICRS de cada nodo determina quién
era condición necesaria del colapso a esa escala. El argumento central: el
colapso no fue el fracaso de la voluntad de los directivos de las instituciones
involucradas, sino el fracaso de la arquitectura del sistema en el que operaban.
La solución no puede ser solo individual: requiere reforma de la arquitectura
del sistema.
§6 Preguntas que responde este capítulo
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
¿El impago era Análisis de R*_impago Declaración A o B si
principalmente descompuesto en sus el expediente
atribuible al cuatro componentes: crediticio es
deudor R*_deudor (capacidad completo.
(R*_deudor > objetiva de servicio de la Declaración C si el
R*_sistema) o al deuda), R*_producto análisis del
diseño del (condiciones del crédito algoritmo requiere
sistema frente al perfil), inferencia
crediticio R*_dataset (sesgo estructural CF6.
(R*_sistema > algorítmico si aplica),
R*_deudor)? R*_entorno (choques
exógenos). El peritaje
CF2 establece cada
componente.
¿El directivo que R*_efectivo_directivo = Declaración B si hay
aprobó el R*_directivo + análisis CF2 del
algoritmo de R*_dataset × P (detección disparate impact y
scoring tiene | auditoría). P se estima documentación CF1
R*_efectivo que desde el análisis de del proceso de
incluye R* del disparate impact CF2: aprobación.
dataset? cuánto habría detectado Declaración C si
P(detección) debe

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
una auditoría estándar del estimarse desde
sector en ese período. CF4.
¿El sistema Análisis CF4 de disparate Declaración A o B si
crediticio impact: tasa de hay datos del Home
producía denegación o de Mortgage
discriminación condiciones Disclosure Act u
sistemática desfavorables del grupo equivalente con
contra un grupo afectado versus grupo análisis CF2.
con perfil comparable en ingresos y Declaración C si el
crediticio deudas. Si la diferencia es análisis debe
comparable? estadísticamente inferirse desde CF5.
significativa → CF4 con
w [0.40, 0.62]. Si el peritaje
CF2 establece el
mecanismo causal →
CF2.
¿El producto Análisis CF2 de la Declaración B si los
financiero era estructura del producto: términos del
predatorio — ¿las condiciones eran producto y el perfil
diseñado para razonablemente pagables del cliente objetivo
producir impago dado el perfil estándar del están
y capturar el cliente objetivo? ¿El documentados.
activo o las margen de comisiones y Declaración C si el
comisiones? penalizaciones por análisis de la
impago superaba el intención del
ingreso esperado del diseñador requiere
crédito pagado? ¿El inferencia CF6.
diseñador tenía incentivos
para maximizar el
impago?
¿Qué nodo del Construcción del grafo de Declaración B si los
sistema interdependencias datos del sistema de
financiero tenía financieras del sistema y interdependencias
mayor ICRS — cálculo del ICRS_i = R*_i son suficientes.
mayor posición sobre ese grafo. El nodo Declaración C para
causal en el con ICRS más alto es el los sistemas donde
colapso? que era condición las
necesaria del colapso a esa interdependencias
escala. deben estimarse
desde posiciones de
mercado y
correlaciones.

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
¿El Estado tiene Grafo histórico: Estado Declaración B si hay
posición causal como diseñador del documentación
histórica como sistema de exclusión + histórica del sistema
nodo de diseño análisis de α_diferido de exclusión y
del sistema de actual (cuánto ha asumido análisis CF4 del
exclusión desde la prohibición del diferencial
crediticia — redlining formal). El patrimonial
fraude annona mismo instrumento del persistente.
crediticio? cap. 3 (plano histórico): Declaración C para
Posición_heredada del la atribución de
Estado y α_diferido de los ΔT_trayectoria.
sucesores institucionales
del sistema de exclusión.
§7 Traducción de D_crédito al dominio
financiero
El D_crédito tiene una estructura tricomponente que se aplica
a tres objetos distintos según el tipo de caso: el D_crédito del
deudor individual (patrimonio perdido), el D_crédito de la
comunidad excluida (acumulación de riqueza truncada), y el
D_crédito del sistema (colapso sistémico). La distinción entre
estos tres objetos es fundamental para construir la pretensión
correctamente.
D_crédito D_crédito de la D_crédito
Componente del deudor comunidad del sistema
individual excluida (colapso)
T_invertido Capital Capital que los Pérdidas
(pérdida prestado no grupos excluidos directas de
directa recuperado habrían depositantes,
verificable) (acreedor). acumulado en el accionistas e
O: pagos período de inversores en
que exclusión activa el colapso.
excedían el del sistema Capitalización
costo real crediticio. pública de las
del capital instituciones
en crédito en crisis.

Taxonomía General de Aplicaciones
D_crédito D_crédito de la D_crédito
Componente del deudor comunidad del sistema
individual excluida (colapso)
predatorio
(deudor).
T_impedido Patrimonio El diferencial de Crédito no
(oportunidad no acumulación disponible
truncada acumulado patrimonial para empresas
durante el durante el entre los grupos y familias
período período de con acceso al durante el
activo) exclusión crédito justo y período de
crediticia: la los grupos congelamient
vivienda no excluidos o del crédito
comprada, durante el post-colapso.
el negocio período del Empleos no
no sistema sesgado. creados.
capitalizado, Proyectos no
la educación ejecutados.
no
financiada.
ΔT_trayectori El La brecha de El daño
a (diferencial diferencial riqueza permanente a
persistente) de intergeneraciona la confianza
acumulació l que persiste hoy en el sistema
n futura como financiero, la
entre la consecuencia del destrucción de
trayectoria sistema histórico valor de
con acceso de exclusión. En mercado de
al crédito el redlining: el largo plazo, el
justo y la componente del costo de las
trayectoria diferencial de reformas
real con el riqueza 1:7 regulatorias
sistema atribuible necesarias
sesgado: causalmente al como
brecha de sistema de consecuencia
riqueza que exclusión. directa del
persiste colapso.
después de
la
corrección
del sistema.

Taxonomía General de Aplicaciones
D_vital_crédito: el daño crediticio expresado en horas de vida de
trabajo cristalizado
D_vital_crédito = D_crédito / w_ref [horas de vida cristalizadas en trabajo
no recompensado]
Esta conversión hace visible la dimensión ontológica del daño crediticio. Los
recursos que el sistema sesgado extrajo de las comunidades excluidas
representan horas de trabajo de personas que no se tradujeron en patrimonio
acumulado porque el acceso al instrumento de conversión — el crédito justo
— les fue negado por diseño. El dinero es tiempo de vida cristalizado: negar
el acceso al crédito justo es negar la posibilidad de convertir el tiempo de trabajo
en patrimonio duradero.
Para el redlining: D_vital = (~$9.8 billones de patrimonio truncado) / $8
por hora ≈ 1.2 × 10¹² horas. Más de un billón de horas de vida de trabajo
cristalizado que no se convirtieron en patrimonio acumulado por el diseño del
sistema crediticio. Ese es el número que hace visible que la exclusión crediticia
histórica no fue un problema de política pública secundario: fue uno de los
daños ontológicamente más grandes documentados en la historia financiera de
los Estados Unidos.
AD_i en el dominio crediticio: el ajuste debitor
proporcional
AD_deudor = R*_deudor × (1 − S_deudor) × D_total. Este
es el monto que es jurídicamente exigible al deudor: la fracción
del impago causalmente atribuible a sus condiciones
idiosincráticas. Si el monto reclamado al deudor supera
significativamente el AD_deudor calculado, hay inversión
causal en el sistema de cobro: el deudor está siendo imputado
por más de lo que causó.
AD_sistema = R*_sistema × D_total es la fracción del daño
atribuible al diseño del sistema. Para el acreedor que diseñó
condiciones predatorias: AD_D = R*_D × D_total. Ese
monto es la base de la pretensión de los deudores afectados y
del regulador contra el diseñador del sistema que causó el
impago estructural.

Taxonomía General de Aplicaciones
§8 Límites del método y errores frecuentes de
aplicación
Límites del método en el dominio crediticio y financiero
Límite 1 — El problema de la causalidad reversa en el crédito.
El bajo score crediticio puede ser causado por condiciones
estructurales (que producen el impago), pero el bajo score
también puede causar condiciones estructurales (acceso a
crédito de mayor costo, que produce mayor probabilidad de
impago). Esta retroalimentación hace que la construcción del
grafo causal sea más compleja que en los dominios anteriores,
y que el R* del deudor pueda tanto sobrestimarse como
subestimarse dependiendo de qué parte del ciclo se captura.
Límite 2 — El problema de las variables proxy y la causalidad
mediada. Cuando el sesgo opera a través de proxis (el código
postal como proxy de la historia de segregación racial), la
causalidad es mediada: el algoritmo no causa directamente
discriminación racial — causa discriminación geográfica que
es estadísticamente equivalente a la racial dado el patrón de
segregación histórica. La construcción del grafo causal debe
explicitar esa mediación.
Límite 3 — El R* del entorno macroeconómico en impagos
masivos. En crisis sistémicas, R*_entorno puede dominar el
grafo de impagos. En esos casos, imputar el impago
principalmente al deudor produce la inversión causal más
visible del sistema financiero. Los datos macroeconómicos
necesarios para estimar R*_entorno con rigor requieren series
de tiempo que no siempre están disponibles a nivel de caso
individual.
Límite 4 — La solución regulatoria trasciende el litigio
individual. Cuando el nodo de mayor R* es el dataset o el
marco regulatorio (estructural y sistémico), el análisis identifica
el problema con precisión, pero la reparación proporcional al
daño total requiere acción sistémica: cambio regulatorio,
auditorías obligatorias, programas de compensación colectiva.

Taxonomía General de Aplicaciones
El sistema identifica los nodos de mayor R* y Δ, pero la
política que actúa sobre ellos trasciende el litigio individual.
Errores frecuentes de aplicación
Por qué Consecuen
Error Corrección
ocurre cia
Tratar el El sistema El acreedor Descomponer
impago como de reclama el R*_impago en sus
hecho del evaluación 100% del cuatro
deudor — crediticia daño al componentes con
R*_deudor = usa el score deudor el expediente del
1.0 como cuando caso. AD_deudor
predictor R*_sistema = R*_deudor × (1
del impago puede ser − S_deudor) ×
y lo mayor que D_total es el
convierte R*_deudor. monto
en causa. Inversión jurídicamente
La causal en el exigible al deudor.
correlación sistema de
estadística cobro.
se
confunde
con
causalidad
causal.
Asignar R* al El analista El análisis El dataset y el
nodo incluye el produce una algoritmo son
algorítmico dataset cadena de nodos causales sin
como si tuviera como actor responsabilid voluntad. Su R* se
voluntad y en el grafo ad que no imputa
pudiera ser con R* y α puede íntegramente al
sancionado propios. ejecutarse: el directivo
dataset no aprobador y al
puede ser diseñador de la
sancionado política histórica
ni puede que generó los
asumir. La datos. No tienen α
cadena de ni Hijos.
responsabilid
ad se
interrumpe.

Taxonomía General de Aplicaciones
Por qué Consecuen
Error Corrección
ocurre cia
No calcular El analista R*_efectivo R*_efectivo_direc
R*_efectivo del separa el del directivo tivo =
directivo R* del subestimado. R*_directivo +
incluyendo directivo La R*_dataset × P
R*_dataset del R* del responsabilid (detección |
dataset sin ad del auditoría). Estimar
calcular directivo P desde el análisis
cuánto parece de disparate
habría menor de lo impact CF2 del
podido que la período: ¿qué
detectar el causalidad habría detectado
directivo justifica una auditoría
con una porque no se estándar?
auditoría. incluye la
fracción del
dataset que
habría
podido
corregir.
Usar el ICRS El analista El ICRS El ICRS requiere
individual de calcula el subestimado el grafo de
una institución riesgo de la o interdependencias
sin el contexto institución sobreestimad del sistema
del sistema de sin mapear o. Una completo, no solo
interdependen su posición institución el riesgo individual
cias en la red de puede tener de cada nodo. El
dependenci riesgo análisis del colapso
as del individual sistémico es
sistema bajo pero sistémico por
financiero. ICRS alto definición.
porque su
colapso
activa
cascadas que
la institución
sola no
explicaría.
§9 Guía de prioridades de recolección de
evidencia

Taxonomía General de Aplicaciones
Si tu prioridad es saber qué buscar primero para reducir la
incertidumbre más relevante de tu caso crediticio o financiero,
usa la tabla y el árbol que siguen. La primera decisión siempre
es identificar el análisis: impago individual, sesgo algorítmico,
o colapso sistémico.
Tabla de prioridades de recolección de evidencia crediticia
y financiera
Si tu Qué
incertid La evidencia Qué buscar /
Por qué
umbre que más la rango qué
funciona
principa reduce es… reduce pregunt
l es… ar
1. ¿El Análisis de Si las Reduce ¿Cuál era
impago capacidad de condicione rango de la
era servicio de la s hacían el R*_deud relación
atribuible deuda CF2: pago or vs pago/ing
al deudor ¿las objetivame R*_prod reso del
o al condiciones nte inviable ucto deudor al
sistema del producto dado el (incertid moment
crediticio (tasa, plazo, perfil del umbre o de la
? pago mensual) deudor → empírica) aprobaci
eran R*_produc ón? ¿El
razonablement to alto → producto
e pagables la acción de era
dado el perfil cobro estándar
de ingresos del íntegra del sector
deudor al contra el o tenía
momento de la deudor no condicio
aprobación? tiene base nes
Comparación causal atípicas?
con productos proporcion ¿Había
equivalentes al. opciones
del mercado. de
renegoci
ación
disponibl
es que el
acreedor
no
ofreció?

Taxonomía General de Aplicaciones
Si tu Qué
incertid La evidencia Qué buscar /
Por qué
umbre que más la rango qué
funciona
principa reduce es… reduce pregunt
l es… ar
2. ¿El Análisis CF4 Sin análisis Determi ¿Hay
algoritm de tasas de cuantitativ na si hay datos del
o aprobación y o sesgo tipo
producía condiciones comparativ algorítmi HMDA
disparate por grupo o, la co y el u
impact controlando discriminac nivel CF equivalen
contra un por perfil ión de la te para
grupo crediticio algorítmica evidencia analizar
con perfil objetivo. Si el no es (incertid las tasas
compara diferencial es demostrabl umbre de
ble? estadísticamen e con empírica) aprobaci
te significativo certeza. El ón por
→ CF4. análisis grupo?
Peritaje CF2 CF4 es la ¿La
que establece puerta de institució
el mecanismo entrada; el n tiene
causal si el peritaje documen
análisis supera CF2 es el tación
CF4. instrument del
o que proceso
establece la de
causalidad. aprobaci
ón y de
las
variables
usadas
por el
algoritm
o?
3. ¿El Comunicacion El Hijo Reduce ¿Hay
directivo es internas dominante rango de correos
tenía CF1 que determina S del internos
conocimi muestran si el el tipo de directivo del
ento del directivo culpabilida (incertid directivo
sesgo — recibió alertas d y el tipo umbre sobre el
Hijo de equidad o de ontológic algoritm
dominan de riesgo. La solución. a) o o el
te del distinción Potós → producto
directivo Anteros/Potó solución ?
? s/Deimos regulatoria. ¿Recibió
desde esas Anteros → adverten
comunicacion proceso cias de

Taxonomía General de Aplicaciones
Si tu Qué
incertid La evidencia Qué buscar /
Por qué
umbre que más la rango qué
funciona
principa reduce es… reduce pregunt
l es… ar
es (§3.1) penal. equidad
determina si el Deimos → o de
proceso es negligencia riesgo?
penal o civil y ¿Actuó
regulatorio. cambio de sobre
proceso. ellas o las
desestim
ó? ¿Cuál
era la
práctica
estándar
del sector
en ese
período?
4. ¿Cuál Análisis CF2 R*_efectiv Establec ¿Qué
es el del disparate o = e la magnitud
R*_efecti impact + R*_directi magnitud tenía el
vo del documentació vo + de la disparate
directivo n CF1 del R*_dataset responsa impact
incluyen proceso de × bilidad documen
do el R* aprobación. P(detecció del tado?
del P(detección | n). Si P ≈ directivo ¿Había
dataset? auditoría) se 0.90 (sesgo (incertid herramie
estima desde la de alta umbre ntas de
magnitud del magnitud), empírica) auditoría
disparate el directivo estándar
impact tiene disponibl
documentado responsabil es en el
y la idad sector en
disponibilidad efectiva ese
de dominante período?
herramientas sobre el ¿El
de auditoría sesgo del directivo
estándar en el algoritmo. las usó
período. para
otros
sistemas
del
portafoli
o?

Taxonomía General de Aplicaciones
Si tu Qué
incertid La evidencia Qué buscar /
Por qué
umbre que más la rango qué
funciona
principa reduce es… reduce pregunt
l es… ar
5. ¿Qué Construcción El ICRS Identifica ¿Qué
nodo del del grafo de identifica el el nodo institució
sistema interdependen eslabón de mayor n,
financier cias CF2: crítico del posición instrume
o tenía mapear las sistema — causal en nto o
mayor exposiciones el nodo sin el política
ICRS en cruzadas entre cuyo colapso tenía
el nodos, las colapso la (incertid mayor
colapso? cláusulas de crisis no umbre exposició
activación en habría sistémica n
cascada, y las alcanzado ) cruzada
dependencias esa escala. con el
de liquidez Sin el grafo resto del
entre de sistema?
instituciones. interdepen ¿Cuáles
El ICRS se dencias, el eran las
calcula sobre análisis del cláusulas
ese grafo. colapso de
solo puede activació
atribuir n en
causalidad cascada?
a los nodos ¿Qué
visibles (los habría
que ocurrido
quebraron) si ese
no a los nodo
que específic
hicieron o hubiera
inevitable sido
la quiebra rescatado
sistémica. o
eliminad
o antes
del
colapso?
6. ¿Cuál Análisis de El Establec ¿Hay
es el brecha D_vital_cr e la escala datos de
D_crédit patrimonial édito = del registro
o de la CF2: D_crédito argument de
comunid diferencial de / w_ref o de propieda
ad acumulación hace visible reparació des del
excluida de riqueza la n período

Taxonomía General de Aplicaciones
Si tu Qué
incertid La evidencia Qué buscar /
Por qué
umbre que más la rango qué
funciona
principa reduce es… reduce pregunt
l es… ar
— base entre el grupo magnitud (incertid del
del excluido y el del daño en umbre sistema
argument grupo horas de empírica de
o de comparable trabajo e exclusión
reparació con acceso al cristalizado histórica) ? ¿Hay
n? crédito justo, . Sin esa datos de
durante el conversión riqueza
período de , la brecha comparat
exclusión. El patrimonia iva actual
análisis l puede entre
histórico del parecer un grupos
tipo del diferencial que
redlining usa económico permitan
los mapas abstracto. establece
históricos de r el
exclusión y los diferenci
registros de al
transferencias atribuible
inmobiliarias al
del período. sistema?
¿El
perito
puede
construir
el
escenario
contrafác
tico de
acumulac
ión sin
exclusión
?
Árbol de decisión crediticio: ¿qué buscar primero?
El árbol comienza con la identificación del análisis: impago
individual, sesgo algorítmico, o colapso sistémico.

Taxonomía General de Aplicaciones
¿Cuál es tu análisis principal?
├─ Análisis del impago individual: ¿R*_deudor o
R*_sistema?
│
└─ PRIORIDAD: Análisis de capacidad de servicio
CF2 + condiciones del producto CF1.
· ¿Pago/ingreso > 40% al momento de la aprobación? →
R*_producto significativo.
· ¿El producto tenía condiciones atípicas del sector? →
peritaje CF2 del diseño del producto.
· AD_deudor = R*_deudor × (1 − S_deudor) ×
D_total. Si es < monto reclamado → inversión causal en el
cobro.
├─ Análisis del sesgo algorítmico: ¿disparate impact y
R*_efectivo del directivo?
│
└─ PRIORIDAD 1: Análisis CF4 de disparate impact
con datos HMDA u equivalente.
· ¿El diferencial de tasas de aprobación es estadísticamente
significativo controlando por perfil?
· Si sí → peritaje CF2 del mecanismo causal del sesgo.
· PRIORIDAD 2: Comunicaciones internas CF1 del
directivo para determinar Hijo (§3.1).
· Potós → solución regulatoria (auditoría obligatoria).
Anteros → proceso penal-civil.
· R*_efectivo_directivo = R*_directivo + R*_dataset ×
P (detección | auditoría).
└─ Análisis del colapso sistémico: ¿qué nodo tenía mayor
ICRS?
└─ PRIORIDAD: Grafo de interdependencias CF2
del sistema financiero en el período.
· Mapear exposiciones cruzadas entre instituciones y
cláusulas de activación en cascada.
· ICRS_i = R*_i sobre el grafo de interdependencias.
El nodo de mayor ICRS era condición necesaria del colapso a
esa escala.

Taxonomía General de Aplicaciones
· El colapso no fue fracaso de voluntad individual: fue
fracaso de la arquitectura del sistema. La solución es
sistémica.
— Fin del Capítulo 11 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

