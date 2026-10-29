### Capítulo 13 Inteligencia artificial y algoritmos de decisión

El diseñador de la métrica: el nodo más invisible y el de mayor

R* en el grafo algorítmico

### §1.  El problema

En 2016, el periodista de investigación Jeff Larson publicó en ProPublica un análisis del sistema COMPAS — Correctional Offender Management Profiling for Alternative Sanctions— utilizado en varios estados de los EE.UU. para asistir a los jueces en las decisiones de libertad condicional y fijación de fianzas. El análisis mostraba que COMPAS producía predicciones de reincidencia significativamente sesgadas por raza: los acusados negros eran clasificados como de alto riesgo de reincidencia a una tasa casi el doble que los acusados blancos con perfiles criminales comparables. La empresa desarrolladora, Northpointe, respondió que el algoritmo era igualmente preciso para ambos grupos raciales. Ambas afirmaciones eran matemáticamente correctas. Y ambas apuntaban a hechos reales del algoritmo.

La aparente contradicción se resuelve cuando se entiende que hay múltiples definiciones de "equidad" matemáticamente incompatibles entre sí bajo ciertas condiciones. Pero esa resolución técnica evita la pregunta

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

más importante: ¿quién decidió que "reincidencia" — definida como un nuevo arresto en los dos años siguientes— era la métrica correcta para predecir riesgo? Esa no es una decisión técnica. Es una decisión política y normativa con consecuencias distribucionales enormes: si la tasa de arresto es históricamente sesgada (más negros arrestados que blancos por los mismos comportamientos, por el sesgo del sistema policial), entonces entrenar un modelo para predecir "arrestos futuros" es entrenar un modelo para reproducir el sesgo policial histórico como si fuera riesgo intrínseco del individuo.

En 2018, Reuters reveló que Amazon había desarrollado un sistema de inteligencia artificial para el screening inicial de candidatos a posiciones de ingeniería. El sistema había sido entrenado con los CVs de empleados contratados y exitosos durante los diez años anteriores. Amazon era en ese período una empresa con una fuerza de trabajo técnica abrumadoramente masculina. El sistema aprendió que "buen candidato de ingeniería" significaba "candidato parecido a los ingenieros que habían tenido éxito en Amazon en los últimos diez años" —es decir, abrumadoramente masculino. Como resultado, el sistema penalizaba activamente los CVs que mencionaban la palabra "mujeres" (como en "presidenta del club de robótica de mujeres") y los egresados de universidades exclusivamente femeninas.

Estos dos casos producen la misma pregunta con respuestas igualmente perturbadoras: ¿quién tiene R* en el resultado discriminatorio del algoritmo? La respuesta convencional es "el algoritmo" o "los datos". La respuesta del sistema de imputación causal es más precisa: el nodo de mayor R* no es el algoritmo ni el dataset. Es quien definió la métrica que el algoritmo optimiza. Esa decisión —qué variable es el target, qué se llama "reincidencia", qué se llama "candidato exitoso"— es el acto de diseño de mayor

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

### R* en el grafo algorítmico, y es sistemáticamente el nodo menos visible.

### 1.1 El triángulo del sistema algorítmico

### Todo sistema algorítmico de decisión tiene tres componentes que el análisis de responsabilidad debe distinguir con precisión:

Componente Descripción Quién lo controla

R* típico

La métrica target

La variable que el algoritmo optimiza. "Reincidencia", "candidato exitoso", "riesgo de impago". Define qué significa el éxito del sistema.

El directivo o el equipo que diseñó el sistema. Es una decisión humana, no técnica.

ALTO — es el nodo de diseño del objetivo

El dataset Los datos históricos con los que el algoritmo aprende a predecir la métrica. Contienen el sesgo de los sistemas que los produjeron.

Hereda el sesgo de quienes generaron los datos históricos. Nodo sin voluntad que transmite ese sesgo al sistema presente.

MODERADO-ALTO — transmite el sesgo histórico

El modelo El algoritmo de aprendizaje

El equipo técnico

BAJO — optimiza la

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

automático que aprende el patrón entre los features y la métrica.

que lo construyó. Sin voluntad propia: optimiza lo que se le pide sobre los datos que le dan.

métrica dada con los datos dados

Principio algorítmico:  La jerarquía de responsabilidad algorítmica invierte la jerarquía de visibilidad: el componente más visible (el modelo, el algoritmo) tiene el R* más bajo. El componente más invisible (quien definió la métrica) tiene el R* más alto. El análisis de responsabilidad algorítmica convencional trabaja al revés: pide cuentas al modelo cuando debería pedir cuentas al diseñador de la métrica.

### 1.2 La métrica como acto de diseño normativo

Definir la métrica que un algoritmo optimiza no es un acto técnico neutral. Es un acto normativo que codifica una teoría sobre qué importa, qué se mide y cómo se distribuirán los resultados del sistema. Cuando esa teoría tiene consecuencias distribucionales que afectan desproporcionadamente a grupos específicos, el diseñador de la métrica tiene R* positivo en esas consecuencias.

### La distinción entre la decisión técnica y la decisión normativa es fundamental para el análisis de responsabilidad:

•  Decisión técnica: qué arquitectura de modelo usar, qué features incluir, cómo regularizar, cuántos parámetros entrenar. Estas decisiones tienen R* bajo porque son sustituibles: cualquier equipo técnico competente

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

tomaría decisiones equivalentes bajo las mismas restricciones. •  Decisión normativa: qué variable optimizar (la métrica target), qué población incluir en el dataset de entrenamiento, qué período histórico usar como referencia, qué umbrales de clasificación usar para la decisión final. Estas decisiones tienen R* alto porque definen el comportamiento del sistema y no hay una única respuesta técnicamente correcta —hay múltiples opciones con consecuencias distribucionales distintas.

Diseñador de la métrica (nodo de mayor R*):  El actor humano o institucional que tomó la decisión normativa de qué variable optimiza el algoritmo. No es necesariamente quien lo programó ni quien lo desplegó: es quien definió el objetivo. En COMPAS, quien decidió que "reincidencia" = "nuevo arresto en 2 años" en lugar de "nueva condena" o "violencia documentada". En Amazon, quien decidió que el "éxito" se mediría con los CVs históricos de contrataciones previas sin ajustar por la composición de género del período.

