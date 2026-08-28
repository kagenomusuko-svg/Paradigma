## PARTE VII · Ingeniería y Tecnología

### Capítulo 49
Inteligencia artificial y sistemas
automatizados
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Nivel C — el nivel de mayor incertidumbre de la
taxonomía. Sus rangos w son candidatos derivados por extensión teórica
desde El cálculo de la responsabilidad cap. 13 (IA y algoritmos de
decisión), no por calibración empírica con datos de litigios. Antes de
usarlos en un procedimiento con pretensión formal, consultar la
jurisprudencia emergente de responsabilidad algorítmica en la
jurisdicción competente. El capítulo es candidato prioritario a la Revista
Meriadock.
La aportación central es conceptual: la jerarquía de responsabilidad en
los sistemas de IA invierte la jerarquía de visibilidad. El modelo — el
componente más visible del sistema — tiene R* próximo a cero porque
S_modelo ≈ 1.0: cualquier modelo competente entrenado con la misma
métrica y el mismo dataset habría producido el mismo resultado dañino.
Quien tiene el mayor R* es el diseñador de la métrica: la persona que
decidió qué optimiza el sistema. Esa es una decisión normativa, no
técnica, y es idiosincrática — alternativas estaban disponibles.
Si tu caso es de sesgo algorítmico en decisiones de alto impacto (empleo,
crédito, justicia penal, diagnóstico médico), ve a §1, §3 y §5. Si es de
daño por sistema autónomo (vehículo, drone, arma), ve a §1 y §5
configuración 2. Si es de daño por modelo de lenguaje grande (LLM),
ve a §1 y §5 configuración 3. Para la descomposición del disparate
impact, ve a §4. Para la prioridad de evidencia, ve directamente a §9.

Taxonomía General de Aplicaciones
§1 Descripción del subcampo
Los sistemas de inteligencia artificial y decisión automatizada
son el dominio donde la jerarquía de responsabilidad está más
sistemáticamente invertida respecto a la jerarquía de
visibilidad. El modelo de machine learning —el componente
más visiblemente complejo del sistema— tiene índice de
sustituibilidad S prácticamente igual a 1.0 y, por tanto, R*_neta
≈ 0: cualquier modelo competente entrenado con la misma
métrica objetivo y el mismo dataset de entrenamiento habría
aprendido los mismos patrones y producido los mismos
daños. Cambiar el modelo sin cambiar la métrica ni el dataset
no resuelve el problema. El principio algorítmico de El cálculo
de la responsabilidad cap. 13 es la piedra de cimiento de este
capítulo: el R* migra del componente técnico visible al decisor
normativo invisible que eligió qué optimiza el sistema.
Esta inversión no es solo analíticamente relevante —es
jurídicamente transformadora. El litigio de responsabilidad
algorítmica que se enfoca en el modelo (su explicabilidad, sus
métricas de fairness, su arquitectura) está atacando el nodo de
menor R*_neta del grafo. El litigio que se enfoca en el
diseñador de la métrica —la persona que decidió que «éxito»
en el sistema de contratación de Amazon significaba «similitud
con el historial de ingenieros masculinos contratados en la
última década»— está atacando el nodo de mayor R*_neta con
S bajo: esa elección no era la única técnicamente disponible,
era la elección que ese diseñador específico hizo entre
alternativas con consecuencias distribucionales distintas.
El principio del diseñador de la métrica: la jerarquía de
responsabilidad algorítmica
En todo sistema algorítmico, la decisión normativa de mayor R* no es la que
escribe el código del modelo — es la que define qué objetivo optimiza ese
modelo. El modelo tiene S ≈ 1.0 porque es técnicamente fungible: dado una
métrica y un dataset, cualquier equipo competente produce un modelo con el
mismo comportamiento. El diseñador de la métrica tiene S bajo porque la
elección de qué optimizar es normativa e idiosincrática — alternativas con
menores consecuencias dañinas estaban técnicamente disponibles.

Taxonomía General de Aplicaciones
R*_modelo × (1 − S_modelo) ≈ 0 → cambiar el
modelo sin cambiar la métrica no reduce el daño
R*_métrica × (1 − S_métrica) >> 0 → la elección de
la métrica era la condición necesaria idiosincrática
Esta jerarquía aplica a todos los sub-dominios del capítulo: el sistema de
reconocimiento facial con sesgo racial tiene S_modelo ≈ 1.0 y S_métrica bajo
(la elección de entrenar con datasets de composición racial sesgada era una
elección entre alternativas). El vehículo autónomo que priorizó la
minimización del daño al pasajero tiene S_modelo ≈ 1.0 y
S_reglas_de_decisión bajo (la jerarquía de valores del sistema era una
decisión ética que alguien tomó). El LLM que genera desinformación
convincente tiene S_modelo ≈ 1.0 y S_objetivo_de_entrenamiento bajo.
Sub-variantes del dominio
Sub-variante Descripción y singularidades del dominio
Sistemas Los sistemas que toman decisiones con
algorítmicos de consecuencias directas sobre derechos y
decisión de alto oportunidades individuales: sistemas de evaluación
impacto del riesgo de reincidencia en el sistema penal
(COMPAS), sistemas de screening de candidatos en
procesos de contratación (Amazon Hiring AI),
algoritmos de scoring crediticio, sistemas de
diagnóstico médico automatizado, algoritmos de
asignación de prestaciones sociales. El daño en este
sub-campo tiene dos componentes: el daño individual
de las decisiones incorrectas y el daño sistémico del
disparate impact sobre grupos protegidos. El
diseñador de la métrica objetivo tiene el mayor R* en
ambos componentes.
Sistemas de Los algoritmos que determinan qué contenido ve
recomendación cada usuario en plataformas digitales, qué productos
y amplificación se recomiendan, qué noticias aparecen primero. El
algorítmica daño incluye la amplificación de desinformación, la
radicalización hacia posiciones extremas, la
exposición de menores a contenido dañino y la
creación de cámaras de eco informativas. Se conecta
directamente con el cap. 17 (plataformas digitales)
donde se desarrolló la escala PD0–PD8 y el
instrumento de la auditoría algorítmica para este tipo
específico de daño.

Taxonomía General de Aplicaciones
Sub-variante Descripción y singularidades del dominio
Sistemas Los vehículos autónomos, los drones, los robots
autónomos industriales y —en el extremo del espectro— los
con capacidad sistemas de armas autónomos letales (LAWS). En
de daño físico estos sistemas, el daño físico directo es la
consecuencia de las reglas de decisión del sistema en
situaciones que el diseñador no anticipó
completamente. El grafo de responsabilidad es
singular: el fabricante del sistema (diseñador de las
reglas de decisión), el certificador (que verificó la
seguridad del sistema), el desplegador (que lo puso en
operación en ese entorno específico), y el regulador
(que estableció o no estableció los estándares de
certificación). Nivel C porque la jurisprudencia es
incipiente.
Modelos de Los modelos de lenguaje que generan texto,
lenguaje imágenes, audio y video con alta verosimilitud. El
grandes daño incluye la generación de desinformación
(LLMs) y convincente, la producción de contenido que viola
sistemas derechos de autor o la privacidad, la generación de
generativos discurso de odio o contenido ilegal, y la facilitación de
daños cuando el usuario del modelo los usa para
causar daño a terceros. La cadena de responsabilidad
es más larga que en los sistemas de decisión: el
desarrollador del modelo base, el ajustador fino (fine-
tuner) que adaptó el modelo para el caso de uso, el
desplegador de la aplicación, y el usuario que generó
el daño específico.
IA en Los sistemas de IA que asisten o automatizan el
diagnóstico y diagnóstico médico (análisis de imágenes
decisión radiológicas, detección de patologías en registros
médica clínicos, predicción del riesgo de deterioro del
paciente). El daño puede ser por falso negativo (el
sistema no detectó una condición que habría
detectado un clínico adecuado) o por falso positivo
(el sistema indicó una condición que no existía y
produjo tratamiento innecesario). Se conecta con el
cap. 24 (salud mental) y el cap. 27 (sistemas de salud)
para el análisis del R* del sistema versus el R* del
clínico que usó el sistema.
IA en sistemas Los algoritmos que gestionan redes eléctricas,
críticos de sistemas de transporte, redes financieras y otras
infraestructura infraestructuras críticas. El daño por fallo del sistema
algorítmico tiene la estructura del fallo de ingeniería

