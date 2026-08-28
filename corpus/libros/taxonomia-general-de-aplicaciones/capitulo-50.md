## PARTE VII · Ingeniería y Tecnología

### Capítulo 50
Ingeniería civil — responsabilidad en
fallas de infraestructura
Organ. Estru. Model. Educa. Crisi.
Nivel B — aplica el cap. 12 de El cálculo de la responsabilidad
(Ingeniería de sistemas y confiabilidad) al dominio de la ingeniería civil
e infraestructura. El instrumento central es el INCF (Índice de
Necesidad Causal del Fallo) aplicado a fallas estructurales: no pregunta
'¿qué elemento falló?' sino '¿sin qué decisión de diseño, mantenimiento o
regulación el fallo no habría ocurrido a esa escala?'
Si tu caso es de colapso estructural por deficiencia de diseño, ve a §3 caso
A. Si es de colapso por mantenimiento diferido, ve a §3 caso B. Para
responsabilidad del regulador, ve a §4.
§1 Descripción del subcampo
La ingeniería civil aplica el mismo patrón estructural del cap.
12 (Challenger / Boeing 737 MAX) a la infraestructura física:
el fallo técnico observable (el elemento estructural que cedió,
el concreto que se deterioró, el suelo que falló) y la decisión
humana que hizo posible ese fallo a esa escala (el diseñador
que no incorporó el margen de seguridad adecuado, el
inspector que aprobó sin la verificación requerida, el
propietario que difirió el mantenimiento sabiendo el riesgo).
El nodo de presión del cap. 12 — la presión que anuló la señal
de advertencia del ingeniero — tiene su equivalente exacto en
la ingeniería civil en la presión de costos, plazos y demanda

Taxonomía General de Aplicaciones
que produce el diferimiento del mantenimiento y la reducción
de los márgenes de seguridad.
El INCF en ingeniería civil: del FTA al grafo de
responsabilidad
El Fault Tree Analysis (FTA) convencional mide la probabilidad de fallo
como función de las probabilidades de fallo de los componentes — es un
instrumento hacia abajo, del accidente al componente. El INCF es un
instrumento hacia arriba, del componente a la decisión humana: dado que el
componente falló, ¿cuál fue la decisión humana que hizo posible que ese
componente llegara al umbral de fallo sin que los mecanismos de detección y
corrección lo interceptaran?
§2 Escala de evidencia Cd0–Cd8 en ingeniería
civil
Tipo de
evidencia en Rango
Nivel Descripción
ingeniería w
civil
Cd1 Análisis El análisis pericial de un [0.72,
forense ingeniero estructural que tuvo 0.90]
estructural con acceso al sitio del colapso, a los
acceso planos originales de diseño, y a
completo al todos los registros de inspección
sitio + planos y mantenimiento, con
originales de metodología documentada.
diseño +
registros de
mantenimiento
e inspección
verificados
Cd2 Análisis El análisis pericial de un [0.62,
pericial de ingeniero independiente con 0.80]
segunda parte acceso parcial al sitio y a los
con acceso materiales recuperados del
parcial al sitio

Taxonomía General de Aplicaciones
Tipo de
evidencia en Rango
Nivel Descripción
ingeniería w
civil
+ análisis de colapso, incluyendo análisis de
los materiales laboratorio de los materiales.
recuperados
Cd3 Informe de la El informe de la comisión de [0.52,
comisión de investigación establecida por la 0.70]
investigación autoridad reguladora con acceso
oficial con completo a los documentos del
acceso diseño, el mantenimiento y la
completo a los inspección.
documentos y
al sitio
Cd4 Registros de Los registros documentados de [0.38,
inspección y las inspecciones realizadas y del 0.56]
mantenimiento mantenimiento ejecutado, sin el
sin análisis análisis forense que los conecte
forense del causalmente con el fallo.
fallo
Cd5 Testimonios Las declaraciones del personal [0.22,
de los que realizó las inspecciones o el 0.40]
inspectores y el mantenimiento, sin los registros
personal de documentales completos.
mantenimiento
sin respaldo
documental
completo
Cd0 Análisis El análisis pericial que establece w =
forense Cd1 que el fallo fue producido por 0.00
que establece fuerzas fuera del espectro de
que el fallo fue diseño requerido y que ningún
consecuencia diseño estándar del período
de un evento habría previsto el evento.
extraordinario
no previsible
con el diseño
correcto

Taxonomía General de Aplicaciones
§3 Casos resueltos
Caso A — Champlain Towers South, Surfside FL (24 de junio
de 2021): el diferimiento sistemático de la reparación
El edificio residencial Champlain Towers South colapsó el 24
de junio de 2021, matando a 98 personas. El análisis post-
colapso estableció que el deterioro estructural del edificio era
conocido desde 1981, cuando un informe de ingeniería había
identificado problemas significativos en el diseño de la
plataforma de la piscina y el parking subterráneo. Un informe
de 2018 documentó un «deterioro mayor» del concreto en las
estructuras de soporte de la piscina y las áreas del parking. Las
reparaciones identificadas en 2018 fueron presupuestadas en
$9.1 millones. El proceso de aprobación de las reparaciones
fue diferido durante años.
Nodo Actor/Factor INCF S Análisis
N1 Junta de ~38% 0.32 INCF alto: la junta tenía
propietarios información documentada
(diferimiento (informe 2018) del
sistemático de deterioro grave y el
las presupuesto de
reparaciones reparación, y difirió la
conocidas) decisión durante años. S
moderado-bajo: el
diferimiento de
reparaciones de esa
magnitud con información
documentada era más
lento que el estándar de
gestión de condominios
para deterioro estructural
crítico.
N2 Diseño ~25% 0.55 El diseño de la plataforma
original de la piscina con drenaje
(deficiencias deficiente aceleró el
en el detalle deterioro del concreto
del drenaje de estructural durante
la plataforma) décadas. S moderado:
diseños similares del
período tenían el mismo
problema de drenaje.

