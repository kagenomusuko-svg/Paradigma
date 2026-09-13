PARTE III · Ciencias de la Salud y Biomédicas

## Capítulo 21

### Epidemiología y salud pública —

### causalidad a escala poblacional

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo Este capítulo es compilación directa del cap. 6 de El cálculo de la responsabilidad (Epidemiología y salud pública). Organiza los conceptos del dominio en la estructura §1–§9 de la Taxonomía y añade la escala EP0– EP8, que es la versión operativa de la escala E0–E8 para el vocabulario epidemiológico. El dominio tiene tres características singulares que lo distinguen de todos los otros capítulos del libro. Primera: los nodos del grafo son tanto personas como estructuras físicas, espacios e instituciones — la bomba de agua, el sistema de alcantarillado, la política de cuarentena son todos nodos con R* real. Segunda: los Hijos de Afrodita aplican únicamente a los superpropagadores con voluntad propia — no a los nodos estructurales. Tercera: el dominio tiene valor tanto retrospectivo (para distribuir responsabilidad) como prospectivo (para diseñar intervenciones). Si tu prioridad es el análisis de responsabilidad institucional, ve a §4 y §7. Para el análisis de superpropagadores, ve a §3. Para el fraude annona epidemiológico, ve a §7. Para la prioridad de evidencia, ve directamente a §9.

### §1  Descripción del subcampo

La epidemiología es el dominio donde el daño se produce a escala poblacional. Un brote epidémico no es el resultado de una sola decisión individual identificable: es la consecuencia

Taxonomía General de Aplicaciones

de la interacción entre nodos de múltiples niveles — individuos infectados, espacios de transmisión, sistemas de vigilancia, políticas de salud pública — que contribuyen causalmente a la escala del daño con pesos muy distintos. La herramienta que el análisis causal aporta a la epidemiología es exactamente la que el dominio necesita y el R₀ convencional no provee: la distribución del peso causal entre los nodos del grafo, que permite identificar qué intervención tiene mayor impacto por unidad de recursos invertida.

El error más frecuente en el análisis epidemiológico — tanto en la investigación académica como en la política pública — es reducir el grafo al nivel individual. Cuando el análisis solo incluye casos de personas infectadas y sus contactos, produce un R* que sobreestima la responsabilidad causal de los casos individuales y subestima o no detecta la responsabilidad del sistema de salud pública. Los brotes de mayor escala en la historia moderna tuvieron siempre nodos estructurales con R* alto que no fueron los casos individuales. John Snow lo demostró en 1854 sin el formalismo matemático: el nodo de mayor R* en el cólera de Broad Street no era ninguno de los 616 muertos ni ninguno de los supervivientes — era la bomba de agua.

El fraude annona epidemiológico: cuando el Estado tiene R* alto y α bajo El fraude annona epidemiológico es la forma específica del incumplimiento del Estado en el dominio de la salud pública: el Estado tiene R* alto en el grafo de un brote (las condiciones que no generó fueron causalmente necesarias para que el brote alcanzara la escala que alcanzó) y su α es bajo (no las generó estando a su alcance hacerlo). El concepto es analíticamente poderoso porque permite distinguir entre brotes que eran inevitables dado el estado del conocimiento y de las tecnologías disponibles (R* del Estado bajo porque no había intervención posible) y brotes que habrían podido ser mucho menores si el Estado hubiera generado las condiciones que estaban a su alcance (R* del Estado alto y Δ positivo). FA_epi = R*_Estado × D_total × (1 − α_Estado) es la medida del fraude annona epidemiológico — la base para calcular la responsabilidad del Estado en demandas colectivas por negligencia en la respuesta y para establecer el presupuesto mínimo de inversión en salud pública que el sistema requiere.

Taxonomía General de Aplicaciones

Sub-variantes del dominio

Análisis de brotes con fuente ambiental identificable (Tipo Snow): el nodo de mayor R* es un factor ambiental o de infraestructura — bomba de agua contaminada, sistema de ventilación deficiente, agua potable sin tratamiento. El grafo tiene estructura relativamente simple con un nodo dominante identificable mediante la variación espacial de los casos. Es el dominio más favorable para el análisis causal retrospectivo porque el contrafáctico es claro: sin ese nodo específico, el brote habría sido radicalmente menor.

Análisis de pandemias con estructura causal compleja (Tipo COVID-19): el grafo incluye nodos en múltiples escalas (molecular, individual, comunitario, nacional, global) y el R* está distribuido entre múltiples nodos con incertidumbre. El análisis debe seleccionar los nodos más relevantes para la pregunta específica. Su mayor valor es distinguir los nodos con Δ positivo significativo (incumplimiento real del sistema) de los nodos donde la incertidumbre genuina del momento de las decisiones limita la atribución de responsabilidad.

Análisis de superpropagadores: el análisis de los nodos individuales de alta transmisión. El instrumento central es el índice de sustituibilidad S del superpropagador: si S es alto (cualquier persona con la misma carga viral en ese mismo entorno habría transmitido igual), la intervención correcta es sobre el entorno, no sobre la persona. Si S es bajo (las características idiosincráticas del superpropagador — su posición en la red de contactos, su actividad laboral, su nivel de exposición — fueron causalmente determinantes), hay más base para la intervención individual.

Análisis de equidad en la respuesta: la distribución del daño del brote entre grupos sociales está determinada no solo por la biología del patógeno sino por las condiciones estructurales que determinan la exposición, el acceso al tratamiento y la capacidad de aislamiento. El análisis de los nodos estructurales (condiciones de trabajo, acceso a cobertura de aislamiento,

Taxonomía General de Aplicaciones

densidad habitacional, acceso a sistemas de salud de calidad) establece qué factores amplifican el daño en los grupos más vulnerables y cuál es el R* del diseñador de esas condiciones en la distribución desigual del daño.

Evaluación de intervenciones de salud pública: el uso prospectivo del análisis causal para establecer qué intervención tiene mayor impacto por unidad de recursos: Impacto_intervención_i ∝ R*_i × (1 − S_i). La intervención sobre el nodo de mayor R* × (1−S) — el nodo de mayor necesidad causal idiosincrática — produce el mayor impacto en la reducción del brote por unidad de recursos invertida.

### §2  Escala de evidencia EP0–EP8  · Epidemiología y salud pública

La escala EP0–EP8 traduce la jerarquía general E0–E8 al vocabulario epidemiológico. Su característica más relevante es la posición central de la secuenciación genómica del patógeno (EP1) y del análisis de brote con variación espacial y temporal (EP2) — los instrumentos que en epidemiología cumplen el rol que la documentación jurídica cumple en los dominios del derecho. La compilación directa de El cálculo de la responsabilidad cap. 6 calibra los rangos empíricamente desde la práctica epidemiológica.

Descripción y ejemplos

