## PARTE VII · Ingeniería y Tecnología

### Capítulo 53
Telecomunicaciones y medios —
responsabilidad de plataformas y redes
Organ. Estru. Model. Educa. Crisi.
Nivel B — aplica el cap. 13 (IA y algoritmos) al dominio de las
plataformas digitales y las redes de comunicación, con énfasis en la
responsabilidad de las plataformas por el contenido que amplifican y los
daños que ese contenido produce. El instrumento central es el INCF del
diseñador del algoritmo de recomendación: quién definió qué métrica de
'engagement' optimizar y con qué consecuencias sobre el tipo de contenido
promovido.
Si tu caso es de responsabilidad de una plataforma por contenido dañino
amplificado, ve a §3. Si es de responsabilidad por desinformación
electoral, ve al cap. 44.
§1 Descripción del subcampo
Las plataformas digitales son el dominio donde el daño
producido por el contenido tiene la misma estructura que el
daño producido por cualquier sistema algorítmico: el
diseñador de la métrica de optimización del algoritmo de
recomendación es el nodo de mayor R* cuando la métrica
elegida produce daño sistemático. La distinción entre las
plataformas del dominio de telecomunicaciones y los sistemas
algorítmicos del cap. 13 es de escala y de naturaleza del daño:
las plataformas amplifican el contenido a escala de millones de
usuarios, y el daño del contenido amplificado puede ser desde
el daño a la salud mental de adolescentes hasta la incitación a
la violencia colectiva.

Taxonomía General de Aplicaciones
El algoritmo de recomendación como nodo de mayor
INCF: la métrica de 'engagement'
El algoritmo de recomendación de las plataformas digitales opera con la
misma estructura que el sistema algorítmico del cap. 13: la métrica target que
el algoritmo optimiza determina el tipo de contenido que se promueve. Si la
métrica es 'engagement' (tiempo de pantalla, interacciones) sin distinción de
calidad del contenido, el algoritmo aprende que el contenido que produce
respuestas emocionales intensas (indignación, miedo, contenido sensacional)
genera más engagement — y lo promueve sistemáticamente. El diseñador de
esa métrica tiene el mayor INCF cuando el daño del contenido amplificado
es la consecuencia predecible de esa elección de diseño.
§2 Escala Cd0–Cd8 en telecomunicaciones y
medios
Tipo de Rango
Nivel Descripción
evidencia w
Cd1 Documentos Los documentos internos [0.70,
internos de la donde los diseñadores del 0.88]
plataforma algoritmo y los ejecutivos de la
sobre el diseño plataforma discutieron el diseño
del algoritmo y de la métrica de optimización y
el conocimiento su relación con el tipo de
de sus efectos + contenido promovido. Las
auditoría externa auditorías externas del
del algoritmo algoritmo con acceso al código.
con acceso al
código
Cd2 Análisis El análisis estadístico del tipo de [0.58,
estadístico del contenido que el algoritmo 0.78]
contenido promueve versus el tipo de
amplificado por contenido que no promueve,
la plataforma con metodología documentada.
con
metodología
documentada +
testimonios bajo
juramento de

Taxonomía General de Aplicaciones
Tipo de Rango
Nivel Descripción
evidencia w
exempleados
con
conocimiento
técnico
Cd3 Investigación Los informes de comités [0.48,
parlamentaria o parlamentarios o agencias 0.66]
regulatoria con reguladoras que tuvieron acceso
acceso a a documentos internos de la
documentos plataforma sobre el diseño del
internos de la algoritmo.
plataforma
Cd4 Análisis El análisis académico del [0.36,
académico del comportamiento del algoritmo 0.54]
tipo de usando datos obtenidos desde
contenido la API pública o de acuerdos de
amplificado investigación con la plataforma.
usando datos de
la API de la
plataforma
Cd0 Auditoría Cd1 La auditoría técnica que w =
que establece establece que el algoritmo no 0.00
que el contenido promovió diferencialmente el
dañino no fue tipo de contenido dañino
amplificado respecto al contenido neutral
diferencialmente equivalente.
por el algoritmo
§3 El caso de referencia: Facebook y Etiopía
(2021)
En 2021, documentos internos de Facebook publicados por
Frances Haugen (la whistleblower de Facebook) revelaron que
ejecutivos de la empresa sabían que el algoritmo de
recomendación amplificaba el contenido de odio y la
desinformación, especialmente en países con recursos de
moderación limitados. En el caso de Etiopía, investigadores

Taxonomía General de Aplicaciones
internos de Facebook documentaron en 2021 que la
plataforma estaba amplificando contenido que incitaba a la
violencia étnica en el contexto de la guerra civil tigriña — y
que la empresa no tenía recursos de moderación suficientes en
amhárico ni en tigriña.
Nodo Actor/Factor INCF S Análisis
N1 Ejecutivos de ~38% 0.32 Los documentos internos
Facebook que muestran que ejecutivos
diseñaron y sabían que el algoritmo
mantuvieron la amplificaba contenido
métrica de dañino y priorizaron el
engagement sin crecimiento del
ajuste por tipo engagement. S
de contenido moderado-bajo: la
elección específica de no
implementar ajustes de
contenido dañino era
idiosincrática de
Facebook del período.
N2 Diseñador del ~25% 0.42 La métrica de
algoritmo de engagement sin
recomendación distinción de calidad era
(métrica de el núcleo del problema.
engagement sin La alternativa —
calidad del optimizar por calidad del
contenido) contenido en lugar de
cantidad del engagement
— estaba disponible
como opción de diseño.
N3 Actores que ~18% 0.72 S alta: otros actores
produjeron el motivados a producir
contenido de contenido de incitación
incitación a la habrían producido
violencia contenido equivalente
dado el sistema de
amplificación disponible.
N4 Reguladores ~10% 0.80 La ausencia de requisitos
(ausencia de regulatorios de auditoría
requisitos de algorítmica era el estándar
auditoría del del período en la mayoría
algoritmo) de jurisdicciones.

Taxonomía General de Aplicaciones
Nodo Actor/Factor INCF S Análisis
N5 Gobierno ~9% 0.85 El conflicto armado
etíope preexistente amplificó el
(contexto de impacto del contenido de
conflicto incitación. El algoritmo
armado que actuó sobre un
amplificó el ecosistema ya en
impacto) conflicto.
§4 La distinción entre el contenido y el
amplificador
La distinción más relevante del dominio de
telecomunicaciones y medios es entre el productor del
contenido dañino (el usuario que publicó el contenido de
incitación, la campaña de desinformación) y el amplificador
del contenido (la plataforma que lo promovió a millones de
usuarios). Esta distinción tiene la misma estructura que la
distinción entre el detonador y la estructura del cap. 43: el
productor del contenido tiene S alta — otro productor habría
publicado contenido equivalente. El amplificador tiene INCF
más alto cuando el diseño del algoritmo fue la condición de
que ese contenido llegara a la escala de audiencia que produjo
el daño.
— Fin del Capítulo 53 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

