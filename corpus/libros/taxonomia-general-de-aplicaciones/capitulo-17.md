PARTE II · Ciencias Económicas y Financieras

## Capítulo 17

### Plataformas digitales — economía de datos y responsabilidad

### algorítmica

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo Este capítulo es Nivel C. Sus rangos son candidatos. La aportación central es conceptual: la jerarquía de responsabilidad algorítmica, la doctrina del diseñador de la métrica como nodo de mayor R*, y la estructura del grafo de la plataforma digital. Antes de usar los rangos en una pretensión formal, ajustar con evidencia empírica específica del caso. Este capítulo integra dos líneas analíticas. La primera, derivada de El cálculo de la responsabilidad cap. 13 (IA y algoritmos de decisión): la responsabilidad en el sistema algorítmico está invertida respecto a la visibilidad — el componente más visible (el modelo) tiene R* más bajo; el más invisible (quien definió la métrica que el modelo optimiza) tiene R* más alto. La segunda, extensión al dominio de plataformas: la plataforma que diseñó el algoritmo de recomendación, la política de monetización de datos y la arquitectura de moderación de contenidos tiene R* sobre los daños que esas decisiones producen en los usuarios. Para la evidencia del sesgo algorítmico, ve a §2. Para el mapa de nodos del grafo de la plataforma, ve a §5. Para la prioridad de evidencia, ve a §9.

### §1  Descripción del subcampo

Las plataformas digitales introducen en el sistema de imputación causal una arquitectura de R* que invierte la

Taxonomía General de Aplicaciones

jerarquía de visibilidad con más fuerza que cualquier dominio anterior. El usuario que publicó el contenido dañino es el nodo más visible documentalmente. El modelo que lo amplificó es el nodo de visibilidad intermedia. El diseñador de la métrica de engagement que el modelo optimizaba — el ejecutivo que decidió que el objetivo del algoritmo era maximizar el tiempo en pantalla o la reacción emocional — es el nodo menos visible y el de mayor R*.

La razón es el principio algorítmico del cap. 13 de El cálculo de la responsabilidad: el modelo tiene S ≈ 1.0 porque cualquier modelo competente entrenado con la misma métrica y el mismo dataset de comportamiento de usuarios habría aprendido los mismos patrones de amplificación del contenido emocionalmente intenso. Cambiar el modelo no resuelve el daño — lo resuelve cambiar la métrica que el modelo optimiza. Y quien define esa métrica tiene R* alto con S bajo: la elección de "maximizar el tiempo en pantalla" versus "maximizar el bienestar informativo del usuario" era una elección deliberada entre alternativas disponibles con consecuencias distribucionales distintas.

El principio del diseñador de la métrica en el dominio de plataformas digitales En toda plataforma digital, el acto de mayor R* no es el que escribe el código del algoritmo — es el que define qué objetivo optimiza ese algoritmo. En la plataforma de redes sociales que amplifica contenido emocionalmente polarizador porque ese contenido produce mayor engagement, el diseñador de la métrica de engagement (el ejecutivo que decidió que "engagement" = "tiempo en pantalla" o "reacciones emocionales") tiene R* mayor que el equipo técnico que construyó el modelo. La misma lógica aplica al sistema de recomendación que amplifica contenido de desinformación (la métrica target era clics o tiempo en pantalla, no precisión informativa), al sistema de precios dinámicos que discrimina por código postal (la métrica target era maximizar ingresos, no equidad en el acceso), y al sistema de moderación de contenidos que tiene disparate impact por idioma o cultura (la métrica target definía "contenido dañino" en función de los patrones del dataset de entrenamiento, que sobrerepresentaba idiomas con más datos de moderación histórica).

Taxonomía General de Aplicaciones

Sub-variantes del dominio

Sistemas de recomendación con amplificación de contenido dañino: el algoritmo de recomendación de una plataforma amplificó sistemáticamente contenido que produce daño documentable — desinformación de salud pública, contenido que radicaliza a los usuarios hacia posiciones extremas, material que explota características de vulnerabilidad psicológica. El daño no es del usuario que publicó el contenido: es de la plataforma que lo amplificó mediante la optimización de la métrica de engagement. Nivel C — la causalidad entre la amplificación y el daño downstream es el componente de mayor incertidumbre.

Uso indebido de datos personales y violación de privacidad: la plataforma recopiló datos de comportamiento de usuarios (navegación, preferencias, relaciones sociales) y los usó o comercializó de maneras que los usuarios no autorizaron explícitamente o que excedían el alcance de lo que razonablemente podían anticipar dado el diseño de la interfaz. El R* de la plataforma depende de si el diseño de la interfaz (dark patterns) fue condición causal de que los usuarios no entendieran a qué datos estaban dando acceso.

Discriminación algorítmica en precios, anuncios y acceso a servicios: el algoritmo de precios, de targeting publicitario o de acceso a servicios produjo resultados con disparate impact — cargando más a usuarios de ciertos grupos demográficos, mostrando anuncios de servicios financieros de mayor costo a usuarios de menor ingreso, o negando acceso a vivienda o empleo de manera sistemática a grupos protegidos. El diseñador de la métrica de optimización tiene R* por ese disparate impact cuando el daño era previsible dado el diseño.

Poder de mercado de plataformas y daño competitivo: la plataforma usó su posición dominante y su acceso privilegiado a los datos de los competidores que operan en su ecosistema para darles un trato menos favorable — rebajando el alcance de su contenido, copiando sus productos, o ajustando los

Taxonomía General de Aplicaciones

algoritmos de búsqueda para favorecer los propios servicios. El R* de la plataforma en el daño a los competidores depende de la documentación de las decisiones algorítmicas que produjeron ese trato diferencial.

Daño a menores por diseño: la plataforma diseñó mecanismos de engagement — notificaciones, likes, métricas de popularidad, ciclos de recompensa variable — que son funcionalmente adictivos, aplicados a usuarios menores sin las salvaguardas necesarias. El R* de la plataforma es alto cuando el diseño de esos mecanismos era su decisión deliberada y cuando había evidencia disponible de sus efectos en el bienestar de menores antes de su implementación a escala.

Responsabilidad de la plataforma por contenidos de terceros: la plataforma hospeda, indexa, o amplifica contenido de terceros que produce daño — difamación, violación de derechos de autor, material de abuso sexual de menores. La distribución de R* entre el creador del contenido y la plataforma depende de si la plataforma tenía conocimiento del contenido dañino y de si la arquitectura de moderación era adecuada para detectarlo a la escala de su operación.

### §2  Escala de evidencia PD0–PD8 · Plataformas digitales y economía de datos

