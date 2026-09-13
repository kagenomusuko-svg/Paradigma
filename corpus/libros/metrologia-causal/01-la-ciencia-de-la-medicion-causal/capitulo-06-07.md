PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·7

### El reporte de sensibilidad I: estructura y

### producción

El algoritmo de exploración del espacio de parámetros y los

criterios de cobertura

### I.  Qué contiene el reporte de sensibilidad

El reporte de sensibilidad tiene tres componentes. El primero es la función de ranking: para cada punto del hipercubo de parámetros Π_ij [a_ij, b_ij], la posición de cada nodo en el ranking de R*. El segundo es la tabla de puntos de quiebre: los puntos del hipercubo donde el ranking cambia — donde un nodo desplaza a otro del primer lugar, o donde el tercer lugar cambia con el cuarto. El tercero es la función de robustez: para cada umbral de cobertura del hipercubo (el porcentaje del hipercubo en el que el ranking es estable), el nivel de confianza de la Declaración correspondiente.

La función de ranking no puede calcularse de manera exhaustiva para hipercubos de alta dimensión (un grafo de diez aristas tiene un hipercubo de diez dimensiones), pero puede calcularse con cobertura suficiente usando muestreo sistemático. El muestreo estándar explora las esquinas del hipercubo (todos los extremos de todos los rangos), el centro

Metrología Causal

del hipercubo (los puntos centrales de todos los rangos), y un muestreo aleatorio del interior. Para grafos de hasta veinte aristas, la cobertura con esquinas + centro + 500 puntos aleatorios es típicamente suficiente para la Declaración.

### II.  El algoritmo del análisis de sensibilidad

El algoritmo procede en seis pasos. Paso 1: construir el hipercubo Π_ij [a_ij, b_ij] desde la hoja de calibración. Paso 2: seleccionar los puntos del hipercubo a explorar (esquinas + centro + puntos aleatorios). Paso 3: para cada punto seleccionado, construir la matriz W con esos valores de w_ij, calcular el eigenvector principal y registrar el ranking. Paso 4: identificar los puntos de quiebre — los puntos en los que el ranking difiere del ranking del punto central. Paso 5: calcular la función de robustez — el porcentaje de puntos explorados en los que el ranking es el mismo que en el punto central. Paso 6: producir la Declaración correspondiente según la función de robustez.

Los puntos de quiebre son la información más valiosa del reporte. Un punto de quiebre específico — «cuando w_FRO→ECP = 0.42 y w_ECP→D = 0.78, ECP desplaza a FRO del primer lugar» — describe exactamente qué supuesto sobre la evidencia haría cambiar la conclusión. La contraparte que quiere impugnar la Declaración necesita demostrar que ese supuesto es el correcto — que la influencia de FRO sobre ECP es ≤ 0.42 o que la influencia de ECP sobre D es ≥ 0.78. Esa demostración requiere atacar la evidencia específica que fundamenta esos rangos.

### III.  Los criterios de cobertura del espacio de parámetros

Metrología Causal

La cobertura suficiente del hipercubo para producir cada nivel de Declaración varía con el estándar requerido. Para la Declaración A (ranking estable con cualquier interpretación razonable), la cobertura mínima es explorar todas las esquinas del hipercubo más el centro. Si el ranking es el mismo en todos esos puntos, la Declaración A está justificada porque las esquinas representan las interpretaciones más extremas de la evidencia: si el ranking no cambia en los extremos, no cambiará en el interior.

Para la Declaración B (ranking estable en la mayoría de las interpretaciones razonables), la cobertura estándar es esquinas + centro + 200 puntos aleatorios. La Declaración B se produce cuando el ranking es estable en el 90% o más de los puntos explorados, con inestabilidad concentrada en las esquinas extremas del hipercubo. Para la Declaración C (ranking inestable en una fracción significativa), la exploración con 500 puntos aleatorios es suficiente para establecer el patrón de inestabilidad con confianza. La Declaración D no requiere exploración completa: si el ranking cambia en el punto central y los puntos centrales adyacentes, la Declaración D está justificada sin necesidad de explorar el hipercubo completo.

Metrología Causal

