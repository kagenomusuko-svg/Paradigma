PARTE II · Ciencias Económicas y Financieras

## Capítulo 15

### Seguros — fraude, responsabilidad y valoración de

### siniestros

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo Este capítulo tiene dos singularidades estructurales respecto a todos los anteriores. Primera: los Hijos de Afrodita no aplican a ningún nodo del dominio asegurador — el análisis es de sistemas e instrumentos, no de disposiciones individuales de voluntad. Segunda: aparece el Δ_B (déficit de asunción del beneficio del siniestro) como concepto central que no había sido necesario en los dominios anteriores con la misma precisión: describe tanto al asegurado que obtuvo más del siniestro de lo que tenía derecho (fraude al seguro) como a la aseguradora cuyo diseño de póliza contribuyó causalmente al siniestro que compensó (aseguradora predatoria). Si tu prioridad es el análisis de fraude al seguro, lee §4 y §5. Para la valoración de siniestros y la distribución proporcional de la indemnización, ve a §7. Para la prima justa ajustada por causalidad, ve a §4.3. Para la prioridad de evidencia, ve directamente a §9.

### §1  Descripción del subcampo

El seguro es el dominio donde el sistema de imputación causal introduce dos conceptos que los capítulos anteriores no habían necesitado con esta precisión. El primero es la distinción entre el seguro como distribución del riesgo (el

Taxonomía General de Aplicaciones

siniestro es causalmente independiente del contrato: la aseguradora no causó el daño, solo lo redistribuyó entre los asegurados; R*_aseguradora ≈ 0) y el seguro como creación o amplificación de riesgo (el diseño de la póliza modifica los incentivos del asegurado de manera que aumenta la probabilidad del siniestro; R*_aseguradora > 0). El segundo es el Δ_B: la brecha entre el beneficio que un nodo obtuvo del siniestro y lo que asumió de ese beneficio.

La distinción entre ambos tipos de seguro no es nominal: tiene consecuencias sobre la prima justa, sobre la distribución de la indemnización y sobre la responsabilidad de la aseguradora ante el regulador. Cuando el diseño de la póliza incluye sobrecobertura (la suma asegurada supera el valor real del activo), incentiva al asegurado a invertir menos en prevención — porque el costo marginal del siniestro para él es negativo. En ese caso, la aseguradora no es solo el compensador del daño: es un nodo con posición causal en el evento que compensa.

Dos funciones ontológicas del seguro: distribución del riesgo versus creación de riesgo Seguro como distribución del riesgo: el siniestro existía como posibilidad antes de la póliza. La aseguradora lo redistribuye entre los asegurados. R*_aseguradora ≈ 0 en el siniestro. La prima justa es proporcional al riesgo actuarialmente documentado. Seguro como creación (o amplificación) de riesgo: el diseño de la póliza modifica los incentivos del asegurado de manera que aumenta P(siniestro). R*_aseguradora > 0. La prima no puede ser completamente justa en el sentido actuarial porque el contrato mismo contribuye al riesgo que cubre. La aseguradora tiene posición causal en el evento que compensa. Analogía del salvavidas que cobra por rescate: si el salvavidas cobra más por cada rescate que por prevenir el ahogamiento, tiene un incentivo estructural para que haya más ahogamientos. Eso no significa que cause los ahogamientos deliberadamente — significa que el diseño de su sistema de compensación tiene posición causal en la probabilidad del evento que cubre. La aseguradora que diseña una póliza con sobrecobertura tiene la misma posición: su diseño no causa el incendio, pero crea el incentivo que hace el incendio más probable.

Taxonomía General de Aplicaciones

Sub-variantes del dominio

Valoración y ajuste de siniestros: distribución de la indemnización entre los nodos del grafo causal del siniestro. El ajustador de siniestros convencional calcula el daño. El análisis causal establece además quién contribuyó causalmente al siniestro y en qué proporción — lo que determina si la indemnización íntegra procede o si debe reducirse en proporción al R* del asegurado.

Fraude al seguro (Δ_B positivo del asegurado): el asegurado obtuvo más del siniestro de lo que tenía derecho según su posición causal y el valor real del activo. El Δ_B positivo del asegurado es la señal formal del fraude: la diferencia entre la indemnización recibida y el daño causalmente atribuible al asegurado. Puede ocurrir por sobrecobertura (suma asegurada superior al valor real), por exageración del daño (T_invertido declarado superior al real) o por provocación del siniestro (R*_asegurado alto con B_siniestro positivo).

Diseño predatorio de póliza (Δ_B positivo de la aseguradora): la aseguradora diseñó el producto con características que incentivan el siniestro — sobrecobertura sin verificación, suscripción sin revisión adecuada, empresa como beneficiaria sin auditoría — y obtuvo beneficio neto del diseño (primas infladas más margen del diseño permisivo) sin asumir su posición causal. El Δ_B de la aseguradora es la medida de ese beneficio no asumido. No es necesariamente fraude penal, pero sí es la descripción matemática de cómo el diseño del producto extrajo valor a costa de las víctimas del siniestro.

Responsabilidad del diseñador del entorno de riesgo: el propietario de un inmueble, el operador de una instalación industrial o el empleador que diseñó las condiciones físicas bajo las que ocurrió el siniestro. El grafo incluye a ese actor como nodo de diseño del entorno con R* positivo, al regulador que estableció (o no estableció) los estándares de seguridad y a la aseguradora cuya póliza pudo haber modificado los incentivos de prevención.

Taxonomía General de Aplicaciones

Prima justa ajustada por causalidad: la aplicación del principio R* × (1−S) al diseño de primas. La prima actuarialmente justa convencional refleja el riesgo de la clase. La prima ajustada por causalidad refleja la contribución causal idiosincrática del asegurado al riesgo: excluye la fracción del riesgo que es estructural (S alto: cualquier asegurado en ese entorno habría tenido el mismo siniestro) y carga solo la fracción que es genuinamente del asegurado (S bajo, R*_asegurado × (1−S)).

Siniestros de causación múltiple acumulativa: incendios, accidentes industriales, fenómenos climáticos extremos donde múltiples factores contribuyen al daño sin que ninguno sea condición necesaria y suficiente por sí solo. Cuando la condición de la iteración de potencia no se cumple, el análisis de valores de Shapley es el instrumento correcto para distribuir R* entre los factores causales.

