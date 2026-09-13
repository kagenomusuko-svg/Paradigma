PARTE V · Validez y límites de la medición causal

### Capítulo V·10

### Incertidumbre epistémica vs.

### incertidumbre estructural

La distinción más importante para el diseño del análisis de

sensibilidad

### I.  Las dos fuentes de incertidumbre en los pesos del grafo

Cuando el analista establece el rango [a_ij, b_ij] para el peso de una arista, la amplitud del rango puede tener dos fuentes distintas. La fuente epistémica: el analista no tiene suficiente información para determinar w_ij con mayor precisión. Si hubiera más documentos, más testimonios, más registros del sistema, el rango podría estrecharse. La amplitud es una función del estado del conocimiento disponible, no de la naturaleza del fenómeno.

La fuente estructural: la influencia causal de i sobre j es genuinamente probabilística dentro de un rango. No hay más información que recopilar que cambiaría la amplitud del rango porque la amplitud refleja la variabilidad real del fenómeno, no la limitación del analista. La presión de un sistema de incentivos sobre los actores que operan dentro de él varía con las circunstancias específicas de cada actor, con el momento

Metrología Causal

temporal, con factores contextuales que no están en el grafo y que no es posible incluir sin complejizar el modelo más allá de lo útil. Esa variabilidad es estructural: no es reducible con más información.

### II.  Por qué la distinción importa para el análisis de sensibilidad

La distinción entre las dos fuentes de incertidumbre determina la respuesta correcta ante un rango amplio. Ante incertidumbre epistémica: buscar más evidencia para estrechar el rango. Si el rango [0.30, 0.70] es ancho porque solo hay un documento que informa sobre la arista, buscar documentos adicionales puede estrecharlo a [0.40, 0.60] o [0.45, 0.55]. El análisis de sensibilidad con el rango estrecho producirá una Declaración más sólida.

Ante incertidumbre estructural: aceptar el rango como la descripción correcta del fenómeno y verificar que la Declaración es robusta a través del rango completo. No tiene sentido buscar más evidencia para estrechar el rango porque la amplitud no refleja falta de información; refleja la variabilidad real. La Declaración correcta es la que declara su robustez a través del rango estructural completo.

Tratar la incertidumbre estructural como si fuera epistémica produce el error más sofisticado del sistema: el analista busca más evidencia, estrecha artificialmente el rango, produce una Declaración A sobre un análisis que en realidad tiene incertidumbre estructural en el rango [0.30, 0.70]. La Declaración parece sólida; en realidad, oculta variabilidad real del sistema que haría la Declaración más modesta si estuviera correctamente declarada.

Metrología Causal

### III.  El protocolo de identificación de la fuente de incertidumbre

El protocolo para identificar la fuente de incertidumbre de un rango tiene tres preguntas. Primera: ¿qué información adicional concebible podría estrechar el rango? Si la respuesta es «ninguna — la variabilidad es inherente al fenómeno», la incertidumbre es estructural. Si la respuesta es «más documentos, más testimonios, acceso a registros internos», la incertidumbre es epistémica.

Segunda: ¿el rango varía sistemáticamente con los tipos de evidencia disponible? Si el rango se estrecha cuando hay más tipos de evidencia, pero no cuando hay más cantidad del mismo tipo de evidencia, la incertidumbre tiene un componente epistémico sobre el tipo de evidencia y un componente estructural sobre la variabilidad intrínseca del fenómeno. El rango tiene dos fuentes que deben declararse separadamente.

Tercera: ¿el análisis de sensibilidad muestra puntos de quiebre del ranking en el interior del rango o solo en sus extremos? Si los puntos de quiebre están en el interior, la incertidumbre sobre la ubicación de w_ij dentro del rango es epistemológicamente relevante: el ranking cambia con la evidencia disponible, lo que indica que conseguir más evidencia puede cambiar la Declaración. Si los puntos de quiebre están solo en los extremos, la incertidumbre central del rango no afecta al ranking: la Declaración es robusta en el rango central, aunque frágil en los extremos.

Metrología Causal

