PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·3

### La hoja de calibración II: cómo leerla

El mapa del caso antes del cálculo y la paradoja de la visibilidad

### I.  La hoja como mapa previo al cálculo

La hoja de calibración es el único documento del expediente que un analista experimentado puede leer para tener una hipótesis sólida sobre el resultado de R* antes de hacer ningún cálculo. La estructura del grafo — quién tiene más aristas salientes, qué nodos están en el trayecto de más caminos hacia D, qué nodo tiene el peso promedio más alto en sus aristas — informa sobre la distribución de R* que el eigenvector producirá. El analista que lee la hoja y no tiene ninguna hipótesis sobre R* antes del cálculo no ha leído la hoja con la atención que merece.

La lectura de la densidad de aristas: un nodo con muchas aristas salientes de alto peso es un candidato para R* alto, pero no necesariamente el de mayor R*. Un nodo con pocas aristas salientes, pero hacia nodos que tienen muchas aristas salientes de alto peso puede tener R* mayor que el nodo más activo directamente. Esta es la propiedad del eigenvector que distingue la centralidad de grado de la centralidad de eigenvector: no es cuántas conexiones tiene sino cuán centrales son los nodos a los que conecta.

Metrología Causal

La lectura de la distribución de pesos: los rangos amplios señalan las aristas que el análisis de sensibilidad identificará como puntos de quiebre potenciales. Una arista con rango [0.20, 0.70] tiene una incertidumbre de 0.50 en su peso — puede ser casi cinco veces más intensa o casi cinco veces menos intensa que el valor central. Esa variabilidad significa que el ranking de R* puede cambiar sustancialmente según cómo se calibre esa arista. La hoja muestra, antes del cálculo, dónde está la fragilidad del análisis.

### II.  Cómo detectar al nodo de alta R* que no aparece en el centro del grafo visual

Los grafos causales de sistemas complejos tienen frecuentemente un nodo de alta R* que no está en el centro del grafo visual. La visualización estándar de un grafo tiende a colocar en el centro los nodos con más conexiones — los que tienen mayor centralidad de grado. Pero el nodo de mayor R* (centralidad de eigenvector) puede tener pocas conexiones directas y estar en la periferia visual del grafo, mientras ejerce su influencia a través de los nodos centrales que él colocó en posición de influencia.

La señal de alerta en la hoja de calibración: si hay un nodo en N cuyas aristas salientes tienen pesos sistemáticamente más altos que el promedio, pero ese nodo tiene pocas aristas, es un candidato para la paradoja de la visibilidad. Su influencia no está en el volumen de sus conexiones sino en la intensidad de cada una. El nodo que diseñó el campo con alta intensidad para dos o tres nodos ejecutores puede tener R* mayor que un nodo ejecutor con diez aristas de baja intensidad.

El protocolo de detección de la paradoja en la hoja: para cada nodo, calcular el producto (número de aristas salientes) × Metrología Causal

(peso promedio de las aristas salientes) × (posición en la jerarquía causal). El nodo cuyo producto es mayor que el de su número de aristas sugiere es el candidato para la paradoja. Este cálculo informal es un atajo antes del eigenvector — no reemplaza el cálculo, pero orienta la lectura de la hoja hacia el nodo correcto.

### III.  Los errores frecuentes de lectura de la hoja

El error más frecuente: identificar como el nodo de mayor responsabilidad al nodo con el mayor número de aristas salientes en el grafo, sin considerar la posición de esos nodos y el peso de las aristas. Este error reproduce la paradoja de la visibilidad desde el análisis: el analista identifica al ejecutor más activo como el más responsable, por la misma razón que el sistema jurídico identifica al ejecutor más visible.

El segundo error frecuente: no registrar las aristas que no tienen evidencia documental directa porque el analista no quiere incluir supuestos sin documentación. Este error produce el Error Tipo III (frontera incorrecta): el nodo de diseño que influye a través de presión informal, cultura organizacional o mecanismos de incentivos no documentados queda fuera del grafo. El resultado es exactamente el análisis que el sistema fue creado para corregir: alta R* de los ejecutores, invisibilidad del diseñador.

Metrología Causal