### §2  Escala de evidencia S0–S8 · Dominio de seguros

La escala S0–S8 traduce la jerarquía general E0–E8 al vocabulario del dominio asegurador. Su característica más relevante es la combinación del peritaje técnico del siniestro (S2 — la cadena causal física del evento) con el análisis actuarial del diseño de la póliza (S2 — la relación entre el diseño y el incentivo al riesgo moral). Sin ambos, la distribución del R* entre el asegurado, el diseñador del entorno y la aseguradora permanece en S5/S6. Nivel A — rangos derivados por extensión desde los principios del sistema.

Descripción y ejemplos

Nivel Tipo de evidencia

Rango

en el dominio

w

asegurador

S1 Documento directo del siniestro, la póliza

Reporte de siniestro con la descripción del evento; póliza con los términos de cobertura, la suma

[0.74, 0.92]

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

Rango

en el dominio

w

asegurador

y el entorno de riesgo

asegurada y las exclusiones; certificación del valor del activo en el momento de la póliza; inspecciones de seguridad del inmueble o instalación antes del siniestro; comunicaciones entre el asegurado y la aseguradora sobre la valoración del activo; registros de mantenimiento del activo asegurado.

S2 Peritaje técnico del siniestro y análisis actuarial del diseño de la póliza

Peritaje técnico que establece las causas físicas del siniestro y la contribución de cada factor (falla estructural, ausencia de sistemas de supresión, materiales inflamables) con sus respectivos pesos causales; análisis actuarial que establece si la suma asegurada correspondía al valor real del activo y si el diseño de la póliza generaba incentivos al riesgo moral; análisis del Δ_B de la aseguradora mediante la comparación de las primas recaudadas, los siniestros pagados y el efecto del diseño sobre la siniestralidad de la cartera.

[0.65, 0.85]

S3 Testimonios convergentes de testigos del siniestro con corroboración documental

Declaraciones de múltiples testigos del evento (bomberos, inspectores de seguridad, vecinos) que describen consistentemente las condiciones en el momento del siniestro, con al menos un registro técnico consistente. En casos de fraude al seguro:

[0.48, 0.66]

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

Rango

en el dominio

w

asegurador

testimonios de colaboradores que describen cómo el asegurado contribuyó al siniestro o cómo exageró el daño.

S4 Análisis estadístico del comportamiento de la cartera aseguradora

Análisis que muestra que la tasa de siniestralidad de la cartera es estadísticamente incompatible con el riesgo actuarial de la clase de activos asegurados; comparación de la siniestralidad de la cartera con la de carteras comparables del sector; análisis del Δ_B de la aseguradora mediante la comparación de la siniestralidad esperada versus observada controlando por las características del diseño de la póliza.

[0.38, 0.60]

S5 Análisis del diseño de la póliza y de las condiciones del entorno de riesgo

Comparación del diseño de la póliza con los estándares del sector para ese tipo de activo y riesgo; análisis de las condiciones físicas del entorno de riesgo (materiales, sistemas de seguridad, protocolos) versus los estándares aplicables; evaluación del historial de siniestros del asegurado en el período anterior a la póliza.

[0.28, 0.48]

S6 Inferencia estructural por posición del actor en el sistema de riesgo

El asegurado, el diseñador del entorno o la aseguradora tenía la posición, la información y el control para haber

[0.18, 0.38]

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

Rango

en el dominio

w

asegurador

modificado los factores causales del siniestro, sin documentación directa de la decisión específica.

S7 Correlación temporal entre condiciones del activo y siniestro sin análisis causal

El deterioro documentado del activo o las decisiones del asegurado coinciden temporalmente con el siniestro sin análisis técnico que establezca la cadena causal.

[0.07, 0.24]

S8 Fuente única sin corroboración técnica

Un solo testimonio o documento sobre el siniestro sin respaldo en peritaje técnico ni análisis actuarial.

[0.04, 0.16]

S0 Ausencia documentada de conexión causal

Peritaje técnico que establece que el siniestro fue producido exclusivamente por un factor exógeno imprevisible (fuerza mayor) sin ninguna contribución causal de los actores del grafo, o que la conducta del asegurado no tenía posición causal en el siniestro.

w = 0.00

La diferencia entre la actuaría predictiva y el análisis causal atributivo La actuaría convencional calcula probabilidades: dada una clase de riesgo y una historia de siniestros, ¿cuál es la probabilidad de que el siniestro ocurra? Esa probabilidad determina la prima. El análisis causal añade una capa diferente: dado que el siniestro ocurrió, ¿cuánto dependía causalmente de cada factor? La diferencia entre ambas es la diferencia entre predicción (antes del siniestro) y atribución (después del siniestro). La actuaría dice "este tipo de activo tiene P(siniestro) = 2.3% anual". El análisis causal dice "en este siniestro específico, el R* del propietario era 45% y el del regulador era 30%". Ambas preguntas son necesarias y se complementan.

Taxonomía General de Aplicaciones

### §3  Los Hijos de Afrodita no aplican en el dominio asegurador

El dominio de seguros tiene una singularidad estructural que lo distingue de todos los capítulos anteriores de la Parte I y de los capítulos 11-14 de la Parte II: los Hijos de Afrodita no aplican a ningún nodo del análisis. La razón es que los nodos del grafo del siniestro son sistemas, estructuras físicas, contratos e instrumentos — no personas con disposiciones de voluntad en el momento del acto relevante.

Los propietarios del edificio tienen R* alto en el siniestro por las condiciones físicas que diseñaron y mantuvieron — puertas cerradas, ausencia de sistemas de supresión, materiales inflamables acumulados — pero la disposición de voluntad con la que tomaron esas decisiones es irrelevante para el cálculo de R*. Lo que importa es si esas decisiones eran condición causal del siniestro, no si fueron tomadas con Anteros, Potós o Deimos.

Cuándo sí aplica el análisis de Hijos en casos relacionados con seguros El análisis de Hijos aplica en los dominios que se superponen con el asegurador cuando hay responsabilidad individual del diseñador del producto de seguros como directivo de la aseguradora (remitir al cap. 13 — gobierno corporativo), responsabilidad penal del asegurado por fraude deliberado al seguro (remitir al cap. 1 — derecho penal), o responsabilidad del inspector de seguridad que no reportó deficiencias (remitir al cap. 8 — responsabilidad médica por analogía de la omisión del perito). En todos esos casos, el análisis de Hijos del dominio correspondiente se aplica al actor individual, y el análisis causal del dominio de seguros distribuye el R* entre los nodos del siniestro.

