## PARTE II · Ciencias Económicas y Financieras

### Capítulo 17
Plataformas digitales —
economía de datos y responsabilidad
algorítmica
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Nivel C. Sus rangos son candidatos. La aportación central
es conceptual: la jerarquía de responsabilidad algorítmica, la doctrina del
diseñador de la métrica como nodo de mayor R*, y la estructura del grafo de
la plataforma digital. Antes de usar los rangos en una pretensión formal,
ajustar con evidencia empírica específica del caso.
Este capítulo integra dos líneas analíticas. La primera, derivada de El cálculo
de la responsabilidad cap. 13 (IA y algoritmos de decisión): la responsabilidad
en el sistema algorítmico está invertida respecto a la visibilidad — el
componente más visible (el modelo) tiene R* más bajo; el más invisible (quien
definió la métrica que el modelo optimiza) tiene R* más alto. La segunda,
extensión al dominio de plataformas: la plataforma que diseñó el algoritmo de
recomendación, la política de monetización de datos y la arquitectura de
moderación de contenidos tiene R* sobre los daños que esas decisiones producen
en los usuarios. Para la evidencia del sesgo algorítmico, ve a §2. Para el mapa
de nodos del grafo de la plataforma, ve a §5. Para la prioridad de evidencia,
ve a §9.
§1 Descripción del subcampo
Las plataformas digitales introducen en el sistema de
imputación causal una arquitectura de R* que invierte la

Taxonomía General de Aplicaciones
jerarquía de visibilidad con más fuerza que cualquier dominio
anterior. El usuario que publicó el contenido dañino es el nodo
más visible documentalmente. El modelo que lo amplificó es
el nodo de visibilidad intermedia. El diseñador de la métrica
de engagement que el modelo optimizaba — el ejecutivo que
decidió que el objetivo del algoritmo era maximizar el tiempo
en pantalla o la reacción emocional — es el nodo menos
visible y el de mayor R*.
La razón es el principio algorítmico del cap. 13 de El cálculo
de la responsabilidad: el modelo tiene S ≈ 1.0 porque cualquier
modelo competente entrenado con la misma métrica y el
mismo dataset de comportamiento de usuarios habría
aprendido los mismos patrones de amplificación del
contenido emocionalmente intenso. Cambiar el modelo no
resuelve el daño — lo resuelve cambiar la métrica que el
modelo optimiza. Y quien define esa métrica tiene R* alto con
S bajo: la elección de "maximizar el tiempo en pantalla" versus
"maximizar el bienestar informativo del usuario" era una
elección deliberada entre alternativas disponibles con
consecuencias distribucionales distintas.
El principio del diseñador de la métrica en el dominio de
plataformas digitales
En toda plataforma digital, el acto de mayor R* no es el que escribe el código
del algoritmo — es el que define qué objetivo optimiza ese algoritmo. En la
plataforma de redes sociales que amplifica contenido emocionalmente
polarizador porque ese contenido produce mayor engagement, el diseñador de
la métrica de engagement (el ejecutivo que decidió que "engagement" =
"tiempo en pantalla" o "reacciones emocionales") tiene R* mayor que el
equipo técnico que construyó el modelo.
La misma lógica aplica al sistema de recomendación que amplifica contenido
de desinformación (la métrica target era clics o tiempo en pantalla, no precisión
informativa), al sistema de precios dinámicos que discrimina por código postal
(la métrica target era maximizar ingresos, no equidad en el acceso), y al
sistema de moderación de contenidos que tiene disparate impact por idioma o
cultura (la métrica target definía "contenido dañino" en función de los
patrones del dataset de entrenamiento, que sobrerepresentaba idiomas con más
datos de moderación histórica).

Taxonomía General de Aplicaciones
Sub-variantes del dominio
Sistemas de recomendación con amplificación de contenido
dañino: el algoritmo de recomendación de una plataforma
amplificó sistemáticamente contenido que produce daño
documentable — desinformación de salud pública, contenido
que radicaliza a los usuarios hacia posiciones extremas,
material que explota características de vulnerabilidad
psicológica. El daño no es del usuario que publicó el
contenido: es de la plataforma que lo amplificó mediante la
optimización de la métrica de engagement. Nivel C — la
causalidad entre la amplificación y el daño downstream es el
componente de mayor incertidumbre.
Uso indebido de datos personales y violación de privacidad: la
plataforma recopiló datos de comportamiento de usuarios
(navegación, preferencias, relaciones sociales) y los usó o
comercializó de maneras que los usuarios no autorizaron
explícitamente o que excedían el alcance de lo que
razonablemente podían anticipar dado el diseño de la interfaz.
El R* de la plataforma depende de si el diseño de la interfaz
(dark patterns) fue condición causal de que los usuarios no
entendieran a qué datos estaban dando acceso.
Discriminación algorítmica en precios, anuncios y acceso a
servicios: el algoritmo de precios, de targeting publicitario o de
acceso a servicios produjo resultados con disparate impact —
cargando más a usuarios de ciertos grupos demográficos,
mostrando anuncios de servicios financieros de mayor costo a
usuarios de menor ingreso, o negando acceso a vivienda o
empleo de manera sistemática a grupos protegidos. El
diseñador de la métrica de optimización tiene R* por ese
disparate impact cuando el daño era previsible dado el diseño.
Poder de mercado de plataformas y daño competitivo: la
plataforma usó su posición dominante y su acceso privilegiado
a los datos de los competidores que operan en su ecosistema
para darles un trato menos favorable — rebajando el alcance
de su contenido, copiando sus productos, o ajustando los

Taxonomía General de Aplicaciones
algoritmos de búsqueda para favorecer los propios servicios.
El R* de la plataforma en el daño a los competidores depende
de la documentación de las decisiones algorítmicas que
produjeron ese trato diferencial.
Daño a menores por diseño: la plataforma diseñó mecanismos
de engagement — notificaciones, likes, métricas de
popularidad, ciclos de recompensa variable — que son
funcionalmente adictivos, aplicados a usuarios menores sin las
salvaguardas necesarias. El R* de la plataforma es alto cuando
el diseño de esos mecanismos era su decisión deliberada y
cuando había evidencia disponible de sus efectos en el
bienestar de menores antes de su implementación a escala.
Responsabilidad de la plataforma por contenidos de terceros:
la plataforma hospeda, indexa, o amplifica contenido de
terceros que produce daño — difamación, violación de
derechos de autor, material de abuso sexual de menores. La
distribución de R* entre el creador del contenido y la
plataforma depende de si la plataforma tenía conocimiento del
contenido dañino y de si la arquitectura de moderación era
adecuada para detectarlo a la escala de su operación.
§2 Escala de evidencia PD0–PD8 · Plataformas
digitales y economía de datos
La escala PD0–PD8 traduce la jerarquía general E0–E8 al
vocabulario de las plataformas digitales. Su característica más
relevante es la posición central de la auditoría algorítmica
(PD2) — el instrumento que establece la cadena causal entre
las decisiones de diseño de la plataforma y los resultados
dañinos en los usuarios. Sin auditoría algorítmica, la mayoría
de las aristas del grafo de la plataforma permanecen en
PD5/PD6, porque las decisiones de diseño de las métricas y
los algoritmos raramente se documentan en registros públicos.
Nivel C — rangos candidatos, pendientes de calibración
empírica formal.