Nivel Tipo de evidencia

Rango

en el dominio epidemiológico

w

EP1 Evidencia genómica y de laboratorio directa del patógeno y la transmisión

Secuenciación genómica que vincula directamente las cepas de los casos en una cadena de transmisión; datos de carga viral documentados por laboratorio; cultivos del patógeno que establecen la fuente ambiental; análisis de biología molecular que establece el mecanismo de

[0.74, 0.92]

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

Rango

en el dominio epidemiológico

w

transmisión. Es el instrumento más directo para establecer quién transmitió a quién con certeza molecular.

EP2 Estudio epidemiológico con análisis causal robusto

Estudio de brote con variación espacial y temporal que establece el nodo ambiental de mayor R* (análogo al método de John Snow); análisis multivariado que controla por factores confusos para aislar la contribución causal de un nodo específico; estudio de cohorte con seguimiento que establece el efecto de una intervención de salud pública sobre la tasa de transmisión secundaria; modelamiento epidemiológico con estimación de R* por nodo con intervalos de confianza.

[0.65, 0.85]

EP3 Rastreo de contactos documentado con corroboración de laboratorio

Cadena de transmisión reconstruida mediante rastreo activo de contactos, con al menos corroboración genómica parcial de los eslabones clave. En brotes con múltiples superpropagadores: el análisis de clúster que identifica los nodos de mayor transmisión secundaria con datos de rastreo consistentes entre investigadores.

[0.48, 0.66]

EP4 Análisis estadístico del patrón de casos con control de confusos

Análisis de la distribución espacial y temporal de los casos que establece la asociación entre el nodo analizado y la escala del brote, con control por las

[0.38, 0.58]

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

Rango

en el dominio epidemiológico

w

características demográficas y socioeconómicas de la población afectada; análisis de regresión que establece el impacto de una política de salud pública sobre las tasas de incidencia controlando por la evolución temporal del brote.

EP5 Análisis de la capacidad de respuesta institucional y cronología de decisiones

Documentación de la cronología de las decisiones de salud pública — cuándo se activó la alerta, cuándo se implementaron las medidas de contención, cuándo se comunicó el riesgo — versus la cronología del brote, que establece si las decisiones fueron causalmente tempranas o tardías respecto al momento de mayor impacto posible.

[0.28, 0.48]

EP6 Inferencia desde la estructura del sistema de salud pública y el estado del conocimiento

El sistema de salud pública tenía la posición institucional, los recursos y los instrumentos para haber actuado de manera que habría reducido el daño, dado el estado del conocimiento disponible al momento de las decisiones. Sin documentación directa de las decisiones específicas.

[0.18, 0.38]

EP7 Correlación temporal entre el evento o la decisión y el cambio en la tasa de transmisión

El evento o la decisión coincide temporalmente con el cambio en la tasa de transmisión sin análisis que establezca la cadena causal versus factores confusos.

[0.07, 0.24]

EP8 Fuente única o evidencia

Un solo caso documentado o un testimonio sin

[0.04, 0.16]

Taxonomía General de Aplicaciones

Descripción y ejemplos

Nivel Tipo de evidencia

Rango

en el dominio epidemiológico

w

anecdótica sin corroboración epidemiológica

corroboración epidemiológica sistemática.

EP0 Ausencia documentada de posición causal del nodo en la escala del brote

Análisis EP2 que establece que el resultado del brote habría sido el mismo sin el nodo analizado dado el estado del sistema de transmisión — el nodo era causalmente irrelevante para la escala del daño, o las acciones del actor institucional ya implementaban las mejores prácticas disponibles en el estado del arte del momento.

w = 0.00

R₀ versus R*: instrumentos complementarios para preguntas distintas R₀ (número básico de reproducción) y R* (vector de peso causal) son instrumentos complementarios, no sustitutos. R₀ mide el número promedio de infecciones secundarias en una población totalmente susceptible — es un escalar que describe la dinámica global del brote. R* distribuye el peso causal del brote entre los nodos del grafo — es un vector que establece cuáles nodos son causalmente críticos y cuáles son reemplazables. R₀ alto con R* concentrado en pocos nodos (como en el cólera de 1854 con la bomba de Broad Street) sugiere que intervenir en esos nodos reducirá el brote eficientemente. R₀ alto con R* distribuido (como en COVID-19 con múltiples nodos en múltiples escalas) sugiere que se necesita intervención en múltiples frentes simultáneamente. La correlación entre superpropagación (patrón 80/20 documentado en muchos patógenos) y R* concentrado es directa: un parámetro de dispersión k pequeño en la distribución del número de infecciones secundarias corresponde a R* concentrado en pocos nodos.

Taxonomía General de Aplicaciones

### §3  Firmas documentales por Hijo  ·  Solo aplica a superpropagadores con voluntad propia

En el dominio epidemiológico, los Hijos de Afrodita tienen un alcance más restringido que en todos los demás capítulos del libro: aplican exclusivamente a los superpropagadores identificados con voluntad propia. No se calculan para los nodos estructurales (el sistema de agua, la ventilación del espacio, la política de cuarentena) porque esos nodos no tienen disposición de voluntad individual. No aplican tampoco a la OMS como institución ni al Estado como nodo normativo en el análisis del brote a escala poblacional — esos nodos tienen R* real, α mensurable y Δ calculable, pero sus Hijos pertenecen al análisis de gobierno corporativo de sus directivos (cap. 13) o al análisis de responsabilidad individual (cap. 1).

La distinción más importante que los Hijos aportan al análisis epidemiológico es entre el superpropagador que actuó desde Fobos (miedo a reportar, miedo a perder el empleo si se aísla, miedo al estigma) y el que actuó desde Anteros (negación deliberada de las medidas de protección) o Deimos (parálisis ante la incertidumbre sobre si estaba realmente infectado). Esta distinción cambia radicalmente la política de intervención recomendada.

### Mapa de Hijos de los superpropagadores y sus implicaciones para la política de salud pública

Qué describe

α predicho

Error frecuente

Hijo dominant

Política

de intervenc

en el contexto epidemiol

si la intervenc

de respuesta institucio

e del superprop

ión correcta

ión es adecuada

agador

ógico

nal

Fobos El superprop

Eliminar las

Alto si se eliminan

Sancionar al

Taxonomía General de Aplicaciones

Qué describe

α predicho

Error frecuente

Hijo dominant

Política

de intervenc

en el contexto epidemiol

si la intervenc

de respuesta institucio

e del superprop

ión correcta

ión es adecuada

agador

ógico

nal

agador transmitió porque tenía miedo a las consecuen cias de aislarse: perder el empleo o el ingreso, el estigma de ser identificad o como caso positivo, las consecuen cias laborales del aislamient o. No quiso transmitir: no pudo dejar de hacerlo dadas las condicione s estructural es que el sistema no cambió. El trabajador esencial sin cobertura de días perdidos es el caso

