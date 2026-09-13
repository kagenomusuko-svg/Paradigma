PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·1

### Los cuatro documentos: función y

### relación

El expediente como sistema articulado, no como colección de

documentos independientes

### I.  Los cuatro documentos y sus funciones

El expediente de análisis causal tiene cuatro documentos. La hoja de calibración es el mapa del caso: describe la estructura del grafo causal, los nodos incluidos, las aristas y sus pesos, la fuente de evidencia para cada peso y el nivel de certeza asignado. Es el único documento que puede ser construido directamente desde la evidencia disponible sin cálculo; todos los demás se derivan de ella. El vector R* es el resultado del cálculo: la distribución de responsabilidad causal entre los nodos, con R*_neta, S, α y Δ para cada uno. El reporte de sensibilidad es el mapa de robustez: describe cómo varía el ranking de R* cuando los pesos del grafo varían dentro de sus rangos plausibles. La Declaración de robustez es la conclusión: el enunciado formal sobre qué tan sólido es el ranking ante cualquier interpretación razonable de la evidencia.

Los cuatro documentos forman un sistema articulado porque cada uno responde una pregunta distinta que los demás no

Metrología Causal

pueden responder solos. La hoja de calibración responde: «¿qué estructura causal describe el caso?». El vector R* responde: «¿quién tuvo mayor centralidad causal en esa estructura?». El reporte de sensibilidad responde: «¿esa conclusión es estable o cambia si interpretamos la evidencia de otra manera?». La Declaración responde: «¿qué nivel de certeza tiene la conclusión ante un adversario que intente impugnarla?». Ninguna de esas cuatro preguntas puede responderse con uno solo de los documentos.

### II.  La secuencia de producción y por qué el orden importa

Los cuatro documentos se producen en una secuencia fija. Primero la hoja de calibración, porque todos los demás dependen de ella. Segundo el vector R*, calculado sobre el grafo de la hoja de calibración con los pesos centrales. Tercero el reporte de sensibilidad, producido explorando el espacio de parámetros definido por los rangos de la hoja de calibración. Cuarto la Declaración, derivada de la lectura del reporte de sensibilidad sobre la estabilidad del ranking.

La secuencia inversa —comenzar por la Declaración y trabajar hacia atrás— es el error de producción más frecuente y el que produce los análisis más frágiles. Un analista que tiene en mente una Declaración A antes de construir la hoja de calibración tiene un sesgo hacia calibrar los pesos de manera que produzcan esa Declaración. La Declaración producida de esa manera puede ser técnicamente correcta —el ranking puede ser estable en el espacio de parámetros que el analista calibró— pero epistemológicamente frágil porque el espacio de parámetros fue definido para producir esa Declaración, no para reflejar honestamente la incertidumbre en la evidencia.

Metrología Causal

La regla de producción: nunca saber de antemano qué Declaración producirá el análisis. La Declaración es el resultado del análisis, no su punto de partida. El analista que construye la hoja de calibración con los rangos correctos para la evidencia disponible, calcula R* sobre esa hoja, produce el reporte de sensibilidad sobre ese espacio de parámetros y lee la Declaración que el reporte produce —ese analista no está haciendo trampa. El analista que ajusta los rangos para que el reporte produzca la Declaración que quería — ese analista está produciendo evidencia, no análisis.

### III.  La relación de dependencia entre documentos

La dependencia entre los cuatro documentos es asimétrica y en cascada. La hoja de calibración puede leerse sin los demás documentos. El vector R* no puede interpretarse sin la hoja de calibración que lo fundamenta. El reporte de sensibilidad no puede interpretarse sin el vector R* que muestra qué ranking está siendo evaluado. La Declaración no puede interpretarse sin el reporte de sensibilidad que le da su base.

Esta asimetría tiene una implicación directa para el uso del expediente en contextos adversariales: la contraparte que recibe solo la Declaración sin los documentos que la sustentan no tiene los elementos para impugnarla correctamente. La impugnación de una Declaración A requiere atacar los rangos de la hoja de calibración — que es el único lugar donde el adversario puede demostrar que la estructura del caso es diferente a la que el analista describió. Sin la hoja de calibración, el adversario no tiene el objeto correcto para impugnar. Por eso el expediente completo —los cuatro documentos— debe entregarse cuando el análisis se usa en contextos adversariales.

Metrología Causal

Notas al capítulo VI·1

1 La organización del expediente en cuatro documentos con relación de dependencia en cascada tiene un paralelo con la estructura de un peritaje técnico en el sistema legal anglosajón. El peritaje estándar tiene: descripción de los hechos relevantes (equivalente a la hoja de calibración), análisis de los hechos (equivalente al vector R*), evaluación de la robustez del análisis (equivalente al reporte de sensibilidad) y conclusión del perito (equivalente a la Declaración). El sistema de Prometeo formaliza esta estructura con precisión matemática, pero la arquitectura argumentativa es la misma que el sistema legal ya reconoce como válida para el testimonio experto.

Metrología Causal