Taxonomía General de Aplicaciones
Descripción y
Rango w
Nive Tipo de ejemplos en el
(candidato
l evidencia dominio de
)
plataformas digitales
PD1 Documento Comunicaciones [0.72, 0.90]
interno de la internas (correos,
plataforma que documentos de
establece las producto) donde la
decisiones de plataforma tomó las
diseño decisiones de diseño de
relevantes la métrica, del algoritmo
o de la política de datos;
documentación de las
pruebas A/B que
establecían el efecto de
las decisiones de diseño
en los usuarios antes de
la implementación a
escala; actas del comité
de ética o de confianza y
seguridad que
discutieron los riesgos
del diseño; registros de
la decisión de escalar el
sistema sin implementar
las salvaguardas
recomendadas
internamente.
PD2 Auditoría Análisis pericial que [0.62, 0.82]
algorítmica establece: (a) qué
independiente o métrica optimiza el
peritaje técnico algoritmo, si esa métrica
especializado es la causa próxima del
resultado dañino y
cuáles eran las
alternativas disponibles
con menor impacto; (b)
análisis de disparate
impact del sistema — si
los resultados del
algoritmo afectan
desproporcionadament
e a grupos protegidos;
(c) reconstrucción de la
cadena causal entre el
diseño de la plataforma
y el daño documentado

Taxonomía General de Aplicaciones
Descripción y
Rango w
Nive Tipo de ejemplos en el
(candidato
l evidencia dominio de
)
plataformas digitales
en los usuarios; (d)
análisis del S del
modelo: si cualquier
modelo competente
con la misma métrica y
dataset habría
producido el mismo
resultado.
PD3 Testimonios Declaraciones de [0.48, 0.66]
convergentes de múltiples exempleados
exempleados o o investigadores que
investigadores describen
con consistentemente las
corroboración decisiones de diseño y
documental su impacto conocido,
con al menos un
documento interno
consistente. Las
whistleblower
disclosures como la de
Frances Haugen en
Facebook (2021) son el
caso paradigmático de
evidencia PD3 con alto
impacto.
PD4 Análisis Análisis que muestra [0.38, 0.58]
estadístico del que el sistema de la
comportamient plataforma produce
o del sistema y resultados con patrones
sus efectos estadísticamente
documentados incompatibles con un
sistema neutral —
disparate impact
documentado,
amplificación
sistemática de ciertas
categorías de contenido,
correlación estadística
entre el uso del
algoritmo y métricas de
daño en los usuarios
(salud mental,

Taxonomía General de Aplicaciones
Descripción y
Rango w
Nive Tipo de ejemplos en el
(candidato
l evidencia dominio de
)
plataformas digitales
radicalización,
desinformación).
PD5 Análisis Documentación de que [0.28, 0.48]
comparativo del el diseño de la
diseño de la plataforma se apartaba
plataforma de las prácticas del
versus sector para ese tipo de
estándares del sistema, o de que ignoró
sector o mejores recomendaciones de
prácticas organismos técnicos o
académicos disponibles
al momento del diseño.
PD6 Inferencia La plataforma tenía la [0.18, 0.38]
estructural por posición, el control del
posición de la algoritmo y los datos
plataforma en el para haber anticipado el
grafo del daño impacto dañino de sus
decisiones de diseño,
sin documentación
directa de que lo
anticipó o lo ignoró
deliberadamente.
PD7 Correlación Los cambios de diseño [0.07, 0.24]
temporal entre de la plataforma
cambios de coinciden
diseño y efectos temporalmente con
documentados cambios en las métricas
sin análisis de daño en los usuarios
causal sin análisis que
establezca la cadena
causal específica versus
factores confusos.
PD8 Especulación Afirmación de que la [0.00, 0.12]
sobre el impacto plataforma causó el
sin daño sin
documentación documentación del
del mecanismo mecanismo específico
ni análisis del sistema.

Taxonomía General de Aplicaciones
Descripción y
Rango w
Nive Tipo de ejemplos en el
(candidato
l evidencia dominio de
)
plataformas digitales
PD0 Ausencia Auditoría algorítmica w = 0.00
documentada de que establece que el
conexión causal resultado dañino no
tiene relación causal con
el diseño del sistema de
la plataforma, o que el
diseño de la plataforma
era consistente con las
mejores prácticas
disponibles y el daño era
imprevisible dado el
estado del
conocimiento en el
momento del diseño.
La asimetría de información en el dominio de plataformas:
el problema del acceso a los datos
La mayor parte de la evidencia sobre el impacto de los algoritmos de las
plataformas está en manos de la plataforma misma: los logs de actividad de
los usuarios, los registros del comportamiento del algoritmo, los resultados de
los experimentos A/B y los documentos de diseño son propiedad de la
plataforma y raramente están disponibles para investigadores externos. Esa
asimetría de información produce una brecha entre la evidencia PD1/PD2
que es la más valiosa para el análisis y la evidencia PD4/PD5 que es
frecuentemente la única disponible sin filtraciones internas. El analista debe
declarar explícitamente cuándo la calidad de su evidencia está limitada por
esta asimetría.
§3 Los Hijos de Afrodita en el dominio de
plataformas digitales
En el dominio de plataformas digitales, los Hijos de Afrodita
aplican a los ejecutivos y directivos que tomaron las decisiones
de diseño del algoritmo, de la métrica y de la política de datos
— no al algoritmo como nodo sin voluntad, no al dataset
como nodo técnico, y no al modelo de aprendizaje automático.

Taxonomía General de Aplicaciones
La restricción es la misma que en los cap. 11 (crédito), cap. 12
(quiebra) y cap. 13 de El cálculo (IA y algoritmos): los sistemas
técnicos sin voluntad tienen R* pero no tienen Hijos.
§3.1 Hijos de legibilidad alta en el dominio de plataformas
Qué
informa Firma en el Error de
Fuente
para S del expediente discrimina
Hijo document
ejecutivo de la ción
al típica
de plataforma frecuente
plataforma
Anter S bajo [0.05, Documento Correos o Confundir
os 0.28]. El s internos documento con Potós
ejecutivo donde el s internos cuando el
tomó ejecutivo del ejecutivo
decisiones reconoce el ejecutivo siguió las
deliberadas impacto durante el prácticas
de diseño dañino del período de estándar de
sabiendo diseño y la decisión. la industria
que decide Resultados en ese
producirían implementa de período. La
daño a rlo de todas experiment pregunta
usuarios o a formas. os A/B con discriminan
terceros, Resultados las métricas te: ¿el
pero las de de daño ejecutivo
mantuvo experiment medidas. diseñó
porque os A/B que Actas del específicam
servían a los mostraban comité de ente el
objetivos de el daño y ética o de mecanismo
negocio de la que el confianza y dañino, o
plataforma. ejecutivo seguridad replicó
La decisión usó para con las prácticas
fue optimizar el decisiones que eran
genuinament engagement de la generalizad
e en lugar de dirección. as en el
idiosincrátic corregir el sector de
a: otros diseño. plataformas
ejecutivos Decisiones en ese
con el de escalar momento?
mismo sistemas
conocimient después de
o técnico, el recibir