La escala PD0–PD8 traduce la jerarquía general E0–E8 al vocabulario de las plataformas digitales. Su característica más relevante es la posición central de la auditoría algorítmica (PD2) — el instrumento que establece la cadena causal entre las decisiones de diseño de la plataforma y los resultados dañinos en los usuarios. Sin auditoría algorítmica, la mayoría de las aristas del grafo de la plataforma permanecen en PD5/PD6, porque las decisiones de diseño de las métricas y los algoritmos raramente se documentan en registros públicos. Nivel C — rangos candidatos, pendientes de calibración empírica formal.

Taxonomía General de Aplicaciones

Descripción y ejemplos en el

Rango w (candidato

Nive

Tipo de evidencia

l

dominio de plataformas digitales

)

PD1 Documento interno de la plataforma que establece las decisiones de diseño relevantes

[0.72, 0.90]

Comunicaciones internas (correos, documentos de producto) donde la plataforma tomó las decisiones de diseño de la métrica, del algoritmo o de la política de datos; documentación de las pruebas A/B que establecían el efecto de las decisiones de diseño en los usuarios antes de la implementación a escala; actas del comité de ética o de confianza y seguridad que discutieron los riesgos del diseño; registros de la decisión de escalar el sistema sin implementar las salvaguardas recomendadas internamente.

PD2 Auditoría algorítmica independiente o peritaje técnico especializado

[0.62, 0.82]

Análisis pericial que establece: (a) qué métrica optimiza el algoritmo, si esa métrica es la causa próxima del resultado dañino y cuáles eran las alternativas disponibles con menor impacto; (b) análisis de disparate impact del sistema — si los resultados del algoritmo afectan desproporcionadament e a grupos protegidos; (c) reconstrucción de la cadena causal entre el diseño de la plataforma y el daño documentado

Taxonomía General de Aplicaciones

Descripción y ejemplos en el

Rango w (candidato

Nive

Tipo de evidencia

l

dominio de plataformas digitales

)

en los usuarios; (d) análisis del S del modelo: si cualquier modelo competente con la misma métrica y dataset habría producido el mismo resultado.

PD3 Testimonios convergentes de exempleados o investigadores con corroboración documental

[0.48, 0.66]

Declaraciones de múltiples exempleados o investigadores que describen consistentemente las decisiones de diseño y su impacto conocido, con al menos un documento interno consistente. Las whistleblower disclosures como la de Frances Haugen en Facebook (2021) son el caso paradigmático de evidencia PD3 con alto impacto.

PD4 Análisis estadístico del comportamient o del sistema y sus efectos documentados

[0.38, 0.58]

Análisis que muestra que el sistema de la plataforma produce resultados con patrones estadísticamente incompatibles con un sistema neutral — disparate impact documentado, amplificación sistemática de ciertas categorías de contenido, correlación estadística entre el uso del algoritmo y métricas de daño en los usuarios (salud mental,

Taxonomía General de Aplicaciones

Descripción y ejemplos en el

Rango w (candidato

Nive

Tipo de evidencia

l

dominio de plataformas digitales

)

radicalización, desinformación).

PD5 Análisis comparativo del diseño de la plataforma versus estándares del sector o mejores prácticas

[0.28, 0.48]

Documentación de que el diseño de la plataforma se apartaba de las prácticas del sector para ese tipo de sistema, o de que ignoró recomendaciones de organismos técnicos o académicos disponibles al momento del diseño.

PD6 Inferencia estructural por posición de la plataforma en el grafo del daño

[0.18, 0.38]

La plataforma tenía la posición, el control del algoritmo y los datos para haber anticipado el impacto dañino de sus decisiones de diseño, sin documentación directa de que lo anticipó o lo ignoró deliberadamente.

PD7 Correlación temporal entre cambios de diseño y efectos documentados sin análisis causal

[0.07, 0.24]

Los cambios de diseño de la plataforma coinciden temporalmente con cambios en las métricas de daño en los usuarios sin análisis que establezca la cadena causal específica versus factores confusos.

PD8 Especulación sobre el impacto sin documentación del mecanismo

[0.00, 0.12]

Afirmación de que la plataforma causó el daño sin documentación del mecanismo específico ni análisis del sistema.

Taxonomía General de Aplicaciones

Descripción y ejemplos en el

Rango w (candidato

Nive

Tipo de evidencia

l

dominio de plataformas digitales

)

PD0 Ausencia documentada de conexión causal

w = 0.00

Auditoría algorítmica que establece que el resultado dañino no tiene relación causal con el diseño del sistema de la plataforma, o que el diseño de la plataforma era consistente con las mejores prácticas disponibles y el daño era imprevisible dado el estado del conocimiento en el momento del diseño.

La asimetría de información en el dominio de plataformas: el problema del acceso a los datos La mayor parte de la evidencia sobre el impacto de los algoritmos de las plataformas está en manos de la plataforma misma: los logs de actividad de los usuarios, los registros del comportamiento del algoritmo, los resultados de los experimentos A/B y los documentos de diseño son propiedad de la plataforma y raramente están disponibles para investigadores externos. Esa asimetría de información produce una brecha entre la evidencia PD1/PD2 que es la más valiosa para el análisis y la evidencia PD4/PD5 que es frecuentemente la única disponible sin filtraciones internas. El analista debe declarar explícitamente cuándo la calidad de su evidencia está limitada por esta asimetría.

### §3  Los Hijos de Afrodita en el dominio de plataformas digitales

En el dominio de plataformas digitales, los Hijos de Afrodita aplican a los ejecutivos y directivos que tomaron las decisiones de diseño del algoritmo, de la métrica y de la política de datos — no al algoritmo como nodo sin voluntad, no al dataset como nodo técnico, y no al modelo de aprendizaje automático.

Taxonomía General de Aplicaciones

La restricción es la misma que en los cap. 11 (crédito), cap. 12 (quiebra) y cap. 13 de El cálculo (IA y algoritmos): los sistemas técnicos sin voluntad tienen R* pero no tienen Hijos.

### §3.1 Hijos de legibilidad alta en el dominio de plataformas

Qué informa para S del

Firma en el

Error de discrimina

Fuente document

expediente

Hijo

ejecutivo

de la plataforma

ción frecuente

al típica

de plataforma

Anter os

S bajo [0.05, 0.28]. El ejecutivo tomó decisiones deliberadas de diseño sabiendo que producirían daño a usuarios o a terceros, pero las mantuvo porque servían a los objetivos de negocio de la plataforma. La decisión fue genuinament e idiosincrátic a: otros ejecutivos con el mismo conocimient o técnico, el

