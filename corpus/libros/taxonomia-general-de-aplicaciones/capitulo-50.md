PARTE VII · Ingeniería y Tecnología

## Capítulo 50

### Ingeniería civil — responsabilidad en

### fallas de infraestructura

Organ.  Estru.  Model.  Educa.  Crisi.

Nivel B — aplica el cap. 12 de El cálculo de la responsabilidad (Ingeniería de sistemas y confiabilidad) al dominio de la ingeniería civil e infraestructura. El instrumento central es el INCF (Índice de Necesidad Causal del Fallo) aplicado a fallas estructurales: no pregunta '¿qué elemento falló?' sino '¿sin qué decisión de diseño, mantenimiento o regulación el fallo no habría ocurrido a esa escala?'

Si tu caso es de colapso estructural por deficiencia de diseño, ve a §3 caso A. Si es de colapso por mantenimiento diferido, ve a §3 caso B. Para responsabilidad del regulador, ve a §4.

### §1  Descripción del subcampo

La ingeniería civil aplica el mismo patrón estructural del cap. 12 (Challenger / Boeing 737 MAX) a la infraestructura física: el fallo técnico observable (el elemento estructural que cedió, el concreto que se deterioró, el suelo que falló) y la decisión humana que hizo posible ese fallo a esa escala (el diseñador que no incorporó el margen de seguridad adecuado, el inspector que aprobó sin la verificación requerida, el propietario que difirió el mantenimiento sabiendo el riesgo). El nodo de presión del cap. 12 — la presión que anuló la señal de advertencia del ingeniero — tiene su equivalente exacto en la ingeniería civil en la presión de costos, plazos y demanda

Taxonomía General de Aplicaciones

### que produce el diferimiento del mantenimiento y la reducción de los márgenes de seguridad.

El INCF en ingeniería civil: del FTA al grafo de responsabilidad El Fault Tree Analysis (FTA) convencional mide la probabilidad de fallo como función de las probabilidades de fallo de los componentes — es un instrumento hacia abajo, del accidente al componente. El INCF es un instrumento hacia arriba, del componente a la decisión humana: dado que el componente falló, ¿cuál fue la decisión humana que hizo posible que ese componente llegara al umbral de fallo sin que los mecanismos de detección y corrección lo interceptaran?

### §2  Escala de evidencia Cd0–Cd8 en ingeniería civil

Tipo de evidencia en

Descripción Rango

Nivel

w

ingeniería

civil

Cd1 Análisis forense estructural con acceso completo al sitio + planos originales de diseño + registros de mantenimiento e inspección verificados

El análisis pericial de un ingeniero estructural que tuvo acceso al sitio del colapso, a los planos originales de diseño, y a todos los registros de inspección y mantenimiento, con metodología documentada.

[0.72, 0.90]

Cd2 Análisis pericial de segunda parte con acceso parcial al sitio

El análisis pericial de un ingeniero independiente con acceso parcial al sitio y a los materiales recuperados del

[0.62, 0.80]

Taxonomía General de Aplicaciones

Tipo de evidencia en

Descripción Rango

Nivel

w

ingeniería

civil

+ análisis de los materiales recuperados

colapso, incluyendo análisis de laboratorio de los materiales.

Cd3 Informe de la comisión de investigación oficial con acceso completo a los documentos y al sitio

El informe de la comisión de investigación establecida por la autoridad reguladora con acceso completo a los documentos del diseño, el mantenimiento y la inspección.

[0.52, 0.70]

Cd4 Registros de inspección y mantenimiento sin análisis forense del fallo

Los registros documentados de las inspecciones realizadas y del mantenimiento ejecutado, sin el análisis forense que los conecte causalmente con el fallo.

[0.38, 0.56]

Cd5 Testimonios de los inspectores y el personal de mantenimiento sin respaldo documental completo

Las declaraciones del personal que realizó las inspecciones o el mantenimiento, sin los registros documentales completos.

[0.22, 0.40]

Cd0 Análisis forense Cd1 que establece que el fallo fue consecuencia de un evento extraordinario no previsible con el diseño correcto

El análisis pericial que establece que el fallo fue producido por fuerzas fuera del espectro de diseño requerido y que ningún diseño estándar del período habría previsto el evento.

w = 0.00

Taxonomía General de Aplicaciones

### §3  Casos resueltos

Caso A — Champlain Towers South, Surfside FL (24 de junio de 2021): el diferimiento sistemático de la reparación

El edificio residencial Champlain Towers South colapsó el 24 de junio de 2021, matando a 98 personas. El análisis post-colapso estableció que el deterioro estructural del edificio era conocido desde 1981, cuando un informe de ingeniería había identificado problemas significativos en el diseño de la plataforma de la piscina y el parking subterráneo. Un informe de 2018 documentó un «deterioro mayor» del concreto en las estructuras de soporte de la piscina y las áreas del parking. Las reparaciones identificadas en 2018 fueron presupuestadas en $9.1 millones. El proceso de aprobación de las reparaciones fue diferido durante años.

Nodo Actor/Factor INCF S Análisis