Taxonomía General de Aplicaciones
Qué
informa Firma en el Error de
Fuente
para S del expediente discrimina
Hijo document
ejecutivo de la ción
al típica
de plataforma frecuente
plataforma
mismo rol y advertencias
la misma internas de
información daño.
no habrían Respuestas a
tomado la recomendac
misma iones del
decisión. equipo de
ética que
fueron
rechazadas.
Potó S moderado- Prácticas de Document Confundir
s alto [0.42, diseño que os del con
0.75]. El eran sector Anteros
ejecutivo generalizada sobre las cuando el
siguió las s en el sector prácticas ejecutivo
prácticas de estándar. recibió
establecidas plataformas Comparaci evidencia
de la en el ón con las específica
industria de período. decisiones del daño y
plataformas Ausencia de de diseño la ignoró
— cuestionami de activament
"maximizar ento del plataformas e. Si hay
el modelo de comparable documento
engagement negocio s en el s donde el
", "crecer los basado en mismo ejecutivo
DAUs" — engagement período. desestimó
sin . Cultura de Cultura advertencia
cuestionar producto corporativa s de daño
sus impactos que del sector por escrito,
downstream maximizaba tech en el Anteros
sobre los métricas de período moderado
usuarios. La crecimiento analizado. es más
conducta era sin medir preciso que
deliberada métricas de Potós.
pero no bienestar de
idiosincrátic usuarios.
a: cualquier
ejecutivo de
plataforma
con la misma
cultura de

Taxonomía General de Aplicaciones
Qué
informa Firma en el Error de
Fuente
para S del expediente discrimina
Hijo document
ejecutivo de la ción
al típica
de plataforma frecuente
plataforma
negocio y los
mismos
KPIs habría
tomado las
mismas
decisiones
de diseño.
Fobo S moderado- Comunicaci Comunicaci Confundir
s alto [0.55, ones que ones del con
0.82]. El documentan ejecutivo Anteros
ejecutivo la presión con el cuando el
implementó sobre el consejo. ejecutivo
diseños ejecutivo: OKRs tenía
dañinos bajo objetivos de documenta libertad real
la presión de crecimiento dos de la para
las métricas de DAUs, empresa. diseñar de
de presión del Análisis manera
crecimiento, consejo para competitiv diferente. Si
del consejo mantener el os internos. el análisis
de ritmo Presión de otras
administraci competitivo documenta plataformas
ón o de la , da del muestra
competencia comparacio mercado de que las
con otras nes capitales alternativas
plataformas. explícitas sobre el de diseño
El miedo a con las crecimiento eran viables
quedar métricas de de usuarios. sin
rezagado plataformas sacrificar
competitiva competidor competitivi
mente as que dad, la
determinó la usaban los presión
decisión de mismos sistémica
priorizar el mecanismos no es
engagement . suficiente
sobre el para Fobos
bienestar de dominante.
los usuarios.
La presión
del entorno
era
condición

Taxonomía General de Aplicaciones
Qué
informa Firma en el Error de
Fuente
para S del expediente discrimina
Hijo document
ejecutivo de la ción
al típica
de plataforma frecuente
plataforma
causal de la
decisión.
§3.2 Hijos de legibilidad baja en el dominio de plataformas
Deimos: puede aparecer en ejecutivos que no comprendían las
implicaciones del diseño algorítmico en el bienestar de los
usuarios — el director de producto que aprobó el sistema de
notificaciones sin comprender los mecanismos de adicción
que activaría, o el ejecutivo que no tenía el marco conceptual
para interpretar los datos de salud mental que el sistema estaba
produciendo. S alto cuando la brecha de conocimiento era
genuina y consistente con la formación del ejecutivo. Asignar
con nota obligatoria de incertidumbre alta dado el ritmo de
evolución del conocimiento en el dominio.
Harmonía en el dominio de plataformas: el ejecutivo,
investigador o empleado que reportó internamente (o
externamente, como whistleblower) las consecuencias dañinas
del diseño a pesar de las consecuencias personales. Las
whistleblower disclosures (Frances Haugen / Facebook, 2021)
son el patrón canónico de Harmonía en el dominio. α alto.
Posible reconocimiento como testigo protegido. El valor de
las disclosures para el sistema de justicia trasciende el caso
individual: permite construir evidencia PD1 que de otra forma
sería inaccesible.
§3.3 El modelo, el dataset y el algoritmo no tienen Hijo —
la jerarquía de R* invertida
Principio algorítmico de El cálculo de la responsabilidad cap. 13: El modelo
tiene S ≈ 1.0 porque cualquier modelo competente entrenado con la misma

Taxonomía General de Aplicaciones
métrica y el mismo dataset habría producido el mismo resultado. Cambiar el
modelo no resuelve el problema si la métrica y el dataset permanecen.
R*_modelo × (1 − S_modelo) ≈ 0. La reforma regulatoria que se enfoca en
la "explicabilidad del modelo" sin abordar la elección de la métrica es análoga
a reformar el traductor sin corregir el texto original.
La jerarquía de responsabilidad algorítmica en el dominio de plataformas:
R*_diseñador_métrica > R*_dataset_histórico > R*_desplegador >
R*_modelo. Esta jerarquía invierte la jerarquía de visibilidad: el modelo es
el más visible en las auditorías técnicas; el diseñador de la métrica es el menos
visible en los documentos públicos. La responsabilidad algorítmica requiere
acceso a los documentos de decisión de la métrica, no solo a la especificación
técnica del modelo.
§4 ¿Qué cuenta como asunción (α) en el
dominio de plataformas digitales?
α de la plataforma mide lo que la empresa ha hecho
concretamente sobre su posición causal: rediseño de la métrica
que el algoritmo optimiza para reducir el daño,
implementación de auditorías de equidad antes del despliegue,
reforma de la política de datos para alinearse con el
consentimiento informado real de los usuarios, cooperación
con investigadores independientes para establecer el impacto
del diseño.
α de la plataforma es completamente independiente del dolo
Una plataforma que diseñó deliberadamente mecanismos de engagement que
producen daño puede tener α alto si después rediseñó la métrica, implementó
salvaguardas verificables y cooperó activamente con reguladores e
investigadores. Una plataforma que replicó prácticas del sector sin intención
deliberada de dañar puede tener α = 0 si nunca auditó ni reformó sus sistemas
una vez que la evidencia del daño era disponible. Los Hijos informan S del
diseñador; α mide lo que la plataforma hizo después sobre su posición causal.

