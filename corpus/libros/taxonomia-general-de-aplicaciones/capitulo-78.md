PARTE XIII · Filosofía, Ética y Pensamiento

## Capítulo 78

### Pensamiento sistémico y causalidad circular

### — los límites del modelo lineal

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo

Este capítulo es Nivel C y es el más técnicamente exigente de la Taxonomía: analiza los límites del modelo causal lineal del sistema — el grafo dirigido acíclico (DAG) sobre el que opera el R* — ante sistemas con retroalimentación, causalidad circular y emergencia. Es también, en cierta medida, el capítulo de cierre: establece con honestidad intelectual qué puede y qué no puede hacer el sistema, y esboza las extensiones que serían necesarias para capturar las formas de causalidad que el modelo lineal no puede representar.

### §1  El supuesto implícito: el grafo dirigido acíclico

El modelo Prometeo opera sobre un grafo causal G = (N, A, w) donde los nodos N son actores y factores, las aristas A son dependencias causales dirigidas, y los pesos w miden la intensidad de cada dependencia. La iteración de potencia que produce el eigenvector dominante — el R* — requiere que el grafo sea una matriz con espectro calculable. En la práctica, el modelo funciona mejor cuando el grafo es aproximadamente un DAG: un grafo dirigido sin ciclos, donde la causalidad fluye en una sola dirección desde los actores hacia los resultados.

El problema: la mayoría de los sistemas sociales, ecológicos y físicos de interés tienen ciclos de retroalimentación que el DAG no puede representar. El sistema de género que produce la violencia de género

Taxonomía General de Aplicaciones

es a su vez reproducido por esa violencia (ciclo). La pobreza que produce el abandono escolar produce la pobreza (ciclo). El cambio climático que produce los desplazamientos forzados produce la presión política que dificulta las reformas climáticas (ciclo). En esos sistemas, la causalidad no fluye en una sola dirección: fluye en ambas, y el estado del sistema en el tiempo t es causa y efecto del estado en el tiempo t-1.

El DAG como aproximación: cuando funciona y cuando falla El DAG es una aproximación válida cuando el período de análisis es suficientemente corto para que los ciclos de retroalimentación no hayan completado un ciclo completo, o cuando la magnitud de la retroalimentación es significativamente menor que la magnitud de la causalidad directa. En el análisis del accidente de Challenger, el período de análisis es de horas — los ciclos de retroalimentación del sistema de seguridad de la NASA (cómo el accidente anterior cambió las prácticas de seguridad que determinaron el siguiente accidente) no son relevantes para el análisis del evento específico. En el análisis del cambio climático acumulado durante décadas, los ciclos de retroalimentación (el calentamiento que produce la liberación de metano del permafrost que produce más calentamiento) son dominantes y el DAG falla.

### §2  Los tres tipos de retroalimentación que el modelo lineal no captura

Tipo de retroalimentació

Extensión necesaria del

Descripción Ejemplo en la

Taxonomía

n

modelo

Retroalimentació n positiva (amplificación)

El resultado de un proceso amplifica su propia causa: el aumento de temperatura produce la liberación de metano que produce más aumento de

El cap. 64 (Cambio climático): los feedbacks climáticos positivos — el albedo del hielo que se derrite, el permafrost que libera metano — amplifican el

Ecuaciones diferenciales no lineales que modelan la dinámica del sistema con retroalimentació n. La responsabilidad del emisor incluye el

Taxonomía General de Aplicaciones

Tipo de retroalimentació

Extensión necesaria del

Descripción Ejemplo en la

Taxonomía

n

modelo

temperatura. El sistema se aleja exponencialmen te del equilibrio.

calentamiento causado por las emisiones. El modelo Shapley climático establece la responsabilidad de las emisiones antropogénicas pero no captura el multiplicador de los feedbacks.

componente multiplicado por los feedbacks que sus emisiones activaron.

Retroalimentació n negativa (estabilización)

Los mecanismos de corrección que devuelven el sistema al equilibrio cuando se desvía: el sistema inmune que responde a la infección, el mercado que ajusta los precios ante el exceso de demanda. El sistema tiene resiliencia.

