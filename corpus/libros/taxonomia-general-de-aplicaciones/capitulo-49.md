PARTE VII · Ingeniería y Tecnología

## Capítulo 49

### Inteligencia artificial y sistemas

### automatizados

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo

Este capítulo es Nivel C — el nivel de mayor incertidumbre de la taxonomía. Sus rangos w son candidatos derivados por extensión teórica desde El cálculo de la responsabilidad cap. 13 (IA y algoritmos de decisión), no por calibración empírica con datos de litigios. Antes de usarlos en un procedimiento con pretensión formal, consultar la jurisprudencia emergente de responsabilidad algorítmica en la jurisdicción competente. El capítulo es candidato prioritario a la Revista Meriadock.

La aportación central es conceptual: la jerarquía de responsabilidad en los sistemas de IA invierte la jerarquía de visibilidad. El modelo — el componente más visible del sistema — tiene R* próximo a cero porque S_modelo ≈ 1.0: cualquier modelo competente entrenado con la misma métrica y el mismo dataset habría producido el mismo resultado dañino. Quien tiene el mayor R* es el diseñador de la métrica: la persona que decidió qué optimiza el sistema. Esa es una decisión normativa, no técnica, y es idiosincrática — alternativas estaban disponibles.

Si tu caso es de sesgo algorítmico en decisiones de alto impacto (empleo, crédito, justicia penal, diagnóstico médico), ve a §1, §3 y §5. Si es de daño por sistema autónomo (vehículo, drone, arma), ve a §1 y §5 configuración 2. Si es de daño por modelo de lenguaje grande (LLM), ve a §1 y §5 configuración 3. Para la descomposición del disparate impact, ve a §4. Para la prioridad de evidencia, ve directamente a §9.

Taxonomía General de Aplicaciones

### §1  Descripción del subcampo

Los sistemas de inteligencia artificial y decisión automatizada son el dominio donde la jerarquía de responsabilidad está más sistemáticamente invertida respecto a la jerarquía de visibilidad. El modelo de machine learning —el componente más visiblemente complejo del sistema— tiene índice de sustituibilidad S prácticamente igual a 1.0 y, por tanto, R*_neta ≈ 0: cualquier modelo competente entrenado con la misma métrica objetivo y el mismo dataset de entrenamiento habría aprendido los mismos patrones y producido los mismos daños. Cambiar el modelo sin cambiar la métrica ni el dataset no resuelve el problema. El principio algorítmico de El cálculo de la responsabilidad cap. 13 es la piedra de cimiento de este capítulo: el R* migra del componente técnico visible al decisor normativo invisible que eligió qué optimiza el sistema.

Esta inversión no es solo analíticamente relevante —es jurídicamente transformadora. El litigio de responsabilidad algorítmica que se enfoca en el modelo (su explicabilidad, sus métricas de fairness, su arquitectura) está atacando el nodo de menor R*_neta del grafo. El litigio que se enfoca en el diseñador de la métrica —la persona que decidió que «éxito» en el sistema de contratación de Amazon significaba «similitud con el historial de ingenieros masculinos contratados en la última década»— está atacando el nodo de mayor R*_neta con S bajo: esa elección no era la única técnicamente disponible, era la elección que ese diseñador específico hizo entre alternativas con consecuencias distribucionales distintas.

El principio del diseñador de la métrica: la jerarquía de responsabilidad algorítmica En todo sistema algorítmico, la decisión normativa de mayor R* no es la que escribe el código del modelo — es la que define qué objetivo optimiza ese modelo. El modelo tiene S ≈ 1.0 porque es técnicamente fungible: dado una métrica y un dataset, cualquier equipo competente produce un modelo con el mismo comportamiento. El diseñador de la métrica tiene S bajo porque la elección de qué optimizar es normativa e idiosincrática — alternativas con menores consecuencias dañinas estaban técnicamente disponibles.

Taxonomía General de Aplicaciones

R*_modelo × (1 − S_modelo) ≈ 0       →       cambiar el

modelo sin cambiar la métrica no reduce el daño R*_métrica × (1 − S_métrica) >> 0    →       la elección de

la métrica era la condición necesaria idiosincrática Esta jerarquía aplica a todos los sub-dominios del capítulo: el sistema de reconocimiento facial con sesgo racial tiene S_modelo ≈ 1.0 y S_métrica bajo (la elección de entrenar con datasets de composición racial sesgada era una elección entre alternativas). El vehículo autónomo que priorizó la minimización del daño al pasajero tiene S_modelo ≈ 1.0 y S_reglas_de_decisión bajo (la jerarquía de valores del sistema era una decisión ética que alguien tomó). El LLM que genera desinformación convincente tiene S_modelo ≈ 1.0 y S_objetivo_de_entrenamiento bajo.

### Sub-variantes del dominio

Sub-variante Descripción y singularidades del dominio

Sistemas algorítmicos de decisión de alto impacto

Los sistemas que toman decisiones con consecuencias directas sobre derechos y oportunidades individuales: sistemas de evaluación del riesgo de reincidencia en el sistema penal (COMPAS), sistemas de screening de candidatos en procesos de contratación (Amazon Hiring AI), algoritmos de scoring crediticio, sistemas de diagnóstico médico automatizado, algoritmos de asignación de prestaciones sociales. El daño en este sub-campo tiene dos componentes: el daño individual de las decisiones incorrectas y el daño sistémico del disparate impact sobre grupos protegidos. El diseñador de la métrica objetivo tiene el mayor R* en ambos componentes.

Sistemas de recomendación y amplificación algorítmica

Los algoritmos que determinan qué contenido ve cada usuario en plataformas digitales, qué productos se recomiendan, qué noticias aparecen primero. El daño incluye la amplificación de desinformación, la radicalización hacia posiciones extremas, la exposición de menores a contenido dañino y la creación de cámaras de eco informativas. Se conecta directamente con el cap. 17 (plataformas digitales) donde se desarrolló la escala PD0–PD8 y el instrumento de la auditoría algorítmica para este tipo específico de daño.

Taxonomía General de Aplicaciones

Sub-variante Descripción y singularidades del dominio

Sistemas autónomos con capacidad de daño físico

Los vehículos autónomos, los drones, los robots industriales y —en el extremo del espectro— los sistemas de armas autónomos letales (LAWS). En estos sistemas, el daño físico directo es la consecuencia de las reglas de decisión del sistema en situaciones que el diseñador no anticipó completamente. El grafo de responsabilidad es singular: el fabricante del sistema (diseñador de las reglas de decisión), el certificador (que verificó la seguridad del sistema), el desplegador (que lo puso en operación en ese entorno específico), y el regulador (que estableció o no estableció los estándares de certificación). Nivel C porque la jurisprudencia es incipiente.

Modelos de lenguaje grandes (LLMs) y sistemas generativos

Los modelos de lenguaje que generan texto, imágenes, audio y video con alta verosimilitud. El daño incluye la generación de desinformación convincente, la producción de contenido que viola derechos de autor o la privacidad, la generación de discurso de odio o contenido ilegal, y la facilitación de daños cuando el usuario del modelo los usa para causar daño a terceros. La cadena de responsabilidad es más larga que en los sistemas de decisión: el desarrollador del modelo base, el ajustador fino (fine-tuner) que adaptó el modelo para el caso de uso, el desplegador de la aplicación, y el usuario que generó el daño específico.