Taxonomía General de Aplicaciones
Acción de la ¿Cuenta Tipo de
Razón
plataforma para α? α
Rediseño de la Sí — α Es la acción de mayor Voluntari
métrica de estructural impacto causal: actúa o o
optimización alto sobre el nodo de requerid
para incluir mayor R* (la o
métricas de métrica). El rediseño
bienestar verificable de la
además de métrica reduce
métricas de directamente el
engagement R*_plataforma
futuro.
Auditoría Sí — α de La auditoría Voluntari
algorítmica transparencia independiente reduce o o
independiente la asimetría de requerid
con información que es el o
publicación de mayor obstáculo para
los resultados establecer la cadena
causal del daño. Su
publicación permite
la verificación
externa.
Implementaci Sí — α de Las salvaguardas para Voluntari
ón de protección grupos vulnerables o o
salvaguardas específica son el α más urgente regulatori
para usuarios cuando el daño o
menores con documentado afecta
mecanismos desproporcionadame
verificables nte a menores.
Apertura de Sí — α de El acceso a datos Voluntari
datos a cooperación para investigadores o
investigadores con la reduce la brecha
independiente investigación PD4/PD6 a PD2,
s para estudiar permitiendo
el impacto del establecer la cadena
algoritmo causal con mayor
certeza.
Reforma de la Sí — α de Los dark patterns de Voluntari
política de rectificación consentimiento son o o
privacidad y del diseño de una fuente autónoma requerid
de los dark consentimien de R* de la o
patterns de to plataforma. Su
consentimient reforma es α directo
o

Taxonomía General de Aplicaciones
Acción de la ¿Cuenta Tipo de
Razón
plataforma para α? α
sobre esa posición
causal.
Pagos a No El pago que suprime —
investigadores la evidencia no es α
bajo acuerdo — es la continuación
de del daño. Su impacto
confidencialid sobre el R*_neta del
ad que impide diseñador es negativo
la publicación (reduce α a futuro
de hallazgos cuando la supresión
adversos se documenta).
Comunicado No modifica Declaración sin —
de α consecuencia
"compromiso concreta sobre el
con la diseño del sistema.
seguridad de No reduce
los usuarios" R*_métrica ni
sin cambios R*_desplegador.
de diseño
verificables
La escala de α de la plataforma
Rango Descripción
Nivel Indicadores
α observable
Negación / 0.00 – La plataforma Sin auditorías
resistencia activa 0.05 niega el daño, externas. Sin
combate rediseño de
activamente las métricas.
investigaciones y Litigación activa
no ha contra
implementado reguladores e
ningún cambio investigadores.
verificable de Supresión de
diseño. investigación
interna.
Reconocimiento 0.06 – La plataforma Comunicados de
nominal 0.20 reconoció el responsabilidad

Taxonomía General de Aplicaciones
Rango Descripción
Nivel Indicadores
α observable
impacto del publicados. Sin
daño, pero sin cambios de
cambios diseño
concretos documentados.
verificables. Sin acceso a datos
Comunicados de para
"bienestar de investigadores
usuarios" sin independientes.
rediseño.
Asunción parcial 0.21 – La plataforma Algunas
0.45 implementó salvaguardas para
algunas menores
salvaguardas implementadas.
menores, abrió Acceso limitado a
acceso limitado a investigadores en
investigadores o condiciones
ajustó restringidas.
parcialmente el Ajustes menores
diseño de la de la métrica sin
métrica. reforma
estructural.
Asunción activa 0.46 – La plataforma Rediseño de la
en proceso 0.70 está métrica en
implementando proceso con
reformas métricas de
sustanciales de bienestar
diseño con incorporadas.
seguimiento Auditoría
verificable y independiente
cooperando activa con
activamente con resultados
reguladores. publicados.
Apertura
sustancial de
datos a
investigadores.
Asunción 0.71 – Las reformas de Reducción
funcional 0.89 diseño son verificable de las
sustanciales y métricas de daño
verificables. Las post-rediseño.
métricas de daño Auditoría
han caído de independiente
manera con resultados

Taxonomía General de Aplicaciones
Rango Descripción
Nivel Indicadores
α observable
documentable positivos
posterior al publicados.
rediseño. Cooperación
activa con
reguladores
documentada.
Asunción plena 0.90 – La plataforma Reforma
1.00 rediseñó la estructural del
métrica, diseño
implementó verificable.
auditorías Auditorías
permanentes, permanentes
abrió datos a independientes.
investigadores y Datos
cooperó disponibles para
plenamente con investigación.
reguladores. Cooperación
regulatoria
documentada.
§5 Construcción del grafo típico del dominio
de plataformas
La jerarquía del grafo algorítmico de la plataforma
R*_diseñador_métrica > R*_contexto_histórico > R*_dataset >
R*_desplegador > R*_modelo
Esta jerarquía es el principio más importante del capítulo. El modelo (el
código que ejecuta el algoritmo de recomendación o de moderación) tiene S ≈
1.0 porque es sustituible: cualquier modelo competente con la misma métrica
y el mismo dataset habría producido el mismo resultado. Su R*_neta ≈ 0.
El diseñador de la métrica tiene S bajo porque la elección de qué variable
optimiza el sistema es una decisión normativa entre alternativas con
consecuencias distribucionales distintas — no hay una única respuesta
técnicamente correcta.

Taxonomía General de Aplicaciones
Tipos de nodo en el grafo de la plataforma
Función en el Ejemplo en el
Tipo S típico
grafo dominio
Diseñador de la El ejecutivo o Bajo- El equipo de
métrica (DM) equipo que moderad producto que
tomó la o [0.15– definió
decisión 0.55] "engagement"
normativa de como tiempo en
qué variable pantalla o
optimiza el número de
algoritmo de la reacciones
plataforma. Es emocionales. El
el nodo de ejecutivo que
mayor R* del decidió usar el
grafo. Sus Hijos historial de clics
informan S. de los usuarios
Anteros: eligió como proxy del
la métrica interés sin ajustar
sabiendo sus por el sesgo de
consecuencias selección. El
dañinas. Potós: directivo que
siguió las aprobó la política
prácticas del de datos que
sector sin permitía la venta
cuestionarlas. de datos de
comportamiento
sin
consentimiento
granular.
Contexto Las estructuras N/A — Las prácticas
histórico históricas de no es históricas de
generador del desigualdad, actor moderación de
sesgo (CH) discriminación individual contenidos que
o generaron
desinformación datasets de
que generaron entrenamiento
los patrones en con
los datos con subrepresentació
los que el n de ciertos
algoritmo fue idiomas y
entrenado. culturas. Los
Nodo sin patrones
voluntad históricos de
individual con acceso desigual al
R* positivo. crédito que

