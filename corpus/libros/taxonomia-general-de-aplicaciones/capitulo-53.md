PARTE VII · Ingeniería y Tecnología

## Capítulo 53

### Telecomunicaciones y medios — responsabilidad de plataformas y redes

Organ.  Estru.  Model.  Educa.  Crisi.

Nivel B — aplica el cap. 13 (IA y algoritmos) al dominio de las plataformas digitales y las redes de comunicación, con énfasis en la responsabilidad de las plataformas por el contenido que amplifican y los daños que ese contenido produce. El instrumento central es el INCF del diseñador del algoritmo de recomendación: quién definió qué métrica de 'engagement' optimizar y con qué consecuencias sobre el tipo de contenido promovido.

Si tu caso es de responsabilidad de una plataforma por contenido dañino amplificado, ve a §3. Si es de responsabilidad por desinformación electoral, ve al cap. 44.

### §1  Descripción del subcampo

Las plataformas digitales son el dominio donde el daño producido por el contenido tiene la misma estructura que el daño producido por cualquier sistema algorítmico: el diseñador de la métrica de optimización del algoritmo de recomendación es el nodo de mayor R* cuando la métrica elegida produce daño sistemático. La distinción entre las plataformas del dominio de telecomunicaciones y los sistemas algorítmicos del cap. 13 es de escala y de naturaleza del daño: las plataformas amplifican el contenido a escala de millones de usuarios, y el daño del contenido amplificado puede ser desde el daño a la salud mental de adolescentes hasta la incitación a la violencia colectiva.

Taxonomía General de Aplicaciones

El algoritmo de recomendación como nodo de mayor INCF: la métrica de 'engagement' El algoritmo de recomendación de las plataformas digitales opera con la misma estructura que el sistema algorítmico del cap. 13: la métrica target que el algoritmo optimiza determina el tipo de contenido que se promueve. Si la métrica es 'engagement' (tiempo de pantalla, interacciones) sin distinción de calidad del contenido, el algoritmo aprende que el contenido que produce respuestas emocionales intensas (indignación, miedo, contenido sensacional) genera más engagement — y lo promueve sistemáticamente. El diseñador de esa métrica tiene el mayor INCF cuando el daño del contenido amplificado es la consecuencia predecible de esa elección de diseño.

### §2  Escala Cd0–Cd8 en telecomunicaciones y medios

Nivel Tipo de evidencia Descripción Rango

w

Cd1 Documentos internos de la plataforma sobre el diseño del algoritmo y el conocimiento de sus efectos + auditoría externa del algoritmo con acceso al código

Los documentos internos donde los diseñadores del algoritmo y los ejecutivos de la plataforma discutieron el diseño de la métrica de optimización y su relación con el tipo de contenido promovido. Las auditorías externas del algoritmo con acceso al código.

[0.70, 0.88]

Cd2 Análisis estadístico del contenido amplificado por la plataforma con metodología documentada + testimonios bajo juramento de

El análisis estadístico del tipo de contenido que el algoritmo promueve versus el tipo de contenido que no promueve, con metodología documentada.

[0.58, 0.78]

Taxonomía General de Aplicaciones

Nivel Tipo de evidencia Descripción Rango

w

exempleados con conocimiento técnico

Cd3 Investigación parlamentaria o regulatoria con acceso a documentos internos de la plataforma

Los informes de comités parlamentarios o agencias reguladoras que tuvieron acceso a documentos internos de la plataforma sobre el diseño del algoritmo.

[0.48, 0.66]

Cd4 Análisis académico del tipo de contenido amplificado usando datos de la API de la plataforma

El análisis académico del comportamiento del algoritmo usando datos obtenidos desde la API pública o de acuerdos de investigación con la plataforma.

[0.36, 0.54]

Cd0 Auditoría Cd1 que establece que el contenido dañino no fue amplificado diferencialmente por el algoritmo

La auditoría técnica que establece que el algoritmo no promovió diferencialmente el tipo de contenido dañino respecto al contenido neutral equivalente.

w = 0.00

### §3  El caso de referencia: Facebook y Etiopía (2021)

En 2021, documentos internos de Facebook publicados por Frances Haugen (la whistleblower de Facebook) revelaron que ejecutivos de la empresa sabían que el algoritmo de recomendación amplificaba el contenido de odio y la desinformación, especialmente en países con recursos de moderación limitados. En el caso de Etiopía, investigadores

Taxonomía General de Aplicaciones

internos de Facebook documentaron en 2021 que la plataforma estaba amplificando contenido que incitaba a la violencia étnica en el contexto de la guerra civil tigriña — y que la empresa no tenía recursos de moderación suficientes en amhárico ni en tigriña.

Nodo Actor/Factor INCF S Análisis

N1 Ejecutivos de Facebook que diseñaron y mantuvieron la métrica de engagement sin ajuste por tipo de contenido

~38% 0.32 Los documentos internos muestran que ejecutivos sabían que el algoritmo amplificaba contenido dañino y priorizaron el crecimiento del engagement. S moderado-bajo: la elección específica de no implementar ajustes de contenido dañino era idiosincrática de Facebook del período.

N2 Diseñador del algoritmo de recomendación (métrica de engagement sin calidad del contenido)

~25% 0.42 La métrica de engagement sin distinción de calidad era el núcleo del problema. La alternativa — optimizar por calidad del contenido en lugar de cantidad del engagement — estaba disponible como opción de diseño.

N3 Actores que produjeron el contenido de incitación a la violencia

~18% 0.72 S alta: otros actores motivados a producir contenido de incitación habrían producido contenido equivalente dado el sistema de amplificación disponible.

N4 Reguladores (ausencia de requisitos de auditoría del algoritmo)

~10% 0.80 La ausencia de requisitos regulatorios de auditoría algorítmica era el estándar del período en la mayoría de jurisdicciones.

Taxonomía General de Aplicaciones

Nodo Actor/Factor INCF S Análisis

N5 Gobierno etíope (contexto de conflicto armado que amplificó el impacto)

~9% 0.85 El conflicto armado preexistente amplificó el impacto del contenido de incitación. El algoritmo actuó sobre un ecosistema ya en conflicto.

### §4  La distinción entre el contenido y el amplificador

La distinción más relevante del dominio de telecomunicaciones y medios es entre el productor del contenido dañino (el usuario que publicó el contenido de incitación, la campaña de desinformación) y el amplificador del contenido (la plataforma que lo promovió a millones de usuarios). Esta distinción tiene la misma estructura que la distinción entre el detonador y la estructura del cap. 43: el productor del contenido tiene S alta — otro productor habría publicado contenido equivalente. El amplificador tiene INCF más alto cuando el diseño del algoritmo fue la condición de que ese contenido llegara a la escala de audiencia que produjo el daño.

— Fin del Capítulo 53 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