Documento s internos donde el ejecutivo reconoce el impacto dañino del diseño y decide implementa rlo de todas formas. Resultados de experiment os A/B que mostraban el daño y que el ejecutivo usó para optimizar el engagement en lugar de corregir el diseño. Decisiones de escalar sistemas después de recibir

Correos o documento s internos del ejecutivo durante el período de la decisión. Resultados de experiment os A/B con las métricas de daño medidas. Actas del comité de ética o de confianza y seguridad con las decisiones de la dirección.

Confundir con Potós cuando el ejecutivo siguió las prácticas estándar de la industria en ese período. La pregunta discriminan te: ¿el ejecutivo diseñó específicam ente el mecanismo dañino, o replicó prácticas que eran generalizad as en el sector de plataformas en ese momento?

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en el

Error de discrimina

Fuente document

expediente

Hijo

ejecutivo

de la plataforma

ción frecuente

al típica

de plataforma

mismo rol y la misma información no habrían tomado la misma decisión.

advertencias internas de daño. Respuestas a recomendac iones del equipo de ética que fueron rechazadas.

Potó s

S moderado-alto [0.42, 0.75]. El ejecutivo siguió las prácticas establecidas de la industria de plataformas — "maximizar el engagement ", "crecer los DAUs" — sin cuestionar sus impactos downstream sobre los usuarios. La conducta era deliberada pero no idiosincrátic a: cualquier ejecutivo de plataforma con la misma cultura de

Prácticas de diseño que eran generalizada s en el sector de plataformas en el período. Ausencia de cuestionami ento del modelo de negocio basado en engagement . Cultura de producto que maximizaba métricas de crecimiento sin medir métricas de bienestar de usuarios.

Document os del sector sobre las prácticas estándar. Comparaci ón con las decisiones de diseño de plataformas comparable s en el mismo período. Cultura corporativa del sector tech en el período analizado.

Confundir con Anteros cuando el ejecutivo recibió evidencia específica del daño y la ignoró activament e. Si hay documento s donde el ejecutivo desestimó advertencia s de daño por escrito, Anteros moderado es más preciso que Potós.

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en el

Error de discrimina

Fuente document

expediente

Hijo

ejecutivo

de la plataforma

ción frecuente

al típica

de plataforma

negocio y los mismos KPIs habría tomado las mismas decisiones de diseño.

Fobo s

S moderado-alto [0.55, 0.82]. El ejecutivo implementó diseños dañinos bajo la presión de las métricas de crecimiento, del consejo de administraci ón o de la competencia con otras plataformas. El miedo a quedar rezagado competitiva mente determinó la decisión de priorizar el engagement sobre el bienestar de los usuarios. La presión del entorno era condición

Comunicaci ones que documentan la presión sobre el ejecutivo: objetivos de crecimiento de DAUs, presión del consejo para mantener el ritmo competitivo , comparacio nes explícitas con las métricas de plataformas competidor as que usaban los mismos mecanismos .

Comunicaci ones del ejecutivo con el consejo. OKRs documenta dos de la empresa. Análisis competitiv os internos. Presión documenta da del mercado de capitales sobre el crecimiento de usuarios.

Confundir con Anteros cuando el ejecutivo tenía libertad real para diseñar de manera diferente. Si el análisis de otras plataformas muestra que las alternativas de diseño eran viables sin sacrificar competitivi dad, la presión sistémica no es suficiente para Fobos dominante.

Taxonomía General de Aplicaciones

Qué informa para S del

Firma en el

Error de discrimina

Fuente document

expediente

Hijo

ejecutivo

de la plataforma

ción frecuente

al típica

de plataforma

causal de la decisión.

### §3.2 Hijos de legibilidad baja en el dominio de plataformas

Deimos: puede aparecer en ejecutivos que no comprendían las implicaciones del diseño algorítmico en el bienestar de los usuarios — el director de producto que aprobó el sistema de notificaciones sin comprender los mecanismos de adicción que activaría, o el ejecutivo que no tenía el marco conceptual para interpretar los datos de salud mental que el sistema estaba produciendo. S alto cuando la brecha de conocimiento era genuina y consistente con la formación del ejecutivo. Asignar con nota obligatoria de incertidumbre alta dado el ritmo de evolución del conocimiento en el dominio.

Harmonía en el dominio de plataformas: el ejecutivo, investigador o empleado que reportó internamente (o externamente, como whistleblower) las consecuencias dañinas del diseño a pesar de las consecuencias personales. Las whistleblower disclosures (Frances Haugen / Facebook, 2021) son el patrón canónico de Harmonía en el dominio. α alto. Posible reconocimiento como testigo protegido. El valor de las disclosures para el sistema de justicia trasciende el caso individual: permite construir evidencia PD1 que de otra forma sería inaccesible.

§3.3 El modelo, el dataset y el algoritmo no tienen Hijo — la jerarquía de R* invertida Principio algorítmico de El cálculo de la responsabilidad cap. 13: El modelo tiene S ≈ 1.0 porque cualquier modelo competente entrenado con la misma

Taxonomía General de Aplicaciones

métrica y el mismo dataset habría producido el mismo resultado. Cambiar el modelo no resuelve el problema si la métrica y el dataset permanecen. R*_modelo × (1 − S_modelo) ≈ 0. La reforma regulatoria que se enfoca en la "explicabilidad del modelo" sin abordar la elección de la métrica es análoga a reformar el traductor sin corregir el texto original. La jerarquía de responsabilidad algorítmica en el dominio de plataformas: R*_diseñador_métrica > R*_dataset_histórico > R*_desplegador > R*_modelo. Esta jerarquía invierte la jerarquía de visibilidad: el modelo es el más visible en las auditorías técnicas; el diseñador de la métrica es el menos visible en los documentos públicos. La responsabilidad algorítmica requiere acceso a los documentos de decisión de la métrica, no solo a la especificación técnica del modelo.

### §4  ¿Qué cuenta como asunción (α) en el dominio de plataformas digitales?

α de la plataforma mide lo que la empresa ha hecho concretamente sobre su posición causal: rediseño de la métrica que el algoritmo optimiza para reducir el daño, implementación de auditorías de equidad antes del despliegue, reforma de la política de datos para alinearse con el consentimiento informado real de los usuarios, cooperación con investigadores independientes para establecer el impacto del diseño.

α de la plataforma es completamente independiente del dolo Una plataforma que diseñó deliberadamente mecanismos de engagement que producen daño puede tener α alto si después rediseñó la métrica, implementó salvaguardas verificables y cooperó activamente con reguladores e investigadores. Una plataforma que replicó prácticas del sector sin intención deliberada de dañar puede tener α = 0 si nunca auditó ni reformó sus sistemas una vez que la evidencia del daño era disponible. Los Hijos informan S del diseñador; α mide lo que la plataforma hizo después sobre su posición causal.

