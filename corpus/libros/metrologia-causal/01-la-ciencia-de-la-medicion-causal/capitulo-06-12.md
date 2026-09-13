PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·12

### El expediente integrado: la secuencia de

### lectura correcta

Por qué el expediente debe leerse en secuencia y lo que cada

documento añade al anterior

### I.  La secuencia correcta de lectura

El expediente debe leerse en la misma secuencia en que fue producido: hoja de calibración → vector R* → reporte de sensibilidad → Declaración. Esta secuencia no es arbitraria — es la secuencia que permite que cada documento sea interpretado con el contexto correcto que solo los documentos anteriores pueden proveer.

La hoja de calibración se lee primero porque es el único documento que puede leerse sin contexto: describe la estructura del grafo tal como el analista la construyó, con la evidencia que fundamenta cada arista y los rangos que reflejan la incertidumbre en esa evidencia. El lector que comienza por la hoja de calibración puede formarse una hipótesis sobre el resultado de R* antes de leerlo, lo que le permite verificar si el vector R* es consistente con su lectura de la estructura causal.

Metrología Causal

El vector R* se lee después de la hoja porque el vector tiene sentido solo como resultado del eigenvector de la hoja. Sin la hoja, el vector es un conjunto de números sin fundamento. Con la hoja, el vector puede verificarse: el lector puede confirmar que los nodos con mayor R* son los que la hoja sugería como candidatos, y puede detectar si hay inconsistencias entre la estructura del grafo y la distribución de R*.

El reporte de sensibilidad se lee después del vector porque el reporte describe la variación de un ranking — el ranking del vector. Sin saber qué ranking es el que se está evaluando, el reporte no tiene objeto. Con el ranking del vector como referencia, el reporte responde: «¿este ranking es estable o no?» Los puntos de quiebre del reporte señalan las aristas de la hoja que son críticas para la estabilidad del ranking.

La Declaración se lee al final porque es la síntesis de todo lo anterior en una afirmación procesable. Sin la hoja, el vector y el reporte, la Declaración es una conclusión sin fundamento verificable. Con los tres documentos anteriores, la Declaración puede verificarse: el lector puede confirmar que la Declaración A se sigue del hecho de que el ranking es estable en todas las esquinas del hipercubo definido por los rangos de la hoja.

### II.  La secuencia inversa como error frecuente

La secuencia inversa — leer la Declaración primero y luego buscar soporte en los demás documentos — es el error de lectura más frecuente, especialmente en contextos donde el lector tiene un interés en el resultado. Un fiscal que recibe un expediente con Declaración A busca en los documentos siguientes la evidencia que sostiene esa Declaración; no está leyendo el expediente sino confirmando su conclusión previa. Un abogado defensor que recibe el mismo expediente con

Metrología Causal

Declaración A busca en los documentos las inconsistencias que la debilitan; tampoco está leyendo el expediente sino atacando su conclusión.

Ambas lecturas son legítimas en contextos adversariales — el fiscal y el defensor tienen roles que requieren esas lecturas. El problema surge cuando esas lecturas se confunden con la lectura analítica del expediente. El juez, el árbitro o el regulador que quiere entender la estructura del caso debe leer en secuencia, no en función de su posición respecto al resultado.

El protocolo para lectores en posición adversarial: leer la Declaración para saber qué nivel de robustez afirma, leer el reporte para identificar qué supuestos son críticos para esa robustez, y leer la hoja para verificar si la evidencia que fundamenta esos supuestos es sólida. Esta lectura estratégica es la inversa de la secuencia analítica, pero es legítima porque no confunde su propósito: identifica dónde atacar, no qué dice el expediente.

Metrología Causal