### 1.3 Por qué los hijos no aplican en este dominio

En el dominio de los algoritmos de IA, los hijos de Afrodita no aplican a ningún nodo del sistema algorítmico. La razón es la misma que en los capítulos 8 (score crediticio) y 9 (quiebra): los nodos del grafo son instrumentos técnicos — el modelo, el dataset, la métrica como entidad matemática— que no tienen voluntad propia.

Los hijos sí aplican a los directivos y diseñadores humanos cuando su responsabilidad se analiza desde la perspectiva del Capítulo 11 (gobierno corporativo) o el Capítulo 1 (responsabilidad jurídica individual). Pero en el análisis del sistema algorítmico como tal, el instrumento correcto es el

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

grafo de dependencias entre componentes, no el diagnóstico de disposiciones de voluntad.

Esta restricción tiene una consecuencia importante: la ausencia de hijos no significa ausencia de responsabilidad humana. Significa que la responsabilidad humana en el dominio algorítmico se atribuye a los actores que tomaron las decisiones que configuraron el sistema —el diseñador de la métrica, el aprobador del dataset, el directivo que desplegó el sistema— y esa atribución se hace a través del INCF de sus decisiones en el grafo, no a través de su disposición de voluntad.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

### §2.  Página puente — Traducción al lenguaje de la IA y los sistemas de decisión algorítmica

Esta página resume las herramientas del sistema en el contexto de la inteligencia artificial, el aprendizaje automático y los sistemas de decisión algorítmica. El lector con formación en ciencias de datos, ingeniería de software o política tecnológica puede comenzar aquí.

Herramienta En IA y algoritmos se llama

Qué significa

Grafo causal G

Red de responsabilidad algorítmica

El mapa de todos los nodos que contribuyeron causalmente al resultado sesgado o dañino: el diseñador de la métrica, el dataset, el modelo, el desplegador, el regulador, y el contexto histórico que generó los datos sesgados.

R* (vector) Responsabilidad algorítmica causal

La fracción del resultado dañino causalmente atribuible a cada nodo. El modelo tiene R* bajo (optimiza lo que le piden). El diseñador de la métrica tiene R* alto (definió qué optimizar). El dataset tiene R* moderado (transmite el sesgo histórico).

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

Nodo de la métrica

Diseñador de la variable objetivo (target)

El nodo de mayor R* del grafo algorítmico. Quien decidió qué optimiza el sistema. Es una decisión normativa, no técnica, y su R* es proporcional a cuánto el resultado dañino depende de esa elección específica.

Nodo del dataset

Dataset histórico sesgado

Nodo sin voluntad que transmite el sesgo de los sistemas históricos que lo produjeron. Su R* apunta hacia quienes generaron esos datos históricos bajo sistemas sesgados (la misma cadena del Capítulo 8 sobre redlining).

Nodo del modelo

Algoritmo de aprendizaje

Nodo sin voluntad. R* bajo: optimiza la métrica que le dieron sobre los datos que le dieron. Su R* apunta hacia el diseñador de la métrica y el proveedor del dataset.

Nodo desplegador

Quien desplegó el sistema en producción

Tiene R* positivo si desplegó el sistema sin auditoría de equidad o sin el análisis de disparate impact que sus consecuencias requerían. R* proporcional a cuánto sabía o debía saber sobre el sesgo antes del despliegue.

S del modelo Fungibilidad del modelo técnico

S muy alto: cualquier modelo de aprendizaje competente entrenado con la misma métrica y el mismo dataset habría

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

producido el mismo sesgo. La solución técnica (cambiar el modelo) no resuelve el problema si la métrica y el dataset permanecen.

S del dataset Fungibilidad del sesgo histórico

S depende de si el sesgo es específico de ese dataset (idiosincrático) o genérico de cualquier dataset de ese período y contexto. Si es genérico (S alto), la corrección debe ser sobre la métrica, no solo sobre el dataset.

α del desplegador

Medidas de mitigación implementadas antes del despliegue

Auditoría de equidad antes del despliegue, análisis de disparate impact, comunicación transparente a los afectados sobre el uso del algoritmo, mecanismos de apelación. α = 0: nada de lo anterior.

Δ del diseñador

Déficit de responsabilidad del diseñador de la métrica

La brecha entre el R* del diseñador de la métrica en el resultado sesgado y su asunción efectiva. Cuando el diseñador afirma "el modelo es técnicamente correcto" sin reconocer que la elección de la métrica era el problema, Δ es positivo.

D_total Daño algorítmico total

T_invertido (decisiones incorrectas ya tomadas por el algoritmo y sus consecuencias directas), T_impedido (oportunidades negadas a los individuos mal

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

clasificados), ΔT_trayectoria (pérdida permanente de potencial de los afectados).

Para el lector que viene del núcleo universal:  Este dominio extiende el concepto del nodo algorítmico/dataset del Capítulo 8 con dos precisiones nuevas. Primera: la distinción entre la métrica (decisión normativa de alto R*) y el modelo (decisión técnica de bajo R*). Segunda: la propiedad de que el modelo tiene S = 1.0 porque optimiza mecánicamente lo que se le pide — la única manera de cambiar el resultado del modelo es cambiar la métrica o el dataset.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

### §3.  Las herramientas en el dominio algorítmico

### 3.1 El grafo de responsabilidad algorítmica

El grafo de un sistema algorítmico tiene una estructura jerárquica que difiere de los grafos de los dominios anteriores en un aspecto crítico: todos los nodos del sistema técnico (métrica, dataset, modelo) son condición necesaria del resultado, pero sus pesos causales son muy distintos. La métrica determina qué se optimiza. El dataset determina con qué patrones se aprende. El modelo optimiza la métrica usando esos patrones. Sin la métrica y el dataset dados, el modelo no puede producir el resultado sesgado.

Nodo Tipo R* típico

Descripción y dirección del R*

Diseñador de la métrica

Decisión normativa

~35– 50% Definir qué optimiza el sistema es el acto de mayor impacto causal. Su R* no apunta "hacia abajo" a otros nodos: es el origen de la cadena. Humano con responsabilidad.

Contexto histórico generador del sesgo

Estructura causal profunda