Taxonomía General de Aplicaciones
Función en el Ejemplo en el
Tipo S típico
grafo dominio
Análogo al informan los
redlining datasets de
histórico del scoring crediticio
cap. 11 de la plataforma
(crédito): de pagos.
transmite el
sesgo al
presente a
través del
dataset.
Dataset de Los datos de Variable El dataset de
comportamient comportamient [0.40– clics de los
o (DB) o de usuarios 0.85] usuarios de
(clics, tiempo de YouTube
visualización, entrenado para el
interacciones) sistema de
con los que el recomendación.
algoritmo fue El dataset de
entrenado. moderación
Nodo sin histórica de
voluntad. S Facebook con
depende de si el subrepresentació
sesgo del n de idiomas no
dataset es europeos. El
genérico a dataset de
cualquier comportamiento
dataset de ese de usuarios de
tipo (S alto) o TikTok que
específico de incluye datos de
cómo fue menores sin
recopilado y salvaguardas de
curado por la edad.
plataforma (S
bajo).
Desplegador El equipo o Moderad El equipo de
del sistema ejecutivo que o [0.30– ingeniería que
(DS) tomó la 0.65] desplegó el
decisión de algoritmo de
desplegar el recomendación a
sistema en escala sin
producción auditoría de
sobre usuarios equidad previa.
reales. R* El ejecutivo que
positivo cuando aprobó el

Taxonomía General de Aplicaciones
Función en el Ejemplo en el
Tipo S típico
grafo dominio
desplegó sin las despliegue del
auditorías de sistema
equidad que el COMPAS a
tamaño del pesar de conocer
impacto los problemas de
requería, o equidad
cuando documentados
desplegó internamente.
después de
haber recibido
evidencia de
impacto
negativo y no
implementó las
salvaguardas
necesarias.
Modelo El sistema de Muy alto El algoritmo de
algorítmico aprendizaje [0.88– recomendación
(MA) automático que 1.00] de YouTube. El
optimiza la sistema de
métrica usando scoring de
el dataset. Nodo COMPAS. El
sin voluntad sistema de
con S ≈ 1.0. Su targeting
R* residual publicitario de
apunta hacia el Facebook. El
diseñador de la modelo de
métrica y el moderación de
proveedor del contenidos de
dataset. Twitter/X. Su S
≈ 1.0 significa
que cambiar el
modelo sin
cambiar la
métrica y el
dataset no reduce
el daño.
Regulador La autoridad Alto La Comisión
omisivo (Reg) regulatoria que [0.55– Europea antes
tenía facultad de 0.85] del Digital
establecer Services Act. La
estándares de FTC antes de
auditoría establecer
obligatoria, de estándares de

Taxonomía General de Aplicaciones
Función en el Ejemplo en el
Tipo S típico
grafo dominio
acceso a datos algorithmic
para accountability.
investigadores, Las autoridades
o de requisitos de protección de
de equidad para datos que no
sistemas de alto investigaron los
impacto, y no dark patterns de
los estableció. consentimiento
R* positivo durante años de
cuando esa evidencia
omisión fue acumulada.
condición de la
continuidad del
diseño dañino a
escala.
Usuarios (U) Los Variable El usuario que
participantes — muy publicó el
del ecosistema alto contenido de
de la plataforma cuando el desinformación.
— creadores de diseño El creador que
contenido, amplifica produjo
consumidores, contenid contenido de
anunciantes — o de radicalización. El
cuyo terceros anunciante que
comportamient [0.70– colocó
o retroalimenta 0.95] publicidad de
el dataset y cuya préstamos
participación es predatorios en el
condición del targeting de
sistema. R* usuarios de bajo
positivo cuando ingreso. Su S es
el usuario alto cuando el
publicó algoritmo
contenido amplificó el
dañino contenido más
deliberadament allá de lo que el
e. S del usuario usuario habría
es alto cuando podido lograr sin
el diseño del el sistema.
sistema
(amplificación
de contenido
emocionalment
e intenso) hacía
inevitable la

Taxonomía General de Aplicaciones
Función en el Ejemplo en el
Tipo S típico
grafo dominio
difusión del
contenido dado
sus
características.
Configuraciones canónicas del grafo de plataformas
digitales
Configuración 1 — Amplificación de contenido dañino por el
algoritmo de recomendación
DM (métrica: maximizar tiempo en pantalla / engagement emocional, S
bajo si la elección era deliberada) → DB (dataset de clics con sesgo hacia
contenido emocionalmente intenso) → MA (modelo que aprende que el
contenido emotivo maximiza la métrica, S ≈ 1.0) → Amplificación del
contenido de desinformación / radicalización → Nf (usuarios)
La S ≈ 1.0 del modelo demuestra que cambiar el algoritmo técnico no resuelve
el daño si la métrica permanece. La reforma correcta: cambiar la métrica de
"engagement emocional" a "calidad informativa" o "bienestar declarado del
usuario". El R* del diseñador de la métrica es alto cuando la elección de
"engagement emocional" como objetivo era una entre múltiples alternativas
técnicamente razonables con consecuencias distintas.
Configuración 2 — Discriminación algorítmica en targeting
publicitario
DM (métrica: maximizar conversiones / CTR por grupo demográfico) →
DB (dataset histórico de comportamiento de usuarios con patrones
demográficos sesgados) → MA (modelo que aprende a mostrar anuncios de
servicios de mayor costo a grupos de menor ingreso porque ese patrón
maximiza el CTR histórico) → Disparate impact sobre grupos protegidos
→ Nf
El análisis de disparate impact PD4/PD2 establece el patrón. La métrica
de "maximizar CTR" sin restricciones de equidad es la decisión normativa
de mayor R*. La alternativa disponible: métricas de CTR ajustadas por
equidad o prohibición de targeting por proxis de características protegidas.
R*_diseñador_métrica es alto cuando esa alternativa era técnicamente viable.