IA en diagnóstico y decisión médica

Los sistemas de IA que asisten o automatizan el diagnóstico médico (análisis de imágenes radiológicas, detección de patologías en registros clínicos, predicción del riesgo de deterioro del paciente). El daño puede ser por falso negativo (el sistema no detectó una condición que habría detectado un clínico adecuado) o por falso positivo (el sistema indicó una condición que no existía y produjo tratamiento innecesario). Se conecta con el cap. 24 (salud mental) y el cap. 27 (sistemas de salud) para el análisis del R* del sistema versus el R* del clínico que usó el sistema.

IA en sistemas críticos de infraestructura

Los algoritmos que gestionan redes eléctricas, sistemas de transporte, redes financieras y otras infraestructuras críticas. El daño por fallo del sistema algorítmico tiene la estructura del fallo de ingeniería

Taxonomía General de Aplicaciones

Sub-variante Descripción y singularidades del dominio

(cap. 50) pero con la particularidad de que el fallo fue producido por el comportamiento del modelo ante situaciones de distribución de datos fuera del rango de entrenamiento (distribution shift). El diseñador del sistema de monitoreo y del proceso de validación del modelo tiene el mayor R* sobre los daños de los fallos por distribution shift.

### §2  Escala de evidencia IA0–IA8 · Inteligencia artificial y sistemas automatizados

La escala IA0–IA8 traduce la jerarquía general E0–E8 al vocabulario de la responsabilidad algorítmica. Su característica más relevante es la posición central de la auditoría de la métrica (IA2) —que establece qué objetivo optimiza el sistema y cuáles eran las alternativas disponibles— sobre la auditoría del modelo (que establece cómo lo optimiza). El error más frecuente en el peritaje técnico es invertir la prioridad: auditar el modelo primero y la métrica después, cuando la métrica es el nodo de mayor R*. Nivel C — rangos candidatos.

Nota de calibración obligatoria: rangos IA0–IA8

Los rangos w de la escala IA0–IA8 son rangos candidatos derivados por extensión teórica desde El cálculo de la responsabilidad cap. 13 y la escala PD0–PD8 del cap. 17 de esta Taxonomía. No están calibrados empíricamente con datos de litigios de responsabilidad algorítmica. La jurisprudencia en este dominio es incipiente y varía significativamente entre jurisdicciones. El analista debe ajustar los rangos con la jurisprudencia local antes de usarlos en una pretensión formal.

Descripción y ejemplos

Nivel Tipo de evidencia

en el dominio de IA y

Rango w (candidato)

sistemas automatizados

IA1 Documentos internos del

[0.70, 0.88]

Comunicaciones internas donde el diseñador tomó

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

en el dominio de IA y

Rango w (candidato)

sistemas automatizados

diseñador que establecen la decisión de la métrica y sus alternativas conocidas

la decisión de la métrica objetivo con conocimiento de las alternativas y sus consecuencias distribucionales; resultados de pruebas A/B o estudios internos que establecían el efecto del diseño antes de su despliegue a escala; actas del comité de ética o de revisión de riesgos que discutieron el impacto del diseño; documentación de la decisión de desplegar el sistema sin implementar las salvaguardas recomendadas internamente.

IA2 Auditoría algorítmica independiente de la métrica + análisis del disparate impact + peritaje técnico especializado

[0.58, 0.78]

Auditoría algorítmica independiente que establece: (a) la métrica que optimiza el sistema y las alternativas técnicamente disponibles con menor impacto dañino; (b) el disparate impact del sistema sobre grupos protegidos, con análisis de si ese impacto era previsible dado el diseño de la métrica; (c) el análisis S_modelo — si cualquier modelo competente con la misma métrica y dataset habría producido el mismo resultado; (d) el análisis DI_métrica + DI_dataset + DI_modelo para establecer qué fracción del disparate impact total

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

en el dominio de IA y

Rango w (candidato)

sistemas automatizados

era atribuible a cada componente.

IA3 Testimonio de exempleados o investigadores + documentación técnica parcial del sistema

[0.46, 0.64]

Declaraciones convergentes de exempleados que describen el proceso de diseño de la métrica y las decisiones tomadas sobre el dataset de entrenamiento, con corroboración en al menos un documento técnico del sistema; publicaciones académicas de investigadores que tuvieron acceso al sistema y documentaron el disparate impact con metodología replicable.

IA4 Análisis de los outputs del sistema con evidencia del disparate impact observable

[0.34, 0.54]

Análisis estadístico de los outputs del sistema sobre una muestra representativa que establece el disparate impact sobre grupos protegidos, con ajuste por los factores de riesgo legítimos que el sistema puede considerar; comparación de las tasas de error del sistema entre grupos con características comparables.

IA5 Análisis comparativo del comportamiento del sistema con el estándar de referencia

[0.24, 0.42]

Comparación del comportamiento del sistema con el de un sistema de referencia que usa criterios establecidos sin el componente algorítmico; o

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

en el dominio de IA y

Rango w (candidato)

sistemas automatizados

comparación de los resultados del sistema con los de un panel de expertos humanos en los mismos casos, que establece si el sistema produce resultados consistentemente peores para grupos específicos.

IA6 Inferencia desde el diseño del sistema y las características del dataset

[0.14, 0.30]

El diseño del sistema —la métrica documentada en los materiales públicos, el dataset de entrenamiento conocido— permite inferir que el sistema probablemente produce disparate impact sin análisis directo de los outputs del sistema analizado.

IA7 Correlación temporal entre el despliegue del sistema y el daño sin análisis de causalidad algorítmica

[0.05, 0.20]

El daño comenzó a producirse o aumentó significativamente después del despliegue del sistema sin análisis de la cadena causal entre el comportamiento del algoritmo y el daño específico.

IA8 Afirmación de sesgo algorítmico sin evidencia técnica del sistema

[0.02, 0.12]

Afirmación de que el sistema produce sesgo sin evidencia técnica del comportamiento del algoritmo ni análisis de sus outputs.

IA0 Ausencia documentada de nexo causal entre el sistema y

w = 0.00

Auditoría IA2 que establece que el sistema analizado no tiene disparate impact

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

en el dominio de IA y

Rango w (candidato)

sistemas automatizados

el daño analizado

significativo sobre el grupo analizado, o que el daño del caso específico no es causalmente atribuible al sistema sino a otros factores del contexto del caso.

### §3  Firmas documentales por Hijo

Los Hijos de Afrodita aplican en el dominio algorítmico exclusivamente a los actores humanos que tomaron las decisiones normativas del sistema: el diseñador de la métrica objetivo, el curador del dataset de entrenamiento, el directivo que aprobó el despliegue del sistema, el regulador que estableció o no estableció los estándares de auditoría, y el desplegador que implementó el sistema en un contexto específico. Los Hijos no aplican al modelo, al dataset ni a ningún otro componente técnico sin voluntad propia. El error de analizar el «comportamiento del algoritmo» con los Hijos de Afrodita es el error de atribuir voluntad a un instrumento.

La distinción más relevante del dominio es entre el diseñador que sabía que su métrica produciría disparate impact sobre grupos específicos —lo había documentado en pruebas internas— y deliberadamente no modificó el diseño (Anteros), el que siguió los estándares del campo del período sin implementar las auditorías de equidad disponibles (Potós), y el que genuinamente no tenía la evidencia de que el diseño producía el daño porque la auditoría de equidad no era una práctica establecida en el período (Deimos).