El cap. 63 (Criminología): los mecanismos de resiliencia comunitaria que reducen la incidencia del delito a pesar del campo criminal — las organizaciones comunitarias, los sistemas de apoyo mutuo. El DAG no captura cómo esos mecanismos de retroalimentació n negativa reducen el R* efectivo de los nodos del campo criminal.

Modelización del equilibrio con retroalimentació n: identificar los mecanismos de resiliencia del sistema y su capacidad de reducir el R* efectivo de los nodos del campo.

Causalidad emergente (el todo es más que la suma de las partes)

El comportamiento del sistema emerge de las interacciones

El cap. 45 (Sociología): el ego colectivo de la organización o el movimiento

La teoría de la complejidad y los sistemas adaptativos complejos

Taxonomía General de Aplicaciones

Tipo de retroalimentació

Extensión necesaria del

Descripción Ejemplo en la

Taxonomía

n

modelo

entre sus componentes y no puede reducirse a la suma de las propiedades de cada componente: la conciencia emerge de las neuronas sin que ninguna neurona individual la tenga, la cultura emerge de los actores sin que ningún actor la diseñe.

tiene R* sobre el comportamient o de sus miembros que no puede reducirse a la suma de los R* individuales. La distribución del IRC establece la distribución del R* emergente entre los diseñadores del c_col y los ejecutores.

(SAC): el modelo Prometeo capta parte de la emergencia con el IRC y el ajuste por IIC, pero la emergencia radical (donde el R* del sistema no puede derivarse de los R* de sus componentes) excede el modelo.

### §3  El eigenvalor como solución parcial: por qué funciona y por qué no es suficiente

La iteración de potencia que produce el R* — el eigenvector dominante de la matriz de pesos W — tiene una propiedad que la hace robusta ante ciclos débiles: si la matriz W tiene ciclos, pero el eigenvalor dominante es real y positivo (que ocurre cuando la matriz es suficientemente «parecida» a una matriz sin ciclos), el R* convergirá a un vector estable que captura la influencia causal de cada nodo incluyendo las retroalimentaciones débiles.

En esos casos, el R* del nodo i incluye implícitamente el efecto de las retroalimentaciones que amplifican su influencia a través de ciclos: si A influye sobre B y B influye sobre A, la iteración de potencia asigna a A un R* que refleja tanto la influencia directa de A sobre el resultado como la influencia indirecta a través del ciclo A→B→A. Esa propiedad hace que el modelo Prometeo sea más robusto ante sistemas con ciclos débiles de lo que parece.

Taxonomía General de Aplicaciones

Pero el modelo falla cuando los ciclos son dominantes — cuando el eigenvalor de los ciclos supera el de la causalidad lineal. En esos casos, el eigenvector dominante no converge o converge a una solución que no tiene interpretación causal válida. El sistema de retroalimentación del cambio climático, el ciclo de la pobreza intergeneracional a escalas de décadas, la espiral de la polarización política — en esos sistemas, el modelo Prometeo produce resultados que subestiman sistemáticamente la responsabilidad de los actores que iniciaron el ciclo.

### §4  Los límites del modelo y las extensiones necesarias

### El sistema establece honestamente cuatro límites que el modelo lineal no puede superar sin extensiones que exceden el alcance de la Taxonomía actual.

Qué dominios

Límite del modelo lineal Por qué ocurre

de la Taxonomía lo

Extensión

posible

enfrentan

La causalidad circular produce eigenvalores complejos que no tienen interpretación de responsabilidad

Cuando el grafo tiene ciclos fuertes, la iteración de potencia puede producir eigenvalores complejos (con componente imaginaria) que no tienen la interpretación de «fracción del resultado causalmente atribuible al nodo».

Cambio climático (feedbacks), polarización política (cap. 44), pobreza intergeneracional (cap. 73, cap. 61), redes ecológicas (cap. 65).

Modelos de equilibrio dinámico que establecen el R* como la contribución marginal al estado estacionario del sistema — el Shapley dinámico, que distribuye la responsabilidad sobre el estado estacionario del ciclo en lugar de sobre un evento final.