Taxonomía General de Aplicaciones
Configuración 3 — Daño a menores por diseño de engagement
adictivo
DM (métricas de retención de usuarios menores: notificaciones, likes, streaks)
→ DS (desplegador sin salvaguardas de edad verificadas) → MA (sistema
de engagement que activa ciclos de recompensa variable) → Daño
documentado al bienestar de menores → Nf
En esta configuración, el R* del desplegador es especialmente alto cuando
había evidencia científica disponible del impacto de esos mecanismos en el
bienestar de menores antes del despliegue. El Hijo del desplegador (Anteros
si ignoró deliberadamente la evidencia disponible, Potós si siguió las prácticas
estándar del sector sin cuestionarlas) informa S y la culpabilidad subjetiva.
§6 Preguntas que responde este capítulo
Nota de calibración: respuestas Nivel C. Ajustar con evidencia empírica
específica del caso y del dominio.
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
¿Qué métrica Identificar la métrica Declaración B con
optimiza el target del sistema PD1 de calidad o
algoritmo — es (PD1 si hay PD2 con auditoría.
esa la decisión de documentos internos; Declaración C si la
mayor R*? PD2 si la auditoría métrica debe inferirse
técnica puede desde el
reconstruir qué comportamiento del
variable el modelo sistema (PD4/PD6).
optimiza). Verificar si
la elección de esa
métrica versus
alternativas razonables
con menor impacto
dañino era una
elección normativa o
técnicamente forzada.
¿El sistema Análisis PD4 de los Declaración B con
produce disparate resultados del sistema PD4 sólido y PD2
impact — daño por grupos que establezca el
desproporcionado demográficos: ¿hay mecanismo causal.

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
a grupos diferencia Declaración C si el
protegidos? estadísticamente análisis de disparate
significativa en la tasa impact requiere datos
de resultados que solo la plataforma
desfavorables tiene (PD6).
(denegación de acceso,
amplificación
negativa, precios altos)
entre grupos con
características
comparables?
¿El desplegador PD1 (documentos Declaración B con
tenía evidencia del internos) o PD3 PD1/PD3 del
impacto dañino (whistleblower período de decisión.
antes del disclosures) que Declaración C si la
despliegue — Hijo muestren qué evidencia disponible
dominante del evidencia del impacto para el desplegador
desplegador? tenía el desplegador debe inferirse desde
antes de la decisión de PD5/PD6.
escalar. El Hijo
dominante (Anteros:
ignoró
deliberadamente;
Potós: siguió prácticas
del sector; Deimos: no
comprendió las
implicaciones)
informa S.
¿El diseño del Análisis PD2/PD5 del Declaración B con
sistema usa dark diseño de la interfaz de análisis PD2 de la
patterns de consentimiento: ¿las interfaz. Declaración
consentimiento opciones de A si los dark patterns
para los datos de privacidad estaban son documentados y
usuarios? diseñadas para reconocidos en el
disuadir el ejercicio del expediente
control del usuario? regulatorio.
¿El diseño de la
interfaz hacía más fácil
el consentimiento
amplio que la
restricción específica?
¿La plataforma Análisis de la posición Declaración B para el
tiene posición de mercado de la análisis de efectos de

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
dominante que le plataforma: cuanto red con datos de
da R* adicional mayor es la cuota de mercado. El impacto
sobre los efectos mercado y los efectos de la posición
de red del daño? de red, mayor es la dominante sobre el
magnitud del D_total D_total es un
de sus decisiones de multiplicador del
diseño — porque más daño individual que el
usuarios son afectados análisis de efectos de
por cada decisión red establece.
algorítmica. El análisis
económico PD2
establece los efectos
de red y su impacto
sobre el D_total.
¿Cuál es el D_total_plataforma = Declaración B para
D_total_platafor N_afectados × N_afectados ×
ma — cómo se D_promedio_individu D_promedio si hay
escala el daño al + datos de escala.
individual al D_sistémico_adiciona Declaración C para
colectivo? l. N_afectados y D_sistémico_adicion
D_promedio_individu al.
al se establecen con la
evidencia del dominio
primario (credencial
algorítmico PD2 +
datos de escala de la
plataforma).
D_sistémico_adiciona
l es el daño a la
confianza en las
instituciones
informativas o
democráticas que
trasciende los casos
individuales —
siempre Declaración
C.
§7 Traducción de D_total al dominio de
plataformas digitales

Taxonomía General de Aplicaciones
En el
Componen dominio de Cómo se Nota de
te plataformas cuantifica calibración
digitales
T_invertido Las Para cada Nivel C para la
(daño consecuencias usuario estimación de
directo por directas y afectado: D_promedio_indivi
decisiones verificables de aplicar el dual en muchos
incorrectas las decisiones instrument casos del dominio.
del sistema) del sistema o del El peritaje de daño
sobre los dominio individual en
usuarios primario plataformas digitales
afectados: (D_vital es una de las
clasificaciones del cap. 1 si fronteras más
incorrectas hay activas de la
que resultaron restricción investigación en el
en acceso de libertad período de escritura
denegado, por de este capítulo.
contenido COMPAS;
amplificado D_crédito
que produjo del cap. 11
daño si hay
documentable denegación
a usuarios de crédito;
específicos, D_salud
datos usados mental si
sin hay daño
consentimient psicológico
o para fines documenta
que causaron do por
daño peritaje).
concreto. Luego
escalar a
N_afectad
os.
T_impedido Las Análisis del Nivel C. La
(oportunida oportunidade diferencial cuantificación de las
des s de de acceso oportunidades
denegadas información, entre el denegadas por
durante el conexión, grupo diseño algorítmico
período del acceso a afectado y discriminatorio es
diseño servicios o el grupo de una de las preguntas
dañino) participación referencia más abiertas del
democrática durante el dominio.
que el diseño período del
dañino de la diseño
plataforma dañino.

Taxonomía General de Aplicaciones
En el
Componen dominio de Cómo se Nota de
te plataformas cuantifica calibración
digitales
negó Escalado al
sistemáticame N_afectad
nte a los os del
usuarios grupo con
afectados. disparate
Para los impact.
grupos con
disparate
impact: el
valor de
acceso a los
servicios que
les fue
denegado por
el diseño
discriminatori
o.
ΔT_trayecto El daño Estudios Nivel C en todos los
ria (daño permanente a de largo casos. Este
sistémico la calidad del plazo sobre componente es
permanente debate el impacto candidato
a la público de la prioritario para
información (desinformaci exposición investigación en la
y al ón sistémica), al sistema Revista Meriadock.
bienestar) a la confianza de la
en las plataforma
instituciones en las
democráticas métricas de
(radicalización bienestar,
algorítmica), o radicalizaci
al bienestar de ón o
largo plazo de calidad
los usuarios informativa
(daño . Siempre
psicológico Declaració
crónico en n C por la
menores por dificultad
diseños de
adictivos). Es establecer
el causalidad
componente versus
de mayor confusas.
magnitud y

Taxonomía General de Aplicaciones
En el
Componen dominio de Cómo se Nota de
te plataformas cuantifica calibración
digitales
menor
certeza.
D_total_plataforma = N_afectados × D_promedio_individual +
D_sistémico_adicional
El daño de un sistema algorítmico de plataforma tiene la característica de
operar a escala que lo distingue de todos los dominios individuales.
COMPAS procesó cientos de miles de casos. Los algoritmos de
recomendación de las grandes plataformas afectan a millones de usuarios
diariamente. El D_total algorítmico tiene dos capas: el daño agregado de
todas las decisiones individuales incorrectas (N_afectados ×
D_promedio_individual, que puede estimarse con Declaración B si los datos
de escala están disponibles) y el daño sistémico que trasciende las decisiones
individuales (erosión de la confianza en las instituciones, degradación del
debate público, efectos de red de la desinformación — siempre Declaración C
por la dificultad de establecer causalidad).
D_vital_plataforma = D_total / w_ref. La conversión a horas de vida hace
visible la magnitud real del daño. Para COMPAS: cada clasificación
incorrecta como "alto riesgo" que resultó en detención preventiva o denegación
de libertad condicional representó en promedio varios meses de vida en
condiciones de reclusión. Multiplicado por los miles de casos afectados con
disparate impact racial, D_vital es sustancial y calculable — y su magnitud
justifica la urgencia de la reforma algorítmica que el análisis de R* señala.
§8 Límites del método y errores frecuentes de
aplicación
Nota especial: límites más amplios en el dominio de
plataformas que en la mayoría de los dominios
El dominio de plataformas digitales es el que opera con mayor incertidumbre
en el libro. La cadena causal entre las decisiones de diseño de la plataforma y
los daños downstream en los usuarios es frecuentemente larga y mediada por
múltiples capas: el algoritmo, el comportamiento de los usuarios que
retroalimenta el dataset, los efectos de red, y la interacción con el entorno
informativo más amplio. La Declaración C es frecuente incluso para el
análisis de los nodos más centrales del grafo. El analista que use este capítulo

