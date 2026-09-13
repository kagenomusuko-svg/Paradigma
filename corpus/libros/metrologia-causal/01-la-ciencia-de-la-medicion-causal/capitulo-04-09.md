PARTE IV · Las tres preguntas del instrumento

### Capítulo IV·9

### Consecuencias prácticas: moverse entre

### series

Cómo la identidad estructural habilita el análisis multi-serie y la

verificación cruzada

### I.  La traducción entre series: el principio y sus condiciones

El mediador que entiende la identidad estructural de las tres series puede traducir el análisis de una a los términos de otra. La traducción no es trivial —requiere ajustar los parámetros de consulta— pero es sistemática porque el operador es el mismo. Las condiciones de traducción: para traducir de Serie I a Serie III, se necesita reescalar los rangos de peso al estándar adversarial y producir la Declaración de robustez. Para traducir de Serie III a Serie II, se necesita incorporar el IIC como modulador de las aristas del nodo de diseño y convertir la Declaración en ajuste debitor.

Hay un límite importante en la traducción: la evidencia que es suficiente para la Serie I puede no ser admisible para la Serie III. Un análisis de Serie I puede incorporar inferencias sobre las aristas del grafo que no están documentadas en evidencia admisible pero que son plausibles dado el conocimiento del

Metrología Causal

campo. Un análisis de Serie III solo puede incorporar aristas cuya existencia puede demostrarse ante el foro con los estándares de ese foro. La traducción de Serie I a Serie III puede requerir identificar las aristas que no tienen evidencia admisible y retirarlas del grafo, con el impacto en R* que eso implica.

La traducción de Serie II a Serie I no tiene restricciones adicionales: la Serie II tiene más componentes (el IIC, las aristas prospectivas) que la Serie I, así que la reducción es una simplificación, no una extensión. La traducción de Serie II a Serie III requiere, además de los ajustes de evidencia, determinar si el fraude annona es imputable formalmente en el foro correspondiente — lo que depende de las normas del sistema jurídico aplicable, no del análisis causal.

### II.  Casos donde el mismo expediente requiere análisis de múltiples series

El caso Altamirano es el ejemplo central de análisis multi-serie en este libro, pero el patrón es general. Los casos donde el análisis multi-serie agrega valor son los casos donde el mismo sistema causó el daño de múltiples maneras simultáneamente: por actos específicos de ejecutores (Serie III), por brechas entre el diseño declarado y la operación real (Serie II), y por una estructura causal que vale la pena comprender para prevenir que se repita (Serie I).

Los tres tipos de casos más frecuentes que requieren análisis multi-serie. Primero: los casos de responsabilidad organizacional con consecuencias legales — donde la institución tiene responsabilidad por el diseño del campo (Serie II), los ejecutores tienen responsabilidad individual (Serie III) y hay un contexto causal que la investigación forense

Metrología Causal

necesita para construir el caso completo (Serie I). Segundo: los casos de política pública con litigio — donde el Estado tiene responsabilidad por el diseño de la política (Serie II), funcionarios específicos tienen responsabilidad por actos de ejecución (Serie III) y el análisis de impacto de la política necesita la Serie I. Tercero: los casos de daño ambiental acumulativo — donde la Serie I describe la distribución de contribuciones causales, la Serie II mide la brecha entre los estándares ambientales declarados y la operación real, y la Serie III produce la imputación proporcional entre las empresas implicadas.

### III.  La verificación cruzada entre series como control de calidad

Cuando el mismo caso ha sido analizado en más de una serie, los resultados deben ser mutuamente consistentes. Si la Serie I produce R*_diseñador = 0.38 y la Serie III produce R*_diseñador ∈ [0.32, 0.45], los resultados son consistentes: el punto de la Serie I cae dentro del rango de la Serie III. Si la Serie I produce R*_diseñador = 0.20 pero la Serie III produce R*_diseñador ∈ [0.35, 0.45], hay una inconsistencia que señala un problema en uno de los dos análisis: las diferencias en rangos de peso no deben producir diferencias de esa magnitud en el punto central de R*.

La verificación cruzada también opera entre Serie II y Serie III. Si la Serie II produce un IIC_diseñador = 0.05 (brecha casi total) y la Serie III produce R*_neta_diseñador bajo, hay una inconsistencia: IIC muy bajo implica aristas de alta intensidad desde el nodo de diseño, lo que debería producir R* alto en la Serie III. Si el R*_neta es bajo a pesar del IIC muy bajo, el grafo de la Serie III probablemente está subestimando las

Metrología Causal

aristas del nodo de diseño — exactamente la paradoja de la visibilidad.

Metrología Causal