Taxonomía General de Aplicaciones

Acción de la

¿Cuenta

para α? Razón Tipo de

plataforma

α

Rediseño de la métrica de optimización para incluir métricas de bienestar además de métricas de engagement

Sí — α estructural alto

Es la acción de mayor impacto causal: actúa sobre el nodo de mayor R* (la métrica). El rediseño verificable de la métrica reduce directamente el R*_plataforma futuro.

Voluntari o o requerid o

Auditoría algorítmica independiente con publicación de los resultados

Sí — α de transparencia

La auditoría independiente reduce la asimetría de información que es el mayor obstáculo para establecer la cadena causal del daño. Su publicación permite la verificación externa.

Voluntari o o requerid o

Implementaci ón de salvaguardas para usuarios menores con mecanismos verificables

Sí — α de protección específica

Las salvaguardas para grupos vulnerables son el α más urgente cuando el daño documentado afecta desproporcionadame nte a menores.

Voluntari o o regulatori o

Apertura de datos a investigadores independiente s para estudiar el impacto del algoritmo

Sí — α de cooperación con la investigación

El acceso a datos para investigadores reduce la brecha PD4/PD6 a PD2, permitiendo establecer la cadena causal con mayor certeza.

Voluntari o

Reforma de la política de privacidad y de los dark patterns de consentimient o

Sí — α de rectificación del diseño de consentimien to

Los dark patterns de consentimiento son una fuente autónoma de R* de la plataforma. Su reforma es α directo

Voluntari o o requerid o

Taxonomía General de Aplicaciones

Acción de la

¿Cuenta

para α? Razón Tipo de

plataforma

α

sobre esa posición causal.

No El pago que suprime la evidencia no es α — es la continuación del daño. Su impacto sobre el R*_neta del diseñador es negativo (reduce α a futuro cuando la supresión se documenta).

—

Pagos a investigadores bajo acuerdo de confidencialid ad que impide la publicación de hallazgos adversos

—

Comunicado de "compromiso con la seguridad de los usuarios" sin cambios de diseño verificables

No modifica α

Declaración sin consecuencia concreta sobre el diseño del sistema. No reduce R*_métrica ni R*_desplegador.

### La escala de α de la plataforma

Nivel Rango

Descripción

observable Indicadores

α

Negación / resistencia activa

### 0.00 – 0.05 La plataforma niega el daño, combate activamente las investigaciones y no ha implementado ningún cambio verificable de diseño.

Sin auditorías externas. Sin rediseño de métricas. Litigación activa contra reguladores e investigadores. Supresión de investigación interna.

Reconocimiento nominal

### 0.06 – 0.20 La plataforma reconoció el

Comunicados de responsabilidad

Taxonomía General de Aplicaciones

Nivel Rango

Descripción

observable Indicadores

α

impacto del daño, pero sin cambios concretos verificables. Comunicados de "bienestar de usuarios" sin rediseño.

publicados. Sin cambios de diseño documentados. Sin acceso a datos para investigadores independientes.

Asunción parcial 0.21 – 0.45 La plataforma implementó algunas salvaguardas menores, abrió acceso limitado a investigadores o ajustó parcialmente el diseño de la métrica.

Algunas salvaguardas para menores implementadas. Acceso limitado a investigadores en condiciones restringidas. Ajustes menores de la métrica sin reforma estructural.

Asunción activa en proceso

### 0.46 – 0.70 La plataforma está implementando reformas sustanciales de diseño con seguimiento verificable y cooperando activamente con reguladores.

Rediseño de la métrica en proceso con métricas de bienestar incorporadas. Auditoría independiente activa con resultados publicados. Apertura sustancial de datos a investigadores.

Asunción funcional

### 0.71 – 0.89 Las reformas de diseño son sustanciales y verificables. Las métricas de daño han caído de manera

Reducción verificable de las métricas de daño post-rediseño. Auditoría independiente con resultados

Taxonomía General de Aplicaciones

Nivel Rango

Descripción

observable Indicadores

α

documentable posterior al rediseño.

positivos publicados. Cooperación activa con reguladores documentada.

Asunción plena 0.90 – 1.00 La plataforma rediseñó la métrica, implementó auditorías permanentes, abrió datos a investigadores y cooperó plenamente con reguladores.

Reforma estructural del diseño verificable. Auditorías permanentes independientes. Datos disponibles para investigación. Cooperación regulatoria documentada.

### §5  Construcción del grafo típico del dominio de plataformas

### La jerarquía del grafo algorítmico de la plataforma

R*_diseñador_métrica > R*_contexto_histórico > R*_dataset > R*_desplegador > R*_modelo Esta jerarquía es el principio más importante del capítulo. El modelo (el código que ejecuta el algoritmo de recomendación o de moderación) tiene S ≈ 1.0 porque es sustituible: cualquier modelo competente con la misma métrica y el mismo dataset habría producido el mismo resultado. Su R*_neta ≈ 0. El diseñador de la métrica tiene S bajo porque la elección de qué variable optimiza el sistema es una decisión normativa entre alternativas con consecuencias distribucionales distintas — no hay una única respuesta técnicamente correcta.

Taxonomía General de Aplicaciones

### Tipos de nodo en el grafo de la plataforma

Tipo Función en el

grafo S típico Ejemplo en el

dominio

Diseñador de la métrica (DM)

El ejecutivo o equipo que tomó la decisión normativa de qué variable optimiza el algoritmo de la plataforma. Es el nodo de mayor R* del grafo. Sus Hijos informan S. Anteros: eligió la métrica sabiendo sus consecuencias dañinas. Potós: siguió las prácticas del sector sin cuestionarlas.

Bajo-moderad o [0.15– 0.55]

El equipo de producto que definió "engagement" como tiempo en pantalla o número de reacciones emocionales. El ejecutivo que decidió usar el historial de clics de los usuarios como proxy del interés sin ajustar por el sesgo de selección. El directivo que aprobó la política de datos que permitía la venta de datos de comportamiento sin consentimiento granular.

Contexto histórico generador del sesgo (CH)

Las estructuras históricas de desigualdad, discriminación o desinformación que generaron los patrones en los datos con los que el algoritmo fue entrenado. Nodo sin voluntad individual con R* positivo.

N/A — no es actor individual

Las prácticas históricas de moderación de contenidos que generaron datasets de entrenamiento con subrepresentació n de ciertos idiomas y culturas. Los patrones históricos de acceso desigual al crédito que

Taxonomía General de Aplicaciones

Tipo Función en el

grafo S típico Ejemplo en el

dominio