Taxonomía General de Aplicaciones
en una pretensión formal debe ser especialmente explícito sobre los límites de
la cadena causal que puede establecer con certeza.
Límites del método en el dominio de plataformas digitales
Límite 1 — La asimetría de información es estructural y
severa. La mayor parte de la evidencia del impacto de los
algoritmos de las plataformas está en manos de la plataforma.
Sin acceso a los documentos de decisión de la métrica (PD1),
al dataset (PD2) y a los resultados de los experimentos A/B
internos, el análisis externo opera desde PD4/PD6 — que no
produce más que Declaración C para los nodos más críticos
del grafo.
Límite 2 — La causalidad en cadenas largas. El daño
downstream (radicalización de un usuario específico, deterioro
del debate público, impacto en la salud mental de menores)
puede tener múltiples causas, de las cuales el algoritmo de la
plataforma es solo una. La separación entre el impacto causal
del algoritmo y los factores confusos (el historial personal del
usuario, el entorno familiar, las condiciones socioeconómicas)
es técnicamente muy difícil y raramente produce más que
Declaración C.
Límite 3 — La velocidad de evolución del dominio. Los
sistemas algorítmicos de las plataformas evolucionan
rápidamente. El análisis del diseño de una versión del
algoritmo puede no ser aplicable a la versión que estaba en
producción en el período del daño analizado. La temporalidad
del análisis debe ser especialmente precisa en este dominio.
Límite 4 — La imputación causal de los efectos de red. Los
efectos de red de las plataformas amplían el daño de cada
decisión individual de diseño: una decisión algorítmica que
produce disparate impact afecta no a un usuario sino a
millones. Cuantificar la escala del efecto de red con certeza
requiere datos de la plataforma raramente disponibles.

Taxonomía General de Aplicaciones
Errores frecuentes de aplicación
Por qué Consecuenci
Error Corrección
ocurre a
Atribuir el El modelo R* del Identificar
daño al es el nodo diseñador de siempre la métrica
modelo más visible la métrica = 0 que el modelo
algorítmico (el y aunque es el optimiza antes de
código) en técnicament nodo de analizar el
lugar del e analizable. mayor R* del modelo. Pregunta
diseñador de El análisis grafo. La clave: ¿qué habría
la métrica se detiene reforma que producido el
en el resulta sistema si la
modelo. (cambiar el métrica fuera
modelo) no diferente? Si la
resuelve el respuesta es
problema "resultados menos
porque el dañinos", el
modelo tiene diseñador de la
S ≈ 1.0. métrica tiene R*
alto.
Tratar el El dataset El sesgo se El R* del dataset
dataset como es el nodo trata como un apunta hacia el
el actor de que problema contexto histórico
mayor "contiene el técnico del que lo generó. La
responsabilida sesgo" y es dataset (que corrección técnica
d sin más fácil de puede del dataset
remontarse al analizar que resolverse (debiasing) es α
contexto las con debiasing del curador del
histórico que estructuras técnico) en dataset, no una
lo generó históricas lugar de un solución al R* del
de problema contexto histórico
desigualdad estructural de que requiere
. las cambios
instituciones institucionales
que más profundos.
generaron los
datos
históricos.
Ignorar la El análisis D_total D_total_platafor
posición cuantifica el subestimado. ma =
dominante de daño La magnitud N_afectados ×
la plataforma individual real del daño D_individual +
como sin de las D_sistémico. Los
incorporar decisiones de efectos de red de

Taxonomía General de Aplicaciones
Por qué Consecuenci
Error Corrección
ocurre a
multiplicador los efectos diseño de las la posición
del D_total de red de la grandes dominante
posición plataformas multiplican el
dominante no es visible. N_afectados para
de la cada decisión de
plataforma. diseño. Incluirlos
en el análisis hace
visible la
magnitud real del
daño de las
decisiones
algorítmicas a
escala.
Usar la El La La auditoría de
"explicabilida regulador o explicabilidad equidad debe
d del modelo" el analista del modelo incluir la
como exige que el no resuelve el evaluación de la
sustituto de la modelo daño si la métrica target, no
auditoría de la explique sus métrica está solo la evaluación
métrica decisiones, sesgada. El técnica del
asumiendo modelo puede modelo. La
que eso explicar pregunta
resuelve el perfectament regulatoria
problema e por qué correcta no es
de equidad. produjo el "¿puede el modelo
resultado explicar su
discriminatori decisión?" sino
o — esa "¿es la métrica que
explicación el modelo
completa el optimiza justa
análisis para todos los
técnico del grupos
modelo sin afectados?".
tocar el R* del
diseñador de
la métrica.
§9 Guía de prioridades de recolección de
evidencia
Nota de uso obligatoria: todas las estimaciones de este capítulo son Nivel
C. La cadena causal en el dominio de plataformas digitales es

Taxonomía General de Aplicaciones
especialmente difícil de establecer con certeza sin acceso a los documentos
internos de la plataforma. La primera prioridad siempre es identificar qué
evidencia PD1 o PD2 está disponible o puede obtenerse — porque sin
esa evidencia, el análisis opera desde PD4/PD6 y no puede producir más
que Declaración C.
Tabla de prioridades de recolección de evidencia en
plataformas digitales
Si tu Qué
incertidu La evidencia Qué buscar /
Por qué
mbre que más la rango qué
funciona
principal reduce es… reduce pregunt
es… ar
1. ¿Qué PD1 La Determin ¿Hay
métrica (documentos métrica a el actor documen
optimiza internos de la target es de mayor tos de
el sistema plataforma que la R* y la producto
— el acto establecen la decisión reforma que
de mayor métrica) o PD2 normativ de mayor describan
R*? (auditoría a de impacto los
algorítmica que mayor (incertidu objetivos
reconstruye la R*. Sin mbre del
métrica desde conocerla empírica algoritmo
el , el crítica) ? ¿La
comportamien análisis auditoría
to del sistema). del grafo técnica
Sin esta es puede
evidencia, el R* incomple reconstru
del diseñador to en su ir qué
de la métrica es nodo más variable
solo una importan el modelo
inferencia te. maximiza
PD6. ? ¿Hay
whistlebl
ower
disclosur
es sobre
la
métrica?
2. ¿El PD4: análisis El Reduce ¿Hay
sistema estadístico de disparate rango de investiga