barreras al aislamient o: subsidio de días perdidos, protecció n del empleo, provisión de alojamient o de aislamient o para quienes no pueden aislarse en casa, equipo de protecció n adecuado, canales de reporte anónimos. La sanción al superprop agador con Fobos dominant e refuerza el Fobos y reduce el α futuro.

las barreras estructural es al aislamient o. El α sube cuando el Fobos disminuye , no cuando la sanción aumenta.

superprop agador individual mente en lugar de abordar el nodo estructural (condicion es laborales) que determinó su conducta. Esto produce el resultado más injusto y el menos eficaz: penaliza a quien tenía menos opciones.

Taxonomía General de Aplicaciones

Qué describe

α predicho

Error frecuente

Hijo dominant

Política

de intervenc

en el contexto epidemiol

si la intervenc

de respuesta institucio

e del superprop

ión correcta

ión es adecuada

agador

ógico

nal

paradigmát ico.

Deimos El superprop agador no reconoció sus síntomas como infección, no entendía el protocolo de aislamient o, no tenía acceso al diagnóstic o necesario para confirmar si debía aislarse. No hubo transgresió n deliberada: hubo ausencia del marco que habría permitido actuar diferente.

Acceso fácil y rápido a diagnóstic o. Comunica ción clara sobre síntomas y protocolo de acción. Reducción de las barreras de acceso al sistema de salud. El Deimos se transform a en Harmonía cuando se provee el marco que faltó.

Alto si se provee el marco informativ o y de acceso. El Deimos es la más reformabl e de las disposicio nes: desaparec e con la provisión de estructura adecuada.

Culpabiliz ar al superprop agador por ignorancia cuando el sistema no había generado el acceso al diagnóstic o ni la comunica ción clara. El Deimos del superprop agador tiene un Δ del Estado como espejo: el Estado no generó las condicion es que habrían convertid o al Deimos en Harmonía .

Potós El superprop

Normas de grupo

Moderado -alto con

Tratar el Potós

Taxonomía General de Aplicaciones

Qué describe

α predicho

Error frecuente

Hijo dominant

Política

de intervenc

en el contexto epidemiol

si la intervenc

de respuesta institucio

e del superprop

ión correcta

ión es adecuada

agador

ógico

nal

agador siguió las normas sociales y los comporta mientos previos a la pandemia sin integrar la informació n nueva sobre el riesgo. La inercia comporta mental determinó la conducta: asistió al evento social, siguió con su rutina, no actualizó su comporta miento porque el campo cultural de su entorno social tampoco había actualizado .

que hacen que el aislamient o y la protecció n sean el comporta miento esperado socialmen te, no la excepción. Los incentivos positivos para la cooperaci ón son más eficaces que las sanciones. La comunica ción que reformula las medidas como norma de grupo reduce el Potós.

intervenci ones de norma social. El Potós responde al campo cultural más que a las sanciones individual es.

como Anteros e imponer sanciones que alienan a la comunida d y reducen la cooperaci ón futura. O tratar el Potós como Deimos e ignorar que la persona sí tenía informaci ón disponible — solo que el campo social no la había integrado.

Taxonomía General de Aplicaciones

Qué describe

α predicho

Error frecuente

Hijo dominant

Política

de intervenc

en el contexto epidemiol

si la intervenc

de respuesta institucio

e del superprop

ión correcta

ión es adecuada

agador

ógico

nal

Anteros El superprop agador rechazó activament e las medidas de protección — negación deliberada del uso de equipo de protección , resistencia activa al aislamient o, difusión intencional de desinform ación sobre el brote. Minoría de los casos, pero alta visibilidad. La confrontac ión directa de las institucion es refuerza la identidad del Anteros: lo hace más visible y

Normas de pares dentro del grupo social del superprop agador que hacen que la cooperaci ón sea la norma del grupo. Framing de las medidas como afirmació n de la autonomía individual y de la responsab ilidad comunitar ia. Evitar la confronta ción institucion al directa. La reducción del Anteros requiere transform ación del sesgo identitario , no

Bajo sin cambio del contexto identitario . El Anteros es la disposició n más resistente a las intervenci ones directas.

Tratar el Anteros como el problema dominant e de la respuesta cuando en realidad es la minoría de los casos. La sobre-atención institucion al al Anteros produce narrativas de guerra cultural que refuerzan la identidad negacionis ta y amplían su impacto social.

Taxonomía General de Aplicaciones

Qué describe

α predicho

Error frecuente

Hijo dominant

Política

de intervenc

en el contexto epidemiol

si la intervenc

de respuesta institucio

e del superprop

ión correcta

ión es adecuada

agador

ógico

nal

más resolutivo.

presión directa.

Harmonía El superprop agador cooperó activament e con todas las medidas disponible s: se aisló en cuanto identificó síntomas, notificó exhaustiva mente sus contactos, cooperó con el rastreo, usó el equipo de protección adecuado. Puede aun así haber transmitid o por carga viral excepciona lmente alta o por transmisió n pre-sintomátic a inevitable.

Reconoce r y reforzar públicame nte la cooperaci ón. Las políticas que tratan igualment e a quien cooperó y a quien no desincenti van la cooperaci ón futura. El reconocim iento de la Harmonía tiene valor de norma social: muestra que el comporta miento cooperativ o es el que la comunida d valora.

Alto (0.70– 1.00). Este superprop agador maximizó su α dado el conocimie nto disponible .

Culpabiliz ar retroactiva mente a quien cooperó de buena fe, pero transmitió por razones fuera de su control (carga viral pre-sintomátic a, periodo de incubació n). Esto destruye la confianza en el sistema de salud pública y reduce la cooperaci ón futura.

Taxonomía General de Aplicaciones

El principio de equidad epidemiológica basado en los Hijos Una política de salud pública justa distingue entre el superpropagador que transmitió desde Fobos (las condiciones estructurales le impidieron actuar de otro modo) y el que lo hizo desde Anteros (eligió actuar contra las medidas). Ambos tienen el mismo R*, pero sus Δ son diferentes: el que actuó desde Fobos tiene Δ positivo porque el sistema de salud pública no generó las condiciones para que pudiera aislarse — eso es fraude annona del Estado hacia el trabajador que perdería el empleo si se aislaba. El que actuó desde Anteros tiene Δ positivo por elección propia. La política de intervención debe ser estructuralmente distinta en cada caso: el primero requiere reforma del sistema; el segundo requiere reforma del contexto identitario de su comunidad.

### §4  ¿Qué cuenta como asunción (α) en el dominio epidemiológico?