S en el dominio asegurador: fungibilidad del factor de riesgo

Taxonomía General de Aplicaciones

### Aunque los Hijos no aplican, S sí aplica con su significado habitual: mide cuánto del riesgo era idiosincrático del asegurado versus estructural del entorno.

Perfil de S

Consecuencia sobre la

Interpretación

del asegurado

prima y la indemnización

S alto del asegurado (≥ 0.60)

Cualquier persona en las mismas condiciones estructurales (mismo entorno físico, mismo sector industrial, misma zona geográfica) habría tenido el mismo siniestro. El riesgo es de la clase o del entorno, no de la persona. La conducta individual del asegurado tuvo poco poder causal sobre el resultado.

La prima diferenciada por comportamiento individual tiene poco fundamento causal. La indemnización íntegra es justa porque el asegurado no fue condición necesaria idiosincrática del siniestro. No hay base para reducción de la indemnización por conducta del asegurado.

S bajo del asegurado (< 0.35)

Las condiciones y decisiones específicas del asegurado (su comportamiento, sus decisiones de mantenimiento, su gestión del riesgo operativo) fueron causalmente determinantes para el siniestro. Otro asegurado en la misma clase de riesgo no habría tenido el mismo resultado.

La prima diferenciada por comportamiento observable tiene fundamento causal. La indemnización puede reducirse en proporción al R*_asegurado × (1−S). Base para cláusulas de franquicia proporcional al comportamiento.

S alto del diseño de la póliza (≥ 0.60)

Cualquier póliza de ese tipo (sobrecobertura, empresa como beneficiaria, suscripción sin revisión médica) habría creado el mismo incentivo al riesgo moral. El problema es de la clase de producto, no del diseñador específico.

La reforma regulatoria debe actuar sobre la clase de producto, no solo sobre la aseguradora específica. La multa mínima disuasoria se calcula sobre el Δ_B de la clase, no del caso individual.

Taxonomía General de Aplicaciones

Perfil de S

Consecuencia sobre la

Interpretación

del asegurado

prima y la indemnización

S bajo del diseño de la póliza (< 0.35)

El diseño específico de esta póliza tenía características idiosincráticas que otros productos del mismo sector no tienen. La sobrecobertura o los incentivos perversos fueron diseñados de manera particular.

El R*_aseguradora es alto. La multa mínima disuasoria se calcula sobre el Δ_B de la póliza específica.

### §4  ¿Qué cuenta como asunción (α) en el dominio asegurador?

α en el dominio asegurador tiene interpretaciones distintas según el nodo, con una característica que no se da en otros dominios: el pago de la indemnización contractual por la aseguradora es α de la obligación contractual, no α de la responsabilidad causal. Cuando el diseño de la póliza contribuyó causalmente al siniestro, la aseguradora que solo paga la indemnización sin reconocer su posición causal tiene α de obligación contractual ≈ 1 pero α de responsabilidad causal ≈ 0.

α en el dominio asegurador

Conducta que

Nodo

sube α Tipo de α

Asegurado Grado de implementació n de medidas preventivas proporcionales a su R*_asegurado × (1−S). α = 0: ninguna medida

Instalar sistemas de supresión de incendios. Mantener el activo en condiciones óptimas. Seguir los protocolos de seguridad. Reportar

Voluntario antes del siniestro / Obligación contractual después

Taxonomía General de Aplicaciones

α en el dominio asegurador

Conducta que

Nodo

sube α Tipo de α

preventiva. α = 1: todas las medidas posibles implementadas dado el R*.

honestamente el siniestro sin exagerar el daño.

Diseñador del entorno

Grado de implementació n de condiciones de seguridad proporcionales al R* del entorno en el riesgo del sector.

Mantener salidas de emergencia despejadas y accesibles. Realizar el mantenimiento de los sistemas de seguridad. Capacitar al personal. Reportar deficiencias al regulador.

Voluntario / Regulatorio

Regulador Grado de implementació n y aplicación efectiva de estándares de seguridad proporcionales al riesgo del sector.

Establecer estándares mínimos adecuados al riesgo. Realizar inspecciones efectivas con consecuencias. Sancionar incumplimiento s. Revisar el marco normativo ante evidencia de siniestralidad sistémica.

Instituciona l

Contractual

Aseguradora — obligación contractual

Pago de la indemnización establecida en la póliza.

Es α de la obligación contractual, no α de la responsabilidad causal. La

Taxonomía General de Aplicaciones

α en el dominio asegurador

Conducta que

Nodo

sube α Tipo de α

aseguradora que solo paga la póliza cumple su contrato pero no asume su posición causal en el siniestro cuando el diseño contribuyó causalmente.

Aseguradora — responsabilida d causal

Reconocimient o de que el diseño de la póliza contribuyó al siniestro y reforma del diseño para eliminar el incentivo al riesgo moral.

Rediseño de la suma asegurada vinculada al valor verificado del activo. Implementación de franquicias proporcionales al R*_asegurado. Auditoría de condiciones de seguridad antes de emitir la póliza. Reforma del sistema de suscripción para los activos de alto riesgo.

Voluntario o requerido

### §4.3 La prima justa ajustada por causalidad

PAC_i = P(siniestro) × E[D_total] × R*_asegurado_i × (1 − S_i) + Carga_administración La prima actuarial convencional es Prima_conv = P(siniestro) × E[D_total] + Carga. Trata a todos los asegurados de la misma clase de riesgo por igual, independientemente de su contribución causal idiosincrática al riesgo. La prima ajustada por causalidad (PAC) descompone el riesgo: R*_asegurado_i × (1−S_i) es la contribución causal idiosincrática del

Taxonomía General de Aplicaciones