Taxonomía General de Aplicaciones
Si tu Qué
incertidu La evidencia Qué buscar /
Por qué
mbre que más la rango qué
funciona
principal reduce es… reduce pregunt
es… ar
produce los resultados impact es la arista ción
disparate del sistema por el de daño a académic
impact — grupos instrume grupos a sobre el
evidencia demográficos nto que protegido disparate
PD4/PD con datos establece s impact
2? públicos o de la (incertidu del
investigadores existencia mbre sistema?
con acceso a del daño empírica) ¿Hay
datos. PD2: a escala. datos
auditoría Sin ese públicos
algorítmica que análisis, el (HMDA
establece el daño equivalen
mecanismo individual te, datos
causal del no es de
disparate evidencia moderaci
impact. suficiente ón de
del daño contenid
sistemátic os) que
o de la permitan
plataform el
a. análisis?
¿El
regulador
ha
realizado
auditorías
con
acceso a
datos?
3. ¿El PD1 La Reduce ¿Hay
desplegad (documentos evidencia rango de whistlebl
or tenía internos del de qué S del ower
evidencia período pre- sabía el desplega disclosur
del daño despliegue) o desplegad dor es del
antes de PD3 or antes (incertidu período?
desplegar (whistleblower de mbre ¿Hay
— Hijo disclosures desplegar ontológic litigación
dominant como la de es el a) regulatori
e? Frances instrume a que
Haugen que nto para haya
incluyeron discrimin producid
documentos de ar o

Taxonomía General de Aplicaciones
Si tu Qué
incertidu La evidencia Qué buscar /
Por qué
mbre que más la rango qué
funciona
principal reduce es… reduce pregunt
es… ar
experimentos Anteros documen
A/B internos). (dolo) de tos
Sin esta Potós internos?
evidencia, el (negligen ¿El
Hijo del cia) de regulador
desplegador es Deimos tiene
Deimos por (ignoranc acceso a
defecto. ia). Esa documen
distinción tos de
determin decisión
a el tipo que
de pueda
proceso. comparti
r?
4. ¿La PD2: análisis Los dark Determin ¿Las
plataform de la patterns a R* opciones
a usó dark arquitectura de son una autónom de
patterns la interfaz de fuente o de la privacida
de consentimient autónom platafor d están
consenti o versus los a de R* ma por diseñadas
miento? estándares de de la diseño de para
UX de plataform consenti disuadir
privacidad. a que es miento el
PD5: independ (incertidu ejercicio
comparación iente del mbre del
con las mejores análisis empírica) control?
prácticas del algorítmi ¿El
sector para el co. Son consenti
tipo de dato y más miento
usuario. directame más
nte amplio es
documen más fácil
tables que de
el R* de otorgar
la métrica que el
porque la consenti
interfaz miento
es restringid
pública. o? ¿Hay
diferenci
as de
tamaño

Taxonomía General de Aplicaciones
Si tu Qué
incertidu La evidencia Qué buscar /
Por qué
mbre que más la rango qué
funciona
principal reduce es… reduce pregunt
es… ar
de letra,
color o
posición
entre las
opciones
de
privacida
d?

### 5. PD4 (datos Sin Establece ¿Cuántos
¿Cuántos públicos de N_afecta la escala usuarios
usuarios escala de la dos, el del están
fueron plataforma: daño D_total expuesto
afectados usuarios individual (incertidu s al
— activos, tasa de no puede mbre de sistema
N_afecta exposición al escalarse escala) analizado
dos para sistema) o PD2 al ? ¿Qué
escalar el (datos internos D_total porcentaj
D_total? obtenidos por que e de los
reguladores o establece usuarios
auditorías). la del grupo
N_afectados × pretensió con
D_promedio_i n contra disparate
ndividual es la la impact
base del plataform fue
D_total a. La afectado?
escalable. escala del ¿Hay
sistema datos
es lo que públicos
convierte de la
el daño platafor
individual ma sobre
en daño la escala
de del
responsa sistema?
bilidad
institucio
nal.
6. ¿Cuál es Identificar si la La Establece ¿Qué
la reforma reforma de la reforma la política métricas
de mayor métrica es de la regulatori alternativ
impacto técnicamente métrica a de as están

Taxonomía General de Aplicaciones
Si tu Qué
incertidu La evidencia Qué buscar /
Por qué
mbre que más la rango qué
funciona
principal reduce es… reduce pregunt
es… ar
— el viable con tiene mayor documen
nudge alternativas mayor impacto tadas en
regulatori documentadas ROI que la
o? en la literatura la literatura
(PD2/PD5). reforma de IA
La alternativa del responsa
de métrica con modelo o ble para
menor impacto el ese tipo
negativo y debiasing de
viabilidad del sistema?
técnica dataset, ¿Cuáles
comparable es porque la tienen
el argumento S ≈ 1.0 evidencia
de política del de
regulatoria más modelo viabilidad
fuerte del significa técnica
capítulo. que compara
cualquier ble?
modelo ¿Cuáles
correcto tienen
aprender menor
á el sesgo disparate
de una impact
métrica documen
sesgada. tado?
Árbol de decisión en plataformas digitales: ¿qué buscar
primero?
El árbol comienza con la disponibilidad de evidencia
PD1/PD2, porque sin esa evidencia el análisis no puede ir más
allá de Declaración C para los nodos más críticos del grafo.
¿Hay evidencia PD1 o PD2 disponible — documentos
internos o auditoría algorítmica?

Taxonomía General de Aplicaciones
├─ Si NO: el análisis opera desde PD4/PD6. Todas las
estimaciones son Declaración C.
│
└─ Prioridad: identificar si hay whistleblower
disclosures, litigación regulatoria con documentos, o
investigación académica con acceso a datos.
· Sin ninguna de esas fuentes: el análisis puede establecer la
existencia del disparate impact (PD4) pero no la cadena
causal hasta el diseñador de la métrica.
├─ Si SÍ hay PD1/PD2: prioridad 1 — identificar la métrica
que el sistema optimiza.
│
└─ ¿La métrica elegida era la única técnicamente
razonable o había alternativas con menor impacto
dañino?
· Si había alternativas → R* del diseñador de la métrica
es alto. S dependiente del Hijo (Anteros vs. Potós).
· Si la métrica era el estándar del sector → S moderado-
alto. R*_neta del diseñador reducido.
├─ Prioridad 2: ¿El sistema produce disparate impact
documentable?
│
└─ PD4 (análisis estadístico público) → PD2
(auditoría con datos internos).
· Si sí → base del D_total del daño a grupos protegidos
con escala N_afectados.
└─ Prioridad 3: ¿El desplegador tenía evidencia del daño
antes de desplegar?
└─ PD1 (documentos pre-despliegue) o PD3
(whistleblower).
· Si sí → Hijo dominante del desplegador: Anteros
(ignoró deliberadamente) → proceso penal / Potós (siguió
prácticas del sector) → responsabilidad civil.
· Si no hay evidencia → Deimos por defecto. S alto del
desplegador.

Taxonomía General de Aplicaciones
— Fin del Capítulo 17 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