~20– 35% Los sistemas históricos sesgados (redlining, discriminación en el empleo) que generaron los datos del dataset. R* apunta hacia el nodo del dataset y retrocede hacia las instituciones históricas. Análogo al redlining del Cap. 8.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

Dataset Nodo técnico sin voluntad

~15– 25% Transmite el sesgo histórico al modelo. Su R* apunta hacia quienes lo generaron (contexto histórico) y hacia el desplegador que lo usó sin auditar.

Desplegador Decisión humana de producción

~10– 20% Quien tomó la decisión de usar el sistema en producción sobre poblaciones reales. Su R* es mayor cuando tenía información sobre el sesgo y no actuó.

Modelo (algoritmo)

Nodo técnico sin voluntad

~3– 8% S = 1.0 prácticamente: cualquier modelo competente habría aprendido el mismo patrón sesgado de los mismos datos para la misma métrica. R* residual apunta hacia el diseñador de la métrica.

Regulador Omisión sistémica

~5– 12% La ausencia de estándares de auditoría obligatoria antes del despliegue. S alto: cualquier regulador bajo el mismo marco habría tenido la misma brecha.

### 3.2 La propiedad de la S = 1.0 del modelo: por qué cambiar el algoritmo no resuelve el sesgo

La propiedad más contraintuitiva del análisis algorítmico es que el modelo tiene sustituibilidad prácticamente perfecta (S ≈ 1.0) respecto al sesgo del sistema. Esto significa que

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

cambiar el modelo —usar Random Forest en lugar de regresión logística, usar una red neuronal en lugar de un árbol de decisión— no reduce el sesgo si la métrica y el dataset permanecen igual.

S_modelo ≈ 1.0 → R*_modelo × (1 − S_modelo) ≈ 0

→ cambiar el modelo tiene impacto mínimo en el

sesgo

Esta propiedad emerge directamente del teorema de la optimalidad estadística de Bayes: si el dataset contiene el sesgo y la métrica target codifica ese sesgo, cualquier modelo suficientemente expresivo aprenderá el mismo patrón sesgado porque ese patrón es el que mejor predice el target en ese dataset. El modelo no "introduce" el sesgo: lo destila del dataset en la dirección de la métrica.

Analogía: El traductor no inventa el mensaje Si tienes un texto racista y le pides a un buen traductor que lo traduzca al inglés, el resultado es un texto racista en inglés. Cambiar el traductor —usar uno diferente, más sofisticado— produce el mismo resultado. El problema no está en el traductor (el modelo): está en el texto original (el dataset) y en la instrucción de traducir en lugar de editar (la métrica).

Esta propiedad tiene una consecuencia regulatoria directa: las regulaciones de IA que se enfocan en la "explicabilidad del modelo" (por qué el algoritmo tomó esa decisión) no resuelven el problema de equidad si no abordan la elección de la métrica. Puedes explicar perfectamente por qué COMPAS clasificó a un acusado negro como de alto riesgo (porque tiene características estadísticamente asociadas con nuevos arrestos en el dataset histórico), y esa explicación completa no resuelve el problema de que el dataset histórico refleja el sesgo del sistema policial.

### 3.3 R* del diseñador de la métrica y la doctrina de la responsabilidad por diseño normativo

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

El diseñador de la métrica tiene R* alto porque su decisión normativa es condición necesaria del resultado sesgado en una forma que no es compartida por los demás nodos: sin esa elección específica de métrica, el sistema podría haber producido un resultado diferente incluso con el mismo dataset y el mismo modelo. La responsabilidad por diseño normativo es la doctrina que el cálculo causal formaliza:

### R*_diseñador_métrica = f (impacto_de_la_elección_de_métrica_en_el_resultad

### o, S_métrica)

S de la métrica mide qué tan idiosincrática era esa elección: si cualquier equipo razonable habría elegido la misma métrica en ese contexto (S alto), el R* del diseñador es moderado. Si la elección era una entre múltiples alternativas razonables con consecuencias distribucionales distintas (S bajo), el R* es alto.

Elección de métrica

S de la métrica

R* del diseñador

Alternativas disponibles y su impacto

### 0.35 Alto Alternativa: "nueva condena" o "violencia documentada". Ambas tienen menor sesgo racial porque los datos de condenas son menos sesgados que los de arrestos.

COMPAS: "reincidencia" = nuevo arresto

### 0.25 Muy alto Alternativa obvia: definir "éxito" con métricas de desempeño futuro (contribuciones documentadas,

Amazon: "candidato exitoso" = similar a empleados históricos

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

promociones, retención) en lugar de similitud con el perfil histórico.

### 0.70 Moderado S alto: la mayoría de los sistemas crediticios definen riesgo como historial de impagos. Es una elección del sector, no solo del diseñador específico.

Sistema de crédito: "riesgo" = historial de impagos

### 0.55 Moderado-alto

Alternativas: calidad de vida ajustada, años de vida ajustados por discapacidad (AVAD). La elección afecta la distribución del tratamiento entre grupos de edad.

Sistema médico: "utilidad del tratamiento" = supervivencia a 5 años

### 3.4 α y Δ en el dominio algorítmico

### En el dominio algorítmico, α tiene interpretaciones específicas para cada tipo de nodo humano:

Conducta que sube α

Nodo humano

α en este dominio

Diseñador de la métrica

Grado en que consideró alternativas de métrica y sus consecuencias distribucionales.

Documentó el análisis de alternativas de métrica. Realizó simulaciones de disparate impact bajo distintas definiciones. Eligió la métrica con menor disparate impact

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

entre las técnicamente razonables. Informó transparentemente sobre las limitaciones de la elección.

Proveedor / curador del dataset

Grado en que auditó el sesgo del dataset antes de usarlo.

Realizó análisis de sesgo histórico en el dataset. Implementó técnicas de debiasing o re-weighting. Documentó las limitaciones conocidas del dataset.

Desplegador Grado en que auditó el sistema antes del despliegue y comunicó sus limitaciones.

Realizó auditoría de equidad completa (disparate impact, calibración por grupo). Comunicó las limitaciones a los decisores que usarían el output. Implementó mecanismos de apelación para los afectados.

Regulador Grado en que estableció estándares obligatorios de auditoría y equidad antes del despliegue.