asegurado i. Si S = 0.80, el 80% del riesgo es estructural y el 20% es idiosincrático. La prima justa refleja solo el 20%. Cuando el riesgo es principalmente estructural (zona sísmica, sector industrial con condiciones de trabajo peligrosas por deficiencias regulatorias), cobrar una prima alta al asegurado equivale a imputarle la responsabilidad causal del entorno que no creó. Principio actuarial: el riesgo actuarialmente justo es R*_asegurado × (1−S) × D_esperado. La prima que excede ese umbral es una transferencia del costo del riesgo estructural al asegurado individual. Cuando esa transferencia es sistemática para grupos históricamente excluidos de servicios o inversión pública, hay fraude annona en el sistema de seguros: el asegurado paga por el riesgo que no creó.

§4.4 El Δ_B: el beneficio del siniestro no asumido

Δ_B_asegurado y Δ_B_aseguradora: las dos formas del déficit de beneficio Δ_B_asegurado = B_siniestro_asegurado − α_asunción_causal. Δ_B_asegurado positivo alto: el asegurado obtuvo más del siniestro de lo que tenía derecho según su R* de contribución causal. Es la señal del fraude al seguro. La diferencia entre la indemnización y el daño causalmente atribuible al asegurado es el monto del enriquecimiento sin causa. Δ_B_aseguradora = B_primas_total + B_diseño_incentivo − α_reconocimiento_R*. Δ_B_aseguradora positivo alto: la aseguradora obtuvo beneficio neto del diseño que incentivó el siniestro. No lo asumió. No es necesariamente fraude en el sentido penal, pero es la descripción matemática de cómo el diseño del producto extrajo valor a costa de las víctimas del siniestro. La multa regulatoria proporcional debe ser al menos Δ_B_aseguradora / P(detección) para que el sistema de incentivos rompa el diseño predatorio.

La escala de α en el dominio asegurador

Taxonomía General de Aplicaciones

Indicadores

Nivel Rango

Descripción

en el expediente

α

observable

Sin medidas preventivas / obstrucción del ajuste

### 0.00 – 0.05 El nodo no implementó ninguna medida preventiva proporcional a su R*, obstruyó el proceso de ajuste del siniestro o exageró el daño declarado.

Sin sistemas de seguridad instalados. Sin mantenimiento documentado. Daño declarado excede el daño real documentado por el peritaje.

Medidas mínimas sin proporcionalidad al R*

### 0.06 – 0.20 El nodo implementó algunas medidas de seguridad estándar de la clase, sin acción específica proporcional a su R* individual en el riesgo.

Sistemas de seguridad básicos instalados. Sin mantenimiento actualizado. Declaración honesta del daño sin acciones preventivas adicionales.

Medidas parciales proporcionales al R*

0.21 – 0.45 El nodo implementó medidas preventivas que redujeron significativamente su R* pero no lo eliminaron. La aseguradora rediseñó parcialmente el producto predatorio.

Sistemas de seguridad mejorados documentados. Suma asegurada revisada parcialmente. Franquicia implementada pero no proporcional al R*.

Asunción activa en proceso

### 0.46 – 0.70 El nodo está en proceso activo de implementación de medidas proporcionales a su R* con

Plan de mejoras de seguridad documentado en ejecución. Rediseño del producto en curso.

Taxonomía General de Aplicaciones

Indicadores

Nivel Rango

Descripción

en el expediente

α

observable

seguimiento verificable.

Cooperación activa con el regulador.

Asunción funcional

### 0.71 – 0.89 Las medidas implementadas son proporcionales a la mayor parte del R* del nodo. El Δ residual es pequeño.

Sistemas de seguridad proporcionales al riesgo del sector instalados y verificados. Suma asegurada vinculada al valor verificado. Siniestralidad de la cartera normalizada.

Asunción plena 0.90 – 1.00 El nodo implementó todas las medidas proporcionales a su R*, eliminó el incentivo al riesgo moral (en el caso de la aseguradora) y cooperó plenamente con el regulador.

Auditoría de seguridad aprobada. Diseño de póliza reformado con Δ_B ≈ 0. Cooperación plena documentada.

### §5  Construcción del grafo típico del dominio asegurador

### Tipos de nodo en el grafo del siniestro

Taxonomía General de Aplicaciones

Tipo Función en el

grafo S típico Ejemplo en el

dominio

Diseñador del entorno de riesgo (DE)

El actor que diseñó y mantuvo las condiciones físicas bajo las que ocurrió el siniestro: el propietario del inmueble, el operador de la instalación industrial, el empleador. Es el nodo de mayor R* en la mayoría de los siniestros laborales e industriales cuando las condiciones del entorno eran la causa dominante.

Variable [0.15–0.70]

Los propietarios de la Triangle Shirtwaist Factory que cerraron las puertas de emergencia con llave y no instalaron sistemas de supresión. El operador de la plataforma petrolera que no implementó los protocolos de seguridad requeridos. El propietario del edificio con instalaciones eléctricas deficientes no mantenidas.

Asegurado (A)

El titular de la póliza cuya conducta o cuyas decisiones de mantenimiento y gestión del activo tienen posición causal en el siniestro. En muchos siniestros, el asegurado y el diseñador del entorno son el mismo actor. En seguros de responsabilidad, el asegurado causó daño a terceros.

Variable [0.15–0.80]

El propietario del vehículo cuya conducta produjo el accidente. El empresario cuyas decisiones de gestión del riesgo operativo contribuyeron al siniestro industrial. El asegurado que no realizó el mantenimiento preventivo requerido.

Taxonomía General de Aplicaciones

Tipo Función en el

grafo S típico Ejemplo en el

dominio

Regulador omisivo (Reg)

La autoridad regulatoria que estableció estándares de seguridad insuficientes para el sector o que no los hizo cumplir. R* positivo cuando el marco normativo inadecuado fue condición necesaria del siniestro a esa escala.

Moderado-alto [0.45– 0.80]

El regulador de edificios que no exigía salidas de emergencia accesibles en edificios de cierta altura. El regulador de la industria química que no inspeccionó las instalaciones. El regulador del sector financiero que no exigió due diligence de valoración en los productos de seguro.

Aseguradora (As)

La entidad que diseñó la póliza. R* positivo cuando el diseño de la póliza modificó los incentivos del asegurado de manera que aumentó P(siniestro). Nodo causal sin el rol activo del diseñador del entorno, pero con posición estructural en el incentivo al riesgo moral.

Moderado [0.30–0.65] para el diseño predatorio específico / Alto para la clase de producto