Taxonomía General de Aplicaciones
Sub-variante Descripción y singularidades del dominio
(cap. 50) pero con la particularidad de que el fallo fue
producido por el comportamiento del modelo ante
situaciones de distribución de datos fuera del rango
de entrenamiento (distribution shift). El diseñador del
sistema de monitoreo y del proceso de validación del
modelo tiene el mayor R* sobre los daños de los fallos
por distribution shift.
§2 Escala de evidencia IA0–IA8 · Inteligencia
artificial y sistemas automatizados
La escala IA0–IA8 traduce la jerarquía general E0–E8 al
vocabulario de la responsabilidad algorítmica. Su característica
más relevante es la posición central de la auditoría de la métrica
(IA2) —que establece qué objetivo optimiza el sistema y cuáles
eran las alternativas disponibles— sobre la auditoría del
modelo (que establece cómo lo optimiza). El error más
frecuente en el peritaje técnico es invertir la prioridad: auditar
el modelo primero y la métrica después, cuando la métrica es
el nodo de mayor R*. Nivel C — rangos candidatos.
Nota de calibración obligatoria: rangos IA0–IA8
Los rangos w de la escala IA0–IA8 son rangos candidatos derivados
por extensión teórica desde El cálculo de la responsabilidad cap. 13 y la
escala PD0–PD8 del cap. 17 de esta Taxonomía. No están calibrados
empíricamente con datos de litigios de responsabilidad algorítmica. La
jurisprudencia en este dominio es incipiente y varía significativamente
entre jurisdicciones. El analista debe ajustar los rangos con la
jurisprudencia local antes de usarlos en una pretensión formal.
Descripción y ejemplos
Tipo de en el dominio de IA y Rango w
Nivel
evidencia sistemas (candidato)
automatizados
IA1 Documentos Comunicaciones internas [0.70, 0.88]
internos del donde el diseñador tomó

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de en el dominio de IA y Rango w
Nivel
evidencia sistemas (candidato)
automatizados
diseñador que la decisión de la métrica
establecen la objetivo con
decisión de la conocimiento de las
métrica y sus alternativas y sus
alternativas consecuencias
conocidas distribucionales;
resultados de pruebas
A/B o estudios internos
que establecían el efecto
del diseño antes de su
despliegue a escala; actas
del comité de ética o de
revisión de riesgos que
discutieron el impacto del
diseño; documentación de
la decisión de desplegar el
sistema sin implementar
las salvaguardas
recomendadas
internamente.
IA2 Auditoría Auditoría algorítmica [0.58, 0.78]
algorítmica independiente que
independiente establece: (a) la métrica
de la métrica + que optimiza el sistema y
análisis del las alternativas
disparate impact técnicamente disponibles
+ peritaje con menor impacto
técnico dañino; (b) el disparate
especializado impact del sistema sobre
grupos protegidos, con
análisis de si ese impacto
era previsible dado el
diseño de la métrica; (c) el
análisis S_modelo — si
cualquier modelo
competente con la misma
métrica y dataset habría
producido el mismo
resultado; (d) el análisis
DI_métrica + DI_dataset
+ DI_modelo para
establecer qué fracción
del disparate impact total

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de en el dominio de IA y Rango w
Nivel
evidencia sistemas (candidato)
automatizados
era atribuible a cada
componente.
IA3 Testimonio de Declaraciones [0.46, 0.64]
exempleados o convergentes de
investigadores + exempleados que
documentación describen el proceso de
técnica parcial diseño de la métrica y las
del sistema decisiones tomadas sobre
el dataset de
entrenamiento, con
corroboración en al
menos un documento
técnico del sistema;
publicaciones académicas
de investigadores que
tuvieron acceso al sistema
y documentaron el
disparate impact con
metodología replicable.
IA4 Análisis de los Análisis estadístico de los [0.34, 0.54]
outputs del outputs del sistema sobre
sistema con una muestra
evidencia del representativa que
disparate impact establece el disparate
observable impact sobre grupos
protegidos, con ajuste por
los factores de riesgo
legítimos que el sistema
puede considerar;
comparación de las tasas
de error del sistema entre
grupos con características
comparables.
IA5 Análisis Comparación del [0.24, 0.42]
comparativo del comportamiento del
comportamiento sistema con el de un
del sistema con sistema de referencia que
el estándar de usa criterios establecidos
referencia sin el componente
algorítmico; o

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de en el dominio de IA y Rango w
Nivel
evidencia sistemas (candidato)
automatizados
comparación de los
resultados del sistema con
los de un panel de
expertos humanos en los
mismos casos, que
establece si el sistema
produce resultados
consistentemente peores
para grupos específicos.
IA6 Inferencia desde El diseño del sistema —la [0.14, 0.30]
el diseño del métrica documentada en
sistema y las los materiales públicos, el
características dataset de entrenamiento
del dataset conocido— permite
inferir que el sistema
probablemente produce
disparate impact sin
análisis directo de los
outputs del sistema
analizado.
IA7 Correlación El daño comenzó a [0.05, 0.20]
temporal entre el producirse o aumentó
despliegue del significativamente
sistema y el daño después del despliegue del
sin análisis de sistema sin análisis de la
causalidad cadena causal entre el
algorítmica comportamiento del
algoritmo y el daño
específico.
IA8 Afirmación de Afirmación de que el [0.02, 0.12]
sesgo sistema produce sesgo sin
algorítmico sin evidencia técnica del
evidencia técnica comportamiento del
del sistema algoritmo ni análisis de
sus outputs.
IA0 Ausencia Auditoría IA2 que w = 0.00
documentada de establece que el sistema
nexo causal analizado no tiene
entre el sistema y disparate impact

Taxonomía General de Aplicaciones
Descripción y ejemplos
Tipo de en el dominio de IA y Rango w
Nivel
evidencia sistemas (candidato)
automatizados
el daño significativo sobre el
analizado grupo analizado, o que el
daño del caso específico
no es causalmente
atribuible al sistema sino a
otros factores del
contexto del caso.
§3 Firmas documentales por Hijo
Los Hijos de Afrodita aplican en el dominio algorítmico
exclusivamente a los actores humanos que tomaron las
decisiones normativas del sistema: el diseñador de la métrica
objetivo, el curador del dataset de entrenamiento, el directivo
que aprobó el despliegue del sistema, el regulador que
estableció o no estableció los estándares de auditoría, y el
desplegador que implementó el sistema en un contexto
específico. Los Hijos no aplican al modelo, al dataset ni a
ningún otro componente técnico sin voluntad propia. El error
de analizar el «comportamiento del algoritmo» con los Hijos
de Afrodita es el error de atribuir voluntad a un instrumento.
La distinción más relevante del dominio es entre el diseñador
que sabía que su métrica produciría disparate impact sobre
grupos específicos —lo había documentado en pruebas
internas— y deliberadamente no modificó el diseño (Anteros),
el que siguió los estándares del campo del período sin
implementar las auditorías de equidad disponibles (Potós), y el
que genuinamente no tenía la evidencia de que el diseño
producía el daño porque la auditoría de equidad no era una
práctica establecida en el período (Deimos).
§3.1 Hijos de legibilidad alta en el dominio de la IA