Publicó estándares de equidad algorítmica antes del despliegue en sectores de alto impacto. Realizó auditorías regulatorias de los sistemas en producción.

### 3.5 El D_total algorítmico: cómo cuantificar el daño de un sistema que opera a escala

El daño de un sistema algorítmico sesgado tiene una característica única respecto a los daños individuales de los capítulos anteriores: opera a escala. COMPAS procesó cientos de miles de casos; el sistema de Amazon analizó millones de CVs. El D_total algorítmico debe capturar tanto las consecuencias individuales (cada decisión

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

incorrecta) como las consecuencias sistémicas (el patrón de decisiones sobre una población).

D_total_algorítmico = N_afectados × D_promedio_individual + D_sistémico_adicional

donde D_promedio_individual es el daño promedio por decisión incorrecta (calculado con la estructura del Capítulo 1 para decisiones de justicia penal o del Capítulo 8 para decisiones crediticias) y D_sistémico_adicional es el daño al sistema de confianza que trasciende las decisiones individuales: la erosión de la legitimidad del sistema de justicia o del proceso de contratación cuando se descubre que operaba con sesgo sistemático.

La expresión en tiempo de vida:

D_vital_algorítmico = D_total / w_ref [horas de vida

de los afectados no recuperadas]

En el caso de COMPAS: cada clasificación incorrecta como "alto riesgo" que resultó en detención preventiva o denegación de libertad condicional representó en promedio varios meses de vida en condiciones de reclusión. Multiplicado por los miles de casos afectados, el D_vital es sustancial y calculable.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

### §4.  Casos resueltos

Caso A — COMPAS (2016)

R* del dataset histórico de arrestos vs. R* de quien definió "reincidencia" como nuevo arresto

A.1 El contexto histórico y técnico

COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) fue desarrollado por Northpointe (ahora Equivant) a finales de los años 1990. Se basa en un cuestionario de 137 preguntas que evalúa factores como la historia criminal, las circunstancias laborales, las relaciones sociales y las actitudes. Produce un score de riesgo de reincidencia en una escala del 1 al 10, donde puntajes altos indican mayor riesgo.

El sistema se usa en varios estados de los EE.UU. para asistir a los jueces en: decisiones de fianza, decisiones de sentencia, programas de supervisión comunitaria, y elegibilidad para libertad condicional. La palabra "asistir" es importante: en teoría, el score es un insumo para la decisión judicial, no la decisión en sí. En la práctica, estudios de psicología de la decisión muestran que los decisores tienden a seguir las recomendaciones algorítmicas con alta frecuencia, especialmente bajo presión de tiempo.

El análisis de ProPublica examinó más de 7,000 evaluaciones en el condado de Broward, Florida, y encontró dos hechos que parecen contradictorios, pero son matemáticamente compatibles: (a) los acusados negros fueron clasificados como de "alto riesgo" aproximadamente el doble de veces que los blancos con perfiles comparables, y (b) el algoritmo tenía precisión predictiva similar para ambos grupos raciales. La resolución está en que hay

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

múltiples definiciones de equidad matemáticamente incompatibles cuando las tasas base de la métrica target difieren entre grupos —lo que ocurre precisamente cuando la métrica está sesgada históricamente.

### A.2 El grafo causal del sesgo de COMPAS

Nodo Actor/Factor Tipo Función causal en el sesgo

N1 Diseñador de la métrica: "reincidencia" = nuevo arresto en 2 años

Decisión normativa

Esta es la decisión de mayor R* del sistema. Definir "reincidencia" como "nuevo arresto" en lugar de "nueva condena" o "reincidencia violenta documentada" crea la conexión con el sesgo del sistema policial. Sin esta elección específica, el sesgo racial sería menor.

N2 Sesgo histórico del sistema policial y judicial

Contexto histórico generador

Los datos de arrestos en los que fue entrenado COMPAS reflejan décadas de prácticas policiales sesgadas. Las comunidades negras fueron sobrevigiladas históricamente, produciendo más arrestos por los mismos comportamientos.

N3 Dataset histórico de

Nodo técnico sin voluntad

Transmite el sesgo de N2 al sistema. Su

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

arrestos (1990s-2000s) R* apunta hacia N2 (que lo generó) y hacia N4 (que lo usó sin auditar).

N4 Northpointe / jurisdicciones que desplegaron COMPAS

Desplegadores Desplegaron el sistema sin publicar su metodología (fue protegida como secreto comercial) y sin auditorías de equidad previas al despliegue. El secreto comercial impidió durante años que los acusados contestaran las predicciones en su contra.

N5 Modelo estadístico de COMPAS

Nodo técnico sin voluntad

S ≈ 1.0. Cualquier modelo competente entrenado con N3 para predecir N1 habría aprendido el mismo patrón racial porque ese patrón es real en los datos. R* residual apunta a N1 y N3.

N6 Reguladores y legisladores: ausencia de estándares

Omisión sistémica

No existían estándares de equidad algorítmica ni requisitos de transparencia para sistemas de decisión penal en la mayoría de los estados.

Nf Acusados mal clasificados

Nodo final Personas que recibieron clasificaciones de "alto riesgo" por

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

razón de su raza, con consecuencias reales sobre su libertad.

### A.3 R*, S y el análisis de causalidad

Nodo R* S α Interpretaci ón

N1 — Diseñador métrica ~38 %

0.2 8 0.0 5 S moderado-bajo. La elección de "nuevo arresto" vs. "nueva condena" era una elección entre alternativas razonables. La elegida produjo el mayor sesgo racial. Δ = +0.33.

N2 — Sesgo policial histórico

~28 %

### 0.8 0 0.0 5 S alto: el sesgo era sistémico de toda la historia del sistema penal, no específico de estos datos.

N3 — Dataset histórico ~18 %

### 0.7 0 0.0 2 S moderado. El sesgo en los datos era conocible y en parte

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

conocido. Δ = +0.16.

N4 — Northpointe/desplegado res

~12 %

### 0.5 5 0.0 8 Desplegaron sin auditoría ni transparencia. Δ = +0.04.

N5 — Modelo COMPAS ~2% 0.9 7 0.0 0 S prácticamente = 1.0. R*_neta ≈ 0. Cambiar el modelo no habría cambiado el sesgo.