α en el dominio epidemiológico tiene dos niveles de aplicación con lógicas distintas. El α individual mide lo que el superpropagador con voluntad hizo para interrumpir las cadenas de transmisión que dependían de él. El α institucional/estatal mide lo que el sistema de salud pública generó — las condiciones materiales que habrían reducido la transmisión — proporcional a su R* y a su capacidad.

El α institucional es estructural: no son acciones individuales sino condiciones que se generan o no se generan El α del Estado en un brote no es un comunicado de prensa ni una declaración de emergencia: son las condiciones materiales de posibilidad que el Estado generó o no generó. El sistema de vigilancia epidemiológica activo antes del brote, la capacidad hospitalaria con reserva suficiente, el acceso a diagnóstico para toda la población, la cobertura de subsidio de días perdidos para trabajadores esenciales, la infraestructura de agua potable y saneamiento — esas son las condiciones cuya ausencia produce Δ positivo del Estado y cuya presencia constituye α institucional. FA_epi = R*_Estado × D_total × (1 − α_Estado). Este monto es la base para calcular la responsabilidad del Estado en demandas colectivas por negligencia en la respuesta pandémica. También es la base para establecer el presupuesto mínimo de inversión en salud pública que el sistema requiere: Taxonomía General de Aplicaciones

α_Estado debe ser proporcional a R*_Estado para que Δ_Estado sea próximo a cero.

α en el dominio epidemiológic

Nivel de α

Conducta que sube α

típico en respuestas deficientes

Nodo

o

Superpropagad or individual (con voluntad)

Grado de interrupción de las cadenas de transmisión: aislamiento, notificación de contactos, cooperación con el rastreo, uso de equipo de protección.

Aislamiento inmediato ante síntomas. Notificación exhaustiva de todos los contactos conocidos. Cooperación activa con el rastreo de contactos. Uso consistente del equipo de protección disponible.

0.00–0.35 cuando el Fobos (no puede aislarse) o el Deimos (no sabe que debe hacerlo) es dominante.

Sistema de vigilancia epidemiológica

Velocidad y cobertura de la detección del brote: tiempo desde los primeros casos hasta la activación de la alerta, cobertura del sistema de vigilancia centinela, capacidad de secuenciación genómica.

Detección del brote antes de que alcanzara transmisión comunitaria amplia. Activación de la alerta en tiempo útil para las intervencione s de contención. Capacidad de rastreo mayor al 80% de los contactos identificados.

0.05–0.15 en los brotes donde la detección tardía fue el factor dominante de la escalada.

Taxonomía General de Aplicaciones

α en el dominio epidemiológic

Nivel de α

Conducta que sube α

típico en respuestas deficientes

Nodo

o

Sistema de atención médica y hospitalario

Capacidad de absorción del brote sin colapso: reserva de camas de cuidados intensivos, disponibilidad de equipo de protección para trabajadores de salud, acceso a diagnóstico para toda la población con síntomas.

Mantenimient o de reserva hospitalaria activa. Provisión de equipo de protección suficiente para todos los trabajadores de salud. Diagnóstico accesible para toda la población con indicación clínica.

0.10–0.30 en sistemas de salud que fueron sobrepasado s por la demanda del brote.

Sistema de comunicación de riesgo

Calidad y veracidad de la comunicación del riesgo a la población: transparencia sobre la incertidumbre, claridad sobre los protocolos de acción, coherencia entre los mensajes de distintas autoridades.

Comunicació n temprana y honesta sobre el riesgo y la incertidumbre . Instrucciones claras y consistentes sobre qué hacer. Adaptación de los mensajes a distintos grupos de la población.

0.10–0.20 en los sistemas que minimizaro n el riesgo en las primeras semanas del brote.

Estado como diseñador de las condiciones estructurales

Grado en que el Estado generó las condiciones materiales de posibilidad que habrían reducido la transmisión:

Existencia de programas de compensació n por días de aislamiento para trabajadores informales y

0.05–0.25 en los sistemas que no generaron las condiciones para que los grupos más

Taxonomía General de Aplicaciones

α en el dominio epidemiológic

Nivel de α

Conducta que sube α

típico en respuestas deficientes

Nodo

o

cobertura de subsidio de días perdidos para trabajadores esenciales, acceso a vivienda con condiciones de aislamiento, infraestructura de agua y saneamiento.

esenciales. Provisión de alojamiento de aislamiento para quienes no pueden aislarse en el hogar. Inversión histórica en infraestructur a de salud pública.

vulnerables pudieran aislarse.

### §5  Construcción del grafo epidemiológico causal

### El grafo de cuatro niveles: de lo individual a lo estructural

El grafo epidemiológico causal se construye en cuatro niveles que van desde lo más micro (los contactos individuales) hasta lo más macro (las condiciones estructurales del sistema de salud pública). A diferencia de las redes de contacto tradicionales en epidemiología — que solo incluyen personas — el grafo causal incluye también los nodos estructurales que determinan las condiciones bajo las cuales los contactos producen transmisión. El error de construir el grafo solo con personas produce un R* que sobreestima la responsabilidad individual y subestima la responsabilidad estructural.

Taxonomía General de Aplicaciones

Fuent

Nivel

Tipo

e de eviden

Función

R* típico S típico

del grafo

de nodo

causal

cia para w

Indivi dual

Person a infecta da con caracter ísticas de alta transmi sión: carga viral excepci onal, posició n en la red de contact os (hub), trabajo con contact o intensiv o.

Transmisi ón directa del patógeno. R* alto si la transmisi ón de ese nodo fue causalme nte necesaria para la escala del brote. S depende de si esas característ icas eran idiosincrá ticas (S bajo: superpro pagador) o genéricas (S alto: cualquier caso habría transmitid o igual).

Variable — bajo en casos ordinario s, alto en superpro pagadore s

Variable — alto en casos ordinario s (cualquie r caso habría transmiti do igual en ese entorno), bajo en superpro pagadore s genuinos

Rastre o de contact os, secuen ciación genómi ca, carga viral docum entada, análisis de clúster por caso índice.

Ambi ental

Espaci o de transmi sión: instalac ión cerrada mal ventila da,

Amplifica o reduce la transmisi ón individual independi entement e de las característ

Moderad o-alto cuando el espacio es la condició n que convierte el caso en

Moderad o — el espacio específic o tiene caracterís ticas que otros espacios no

Estudi os de ventila ción, análisis de clúster por ubicaci ón,

Taxonomía General de Aplicaciones

Fuent

Nivel

Tipo

e de eviden

Función

R* típico S típico

del grafo

de nodo

causal

cia para w

sistema de agua o aire compar tido, transpo rte de alta densida d.

icas de las personas. Un espacio mal ventilado puede convertir una transmisi ón ordinaria en un evento superspre ader.

superpro pagador

tendrían si estuviera n mejor ventilado s o mantenid os

compa ración de tasas de ataque por espacio , análisis de aerosol es.