Taxonomía General de Aplicaciones

Qué dominios

Límite del modelo lineal Por qué ocurre

de la Taxonomía lo

Extensión

posible

enfrentan

La emergencia hace que el R* del sistema no sea la suma de los R* de sus componentes

Los sistemas con propiedades emergentes (la cultura, la conciencia, la vida) tienen R* sobre los resultados que no pueden distribuirse entre sus componentes sin perder la información de la emergencia.

Ego colectivo (cap. 45), sistemas ecológicos (cap. 65), cultura como campo (cap. 47, 68).

El IRC y el ajuste por IIC del cap. 45 son una aproximación a la responsabilidad emergente — capturan el R* del diseñador del c_col colectivo que determina el comportamiento de los miembros. La extensión completa requiere teoría de sistemas complejos adaptativos.

La incertidumbre ontológica (no empírica) no puede reducirse con más evidencia

La incertidumbre sobre qué habría ocurrido sin la acción de un actor no es empírica (reducible con mejor observación) sino ontológica (el contrafáctico es estructuralmente inaccesible). La transformación formal, cap. 4.1, establece esta distinción.

Todos los dominios tienen este límite. Es especialmente relevante en los daños históricos (cap. 42, 43, 73) y en los daños diferidos (cap. 64, 67, 75).

El análisis de sensibilidad que establece la robustez de las conclusiones al rango de la incertidumbre ontológica. El sistema declara los supuestos del contrafáctico y establece qué conclusiones son robustas a diferentes supuestos.

El modelo no captura la responsabilidad por el diseño de los supuestos

El analista que usa el sistema para distribuir responsabilidad tiene él mismo

Todos los dominios. Especialmente relevante en los dominios

La transparencia metodológica obligatoria del sistema: el análisis debe declarar los

Taxonomía General de Aplicaciones

Qué dominios

Límite del modelo lineal Por qué ocurre

de la Taxonomía lo

Extensión

posible

enfrentan

del propio modelo

R* sobre las conclusiones que el modelo produce — si el grafo fue construido incorrectamente, si los pesos fueron estimados con sesgo, si el período de análisis fue elegido para favorecer una conclusión.

jurídicos (caps. 1–4) y en los dominios de mayor sensibilidad política (caps. 42–44, 64, 72– 75).

supuestos del grafo, los rangos de los pesos, y las conclusiones que son robustas versus las que dependen de supuestos específicos.

### §5  La causalidad circular en los sistemas sociales: tres casos de la Taxonomía

Caso 1 — El ciclo de la pobreza intergeneracional: la espiral DAG-breaking

El cap. 73 establece que el campo de exclusión diseñado por las políticas estatales tiene R* positivo sobre la pobreza del grupo excluido. Pero esa misma pobreza produce menor capital político del grupo excluido, que produce menor capacidad de cambiar las políticas que la producen, que perpetúa el campo de exclusión. En el análisis puntual del cap. 73, el DAG establece el R* de la política sobre la pobreza — captura la causalidad en una dirección. El ciclo completo requiere modelizar la retroalimentación: la pobreza como condición que reproduce el campo que la produce.

El modelo Prometeo establece el instrumento correcto para el inicio del ciclo (quién diseñó las políticas que iniciaron el campo de exclusión). La extensión dinámica añade la pregunta del ciclo: ¿qué

Taxonomía General de Aplicaciones

actores tienen R* sobre el mantenimiento del ciclo? — los actores que tienen interés en que el ciclo continúe (los beneficiarios del campo de exclusión) y los actores que podrían romper el ciclo (el actor con mayor INCF sobre la intervención que lo rompería) tienen R* sobre el estado estacionario del sistema, no solo sobre el inicio.

Caso 2 — La polarización política: el ciclo de retroalimentación de la confianza

