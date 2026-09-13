PARTE II · El análisis simple: una sola serie

### Capítulo II·1

### Serie I: Contabilidad Ontológica

El protocolo completo del análisis causal base

### I.  Cuándo aplica la Serie I

La Serie I es el análisis causal base del sistema. Responde la pregunta de Tipo 1 —¿quién fue condición necesaria de este resultado y en qué proporción? — y es el punto de partida obligatorio de toda combinación de series. Ningún análisis del sistema, con independencia del tipo de pregunta que responda, omite la Serie I: sus siete pasos producen el vector R* que todas las series subsiguientes usan como insumo.

La Serie I aplica en solitario cuando el destinatario necesita únicamente el diagnóstico causal: la distribución de responsabilidad entre los nodos del grafo, con sus componentes de sustituibilidad y asunción, y con las hipótesis de prevención que esa distribución produce. Cuando el destinatario necesita también compliance o imputación adversarial, la Serie I se ejecuta primero y sus resultados alimentan la Serie II o la III.

### II.  Paso 1 · Construcción del grafo G = (N, E, W)

Metrología Causal · Vol. II

El grafo es el objeto matemático sobre el que opera todo el cálculo de la Serie I. Su construcción no es un paso previo al análisis: es la primera operación analítica, y determina la validez de todo lo que sigue. Un grafo bien construido produce R* que mide responsabilidad causal real. Un grafo mal construido produce R* que mide algo diferente con exacta precisión formal.

El grafo G = (N, E, W) tiene tres componentes. El conjunto de nodos N contiene todos los actores con capacidad causal sobre el resultado D, incluyendo el nodo sumidero Nf que representa D. El conjunto de aristas E contiene las relaciones de influencia causal entre nodos, con su dirección. La matriz de pesos W asigna a cada arista un peso w_ij que refleja la intensidad de la influencia del nodo i sobre el nodo j.

El peso de cada arista no se asigna como un valor puntual: se asigna como un rango [a_ij, b_ij] calibrado según el nivel de evidencia disponible para esa relación. El valor de cálculo del Paso 3 es el midpoint m_ij = (a_ij + b_ij) / 2. La amplitud del rango alimenta el análisis de sensibilidad de la Serie III si el caso lo requiere.

Descripción de la evidencia Amplitud del rango [a_ij, b_ij]

Nivel E

E8 Evidencia experimental controlada o réplica verificada

±0.02 sobre el midpoint estimado

E7 Estudio observacional prospectivo con grupo de control

±0.05

E6 Múltiples estudios convergentes o consenso de expertos

±0.07

E5 Evidencia documental directa y consistente

±0.10

Metrología Causal · Vol. II

Descripción de la evidencia Amplitud del rango [a_ij, b_ij]

Nivel E

E4 Evidencia documental directa con inconsistencias menores

±0.12

E3 Evidencia indirecta sólida o inferencia estructural fuerte

±0.15

E2 Evidencia indirecta débil o inferencia estructural moderada

±0.18

E1 Evidencia mínima o testimonial no corroborada

±0.22

E0 Sin evidencia: nodo estructuralmente necesario pero no documentado

±0.25 sobre midpoint 0.30

### Ejemplo numérico — Caso de referencia (4 nodos)

### Nf = resultado D (nodo sumidero). N = {D (diseño), E (ejecutor), S (supervisor), Nf}.

### Aristas: D → Nf [0.35, 0.55], E → Nf [0.20, 0.40], S → Nf [0.10, 0.24], D → E [0.40, 0.60], S → E [0.25, 0.45].

Niveles de evidencia: D→Nf E5, E→Nf E4, S→Nf E3, D→E E5, S→E E4. Midpoints: D→Nf 0.45, E→Nf 0.30, S→Nf 0.17, D→E 0.50, S→E 0.35.

### III.  Paso 2 · Verificación de condiciones de validez

Antes del cálculo, el grafo debe cumplir dos condiciones que el Teorema de Perron-Frobenius requiere para garantizar la existencia y unicidad del eigenvector principal positivo: irreducibilidad y aperiodicidad.

Metrología Causal · Vol. II

El grafo es irreducible si desde cada nodo existe al menos un camino dirigido al nodo sumidero Nf. Un nodo sin camino al sumidero no tiene relación causal con D y debe eliminarse del grafo antes del cálculo. La irreducibilidad se verifica inspeccionando el grafo: si hay nodos "flotantes" sin camino a Nf, no son causalmente relevantes para el resultado analizado.

El grafo es aperiódico si no contiene ciclos de longitud fija que atrapen el método de potencias en una oscilación permanente. En la práctica, la aperiodicidad se garantiza añadiendo un autolazo de peso ε = 0.01 al nodo sumidero Nf: w_Nf,Nf = ε. Este ajuste es suficiente para romper cualquier periodicidad sin afectar la distribución R* de manera significativa.

Corrección de aperiodicidad

