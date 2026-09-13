PARTE I · El flujo de trabajo del mediador

### Capítulo I·2

### El mapa completo del proceso

De ECO al expediente: seis estaciones, un producto en cada una

### I.  El proceso como cadena de productos

El análisis causal no es un evento sino una cadena. Cada estación del proceso recibe el producto de la estación anterior y entrega un producto nuevo. El mediador que sabe exactamente qué produce en cada estación sabe cuándo terminó cada paso — y sabe, también, qué pasa si una estación falla: qué producto queda sin insumo y qué parte del expediente resulta comprometida.

El mapa que este capítulo establece tiene seis estaciones. No todas se activan en todos los casos: la Estación ECO solo aplica cuando hay un ego humano a localizar; la Estación HISTOS solo aplica cuando el caso tiene componente de acompañamiento. Pero el orden entre las estaciones que se activan es invariante: ninguna puede producir su producto sin el insumo de la anterior.

### II.  Estación 1 · ECO — Localización del ego

Metrología Causal · Vol. II

La Entrevista Clínica Ontológica es el primer instrumento que opera cuando el caso tiene un ego humano como nodo relevante. Su función no es clínica en el sentido de diagnóstico de salud mental: es metrológica. ECO produce la localización del ego en el campo de posibilidades — qué Hijo domina su voluntad, con qué nivel de evidencia, con qué consistencia entre la autopercepción del sujeto y la conducta observable.

El producto de la Estación ECO es la DI-ECO: la Declaración de Identidad de la Entrevista Clínica Ontológica. La DI-ECO contiene el vector P(Hijos) con sus niveles EP, el código de eje del SDO, y la descripción del contexto que alimentará el Bloque II del grafo. Todo lo que la DI-ECO no captura —el grafo del campo, los nodos institucionales, los nodos normativos— es insumo de las estaciones siguientes.

Estación ECO → Producto

Entrada: el ego a localizar (sujeto de la entrevista o caso documental).

Operación: administración de los seis módulos del Bloque I + preguntas contextuales del Bloque II.

Producto: DI-ECO completa → P(Hijos) con niveles EP + código de eje SDO + descripción de contexto.

Condición de completitud: todos los módulos administrados sin condiciones de invalidación [ECO · Cap. II·V]. Si hay invalidación parcial, documentar y aplicar protocolo de datos incompletos [Vol.I · Cap. IV·4].

### III.  Estación 2 · SDO — Posición estructural del ego

El Sistema de Diagnóstico Ontológico recibe la DI-ECO y produce la lectura de los cinco ejes del ego. La diferencia entre ECO y SDO no es de escala sino de perspectiva: ECO observa

Metrología Causal · Vol. II

desde el diálogo; SDO lee desde la estructura. El mismo ego puede producir una DI-ECO con señales mixtas que el SDO resuelve al leer la configuración de los cinco ejes en conjunto.

El producto del SDO es el código de eje: una secuencia de cinco dígitos que describe la posición estructural del ego con suficiente precisión para que el Capítulo I·4 asigne el rango de S correcto. El código de eje es también el punto de entrada de HISTOS si el caso tiene componente de acompañamiento — el Protocolo Histos parte del código SDO como diagnóstico de situación inicial.

### IV.  Estación 3 · Grafo G = (N, E, W)

La construcción del grafo es la estación central del proceso. Recibe como insumo la DI-ECO (para los nodos humanos), el SDO (para la posición de S de esos nodos), y el expediente documental del caso (para todos los nodos, incluyendo los institucionales, normativos, y algorítmicos que ECO y SDO no cubren).

El grafo tiene tres componentes que el mediador construye en secuencia. Primero: el conjunto de nodos N — todos los actores con capacidad causal sobre el resultado D, incluyendo los que no aparecen en la evidencia disponible pero cuya posición estructural los hace necesarios. Segundo: el conjunto de aristas E con su dirección — quién influye sobre quién. Tercero: la matriz de pesos W — la intensidad de cada influencia expresada como rango [a_ij, b_ij] calibrado según el nivel de evidencia E0–E8.

El producto de la Estación Grafo es la hoja de calibración completa: una tabla con todos los nodos, todas las aristas, todos los rangos de peso, todos los niveles de evidencia, y los valores de S y α asignados a cada nodo. La hoja de calibración es el insumo completo de la Estación Cálculo.

Metrología Causal · Vol. II

Estación Grafo → Producto

Entrada: DI-ECO + código SDO + expediente documental.

Operación: identificación de nodos → construcción de aristas → asignación de rangos [a_ij, b_ij] según E0–E8 → asignación de S y α.

Producto: Hoja de Calibración completa [plantilla Vol.II · Sec. 4.1].

Condición de completitud: todos los nodos con capacidad causal identificados — incluyendo los no documentados cuya posición estructural los hace necesarios. Un grafo incompleto produce R* incorrecto con independencia de la precisión del cálculo.

### V.  Estación 4 · Cálculo

La Estación Cálculo recibe la hoja de calibración y produce los parámetros del expediente. No requiere decisión sobre qué calcular: esa decisión fue tomada en el Capítulo I·1 (qué serie), en el I·4 (S), en el I·5 (α), y en el I·6 (eigenvector o Shapley). El cálculo ejecuta.

Para la Serie I: el método de potencias sobre la matriz W de midpoints produce el vector R*. Con R* y S se calcula R*_neta. Con R* y α se calcula Δ. Para la Serie II: el IIC del nodo de diseño ajusta los pesos de sus aristas; el cálculo se repite sobre W ajustada. Para la Serie III: el hipercubo de parámetros se construye sobre los rangos [a_ij, b_ij] y el ranking σ(w) se calcula en cada punto del hipercubo. El nivel de la Declaración (A, B, C, D) emerge del análisis de estabilidad del ranking.

### VI.  Estaciones 5 y 6 · Expediente y HISTOS

Metrología Causal · Vol. II

El expediente recibe los parámetros del cálculo y los organiza en los cuatro documentos que el análisis entrega: la hoja de calibración (ya producida en la Estación 3), el vector R* (con sus derivados R*_neta, Δ, e IIC según la serie), el reporte de sensibilidad (solo para Serie III), y la Declaración. Las plantillas de estos documentos están en la Sección 4 de este volumen.

HISTOS recibe el expediente completo y produce el plan de acompañamiento cuando el caso lo requiere. El Protocolo Histos parte del Δ como medida de la brecha que el acompañamiento debe trabajar y del código SDO como diagnóstico de situación. HISTOS es la estación de cierre del proceso en los casos con componente de acompañamiento clínico u ontológico.

Producto de salida · Capítulo I·2

Mapa de ruta del caso: qué estaciones se activan, en qué orden, qué produce cada una, y cuáles son las condiciones de completitud que habilitan el paso a la siguiente. El mapa de ruta queda registrado en el encabezado del expediente junto a la decisión de serie del Capítulo I·1.

Notas al Capítulo I·2

Metrología Causal · Vol. II

tiene evidencia de él debe incluirlo con nivel de evidencia E0 y documentar la ausencia.

3  HISTOS no es una estación obligatoria. Es el protocolo de cierre cuando el análisis tiene consecuencias de acompañamiento para el ego localizado. En contextos puramente forenses o de auditoría, el proceso termina con la entrega del expediente.

Metrología Causal · Vol. II