N6 — Reguladores ~2% 0.8 8 0.0 5 Omisión sistémica con S alto.

El resultado central del análisis: el modelo COMPAS (N5), que es el único componente que puede ser "auditado" con las herramientas de explicabilidad de IA, tiene R* = 2% y S = 0.97. Las herramientas de explicabilidad de IA que muestran "por qué el modelo tomó esa decisión" están auditando el nodo de menor responsabilidad causal del sistema. El nodo de mayor R* (N1, el diseñador de la métrica) es el que menos aparece en los debates técnicos sobre la equidad del algoritmo.

### A.4 El argumento de Northpointe y la paradoja de la equidad

La respuesta de Northpointe a ProPublica fue técnicamente correcta: el modelo tiene la misma precisión predictiva (mismo porcentaje de verdaderos positivos) para acusados negros y blancos. ¿Cómo puede ser al mismo tiempo sesgado y preciso?

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

La respuesta está en que hay dos definiciones de equidad que son matemáticamente incompatibles cuando las tasas base difieren entre grupos:

•  Equidad de calibración (Northpointe): el score de "alto riesgo" tiene el mismo significado para ambos grupos —si el modelo dice 70% de probabilidad de reincidencia, eso se cumple al 70% tanto para acusados negros como blancos. Este criterio está satisfecho. •  Equidad de error diferencial (ProPublica): la tasa de falsos positivos (clasificar como alto riesgo a quien no va a reincidir) y la tasa de falsos negativos (clasificar como bajo riesgo a quien sí va a reincidir) deben ser iguales entre grupos. Este criterio no está satisfecho: los acusados negros que no reinciden son clasificados como "alto riesgo" a una tasa casi el doble que los blancos equivalentes.

El teorema de Chouldechova (2017) demuestra que los dos criterios son matemáticamente incompatibles cuando las tasas base de la variable predicha difieren entre grupos. No hay modelo que satisfaga ambos simultáneamente. La elección entre los dos criterios de equidad no es técnica: es normativa. Y esa elección normativa — que en COMPAS se hizo implícitamente al elegir la métrica — es exactamente el acto de diseño con mayor R* del sistema.

Principio algorítmico:  El teorema de Chouldechova formaliza por qué la pregunta "¿es justo el algoritmo?" no tiene respuesta técnica única. Hay múltiples definiciones de "justo" matemáticamente incompatibles bajo ciertas condiciones. La elección entre ellas es siempre política y normativa. El análisis de R* no elige entre las definiciones: identifica con precisión quién tomó la decisión de qué definición usar (implícita o explícitamente), y atribuye a ese actor la responsabilidad proporcional a las consecuencias de esa elección.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

A.5 El D_total de COMPAS: cuantificando el daño a escala

Parámetros para la estimación:

•  Casos procesados con COMPAS en Broward County entre 2013 y 2014 (muestra del estudio ProPublica): ~7,214. •  Tasa de falsos positivos para acusados negros: 44.9%. Para blancos: 23.5%. Diferencia: 21.4 puntos porcentuales. •  Casos de acusados negros en la muestra: aproximadamente 3,800. •  Falsos positivos adicionales para acusados negros (por el sesgo): 3,800 × 0.214 ≈ 813 casos. •  Impacto promedio de una clasificación de "alto riesgo" incorrecta: mayor probabilidad de detención preventiva, mayor fianza, decisiones de sentencia más severas. Estudios estiman que el impacto promedio es ~3-4 meses adicionales de privación de libertad o condiciones de supervisión más restrictivas. •  D_promedio_individual ≈ 3.5 meses × 730 horas/mes = 2,555 horas de vida en condiciones restrictivas.

D_vital_Broward = 813 casos × 2,555 h/caso = 2.077

× 10⁶ horas

D_monetary_equiv = 2.077M h × $8/h = $16.6M USD

(2024)

Para el conjunto del estado de Florida (donde COMPAS ha sido usado en decenas de miles de casos), la escala del daño es un múltiplo de este número. La estimación para el uso nacional de COMPAS y sistemas similares en los EE.UU. produciría D_vital en el orden de decenas de millones de horas.

Distribución del ajuste debitor: El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

AD_N1 (diseñador métrica) = 0.38 × $16.6M = $6. 3M

AD_N2 (sesgo policial hist.) = 0.28 × $16.6M = $4.6M

(atribuible a los sistemas históricos)

AD_N4 (Northpointe) = 0.12 × $16.6M = $2.0M

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

Caso B — Amazon Hiring AI (2018)

R* del directivo que fijó la métrica: "candidato exitoso" = similar a los ingenieros masculinos históricos

B.1 El contexto

Amazon comenzó a desarrollar su sistema de screening algorítmico de candidatos alrededor de 2014. El objetivo era automatizar la revisión inicial de los CVs que llegaban a posiciones de ingeniería, usando machine learning para identificar los candidatos más prometedores.

El sistema fue entrenado con los CVs de personas que habían sido contratadas y habían tenido desempeño exitoso en Amazon durante los diez años anteriores. La muestra de entrenamiento refleja fielmente la composición de la fuerza de trabajo técnica de Amazon en ese período: aproximadamente el 76% masculina en posiciones de ingeniería. El algoritmo aprendió que los patrones lingüísticos, las referencias a actividades extracurriculares, las instituciones educativas y las palabras específicas de los CVs de hombres exitosos eran predictores de "candidato exitoso".

Las consecuencias documentadas incluyen: el sistema penalizaba automáticamente cualquier CV que mencionara la palabra "mujeres" (como en "directora del club de robótica de mujeres") y rebajaba la puntuación de candidatos egresados de las dos universidades femeninas más reconocidas en ciencias computacionales de los EE.UU. Amazon descubrió el problema internamente en 2015, intentó corregirlo, no pudo garantizar que el sesgo hubiera sido eliminado, y descontinuó el sistema en 2017. Reuters lo reportó públicamente en 2018.

B.2 El grafo causal del sesgo de Amazon

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

Nodo Actor/Factor Tipo Función causal

N1 Diseñador de la métrica: "éxito" = similitud con historial de contrataciones

Decisión normativa

