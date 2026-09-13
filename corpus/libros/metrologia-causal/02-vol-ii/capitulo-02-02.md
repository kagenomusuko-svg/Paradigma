PARTE II · El análisis simple: una sola serie

### Capítulo II·2

### Serie II: Compliance Causal

El protocolo de evaluación de congruencia del nodo de diseño

### I.  Cuándo aplica la Serie II

La Serie II responde la pregunta de Tipo 2: ¿el nodo de diseño operó en conformidad con lo que declaró que haría? Es la serie del compliance en su sentido más preciso — no el cumplimiento de una norma externa sino la congruencia entre el campo que el nodo de diseño declaró que produciría y el campo que efectivamente produjo.

El nodo de diseño es el actor que diseñó las condiciones estructurales bajo las cuales los demás nodos del grafo operaron: la institución que estableció el protocolo, la organización que diseñó el sistema de incentivos, el regulador que fijó las reglas, el arquitecto del sistema que determinó las restricciones de operación. La Serie II evalúa a ese nodo en términos de la brecha entre su diseño declarado y su operación real.

La Serie II nunca se aplica sin Serie I previa. El IIC requiere el vector R* del nodo de diseño como denominador de la fracción de responsabilidad que la congruencia modula. Sin R*, el IIC no tiene contexto causal: mide la brecha entre declaración y

Metrología Causal · Vol. II

operación, pero no dice cuánto pesa esa brecha en el resultado analizado.

### II.  Paso 1 · El grafo con horizonte prospectivo y el nodo de diseño

El grafo de la Serie II tiene la misma estructura del grafo de la Serie I con dos diferencias. La primera: el nodo de diseño N_D debe estar identificado explícitamente antes de comenzar el Paso 2. No todos los grafos tienen un único nodo de diseño claro — en algunos casos hay múltiples niveles de diseño. El mediador identifica el nodo de diseño más relevante para la pregunta de compliance que el destinatario plantea.

La segunda diferencia: el grafo puede incluir aristas prospectivas — relaciones de influencia que el nodo de diseño declaró que existirían pero que el análisis retroactivo de Serie I no incluyó porque no se verificaron en la evidencia disponible. Estas aristas prospectivas son el insumo del Paso 2: son los protocolos declarados que el IIC contrasta con lo observable.

Identificación del nodo de diseño — criterios

El nodo de diseño N_D es el nodo que cumple simultáneamente tres condiciones: (1) diseñó las condiciones estructurales bajo las que operaron otros nodos, (2) declaró explícitamente qué campo produciría su diseño (en documentos, normas, contratos, o comunicaciones verificables), y (3) tiene R* > 0 en el análisis de Serie I — es causalmente relevante para el resultado analizado.

Si hay múltiples candidatos a nodo de diseño, el análisis de Serie II se aplica al nodo con mayor R* entre ellos, salvo que el destinatario especifique otro nodo explícitamente.

Metrología Causal · Vol. II

### III.  Paso 2 · Cálculo del IIC

El Índice de Integridad Causal (IIC) mide la correlación promedio entre lo que el nodo de diseño declaró que produciría y lo que produjo. Opera sobre los protocolos declarados del nodo de diseño que son relevantes para el resultado analizado: no sobre todos los protocolos del nodo, sino sobre los que tienen relación directa con la cadena causal que produjo D.

Para cada protocolo declarado k relevante para D, el mediador calcula la correlación c_k entre la variable declarada (lo que el protocolo prometía producir) y la variable observable (lo que efectivamente produjo en el período analizado). La correlación puede calcularse sobre datos cuantitativos o estimarse cualitativamente usando la escala de la tabla siguiente.

IIC — Índice de Integridad Causal

IIC  =  (1/n)  Σ_k  c_k        con  c_k  =  corr(declarado_k, observable_k)

n = número de protocolos declarados relevantes para D. c_k □ [−1, 1]. IIC = 1 indica congruencia total entre todos los protocolos. IIC = 0 indica ausencia de correlación. IIC < 0 indica divergencia sistemática (el campo real es opuesto al declarado).

Descripción Cómo se estima cualitativamente

Valor de c_k

c_k = 1.00 Congruencia perfecta: el protocolo produjo exactamente lo que declaró.

El indicador de cumplimiento del protocolo muestra 100% o el evaluador no puede distinguir el campo real del declarado.

c_k □ [0.70, 1.00)

Alta congruencia: el campo real sigue la

Las principales variables del protocolo se comportaron como

Metrología Causal · Vol. II

Descripción Cómo se estima cualitativamente

Valor de c_k

dirección del declarado con desviaciones menores.

fueron diseñadas; hay excepciones documentadas menores.