Taxonomía General de Aplicaciones
Qué
informa Firma Error de
Fuente
Hijo para S del documenta discrimina
típica
diseñador o l ción
desplegador
Anter S muy bajo Comunicaci Discovery de Confundir
os [0.03, 0.20]. ones litigios. con Potós
El diseñador internas Whistleblow cuando el
sabía que la donde se ers con diseñador
métrica documentó documentaci siguió los
producía el disparate ón. estándares
disparate impact antes Investigacio del campo
impact o que del nes sin
el sistema despliegue parlamentari evidencia
generaría sin que eso as o interna que
daño en el produjera regulatorias. mostrara el
dominio de cambio del Reportes impacto
despliegue, y diseño. filtrados de sobre los
deliberadame Resultados equipos de grupos
nte no de pruebas confianza y específicos
modificó el A/B que seguridad. perjudicado
diseño mostraban s.
porque los el efecto
costos de la dañino en
reforma grupos
(menor específicos
rendimiento sin que se
del sistema, detuviera el
mayor costo despliegue.
computacion Actas de
al, menor comités de
precisión en ética que
el caso de uso señalaron el
principal) riesgo sin
superaban — que el
en su equipo de
evaluación— producto
los costos del implementar
daño. Es el a las
patrón de los salvaguardas
sistemas de recomendad
IA que as.
mantuvieron Decisiones
métricas con documentad
disparate as de escalar
impact el sistema
documentad sin las
o medidas de

Taxonomía General de Aplicaciones
Qué
informa Firma Error de
Fuente
Hijo para S del documenta discrimina
típica
diseñador o l ción
desplegador
internamente mitigación
durante que los
múltiples propios
ciclos de ingenieros
revisión sin habían
acción recomendad
correctora. o.
Potós S moderado- Métricas Comparació Confundir
alto [0.40, objetivo n con las con Anteros
0.70]. El coherentes prácticas cuando el
diseñador con las que estándar del diseñador
siguió los otros campo en el disponía de
estándares de sistemas del período. evidencia
diseño de campo Publicacione interna del
sistemas de usaban en el s de las impacto que
IA del período. conferencias no fue
período —las Ausencia de de referencia incorporada
métricas evidencia (NeurIPS, al diseño
estándar del interna del ICML, por razones
campo, los disparate FAccT) no
datasets de impact sobre las relacionadas
entrenamient sobre los métricas de con la
o habituales, grupos equidad capacidad
las prácticas específicos adoptadas. técnica de
de evaluación perjudicado Estándares detectarlo.
convencional s. sectoriales
es— sin Participació de auditoría
implementar n en del período.
auditorías de benchmarks
equidad estándar del
disponibles, campo que
pero no no incluían
generalizadas métricas de
en el período. equidad
El disparate como
impact era criterio de
una evaluación.
consecuencia Prácticas de
de las evaluación
prácticas consistentes
estándar del con las
sector, no de publicadas

Taxonomía General de Aplicaciones
Qué
informa Firma Error de
Fuente
Hijo para S del documenta discrimina
típica
diseñador o l ción
desplegador
una decisión en las
idiosincrática conferencias
del de
diseñador. referencia
del campo.
Deim S alto [0.56, Documenta Corresponde Confundir
os 0.84]. El ción de la ncia interna con la
desplegador incertidumb del equipo incertidumb
o el regulador re sobre de producto. re genuina
se paralizó cómo Actas de sobre qué
ante la auditar el comités de métrica de
complejidad sistema sin revisión. equidad es la
de la que esa Comunicaci correcta —
auditoría de incertidumb ones con el que es un
los sistemas re produzca regulador problema
de IA —la consulta a sobre los técnico-
opacidad de expertos ni estándares filosófico
los modelos pausa del de auditoría. real. La
de despliegue. diferencia:
aprendizaje Solicitudes Deimos
profundo, la de produce el
dificultad de financiamie expediente
definir nto para vacío ante la
operativamen auditoría no incertidumb
te la equidad, atendidas. re; la gestión
la Comunicaci adecuada
incertidumbr ones que produce
e sobre qué identifican el consulta
métricas de problema experta
fairness sin agenda documentad
aplicar— sin de a y decisión
consultar con resolución. justificada
expertos ni Regulacione aunque no
derivar la s pendientes perfecta.
decisión a sin
quienes implementa
tenían los ción en el
conocimient período del
os técnicos. despliegue.
El expediente
del Deimos
en IA:

Taxonomía General de Aplicaciones
Qué
informa Firma Error de
Fuente
Hijo para S del documenta discrimina
típica
diseñador o l ción
desplegador
documentos
que
identifican la
necesidad de
auditoría sin
que esa
identificación
produzca
acción o plan.
§3.2 Hijos de legibilidad baja y nota Harmonía
Fobos: el desplegador que implementó salvaguardas excesivas
—auditorías continuas, listas blancas restrictivas, umbrales de
confianza conservadores— motivado por el miedo a la
responsabilidad legal más que por el análisis del impacto real
del sistema. El Fobos en IA produce el sistema que rechaza
todas las solicitudes ambiguas para no cometer errores,
transfiriendo el daño a los usuarios falsamente rechazados. S
moderado [0.32, 0.58]. Distinguible de Harmonía porque la
Harmonía equilibra el rendimiento del sistema con la equidad;
el Fobos sacrifica el rendimiento para minimizar la
responsabilidad visible.
Eros en el desplegador: el desplegador que adoptó el sistema
de IA más avanzado disponible —mayor precisión media,
mayor velocidad, mayor escala— sin evaluar si ese avance
técnico producía mayor equidad distributiva. El Eros en IA
produce el sistema de última generación con el disparate
impact de la última generación. S moderado-alto [0.45, 0.72]
cuando el sistema adoptado era el de referencia del campo en
el período.

Taxonomía General de Aplicaciones
§3.3 Nota Harmonía — el equipo que auditó la métrica
y documentó las alternativas
El equipo que: (a) definió la métrica objetivo con análisis explícito de
las alternativas disponibles y sus consecuencias distribucionales; (b)
realizó la auditoría de equidad del sistema antes del despliegue con
instrumentos validados; (c) documentó el disparate impact residual y las
razones por las que no fue técnicamente eliminable; (d) implementó las
salvaguardas de monitoreo continuo del comportamiento del sistema en
producción; y (e) estableció un mecanismo de reclamación accesible para
los afectados tiene α ≈ 1.00 para su arista en el grafo — aunque el
sistema produzca daño residual que no era técnicamente eliminable con
el estado del arte disponible.
La Harmonía del equipo técnico no elimina el R* del directivo que
aprobó el despliegue sin implementar las salvaguardas recomendadas
internamente: son nodos distintos con R* distintos.
§4 Escala de α con la tabla de acciones que
cuentan
La descomposición del disparate impact: DI_total =
DI_métrica + DI_dataset + DI_modelo
El disparate impact total de un sistema algorítmico puede descomponerse en
tres componentes causales con R* distintos:
DI_métrica: el disparate impact producido por la elección de la variable
objetivo. Si la métrica fuera reemplazada por la alternativa óptima con menor
impacto, este componente desaparecería. R*_diseñador_métrica =
DI_métrica / DI_total.
DI_dataset: el disparate impact producido por el sesgo histórico en el dataset
de entrenamiento, dado la métrica. Si el dataset fuera auditado y
rebalanceado, este componente reduciría. R*_curador_dataset = DI_dataset
/ DI_total.
DI_modelo: el disparate impact adicional producido por la arquitectura y el
proceso de entrenamiento del modelo, dado la métrica y el dataset. S_modelo
≈ 1.0, por lo que R*_neta_modelo ≈ 0. Cambiar el modelo sin cambiar la
métrica ni el dataset tiene impacto mínimo.