§3.1  Hijos de legibilidad alta en el dominio de la IA

Taxonomía General de Aplicaciones

Qué informa para S del diseñador o desplegador

Firma documenta

Error de discrimina

Fuente

Hijo

típica

l

ción

Anter os

S muy bajo [0.03, 0.20]. El diseñador sabía que la métrica producía disparate impact o que el sistema generaría daño en el dominio de despliegue, y deliberadame nte no modificó el diseño porque los costos de la reforma (menor rendimiento del sistema, mayor costo computacion al, menor precisión en el caso de uso principal) superaban — en su evaluación— los costos del daño. Es el patrón de los sistemas de IA que mantuvieron métricas con disparate impact documentad o

Comunicaci ones internas donde se documentó el disparate impact antes del despliegue sin que eso produjera cambio del diseño. Resultados de pruebas A/B que mostraban el efecto dañino en grupos específicos sin que se detuviera el despliegue. Actas de comités de ética que señalaron el riesgo sin que el equipo de producto implementar a las salvaguardas recomendad as. Decisiones documentad as de escalar el sistema sin las medidas de

Discovery de litigios. Whistleblow ers con documentaci ón. Investigacio nes parlamentari as o regulatorias. Reportes filtrados de equipos de confianza y seguridad.

Confundir con Potós cuando el diseñador siguió los estándares del campo sin evidencia interna que mostrara el impacto sobre los grupos específicos perjudicado s.

Taxonomía General de Aplicaciones

Qué informa para S del diseñador o desplegador

Firma documenta

Error de discrimina

Fuente

Hijo

típica

l

ción

internamente durante múltiples ciclos de revisión sin acción correctora.

mitigación que los propios ingenieros habían recomendad o.

Potós S moderado-alto [0.40, 0.70]. El diseñador siguió los estándares de diseño de sistemas de IA del período —las métricas estándar del campo, los datasets de entrenamient o habituales, las prácticas de evaluación convencional es— sin implementar auditorías de equidad disponibles, pero no generalizadas en el período. El disparate impact era una consecuencia de las prácticas estándar del sector, no de

Métricas objetivo coherentes con las que otros sistemas del campo usaban en el período. Ausencia de evidencia interna del disparate impact sobre los grupos específicos perjudicado s. Participació n en benchmarks estándar del campo que no incluían métricas de equidad como criterio de evaluación. Prácticas de evaluación consistentes con las publicadas

Comparació n con las prácticas estándar del campo en el período. Publicacione s de las conferencias de referencia (NeurIPS, ICML, FAccT) sobre las métricas de equidad adoptadas. Estándares sectoriales de auditoría del período.

Confundir con Anteros cuando el diseñador disponía de evidencia interna del impacto que no fue incorporada al diseño por razones no relacionadas con la capacidad técnica de detectarlo.

Taxonomía General de Aplicaciones

Qué informa para S del diseñador o desplegador

Firma documenta

Error de discrimina

Fuente

Hijo

típica

l

ción

una decisión idiosincrática del diseñador.

en las conferencias de referencia del campo.

Deim os

S alto [0.56, 0.84]. El desplegador o el regulador se paralizó ante la complejidad de la auditoría de los sistemas de IA —la opacidad de los modelos de aprendizaje profundo, la dificultad de definir operativamen te la equidad, la incertidumbr e sobre qué métricas de fairness aplicar— sin consultar con expertos ni derivar la decisión a quienes tenían los conocimient os técnicos. El expediente del Deimos en IA:

Documenta ción de la incertidumb re sobre cómo auditar el sistema sin que esa incertidumb re produzca consulta a expertos ni pausa del despliegue. Solicitudes de financiamie nto para auditoría no atendidas. Comunicaci ones que identifican el problema sin agenda de resolución. Regulacione s pendientes sin implementa ción en el período del despliegue.

Corresponde ncia interna del equipo de producto. Actas de comités de revisión. Comunicaci ones con el regulador sobre los estándares de auditoría.

Confundir con la incertidumb re genuina sobre qué métrica de equidad es la correcta — que es un problema técnico-filosófico real. La diferencia: Deimos produce el expediente vacío ante la incertidumb re; la gestión adecuada produce consulta experta documentad a y decisión justificada aunque no perfecta.

Taxonomía General de Aplicaciones

Qué informa para S del diseñador o desplegador

Firma documenta

Error de discrimina

Fuente

Hijo

típica

l

ción

documentos que identifican la necesidad de auditoría sin que esa identificación produzca acción o plan.

§3.2  Hijos de legibilidad baja y nota Harmonía

Fobos: el desplegador que implementó salvaguardas excesivas —auditorías continuas, listas blancas restrictivas, umbrales de confianza conservadores— motivado por el miedo a la responsabilidad legal más que por el análisis del impacto real del sistema. El Fobos en IA produce el sistema que rechaza todas las solicitudes ambiguas para no cometer errores, transfiriendo el daño a los usuarios falsamente rechazados. S moderado [0.32, 0.58]. Distinguible de Harmonía porque la Harmonía equilibra el rendimiento del sistema con la equidad; el Fobos sacrifica el rendimiento para minimizar la responsabilidad visible.

Eros en el desplegador: el desplegador que adoptó el sistema de IA más avanzado disponible —mayor precisión media, mayor velocidad, mayor escala— sin evaluar si ese avance técnico producía mayor equidad distributiva. El Eros en IA produce el sistema de última generación con el disparate impact de la última generación. S moderado-alto [0.45, 0.72] cuando el sistema adoptado era el de referencia del campo en el período.

Taxonomía General de Aplicaciones

§3.3  Nota Harmonía — el equipo que auditó la métrica y documentó las alternativas

El equipo que: (a) definió la métrica objetivo con análisis explícito de las alternativas disponibles y sus consecuencias distribucionales; (b) realizó la auditoría de equidad del sistema antes del despliegue con instrumentos validados; (c) documentó el disparate impact residual y las razones por las que no fue técnicamente eliminable; (d) implementó las salvaguardas de monitoreo continuo del comportamiento del sistema en producción; y (e) estableció un mecanismo de reclamación accesible para los afectados tiene α ≈ 1.00 para su arista en el grafo — aunque el sistema produzca daño residual que no era técnicamente eliminable con el estado del arte disponible.

La Harmonía del equipo técnico no elimina el R* del directivo que aprobó el despliegue sin implementar las salvaguardas recomendadas internamente: son nodos distintos con R* distintos.

### §4  Escala de α con la tabla de acciones que cuentan

La descomposición del disparate impact: DI_total = DI_métrica + DI_dataset + DI_modelo El disparate impact total de un sistema algorítmico puede descomponerse en tres componentes causales con R* distintos: DI_métrica: el disparate impact producido por la elección de la variable objetivo. Si la métrica fuera reemplazada por la alternativa óptima con menor impacto, este componente desaparecería. R*_diseñador_métrica = DI_métrica / DI_total. DI_dataset: el disparate impact producido por el sesgo histórico en el dataset de entrenamiento, dado la métrica. Si el dataset fuera auditado y rebalanceado, este componente reduciría. R*_curador_dataset = DI_dataset / DI_total. DI_modelo: el disparate impact adicional producido por la arquitectura y el proceso de entrenamiento del modelo, dado la métrica y el dataset. S_modelo ≈ 1.0, por lo que R*_neta_modelo ≈ 0. Cambiar el modelo sin cambiar la métrica ni el dataset tiene impacto mínimo.