c_k □ [0.40, 0.70)

Congruencia moderada: el campo real se parece al declarado pero con brechas significativas.

Algunos indicadores clave del protocolo funcionaron; otros no. Las desviaciones tienen efecto material.

c_k □ [0.00, 0.40)

Congruencia baja: el campo real diverge sustancialmente del declarado.

La mayoría de los indicadores del protocolo no produjeron lo prometido. El diseño existe en papel.

c_k < 0 Divergencia: el campo real va en dirección opuesta al declarado.

El protocolo prometía controlar algo que en la práctica amplificó. El diseño produjo el efecto inverso al declarado.

### Ejemplo numérico — IIC del nodo D (caso de referencia)

Protocolos declarados relevantes (n = 3): P1 — sistema de incentivos: c□ = 0.18 (los incentivos prometían alinear crecimiento con riesgo; en la práctica desalinearon). P2 — protocolo de aprobación: c□ = 0.35 (el protocolo prometía filtrar activos tóxicos; en la práctica los aprobó con excepciones). P3 — reporte de riesgo: c□ = 0.61 (el sistema de reporte funcionó moderadamente).

IIC_D = (0.18 + 0.35 + 0.61) / 3 = 1.14 / 3 = 0.38. El nodo de diseño opera con 38% de congruencia respecto a sus declaraciones. Baja congruencia — el campo real diverge sustancialmente del declarado.

Metrología Causal · Vol. II

### IV.  Paso 3 · Ajuste de pesos por IIC y recalculo de R*

El IIC del nodo de diseño ajusta los pesos de sus aristas estructurales salientes. La lógica del ajuste es directa: un nodo de diseño con baja congruencia influye sobre los demás nodos con menos efectividad de la que su posición estructural indicaría — su influencia real es mayor que la que el campo observable refleja porque parte de esa influencia opera a través de la brecha entre el diseño declarado y el real.

Ajuste de pesos por IIC

w_ij(ajustado) = w_ij(base) × (1 + k × (1 − IIC_D))

k es el coeficiente de amplificación de la brecha: k □ [0.5, 1.5] según la magnitud del resultado analizado. Valor estándar: k = 1.0. El ajuste amplifica las aristas del nodo de diseño reflejando que la brecha entre su campo declarado y real tiene efecto causal.

Con los pesos ajustados, se recalcula R* usando el mismo método de potencias del Paso 3 de la Serie I sobre la nueva matriz W(ajustado). El nuevo vector R*(ajustado) refleja la posición causal del nodo de diseño una vez que su baja congruencia es incorporada en la estructura del grafo.

Ejemplo numérico — Ajuste y recalculo (k = 1.0)

IIC_D = 0.38. Factor de ajuste: 1 + 1.0 × (1 − 0.38) = 1 + 0.62 = 1.62.

Aristas ajustadas de D: D→Nf pasa de 0.45 a 0.45 × 1.62 = 0.73 (luego renormalizado). D→E pasa de 0.50 a 0.81.

R*(ajustado): D = 0.5841, E = 0.2713, S = 0.1082. El ajuste por IIC aumenta R* del nodo de diseño en 10 puntos porcentuales, reflejando que su baja congruencia amplifica su peso causal real.

Metrología Causal · Vol. II

### V.  Paso 4 · El fraude annona y el umbral de acción

El fraude annona es el corolario III del Teorema de la Responsabilidad Causal Proporcional. Mide la posición más grave que el sistema puede registrar en un nodo de diseño: alta centralidad causal (R* alto), baja asunción (α bajo), y baja congruencia (IIC bajo). El nombre proviene del término romano annona — la gestión del suministro de grano — y la figura del funcionario que administra un bien esencial prometiendo calidad que no entrega.

Fraude annona

Fraude_annona_D  =  R*_D  ×  (1 − α_D)  ×  (1 − IIC_D)

El fraude annona alcanza su máximo cuando R*_D = 1, α_D = 0, e IIC_D = 0: el nodo es el único responsable, no ha asumido nada, y opera en dirección opuesta a lo que declaró. En la práctica, valores superiores a 0.20 indican una posición de responsabilidad institucional grave.

Ejemplo numérico — Fraude annona del caso de referencia

R*_D(ajustado) = 0.5841, α_D = 0.15, IIC_D = 0.38.

Fraude_annona_D = 0.5841 × (1 − 0.15) × (1 − 0.38) = 0.5841 × 0.85 × 0.62 = 0.3078.

Interpretación: el nodo de diseño genera una posición de fraude annona del 31% — dentro del rango de responsabilidad institucional grave. Este valor supera el umbral de 0.20 que, en la mayoría de los dominios regulatorios, activa requisitos formales de intervención.