Taxonomía General de Aplicaciones
Nodo Actor/Factor INCF S Análisis
N3 Reguladores ~20% 0.70 Miami-Dade no tenía un
de programa de inspección
construcción obligatoria periódica de
de Miami- edificios de más de 40
Dade (falta de años hasta después del
inspección colapso. S alto: la mayoría
obligatoria de jurisdicciones del
periódica) período no tenían ese tipo
de programa.
N4 Cambio ~10% 0.88 El nivel del mar y la
climático / subsidencia del suelo
subsidencia aceleraron el deterioro. S
(aceleración altísima: condición
del deterioro) ambiental no controlada
por ningún actor.
N5 Ingenieros ~7% 0.65 Los informes técnicos
consultores identificaron el deterioro
(no escalaron pero sin la urgencia que el
la urgencia de INCF del deterioro
las requería.
reparaciones
con suficiente
fuerza)
El resultado central: el INCF más alto es el de la junta de propietarios
— no por el diseño original ni por los reguladores, sino por la decisión
de diferir la reparación de un deterioro documentado durante años. El
patrón es idéntico al Challenger y el Boeing 737 MAX: la información
de riesgo existía, el sistema de decisión no la conectó con el poder de
detener el proceso hasta que fue demasiado tarde.
Caso B — Colapso del puente I-35W, Minneapolis (1 de
agosto de 2007): el nodo de placa de conexión subestimada
El puente interestatal I-35W sobre el río Mississippi colapsó el
1 de agosto de 2007, matando a 13 personas e hiriendo a 145.
La investigación del NTSB estableció que la causa probable
era el diseño inadecuado de las placas de conexión del nodo
(gusset plates) en el diseño original de 1961, que eran

Taxonomía General de Aplicaciones
demasiado delgadas para las cargas adicionales que el puente
había acumulado con las sucesivas modificaciones y el peso
adicional del equipo de construcción presente en el puente el
día del colapso.
Nodo Actor/Factor INCF S Análisis
N1 Diseñador ~35% 0.45 Las placas fueron
original (error diseñadas con la mitad del
de diseño en grosor que el cálculo
las placas de correcto requería. S
conexión, moderado: los métodos de
1961) cálculo del período tenían
cierta incertidumbre en ese
tipo de detalle, pero la
diferencia era sustancial.
N2 MnDOT (no ~30% 0.60 El programa de
identificó el inspecciones no incluía el
error en 46 análisis de los nodos de
años de diseño originales. S
inspecciones) moderado-alto: la práctica
de inspección del período
enfatizaba la condición
observable, no el análisis
de los supuestos del
diseño original.
N3 FHWA ~18% 0.72 El programa de inspección
(regulador de puentes del período no
federal) y el requería el recálculo de los
proceso de supuestos de diseño
inspección original cuando el puente
nacional acumulaba cargas
adicionales.
N4 Equipo de ~12% 0.68 El peso adicional del
construcción equipo de construcción
sobre el (240 toneladas) fue la
puente el día carga adicional que llevó
del colapso las placas al punto de fallo.
S moderado: cualquier día
de construcción
equivalente habría
producido la misma carga.

Taxonomía General de Aplicaciones
Nodo Actor/Factor INCF S Análisis
N5 Acero ~5% 0.80 Las sucesivas capas de
corrugado del asfalto añadidas durante
recubrimiento décadas aumentaron el
del camino peso del puente más allá
(carga del diseño original.
acumulada no
prevista)
§4 Preguntas que responde este capítulo
Pregunta Instrumento Nivel de certeza
¿El fallo fue por Análisis forense que Declaración A con
diseño, establece la cadena: ¿el análisis Cd1.
mantenimiento diseño original tenía el Declaración B con
o inspección — margen de seguridad Cd2/Cd3.
cuál es el INCF correcto? ¿El programa de
de cada nodo? mantenimiento era
adecuado? ¿El programa de
inspección detectaría el
deterioro con tiempo
suficiente para intervenir?
¿El S del Comparación con los Declaración B con
diseñador era códigos de diseño del análisis Cd3/Cd4 del
alto o bajo — el período y las prácticas estándar del período.
margen documentadas de
insuficiente era diseñadores equivalentes.
el estándar del
período?
¿Hubo Análisis de los registros de Declaración A con
diferimiento del inspección y las decisiones registros Cd1/Cd4 de
mantenimiento de la junta propietaria: las decisiones de la
conocido — ¿había información junta.
cuál es el INCF documentada del deterioro
de la junta sin acción proporcional?
propietaria?
— Fin del Capítulo 50 —

Taxonomía General de Aplicaciones
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