La aseguradora que diseñó la póliza con sobrecobertura sin verificación del valor real del activo. La aseguradora que emitió seguros de vida colectivos de empleados clave sin revisión médica en el rango de sumas relevantes.

Factor ambiental (FA)

Los factores físicos del entorno que contribuyeron al siniestro sin ser controlables por

Muy alto [0.80–0.99]

El terremoto que derrumbó el edificio. El rayo que inició el incendio en el bosque. La

Taxonomía General de Aplicaciones

Tipo Función en el

grafo S típico Ejemplo en el

dominio

ningún actor: condiciones climáticas extremas, actividad sísmica, degradación natural de materiales. S muy alto. R* bajo porque cualquier actor en ese entorno habría tenido el mismo siniestro.

tormenta que hundió el barco. El envejecimiento natural del cableado que produjo el cortocircuito.

### Configuraciones canónicas del grafo asegurador

Configuración 1 — Siniestro con diseñador del entorno de alto R* (Triangle Shirtwaist) DE (propietarios, condiciones idiosincráticas del entorno: R* ~45%, S ~0.22) + Reg (marco normativo inadecuado: R* ~30%, S ~0.65) + As (sobrecobertura, incentivo al riesgo moral: R* ~12%) + FA (materiales inflamables: R* ~4%) → Siniestro → Nf (146 víctimas) AD_DE = 0.45 × D_total = $317M USD (2024). Los propietarios pagaron efectivamente < $20,000 USD. Δ_N1 = +0.45 en toda su magnitud. J_Triangle ≈ 0.12: injusticia estructural severa. La lección del caso: el análisis causal no necesita el dolo para establecer el R* del propietario. Sus decisiones de diseño del entorno eran condición necesaria del colapso a esa escala, independientemente de si sabían o no que las puertas estaban cerradas en ese momento.

Configuración 2 — Diseño predatorio de póliza (Δ_B de la aseguradora) As (diseño: suma asegurada inflada + empresa como beneficiaria + suscripción sin revisión médica: R* ~42%, S ~0.30) + A (empresas aseguradas que aprovecharon el diseño: R* ~30%) + Reg (omisión

Taxonomía General de Aplicaciones

regulatoria: R* ~18%) → Siniestralidad anómala → Nf (sistema de seguros y asegurados de la cartera) Δ_B_aseguradora = B_primas_infladas + B_margen_diseño_permisivo − α_reconocimiento. Multa_mínima_disuasoria ≥ Δ_B / P(detección). Si P(detección) = 0.30, la multa mínima disuasoria es ~3.3 × Δ_B — suficientemente alta para que el valor esperado del diseño predatorio sea negativo. Cuando la multa regulatoria < Δ_B / P(detección), la aseguradora tiene incentivo racional para seguir diseñando productos predatorios.

Configuración 3 — Fraude al seguro por el asegurado (Δ_B positivo del asegurado) A (asegurado que provocó o exageró el siniestro: R* alto, S bajo) → Siniestro declarado con B_siniestro > D_real → Indemnización recibida > Daño causalmente atribuible al asegurado → Δ_B_asegurado > 0 Señal del fraude: Δ_B_asegurado = Indemnización_recibida − (R*_asegurado × D_total_real). Cuando la suma asegurada supera el valor real del activo (sobrecobertura) y el asegurado tiene posición causal en el siniestro (R* alto, S bajo), el Δ_B es la medida del enriquecimiento sin causa. En fraudes por provocación deliberada del siniestro, Δ_B_asegurado ≈ B_siniestro_completo porque el asegurado diseñó el evento para cobrar la póliza.

### §6  Preguntas que responde este capítulo

Nivel de

Pregunta del

Instrumento que la

certeza posible

caso

responde

¿Cuál es la distribución de R* entre el asegurado, el diseñador del entorno, el regulador y la aseguradora en el siniestro?

Grafo causal del siniestro con los cuatro niveles (del asegurado, del entorno, del diseño regulatorio, del diseño de la póliza). Peritaje técnico S2 que establece las causas físicas y sus contribuciones causales. Análisis actuarial S2 del diseño de la póliza.

Declaración B si el peritaje técnico S2 es de calidad y la suma asegurada versus el valor real del activo está documentada S1. Declaración C si algún nivel del grafo

Taxonomía General de Aplicaciones

Nivel de

Pregunta del

Instrumento que la

certeza posible

caso

responde

requiere inferencia estructural S6.

¿La suma asegurada excedía el valor real del activo — hay sobrecobertura con incentivo al riesgo moral?

Comparación S1/S2 de la suma asegurada con el valor real del activo en el momento de la póliza: tasación independiente del activo versus suma declarada en la solicitud. Si la diferencia supera el umbral de variación actuarialmente razonable, hay sobrecobertura con R*_aseguradora positivo.

Declaración A o B si hay tasación independiente contemporánea a la póliza. Declaración C si la tasación contrafáctica del activo requiere estimación retrospectiva.

¿Hay Δ_B_asegurado positivo — señal de fraude al seguro?

Comparación S1/S2 de la indemnización recibida (o reclamada) con el daño causalmente atribuible al asegurado: D_real × R*_asegurado. Si la primera supera significativamente la segunda, hay Δ_B_asegurado positivo y señal de fraude.

Declaración B si el peritaje técnico establece el D_real con precisión y el R*_asegurado está documentado. Declaración C si el D_real requiere estimación retrospectiva del valor del activo.

¿Hay Δ_B_aseguradora positivo — la aseguradora obtuvo beneficio del diseño que incentivó el siniestro?

Análisis S4 del comportamiento de la cartera: comparación de la siniestralidad observada versus la esperada sin el incentivo del diseño. Cálculo de B_primas_infladas + B_margen_diseño_permisivo − α_reconocimiento.

Declaración B si hay datos de la cartera disponibles para comparar la siniestralidad observada versus la actuarialmente esperada sin el

Taxonomía General de Aplicaciones

Nivel de

Pregunta del

Instrumento que la

certeza posible

caso

responde

diseño. Declaración C si el efecto del diseño sobre la siniestralidad debe inferirse desde S4 sin datos completos de la cartera.

¿Cuál es la prima justa ajustada por causalidad para este tipo de activo?