Taxonomía General de Aplicaciones
R*_diseñador_métrica = (DI_métrica_actual −
DI_métrica_alternativa) / DI_total
Si DI_métrica_alternativa << DI_métrica_actual → la elección de
métrica es la condición necesaria idiosincrática del daño.
Nivel de α
α en el
Conducta que típico en
Nodo dominio
sube α desempeño
algorítmico
deficiente
Diseñador Análisis de las Análisis formal 0.05–0.20 para
de la métrica alternativas de de las diseñadores con
(DM) métrica con sus alternativas de Anteros
consecuencias métrica con documentado:
distribucionales estimación del conocían el
documentado; disparate disparate impact
elección de la impact de cada y eligieron la
métrica con alternativa antes métrica de
menor disparate de la decisión. mayor impacto.
impact Elección 0.25–0.50 para
técnicamente documentada diseñadores con
compatible con de la métrica Potós: siguieron
el objetivo del con menor el estándar del
sistema; disparate campo sin
documentación impact entre las auditoría de
de por qué la técnicamente equidad de la
alternativa de viables. métrica.
menor impacto Comunicación
no fue adoptada transparente de
cuando no lo los límites del
fue. sistema y del
disparate
impact residual
a los
desplegadores y
los afectados.
Curador del Auditoría del Análisis de 0.10–0.30 para
dataset (CD) sesgo histórico representación curadores que
del dataset antes de grupos usaron datasets
de su uso para protegidos en el con sesgo
entrenamiento; dataset. conocido sin
implementación Técnicas de auditoría ni
de técnicas de debiasing debiasing. 0.05–
debiasing o aplicadas con 0.15 cuando el
rebalanceo documentación curador conocía

Taxonomía General de Aplicaciones
Nivel de α
α en el
Conducta que típico en
Nodo dominio
sube α desempeño
algorítmico
deficiente
cuando el sesgo del efecto sobre el sesgo
era el disparate específico del
técnicamente impact. dataset relevante
corregible; Documentación para el caso de
documentación del sesgo uso y no lo
del sesgo residual comunicó.
residual y su comunicada al
impacto equipo de
esperado sobre entrenamiento
el sistema. del modelo.
Actualización
periódica del
dataset con
monitoreo de la
distribución.
Desplegador Auditoría del Auditoría de 0.05–0.20 para
(DE) sistema en el equidad del desplegadores
entorno de sistema en el que lanzaron a
despliegue dominio de escala sin
específico antes despliegue antes auditoría de
del lanzamiento del equidad en el
a escala; lanzamiento. dominio
implementación Monitoreo específico. 0.10–
del monitoreo continuo del 0.30 para
continuo del disparate desplegadores
disparate impact en que
impact en producción con monitorearon el
producción; umbrales de sistema pero no
establecimiento acción activaron el
de mecanismo predefinidos. mecanismo de
de reclamación Mecanismo de acción ante
accesible; reclamación señales de
definición de accesible y con disparate
umbrales de resolución en impact.
alerta con plan plazo definido.
de acción para Suspensión del
cuando el sistema cuando
disparate el disparate
impact supere el impact supera
umbral. los umbrales
establecidos.

Taxonomía General de Aplicaciones
Nivel de α
α en el
Conducta que típico en
Nodo dominio
sube α desempeño
algorítmico
deficiente
Regulador Establece los Estándares de 0.05–0.20 para
(RG) estándares de auditoría reguladores que
auditoría algorítmica no establecieron
algorítmica publicados con estándares de
requeridos metodología y auditoría en el
antes del umbrales por período del
despliegue en dominio de daño cuando la
aplicaciones de aplicación. evidencia del
alto impacto; Requisito de riesgo ya estaba
define los auditoría disponible.
umbrales de independiente 0.10–0.25 para
disparate antes del reguladores con
impact despliegue en estándares
aceptables para aplicaciones de insuficientes en
cada dominio alto impacto el dominio de
de aplicación; (justicia penal, aplicación del
realiza o exige la crédito, empleo, sistema
auditoría diagnóstico analizado.
independiente médico).
de los sistemas Mecanismo de
con mayor R* supervisión
potencial sobre post-despliegue
la población. con acceso a los
datos del
sistema en
producción.
Los seis niveles de α y el patrón de inversión causal en IA
Nivel de
Descripción del actor en el dominio algorítmico
α
α = 0.00– Diseñador con Anteros documentado: sabía que la
0.15 (Δ métrica producía disparate impact sobre grupos
máximo) específicos —había pruebas internas— y deliberadamente
no modificó el diseño. O desplegador que conocía el
disparate impact del sistema y lo escaló sin salvaguardas
porque el costo del retraso superaba —en su evaluación—
el costo del daño.

Taxonomía General de Aplicaciones
Nivel de
Descripción del actor en el dominio algorítmico
α
α = 0.16– Diseñador que usó una métrica con disparate impact
0.35 documentado en la literatura del campo sin realizar
auditoría de la alternativa de menor impacto. Desplegador
que lanzó a escala sin auditoría del sistema en el dominio
de despliegue específico. Curador que usó dataset con
sesgo conocido sin debiasing ni documentación del sesgo
residual.
α = 0.36– Diseñador que realizó auditoría del modelo, pero no de la
0.55 métrica. Desplegador que implementó monitoreo del
rendimiento del sistema, pero no de su disparate impact.
Regulador que publicó guías no vinculantes de buenas
prácticas sin estándares de auditoría exigibles.
α = 0.56– Diseñador que documentó las alternativas de métrica y
0.74 eligió con justificación la de menor impacto técnicamente
compatible. Desplegador con monitoreo del disparate
impact en producción, pero sin umbrales de acción
predefinidos. Regulador con estándares de auditoría
obligatorios para algunos dominios de alto impacto.
α = 0.75– Diseñador que realizó análisis formal de alternativas,
0.90 eligió con documentación la de menor impacto, comunicó
el disparate impact residual al desplegador. Desplegador
con auditoría, monitoreo con umbrales de acción y
mecanismo de reclamación funcional. Regulador con
estándares de auditoría exigibles y supervisión post-
despliegue.
α = 0.91– Equipo que implementó el proceso completo: auditoría de
1.00 (Δ ≈ métrica con análisis de alternativas, auditoría de dataset
0) con debiasing documentado, auditoría del sistema en el
dominio de despliegue, monitoreo continuo con umbrales
predefinidos, mecanismo de reclamación, y
documentación transparente del disparate impact residual
comunicada a los afectados.
La paradoja de la auditoría del modelo: por qué atacar
el componente equivocado es ineficaz
El litigio y la regulación de IA tienden a enfocarse en la explicabilidad
y la auditabilidad del modelo — en los pesos, las características de
entrada, las reglas de decisión. Eso es atacar el nodo de menor R*_neta.