El cap. 44 analiza los procesos electorales y la desinformación con el modelo lineal: el diseñador del sistema de desinformación tiene INCF positivo sobre los resultados electorales sesgados. Pero la polarización política tiene un ciclo de retroalimentación que el DAG no captura: la polarización produce menor confianza en las instituciones, que produce mayor receptividad a la desinformación, que produce mayor polarización. El sistema lineal establece quién diseñó la campaña de desinformación específica; el sistema dinámico pregunta quién tiene R* sobre el estado de polarización del sistema en el tiempo t.

La extensión dinámica es especialmente relevante porque los ciclos de polarización tienen puntos de bifurcación — estados del sistema donde una pequeña perturbación puede producir un cambio de equilibrio cualitativo (de un sistema polarizado a uno más integrado o, en la dirección opuesta, a una crisis institucional). El análisis del INCF en los puntos de bifurcación produce la distribución de responsabilidad más relevante para la intervención: quién tiene R* sobre la condición de posibilidad de los estados de equilibrio alternativos.

Caso 3 — Las redes ecológicas con cascadas tróficas: la emergencia como responsabilidad distribuida

El cap. 65 establece el D_sistémico_cascada: el daño que la pérdida de una especie produce en las demás especies de la red trófica. Esa cascada es un ciclo de retroalimentación ecológica: la pérdida del depredador tope produce el crecimiento de la población de

Taxonomía General de Aplicaciones

herbívoros que produce la degradación de la vegetación que produce la pérdida de hábitat que produce la pérdida de otras especies que afecta la funcionalidad del ecosistema que amplifica el daño inicial. El DAG captura el primer paso de la cascada (la pérdida del depredador como causa del crecimiento de los herbívoros) pero no los pasos posteriores de la retroalimentación.

La responsabilidad del actor que eliminó la especie clave incluye la responsabilidad sobre todos los pasos de la cascada — incluyendo los pasos de retroalimentación que el DAG no puede representar directamente. La estimación del D_sistémico_cascada en el cap. 65 es una aproximación que el peritaje ecológico cuantifica con modelos de redes tróficas más completos que el DAG lineal. El instrumento del R* establece el punto de inicio de la responsabilidad; la modelización de la cascada establece su extensión completa.

### §6  El cierre del sistema: lo que puede y lo que no puede hacer

El capítulo cierra con el inventario de lo que el sistema puede y no puede hacer — la descripción honesta de los límites que define el alcance de la Taxonomía completa.

El sistema puede: distribuir con precisión la responsabilidad causal sobre eventos pasados en sistemas donde la causalidad es aproximadamente lineal o cíclica con ciclos débiles; establecer el INCF de cada nodo en la producción del daño; calibrar la S como la fracción estructural del comportamiento que el sistema produjo; establecer el Δ como el déficit de asunción que el análisis puede dirigir hacia la acción; formalizar las teorías de justicia en vocabulario consistente; y establecer con honestidad los límites de la certeza de cada afirmación con la escala de evidencia correspondiente.

El sistema no puede: establecer por sí solo qué distribución del D_total es justa (requiere una teoría de la justicia que el cap. 76 formaliza pero no elige); predecir el comportamiento futuro de sistemas con causalidad circular dominante; establecer el R* sobre

Taxonomía General de Aplicaciones

estados estacionarios de sistemas con retroalimentación sin las extensiones dinámicas que este capítulo esboza; suplantar el juicio moral con el cálculo causal; ni garantizar que su aplicación no produzca daño cuando el analista construye el grafo con sesgos no declarados o con supuestos no verificados.

La honestidad intelectual del sistema es una condición de su utilidad

Un sistema que promete más de lo que puede dar produce el mismo error que el periodista que publica sin verificar (cap. 71) o el médico que no declara la incertidumbre de su diagnóstico (cap. 59): convierte la apariencia de precisión en fuente de daño. La Taxonomía General de Evidencia es un instrumento operativo del paradigma de Mediación Ontológica — no una máquina de verdades. Su valor está en la organización sistemática de la evidencia, en la coherencia entre los instrumentos, y en la transparencia sobre lo que no puede hacer. Esa transparencia es el α del sistema sobre el Δ entre lo que promete y lo que produce.

— Fin del Capítulo 78 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026