### VI.  Paso 5 · El ajuste debitor

Metrología Causal · Vol. II

El ajuste debitor es la propuesta del sistema al destinatario sobre cómo reducir la brecha de compliance del nodo de diseño. No es una sanción ni una prescripción: es la lectura estructural de qué cambios en el nodo de diseño reducirían su Δ y su fraude annona. El mediador formula el ajuste debitor en tres componentes que corresponden a los tres orígenes de la brecha.

Qué corrige Cómo se formula

Componente del ajuste debitor

Estructural — protocolos

La brecha entre el campo declarado y el real (IIC bajo). Corrige los protocolos cuyo c_k es más bajo.

Para cada protocolo con c_k < 0.50: describir qué cambio de diseño elevaría c_k al rango [0.70, 1.00]. Expresar como condición estructural, no como instrucción de conducta.

Procesal — acción pendiente

El déficit de acción del nodo de diseño (α bajo). Corrige los criterios de la Ruta B que no se cumplieron.

Para cada criterio de α que el nodo de diseño no cumplió (conocimiento sin acción, oportunidades no actuadas): describir la acción concreta con plazo verificable que cubriría ese criterio.

Reparatorio — daño en curso

La fracción AD_D del daño que el nodo de diseño generó y que no ha sido abordada. Corrige el Δ del nodo de diseño hacia atrás.

Si D_total está cuantificado: AD_D = R*_D(ajustado) × D_total. El ajuste reparatorio es esa fracción no cubierta por acciones verificables de α ya registradas.

Metrología Causal · Vol. II

### VII.  Paso 6 · El expediente de Serie II

### El expediente de Serie II entrega cuatro documentos. Los dos primeros son actualizaciones de los documentos de Serie I; los dos siguientes son específicos de Serie II.

Documento Contenido Diferencia respecto a Serie I

1 · Hoja de calibración (actualizada)

La hoja de Serie I con la adición de: identificación del nodo de diseño, protocolos declarados relevantes con sus c_k, coeficiente k del ajuste.

Añade la sección de compliance al documento base de Serie I.

2 · Vector R* ajustado

El vector R* recalculado con los pesos ajustados por IIC. Tabla comparativa R*(base) vs R*(ajustado) para cada nodo.

El vector R* de Serie I es el punto de referencia; el de Serie II es el resultado del ajuste por congruencia.

3 · Mapa de brecha IIC

Para cada protocolo declarado relevante: c_k documentado, descripción de la brecha, evidencia que la sustenta. El IIC global del nodo de diseño con su cálculo explícito.

Documento nuevo. Específico de Serie II.

4 · Ajuste debitor con cronograma

Los tres componentes del ajuste debitor (estructural, procesal, reparatorio) con plazos verificables para cada acción propuesta.

Documento nuevo. Específico de Serie II.

### Producto de salida · Capítulo II·2

Metrología Causal · Vol. II

Expediente de Serie II completo: hoja de calibración actualizada + vector R* ajustado + mapa de brecha IIC + ajuste debitor con cronograma. El IIC del nodo de diseño y el fraude annona son los dos indicadores centrales que el destinatario recibe como resultado del análisis de compliance.

Notas al Capítulo II·2

1  El coeficiente k del ajuste de pesos por IIC tiene rango [0.5, 1.5]. El valor estándar k = 1.0 aplica cuando la magnitud del resultado es consistente con el dominio típico del sistema. En casos donde el resultado es extraordinariamente grave para el dominio (colapsos sistémicos, daños masivos, crisis institucionales) puede justificarse k > 1.0. En casos donde el resultado es menor o el contexto es de alta incertidumbre regulatoria genuina, puede justificarse k < 1.0. La elección de k debe documentarse en la hoja de calibración con su justificación explícita.

2  El fraude annona tiene el nombre que tiene porque el sistema lo diseñó para capturar una posición específica: la de quien administra un bien esencial (un sistema de crédito, un protocolo de salud, un programa social) declarando estándares que luego no cumple, con alta centralidad causal en el resultado dañoso que esa brecha produce. No es una calificación moral: es una medición estructural de la combinación de R* alto, α bajo, e IIC bajo. El nombre orienta la interpretación, pero la medición es formal.

3  El ajuste debitor en su componente reparatorio no es equivalente a una determinación de reparación legal o contractual. Es la lectura estructural de la fracción del daño que corresponde al nodo de diseño según el análisis causal. Cualquier determinación de reparación formal requiere instancias adicionales (jurídicas, regulatorias, arbitrales) que el análisis causal informa, pero no reemplaza.

Metrología Causal · Vol. II

