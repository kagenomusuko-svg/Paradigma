PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·9

### La Declaración de robustez: las cuatro

### declaraciones

Las condiciones formales, el contenido exacto y lo que cada una

dice sobre el caso

### I.  Declaración A: el ranking es estable en todo el espacio de parámetros

La Declaración A se produce cuando el ranking de R* es el mismo en todos los puntos del hipercubo explorados, incluyendo todas las esquinas. La formulación estándar: «Con cualquier interpretación razonable de la evidencia disponible — incluyendo los supuestos más extremos dentro del rango plausible de cada peso — el nodo [i] tiene mayor responsabilidad causal que cualquier otro nodo del grafo analizado. Para impugnar esta Declaración, la contraparte debe demostrar que existe algún valor de algún peso w_ij que sea consistente con la evidencia y que, bajo ese valor, el nodo [i] ya no es el de mayor responsabilidad causal.»

La Declaración A no afirma que el análisis sea exhaustivo, que el grafo incluya todos los nodos causalmente relevantes, ni que los rangos de peso sean los únicos rangos posibles. Afirma exclusivamente que el ranking es estable dentro del espacio de

Metrología Causal

parámetros definido por los rangos calibrados. Si la contraparte quiere impugnar la Declaración A, tiene dos caminos: demostrar que algún peso está fuera de su rango (ataque a la calibración) o demostrar que hay un nodo causalmente relevante que no está en el grafo (ataque a la frontera). Ninguno de los dos ataques es sobre el número R*; son sobre la construcción del análisis.

### II.  Declaración B: el ranking es estable en la mayoría de las interpretaciones razonables

La Declaración B se produce cuando el ranking es estable en el 90% o más de los puntos explorados, con inestabilidad concentrada en los extremos del hipercubo. La formulación estándar: «Con la gran mayoría de las interpretaciones razonables de la evidencia disponible, el nodo [i] tiene mayor responsabilidad causal. Las excepciones se producen solo bajo supuestos extremos sobre [aristas específicas identificadas en el reporte]. Para impugnar esta Declaración, la contraparte debe demostrar que los supuestos extremos que producen el cambio de ranking son en realidad los supuestos más plausibles dado [la evidencia específica de esas aristas].»

La Declaración B es la declaración de mayor uso práctico en el sistema porque refleja la condición real de la mayoría de los análisis: evidencia suficiente para el caso central, incertidumbre residual en los extremos. La Declaración B no es una versión débil de la A; es la declaración correcta para el nivel de evidencia disponible. En el estándar de preponderancia de la evidencia (proceso civil), la Declaración B es típicamente suficiente. En el estándar de «más allá de toda duda razonable» (proceso penal), la Declaración B justifica el inicio de la acción, pero puede ser insuficiente para la condena.

Metrología Causal

### III.  Declaración C y Declaración D

La Declaración C se produce cuando el ranking es inestable en una fracción significativa del hipercubo — entre el 15% y el 50% de los puntos explorados muestran un ranking diferente. La formulación: «El análisis sugiere que el nodo [i] tiene alta probabilidad de ser el de mayor responsabilidad causal, pero la evidencia disponible no permite afirmar que esa conclusión es robusta ante todas las interpretaciones razonables. La incertidumbre se concentra en [aristas específicas]. Para elevar esta Declaración al nivel B o A, se requiere evidencia adicional sobre [tipo de evidencia que estrecharía los rangos de esas aristas].»

La Declaración C es el instrumento más útil para la investigación: señala exactamente qué evidencia adicional cambiaría la conclusión del análisis y la llevaría a una Declaración más robusta. El fiscal que recibe una Declaración C sabe dónde buscar — el reporte de sensibilidad le indica qué aristas tienen puntos de quiebre en el interior del hipercubo y qué tipo de evidencia estrecharía esos rangos. La Declaración C no es un fracaso: es una instrucción de investigación.

La Declaración D se produce cuando el análisis no puede establecer ningún ranking estable con los datos disponibles — el ranking cambia incluso en la vecindad del punto central, lo que indica que la evidencia es insuficiente para distinguir entre los nodos con suficiente confianza. La Declaración D no invalida el análisis; establece que el análisis ha llegado al límite de lo que la evidencia permite afirmar. La formulación: «La evidencia disponible no permite establecer con el nivel mínimo de robustez requerido qué nodo tiene mayor responsabilidad causal. El análisis ha identificado los nodos plausiblemente centrales —[lista]— pero no puede discriminar entre ellos con el estándar requerido.»

Metrología Causal

Notas al capítulo VI·9

1 Las cuatro declaraciones A–D tienen un paralelo conceptual con los estándares de evidencia en la práctica científica. La Declaración A corresponde a la certeza que la física teórica requiere para una demostración formal: válida bajo cualquier interpretación razonable. La Declaración B corresponde al estándar de la evidencia estadística con p < 0.05: válida bajo la gran mayoría de condiciones, con excepciones en los extremos. La Declaración C corresponde a una tendencia estadísticamente sugerida: hay una señal, pero no es concluyente. La Declaración D corresponde a datos insuficientes: no se puede hacer ninguna afirmación con el nivel mínimo de confianza.

Metrología Causal