N1 Junta de propietarios (diferimiento sistemático de las reparaciones conocidas)

~38% 0.32 INCF alto: la junta tenía información documentada (informe 2018) del deterioro grave y el presupuesto de reparación, y difirió la decisión durante años. S moderado-bajo: el diferimiento de reparaciones de esa magnitud con información documentada era más lento que el estándar de gestión de condominios para deterioro estructural crítico.

N2 Diseño original (deficiencias en el detalle del drenaje de la plataforma)

~25% 0.55 El diseño de la plataforma de la piscina con drenaje deficiente aceleró el deterioro del concreto estructural durante décadas. S moderado: diseños similares del período tenían el mismo problema de drenaje.

Taxonomía General de Aplicaciones

Nodo Actor/Factor INCF S Análisis

N3 Reguladores de construcción de Miami-Dade (falta de inspección obligatoria periódica)

~20% 0.70 Miami-Dade no tenía un programa de inspección obligatoria periódica de edificios de más de 40 años hasta después del colapso. S alto: la mayoría de jurisdicciones del período no tenían ese tipo de programa.

N4 Cambio climático / subsidencia (aceleración del deterioro)

~10% 0.88 El nivel del mar y la subsidencia del suelo aceleraron el deterioro. S altísima: condición ambiental no controlada por ningún actor.

N5 Ingenieros consultores (no escalaron la urgencia de las reparaciones con suficiente fuerza)

~7% 0.65 Los informes técnicos identificaron el deterioro pero sin la urgencia que el INCF del deterioro requería.

El resultado central: el INCF más alto es el de la junta de propietarios — no por el diseño original ni por los reguladores, sino por la decisión de diferir la reparación de un deterioro documentado durante años. El patrón es idéntico al Challenger y el Boeing 737 MAX: la información de riesgo existía, el sistema de decisión no la conectó con el poder de detener el proceso hasta que fue demasiado tarde.

Caso B — Colapso del puente I-35W, Minneapolis (1 de agosto de 2007): el nodo de placa de conexión subestimada

El puente interestatal I-35W sobre el río Mississippi colapsó el 1 de agosto de 2007, matando a 13 personas e hiriendo a 145. La investigación del NTSB estableció que la causa probable era el diseño inadecuado de las placas de conexión del nodo (gusset plates) en el diseño original de 1961, que eran

Taxonomía General de Aplicaciones

demasiado delgadas para las cargas adicionales que el puente había acumulado con las sucesivas modificaciones y el peso adicional del equipo de construcción presente en el puente el día del colapso.

Nodo Actor/Factor INCF S Análisis

N1 Diseñador original (error de diseño en las placas de conexión, 1961)

~35% 0.45 Las placas fueron diseñadas con la mitad del grosor que el cálculo correcto requería. S moderado: los métodos de cálculo del período tenían cierta incertidumbre en ese tipo de detalle, pero la diferencia era sustancial.

N2 MnDOT (no identificó el error en 46 años de inspecciones)

~30% 0.60 El programa de inspecciones no incluía el análisis de los nodos de diseño originales. S moderado-alto: la práctica de inspección del período enfatizaba la condición observable, no el análisis de los supuestos del diseño original.

N3 FHWA (regulador federal) y el proceso de inspección nacional

~18% 0.72 El programa de inspección de puentes del período no requería el recálculo de los supuestos de diseño original cuando el puente acumulaba cargas adicionales.

N4 Equipo de construcción sobre el puente el día del colapso

~12% 0.68 El peso adicional del equipo de construcción (240 toneladas) fue la carga adicional que llevó las placas al punto de fallo. S moderado: cualquier día de construcción equivalente habría producido la misma carga.

Taxonomía General de Aplicaciones

Nodo Actor/Factor INCF S Análisis

N5 Acero corrugado del recubrimiento del camino (carga acumulada no prevista)

~5% 0.80 Las sucesivas capas de asfalto añadidas durante décadas aumentaron el peso del puente más allá del diseño original.

### §4  Preguntas que responde este capítulo

Pregunta Instrumento Nivel de certeza

¿El fallo fue por diseño, mantenimiento o inspección — cuál es el INCF de cada nodo?

Análisis forense que establece la cadena: ¿el diseño original tenía el margen de seguridad correcto? ¿El programa de mantenimiento era adecuado? ¿El programa de inspección detectaría el deterioro con tiempo suficiente para intervenir?

Declaración A con análisis Cd1. Declaración B con Cd2/Cd3.

¿El S del diseñador era alto o bajo — el margen insuficiente era el estándar del período?

Comparación con los códigos de diseño del período y las prácticas documentadas de diseñadores equivalentes.

Declaración B con análisis Cd3/Cd4 del estándar del período.

¿Hubo diferimiento del mantenimiento conocido — cuál es el INCF de la junta propietaria?

Análisis de los registros de inspección y las decisiones de la junta propietaria: ¿había información documentada del deterioro sin acción proporcional?

Declaración A con registros Cd1/Cd4 de las decisiones de la junta.

— Fin del Capítulo 50 —

Taxonomía General de Aplicaciones

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

