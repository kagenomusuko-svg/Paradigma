PARTE I · El flujo de trabajo del mediador

### Capítulo I·6

### El protocolo de decisión entre eigenvector y

### Shapley

Cuándo cada método aplica y cómo elegir

### I.  El problema que este capítulo resuelve

El sistema tiene dos métodos de cálculo de responsabilidad causal: el eigenvector principal de W y el valor de Shapley. El Volumen I establece cuándo cada uno es matemáticamente válido [Vol.I · Cap. VII·3]. Este capítulo establece cómo el mediador identifica, desde la estructura del grafo que tiene delante, cuál de los dos métodos aplica a su caso.

La confusión entre los dos métodos no es un error de cálculo: es un error de tipo. Aplicar el eigenvector cuando la condición que lo justifica no se cumple produce R* que mide centralidad estructural pero no responsabilidad causal. Aplicar Shapley cuando el eigenvector es el método correcto produce un cálculo más costoso computacionalmente que produce el mismo resultado. El primero error es sustantivo; el segundo, ineficiente. Este capítulo previene ambos.

Metrología Causal · Vol. II

### II.  El eigenvector: condición de aplicación

El eigenvector principal de W es el método correcto cuando al menos uno de los nodos del grafo es individualmente condición sine qua non del resultado D. Un nodo i es condición sine qua non de D si, al eliminar i del grafo y todas sus aristas, el resultado D no puede ocurrir en su forma específica a través de los nodos y aristas restantes.

La condición sine qua non individual es una condición estructural del grafo, no una condición empírica. El mediador no la verifica experimentalmente —el evento ya ocurrió. La verifica estructuralmente: ¿existe en G algún camino alternativo de cualquier otro nodo a D que no pase por i, con peso total suficiente para producir D en su forma específica? Si no existe ese camino alternativo, i es condición sine qua non individual.

El eigenvector mide cuánto de D se explica por la posición estructural de cada nodo en el grafo, tomando en cuenta no solo la influencia directa sino la indirecta a través de todos los caminos. Su validez como medida de responsabilidad causal descansa sobre la condición de que al menos un nodo sea condición necesaria individual: sin esa condición, la distribución eigenvectorial no tiene la interpretación causal que R* requiere.

Vol.I · Cap. VII·3

### III.  El valor de Shapley: condición de aplicación

El valor de Shapley es el método correcto cuando ningún nodo del grafo es individualmente condición sine qua non de D. Esto ocurre cuando las contribuciones de los nodos son genuinamente no separables: cada nodo solo produce D en conjunto con otros nodos, y no existe ningún nodo cuya eliminación sola impediría D.

Metrología Causal · Vol. II

El caso Shapley no es infrecuente en la práctica. Es el caso de los sistemas donde el resultado emerge de la intersección de múltiples condiciones necesarias colectivamente pero no individualmente: la falla sistémica que requiere que todos los controles fallen simultáneamente, el resultado social que requiere que múltiples actores mantengan su conducta en paralelo, el colapso organizacional que resulta de la acumulación de decisiones ninguna de las cuales sola lo habría producido.

En el caso Shapley, la distribución de responsabilidad es el valor de Shapley de la función característica v(S) donde S es cualquier coalición de nodos y v(S) es la fracción del resultado D que la coalición S puede producir por sí sola. El valor de Shapley de cada nodo es su contribución marginal promedio sobre todas las coaliciones posibles en las que podría participar.

### IV.  El test de decisión: la prueba de condición sine qua non

El test de decisión se aplica nodo por nodo sobre el grafo construido. Para cada nodo i, el mediador responde la siguiente pregunta estructural: eliminado i del grafo, ¿existe algún conjunto de nodos restantes suficiente para producir D en su forma específica?

El test de condición sine qua non individual · Protocolo

Paso 1: Identificar el nodo candidato i y el resultado específico D (el nodo sumidero Nf).

Paso 2: Eliminar i y todas sus aristas del grafo. Llamar G' al grafo resultante.

Metrología Causal · Vol. II

Paso 3: Verificar si en G' existe al menos un camino desde cualquier nodo fuente a Nf con peso acumulado suficiente para producir D en su forma específica.

Resultado A — No existe ese camino: i es condición sine qua non individual → el eigenvector es el método correcto.

Resultado B — Existe ese camino: i no es condición sine qua non individual → i no funda por sí solo la condición del eigenvector.

Decisión final: si al menos un nodo produce Resultado A → eigenvector. Si todos los nodos producen Resultado B → Shapley.

### V.  Los casos mixtos y la conjetura del operador unificador

Un caso mixto es un grafo donde algunos nodos son condición sine qua non individual y otros no lo son. En ese caso, la teoría del sistema predice que el eigenvector es el método correcto para la distribución global — porque la condición que funda su validez se cumple para al menos un nodo— pero que los nodos que no son individualmente sine qua non tienen una componente de su R* que el eigenvector distribuye de manera diferente a como lo haría Shapley.

El sistema maneja los casos mixtos con el eigenvector como método primario y el Shapley como verificación secundaria para los nodos que no son individualmente sine qua non. Si los dos métodos producen valores similares para esos nodos, el eigenvector se usa como resultado definitivo. Si producen valores significativamente diferentes, se documenta la diferencia y se reporta al destinatario como incertidumbre estructural del análisis.

La conjetura del operador unificador — la demostración formal de que existe un operador que produce el eigenvector en el caso sine qua non y el Shapley en el caso no-sine-qua-non,

Metrología Causal · Vol. II

interpolando entre ellos en casos mixtos — está formulada con precisión en el Capítulo IV·7 de este volumen y en la Axiomatización del Sistema de la Doble Mediación. Es el programa de investigación abierto más importante del paradigma. Los precedentes de la literatura que apuntan en esta dirección (Hu & Shapley 2003, Teng 2016, Aleandri et al. 2025) sugieren que la conjetura es verdadera, pero la demostración completa no existe aún.

### Producto de salida · Capítulo I·6

Decisión de método de cálculo: eigenvector (si al menos un nodo supera el test de condición sine qua non) o Shapley (si ningún nodo la supera), con la documentación del test aplicado. En casos mixtos: eigenvector primario con verificación Shapley sobre los nodos no-sine-qua-non y documentación de la diferencia.

Notas al Capítulo I·6

1  El "peso acumulado suficiente" del Paso 3 del test requiere una aclaración operativa. En términos del grafo, significa que el camino alternativo en G' produce un resultado D' tal que D' = D en su forma específica — no en alguna forma aproximada. Si la eliminación de i produciría un resultado cuantitativamente menor pero cualitativamente idéntico, i no es condición sine qua non: el resultado habría ocurrido de todas formas, solo con menor intensidad. Si la eliminación de i produciría un resultado cualitativamente diferente, i es condición sine qua non.

2  La confusión entre la fórmula I = R* × (1−S) × (1−α) —que circuló en la conversación con modelos de lenguaje externos— y el sistema formal merece una aclaración explícita. Esa fórmula combina dos corolarios del Teorema (R*_neta y Δ) en una sola cantidad que el sistema no define como tal. R*_neta = R* × (1−S) mide la fracción idiosincrática del peso causal. Δ = R* × (1−α) mide el déficit de asunción. Son cantidades independientes con interpretaciones distintas. El producto de las dos es

Metrología Causal · Vol. II

una cantidad sin nombre en el sistema formal porque no tiene interpretación metrológica propia.

Metrología Causal · Vol. II