Análogo al redlining histórico del cap. 11 (crédito): transmite el sesgo al presente a través del dataset.

informan los datasets de scoring crediticio de la plataforma de pagos.

Dataset de comportamient o (DB)

Los datos de comportamient o de usuarios (clics, tiempo de visualización, interacciones) con los que el algoritmo fue entrenado. Nodo sin voluntad. S depende de si el sesgo del dataset es genérico a cualquier dataset de ese tipo (S alto) o específico de cómo fue recopilado y curado por la plataforma (S bajo).

Variable [0.40– 0.85]

El dataset de clics de los usuarios de YouTube entrenado para el sistema de recomendación. El dataset de moderación histórica de Facebook con subrepresentació n de idiomas no europeos. El dataset de comportamiento de usuarios de TikTok que incluye datos de menores sin salvaguardas de edad.

Desplegador del sistema (DS)

El equipo o ejecutivo que tomó la decisión de desplegar el sistema en producción sobre usuarios reales. R* positivo cuando

Moderad o [0.30– 0.65]

El equipo de ingeniería que desplegó el algoritmo de recomendación a escala sin auditoría de equidad previa. El ejecutivo que aprobó el

Taxonomía General de Aplicaciones

Tipo Función en el

grafo S típico Ejemplo en el

dominio

desplegó sin las auditorías de equidad que el tamaño del impacto requería, o cuando desplegó después de haber recibido evidencia de impacto negativo y no implementó las salvaguardas necesarias.

despliegue del sistema COMPAS a pesar de conocer los problemas de equidad documentados internamente.

Modelo algorítmico (MA)

El sistema de aprendizaje automático que optimiza la métrica usando el dataset. Nodo sin voluntad con S ≈ 1.0. Su R* residual apunta hacia el diseñador de la métrica y el proveedor del dataset.

Muy alto [0.88– 1.00]

El algoritmo de recomendación de YouTube. El sistema de scoring de COMPAS. El sistema de targeting publicitario de Facebook. El modelo de moderación de contenidos de Twitter/X. Su S ≈ 1.0 significa que cambiar el modelo sin cambiar la métrica y el dataset no reduce el daño.

Regulador omisivo (Reg)

La autoridad regulatoria que tenía facultad de establecer estándares de auditoría obligatoria, de

Alto [0.55– 0.85]

La Comisión Europea antes del Digital Services Act. La FTC antes de establecer estándares de

Taxonomía General de Aplicaciones

Tipo Función en el

grafo S típico Ejemplo en el

dominio

acceso a datos para investigadores, o de requisitos de equidad para sistemas de alto impacto, y no los estableció. R* positivo cuando esa omisión fue condición de la continuidad del diseño dañino a escala.

algorithmic accountability. Las autoridades de protección de datos que no investigaron los dark patterns de consentimiento durante años de evidencia acumulada.

Usuarios (U) Los participantes del ecosistema de la plataforma — creadores de contenido, consumidores, anunciantes — cuyo comportamient o retroalimenta el dataset y cuya participación es condición del sistema. R* positivo cuando el usuario publicó contenido dañino deliberadament e. S del usuario es alto cuando el diseño del sistema (amplificación de contenido emocionalment e intenso) hacía inevitable la

Variable — muy alto cuando el diseño amplifica contenid o de terceros [0.70– 0.95]

El usuario que publicó el contenido de desinformación. El creador que produjo contenido de radicalización. El anunciante que colocó publicidad de préstamos predatorios en el targeting de usuarios de bajo ingreso. Su S es alto cuando el algoritmo amplificó el contenido más allá de lo que el usuario habría podido lograr sin el sistema.

Taxonomía General de Aplicaciones

Tipo Función en el

grafo S típico Ejemplo en el

dominio

difusión del contenido dado sus características.

### Configuraciones canónicas del grafo de plataformas digitales

Configuración 1 — Amplificación de contenido dañino por el algoritmo de recomendación DM (métrica: maximizar tiempo en pantalla / engagement emocional, S bajo si la elección era deliberada) → DB (dataset de clics con sesgo hacia contenido emocionalmente intenso) → MA (modelo que aprende que el contenido emotivo maximiza la métrica, S ≈ 1.0) → Amplificación del contenido de desinformación / radicalización → Nf (usuarios) La S ≈ 1.0 del modelo demuestra que cambiar el algoritmo técnico no resuelve el daño si la métrica permanece. La reforma correcta: cambiar la métrica de "engagement emocional" a "calidad informativa" o "bienestar declarado del usuario". El R* del diseñador de la métrica es alto cuando la elección de "engagement emocional" como objetivo era una entre múltiples alternativas técnicamente razonables con consecuencias distintas.

Configuración 2 — Discriminación algorítmica en targeting publicitario DM (métrica: maximizar conversiones / CTR por grupo demográfico) → DB (dataset histórico de comportamiento de usuarios con patrones demográficos sesgados) → MA (modelo que aprende a mostrar anuncios de servicios de mayor costo a grupos de menor ingreso porque ese patrón maximiza el CTR histórico) → Disparate impact sobre grupos protegidos → Nf El análisis de disparate impact PD4/PD2 establece el patrón. La métrica de "maximizar CTR" sin restricciones de equidad es la decisión normativa de mayor R*. La alternativa disponible: métricas de CTR ajustadas por equidad o prohibición de targeting por proxis de características protegidas. R*_diseñador_métrica es alto cuando esa alternativa era técnicamente viable.

Taxonomía General de Aplicaciones

Configuración 3 — Daño a menores por diseño de engagement adictivo DM (métricas de retención de usuarios menores: notificaciones, likes, streaks) → DS (desplegador sin salvaguardas de edad verificadas) → MA (sistema de engagement que activa ciclos de recompensa variable) → Daño documentado al bienestar de menores → Nf En esta configuración, el R* del desplegador es especialmente alto cuando había evidencia científica disponible del impacto de esos mecanismos en el bienestar de menores antes del despliegue. El Hijo del desplegador (Anteros si ignoró deliberadamente la evidencia disponible, Potós si siguió las prácticas estándar del sector sin cuestionarlas) informa S y la culpabilidad subjetiva.

### §6  Preguntas que responde este capítulo

### Nota de calibración: respuestas Nivel C. Ajustar con evidencia empírica específica del caso y del dominio.

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

¿Qué métrica optimiza el algoritmo — es esa la decisión de mayor R*?

Identificar la métrica target del sistema (PD1 si hay documentos internos; PD2 si la auditoría técnica puede reconstruir qué variable el modelo optimiza). Verificar si la elección de esa métrica versus alternativas razonables con menor impacto dañino era una elección normativa o técnicamente forzada.

