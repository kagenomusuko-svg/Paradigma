PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·13

### Las tensiones que revelan los

### documentos leídos juntos

Las inconsistencias internas del expediente como información

diagnóstica de primer orden

### I.  La tensión: Alta Declaración + reporte con muchos puntos de quiebre

La tensión entre Declaración A y un reporte de sensibilidad con muchos puntos de quiebre es la inconsistencia más instructiva del expediente. Si la Declaración A significa que el ranking es estable en todo el hipercubo, ¿cómo puede el reporte tener muchos puntos de quiebre? La respuesta: los puntos de quiebre están todos en los extremos del hipercubo — en los valores de peso que están en los límites del rango plausible de cada arista. El ranking es estable en el interior del hipercubo (que produce la Declaración A) pero frágil en los extremos.

La interpretación de esta tensión: el análisis es robusto ante las interpretaciones centrales de la evidencia, pero frágil ante las interpretaciones más extremas. El adversario que recibe este expediente tiene información útil: si puede demostrar que algún peso pertenece a los extremos del rango (que la

Metrología Causal

influencia es más alta o más baja de lo que el rango central sugiere), el ranking puede cambiar. Esta tensión no debilita la Declaración A — que es técnicamente correcta — pero señala que el análisis tiene vulnerabilidades específicas que el adversario puede explotar si tiene evidencia sobre los pesos extremos.

### II.  La tensión: Baja Declaración + pocos puntos de quiebre

La tensión opuesta es igualmente informativa: una Declaración C o D con muy pocos puntos de quiebre. Esta combinación indica que el análisis tiene incertidumbre alta pero localizada — hay pocos valores de peso que producen cambio de ranking, pero esos pocos valores producen cambios grandes. El análisis no es robusto, pero la razón no es que el ranking sea inestable en general; es que una o dos aristas del grafo tienen rangos tan amplios que cuando esas aristas toman sus valores extremos, el ranking se invierte completamente.

La interpretación: el caso tiene incertidumbre concentrada — pocas aristas críticas con rangos muy amplios. Esto es información diagnóstica valiosa para la investigación: la evidencia adicional que se necesita no es evidencia genérica sobre el caso sino evidencia específica sobre las aristas con puntos de quiebre. En el contexto forense, esas aristas son el objetivo de la investigación complementaria; en el contexto del acompañamiento, son las preguntas que ECO necesita responder para hacer operable el análisis.

### III.  La tensión: Vector con paradoja de visibilidad + hoja sin aristas al nodo invisible

Metrología Causal

La tercera tensión diagnóstica es la más peligrosa: un vector R* que muestra la paradoja de la visibilidad (el nodo de mayor R*_neta tiene poca visibilidad documental) combinada con una hoja de calibración que no tiene aristas con certeza alta desde ese nodo. Esta combinación no es una inconsistencia del análisis — es una señal de alerta sobre la construcción del grafo.

Si el nodo de mayor R*_neta tiene todas sus aristas calibradas con certeza baja (evidencia hipotética), el resultado de R* descansa sobre supuestos que no tienen evidencia sólida. El nodo puede tener R* alto simplemente porque el analista asumió que existe una influencia fuerte sobre los ejecutores, sin evidencia que justifique esa suposición. En ese caso, el análisis de sensibilidad debería producir una Declaración C o D porque los rangos amplios de las aristas hipotéticas producen inestabilidad de ranking.

Si el vector produce Declaración A con aristas de certeza baja para el nodo de mayor R*, hay un problema de calibración: los rangos de las aristas de certeza baja están siendo calibrados con amplitud menor de la que la incertidumbre en la evidencia justifica. El resultado es un análisis que parece robusto pero que está subestimando la incertidumbre real — exactamente el error de producir un número puntual sin análisis de sensibilidad, solo que en forma más sofisticada.

Metrología Causal