Taxonomía General de Aplicaciones

R*_diseñador_métrica = (DI_métrica_actual −

DI_métrica_alternativa) / DI_total Si DI_métrica_alternativa << DI_métrica_actual → la elección de

métrica es la condición necesaria idiosincrática del daño.

Nivel de α

α en el dominio algorítmico

Conducta que

típico en desempeño

Nodo

sube α

deficiente

Diseñador de la métrica (DM)

Análisis de las alternativas de métrica con sus consecuencias distribucionales documentado; elección de la métrica con menor disparate impact técnicamente compatible con el objetivo del sistema; documentación de por qué la alternativa de menor impacto no fue adoptada cuando no lo fue.

Análisis formal de las alternativas de métrica con estimación del disparate impact de cada alternativa antes de la decisión. Elección documentada de la métrica con menor disparate impact entre las técnicamente viables. Comunicación transparente de los límites del sistema y del disparate impact residual a los desplegadores y los afectados.

0.05–0.20 para diseñadores con Anteros documentado: conocían el disparate impact y eligieron la métrica de mayor impacto. 0.25–0.50 para diseñadores con Potós: siguieron el estándar del campo sin auditoría de equidad de la métrica.

Curador del dataset (CD)

Auditoría del sesgo histórico del dataset antes de su uso para entrenamiento; implementación de técnicas de debiasing o rebalanceo

Análisis de representación de grupos protegidos en el dataset. Técnicas de debiasing aplicadas con documentación

0.10–0.30 para curadores que usaron datasets con sesgo conocido sin auditoría ni debiasing. 0.05– 0.15 cuando el curador conocía

Taxonomía General de Aplicaciones

Nivel de α

α en el dominio algorítmico

Conducta que

típico en desempeño

Nodo

sube α

deficiente

cuando el sesgo era técnicamente corregible; documentación del sesgo residual y su impacto esperado sobre el sistema.

del efecto sobre el disparate impact. Documentación del sesgo residual comunicada al equipo de entrenamiento del modelo. Actualización periódica del dataset con monitoreo de la distribución.

el sesgo específico del dataset relevante para el caso de uso y no lo comunicó.

Desplegador (DE)

Auditoría del sistema en el entorno de despliegue específico antes del lanzamiento a escala; implementación del monitoreo continuo del disparate impact en producción; establecimiento de mecanismo de reclamación accesible; definición de umbrales de alerta con plan de acción para cuando el disparate impact supere el umbral.

Auditoría de equidad del sistema en el dominio de despliegue antes del lanzamiento. Monitoreo continuo del disparate impact en producción con umbrales de acción predefinidos. Mecanismo de reclamación accesible y con resolución en plazo definido. Suspensión del sistema cuando el disparate impact supera los umbrales establecidos.

0.05–0.20 para desplegadores que lanzaron a escala sin auditoría de equidad en el dominio específico. 0.10– 0.30 para desplegadores que monitorearon el sistema pero no activaron el mecanismo de acción ante señales de disparate impact.

Taxonomía General de Aplicaciones

Nivel de α

α en el dominio algorítmico

Conducta que

típico en desempeño

Nodo

sube α

deficiente

Regulador (RG)

Establece los estándares de auditoría algorítmica requeridos antes del despliegue en aplicaciones de alto impacto; define los umbrales de disparate impact aceptables para cada dominio de aplicación; realiza o exige la auditoría independiente de los sistemas con mayor R* potencial sobre la población.

Estándares de auditoría algorítmica publicados con metodología y umbrales por dominio de aplicación. Requisito de auditoría independiente antes del despliegue en aplicaciones de alto impacto (justicia penal, crédito, empleo, diagnóstico médico). Mecanismo de supervisión post-despliegue con acceso a los datos del sistema en producción.

0.05–0.20 para reguladores que no establecieron estándares de auditoría en el período del daño cuando la evidencia del riesgo ya estaba disponible. 0.10–0.25 para reguladores con estándares insuficientes en el dominio de aplicación del sistema analizado.

### Los seis niveles de α y el patrón de inversión causal en IA

Nivel de

α Descripción del actor en el dominio algorítmico

α = 0.00– 0.15 (Δ máximo)

Diseñador con Anteros documentado: sabía que la métrica producía disparate impact sobre grupos específicos —había pruebas internas— y deliberadamente no modificó el diseño. O desplegador que conocía el disparate impact del sistema y lo escaló sin salvaguardas porque el costo del retraso superaba —en su evaluación— el costo del daño.

Taxonomía General de Aplicaciones

Nivel de

α Descripción del actor en el dominio algorítmico

α = 0.16– 0.35 Diseñador que usó una métrica con disparate impact documentado en la literatura del campo sin realizar auditoría de la alternativa de menor impacto. Desplegador que lanzó a escala sin auditoría del sistema en el dominio de despliegue específico. Curador que usó dataset con sesgo conocido sin debiasing ni documentación del sesgo residual.

α = 0.36– 0.55 Diseñador que realizó auditoría del modelo, pero no de la métrica. Desplegador que implementó monitoreo del rendimiento del sistema, pero no de su disparate impact. Regulador que publicó guías no vinculantes de buenas prácticas sin estándares de auditoría exigibles.

α = 0.56– 0.74 Diseñador que documentó las alternativas de métrica y eligió con justificación la de menor impacto técnicamente compatible. Desplegador con monitoreo del disparate impact en producción, pero sin umbrales de acción predefinidos. Regulador con estándares de auditoría obligatorios para algunos dominios de alto impacto.

α = 0.75– 0.90 Diseñador que realizó análisis formal de alternativas, eligió con documentación la de menor impacto, comunicó el disparate impact residual al desplegador. Desplegador con auditoría, monitoreo con umbrales de acción y mecanismo de reclamación funcional. Regulador con estándares de auditoría exigibles y supervisión post-despliegue.

α = 0.91– 1.00 (Δ ≈ 0)

Equipo que implementó el proceso completo: auditoría de métrica con análisis de alternativas, auditoría de dataset con debiasing documentado, auditoría del sistema en el dominio de despliegue, monitoreo continuo con umbrales predefinidos, mecanismo de reclamación, y documentación transparente del disparate impact residual comunicada a los afectados.

La paradoja de la auditoría del modelo: por qué atacar el componente equivocado es ineficaz

El litigio y la regulación de IA tienden a enfocarse en la explicabilidad y la auditabilidad del modelo — en los pesos, las características de entrada, las reglas de decisión. Eso es atacar el nodo de menor R*_neta.

Taxonomía General de Aplicaciones

El teorema de Chouldechova (2016) establece que las definiciones de equidad matemáticamente más intuitivas son incompatibles entre sí cuando las tasas base de la métrica difieren entre grupos — lo que ocurre precisamente cuando la métrica está sesgada históricamente. El sistema COMPAS no podía simultáneamente satisfacer la equidad de calibración (igual precisión entre grupos) y la equidad de paridad (igual tasa de error entre grupos) porque las tasas de reincidencia diferían entre grupos — y las tasas diferían porque la métrica target ('nuevo arresto') era función de las tasas de arresto diferencial de la policía, que son en sí mismas sesgadas. La solución no era cambiar el modelo: era cambiar la métrica de 'nuevo arresto' a 'nueva condena con pruebas suficientes'.