Declaración B con PD1 de calidad o PD2 con auditoría. Declaración C si la métrica debe inferirse desde el comportamiento del sistema (PD4/PD6).

¿El sistema produce disparate impact — daño desproporcionado

Análisis PD4 de los resultados del sistema por grupos demográficos: ¿hay

Declaración B con PD4 sólido y PD2 que establezca el mecanismo causal.

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

a grupos protegidos?

diferencia estadísticamente significativa en la tasa de resultados desfavorables (denegación de acceso, amplificación negativa, precios altos) entre grupos con características comparables?

Declaración C si el análisis de disparate impact requiere datos que solo la plataforma tiene (PD6).

¿El desplegador tenía evidencia del impacto dañino antes del despliegue — Hijo dominante del desplegador?

PD1 (documentos internos) o PD3 (whistleblower disclosures) que muestren qué evidencia del impacto tenía el desplegador antes de la decisión de escalar. El Hijo dominante (Anteros: ignoró deliberadamente; Potós: siguió prácticas del sector; Deimos: no comprendió las implicaciones) informa S.

Declaración B con PD1/PD3 del período de decisión. Declaración C si la evidencia disponible para el desplegador debe inferirse desde PD5/PD6.

¿El diseño del sistema usa dark patterns de consentimiento para los datos de usuarios?

Análisis PD2/PD5 del diseño de la interfaz de consentimiento: ¿las opciones de privacidad estaban diseñadas para disuadir el ejercicio del control del usuario? ¿El diseño de la interfaz hacía más fácil el consentimiento amplio que la restricción específica?

Declaración B con análisis PD2 de la interfaz. Declaración A si los dark patterns son documentados y reconocidos en el expediente regulatorio.

¿La plataforma tiene posición

Análisis de la posición de mercado de la

Declaración B para el análisis de efectos de

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

dominante que le da R* adicional sobre los efectos de red del daño?

plataforma: cuanto mayor es la cuota de mercado y los efectos de red, mayor es la magnitud del D_total de sus decisiones de diseño — porque más usuarios son afectados por cada decisión algorítmica. El análisis económico PD2 establece los efectos de red y su impacto sobre el D_total.

red con datos de mercado. El impacto de la posición dominante sobre el D_total es un multiplicador del daño individual que el análisis de efectos de red establece.

¿Cuál es el D_total_platafor ma — cómo se escala el daño individual al colectivo?

D_total_plataforma = N_afectados × D_promedio_individu al + D_sistémico_adiciona l. N_afectados y D_promedio_individu al se establecen con la evidencia del dominio primario (credencial algorítmico PD2 + datos de escala de la plataforma). D_sistémico_adiciona l es el daño a la confianza en las instituciones informativas o democráticas que trasciende los casos individuales — siempre Declaración C.

Declaración B para N_afectados × D_promedio si hay datos de escala. Declaración C para D_sistémico_adicion al.

### §7  Traducción de D_total al dominio de plataformas digitales

Taxonomía General de Aplicaciones

En el dominio de plataformas

Componen

Cómo se cuantifica

Nota de calibración

te

digitales

T_invertido (daño directo por decisiones incorrectas del sistema)

Las consecuencias directas y verificables de las decisiones del sistema sobre los usuarios afectados: clasificaciones incorrectas que resultaron en acceso denegado, contenido amplificado que produjo daño documentable a usuarios específicos, datos usados sin consentimient o para fines que causaron daño concreto.

Para cada usuario afectado: aplicar el instrument o del dominio primario (D_vital del cap. 1 si hay restricción de libertad por COMPAS; D_crédito del cap. 11 si hay denegación de crédito; D_salud mental si hay daño psicológico documenta do por peritaje). Luego escalar a N_afectad os.

Nivel C para la estimación de D_promedio_indivi dual en muchos casos del dominio. El peritaje de daño individual en plataformas digitales es una de las fronteras más activas de la investigación en el período de escritura de este capítulo.

T_impedido (oportunida des denegadas durante el período del diseño dañino)

Las oportunidade s de información, conexión, acceso a servicios o participación democrática que el diseño dañino de la plataforma

Análisis del diferencial de acceso entre el grupo afectado y el grupo de referencia durante el período del diseño dañino.

Nivel C. La cuantificación de las oportunidades denegadas por diseño algorítmico discriminatorio es una de las preguntas más abiertas del dominio.

Taxonomía General de Aplicaciones

En el dominio de plataformas

Componen

Cómo se cuantifica

Nota de calibración

te

digitales

negó sistemáticame nte a los usuarios afectados. Para los grupos con disparate impact: el valor de acceso a los servicios que les fue denegado por el diseño discriminatori o.

Escalado al N_afectad os del grupo con disparate impact.

ΔT_trayecto ria (daño sistémico permanente a la información y al bienestar)

El daño permanente a la calidad del debate público (desinformaci ón sistémica), a la confianza en las instituciones democráticas (radicalización algorítmica), o al bienestar de largo plazo de los usuarios (daño psicológico crónico en menores por diseños adictivos). Es el componente de mayor magnitud y

Estudios de largo plazo sobre el impacto de la exposición al sistema de la plataforma en las métricas de bienestar, radicalizaci ón o calidad informativa . Siempre Declaració n C por la dificultad de establecer causalidad versus confusas.

Nivel C en todos los casos. Este componente es candidato prioritario para investigación en la Revista Meriadock.

Taxonomía General de Aplicaciones

En el dominio de plataformas

Componen

Cómo se cuantifica

Nota de calibración

te

digitales

menor certeza.

D_total_plataforma = N_afectados × D_promedio_individual + D_sistémico_adicional El daño de un sistema algorítmico de plataforma tiene la característica de operar a escala que lo distingue de todos los dominios individuales. COMPAS procesó cientos de miles de casos. Los algoritmos de recomendación de las grandes plataformas afectan a millones de usuarios diariamente. El D_total algorítmico tiene dos capas: el daño agregado de todas las decisiones individuales incorrectas (N_afectados × D_promedio_individual, que puede estimarse con Declaración B si los datos de escala están disponibles) y el daño sistémico que trasciende las decisiones individuales (erosión de la confianza en las instituciones, degradación del debate público, efectos de red de la desinformación — siempre Declaración C por la dificultad de establecer causalidad). D_vital_plataforma = D_total / w_ref. La conversión a horas de vida hace visible la magnitud real del daño. Para COMPAS: cada clasificación incorrecta como "alto riesgo" que resultó en detención preventiva o denegación de libertad condicional representó en promedio varios meses de vida en condiciones de reclusión. Multiplicado por los miles de casos afectados con disparate impact racial, D_vital es sustancial y calculable — y su magnitud justifica la urgencia de la reforma algorítmica que el análisis de R* señala.