La decisión de definir "candidato exitoso" usando el historial de contrataciones pasadas, sin ajustar por la composición de género del período, es la decisión de mayor R* del sistema. S bajo: la alternativa (definir éxito por desempeño futuro documentado) era técnicamente disponible.

N2 Brecha de género histórica en la industria tecnológica

Contexto histórico generador

La sub-representación histórica de mujeres en posiciones técnicas en la industria tecnológica, producida por décadas de discriminación en la contratación y el desarrollo de carrera.

N3 Dataset: CVs de empleados exitosos 2005-2015

Nodo técnico sin voluntad

Refleja fielmente la composición del período: ~76% masculina. Su R* apunta hacia N2 (que produjo esa brecha) y N1 (que usó ese dataset sin ajustar).

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

N4 Equipo técnico de Amazon que desarrolló el modelo

Desarrollo técnico

Construyó el modelo con la métrica y el dataset dados. S prácticamente 1.0: cualquier equipo técnico competente habría producido el mismo sesgo. Su R* apunta hacia N1.

N5 Dirección de Amazon que aprobó el despliegue y continuó su uso en 2015-2017

Desplegador con conocimiento del sesgo

Conocía el sesgo desde 2015 (un año después del despliegue), intentó corregirlo, no pudo garantizarlo, pero continuó usando el sistema durante dos años más. Este conocimiento sin corrección efectiva aumenta su R*.

N6 Modelo de ML (regresión, gradient boosting)

Nodo técnico sin voluntad

S ≈ 1.0. Optimizó la métrica con los datos dados. R*_neta ≈ 0.

Nodo final Candidatas técnicamente cualificadas que no llegaron a la revisión humana por el sesgo del sistema.

Nf Candidatas mujeres que no pasaron el primer filtro

### B.3 La distinción crítica: COMPAS vs. Amazon

Los dos casos tienen estructuras similares pero una diferencia que el análisis causal captura con precisión: la relación entre el diseñador de la métrica y su conocimiento del sesgo.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

Dimensión COMPAS Amazon

Tipo de sesgo en la métrica

"Reincidencia" como nuevo arresto: la métrica tiene sesgo incorporado por el sesgo del sistema policial.

"Éxito" como similitud histórica: la métrica tiene sesgo incorporado por la composición de género del período.

¿Había alternativas de métrica menos sesgadas disponibles?

Sí: "nueva condena" o "violencia documentada" habrían producido menor sesgo racial.

Sí y más claramente: el desempeño futuro documentado era medible y menos sesgado.

¿Sabía el diseñador que el sesgo existía?

El diseño original no incluyó un análisis de equidad racial de la métrica.

El equipo detectó el sesgo en 2015 y continuó usando el sistema. Conocimiento confirmado, acción insuficiente.

R* del diseñador de la métrica

~38% (sin conocimiento previo del sesgo)

~40% + extra por continuación con conocimiento (R* efectivo ~45%)

Δ del diseñador +0.33 (sin asunción del sesgo de la métrica)

+0.37 a +0.40 (mayor por conocimiento confirmado y continuación)

La continuación del uso del sistema durante dos años después de detectar el sesgo aumenta el R* efectivo de la dirección de Amazon (N5) porque convierte la negligencia en conocimiento confirmado con acción insuficiente. Eso produce un Δ mayor y una culpabilidad subjetiva más cercana a Anteros que a Deimos.

### B.4 El D_total de Amazon: las candidatas que no llegaron

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

Parámetros:

•  El sistema procesó candidaturas en Amazon durante aproximadamente 3 años (2014-2017) con el sesgo activo en los últimos 2 años con conocimiento. •  Amazon recibe en el orden de millones de solicitudes al año. Para posiciones de ingeniería, estimado en ~200,000 anuales. •  Fracción de solicitudes de candidatas mujeres: ~30% (consistente con la representación en programas de informática del período). •  Probabilidad de que una candidata cualificada fuera incorrectamente filtrada por el sesgo: estimada en 15-25% del subconjunto que habría pasado sin el sesgo. •  Impacto promedio de no pasar el filtro inicial: pérdida de la oportunidad de entrevista en Amazon, con impacto en trayectoria de carrera estimado en 2-4 años de diferencial salarial.

N_afectadas_anuales ≈ 200,000 × 0.30 × 0.20 = 12,000

candidatas/año

N_afectadas_3_años ≈ 36,000 candidatas

D_promedio = 3 años × ($120,000/año diferencial) =

$360,000 por candidata afectada

D_total_estimado ≈ 36,000 × $360,000 × P(candidata_cualificada) ≈ $6,480M × 0.15 ≈ $972M

Las incertidumbres en este cálculo son altas (especialmente P(candidata_cualificada) y el porcentaje afectado por el sesgo). El rango razonable es $500M-$2,000M. Amazon no pagó indemnizaciones: descontinuó el sistema y no fue procesada. AD_N1 proporcional = 0.40 × $972M = $389M no asumido. Δ efectivo del caso = +0.37.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

B.5 La lección común: el imperativo de la auditoría de métrica

Los dos casos producen una conclusión convergente que el análisis de R* hace explícita: las auditorías de equidad algorítmica que se enfocan en el modelo (explicabilidad, métricas de fairness del output) son necesarias pero insuficientes. El paso previo obligatorio es la auditoría de la métrica: el análisis de las consecuencias distribucionales de la elección de qué se optimiza, antes de que el modelo sea entrenado.

Una auditoría de métrica responde tres preguntas:

1. ¿Cuáles son las alternativas razonables de métrica para este problema? ¿Qué consecuencias distribucionales diferentes producen? 2. ¿Qué grupos se ven desproporcionadamente afectados negativamente por la elección de la métrica actual? ¿Cuánto? 3. ¿Hay una alternativa de métrica que produzca consecuencias distribucionales más equitativas sin sacrificar de manera inaceptable la utilidad técnica del sistema?

Si la respuesta a la pregunta 3 es sí, el diseñador de la métrica tiene R* positivo en el daño producido por la elección actual y Δ proporcional a ese R* hasta que cambie la métrica. Si la respuesta es no (no hay alternativa técnicamente viable con menor disparate impact), el R* del diseñador de la métrica es bajo porque la elección era virtualmente necesaria. Si la respuesta es "no lo sabemos porque no se analizó", el R* del desplegador es alto por no haber realizado la auditoría que las consecuencias del sistema requerían.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

