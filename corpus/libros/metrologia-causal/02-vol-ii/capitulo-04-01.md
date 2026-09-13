PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·1

### Los cuatro axiomas de la responsabilidad

### causal proporcional

Enunciado formal y justificación de cada axioma

### I.  La función del sistema axiomático

El Teorema de la Responsabilidad Causal Proporcional descansa sobre cuatro axiomas. Los axiomas no son hipótesis empíricas que pueden ser verificadas o refutadas con datos — son condiciones que cualquier distribución de responsabilidad debe satisfacer para ser interpretable como distribución de responsabilidad causal proporcional en el sentido de este sistema. Su función es doble: determinan de manera única la distribución correcta (el Capítulo IV·2 demuestra que solo el eigenvector las satisface simultáneamente) y permiten diagnosticar exactamente qué propiedad se viola cuando una distribución alternativa es propuesta.

Los cuatro axiomas son independientes entre sí: ninguno se sigue de los demás. Y son suficientes en conjunto: cualquier distribución que los satisface simultáneamente es el eigenvector. La demostración de ambas propiedades — independencia y suficiencia conjunta — forma el núcleo del Capítulo IV·2.

Metrología Causal · Vol. II

### II.  Axioma A1 — Eficiencia

Axioma A1 · Eficiencia

Σᵢ R*(i) = 1

La totalidad del resultado D está distribuida entre los nodos causalmente necesarios. Ninguna fracción se pierde ni se inventa.

La eficiencia exige que la distribución cierre: la suma de las responsabilidades causales de todos los nodos es exactamente el resultado total. No puede ser menor — eso significaría que parte del resultado no tiene origen causal asignado, lo que contradice que el grafo incluye todos los nodos causalmente relevantes. No puede ser mayor — eso significaría que el sistema atribuye más responsabilidad de la que el resultado contiene, lo cual es metrológicamente incoherente.

La eficiencia no es una convención aritmética de normalización. Es la condición de que el análisis causal es completo: si el grafo es correcto y todos los nodos causalmente relevantes están incluidos, la suma de sus pesos debe ser exactamente uno. Una distribución que no cumple A1 señala que el grafo está incompleto o que la distribución se calculó incorrectamente.

### III.  Axioma A2 — Causalidad necesaria

Axioma A2 · Causalidad necesaria

R*(i) > 0  □  i es condición sine qua non de D

El nodo i tiene responsabilidad causal positiva si y solo si su eliminación del grafo produce un resultado D' tal que D' ≠ D en su forma específica. Los nodos causalmente irrelevantes tienen R* = 0.

Metrología Causal · Vol. II

La causalidad necesaria vincula la distribución de responsabilidad a la estructura causal del grafo. Un nodo que no es condición necesaria de D — cuya eliminación dejaría D intacto — no tiene responsabilidad causal en D. Asignarle R* > 0 violaría el principio más básico de la causalidad: no se es responsable de algo que hubiera ocurrido igual sin uno.

La dirección inversa del bicondicional es igualmente importante: un nodo que sí es condición necesaria de D debe tener R* > 0. Una distribución que asigna R* = 0 a un nodo que es condición sine qua non viola A2, aunque sea aritméticamente coherente. Esta exigencia es la condición que previene que el análisis omita actores con alta responsabilidad estructural por razones extra-metodológicas.

### IV.  Axioma A3 — Centralidad recursiva

Axioma A3 · Centralidad recursiva

R*(i) es proporcional a Σ□ w_ij · R*(j)

La responsabilidad de un nodo es proporcional a la suma ponderada de las responsabilidades de los nodos sobre los que ejerce influencia causal. La responsabilidad se propaga recursivamente a través de toda la estructura del grafo.