### §8  Límites del método y errores frecuentes de aplicación

Nota especial: límites más amplios en el dominio de plataformas que en la mayoría de los dominios El dominio de plataformas digitales es el que opera con mayor incertidumbre en el libro. La cadena causal entre las decisiones de diseño de la plataforma y los daños downstream en los usuarios es frecuentemente larga y mediada por múltiples capas: el algoritmo, el comportamiento de los usuarios que retroalimenta el dataset, los efectos de red, y la interacción con el entorno informativo más amplio. La Declaración C es frecuente incluso para el análisis de los nodos más centrales del grafo. El analista que use este capítulo

Taxonomía General de Aplicaciones

en una pretensión formal debe ser especialmente explícito sobre los límites de la cadena causal que puede establecer con certeza.

Límites del método en el dominio de plataformas digitales

Límite 1 — La asimetría de información es estructural y severa. La mayor parte de la evidencia del impacto de los algoritmos de las plataformas está en manos de la plataforma. Sin acceso a los documentos de decisión de la métrica (PD1), al dataset (PD2) y a los resultados de los experimentos A/B internos, el análisis externo opera desde PD4/PD6 — que no produce más que Declaración C para los nodos más críticos del grafo.

Límite 2 — La causalidad en cadenas largas. El daño downstream (radicalización de un usuario específico, deterioro del debate público, impacto en la salud mental de menores) puede tener múltiples causas, de las cuales el algoritmo de la plataforma es solo una. La separación entre el impacto causal del algoritmo y los factores confusos (el historial personal del usuario, el entorno familiar, las condiciones socioeconómicas) es técnicamente muy difícil y raramente produce más que Declaración C.

Límite 3 — La velocidad de evolución del dominio. Los sistemas algorítmicos de las plataformas evolucionan rápidamente. El análisis del diseño de una versión del algoritmo puede no ser aplicable a la versión que estaba en producción en el período del daño analizado. La temporalidad del análisis debe ser especialmente precisa en este dominio.

Límite 4 — La imputación causal de los efectos de red. Los efectos de red de las plataformas amplían el daño de cada decisión individual de diseño: una decisión algorítmica que produce disparate impact afecta no a un usuario sino a millones. Cuantificar la escala del efecto de red con certeza requiere datos de la plataforma raramente disponibles.

Taxonomía General de Aplicaciones

### Errores frecuentes de aplicación

Error Por qué

Consecuenci

a Corrección

ocurre

Atribuir el daño al modelo algorítmico (el código) en lugar del diseñador de la métrica

El modelo es el nodo más visible y técnicament e analizable. El análisis se detiene en el modelo.

R* del diseñador de la métrica = 0 aunque es el nodo de mayor R* del grafo. La reforma que resulta (cambiar el modelo) no resuelve el problema porque el modelo tiene S ≈ 1.0.

Identificar siempre la métrica que el modelo optimiza antes de analizar el modelo. Pregunta clave: ¿qué habría producido el sistema si la métrica fuera diferente? Si la respuesta es "resultados menos dañinos", el diseñador de la métrica tiene R* alto.

Tratar el dataset como el actor de mayor responsabilida d sin remontarse al contexto histórico que lo generó

El dataset es el nodo que "contiene el sesgo" y es más fácil de analizar que las estructuras históricas de desigualdad .

El sesgo se trata como un problema técnico del dataset (que puede resolverse con debiasing técnico) en lugar de un problema estructural de las instituciones que generaron los datos históricos.

El R* del dataset apunta hacia el contexto histórico que lo generó. La corrección técnica del dataset (debiasing) es α del curador del dataset, no una solución al R* del contexto histórico que requiere cambios institucionales más profundos.

Ignorar la posición dominante de la plataforma como

El análisis cuantifica el daño individual sin incorporar

D_total subestimado. La magnitud real del daño de las decisiones de

D_total_platafor ma = N_afectados × D_individual + D_sistémico. Los efectos de red de

Taxonomía General de Aplicaciones

Error Por qué

Consecuenci

a Corrección

ocurre

multiplicador del D_total

los efectos de red de la posición dominante de la plataforma.

diseño de las grandes plataformas no es visible.

la posición dominante multiplican el N_afectados para cada decisión de diseño. Incluirlos en el análisis hace visible la magnitud real del daño de las decisiones algorítmicas a escala.

Usar la "explicabilida d del modelo" como sustituto de la auditoría de la métrica

El regulador o el analista exige que el modelo explique sus decisiones, asumiendo que eso resuelve el problema de equidad.

La explicabilidad del modelo no resuelve el daño si la métrica está sesgada. El modelo puede explicar perfectament e por qué produjo el resultado discriminatori o — esa explicación completa el análisis técnico del modelo sin tocar el R* del diseñador de la métrica.

La auditoría de equidad debe incluir la evaluación de la métrica target, no solo la evaluación técnica del modelo. La pregunta regulatoria correcta no es "¿puede el modelo explicar su decisión?" sino "¿es la métrica que el modelo optimiza justa para todos los grupos afectados?".

### §9  Guía de prioridades de recolección de evidencia

### Nota de uso obligatoria: todas las estimaciones de este capítulo son Nivel C. La cadena causal en el dominio de plataformas digitales es

Taxonomía General de Aplicaciones

especialmente difícil de establecer con certeza sin acceso a los documentos internos de la plataforma. La primera prioridad siempre es identificar qué evidencia PD1 o PD2 está disponible o puede obtenerse — porque sin esa evidencia, el análisis opera desde PD4/PD6 y no puede producir más que Declaración C.

### Tabla de prioridades de recolección de evidencia en plataformas digitales

Si tu incertidu

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce es…

qué pregunt

es…

ar

### 1. ¿Qué métrica optimiza el sistema — el acto de mayor R*?

PD1 (documentos internos de la plataforma que establecen la métrica) o PD2 (auditoría algorítmica que reconstruye la métrica desde el comportamien to del sistema). Sin esta evidencia, el R* del diseñador de la métrica es solo una inferencia PD6.

La métrica target es la decisión normativ a de mayor R*. Sin conocerla , el análisis del grafo es incomple to en su nodo más importan te.

Determin a el actor de mayor R* y la reforma de mayor impacto (incertidu mbre empírica crítica)

¿Hay documen tos de producto que describan los objetivos del algoritmo ? ¿La auditoría técnica puede reconstru ir qué variable el modelo maximiza ? ¿Hay whistlebl ower disclosur es sobre la métrica?

### 2. ¿El sistema

PD4: análisis estadístico de

El disparate

Reduce rango de