### §5  Tipos de nodo, tipos de arista y configuraciones canónicas del dominio

### Tipos de nodo en el grafo algorítmico

Tipo de

Función en

el grafo S típico R* en el grafo de daño algorítmico

nodo

Diseñador de la métrica (DM)

Tomó la decisión normativa de qué optimiza el sistema. Es la decisión de mayor consecuencia en el grafo. R* positivo cuando la elección de la métrica era la condición necesaria del disparate impact y había alternativas disponibles con menor impacto.

S bajo [0.05– 0.30] cuando la métrica era idiosincrática del diseñador. S alto [0.50– 0.78] cuando la métrica era el estándar del campo.

R*_DM × D_total × (1 − α_DM). El más alto del grafo cuando hay alternativas de métrica con menor disparate impact documentadas en el período.

Taxonomía General de Aplicaciones

Tipo de

Función en

el grafo S típico R* en el grafo de daño algorítmico

nodo

Curador del dataset (CD)

Seleccionó y preparó los datos de entrenamiento del modelo. R* positivo cuando el sesgo del dataset era conocido o detectable y no fue corregido. El dataset es un nodo técnico sin voluntad — su R* apunta hacia los actores que lo generaron históricamente y hacia quienes lo usaron sin auditoría.

S alto [0.55– 0.85] en la mayoría de los casos: el sesgo histórico del dataset es compartido por todos los que usaron datos de ese período.

R*_CD × D_total. La fracción del disparate impact atribuible al sesgo del dataset (DI_dataset / DI_total).

Modelo (ML)

Optimizó la métrica dada sobre el dataset dado. Nodo técnico sin voluntad propia. S ≈ 1.0 porque es fungible: cualquier modelo competente con la misma métrica y dataset habría producido el mismo resultado.

S ≈ 1.0 en todos los casos. Es el principio algorítmico central del dominio.

R*_neta_ML = R*_ML × (1 − S_ML) ≈ 0. Cambiar el modelo sin cambiar la métrica ni el dataset tiene impacto mínimo sobre el disparate impact.

Taxonomía General de Aplicaciones

Tipo de

Función en

el grafo S típico R* en el grafo de daño algorítmico

nodo

Desplegador (DE)

Tomó la decisión de implementar el sistema en el entorno específico donde produjo el daño. R* positivo cuando la auditoría del sistema en ese entorno habría revelado el disparate impact o cuando el monitoreo en producción no fue adecuado.

Variable: S bajo [0.10– 0.35] si el despliegue era idiosincrático en ese dominio. S alto [0.55– 0.80] si el despliegue era el estándar de la industria.

R*_DE × D_total × (1 − α_DE). Incluye el R* por el daño producido durante el período entre el despliegue y la corrección cuando el disparate impact era detectable.

Regulador (RG)

Estableció — o no estableció— los estándares de auditoría y las condiciones de despliegue en aplicaciones de alto impacto. R* positivo por omisión cuando los estándares eran insuficientes dado el estado del conocimiento sobre los

Alto [0.55– 0.82] cuando la ausencia de estándares era el paradigma regulatorio del período. Moderado [0.35–0.55] cuando la evidencia de los riesgos del sistema era ya suficiente para justificar la acción.

Fracción del daño total atribuible al exceso de disparate impact sobre el umbral que la regulación adecuada habría establecido.

Taxonomía General de Aplicaciones

Tipo de

Función en

el grafo S típico R* en el grafo de daño algorítmico

nodo

riesgos del sistema.

### Configuraciones canónicas del dominio

Configuración 1 — Sistema algorítmico de decisión de alto impacto con disparate impact racial

Caso tipo COMPAS/Amazon. DM (diseñador de la métrica 'reincidencia como nuevo arresto' o 'candidato exitoso como similar al historial': S moderado-bajo [0.15–0.35], la métrica era una elección entre alternativas documentadas) + CD (dataset de arrestos sesgados por políticas de vigilancia diferencial: S alto, el sesgo era sistémico del período) + ML (modelo que aprendió el patrón: S ≈ 1.0, R*_neta ≈ 0) + DE (desplegador sin auditoría de equidad independiente antes del despliegue a escala: α bajo) + RG (regulador sin estándares de auditoría exigibles en el período) DI_total = DI_métrica (≈40%) + DI_dataset (≈50%) + DI_modelo (≈10%). R*_DM × (1−S_DM) >> R*_ML × (1−S_ML) ≈ 0. D_total_algorítmico = N_afectados × D_promedio_individual + D_sistémico_adicional. El litigio que ataca la explicabilidad del modelo está atacando el nodo de menor R*_neta. El litigio que establece que la métrica alternativa ('nueva condena' en lugar de 'nuevo arresto') habría reducido el DI en más del 30% está atacando el nodo de mayor R*_neta con S moderado-bajo.

Configuración 2 — Sistema autónomo con daño físico (vehículo autónomo)

DM_reglas (diseñador de las reglas de decisión del sistema ante dilemas éticos —priorización del pasajero versus el peatón en colisiones inevitables: S bajo, la jerarquía de valores era una elección entre alternativas filosóficamente debatidas) + DE_fabricante (fabricante que desplegó el sistema con esas reglas sin validación con los estándares éticos de la jurisdicción) + Taxonomía General de Aplicaciones

DE_operador (empresa o individuo que operó el vehículo en el entorno específico del accidente) + RG (regulador que no estableció estándares de certificación de las reglas de decisión éticas antes de la autorización de operación) El daño por distribución fuera del rango de entrenamiento (distribution shift): cuando el sistema autónomo falla en una situación que no estaba representada en el dataset de entrenamiento, el R* del diseñador del proceso de validación y del curador del dataset de entrenamiento supera al del modelo. La auditoría de la cobertura del dataset de entrenamiento respecto al dominio de despliegue es el instrumento central.

Configuración 3 — Modelo de lenguaje grande (LLM) con daño a terceros

DM_base (desarrollador del modelo base con la métrica de entrenamiento que determina el comportamiento por defecto: S moderado, la elección del corpus y del proceso de alineamiento tiene alternativas documentadas) + DE_fine-tuner (empresa o individuo que ajustó el modelo base para el caso de uso sin restricciones de contenido adecuadas para ese dominio) + DE_aplicación (operador de la aplicación que dio acceso al modelo sin filtros adecuados para el contexto de uso) + Usuario (actor que usó el modelo para producir el daño: S variable según si el sistema tenía restricciones que impidieran el uso dañino) La cadena de responsabilidad en LLMs es más larga que en los sistemas de decisión: el desarrollador del modelo base, el ajustador fino, el operador de la aplicación y el usuario tienen R* sobre el daño en proporciones que dependen de las restricciones que cada nodo de la cadena implementó. El principio algorítmico se aplica: el modelo tiene S alto entre modelos equivalentes, pero la elección del proceso de alineamiento (RLHF, los valores que se reforzaron) tiene S bajo.

### §6  Preguntas que responde este capítulo

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

¿Cuál es el nodo de mayor R*_neta en el grafo algorítmico — el modelo, la métrica, o el dataset?