w_Nf,Nf = ε = 0.01  →  renormalizar cada columna de W para que Σ_j w_ij = 1

Solo se aplica si el grafo falla el test de aperiodicidad. En la mayoría de los casos prácticos el grafo ya es aperiódico.

### IV.  Paso 3 · Cálculo de R* por el método de potencias

Con la matriz W de midpoints construida y las condiciones de validez verificadas, el método de potencias calcula el eigenvector principal normalizado. El método es iterativo: parte de un vector inicial uniforme y lo multiplica repetidamente por W hasta que la diferencia entre iteraciones sucesivas cae por debajo del umbral de convergencia.

Método de potencias — iteración

R*(k+1) = W · R*(k)  /  ||W · R*(k)||□

Metrología Causal · Vol. II

Condición inicial: R*(0) = [1/n, 1/n, ..., 1/n]. Criterio de convergencia: ||R*(k+1) ₁ ⁶ ⁻ − R*(k)|| < 10 . En sistemas de 3–8 nodos típicos, la convergencia ocurre entre 15 y 40 iteraciones.

La condición de convergencia 10 ⁶ ⁻ garantiza que el vector R* es estable hasta la sexta cifra decimal. Para los propósitos del expediente, se reportan cuatro cifras decimales. La verificación final es simple: Σ_i R*_i = 1.000 (±0.001 por redondeo).

Nodo R* (resultado del caso de referencia)

Interpretación

0.4812 El nodo de diseño explica el 48% del resultado. Su influencia directa sobre Nf y su influencia estructural sobre E lo posicionan como el nodo de mayor centralidad causal.

D — Diseño

### 0.3104 El ejecutor explica el 31% del resultado. Su posición es significativa pero dependiente del diseño que lo orienta.

E — Ejecutor

### 0.1521 El supervisor explica el 15% del resultado. Su influencia se ejerce principalmente a través de E.

S — Supervisor

### 0.0563 El nodo sumidero retiene el residuo del autolazo ε. Este valor no tiene interpretación de responsabilidad.

Nf — Resultado

### V.  Paso 4 · Determinación de S y cálculo de R*_neta

Metrología Causal · Vol. II

Con el vector R* calculado, el Paso 4 determina S para cada nodo y calcula R*_neta: la fracción idiosincrática del peso causal de cada nodo, excluyendo la parte que cualquier otro en esa posición también habría producido.

S se deriva del Hijo dominante de cada nodo usando la tabla de conversión del Capítulo I·4. Para nodos institucionales o algoritmos sin ECO disponible, S se determina desde los tres criterios universales de la Introducción de este volumen: existencia de alternativa documentada, conformidad con la norma del dominio, y replicabilidad ante un par equivalente.

R*_neta

R*_neta_i = R*_i × (1 − S_i)

La fracción (1−S_i) es la proporción del acto que es idiosincrática del nodo i. Σ R*_neta_i ≤ 1. La diferencia 1 − Σ R*_neta_i es la responsabilidad sistémica total del campo.

Nodo R* S 1 − S

R*_neta Fuente de S

D — Diseño 0.4812 0.20 0.80 0.3850 Harmonía dominante — EP4. Decisión de diseño altamente idiosincrática.

E — Ejecutor 0.3104 0.72 0.28 0.0869 Fobos dominante — EP4. Alta presión del sistema de incentivos

Metrología Causal · Vol. II

Nodo R* S 1 − S

R*_neta Fuente de S

diseñado por D.

S — Supervisor 0.1521 0.55 0.45 0.0684 Anteros dominante — EP3. Supervisión condicionada a la respuesta del ejecutivo.

— — — 0.4597 Campo c: fracción del resultado que cualquier actor en estas posiciones habría producido.

Responsabilidad sistémica

### VI.  Paso 5 · Determinación de α y cálculo de Δ

El Paso 5 determina α para cada nodo usando la ruta disponible (A, B, o C según el tipo de caso) y calcula Δ: el déficit de asunción, la fracción de R* que el nodo causó, pero no integró como propia mediante acciones verificables.

Δ — Déficit de asunción

Δ_i  =  R*_i  ×  (1 − α_i)       Δ_total  =  Σ_i  Δ_i

Δ_i > 0 indica que el nodo causó más de lo que asumió. Δ_i < 0 indica inversión causal: el nodo asumió más de lo que causó. Δ_i = 0 indica equilibrio de asunción.

Metrología Causal · Vol. II

Nodo R* α 1 − α

Δ_i Fuente de α

### 0.4812 0.15 0.85 0.4090 Ruta B — Criterio de conocimiento: sí. Acción: mínima. Oportunidad: sí. α = 0.15.

D — Diseño

### 0.3104 0.40 0.60 0.1862 Ruta A — φ□ activo con facilitación. Reconoce el acto con apoyo del ECO.

E — Ejecutor