Taxonomía General de Aplicaciones
El teorema de Chouldechova (2016) establece que las definiciones de
equidad matemáticamente más intuitivas son incompatibles entre sí
cuando las tasas base de la métrica difieren entre grupos — lo que ocurre
precisamente cuando la métrica está sesgada históricamente. El sistema
COMPAS no podía simultáneamente satisfacer la equidad de
calibración (igual precisión entre grupos) y la equidad de paridad (igual
tasa de error entre grupos) porque las tasas de reincidencia diferían entre
grupos — y las tasas diferían porque la métrica target ('nuevo arresto')
era función de las tasas de arresto diferencial de la policía, que son en sí
mismas sesgadas. La solución no era cambiar el modelo: era cambiar la
métrica de 'nuevo arresto' a 'nueva condena con pruebas suficientes'.
§5 Tipos de nodo, tipos de arista y
configuraciones canónicas del dominio
Tipos de nodo en el grafo algorítmico
Tipo de Función en R* en el grafo de
S típico
nodo el grafo daño algorítmico
Diseñador Tomó la S bajo [0.05– R*_DM × D_total
de la métrica decisión 0.30] cuando × (1 − α_DM). El
(DM) normativa de la métrica era más alto del grafo
qué optimiza idiosincrática cuando hay
el sistema. Es del alternativas de
la decisión de diseñador. S métrica con menor
mayor alto [0.50– disparate impact
consecuencia 0.78] cuando documentadas en el
en el grafo. R* la métrica era período.
positivo el estándar
cuando la del campo.
elección de la
métrica era la
condición
necesaria del
disparate
impact y había
alternativas
disponibles
con menor
impacto.

Taxonomía General de Aplicaciones
Tipo de Función en R* en el grafo de
S típico
nodo el grafo daño algorítmico
Curador del Seleccionó y S alto [0.55– R*_CD × D_total.
dataset (CD) preparó los 0.85] en la La fracción del
datos de mayoría de disparate impact
entrenamiento los casos: el atribuible al sesgo
del modelo. sesgo del dataset
R* positivo histórico del (DI_dataset /
cuando el dataset es DI_total).
sesgo del compartido
dataset era por todos los
conocido o que usaron
detectable y datos de ese
no fue período.
corregido. El
dataset es un
nodo técnico
sin voluntad
— su R*
apunta hacia
los actores que
lo generaron
históricamente
y hacia quienes
lo usaron sin
auditoría.
Modelo Optimizó la S ≈ 1.0 en R*_neta_ML =
(ML) métrica dada todos los R*_ML × (1 −
sobre el casos. Es el S_ML) ≈ 0. Cambiar
dataset dado. principio el modelo sin
Nodo técnico algorítmico cambiar la métrica ni
sin voluntad central del el dataset tiene
propia. S ≈ 1.0 dominio. impacto mínimo
porque es sobre el disparate
fungible: impact.
cualquier
modelo
competente
con la misma
métrica y
dataset habría
producido el
mismo
resultado.

Taxonomía General de Aplicaciones
Tipo de Función en R* en el grafo de
S típico
nodo el grafo daño algorítmico
Desplegador Tomó la Variable: S R*_DE × D_total ×
(DE) decisión de bajo [0.10– (1 − α_DE). Incluye
implementar 0.35] si el el R* por el daño
el sistema en el despliegue producido durante el
entorno era período entre el
específico idiosincrático despliegue y la
donde en ese corrección cuando el
produjo el dominio. S disparate impact era
daño. R* alto [0.55– detectable.
positivo 0.80] si el
cuando la despliegue
auditoría del era el
sistema en ese estándar de la
entorno habría industria.
revelado el
disparate
impact o
cuando el
monitoreo en
producción no
fue adecuado.
Regulador Estableció — Alto [0.55– Fracción del daño
(RG) o no 0.82] cuando total atribuible al
estableció— la ausencia de exceso de disparate
los estándares estándares impact sobre el
de auditoría y era el umbral que la
las paradigma regulación adecuada
condiciones regulatorio habría establecido.
de despliegue del período.
en Moderado
aplicaciones [0.35–0.55]
de alto cuando la
impacto. R* evidencia de
positivo por los riesgos
omisión del sistema
cuando los era ya
estándares suficiente
eran para justificar
insuficientes la acción.
dado el estado
del
conocimiento
sobre los

