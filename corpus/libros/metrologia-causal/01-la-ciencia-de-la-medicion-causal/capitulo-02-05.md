PARTE II · Los fundamentos formales de la medición

### Capítulo II·5

### R* I: el eigenvector como medida de

### centralidad causal

Por qué el eigenvector y no otras medidas de centralidad

### I.  Las cuatro medidas estándar de centralidad en grafos

La teoría de redes provee varias medidas de centralidad que cuantifican la importancia de un nodo en una red. La centralidad de grado (degree centrality) mide el número de conexiones directas del nodo: cuántas aristas entran y salen. En un grafo ponderado, es la suma de los pesos de las aristas directas. La centralidad de intermediación (betweenness centrality) mide cuántos caminos más cortos entre pares de nodos pasan a través del nodo en cuestión: cuántas veces el nodo actúa como intermediario. La centralidad de cercanía (closeness centrality) mide la inversa de la distancia promedio desde el nodo a todos los demás: cuán próximo está el nodo al resto de la red. La centralidad de eigenvector (eigenvector centrality) asigna a cada nodo un peso proporcional a la suma de los pesos de eigenvector de sus vecinos: es la medida recursiva de centralidad.

Metrología Causal

Cada una de estas medidas captura un aspecto distinto de la estructura de la red. La centralidad de grado captura la actividad directa: cuántas influencias directas tiene el nodo. La betweenness captura el control de flujo de información: cuántos intercambios dependen de que el nodo esté presente. La closeness captura la accesibilidad: cuán eficientemente puede el nodo alcanzar a todos los demás. El eigenvector captura la influencia recursiva: cuán importante es el nodo dado que sus vecinos son importantes.

### II.  Por qué el eigenvector es la medida correcta para R*

La centralidad de grado no es la medida correcta para R* por una razón fundamental: no distingue entre conectarse a nodos importantes y conectarse a nodos irrelevantes. Un nodo que influye sobre diez nodos de baja centralidad causal tiene la misma centralidad de grado que un nodo que influye sobre un único nodo de centralidad causal máxima. Para la imputación causal, estas dos posiciones son completamente distintas: el primero difunde su influencia en diez direcciones de poca importancia; el segundo concentra toda su influencia en el nodo que más determina el resultado.

La betweenness no es la medida correcta porque captura el control de flujo de información, no la influencia causal. Un nodo puede estar en el camino de muchos intercambios de información sin ser causalmente central en el resultado. En sistemas institucionales, el secretario que pasa los documentos entre departamentos tiene betweenness alta, pero R* bajo; el director que diseñó los procedimientos que los documentos implementan tiene betweenness baja, pero R* alto. La betweenness mide posición en la estructura de comunicación; R* mide posición en la estructura causal.

Metrología Causal

El eigenvector es la medida correcta porque captura exactamente lo que la causalidad necesaria requiere: la importancia de un nodo en función de la importancia de los nodos sobre los que influye. El nodo i tiene eigenvector alto si tiene influencia sobre nodos j que a su vez tienen influencia alta sobre el resultado D. Esta propiedad recursiva —ser central porque se influye sobre lo central— es precisamente la estructura de la responsabilidad en sistemas complejos donde el diseñador del campo influye sobre los ejecutores que a su vez producen el acto que causa el daño.

### III.  El eigenvector como solución al problema de la responsabilidad mutua

Hay un problema que las medidas no-recursivas de centralidad no pueden resolver y que el eigenvector resuelve por construcción: el problema de la responsabilidad mutua. En sistemas donde A influye sobre B que a su vez influye sobre C que a su vez influye sobre A (retroalimentación), la pregunta «¿cuánto causó A?» no tiene respuesta directa en términos de influencias directas porque A es causa y efecto simultáneamente a través de la cadena.

El eigenvector resuelve este problema buscando el punto fijo de la propagación de influencias: la distribución de scores R* que es consistente consigo misma bajo la estructura del grafo. Si R*_i = λ⁻¹ Σⱼ w_ji R*_j para todo i (donde λ es el eigenvector principal), entonces la distribución R* es estable: la centralidad de cada nodo es exactamente la que se sigue de la centralidad de sus vecinos, sin ninguna contradicción. El eigenvector no asigna arbitrariamente los scores; los deriva de la estructura del grafo como su punto fijo.

Metrología Causal

Esta propiedad tiene una interpretación ontológica directa: R* es la distribución de responsabilidad que es consistente con la estructura causal del sistema. Si R*_i es alto, es porque la posición de i en el grafo justifica ese score de manera recursiva —porque i influye sobre nodos importantes que influyen sobre el resultado de maneras que a su vez reflejan la importancia de i. No hay asignación arbitraria; hay derivación estructural.

Metrología Causal