Instit ucion al

Sistema de vigilanc ia epidem iológica , hospita les, laborat orios de diagnós tico, autorid ades de salud pública.

Detecta, contiene y trata. Su fallo aumenta el R* efectivo de los nodos individual es porque reduce α del sistema. Su éxito lo disminuye . Es el nodo donde el fraude annona del Estado es más directame

Moderad o-alto en los brotes donde la detecció n tardía o la capacida d hospitala ria sobrepas ada fueron factores determin antes de la escala

Moderad o — los sistemas de salud pública con distinto nivel de inversión histórica producen respuesta s muy distintas

Cronol ogía de decisio nes versus cronol ogía del brote, capacid ad de rastreo, tiempo de respues ta desde detecci ón hasta interve nción, cobert ura de diagnó stico.

Taxonomía General de Aplicaciones

Fuent

Nivel

Tipo

e de eviden

Función

R* típico S típico

del grafo

de nodo

causal

cia para w

nte medible.

Norm ativo / polític o

Política s de cuarent ena, mandat os de equipo de protecc ión, restricci ones de movilid ad, campañ as de vacuna ción, subsidi os de aislami ento, comuni cación de riesgo.

Determin a las condicion es bajo las cuales ocurre la transmisi ón a escala poblacion al. El nodo de mayor R* en muchos brotes es una política que tardó en activarse o que no se activó — no un caso individual .

Alto cuando las decisione s políticas crearon condicio nes que amplifica ron la transmisi ón más allá de lo que el sistema de salud podía absorber

Moderad o-bajo cuando las decisione s eran idiosincr áticas del gobierno específic o; moderad o-alto cuando cualquier gobierno bajo las mismas restriccio nes institucio nales habría tomado las mismas decisione s

Cronol ogía de decisio nes versus model os contraf ácticos de la escala del brote con activaci ón tempra na, compa ración entre jurisdic ciones con distinta s política s, estudio s de impact o de las interve ncione s.

Taxonomía General de Aplicaciones

### El índice de sustituibilidad S en epidemiología: hacia dónde apunta la intervención

S alto del nodo → la intervención debe ser sobre la clase, no sobre el nodo específico S alto de una persona infectada: cualquier persona con la misma carga viral en el mismo entorno habría transmitido igual. La intervención no debe focalizarse en esa persona sino en el entorno que la hace transmisora — la ventilación del espacio, la densidad de contactos, el acceso a equipo de protección. S alto de un nodo estructural (sistema de agua contaminado): cualquier sistema de agua equivalente habría producido la misma transmisión. La intervención no es solo sobre ese sistema específico sino sobre la clase de sistemas similares. S bajo del superpropagador: las características idiosincráticas de esa persona en ese momento — carga viral excepcional, posición en la red de contactos, trabajo con contacto intensivo en espacio cerrado — fueron causalmente determinantes. La intervención puede focalizarse en ese perfil de persona. La combinación de R* × (1−S) produce la guía de intervención más eficiente: Impacto_intervención_i ∝ R*_i × (1 − S_i). Intervenir en el nodo de mayor R* × (1−S) produce el mayor impacto en la reducción del brote por unidad de recursos invertida.

### §6  Preguntas que responde este capítulo

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

¿Cuál es el nodo de mayor R* en el brote — el que más contribuyó causalmente a su escala?

Construcción del grafo epidemiológico con los cuatro niveles y cálculo del eigenvector dominante de la matriz de pesos W. El nodo de mayor R* es el que, si se hubiera intervenido, habría producido la mayor reducción del brote. John Snow lo identificó sin el formalismo matemático mediante la

Declaración B si hay análisis EP2 de calidad con variación espacial y temporal. Declaración A si hay secuenciación EP1 que establece la cadena de transmisión con precisión molecular.

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

variación espacial de los casos.

¿La política de respuesta institucional fue causalmente adecuada o hay fraude annona epidemiológico?

Análisis cronológico EP2/EP5: ¿las decisiones se tomaron cuando el sistema tenía la información y la capacidad para actuar de manera diferente? ¿Qué habría ocurrido si las medidas se hubieran implementado dos semanas antes? FA_epi = R*_Estado × D_total × (1 − α_Estado).

Declaración B si hay evidencia de las decisiones y de sus alternativas disponibles EP5. Declaración C si el contrafáctico de la activación temprana requiere modelamiento epidemiológico con alta incertidumbre.

¿El superpropagador actuó desde Fobos (condiciones de trabajo), Deimos (falta de diagnóstico) o Anteros (negación deliberada)?

Análisis de Hijos del superpropagador desde la evidencia epidemiológica y contextual: ¿tenía cobertura de días perdidos para aislarse? ¿Tenía acceso a diagnóstico? ¿Hay evidencia de comportamiento negacionista activo? El Hijo dominante determina la política de intervención.

Declaración B con evidencia contextual EP3/EP5 de las condiciones estructurales del superpropagador. Declaración C si el Hijo debe inferirse sin documentación directa del caso.

¿Qué intervención tiene mayor impacto por unidad de recursos — análisis prospectivo?

Cálculo de R*_i × (1−S_i) para cada nodo candidato a intervención. El nodo de mayor R* × (1−S) produce el mayor impacto por unidad de recursos. Si S del entorno físico es alto (cualquier instalación similar produciría el mismo resultado), la

Declaración B con análisis EP2 que establezca los R* y S de los nodos candidatos. El análisis prospectivo tiene mayor incertidumbre que el análisis retrospectivo.

Taxonomía General de Aplicaciones

Pregunta del

Instrumento que la

Nivel de certeza

caso

responde

posible

intervención sobre la clase es más eficiente que la intervención sobre un espacio específico.

¿Cuánto del D_total del brote es causalmente atribuible a los nodos institucionales versus a los factores estructurales de fondo?

Distribución de R* entre los cuatro niveles del grafo: individual, ambiental, institucional, normativo/político. AD_institucional = R*_institucional × D_total_AVAD. El D_total en unidades comparables internacionalmente usa AVAD × w_ref.

Declaración B con análisis EP2 completo. La distribución de R* entre niveles es el análisis más disputado del dominio porque requiere establecer contrafácticos para múltiples nodos simultáneamente.

¿Hay desigualdad epidemiológica — el brote afectó más a los grupos más vulnerables por razones de diseño del sistema?

Análisis del diferencial de daño entre grupos sociales controlando por las características del patógeno: ¿los grupos con mayor mortalidad o morbilidad lo son por características biológicas o por condiciones de exposición, acceso al tratamiento y capacidad de aislamiento determinadas estructuralmente?

Declaración B con análisis EP4 de la distribución del daño por grupo social controlando por la severidad de la condición. El R* de los nodos estructurales (condiciones laborales, acceso al sistema de salud) en el diferencial de daño entre grupos establece la responsabilidad del diseñador de esas condiciones.