### §5.  Límites del método en IA y algoritmos

### 5.1 El problema de la definición del daño en sistemas de recomendación

Los algoritmos de recomendación (de contenido, de productos, de noticias) producen daños difusos y acumulativos que son difíciles de atribuir a decisiones individuales del sistema. El daño de la radicalización algorítmica, por ejemplo, no es producido por una decisión puntual del algoritmo sino por el patrón acumulado de miles de recomendaciones a lo largo de meses. El análisis de R* sobre ese tipo de daño requiere modelos de trayectoria del usuario que van más allá del grafo estático del capítulo.

### 5.2 La dificultad de identificar al "diseñador de la métrica" en sistemas de gran escala

En los sistemas algorítmicos desarrollados por grandes organizaciones, la decisión de qué métrica optimizar frecuentemente no es tomada por una sola persona en un momento identificable. Es el resultado de múltiples decisiones iterativas de equipos, revisiones de negocio y constrains técnicos. En esos casos, el "diseñador de la métrica" como nodo del grafo puede ser difuso, lo que complica el análisis de R*. La solución metodológica es tratar la organización como el nodo de diseño de la métrica, con R* atribuido al ego colectivo (Capítulo 11).

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

### 5.3 El problema del sesgo emergente: cuando el algoritmo aprende más que la métrica

Algunos sistemas de IA desarrollan patrones de comportamiento que no estaban explícitamente codificados en la métrica ni en el dataset, pero emergen de la interacción entre ambos. Estos sesgos emergentes son más difíciles de atribuir causalmente porque no reducen a ninguna decisión de diseño identificable. Son propiedades emergentes del sistema completo, lo que hace que el análisis de R* sobre el sistema estático sea insuficiente.

### 5.4 El límite de la interpretabilidad como solución

Las técnicas de interpretabilidad de IA (SHAP values, LIME, atención) explican qué features influyeron en cada decisión individual del modelo. Esa información es útil pero no resuelve el problema de responsabilidad causal porque explica el nodo de menor R* del sistema (el modelo) en lugar de identificar el nodo de mayor R* (el diseñador de la métrica). El análisis de R* complementa la interpretabilidad: la interpretabilidad dice cómo decide el modelo; el análisis de R* dice quién es responsable de que el modelo decida de esa manera.

### 5.5 La tensión entre la eficiencia predictiva y la equidad distributiva

En muchos sistemas, la métrica de máxima eficiencia predictiva (la que minimiza el error de predicción en el dataset) y la métrica de máxima equidad distribucional (la que minimiza el disparate impact entre grupos) producen resultados distintos. Cuando son incompatibles, la elección entre ellas no es técnica. El sistema de imputación causal no

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

### resuelve esa tensión: identifica con precisión quién la resuelve y qué responsabilidad tiene esa persona por la resolución que adoptó.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

§6.  Profundización formal — Esta sección puede saltarse sin perder el argumento del capítulo

### §6.  Profundización formal

### 6.1 El teorema de Chouldechova y sus implicaciones para R*

Sea f un clasificador, Y la variable predicha (reincidencia), Â la predicción y A la variable de grupo protegido (raza). Las tres definiciones de equidad relevantes son:

Calibración:    P (Y=1|Â=1, A=0) = P (Y=1|Â=1,

A=1)

Balance FPR:    P (Â=1|Y=0, A=0) = P (Â=1|Y=0,

A=1)

Balance FNR:    P (Â=0|Y=1, A=0) = P (Â=0|Y=1,

A=1)

El teorema de Chouldechova establece: si P(Y=1|A=0) ≠ P(Y=1|A=1) (las tasas base difieren entre grupos), entonces no existe f que satisfaga simultáneamente calibración y balance de FPR/FNR, a menos que f sea perfecto (tasa de error = 0).

En términos del análisis de R*: cuando las tasas base difieren por razones de sesgo histórico (el caso de COMPAS, donde la tasa de "nuevo arresto" es históricamente mayor para acusados negros por el sesgo policial), la incompatibilidad entre definiciones de equidad no es un problema técnico del modelo — es una consecuencia de la elección de la métrica target. El R* de esa incompatibilidad pertenece al diseñador de la métrica, no al modelo que la hereda.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

### 6.2 La descomposición causal del disparate impact

El disparate impact observado de un sistema algorítmico puede descomponerse en tres componentes causales:

DI_total = DI_métrica + DI_dataset + DI_modelo

donde:

DI_métrica:  el disparate impact producido por la elección de la variable target

(qué pasaría con un dataset sin sesgo y esa métrica) DI_dataset:  el disparate impact adicional introducido por el sesgo del dataset (qué pasaría con la misma métrica y un dataset debiased)

DI_modelo:   el disparate impact adicional introducido por el modelo

(típicamente mínimo: S_modelo ≈ 1.0) Esta descomposición produce directamente los R* proporcionales de cada nodo:

R*_diseñador_métrica ∝ DI_métrica / DI_total

R*_dataset           ∝ DI_dataset / DI_total

R*_modelo            ∝ DI_modelo / DI_total ≈ 0

### 6.3 El análisis de sensibilidad de la métrica

La manera más directa de estimar el R* del diseñador de la métrica es el análisis de sensibilidad: calcular el disparate impact del sistema bajo distintas definiciones de la métrica target y comparar.

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

R*_diseñador_métrica = (DI_métrica_actual −

DI_métrica_alternativa_mínima) / DI_total

Si el disparate impact bajo la métrica alternativa óptima (la que produce el menor DI técnicamente razonable) es significativamente menor que el actual, la diferencia es causalmente atribuible a la elección de métrica. Ese diferencial dividido por el DI total produce el R* del diseñador.

Para COMPAS con la métrica "nuevo arresto" vs. la alternativa "nueva condena violenta":

DI_métrica_actual (nuevo arresto):          1.80 (80% mayor tasa de clasificación alto riesgo para negros) DI_métrica_alternativa (nueva condena viol.): ~1.25 (25% mayor — consistente con estudios de recidivism) R*_diseñador_métrica ≈ (1.80 − 1.25) / (1.80 − 1.0) = 0.55 / 0.80 ≈ 0.69 Un R* de 0.69 para el diseñador de la métrica es el resultado más alto del grafo y confirma que la elección de "nuevo arresto" como proxy de reincidencia es el nodo causal dominante en el sesgo racial del sistema.