PAC_i = P(siniestro) × E[D_total] × R*_asegurado_i × (1−S_i). La estimación de R*_asegurado_i y S_i requiere el peritaje técnico S2 del perfil de riesgo idiosincrático del asegurado versus el riesgo estructural del entorno.

Declaración B si el peritaje S2 establece los componentes idiosincráticos y estructurales del riesgo. Declaración C si la separación R*_asegurado / R*_entorno requiere estimación desde S4.

¿Cuántos siniestros adicionales producirá el diseño predatorio antes de la detección regulatoria?

Predictor de siniestros: t_detección = log (θ_ratio / ratio_inicial) / log (1 + crecimiento_anomalía). Si t_detección ≤ 0: el umbral ya fue superado — reporte proactivo inmediato. Si t_detección > 0: N_adicionales = Cartera × (P_diseño − P_actuarial) × t_detección.

Declaración B si hay datos de la cartera para estimar P_diseño versus P_actuarial. Declaración C si las tasas de siniestralidad requieren extrapolación.

### §7  Traducción de D_total al dominio asegurador

Taxonomía General de Aplicaciones

El D_total del siniestro en el dominio asegurador tiene la misma estructura tricomponente de todos los dominios, pero con una característica que lo distingue: la póliza define la cobertura — qué componentes del D_total la aseguradora se comprometió a cubrir. La distribución de la indemnización justa entre los nodos del grafo es proporcional a su R*, no a la cobertura contractual de la póliza.

En el dominio asegurador

Cobertura habitual de

Notas para el análisis causal

Componente

la póliza

T_invertido (pérdida directa del siniestro)

El valor del activo destruido o dañado (para bienes materiales), las lesiones corporales directas (para seguros de personas), la pérdida de ingresos inmediata documentada.

Cubierto típicamente en la mayoría de las pólizas de daños. Es el component e que la póliza cubre de manera más completa.

El valor del activo destruido debe estimarse al valor real en el momento del siniestro, no al valor declarado en la póliza si hay sobrecobertura. El peritaje S2 establece el D_real versus la suma asegurada.

T_impedido (interrupción del negocio / recuperación)

Los ingresos perdidos durante el período de reconstrucció n o recuperación, los costos de instalaciones provisionales, los contratos perdidos durante la interrupción, los gastos de recuperación del estado

Cubierto en pólizas de interrupción del negocio. No siempre incluido en pólizas básicas de daños.

Este componente es frecuentemente subestimado en la valoración convencional del siniestro. Su inclusión completa en el D_total afecta los AD_i de todos los nodos con R* positivo.

Taxonomía General de Aplicaciones

En el dominio asegurador

Cobertura habitual de

Notas para el análisis causal

Componente

la póliza

previo al siniestro.

ΔT_trayectori a (pérdida permanente de potencial)

Para siniestros con víctimas: la pérdida del potencial de ingresos futuros, la discapacidad permanente, la reducción de la esperanza de vida. Para siniestros de negocio: la pérdida de contratos, reputación y posición de mercado que no se recuperan aunque el activo sea reconstruido.

Cubierto en seguros de vida y accidentes personales. Raramente cubierto en pólizas básicas de daños materiales.

Es el componente más difícil de estimar y el más frecuentemente excluido de las indemnizaciones . D_vital = ΔT_trayectoria / w_ref cuando hay vidas afectadas. El caso Triangle produce D_vital ≈ 88.2 millones de horas para las 146 víctimas y sus dependientes.

La distribución de la indemnización justa entre los nodos del grafo Indemnización_justa_nodo_i = R*_i × D_total. La indemnización que la aseguradora paga al asegurado no es Indemnización_justa_asegurado = R*_asegurado × D_total (que podría ser menor al pago contractual si R*_asegurado es bajo). Es la indemnización contractual — a menos que el contrato tenga cláusulas de reducción por conducta del asegurado. La distribución de AD_i entre los nodos del grafo establece la responsabilidad de compensación de cada nodo en la cadena causal. En el caso Triangle: AD_DE = 0.45 × $705M = $317M. La aseguradora pagó la póliza íntegra ($445K en 1911 ≈ $13.8M de 2024) y cobró sus primas. Los propietarios pagaron < $20,000 en indemnizaciones netas. La diferencia entre el D_total calculado y lo que efectivamente asumió cada nodo es la

Taxonomía General de Aplicaciones

medida de la injusticia estructural del sistema de distribución de responsabilidades: J_Triangle ≈ 0.12.

### §8  Límites del método y errores frecuentes de aplicación

Límites del método en el dominio asegurador

Límite 1 — Siniestros de causación múltiple acumulativa: muchos siniestros tienen causas múltiples que contribuyen simultáneamente sin que ninguna sea condición necesaria y suficiente por sí sola. En esos casos, la condición de irreductibilidad de la matriz W puede no cumplirse. El análisis de valores de Shapley — desarrollado en la Parte IV de El cálculo de la responsabilidad — ofrece la solución para los siniestros de causación múltiple acumulativa.

Límite 2 — La causalidad contrafáctica en el seguro de vida: la pregunta "¿habría muerto sin ese factor causal?" es frecuentemente incontestable con certeza individual. La actuaría maneja esta incertidumbre estadísticamente, pero el análisis causal individual requiere un contrafáctico que a veces no existe. El sistema recomienda trabajar con rangos de R* y análisis de sensibilidad en lugar de valores puntuales.

Límite 3 — El riesgo de usar R* × (1−S) para discriminar primas injustamente: si S no se estima correctamente y se usa una S baja para cobrar prima alta a un asegurado cuyo riesgo es principalmente estructural, se le imputa la responsabilidad del entorno que no creó. El principio de prima justa ajustada por causalidad protege contra ese error solo si la estimación de S es precisa.

Límite 4 — El predictor de siniestros adicionales es una estimación sobre una distribución de probabilidad, no una certeza. Los parámetros del modelo (P_actuarial, P_diseño, t_detección) tienen incertidumbre y deben presentarse con análisis de sensibilidad explícito.

Taxonomía General de Aplicaciones

### Errores frecuentes de aplicación

Error Por qué

Consecuenci

a Corrección

ocurre

Confundir el pago de la indemnizaci ón contractual con la asunción de la responsabili dad causal de la aseguradora