### §7  Traducción de D_total al dominio epidemiológico

Taxonomía General de Aplicaciones

D_vital_epi = AVAD × w_ref · Los Años de Vida Ajustados por Discapacidad como unidad estándar El daño epidemiológico se cuantifica en la unidad estándar de la OMS para la carga de enfermedad: AVAD = AVPP (Años de Vida Perdidos por Muerte Prematura) + AVD (Años Vividos con Discapacidad). Convertido al sistema: D_vital_epi = AVAD × w_ref, donde w_ref es el salario de referencia global universal (no el salario del país afectado), para mantener el principio ontológico de igualdad del tiempo de vida. La hora de vida de un trabajador esencial de un país de ingreso bajo que murió por COVID-19 porque el sistema no le dio condiciones para aislarse tiene el mismo valor ontológico que la de un ciudadano de un país de ingreso alto. La conversión D_vital = AVAD × w_ref × 8,760 horas/año transforma los AVAD en la misma unidad de horas de vida que se usa en todos los dominios del libro — lo que permite comparar el fraude annona epidemiológico con el fraude annona financiero, el daño de un brote con el daño de una catástrofe ambiental, y el costo de la inversión preventiva con el D_total que esa inversión habría prevenido.

En el dominio epidemioló

Fuente

Compon

Estimación en unidades comparables

de evidenci

ente

gico

a

T_invertid o (muertes y morbilida d aguda directa)

Las muertes atribuibles al brote (AVPP) y las hospitalizaci ones, discapacida des y morbilidad producidas en el período agudo del brote. Es el component e que las estadísticas de mortalidad registran más

D_vital_T_invertido = AVPP × 8,760 h/año × w_ref. Los AVPP se calculan como (esperanza_de_vida − edad_de_muerte) para cada fallecimiento atribuido al brote. Para el COVID-19 con 17 millones de muertes en exceso: ~2.23 × 10¹² horas de vida.

Datos de mortalida d en exceso de las autoridad es estadística s nacionale s. Análisis de AVPP de la OMS y de institutos de estadística s nacionale s. Estudios de mortalida

Taxonomía General de Aplicaciones

En el dominio epidemioló

Fuente

Compon

Estimación en unidades comparables

de evidenci

ente

gico

a

directament e.

d por todas las causas durante el brote versus períodos comparab les.

T_impedi do (colapso del sistema de salud y atención pospuesta )

Durante un brote severo el sistema de salud no puede atender otras condiciones: cirugías pospuestas, enfermedad es crónicas sin atención, detección de cáncer retrasada, atención de urgencias comprometi da. Este component e frecuenteme nte supera a T_invertido en los brotes más graves.

D_vital_T_impedido = AVD_cond_pospuestas × 8,760 h/año × w_ref. Los AVD se calculan usando los pesos de discapacidad de la OMS para las condiciones que no recibieron atención oportuna.

Datos de actividad hospitalar ia durante el brote versus períodos comparab les. Estudios del impacto del brote sobre las listas de espera. Análisis de la mortalida d por condicion es no COVID durante el período del brote.

ΔT_trayec toria (secuelas de largo plazo y pérdida

Las secuelas crónicas de los supervivient es (COVID largo,

D_vital_trayectoria = AVD_secuelas_crónicas × 8,760 h/año × w_ref + pérdida_de_potencial_ge neracional. Este componente tiene la

Estudios de largo plazo sobre COVID largo y

Taxonomía General de Aplicaciones

En el dominio epidemioló

Fuente

Compon

Estimación en unidades comparables

de evidenci

ente

gico

a

generacio nal)

síndrome post-viral, daño orgánico persistente), el impacto en el desarrollo infantil por interrupcion es educativas, la pérdida de potencial de las cohortes más afectadas.

mayor incertidumbre del D_total y debe declararse como rango con análisis de sensibilidad.

otros síndrome s post-virales. Análisis del impacto de las interrupci ones educativa s sobre el potencial de ingresos de las cohortes afectadas. Estudios de impacto en el desarrollo cognitivo por interrupci ones en el período crítico.

### Distribución del AD entre los nodos del grafo y el fraude annona epidemiológico

AD_i = R*_i × D_total_epi · FA_epi = R*_Estado × D_total × (1 − α_Estado) En el COVID-19 con D_total ≈ $38.9 billones USD (2024): AD_N1 (sistemas de alerta OMS/China, R* ~28%) ≈ $10.9B. AD_N2 (conectividad aérea, R* ~22%) ≈ $8.6B. AD_N3 (desigualdad sanitaria, R* ~18%) ≈ $7.0B. AD_N5 (comunicación minimizante, R* ~12%) ≈ $4.7B. El FA_epi se aplica a los nodos institucionales/normativos bajo

Taxonomía General de Aplicaciones

control del Estado: con R*_Estado ≈ 58% (N1+N3+N5+N6) y α_Estado ≈ 0.10, FA_epi ≈ $20.3 billones USD. Para el cólera de Broad Street de 1854 con D_monetary_equiv ≈ $705M USD (2024): AD_N1 (bomba, R* ~48%) ≈ $339M. AD_N4 (autoridades sanitarias, R* ~8%) ≈ $56M. J_sistema = 1 − Σ|Δ_i| ≈ 0.06: injusticia estructural casi máxima. Los nodos de mayor R* (la bomba, el pozo negro, la infraestructura) tenían α ≈ 0 antes del brote. El fraude annona del sistema de salud pública de Londres en 1854 era masivo y medible: el sistema había recibido el capital de los ciudadanos y no había generado las condiciones materiales básicas (alcantarillado separado, agua potable) que habrían evitado el brote.

### §8  Límites del método y errores frecuentes de aplicación

Límites del método en el dominio epidemiológico

Límite 1 — La incertidumbre sobre los pesos en tiempo real. En un brote activo, los pesos del grafo son inciertos porque la evidencia está siendo generada simultáneamente con la toma de decisiones. Los R* estimados en las primeras semanas de un brote tienen intervalos de confianza amplios. El análisis en tiempo real debe incluir rangos de pesos y análisis de sensibilidad, no valores puntuales.

Límite 2 — La causalidad en múltiples escalas simultáneas. Una pandemia opera en múltiples escalas causales: molecular, individual, comunitaria, nacional, global. El grafo completo tendría miles de nodos. En la práctica, el análisis debe seleccionar los nodos más relevantes para la pregunta específica. La selección de los nodos incluidos en el análisis es una decisión metodológica que debe declararse explícitamente.

Límite 3 — El problema del contrafáctico en pandemia. Las intervenciones cambian el comportamiento de los otros nodos: si los sistemas de alerta hubieran actuado dos semanas antes, los sistemas de conectividad aérea y las políticas de comunicación también habrían actuado diferente. El grafo