Auditoría de la métrica (IA2): ¿hay alternativas de métrica con menor disparate impact que eran técnicamente disponibles en el período? Si DI_métrica_alternativa << DI_métrica_actual, el R*_DM es el dominante. Cálculo de S_modelo: si cualquier modelo competente con la misma métrica y dataset habría producido el mismo resultado, R*_neta_ML ≈ 0.

Declaración B con auditoría de la métrica IA2 que establezca las alternativas disponibles. Declaración A si hay documentos internos que muestren el análisis de alternativas (IA1). Declaración C si la auditoría de la métrica debe realizarse retroactivamente sobre el sistema ya desplegado.

¿El diseñador sabía que la métrica producía disparate impact — cuál es su Hijo dominante?

Cronología del conocimiento del disparate impact: ¿había publicaciones del campo que documentaban el problema de la métrica antes del despliegue? ¿Hay documentos internos de pruebas que mostraban el impacto diferencial? ¿Otros sistemas del campo habían adoptado métricas alternativas?

Declaración A con documentos internos IA1 que muestren el conocimiento del disparate impact. Declaración B con cronología de publicaciones del campo sobre el problema de la métrica. Declaración C si el estado del conocimiento debe inferirse solo desde la literatura pública del período.

¿Cuál es la descomposición del disparate impact — DI_métrica + DI_dataset + DI_modelo?

Auditoría IA2 con análisis contrafáctico: ¿cuál habría sido el DI con la métrica alternativa óptima, dado el mismo dataset? ¿Cuál habría sido el DI con el dataset debiased, dada la misma métrica? La diferencia entre el DI observado y el DI contrafáctico establece la

Declaración B con auditoría IA2 que tenga acceso al sistema o a un sistema equivalente con la métrica alternativa. Declaración C cuando la descomposición debe estimarse desde el análisis teórico del

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

fracción atribuible a cada componente.

sesgo sin acceso al sistema.

¿El daño del sistema autónomo fue por distribution shift — el sistema falló fuera del rango de entrenamiento?

Análisis de la cobertura del dataset de entrenamiento respecto al dominio de despliegue: ¿estaba la situación del accidente o el fallo representada en el dataset de entrenamiento? Si no estaba representada, el R* del diseñador del proceso de validación supera al del modelo específico que falló.

Declaración B con auditoría del dataset de entrenamiento y análisis del evento de fallo respecto a la distribución del training data. Declaración A si hay documentación del proceso de validación que muestra las situaciones excluidas del testing.

¿Cuál es el D_total del daño algorítmico — individual y sistémico?

D_total_algorítmico = N_afectados × D_promedio_individual + D_sistémico_adicional. Para daños individuales: los mismos instrumentos que en los caps. correspondientes al dominio (cap. 1 para daño en justicia penal, cap. 25 para daño laboral, cap. 27 para daño sanitario). El D_sistémico adicional captura el efecto de escala del sistema sobre la población afectada.

Declaración B para el D_individual con los instrumentos del dominio de aplicación. Declaración C para el D_sistémico cuando el número de afectados y el D_promedio deben estimarse con supuestos de alto impacto sobre el resultado.

### §7  Traducción de D_total al dominio algorítmico

D_total_algorítmico = N_afectados × D_promedio_individual + D_sistémico_adicional

Taxonomía General de Aplicaciones

El daño algorítmico tiene una característica singular respecto a todos los demás capítulos del libro: opera simultáneamente a escala individual y a escala poblacional. El sistema de IA toma decisiones sobre cada individuo afectado (D_individual: la persona que no obtuvo el crédito por el score sesgado, la persona que recibió una evaluación de riesgo más alta por el sistema penal sesgado) y sobre el conjunto de los afectados (D_sistémico: el efecto acumulado del disparate impact sobre la distribución de oportunidades, la cronificación de la desigualdad estructural, el daño a la confianza en las instituciones). El D_sistémico puede superar al D_individual agregado cuando el sesgo afecta a grupos ya estructuralmente desfavorecidos.

En el dominio algorítmic

Compone

Cómo se cuantifica Fuente de

nte

evidencia

o

D_individu al × N_afectad os (daño directo por decisión incorrecta)

El daño de cada individuo afectado por la decisión incorrecta del sistema: la persona clasificada incorrectam ente en el sistema penal (D_vital por los meses de privación de libertad adicional), la persona excluida del empleo (D_vital por la pérdida de ingresos y trayectoria laboral), la persona excluida del crédito (D_vital por

D_promedio_individu al × N_afectados = Σ D_i para todos los individuos afectados. Para sistemas penales: AVAD_privación_de_ libertad + ΔT_trayectoria_post-encarcelamiento. Para sistemas de empleo: diferencial de ingresos acumulados. Para sistemas de crédito: diferencial de acceso al capital y acumulación de patrimonio.

Registros del sistema con las decisiones individuales. Datos de seguimiento de los afectados (registros de empleo, ingresos, antecedentes) . Análisis de los counterfactua ls individuales con el sistema sin el disparate impact.

Taxonomía General de Aplicaciones

En el dominio algorítmic

Compone

Cómo se cuantifica Fuente de

nte

evidencia

o

el acceso al capital y la acumulació n de patrimonio). Se calcula con los instrumento s del cap. del dominio de aplicación específico.

D_sistémic o (daño a la distribució n de oportunida des y cronificaci ón de la desigualda d)

El daño que supera a la suma de los daños individuales: el efecto del disparate impact sobre la distribución de oportunidad es en la población afectada, la señal sistémica que envía a grupos sobre qué es posible para ellos, el daño a la confianza en las institucione s que usan el sistema, la cronificació n de la desigualdad

D_sistémico requiere modelización con supuestos sobre el efecto multiplicador del sesgo algorítmico sobre la desigualdad estructural preexistente. El análisis del índice de Gini de la distribución de oportunidades antes y después del despliegue del sistema es el indicador más directamente medible.

Datos macroeconó micos de distribución de ingresos, acceso al crédito, tasas de empleo y encarcelamie nto por grupo antes y después del despliegue del sistema. Encuestas de confianza institucional. Análisis de la persistencia intergeneraci onal de la desventaja en los grupos afectados.

Taxonomía General de Aplicaciones

En el dominio algorítmic

Compone

Cómo se cuantifica Fuente de

nte

evidencia

o

estructural que el sistema reprodujo a escala y velocidad algorítmica.

ΔT_trayect oria (desvío de la trayectoria vital de los afectados por el disparate impact crónico)

El desvío de la trayectoria de vida de los individuos afectados por el acceso diferencial a oportunidad es que el sistema produjo: la reducción de la expectativa de ingresos de vida, la reducción del potencial educativo de los hijos de los afectados, el daño a la red de relaciones por la exclusión de institucione s donde el sistema tomaba decisiones

D_ΔT = diferencial de trayectoria vital entre la población afectada y la contrafáctica sin el disparate impact del sistema, multiplicado por el número de afectados. Requiere análisis longitudinal de los afectados versus grupo de control.

Estudios longitudinales de los afectados por sistemas con disparate impact documentado . Datos de movilidad intergeneraci onal en los grupos afectados. Análisis de la transmisión intergeneraci onal de la desventaja producida por el sistema.

Taxonomía General de Aplicaciones

En el dominio algorítmic

Compone

Cómo se cuantifica Fuente de

nte

evidencia

o