El analista trata el pago de la póliza como α completo de la aseguradora , ignorando que cuando el diseño de la póliza contribuyó al siniestro, la aseguradora tiene una responsabili dad causal adicional.

Δ_B_asegura dora = 0 aunque la aseguradora obtuvo beneficio neto del diseño predatorio. El diseño predatorio permanece sin análisis.

Distinguir α_obligación_contr actual (pago de la póliza) de α_responsabilidad_ causal (reconocimiento del R* del diseño y reforma del producto). Son componentes independientes.

Atribuir el D_total del siniestro al asegurado como base de la indemnizaci ón sin estimar R*_asegura do

El ajustador calcula el D_total y lo usa directament e como base de la indemnizaci ón, sin establecer cuánto del siniestro era causalmente atribuible al asegurado versus al entorno o al regulador.

Indemnizació n sobreestimad a cuando R*_entorno o R*_regulatori o es alto. O infravalorada cuando el asegurado tiene R* bajo y S alto. Decisión de cobertura basada en el daño total, no en la responsabilid ad causal.

AD_asegurado = R*_asegurado × (1−S_asegurado) × D_total es el componente del daño causalmente atribuible al asegurado. Es la base justa para la indemnización y para las cláusulas de reducción por conducta.

Taxonomía General de Aplicaciones

Error Por qué

Consecuenci

a Corrección

ocurre

No incluir el regulador en el grafo cuando el marco normativo fue condición del siniestro

El analista construye el grafo con solo el asegurado, el entorno físico y la aseguradora , sin incluir el marco regulatorio insuficiente como nodo causal.

R* del regulador = 0 aunque el marco normativo inadecuado fue condición necesaria del siniestro a esa escala.

El marco regulatorio (o su ausencia) tiene posición causal en el siniestro cuando los estándares que habría requerido la situación estaban ausentes o no se aplicaban. El regulador es un nodo del grafo con R* positivo proporcional a esa brecha.

Usar Δ_B_asegur ado como único indicador de fraude sin verificar R* y S

El analista detecta que la indemnizaci ón reclamada supera el valor real del activo y concluye fraude sin verificar si el asegurado era condición causal del siniestro.

Falso positivo de fraude cuando el siniestro era causalmente independient e del asegurado (S alto) y la sobrecobertu ra no fue determinante de la conducta del asegurado.

El fraude al seguro requiere: (1) Δ_B_asegurado positivo significativo; (2) R*_asegurado significativo (el asegurado fue condición causal del siniestro o lo exageró); (3) S_asegurado bajo (la conducta era idiosincrática). Si S es alto, la sobrecobertura puede ser un error actuarial, no fraude.

### §9 Guía de prioridades de recolección de evidencia

Si tu prioridad es saber qué buscar primero en un caso asegurador, usa la tabla y el árbol que siguen. La primera decisión siempre es identificar el análisis: valoración del siniestro (distribución del D_total entre los nodos del grafo),

Taxonomía General de Aplicaciones

### fraude del asegurado (Δ_B_asegurado positivo), o diseño predatorio de la aseguradora (Δ_B_aseguradora positivo). Cada análisis tiene prioridades de evidencia distintas.

### Tabla de prioridades de recolección de evidencia aseguradora

Si tu incertidu

Qué buscar /

La evidencia

Por qué funcion

Qué rango reduce

mbre principal

que más la reduce es…

qué pregunta

a

es…

r

### 1. ¿Cuál es el análisis principal — valoración , fraude del asegurado o diseño predatori o?

Identificar el eje del caso: ¿el D_total está disputado o hay indicios de que fue exagerado (fraude del asegurado)? ¿La siniestralidad de la cartera es anómalamente alta (diseño predatorio)? ¿La distribución del R* entre los nodos es la pregunta principal (valoración)?

Cada análisis tiene instrume ntos y evidenci as prioritari as distintas. Confund irlos produce una recolecci ón ineficient e.

Determin a el instrume nto principal y el orden de recolecci ón

¿La suma asegurada excede el valor del activo? ¿El asegurado tiene historial de siniestros anteriores ? ¿La siniestrali dad de la cartera es comparati vamente alta?

### 2. [VALOR ACIÓN] ¿Cuál es la distribuci ón del R* entre los

Peritaje técnico S2 de las causas físicas del siniestro: ¿qué factores fueron condición

Sin el peritaje técnico, los pesos del grafo son inferenci as S6.

Reduce rango de R* de cada nodo (incertidu mbre empírica)

¿Cuáles fueron las causas físicas directas del siniestro? ¿Cuál

Taxonomía General de Aplicaciones

Si tu incertidu

Qué buscar /

La evidencia

Por qué funcion

Qué rango reduce

mbre principal

que más la reduce es…

qué pregunta

a

es…

r

nodos del siniestro?

necesaria del evento?, ¿cuáles lo amplificaron y cuáles fueron exógenos? El peritaje establece los pesos w de las aristas del grafo.

Con él, alcanzan S2 y permiten Declarac ión B.

habría sido la magnitud del siniestro sin la ausencia de sistemas de supresión ? ¿El marco regulatori o exigía condicion es que no se cumplían?

### 3. [FRAUD E DEL ASEGUR ADO] ¿La suma asegurada correspon de al valor real del activo?

Tasación independiente del valor real del activo en el momento de la póliza, comparada con la suma asegurada declarada. Si la diferencia es significativa, hay sobrecobertur a y Δ_B_asegurad o potencial.

La sobrecob ertura es la condició n necesaria para el Δ_B_ase gurado en fraudes por incendio o destrucci ón de activos. Sin establece r el valor real del activo, el

Reduce rango de Δ_B_aseg urado (incertidu mbre empírica crítica)

¿Hay tasación independi ente contempo ránea a la solicitud de la póliza? ¿Hubo ajuste de la suma asegurada inmediata mente antes del siniestro? ¿El valor del activo asegurado excede significati vamente

Taxonomía General de Aplicaciones

Si tu incertidu

Qué buscar /

La evidencia

Por qué funcion

Qué rango reduce

mbre principal

que más la reduce es…

qué pregunta

a

es…

r

análisis del fraude no puede avanzar.

los valores comparab les del mercado?

### 4. [FRAUD E DEL ASEGUR ADO] ¿El asegurado tiene posición causal en el siniestro — R* alto?