Taxonomía General de Aplicaciones

### completo con dinámicas de respuesta requiere modelos epidemiológicos más sofisticados que el cálculo estático de R*.

Límite 4 — Los Hijos y la privacidad de los superpropagadores. El análisis de Hijos de superpropagadores identificados plantea problemas de privacidad y estigmatización. El objetivo del análisis de Hijos no es culpabilizar a los superpropagadores sino orientar la política de intervención hacia las causas estructurales. Si el análisis se usa para identificar y sancionar a individuos en lugar de reformar el sistema, pierde su valor y produce efectos contraproducentes.

Límite 5 — R* identifica retrospectivamente, no predice prospectivamente el próximo superpropagador. R* identifica qué nodos tuvieron mayor peso causal en el brote analizado. No predice cuál nodo será el superpropagador en el próximo brote, porque esa posición depende de condiciones que varían en cada caso. Lo que permite en sentido prospectivo es identificar los tipos de nodos que tienden a tener mayor R* bajo condiciones similares y diseñar intervenciones estructurales para reducir ese peso antes del próximo brote.

### Errores frecuentes de aplicación

Error Por qué

Consecuen

cia Corrección

ocurre

Construir el grafo epidemiológ ico solo con personas e ignorar los nodos estructurale s e institucional es

El rastreo de contactos es la práctica estándar en epidemiolog ía y produce naturalment e un grafo de personas.

R* sobreestima do de los casos individuales . R* del sistema de salud pública y de las condiciones estructurale

El grafo causal completo incluye cuatro niveles: individual, ambiental, institucional y normativo/político. La omisión de cualquier nivel produce una distribución de R* incompleta y una guía

Taxonomía General de Aplicaciones

Error Por qué

Consecuen

cia Corrección

ocurre

s = 0. Las políticas resultantes se focalizan en el comportam iento individual cuando el mayor potencial de impacto está en los nodos estructurale s.

de intervención subóptima.

Usar el Hijo dominante del superpropa gador para sancionarlo en lugar de para diseñar la intervenció n correcta

El análisis identifica a un superpropa gador con Fobos dominante y el sistema responde con sanción.

Sanción a quien tenía las menores opciones reales para actuar diferente. Incremento del Fobos de otros potenciales casos que no reportarán ni cooperarán. Reducción del α general del sistema.

El Hijo dominante determina la política de intervención, no el nivel de sanción. Fobos → eliminar las barreras al aislamiento. Deimos → proveer el marco que faltó. Solo Anteros justifica la sanción individual, y aun así la reforma del contexto identitario es más eficaz que la sanción directa.