¿Hay investiga

Taxonomía General de Aplicaciones

Si tu incertidu

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce es…

qué pregunt

es…

ar

produce disparate impact — evidencia PD4/PD 2?

los resultados del sistema por grupos demográficos con datos públicos o de investigadores con acceso a datos. PD2: auditoría algorítmica que establece el mecanismo causal del disparate impact.

impact es el instrume nto que establece la existencia del daño a escala. Sin ese análisis, el daño individual no es evidencia suficiente del daño sistemátic o de la plataform a.

la arista de daño a grupos protegido s (incertidu mbre empírica)

ción académic a sobre el disparate impact del sistema? ¿Hay datos públicos (HMDA equivalen te, datos de moderaci ón de contenid os) que permitan el análisis? ¿El regulador ha realizado auditorías con acceso a datos?

### 3. ¿El desplegad or tenía evidencia del daño antes de desplegar — Hijo dominant e?

PD1 (documentos internos del período pre-despliegue) o PD3 (whistleblower disclosures como la de Frances Haugen que incluyeron documentos de

La evidencia de qué sabía el desplegad or antes de desplegar es el instrume nto para discrimin ar

Reduce rango de S del desplega dor (incertidu mbre ontológic a)

¿Hay whistlebl ower disclosur es del período? ¿Hay litigación regulatori a que haya producid o

Taxonomía General de Aplicaciones

Si tu incertidu

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce es…

qué pregunt

es…

ar

experimentos A/B internos). Sin esta evidencia, el Hijo del desplegador es Deimos por defecto.

Anteros (dolo) de Potós (negligen cia) de Deimos (ignoranc ia). Esa distinción determin a el tipo de proceso.

documen tos internos? ¿El regulador tiene acceso a documen tos de decisión que pueda comparti r?

### 4. ¿La plataform a usó dark patterns de consenti miento?

PD2: análisis de la arquitectura de la interfaz de consentimient o versus los estándares de UX de privacidad. PD5: comparación con las mejores prácticas del sector para el tipo de dato y usuario.

Los dark patterns son una fuente autónom a de R* de la plataform a que es independ iente del análisis algorítmi co. Son más directame nte documen tables que el R* de la métrica porque la interfaz es pública.

Determin a R* autónom o de la platafor ma por diseño de consenti miento (incertidu mbre empírica)

¿Las opciones de privacida d están diseñadas para disuadir el ejercicio del control? ¿El consenti miento más amplio es más fácil de otorgar que el consenti miento restringid o? ¿Hay diferenci as de tamaño

Taxonomía General de Aplicaciones

Si tu incertidu

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce es…

qué pregunt

es…

ar

de letra, color o posición entre las opciones de privacida d?

### 5. ¿Cuántos usuarios fueron afectados — N_afecta dos para escalar el D_total?

PD4 (datos públicos de escala de la plataforma: usuarios activos, tasa de exposición al sistema) o PD2 (datos internos obtenidos por reguladores o auditorías). N_afectados × D_promedio_i ndividual es la base del D_total escalable.

Sin N_afecta dos, el daño individual no puede escalarse al D_total que establece la pretensió n contra la plataform a. La escala del sistema es lo que convierte el daño individual en daño de responsa bilidad institucio nal.

Establece la escala del D_total (incertidu mbre de escala)

¿Cuántos usuarios están expuesto s al sistema analizado ? ¿Qué porcentaj e de los usuarios del grupo con disparate impact fue afectado? ¿Hay datos públicos de la platafor ma sobre la escala del sistema?

### 6. ¿Cuál es la reforma de mayor impacto

Identificar si la reforma de la métrica es técnicamente

La reforma de la métrica

Establece la política regulatori a de

¿Qué métricas alternativ as están

Taxonomía General de Aplicaciones

Si tu incertidu

Qué buscar /

La evidencia

Qué rango reduce

Por qué funciona

mbre principal

que más la reduce es…

qué pregunt

es…

ar

— el nudge regulatori o?

viable con alternativas documentadas en la literatura (PD2/PD5). La alternativa de métrica con menor impacto negativo y viabilidad técnica comparable es el argumento de política regulatoria más fuerte del capítulo.

tiene mayor ROI que la reforma del modelo o el debiasing del dataset, porque la S ≈ 1.0 del modelo significa que cualquier modelo correcto aprender á el sesgo de una métrica sesgada.

mayor impacto

documen tadas en la literatura de IA responsa ble para ese tipo de sistema? ¿Cuáles tienen evidencia de viabilidad técnica compara ble? ¿Cuáles tienen menor disparate impact documen tado?

### Árbol de decisión en plataformas digitales: ¿qué buscar primero?

### El árbol comienza con la disponibilidad de evidencia PD1/PD2, porque sin esa evidencia el análisis no puede ir más allá de Declaración C para los nodos más críticos del grafo.

¿Hay evidencia PD1 o PD2 disponible — documentos internos o auditoría algorítmica?

Taxonomía General de Aplicaciones

├─ Si NO: el análisis opera desde PD4/PD6. Todas las estimaciones son Declaración C. │

└─  Prioridad: identificar si hay whistleblower disclosures, litigación regulatoria con documentos, o investigación académica con acceso a datos.

· Sin ninguna de esas fuentes: el análisis puede establecer la existencia del disparate impact (PD4) pero no la cadena causal hasta el diseñador de la métrica.

├─ Si SÍ hay PD1/PD2: prioridad 1 — identificar la métrica que el sistema optimiza. │

└─  ¿La métrica elegida era la única técnicamente razonable o había alternativas con menor impacto dañino?

· Si había alternativas → R* del diseñador de la métrica es alto. S dependiente del Hijo (Anteros vs. Potós). · Si la métrica era el estándar del sector → S moderado-alto. R*_neta del diseñador reducido.

├─ Prioridad 2: ¿El sistema produce disparate impact documentable? │

└─  PD4 (análisis estadístico público) → PD2 (auditoría con datos internos).

· Si sí → base del D_total del daño a grupos protegidos con escala N_afectados.

└─ Prioridad 3: ¿El desplegador tenía evidencia del daño antes de desplegar?

└─  PD1 (documentos pre-despliegue) o PD3 (whistleblower).

· Si sí → Hijo dominante del desplegador: Anteros (ignoró deliberadamente) → proceso penal / Potós (siguió prácticas del sector) → responsabilidad civil. · Si no hay evidencia → Deimos por defecto. S alto del desplegador.

Taxonomía General de Aplicaciones

— Fin del Capítulo 17 — Centro Multidisciplinario Meriadock Formación y Asesoría A.C.  · 2026

Taxonomía General de Aplicaciones

