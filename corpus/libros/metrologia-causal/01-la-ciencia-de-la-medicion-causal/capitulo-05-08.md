PARTE V · Validez y límites de la medición causal

### Capítulo V·8

### Los límites estructurales II: causalidad

### circular

Los grafos con ciclos, la circularidad como información y el

protocolo de descomposición temporal

### I.  La causalidad circular como propiedad real de algunos sistemas

La mayoría de los grafos causales que el sistema analiza son acíclicos o tienen ciclos moderados que no afectan la interpretabilidad de R*. Pero hay sistemas donde la causalidad es genuinamente circular: A influye sobre B que influye sobre A en una retroalimentación mutua que no tiene sentido descomponer unidireccionalmente. En esos sistemas, preguntarse «¿causó A a B o causó B a A?» es hacer la pregunta incorrecta: la respuesta es «los dos simultáneamente, en una relación de co-determinación».

Los ejemplos más frecuentes de causalidad genuinamente circular en los dominios de la Taxonomía: la relación entre el precio de un activo financiero y las expectativas de los inversores sobre ese precio (el precio sube porque los inversores esperan que suba, y los inversores esperan que suba porque está subiendo), la relación entre la confianza

Metrología Causal

institucional y el comportamiento de los ciudadanos (los ciudadanos cumplen las normas porque confían en las instituciones, y las instituciones funcionan porque los ciudadanos las cumplen), la relación entre el abusador y la víctima en ciclos de violencia doméstica (el comportamiento del abusador modifica el comportamiento de la víctima que a su vez modifica el comportamiento del abusador).

La circularidad en estos casos no es un problema a resolver sino una propiedad del sistema a describir. La causalidad circular es la estructura causal del sistema; pretender que no existe — descomponiéndola artificialmente en una dirección única — produce análisis que no representan correctamente cómo funciona el sistema.

### II.  Cuándo el grafo circular produce R* interpretable

La causalidad circular no invalida automáticamente el cálculo de R*. El eigenvector del grafo con ciclos es calculable y el teorema de Perron-Frobenius aplica cuando el grafo es irreducible y aperiódico — condiciones que los grafos con ciclos típicamente satisfacen. La pregunta es si R* calculado sobre un grafo con ciclos tiene interpretación válida como distribución de responsabilidad causal.

La interpretación es válida cuando los ciclos representan retroalimentación real entre nodos que tienen contribuciones causales distinguibles sobre el resultado D. En la relación precio-expectativas, si D es el colapso del precio de un activo, el grafo circular captura correctamente que tanto el nodo «expectativas de los inversores» como el nodo «precio del activo» contribuyeron al colapso — y R* puede distribuir la

Metrología Causal

responsabilidad entre los dos con los pesos proporcionales a sus contribuciones en el ciclo.

La interpretación falla cuando los ciclos representan la misma entidad descrita dos veces. Si el analista ha construido un nodo «política de incentivos» y otro nodo «cultura de la institución» que en realidad son el mismo fenómeno descrito desde dos ángulos diferentes, el ciclo entre los dos nodos es artefactual: no hay dos causas que se retroalimentan, hay una causa descrita dos veces. En ese caso, R* distribuye la responsabilidad entre los dos nodos de manera que no tiene interpretación válida — la aparente distribución entre «política de incentivos» y «cultura de la institución» no refleja dos contribuciones causales distintas.

### III.  El protocolo de descomposición temporal

Cuando el ciclo tiene interpretación válida (retroalimentación real entre nodos distintos) pero la pregunta del análisis es sobre la distribución de responsabilidad en un momento específico del tiempo, el protocolo de descomposición temporal permite tratar el grafo circular como una secuencia de grafos acíclicos en el tiempo.

El protocolo tiene tres pasos. Primero: identificar el período de análisis T que incluye el inicio del ciclo y el momento del resultado D. Segundo: descomponer el ciclo en períodos sucesivos — en el período t₁, A influye sobre B; en el período t₂, B influye sobre A; en el período t₃, el resultado D se produce. Tercero: construir el grafo acíclico dirigido del período T como la superposición de las influencias de todos los subperiodos, con pesos que reflejan la intensidad de la influencia en cada subperiodo.

Metrología Causal

La descomposición temporal convierte el grafo circular en un grafo acíclico sobre el que R* tiene interpretación directa. El precio pagado es la necesidad de especificar los subperiodos y sus pesos, lo que añade supuestos que deben declararse. En contextos adversariales, esos supuestos adicionales pueden ser impugnados; el análisis de sensibilidad sobre los subperiodos es el instrumento para evaluar la robustez de la Declaración ante variaciones de esos supuestos.

Metrología Causal