Atribuir toda la responsabili dad del brote a un único nodo visible (el "paciente

La narrativa política tiende a personalizar la causa en el nodo más visible — el caso índice,

R* del nodo más visible sobreestima do. R* de los nodos sistémicos (sistemas de alerta,

El análisis causal siempre distribuye R* entre múltiples nodos. El nodo de origen típicamente tiene S alto (cualquier evento similar en esas condiciones habría

Taxonomía General de Aplicaciones

Error Por qué

Consecuen

cia Corrección

ocurre

cero" o el Estado de origen)

el Estado donde comenzó el brote.

desigualdad sanitaria, conectivida d aérea) = 0 en la narrativa dominante. Las reformas resultantes son ineficaces porque atacan el detonador visible (S alto) en lugar del sistema que lo amplificó (S bajo).

producido resultados similares); los nodos estructurales tienen S moderado-bajo y son los que más podrían cambiar el resultado de brotes futuros.

No distinguir entre el R* del superpropa gador y la responsabili dad del sistema que lo produjo

El análisis establece el R* del superpropa gador sin preguntar cuánto de ese R* es causalmente atribuible a las condiciones que el sistema no generó para reducirlo.

Responsabil idad individual sobreestima da. El Δ del Estado como espejo del Fobos del trabajador esencial permanece invisible.

R*_superpropagador _efectivo = R*_intrínseco × (1 − α_sistema). Cuando α_sistema es bajo (el sistema no generó las condiciones de aislamiento), el R*_efectivo del superpropagador es amplificado por la inacción sistémica. El Δ del Estado que no generó las condiciones de aislamiento es la medida de su responsabilidad en la amplificación del R*_efectivo de los nodos individuales.

Taxonomía General de Aplicaciones

### §9  Guía de prioridades de recolección de evidencia

Si tu prioridad es saber qué buscar primero en un análisis epidemiológico de responsabilidad, usa la tabla y el árbol que siguen. La primera decisión siempre es establecer si el análisis es retrospectivo (distribución de responsabilidad en un brote ocurrido) o prospectivo (diseño de intervenciones para el brote en curso o para la preparación del próximo). Cada análisis tiene prioridades de evidencia distintas.

### Tabla de prioridades de recolección de evidencia en epidemiología y salud pública

La evidencia

Qué buscar /

Por qué funcio

Si tu incertidumbre principal es…

Qué rango reduce

que más la reduce

qué pregunta

na

es…

r

### 1. ¿El análisis es retrospectivo (responsabilidad por un brote ocurrido) o prospectivo (diseño de intervenciones)?

Identificar el objetivo del análisis: ¿se busca distribuir responsabi lidad entre actores por un brote ya ocurrido, o identificar los nodos de mayor impacto para intervenci ones durante el brote activo o para la preparació

El objetiv o determi na los instrum entos priorita rios y el nivel de certeza requeri do. El análisis retrosp ectivo usa EP2 con más datos disponi bles; el

Determ ina el instrum ento principa l y el nivel de certeza necesari o

¿El análisis se usa para atribución de responsab ilidad legal o institucion al (retrospec tivo), para guiar la respuesta actual (prospecti vo en tiempo real), o para preparació n

Taxonomía General de Aplicaciones

La evidencia

Qué buscar /

Por qué funcio

Si tu incertidumbre principal es…

Qué rango reduce

que más la reduce

qué pregunta

na

es…

r

n del próximo?

análisis prospec tivo requiere rangos y escenari os de estrés.

preventiva (prospecti vo a largo plazo)?

### 2. [TODOS] ¿Cuáles son los cuatro niveles del grafo — está el análisis incluyendo los nodos estructurales?

Construcci ón del grafo con los cuatro niveles: individual, ambiental, institucion al, normativo /político. ¿Hay nodos de infraestruc tura (sistemas de agua, ventilación , densidad habitacion al) incluidos? ¿Hay nodos de política (cronologí a de decisiones, cobertura del sistema de salud) incluidos?

La omisión de cualqui er nivel produc e un R* incomp leto. El error más frecuen te es reducir el grafo al nivel individ ual. Los nodos de mayor R* en la mayoría de los brotes de escala significa tiva son estructu rales, no

Estable ce la complet itud del grafo (incerti dumbre empíric a estructu ral)

¿Hay datos de infraestruc tura de salud pública disponible s (cobertura de agua potable, acceso a saneamien to, densidad hospitalari a)? ¿Hay cronología de decisiones de los actores institucion ales? ¿Hay datos de condicion es laborales y de cobertura social de los grupos

Taxonomía General de Aplicaciones

La evidencia

Qué buscar /

Por qué funcio

Si tu incertidumbre principal es…

Qué rango reduce

que más la reduce

qué pregunta

na

es…

r

individ uales.

más afectados?

### 3. [RETROSPEC TIVO] ¿Cuál fue el nodo de mayor R* en el brote — análisis de la fuente primaria?

Análisis EP2 de la variación espacial y temporal de los casos: ¿hay un cluster de casos que apunta a un nodo ambiental específico (bomba de agua, instalación de procesami ento, evento social)? La variación espacial con epicentro claro sugiere R* alto del nodo físico identificad o.

El método de John Snow — variació n espacial de los casos con el nodo ambient al como epicentr o — es el instrum ento más directo y robusto para identific ar el nodo de mayor R* cuando hay una fuente primari a identific able.

Estable ce el nodo de mayor R* (incerti dumbre empíric a crítica)

¿Los casos se agrupan espacialm ente alrededor de un nodo específico ? ¿Las anomalías (grupos que no se infectaron , grupos que sí) confirman la hipótesis del nodo primario? ¿La secuenciac ión genómica EP1 establece la cadena de transmisió n?

### 4. [RETROSPEC TIVO] ¿Hay

Análisis cronológic o EP5:

Si el sistema tenía

Estable ce el FA_epi

¿Cuándo tuvo el sistema de

Taxonomía General de Aplicaciones

La evidencia

Qué buscar /

Por qué funcio

Si tu incertidumbre principal es…

Qué rango reduce

que más la reduce

qué pregunta

na

es…

r

fraude annona epidemiológico — el sistema tenía la capacidad de actuar diferente?

comparaci ón entre el momento en que el sistema tuvo la informació n para actuar y el momento en que actuó. ¿Había precedente s de brotes similares con respuestas más tempranas ? ¿Los recursos disponible s permitían una respuesta más rápida o más completa?

informa ción y capacid ad para actuar antes de lo que actuó, hay Δ positivo del nodo instituci onal — fraude annona medible .

del sistema de salud pública (incerti dumbre empíric a y normati va)

vigilancia la informaci ón suficiente para activar la alerta? ¿Había recursos disponible s no utilizados? ¿Otros sistemas con capacidad es similares respondier on más temprana mente? ¿Los planes de respuesta existentes se activaron en tiempo?

### 5. [SUPERPROP AGADORES] ¿El superpropagado r transmitió desde Fobos, Deimos, Potós o Anteros?

Análisis contextual del superprop agador: ¿tenía cobertura de días perdidos para aislarse

El Hijo domina nte determi na la política de interve nción correcta . La

Reduce la incertid umbre sobre la política de interven ción (incerti dumbre

¿Tenía el superprop agador trabajo informal o sin cobertura de días perdidos? ¿Había acceso

Taxonomía General de Aplicaciones

La evidencia

Qué buscar /

Por qué funcio

Si tu incertidumbre principal es…

Qué rango reduce

que más la reduce

qué pregunta

na

es…

r

(ausencia → Fobos probable)? ¿Tenía acceso a diagnóstic o cuando empezó a tener síntomas (ausencia → Deimos probable)? ¿Hay evidencia de comporta miento negacionis ta activo (Anteros)?

confusi ón entre Fobos y Anteros produc e la política más injusta (sancio nar a quien no tenía opcione s) y la menos eficaz.

ontológ ica)

gratuito y rápido a diagnóstic o en su área? ¿Hay registros de comporta miento negacionis ta activo document ado?

### 6. [PROSPECTIV O] ¿Qué intervención tiene mayor impacto por unidad de recursos?

Cálculo de R*_i × (1−S_i) para cada nodo candidato a intervenci ón con los datos disponible s. Si S del nodo es alto (cualquier persona o instalación similar produciría el mismo resultado),

R* × (1−S) es el criterio de prioriza ción de interve nciones — el mismo principi o del cap. 12 (insolve ncia) aplicad o al diseño de la respues

Estable ce las priorida des de interven ción (incerti dumbre empíric a y de política)

¿Los superprop agadores identificad os tienen característ icas comunes que permiten identificar la clase (trabajado res esenciales en espacios cerrados, instalacion es con ventilació

Taxonomía General de Aplicaciones

La evidencia

Qué buscar /

Por qué funcio

Si tu incertidumbre principal es…

Qué rango reduce

que más la reduce

qué pregunta

na

es…

r

la intervenci ón sobre la clase supera a la intervenci ón sobre el nodo específico.

ta de salud pública.

n deficiente, etc.)? ¿La intervenci ón sobre esa clase es factible con los recursos disponible s?

### Árbol de decisión en epidemiología y salud pública: ¿qué buscar primero?

### El árbol bifurca entre el análisis retrospectivo de responsabilidad y el análisis prospectivo de diseño de intervenciones.

¿Cuál es el análisis principal?

├─ Análisis A: RETROSPECTIVO — distribución de responsabilidad en un brote ocurrido │

├─  PRIORIDAD 1: Construir el grafo con los cuatro niveles — no omitir los nodos estructurales.

· Individual, ambiental, institucional y normativo/político.

├─  PRIORIDAD 2: ¿Cuál fue el nodo de mayor R* — variación espacial EP2 o genómica EP1?

· El método de Snow: variación espacial con epicentro claro = nodo ambiental dominante.

Taxonomía General de Aplicaciones

├─  PRIORIDAD 3: ¿Hay fraude annona — el sistema tuvo la capacidad de actuar diferente?

· Cronología de decisiones EP5 versus cronología del brote. · FA_epi = R*_Estado × D_total × (1 − α_Estado).

└─  PRIORIDAD 4 (si hay superpropagadores identificados): Hijo dominante → política de respuesta.

· Fobos → reforma estructural. Deimos → acceso y comunicación. Anteros → norma de pares.

└─ Análisis B: PROSPECTIVO — diseño de intervenciones durante el brote o para preparación

└─  PRIORIDAD ÚNICA: Calcular R*_i × (1−S_i) para cada nodo candidato a intervención.

· El nodo de mayor R* × (1−S) es el de mayor impacto por unidad de recursos. · S alto → intervención sobre la clase. S bajo → intervención focalizada en el nodo. · Hijos de los superpropagadores: la intervención correcta depende del Hijo, no del R*.

— Fin del Capítulo 21 — Centro Multidisciplinario Meriadock Formación y Asesoría A.C.  · 2026

Taxonomía General de Aplicaciones