### 0.1521 0.62 0.38 0.0578 Ruta B — Acción de supervisión parcialmente documentada. Tres oportunidades de intervención identificadas, una actuada.

S — Supervisor

Δ_total — — — 0.6530 63% del resultado total no fue integrado como propio por ningún nodo. Brecha sistémica de asunción.

### VII.  Paso 6 · Cuantificación del daño D y las fracciones AD_i

El análisis causal distribuye responsabilidad en términos relativos (R*). Cuando el caso requiere también una distribución en términos absolutos —cuánto del daño total corresponde a cada nodo— el Paso 6 cuantifica D_total y calcula la fracción atribuible AD_i a cada nodo.

Metrología Causal · Vol. II

D_total tiene tres componentes que el mediador cuantifica desde el expediente del caso. T_inv es el daño de inversión: costos directos incurridos como consecuencia del resultado analizado. T_imp es el daño de impacto: consecuencias directas del resultado sobre los afectados, cuantificadas en las mismas unidades que T_inv. ΔT_tray es el daño de trayectoria: la diferencia entre el valor de la trayectoria esperada sin el resultado y el valor de la trayectoria real, proyectada al horizonte relevante para el caso.

D_total y fracción atribuible AD_i

D_total = T_inv + T_imp + ΔT_tray       AD_i = R*_i × D_total

AD_i es la contribución causal del nodo i al daño total en unidades absolutas. La suma Σ AD_i = D_total. Las fracciones AD_i son el insumo directo para cualquier determinación de compensación o reparación proporcional.

La cuantificación de D_total es responsabilidad del destinatario del análisis, no del mediador. El mediador recibe los valores de T_inv, T_imp, y ΔT_tray del expediente del caso y aplica la fórmula. Si el destinatario no tiene estimados de los tres componentes, el mediador entrega únicamente R* y documenta que AD_i está condicionado a la cuantificación de D_total por el destinatario.

### VIII.  Paso 7 · El expediente de Serie I

El expediente de Serie I contiene tres documentos. El mediador los produce en el orden que sigue: primero la hoja de calibración (ya completada en el Paso 1), después el vector R* con su análisis descriptivo, y finalmente las hipótesis de prevención.

Metrología Causal · Vol. II

Documento Contenido Criterio de completitud

1 · Hoja de calibración

Todos los nodos, todas las aristas con sus rangos [a_ij, b_ij] y niveles E0–E8, valores de S y α con sus fuentes, método de cálculo seleccionado.

Todos los ítems de la lista de verificación del Cap. I·7 completados y firmados.

2 · Vector R* con análisis descriptivo

Tabla de distribución con R*, S, R*_neta, α, Δ para cada nodo. Párrafo narrativo que describe la distribución causal en lenguaje del dominio del destinatario. Δ_total y su interpretación sistémica.

Σ R*_i = 1.000 (±0.001). El análisis narrativo no introduce juicios que el vector no sostiene.

3 · Hipótesis de prevención

Para cada nodo con R* > 0.15: una hipótesis de rediseño que reduciría su R* en sistemas futuros similares. Las hipótesis se formulan como condiciones estructurales, no como recomendaciones de conducta.

Cada hipótesis especifica qué cambio en el grafo produciría qué reducción estimada en R*. No se formulan hipótesis sin ancla estructural.

### Producto de salida · Capítulo II·1

Expediente de Serie I completo: hoja de calibración + vector R* con análisis descriptivo + hipótesis de prevención. El vector R* es el producto central que toda serie subsiguiente presupone. Sin el expediente de Serie I completo y verificado, ninguna otra serie puede iniciarse.

Notas al Capítulo II·1

Metrología Causal · Vol. II

1  El nodo sumidero Nf no tiene R* interpretable como responsabilidad causal: es el nodo que representa el resultado D, no un actor que lo produjo. El valor residual que retiene por el autolazo ε no debe incluirse en el análisis narrativo ni en las hipótesis de prevención. Cuando se reporta el vector R*, Nf se excluye de la tabla o se incluye con la nota explícita de que su valor es el residuo del ajuste de aperiodicidad.

2  La separación entre R* (responsabilidad causal estructural) y Δ (déficit de asunción) es una de las distinciones más importantes del sistema para la práctica. Un nodo con R* alto y Δ bajo ha asumido correctamente su posición causal: el daño es grande pero la responsabilidad fue integrada. Un nodo con R* bajo y Δ alto ha causado poco pero no ha asumido ni eso: la proporción es pequeña pero la evasión es total. Las dos situaciones tienen consecuencias completamente distintas para la prevención y para cualquier determinación de reparación.

3  La cuantificación de ΔT_tray requiere especificar el horizonte temporal de la proyección. Un horizonte demasiado corto subestima el daño de trayectoria; uno demasiado largo lo sobreestima con incertidumbre creciente. La práctica estándar es usar el horizonte que el destinatario del análisis considera relevante para su decisión, documentado en el expediente.

Metrología Causal · Vol. II