Peritaje técnico S2 de la contribución del asegurado al siniestro: ¿las decisiones de mantenimient o, las condiciones de operación o las acciones directas del asegurado fueron condición causal del siniestro? ¿Otros asegurados en la misma clase de riesgo habrían tenido el mismo siniestro?

El Δ_B_ase gurado requiere tanto sobrecob ertura como R*_aseg urado positivo. Si el asegurad o tenía S alto (cualquie r asegurad o en ese entorno habría tenido el mismo siniestro) , la sobrecob ertura es un error actuarial pero no fraude.

Reduce rango de R*_asegu rado y S (incertidu mbre empírica y ontológic a)

¿Hubo fallos de mantenim iento o incumpli mientos de protocolo s de seguridad por parte del asegurado ? ¿Hay historial de conductas de riesgo anteriores document adas? ¿Otros activos de la misma clase, en condicion es similares, han tenido siniestros similares?

### 5. [DISEÑ O PREDAT

Análisis estadístico S4 de la tasa de siniestralidad

Si la siniestral idad es estadístic

Reduce rango de Δ_B_aseg uradora

¿Cuál es la tasa de siniestrali dad de la

Taxonomía General de Aplicaciones

Si tu incertidu

Qué buscar /

La evidencia

Por qué funcion

Qué rango reduce

mbre principal

que más la reduce es…

qué pregunta

a

es…

r

ORIO] ¿La siniestrali dad de la cartera excede la actuarialm ente esperada?

de la cartera comparada con la de carteras del mismo tipo en el sector, controlando por las características de los activos asegurados.

amente incompa tible con el perfil actuarial de la clase de activos, hay una señal de que el diseño del producto está generand o incentivo s al siniestro más allá de lo actuarial mente esperado .

(incertidu mbre empírica)

cartera comparad a con la del sector? ¿Hay concentra ción de siniestros en el segmento de mayor sobrecobe rtura? ¿El diseño del producto tiene característ icas que lo distinguen de los estándares del sector?

### 6. ¿Cuántos siniestros adicionale s producirá el diseño predatori o antes de la detección ?

Predictor de siniestros: comparar ratio_siniestral idad_actual vs θ_detección_r egulatoria. Si ratio ≥ θ → el umbral ya fue superado: reporte proactivo inmediato. Si ratio < θ → calcular t_detección y

Cuando el umbral ya fue superado , cada siniestro adicional aumenta P(investi gación) de manera no lineal. El reporte proactiv

Establece la urgencia del reporte y la estrategia óptima

¿La tasa de siniestrali dad actual supera 1.5 veces la actuarialm ente esperada? Si sí → umbral superado. Si no → ¿cuándo se estima

Taxonomía General de Aplicaciones

Si tu incertidu

Qué buscar /

La evidencia

Por qué funcion

Qué rango reduce

mbre principal

que más la reduce es…

qué pregunta

a

es…

r

N_adicionales .

o es la estrategi a óptima para reducir el Δ_B acumula do.

que lo superará?

### 7. ¿Cuál es la prima justa ajustada por causalidad para el activo?

PAC_i = P(siniestro) × E[D_total] × R*_asegurado _i × (1−S_i). El peritaje S2 establece R*_asegurado _i y S_i. Comparar con la prima actual para identificar si hay transferencia injusta del riesgo estructural al asegurado individual.

La prima ajustada por causalida d refleja solo el riesgo que el asegurad o causó. La diferenci a entre la prima actual y la PAC es la fracción del riesgo estructur al (entorno , regulator io) que está siendo imputad a injustam ente al asegurad o.

Establece la justicia de la prima y el argument o de equidad actuarial

¿Qué porcentaje del riesgo de la clase es estructural (cualquier asegurado en ese entorno lo tiene) versus idiosincrát ico (depende de las decisiones del asegurado específico )?

Taxonomía General de Aplicaciones

Árbol de decisión asegurador: ¿qué buscar primero?

El árbol comienza con la identificación del análisis principal, porque valoración, fraude del asegurado y diseño predatorio de la aseguradora tienen instrumentos y prioridades de evidencia radicalmente distintos.

¿Cuál es el análisis principal?

├─ Análisis A: VALORACIÓN DE SINIESTROS — distribución justa del D_total y la indemnización │

└─  PRIORIDAD 1: Peritaje técnico S2 de las causas físicas del siniestro.

· ¿Qué factores fueron condición necesaria del evento? ¿Cuáles lo amplificaron? · Construir el grafo causal con los cuatro niveles (asegurado, entorno, regulatorio, diseño de póliza). · Indemnización_justa_i = R*_i × D_total para cada nodo con R* positivo.

├─ Análisis B: FRAUDE DEL ASEGURADO — Δ_B_asegurado positivo │

├─  PRIORIDAD 1: Tasación independiente del valor real del activo S1/S2.

· ¿La suma asegurada excede el valor real? → Sobrecobertura.

├─  PRIORIDAD 2: Peritaje técnico S2 de la contribución causal del asegurado.

· ¿R*_asegurado es significativo? ¿S_asegurado es bajo? · Si sí a ambas → Δ_B_asegurado = Indemnización − R*_asegurado × D_real. Fraude verificable. · Si S alto → sobrecobertura sin fraude. Error actuarial en el diseño de la póliza.

Taxonomía General de Aplicaciones

└─ Análisis C: DISEÑO PREDATORIO — Δ_B_aseguradora positivo

├─  PRIORIDAD 1: Análisis estadístico S4 de la siniestralidad de la cartera.

· ¿La siniestralidad excede el umbral actuarialmente esperado para la clase?

├─  PRIORIDAD 2: Comparar ratio_actual vs θ_detección.

· Si ratio ≥ θ → umbral superado. Reporte proactivo inmediato. · Si ratio < θ → calcular t_detección y N_adicionales_esperados.

└─  PRIORIDAD 3: Calcular Δ_B_aseguradora y multa mínima disuasoria.

· Δ_B = B_primas_infladas + B_margen_diseño − α_reconocimiento. · Multa_mínima = Δ_B / P(detección) para romper el incentivo al diseño predatorio.

— Fin del Capítulo 15 — Centro Multidisciplinario Meriadock Formación y Asesoría A.C.  · 2026

Taxonomía General de Aplicaciones