Taxonomía General de Aplicaciones
Tipo de Función en R* en el grafo de
S típico
nodo el grafo daño algorítmico
riesgos del
sistema.
Configuraciones canónicas del dominio
Configuración 1 — Sistema algorítmico de decisión de alto
impacto con disparate impact racial
Caso tipo COMPAS/Amazon. DM (diseñador de la métrica 'reincidencia
como nuevo arresto' o 'candidato exitoso como similar al historial': S
moderado-bajo [0.15–0.35], la métrica era una elección entre alternativas
documentadas) + CD (dataset de arrestos sesgados por políticas de vigilancia
diferencial: S alto, el sesgo era sistémico del período) + ML (modelo que
aprendió el patrón: S ≈ 1.0, R*_neta ≈ 0) + DE (desplegador sin auditoría
de equidad independiente antes del despliegue a escala: α bajo) + RG
(regulador sin estándares de auditoría exigibles en el período)
DI_total = DI_métrica (≈40%) + DI_dataset (≈50%) + DI_modelo
(≈10%). R*_DM × (1−S_DM) >> R*_ML × (1−S_ML) ≈ 0.
D_total_algorítmico = N_afectados × D_promedio_individual +
D_sistémico_adicional.
El litigio que ataca la explicabilidad del modelo está atacando el nodo de
menor R*_neta. El litigio que establece que la métrica alternativa ('nueva
condena' en lugar de 'nuevo arresto') habría reducido el DI en más del 30%
está atacando el nodo de mayor R*_neta con S moderado-bajo.
Configuración 2 — Sistema autónomo con daño físico
(vehículo autónomo)
DM_reglas (diseñador de las reglas de decisión del sistema ante dilemas éticos
—priorización del pasajero versus el peatón en colisiones inevitables: S bajo,
la jerarquía de valores era una elección entre alternativas filosóficamente
debatidas) + DE_fabricante (fabricante que desplegó el sistema con esas
reglas sin validación con los estándares éticos de la jurisdicción) +

Taxonomía General de Aplicaciones
DE_operador (empresa o individuo que operó el vehículo en el entorno
específico del accidente) + RG (regulador que no estableció estándares de
certificación de las reglas de decisión éticas antes de la autorización de
operación)
El daño por distribución fuera del rango de entrenamiento (distribution shift):
cuando el sistema autónomo falla en una situación que no estaba representada
en el dataset de entrenamiento, el R* del diseñador del proceso de validación
y del curador del dataset de entrenamiento supera al del modelo. La auditoría
de la cobertura del dataset de entrenamiento respecto al dominio de despliegue
es el instrumento central.
Configuración 3 — Modelo de lenguaje grande (LLM) con
daño a terceros
DM_base (desarrollador del modelo base con la métrica de entrenamiento que
determina el comportamiento por defecto: S moderado, la elección del corpus y
del proceso de alineamiento tiene alternativas documentadas) + DE_fine-
tuner (empresa o individuo que ajustó el modelo base para el caso de uso sin
restricciones de contenido adecuadas para ese dominio) + DE_aplicación
(operador de la aplicación que dio acceso al modelo sin filtros adecuados para
el contexto de uso) + Usuario (actor que usó el modelo para producir el daño:
S variable según si el sistema tenía restricciones que impidieran el uso dañino)
La cadena de responsabilidad en LLMs es más larga que en los sistemas de
decisión: el desarrollador del modelo base, el ajustador fino, el operador de la
aplicación y el usuario tienen R* sobre el daño en proporciones que dependen
de las restricciones que cada nodo de la cadena implementó. El principio
algorítmico se aplica: el modelo tiene S alto entre modelos equivalentes, pero
la elección del proceso de alineamiento (RLHF, los valores que se reforzaron)
tiene S bajo.
§6 Preguntas que responde este capítulo

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
¿Cuál es el nodo Auditoría de la métrica Declaración B con
de mayor (IA2): ¿hay alternativas de auditoría de la métrica
R*_neta en el métrica con menor IA2 que establezca las
grafo disparate impact que eran alternativas
algorítmico — técnicamente disponibles disponibles.
el modelo, la en el período? Si Declaración A si hay
métrica, o el DI_métrica_alternativa documentos internos
dataset? << DI_métrica_actual, el que muestren el
R*_DM es el dominante. análisis de alternativas
Cálculo de S_modelo: si (IA1). Declaración C
cualquier modelo si la auditoría de la
competente con la misma métrica debe
métrica y dataset habría realizarse
producido el mismo retroactivamente
resultado, R*_neta_ML ≈ sobre el sistema ya
0. desplegado.
¿El diseñador Cronología del Declaración A con
sabía que la conocimiento del disparate documentos internos
métrica impact: ¿había IA1 que muestren el
producía publicaciones del campo conocimiento del
disparate que documentaban el disparate impact.
impact — cuál problema de la métrica Declaración B con
es su Hijo antes del despliegue? ¿Hay cronología de
dominante? documentos internos de publicaciones del
pruebas que mostraban el campo sobre el
impacto diferencial? problema de la
¿Otros sistemas del campo métrica. Declaración
habían adoptado métricas C si el estado del
alternativas? conocimiento debe
inferirse solo desde la
literatura pública del
período.
¿Cuál es la Auditoría IA2 con análisis Declaración B con
descomposición contrafáctico: ¿cuál habría auditoría IA2 que
del disparate sido el DI con la métrica tenga acceso al
impact — alternativa óptima, dado el sistema o a un sistema
DI_métrica + mismo dataset? ¿Cuál equivalente con la
DI_dataset + habría sido el DI con el métrica alternativa.
DI_modelo? dataset debiased, dada la Declaración C
misma métrica? La cuando la
diferencia entre el DI descomposición debe
observado y el DI estimarse desde el
contrafáctico establece la análisis teórico del

Taxonomía General de Aplicaciones
Pregunta del Instrumento que la Nivel de certeza
caso responde posible
fracción atribuible a cada sesgo sin acceso al
componente. sistema.
¿El daño del Análisis de la cobertura del Declaración B con
sistema dataset de entrenamiento auditoría del dataset
autónomo fue respecto al dominio de de entrenamiento y
por distribution despliegue: ¿estaba la análisis del evento de
shift — el situación del accidente o el fallo respecto a la
sistema falló fallo representada en el distribución del
fuera del rango dataset de entrenamiento? training data.
de Si no estaba representada, Declaración A si hay
entrenamiento? el R* del diseñador del documentación del
proceso de validación proceso de validación
supera al del modelo que muestra las
específico que falló. situaciones excluidas
del testing.
¿Cuál es el D_total_algorítmico = Declaración B para el
D_total del N_afectados × D_individual con los
daño D_promedio_individual + instrumentos del
algorítmico — D_sistémico_adicional. dominio de
individual y Para daños individuales: aplicación.
sistémico? los mismos instrumentos Declaración C para el
que en los caps. D_sistémico cuando
correspondientes al el número de
dominio (cap. 1 para daño afectados y el
en justicia penal, cap. 25 D_promedio deben
para daño laboral, cap. 27 estimarse con
para daño sanitario). El supuestos de alto
D_sistémico adicional impacto sobre el
captura el efecto de escala resultado.
del sistema sobre la
población afectada.
§7 Traducción de D_total al dominio
algorítmico
D_total_algorítmico = N_afectados ×
D_promedio_individual + D_sistémico_adicional

Taxonomía General de Aplicaciones
El daño algorítmico tiene una característica singular respecto a todos los
demás capítulos del libro: opera simultáneamente a escala individual y a escala
poblacional. El sistema de IA toma decisiones sobre cada individuo afectado
(D_individual: la persona que no obtuvo el crédito por el score sesgado, la
persona que recibió una evaluación de riesgo más alta por el sistema penal
sesgado) y sobre el conjunto de los afectados (D_sistémico: el efecto acumulado
del disparate impact sobre la distribución de oportunidades, la cronificación
de la desigualdad estructural, el daño a la confianza en las instituciones). El
D_sistémico puede superar al D_individual agregado cuando el sesgo afecta
a grupos ya estructuralmente desfavorecidos.
En el
Compone dominio Fuente de
Cómo se cuantifica
nte algorítmic evidencia
o
D_individu El daño de D_promedio_individu Registros del
al × cada al × N_afectados = Σ sistema con
N_afectad individuo D_i para todos los las decisiones
os (daño afectado por individuos afectados. individuales.
directo por la decisión Para sistemas penales: Datos de
decisión incorrecta AVAD_privación_de_ seguimiento
incorrecta) del sistema: libertad + de los
la persona ΔT_trayectoria_post- afectados
clasificada encarcelamiento. Para (registros de
incorrectam sistemas de empleo: empleo,
ente en el diferencial de ingresos ingresos,
sistema acumulados. Para antecedentes)
penal sistemas de crédito: . Análisis de
(D_vital por diferencial de acceso al los
los meses de capital y acumulación counterfactua
privación de de patrimonio. ls individuales
libertad con el sistema
adicional), la sin el
persona disparate
excluida del impact.
empleo
(D_vital por
la pérdida
de ingresos
y trayectoria
laboral), la
persona
excluida del
crédito
(D_vital por

Taxonomía General de Aplicaciones
En el
Compone dominio Fuente de
Cómo se cuantifica
nte algorítmic evidencia
o
el acceso al
capital y la
acumulació
n de
patrimonio).
Se calcula
con los
instrumento
s del cap. del
dominio de
aplicación
específico.
D_sistémic El daño que D_sistémico requiere Datos
o (daño a la supera a la modelización con macroeconó
distribució suma de los supuestos sobre el micos de
n de daños efecto multiplicador distribución
oportunida individuales: del sesgo algorítmico de ingresos,
des y el efecto del sobre la desigualdad acceso al
cronificaci disparate estructural crédito, tasas
ón de la impact preexistente. El análisis de empleo y
desigualda sobre la del índice de Gini de la encarcelamie
d) distribución distribución de nto por grupo
de oportunidades antes y antes y
oportunidad después del despliegue después del
es en la del sistema es el despliegue del
población indicador más sistema.
afectada, la directamente medible. Encuestas de
señal confianza
sistémica institucional.
que envía a Análisis de la
grupos persistencia
sobre qué es intergeneraci
posible para onal de la
ellos, el desventaja en
daño a la los grupos
confianza afectados.
en las
institucione
s que usan el
sistema, la
cronificació
n de la
desigualdad

Taxonomía General de Aplicaciones
En el
Compone dominio Fuente de
Cómo se cuantifica
nte algorítmic evidencia
o
estructural
que el
sistema
reprodujo a
escala y
velocidad
algorítmica.
ΔT_trayect El desvío de D_ΔT = diferencial de Estudios
oria (desvío la trayectoria vital entre la longitudinales
de la trayectoria población afectada y la de los
trayectoria de vida de contrafáctica sin el afectados por
vital de los los disparate impact del sistemas con
afectados individuos sistema, multiplicado disparate
por el afectados por el número de impact
disparate por el afectados. Requiere documentado
impact acceso análisis longitudinal de . Datos de
crónico) diferencial a los afectados versus movilidad
oportunidad grupo de control. intergeneraci
es que el onal en los
sistema grupos
produjo: la afectados.
reducción Análisis de la
de la transmisión
expectativa intergeneraci
de ingresos onal de la
de vida, la desventaja
reducción producida por
del el sistema.
potencial
educativo
de los hijos
de los
afectados, el
daño a la red
de
relaciones
por la
exclusión de
institucione
s donde el
sistema
tomaba
decisiones

Taxonomía General de Aplicaciones
En el
Compone dominio Fuente de
Cómo se cuantifica
nte algorítmic evidencia
o
con
disparate
impact.
§8 Límites del método y errores frecuentes de
aplicación
Límites del método en el dominio algorítmico
Límite 1 — La imposibilidad de la equidad perfecta cuando las
tasas base difieren entre grupos. El teorema de Chouldechova
establece que las definiciones de equidad matemáticamente
más intuitivas son incompatibles entre sí cuando las tasas base
de la métrica difieren entre grupos. El análisis de
responsabilidad no puede requerir que el sistema satisfaga
simultáneamente todas las definiciones de equidad — debe
establecer cuál definición era la más relevante para el dominio
de aplicación y si el sistema la satisfacía.
Límite 2 — El problema del sesgo emergente: cuando el
sistema aprende más que la métrica. Algunos sistemas de IA
desarrollan patrones de comportamiento que no estaban
codificados en la métrica ni en el dataset, pero emergen de su
interacción. El sesgo emergente es más difícil de atribuir a una
decisión normativa específica porque no fue intencional ni
predictible desde ningún punto del diseño.
Límite 3 — La opacidad de los modelos de aprendizaje
profundo. Los modelos de redes neuronales profundas son
difíciles de auditar porque la relación entre las entradas y las
salidas no es transparente. Esa opacidad no reduce el R* del
diseñador de la métrica — el diseñador de la métrica tiene R*
por haber elegido un objetivo que produce disparate impact
independientemente de que el modelo sea o no explicable.

Taxonomía General de Aplicaciones
Pero la opacidad sí reduce la certeza con que el análisis puede
atribuir el daño a componentes específicos del sistema.
Límite 4 — La causalidad en sistemas de recomendación: el
problema del counterfactual. Los sistemas de recomendación
producen daños difusos y acumulativos donde establecer qué
habría ocurrido sin el sistema tiene alta incertidumbre. La
relación entre el algoritmo de recomendación de contenido y
la radicalización de un usuario específico no puede
establecerse con el mismo nivel de certeza que la relación entre
el sistema de scoring crediticio y la denegación de un crédito
específico.
Errores frecuentes de aplicación
Por qué
Error Consecuencia Corrección
ocurre
Atacar la La Se ataca el La auditoría que
explicabilidad explicabilidad nodo de menor establece el R*
del modelo en del modelo R*_neta del debe comenzar
lugar de la (SHAP, grafo. La por la métrica:
auditoría de la LIME, árboles explicabilidad ¿cuál era la
métrica de decisión del modelo variable
interpretativos muestra cómo objetivo? ¿Cuáles
) es el sistema tomó eran las
técnicamente una decisión, alternativas
más accesible no si la métrica disponibles?
que la que optimizaba ¿Cuánto del
auditoría de la era la correcta. disparate impact
métrica La estrategia de habría reducido
objetivo. El litigio es la métrica
litigio se ineficaz para el alternativa? La
enfoca en lo nodo de mayor explicabilidad del
que se puede responsabilida modelo es
medir d. complementaria,
fácilmente. no central.
Confundir el El disparate Anteros La
disparate impact atribuido a descomposición
impact del observable en actores con DI_total =
sistema con la los outputs del Potós o DI_métrica +
intención sistema se usa Deimos. El DI_dataset +
discriminatori para inferir la diseñador que DI_modelo
intención siguió los permite separar
discriminatori estándares del la fracción del DI

Taxonomía General de Aplicaciones
Por qué
Error Consecuencia Corrección
ocurre
a del a del campo del atribuible a cada
diseñador diseñador, sin período tiene S nodo antes de
distinguir moderado-alto analizar el Hijo
entre el DI y no tiene dominante del
producido por responsabilida diseñador.
la métrica d por la
(decisión fracción del DI
normativa), atribuible al
por el dataset sesgo histórico
(sesgo del dataset.
histórico
sistémico) y
por el modelo
(residual).
Atribuir el R* El equipo R* incorrecto: El equipo
del modelo al técnico es el el equipo técnico solo tiene
equipo actor más técnico tiene S R* positivo
técnico que lo visible en la ≈ 1.0 porque cuando su
construyó cadena de cualquier implementación
desarrollo del equipo se desvió de lo
sistema. El competente que el diseñador
análisis se habría de la métrica y el
enfoca en lo producido el curador del
que el equipo mismo sistema dataset
técnico hizo con la misma especificaron —
en lugar de en métrica y cuando el DI del
la decisión dataset. El modelo supera
normativa del R*_neta del significativament
diseñador de equipo técnico e al DI esperado
la métrica. es próximo a 0. dado la métrica y
El R* migra al el dataset.
diseñador de la
métrica.
No calcular el El análisis D_total El D_total debe
D_sistémico calcula solo el algorítmico incluir el
del daño daño subestimado. componente
algorítmico individual de En sistemas sistémico: el
las decisiones que operaron efecto del
incorrectas durante años disparate impact
específicas del sobre millones sobre la
sistema sin de individuos, distribución de
capturar el el D_sistémico oportunidades
efecto de puede superar en la población
escala del al D_individual afectada, la

Taxonomía General de Aplicaciones
Por qué
Error Consecuencia Corrección
ocurre
disparate agregado. La cronificación de
impact sobre pretensión no la desigualdad
la distribución refleja la estructural, y el
de magnitud real daño a la
oportunidades del daño. confianza
. institucional.
§9 Guía de prioridades de recolección de
evidencia
La primera decisión es establecer cuál es el tipo de sistema:
sistema de decisión de alto impacto (empleo, crédito, justicia
penal, salud), sistema de recomendación, sistema autónomo
con capacidad de daño físico, o LLM. Cada uno tiene un
instrumento causal central diferente y una jerarquía de nodos
con R* distinta.
Tabla de prioridades de recolección de evidencia en IA y
sistemas automatizados
La
Si tu
evidenci
incertidu Qué Qué buscar /
a que Por qué
mbre rango qué
más la funciona
principal reduce preguntar
reduce
es...
1. ¿Cuál es Establece El tipo de Determi ¿Cuál es la
el tipo de r la sistema na la variable
sistema y arquitect determina el estrategi objetivo que
su nodo ura del instrumento a de optimiza el
de mayor sistema: central y el auditoría sistema? ¿Con
R*? ¿qué nodo de e qué datos fue
métrica mayor R*. La instrume entrenado?
optimiza? auditoría de la nto ¿Quién definió
¿Con qué métrica es causal la métrica
dataset siempre la (incertid objetivo?
fue prioridad 1. umbre ¿Cuándo fue
entrenad desplegado y

Taxonomía General de Aplicaciones
La
Si tu
evidenci
incertidu Qué Qué buscar /
a que Por qué
mbre rango qué
más la funciona
principal reduce preguntar
reduce
es...
o? estructur en qué
¿Quién al). dominio?
tomó las
decisione
s
normativ
as clave?
2. ¿Cuáles Auditoría El R*_DM es Establec ¿Había otras
eran las IA2 de la función de si e el métricas
alternativa métrica alternativas R*_DM usadas en
s de con con menor y su S sistemas
métrica análisis DI eran (incertid similares del
— cuál es del técnicamente umbre campo con
el R* del DI_métri disponibles. ontológi menor
DM? ca: Si ca del disparate
¿cuánto DI_métrica_a nodo impact? ¿El
habría lternativa ≈ 0 diseñado equipo interno
reducido y r). evaluó
el DI_métrica_a alternativas?
disparate ctual >> 0, el ¿Las
impact la diseñador publicaciones
métrica tiene R* del campo del
alternativ pleno sobre período
a óptima? ese señalaban el
Docume componente. problema de la
ntos métrica usada?
internos
IA1 que
muestren
el análisis
de
alternativ
as.
3. ¿Cuál es Análisis Sin el Establec ¿Cuáles son las
el de los DI_total y su e el tasas de error
disparate outputs descomposici D_total del sistema
impact del ón, el análisis y la entre grupos?
document sistema de R* no tiene distribuc ¿Hay datos de
ado — (IA4) + base empírica. ión de los outputs del
cuál es el auditoría El DI_total R* entre sistema sobre

Taxonomía General de Aplicaciones
La
Si tu
evidenci
incertidu Qué Qué buscar /
a que Por qué
mbre rango qué
más la funciona
principal reduce preguntar
reduce
es...
DI_total y IA2 con establece la DM, CD la población
su análisis escala del y ML afectada? ¿Se
descompo contrafác daño y la (incertid puede
sición? tico de la descomposici umbre reconstruir el
métrica y ón distribuye empírica DI con la
el dataset. el R*. central). métrica
alternativa?
4. ¿El Docume El Hijo Establec ¿Hay
diseñador ntos dominante e el S del documentos
sabía del internos determina el S DM y la internos de
disparate IA1 del del DM. fracción pruebas que
impact — período Anteros → S idiosincr muestren el
cuál es el + bajo [0.03– ática del disparate
Hijo cronologí 0.20]; Potós R* impact antes
dominant a de → S (incertid del
e? publicaci moderado- umbre despliegue?
ones del alto [0.40– ontológi ¿Las
campo 0.70]; Deimos ca). publicaciones
sobre el → S alto del campo ya
problema [0.56–0.84]. documentaba
de la n el problema?
métrica ¿Otros
usada + sistemas
compara comparables
ción con habían
la adoptado la
adopción métrica
de alternativa?
métricas
alternativ
as en
sistemas
del
campo.
5. ¿El Registros El R*_DE Establec ¿Realizó el
desplegad del depende de si e el desplegador
or realizó proceso el disparate R*_DE auditoría de
auditoría de impact era y el equidad del
antes del validació detectable en α_DE sistema en el
n antes el dominio (incertid dominio de

Taxonomía General de Aplicaciones
La
Si tu
evidenci
incertidu Qué Qué buscar /
a que Por qué
mbre rango qué
más la funciona
principal reduce preguntar
reduce
es...
despliegue del específico de umbre despliegue
? lanzamie despliegue del nodo antes del
nto + antes del desplega lanzamiento?
auditoría lanzamiento a dor). ¿Había
s de escala. monitoreo del
equidad disparate
realizadas impact en
+ producción?
mecanis ¿Existía
mos de mecanismo de
monitore reclamación?
o
impleme
ntados.
6. ¿Cuál es D_indivi Sin el D_total, Establec ¿Cuántos
el D_total dual: el AD de cada e la individuos
— instrume nodo no tiene escala de fueron
individual ntos del base la afectados por
y cap. del cuantificada. pretensi el disparate
sistémico? dominio ón impact del
de (incertid sistema? ¿Cuál
aplicació umbre es el
n (cap. 1 empírica D_promedio_
para del individual
justicia daño). dado el tipo de
penal, decisión?
cap. 25 ¿Qué efecto
para tuvo el sistema
empleo, sobre la
etc.). distribución
D_sistém de
ico: datos oportunidades
de en la
distribuci población
ón de afectada?
oportuni
dades
antes y
después
del

Taxonomía General de Aplicaciones
La
Si tu
evidenci
incertidu Qué Qué buscar /
a que Por qué
mbre rango qué
más la funciona
principal reduce preguntar
reduce
es...
despliegu
e.
Árbol de decisión en IA y sistemas automatizados: tres
pasos
¿Cuál es el tipo de sistema y su nodo de mayor R* probable?
│
├─ ANÁLISIS A: SISTEMA DE DECISIÓN DE ALTO
IMPACTO (empleo, crédito, justicia, salud)
│ └─ PRIORIDAD 1: Auditoría de la métrica
objetivo → ¿cuáles eran las alternativas
disponibles?
│ · DI_métrica_alternativa <<
DI_métrica_actual → R*_DM dominante con S
bajo.
│ · S_modelo ≈ 1.0 → cambiar el modelo sin
cambiar la métrica no resuelve el problema.
│ └─ PRIORIDAD 2: Descomposición
DI_total = DI_métrica + DI_dataset +
DI_modelo
│ · Establece la distribución del R* entre DM,
CD y ML (neto ≈ 0 para ML).
│ └─ PRIORIDAD 3: Hijo dominante del DM
→ Anteros / Potós / Deimos
│ · Anteros → S_DM bajo [0.03–0.20]. R*
pleno sobre DI_métrica.
│ └─ PRIORIDAD 4: D_total = N_afectados
× D_individual + D_sistémico
├─ ANÁLISIS B: SISTEMA DE RECOMENDACIÓN
→ cap. 17 (plataformas digitales) como instrumento
primario

Taxonomía General de Aplicaciones
│ └─ Escala PD0–PD8 del cap. 17. El
principio del diseñador de la métrica aplica
igualmente.
│ · La métrica de engagement que el
recomendador optimiza es el nodo de mayor R*.
├─ ANÁLISIS C: SISTEMA AUTÓNOMO CON
DAÑO FÍSICO
│ └─ PRIORIDAD 1: ¿El fallo fue dentro del
rango de entrenamiento o por distribution shift?
│ · Dentro del rango → R* del diseñador de
las reglas de decisión. Las reglas eran la condición
necesaria.
│ · Distribution shift → R* del diseñador del
proceso de validación que no cubrió esa situación.
│ └─ PRIORIDAD 2: ¿El desplegador operó el
sistema en el entorno para el que fue certificado?
│ · Si el entorno de despliegue excedió el
dominio de certificación → R*_DE positivo.
└─ ANÁLISIS D: LLM / SISTEMA GENERATIVO
└─ PRIORIDAD 1: Identificar el nodo de la
cadena donde se tomó la decisión que permitió
el daño
· Desarrollador modelo base / Ajustador fino
/ Operador de la aplicación / Usuario.
└─ PRIORIDAD 2: ¿El nodo tenía
restricciones que habrían prevenido el daño
específico?
· Si las restricciones habrían prevenido el daño
y no fueron implementadas → R* de ese nodo
positivo.
├─ Paso 2: ¿El diseñador de la métrica tiene Anteros o
Potós documentado?
│
├─ Anteros documentado → S_DM bajo [0.03–0.20] →
R*_DM pleno sobre DI_métrica
│ └─ El DM sabía que la métrica producía DI
y eligió no modificarla. Pretensión máxima
contra DM.

Taxonomía General de Aplicaciones
├─ Potós (estándar del campo del período) → S_DM
moderado-alto [0.40–0.70]
│ └─ Responsabilidad civil. Reforma del
sistema con auditoría de la métrica como
requisito.
└─ Deimos (evidencia del DI de la métrica no disponible
en el período) → S_DM alto [0.56–0.84]
└─ Responsabilidad reducida del DM.
Analizar R*_RG por ausencia de estándares de
auditoría.
└─ Paso 3: ¿El D_total incluye el componente sistémico?
├─ SÍ (sistema operó durante meses o años sobre
población amplia) → D_sistémico relevante
│ └─ D_total = N_afectados × D_individual
+ D_sistémico. El D_sistémico puede dominar.
└─ NO (sistema de despliegue limitado o daño
individual único) → D_total = D_individual
└─ AD_i = R*_i × D_individual × (1 − α_i).
Mismos instrumentos del dominio de
aplicación.
— Fin del Capítulo 49 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