La centralidad recursiva captura la dimensión más importante de la responsabilidad en sistemas complejos: que la influencia no es solo directa. Un nodo que influye sobre nodos intermedios que a su vez influyen sobre el resultado final tiene responsabilidad causal que va más allá de sus aristas directas al nodo sumidero. El diseñador que produce el incentivo que produce la conducta que produce el daño es responsable no solo de su arista directa al daño sino de toda la cadena causal que su diseño habilitó.

Metrología Causal · Vol. II

Sin la centralidad recursiva, el análisis causal sería superficial: mediría quién actuó en el último paso, ignorando quién construyó el sistema que hizo posible ese último paso. A3 es el axioma que hace al sistema capaz de identificar la responsabilidad estructural de los nodos de diseño, que frecuentemente no tienen aristas directas al resultado, pero tienen R* alto porque su influencia se ejerce a través de múltiples niveles del grafo.

### V.  Axioma A4 — Monotonicidad

Axioma A4 · Monotonicidad

Si w_ji aumenta → R*(i) no decrece

Si la influencia del nodo j sobre el nodo i se intensifica, la responsabilidad causal de i no puede disminuir. Más influencia causal recibida no reduce la centralidad causal del receptor.

La monotonicidad es la condición de coherencia ordinal del sistema. Si un nodo recibe más influencia causal de otros nodos, su posición causal en el resultado no puede ser menor que antes. Una distribución que viola A4 produciría la paradoja de que un nodo con más influencia sobre el resultado tiene menos responsabilidad, lo que contradice el principio de que la responsabilidad causal crece con la influencia estructural.

A4 también tiene una consecuencia importante para el análisis de sensibilidad de la Serie III: cuando los pesos del grafo varían dentro de sus rangos admisibles, el ranking de los nodos solo puede cambiar de maneras consistentes con la monotonicidad. Un nodo no puede ganar influencia y perder posición en el ranking simultáneamente.

Metrología Causal · Vol. II

Axioma Nombre Condición Lo que viola si se relaja

A1 Eficiencia Σᵢ R*(i) = 1 La distribución no cubre todo el resultado o lo excede. El análisis es incompleto o sobrecontribuyente.

A2 Causalidad necesaria

R*(i) > 0 □ condición sine qua non

Nodos irrelevantes reciben responsabilidad, o nodos necesarios son ignorados. El vínculo entre causalidad y responsabilidad se rompe.

A3 Centralidad recursiva

R*(i) □ Σ□ w_ij · R*(j)

La responsabilidad es solo directa. Los nodos de diseño con influencia indirecta son invisibles al análisis.

A4 Monotonicidad ↑w_ji □ R*(i) no decrece

Más influencia produce menos responsabilidad. El análisis viola coherencia ordinal básica.

### Producto de salida · Capítulo IV·1

Los cuatro axiomas formalmente enunciados con su justificación. Cualquier distribución de responsabilidad causal proporcional debe satisfacerlos simultáneamente. El Capítulo IV·2 demuestra que exactamente una distribución los satisface: el eigenvector principal normalizado de W.

Notas al Capítulo IV·1

1  La independencia de los cuatro axiomas puede verificarse mostrando que para cada axioma existe una distribución que satisface los tres restantes,

Metrología Causal · Vol. II

pero viola ese axioma específico. Para A3: la distribución de pesos directos al sumidero (sin propagación recursiva) satisface A1, A2 y A4, pero viola A3. La demostración completa de independencia está en el apéndice de la Axiomatización del Sistema de la Doble Mediación.

2  El axioma A2 formula la condición sine qua non en términos de forma específica del resultado: 'D' ≠ D en su forma específica'. Esta precisión es metrológicamente crítica. Si un nodo es eliminado del grafo y el resultado ocurre con menor magnitud, pero la misma forma, el nodo no es condición sine qua non bajo A2. Si el resultado ocurre en una forma diferente, sí lo es. La distinción entre magnitud y forma del resultado tiene consecuencias directas para la aplicación en dominios donde la forma del resultado importa más que su magnitud.

Metrología Causal · Vol. II