### 6.4 Código Python de referencia

import numpy as np from scipy.stats import pearsonr  def analisis_responsabilidad_algoritmica(W_algo, alpha_nodos, DI_observado=None,                                           DI_alternativa=None, D_total=None, w_ref=8.0,                                           nombres=None): """     Análisis de responsabilidad algorítmica causal.     W_algo: matriz de pesos del grafo algorítmico     alpha_nodos:  α por nodo (auditoría/mitigación implementada)     DI_observado: disparate impact observado del sistema actual     DI_alternativa: DI bajo la métrica alternativa de menor sesgo     D_total:      daño total estimado     """     n = W_algo.shape[0]      # ── R*: responsabilidad algorítmica causal ── R = np.ones(n) / n     for _ in range(500):         Rn = W_algo @ R; s = np.sum(Rn)         if s < 1e-12: break         Rn /= s         if np.max(np.abs(Rn - R)) < 1e-9: break         R = Rn     R_star = Rn      # ── S: fungibilidad algorítmica ──     S = np.zeros(n)     for i in range(n): max_c = 0         for j in range(n):             if j == i: continue             Wm = W_algo.copy()             Wm[i,:] = np.mean(W_algo, axis=0)             Rm

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

= np.ones(n)/n             for _ in range(200):                 Rm2 = Wm @ Rm; sm = np.sum(Rm2)                 if sm < 1e-12: break                 Rm2 /= sm                 if np.max(np.abs(Rm2-Rm)) < 1e-6: break Rm = Rm2             c, _ = pearsonr(R_star, Rm2)             max_c = max(max_c, abs(c))         S[i] = 1 - max_c      Delta = R_star -alpha_nodos     R_neta = R_star * (1 - S)      result = {         'R_star': R_star, 'S': S,         'Delta': Delta, 'R_neta': R_neta,         'J_sistema': float(1 - np.sum(np.abs(Delta))),     }      # ── R* del diseñador de la métrica via análisis de sensibilidad ──     if DI_observado and DI_alternativa:         DI_base = 1.0         R_star_metrica = (DI_observado - DI_alternativa) / (DI_observado - DI_base) result['R_star_disenador_metrica_por_DI'] = max(0, R_star_metrica) if D_total:         result['AD'] = R_star * D_total         result['D_vital'] = D_total / w_ref      return result  # ── COMPAS ── # N0=Diseñador_métrica, N1=Sesgo_policial_hist, N2=Dataset, # N3=Northpointe_desp, N4=Modelo, N5=Reguladores, N6=Nf W_c = np.zeros((7,7)) W_c[0,2]=0.85; W_c[0,3]=0.75; W_c[0,6]=0.80 W_c[1,2]=0.90; W_c[1,6]=0.65 W_c[2,4]=0.95; W_c[2,6]=0.70 W_c[3,6]=0.60; W_c[4,6]=0.50; W_c[5,6]=0.30  alpha_c = np.array([0.05, 0.05, 0.02, 0.08, 0.00, 0.05, 0.0]) noms_c = ['N0-Diseñ_métrica','N1-Sesgo_policial','N2-Dataset',           'N3-Northpointe','N4-Modelo','N5-Reguladores','Nf']  res_c = analisis_responsabilidad_algoritmica(     W_c, alpha_c, DI_observado=1.80, DI_alternativa=1.25,     D_total=16_600_000, w_ref=8.0, nombres=noms_c)  print("=== COMPAS — Responsabilidad algorítmica causal ===") for nm, rs, si, di in zip(noms_c, res_c['R_star'],                            res_c['S'], res_c['Delta']): notas = ' ← modelo (S≈1.0)' if nm == 'N4-Modelo' else ''     print(f" {nm:22s} R*={rs:.3f} S={si:.2f} Δ={di:+.3f}{notas}")  r_dm = res_c.get('R_star_disenador_metrica_por_DI', 0) J = res_c['J_sistema'] print(f"\nR* diseñador métrica (DI): {r_dm:.3f}") print(f"J (justicia estructural):  {J:.3f}") print(f"D_vital:                   {res_c['D_vital']:,.0f} horas")  # ── Amazon ── W_a = np.zeros((7,7)) # N0=Diseñ_métrica, N1=Brecha_gén_hist, N2=Dataset_CVs, # N3=Equipo_técnico, N4=Dirección_despliegue, N5=Modelo, N6=Nf W_a[0,2]=0.88; W_a[0,4]=0.80; W_a[0,6]=0.82 W_a[1,2]=0.85; W_a[1,6]=0.60 W_a[2,3]=0.92; W_a[2,6]=0.70 W_a[3,5]=0.95; W_a[4,6]=0.65; W_a[5,6]=0.50  alpha_a = np.array([0.04, 0.03, 0.02, 0.05, 0.10, 0.00, 0.0]) noms_a = ['N0-Diseñ_métrica','N1-Brecha_gén','N2-Dataset_CVs',           'N3-Equipo_técn','N4-Dirección','N5-Modelo','Nf']  res_a = analisis_responsabilidad_algoritmica(     W_a, alpha_a, DI_observado=1.65, DI_alternativa=1.10,     D_total=972_000_000, w_ref=8.0)  print("\n=== Amazon Hiring AI — Responsabilidad algorítmica causal ===") for nm, rs, si, di in zip(noms_a, res_a['R_star'], res_a['S'], res_a['Delta']):     print(f"  {nm:22s} R*={rs:.3f} S={si:.2f} Δ={di:+.3f}") r_am = res_a.get('R_star_disenador_metrica_por_DI', 0) print(f"\nR* diseñador métrica (DI): {r_am:.3f}") print(f"J (justicia estructural):  {res_a['J_sistema']:.3f}")

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión

Miguel Hilario Olvera Aguilar Centro Multidisciplinario Meriadock Formación y Asesoría A.C, 2026

Continúa en el Capítulo 14 — Medio ambiente y ecología

El Cálculo de la Responsabilidad · Cap. 14 — Medio ambiente y ecología

PARTE IV · INGENIERÍA Y TECNOLOGÍA