con disparate impact.

### §8  Límites del método y errores frecuentes de aplicación

Límites del método en el dominio algorítmico

Límite 1 — La imposibilidad de la equidad perfecta cuando las tasas base difieren entre grupos. El teorema de Chouldechova establece que las definiciones de equidad matemáticamente más intuitivas son incompatibles entre sí cuando las tasas base de la métrica difieren entre grupos. El análisis de responsabilidad no puede requerir que el sistema satisfaga simultáneamente todas las definiciones de equidad — debe establecer cuál definición era la más relevante para el dominio de aplicación y si el sistema la satisfacía.

Límite 2 — El problema del sesgo emergente: cuando el sistema aprende más que la métrica. Algunos sistemas de IA desarrollan patrones de comportamiento que no estaban codificados en la métrica ni en el dataset, pero emergen de su interacción. El sesgo emergente es más difícil de atribuir a una decisión normativa específica porque no fue intencional ni predictible desde ningún punto del diseño.

Límite 3 — La opacidad de los modelos de aprendizaje profundo. Los modelos de redes neuronales profundas son difíciles de auditar porque la relación entre las entradas y las salidas no es transparente. Esa opacidad no reduce el R* del diseñador de la métrica — el diseñador de la métrica tiene R* por haber elegido un objetivo que produce disparate impact independientemente de que el modelo sea o no explicable.

Taxonomía General de Aplicaciones

### Pero la opacidad sí reduce la certeza con que el análisis puede atribuir el daño a componentes específicos del sistema.

Límite 4 — La causalidad en sistemas de recomendación: el problema del counterfactual. Los sistemas de recomendación producen daños difusos y acumulativos donde establecer qué habría ocurrido sin el sistema tiene alta incertidumbre. La relación entre el algoritmo de recomendación de contenido y la radicalización de un usuario específico no puede establecerse con el mismo nivel de certeza que la relación entre el sistema de scoring crediticio y la denegación de un crédito específico.

### Errores frecuentes de aplicación

Error Por qué

ocurre Consecuencia Corrección

Atacar la explicabilidad del modelo en lugar de la auditoría de la métrica

La explicabilidad del modelo (SHAP, LIME, árboles de decisión interpretativos ) es técnicamente más accesible que la auditoría de la métrica objetivo. El litigio se enfoca en lo que se puede medir fácilmente.

Se ataca el nodo de menor R*_neta del grafo. La explicabilidad del modelo muestra cómo el sistema tomó una decisión, no si la métrica que optimizaba era la correcta. La estrategia de litigio es ineficaz para el nodo de mayor responsabilida d.

La auditoría que establece el R* debe comenzar por la métrica: ¿cuál era la variable objetivo? ¿Cuáles eran las alternativas disponibles? ¿Cuánto del disparate impact habría reducido la métrica alternativa? La explicabilidad del modelo es complementaria, no central.

Confundir el disparate impact del sistema con la intención discriminatori

El disparate impact observable en los outputs del sistema se usa para inferir la intención discriminatori

Anteros atribuido a actores con Potós o Deimos. El diseñador que siguió los estándares del

La descomposición DI_total = DI_métrica + DI_dataset + DI_modelo permite separar la fracción del DI

Taxonomía General de Aplicaciones

Error Por qué

ocurre Consecuencia Corrección

a del diseñador

a del diseñador, sin distinguir entre el DI producido por la métrica (decisión normativa), por el dataset (sesgo histórico sistémico) y por el modelo (residual).

campo del período tiene S moderado-alto y no tiene responsabilida d por la fracción del DI atribuible al sesgo histórico del dataset.

atribuible a cada nodo antes de analizar el Hijo dominante del diseñador.

Atribuir el R* del modelo al equipo técnico que lo construyó

El equipo técnico es el actor más visible en la cadena de desarrollo del sistema. El análisis se enfoca en lo que el equipo técnico hizo en lugar de en la decisión normativa del diseñador de la métrica.

R* incorrecto: el equipo técnico tiene S ≈ 1.0 porque cualquier equipo competente habría producido el mismo sistema con la misma métrica y dataset. El R*_neta del equipo técnico es próximo a 0. El R* migra al diseñador de la métrica.

El equipo técnico solo tiene R* positivo cuando su implementación se desvió de lo que el diseñador de la métrica y el curador del dataset especificaron — cuando el DI del modelo supera significativament e al DI esperado dado la métrica y el dataset.

No calcular el D_sistémico del daño algorítmico

El análisis calcula solo el daño individual de las decisiones incorrectas específicas del sistema sin capturar el efecto de escala del

D_total algorítmico subestimado. En sistemas que operaron durante años sobre millones de individuos, el D_sistémico puede superar al D_individual

El D_total debe incluir el componente sistémico: el efecto del disparate impact sobre la distribución de oportunidades en la población afectada, la

Taxonomía General de Aplicaciones

Error Por qué

ocurre Consecuencia Corrección

disparate impact sobre la distribución de oportunidades .

agregado. La pretensión no refleja la magnitud real del daño.

cronificación de la desigualdad estructural, y el daño a la confianza institucional.

### §9  Guía de prioridades de recolección de evidencia

La primera decisión es establecer cuál es el tipo de sistema: sistema de decisión de alto impacto (empleo, crédito, justicia penal, salud), sistema de recomendación, sistema autónomo con capacidad de daño físico, o LLM. Cada uno tiene un instrumento causal central diferente y una jerarquía de nodos con R* distinta.

### Tabla de prioridades de recolección de evidencia en IA y sistemas automatizados

La evidenci

Si tu incertidu

Qué rango reduce

Qué buscar /

a que más la reduce

Por qué funciona

mbre principal

qué preguntar

es...

es...

### 1. ¿Cuál es el tipo de sistema y su nodo de mayor R*?

Establece r la arquitect ura del sistema: ¿qué métrica optimiza? ¿Con qué dataset fue entrenad

El tipo de sistema determina el instrumento central y el nodo de mayor R*. La auditoría de la métrica es siempre la prioridad 1.

Determi na la estrategi a de auditoría e instrume nto causal (incertid umbre

¿Cuál es la variable objetivo que optimiza el sistema? ¿Con qué datos fue entrenado? ¿Quién definió la métrica objetivo? ¿Cuándo fue desplegado y

Taxonomía General de Aplicaciones

La evidenci

Si tu incertidu

Qué rango reduce

Qué buscar /

a que más la reduce

Por qué funciona

mbre principal

qué preguntar

es...

es...

o? ¿Quién tomó las decisione s normativ as clave?

estructur al).

en qué dominio?

### 2. ¿Cuáles eran las alternativa s de métrica — cuál es el R* del DM?

Auditoría IA2 de la métrica con análisis del DI_métri ca: ¿cuánto habría reducido el disparate impact la métrica alternativ a óptima? Docume ntos internos IA1 que muestren el análisis de alternativ as.

El R*_DM es función de si alternativas con menor DI eran técnicamente disponibles. Si DI_métrica_a lternativa ≈ 0 y DI_métrica_a ctual >> 0, el diseñador tiene R* pleno sobre ese componente.

Establec e el R*_DM y su S (incertid umbre ontológi ca del nodo diseñado r).

¿Había otras métricas usadas en sistemas similares del campo con menor disparate impact? ¿El equipo interno evaluó alternativas? ¿Las publicaciones del campo del período señalaban el problema de la métrica usada?

### 3. ¿Cuál es el disparate impact document ado — cuál es el

Análisis de los outputs del sistema (IA4) + auditoría

Sin el DI_total y su descomposici ón, el análisis de R* no tiene base empírica. El DI_total

Establec e el D_total y la distribuc ión de R* entre

¿Cuáles son las tasas de error del sistema entre grupos? ¿Hay datos de los outputs del sistema sobre

Taxonomía General de Aplicaciones

La evidenci

Si tu incertidu

Qué rango reduce

Qué buscar /

a que más la reduce

Por qué funciona

mbre principal

qué preguntar

es...

es...

DI_total y su descompo sición?

IA2 con análisis contrafác tico de la métrica y el dataset.

establece la escala del daño y la descomposici ón distribuye el R*.

DM, CD y ML (incertid umbre empírica central).

la población afectada? ¿Se puede reconstruir el DI con la métrica alternativa?

### 4. ¿El diseñador sabía del disparate impact — cuál es el Hijo dominant e?

Docume ntos internos IA1 del período + cronologí a de publicaci ones del campo sobre el problema de la métrica usada + compara ción con la adopción de métricas alternativ as en sistemas del campo.

El Hijo dominante determina el S del DM. Anteros → S bajo [0.03– 0.20]; Potós → S moderado-alto [0.40– 0.70]; Deimos → S alto [0.56–0.84].

Establec e el S del DM y la fracción idiosincr ática del R* (incertid umbre ontológi ca).

¿Hay documentos internos de pruebas que muestren el disparate impact antes del despliegue? ¿Las publicaciones del campo ya documentaba n el problema? ¿Otros sistemas comparables habían adoptado la métrica alternativa?

### 5. ¿El desplegad or realizó auditoría antes del

Registros del proceso de validació n antes

El R*_DE depende de si el disparate impact era detectable en el dominio

Establec e el R*_DE y el α_DE (incertid

¿Realizó el desplegador auditoría de equidad del sistema en el dominio de

Taxonomía General de Aplicaciones

La evidenci

Si tu incertidu

Qué rango reduce

Qué buscar /

a que más la reduce

Por qué funciona

mbre principal

qué preguntar

es...

es...

despliegue ?

del lanzamie nto + auditoría s de equidad realizadas + mecanis mos de monitore o impleme ntados.

específico de despliegue antes del lanzamiento a escala.

umbre del nodo desplega dor).

despliegue antes del lanzamiento? ¿Había monitoreo del disparate impact en producción? ¿Existía mecanismo de reclamación?

### 6. ¿Cuál es el D_total — individual y sistémico?

D_indivi dual: instrume ntos del cap. del dominio de aplicació n (cap. 1 para justicia penal, cap. 25 para empleo, etc.). D_sistém ico: datos de distribuci ón de oportuni dades antes y después del

Sin el D_total, el AD de cada nodo no tiene base cuantificada.

Establec e la escala de la pretensi ón (incertid umbre empírica del daño).

¿Cuántos individuos fueron afectados por el disparate impact del sistema? ¿Cuál es el D_promedio_ individual dado el tipo de decisión? ¿Qué efecto tuvo el sistema sobre la distribución de oportunidades en la población afectada?

Taxonomía General de Aplicaciones

La evidenci

Si tu incertidu

Qué rango reduce

Qué buscar /

a que más la reduce

Por qué funciona

mbre principal

qué preguntar

es...

es...

despliegu e.

### Árbol de decisión en IA y sistemas automatizados: tres pasos

¿Cuál es el tipo de sistema y su nodo de mayor R* probable? │

├─ ANÁLISIS A: SISTEMA DE DECISIÓN DE ALTO IMPACTO (empleo, crédito, justicia, salud)

│  └─  PRIORIDAD 1: Auditoría de la métrica objetivo → ¿cuáles eran las alternativas disponibles?

│         · DI_métrica_alternativa << DI_métrica_actual → R*_DM dominante con S bajo. │         · S_modelo ≈ 1.0 → cambiar el modelo sin cambiar la métrica no resuelve el problema. │  └─  PRIORIDAD 2: Descomposición DI_total = DI_métrica + DI_dataset + DI_modelo

│         · Establece la distribución del R* entre DM, CD y ML (neto ≈ 0 para ML). │  └─  PRIORIDAD 3: Hijo dominante del DM → Anteros / Potós / Deimos

│         · Anteros → S_DM bajo [0.03–0.20]. R* pleno sobre DI_métrica. │  └─  PRIORIDAD 4: D_total = N_afectados × D_individual + D_sistémico

├─ ANÁLISIS B: SISTEMA DE RECOMENDACIÓN → cap. 17 (plataformas digitales) como instrumento primario

Taxonomía General de Aplicaciones

│  └─  Escala PD0–PD8 del cap. 17. El principio del diseñador de la métrica aplica igualmente.

│         · La métrica de engagement que el recomendador optimiza es el nodo de mayor R*.

├─ ANÁLISIS C: SISTEMA AUTÓNOMO CON DAÑO FÍSICO

│  └─  PRIORIDAD 1: ¿El fallo fue dentro del rango de entrenamiento o por distribution shift?

│         · Dentro del rango → R* del diseñador de las reglas de decisión. Las reglas eran la condición necesaria. │         · Distribution shift → R* del diseñador del proceso de validación que no cubrió esa situación. │  └─  PRIORIDAD 2: ¿El desplegador operó el sistema en el entorno para el que fue certificado?

│         · Si el entorno de despliegue excedió el dominio de certificación → R*_DE positivo.

└─ ANÁLISIS D: LLM / SISTEMA GENERATIVO

└─  PRIORIDAD 1: Identificar el nodo de la cadena donde se tomó la decisión que permitió el daño

· Desarrollador modelo base / Ajustador fino / Operador de la aplicación / Usuario. └─  PRIORIDAD 2: ¿El nodo tenía restricciones que habrían prevenido el daño específico?

· Si las restricciones habrían prevenido el daño y no fueron implementadas → R* de ese nodo positivo.

├─ Paso 2: ¿El diseñador de la métrica tiene Anteros o Potós documentado? │

├─ Anteros documentado → S_DM bajo [0.03–0.20] → R*_DM pleno sobre DI_métrica

│  └─  El DM sabía que la métrica producía DI y eligió no modificarla. Pretensión máxima contra DM.

Taxonomía General de Aplicaciones

├─ Potós (estándar del campo del período) → S_DM moderado-alto [0.40–0.70]

│  └─  Responsabilidad civil. Reforma del sistema con auditoría de la métrica como requisito. └─ Deimos (evidencia del DI de la métrica no disponible en el período) → S_DM alto [0.56–0.84]

└─  Responsabilidad reducida del DM. Analizar R*_RG por ausencia de estándares de auditoría.

└─ Paso 3: ¿El D_total incluye el componente sistémico?

├─ SÍ (sistema operó durante meses o años sobre población amplia) → D_sistémico relevante

│  └─  D_total = N_afectados × D_individual + D_sistémico. El D_sistémico puede dominar. └─ NO (sistema de despliegue limitado o daño individual único) → D_total = D_individual

└─  AD_i = R*_i × D_individual × (1 − α_i). Mismos instrumentos del dominio de aplicación.

— Fin del Capítulo 49 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

