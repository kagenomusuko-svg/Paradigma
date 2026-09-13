PARTE V · La integración: los tres instrumentos como sistema

### Capítulo 5.3

### El sistema integrado: mapa de uso para el mediador

Capítulo de cierre del Volumen I

### I.  El mapa como derivación, no como manual

Este capítulo cierra el libro. Pero su posición al final no lo convierte en un capítulo de recapitulación — es el capítulo donde las consecuencias prácticas de toda la demostración anterior se concretan en un mapa de uso operativo.

La palabra 'mapa' es deliberada. Un manual prescribe procedimientos que deben seguirse. Un mapa muestra el terreno y establece las rutas posibles según la posición de quien lo usa y el destino que quiere alcanzar. El mediador que tiene los tres instrumentos no necesita un procedimiento fijo — necesita saber qué instrumento es pertinente en cada configuración del caso y por qué.

El mapa de este capítulo es una derivación — emerge de todo lo que el libro demostró — y no una convención arbitraria. La secuencia SDO → Prometeo → ECO no es la secuencia que alguien decidió que era la más eficiente. Es la secuencia que la estructura del sistema implica: el SDO provee los insumos ontológicos que Prometeo necesita para producir rangos de S y α fundamentados (en lugar de estimados), y

La transformación formal

Prometeo produce la descripción de Δ que el ECO necesita para orientar su trabajo.

Los casos límite que el capítulo desarrolla — cuándo puede omitirse el SDO previo, cuándo el SDO no es suficiente para que Prometeo produzca resultados robustos, cuándo ninguno de los tres puede resolver lo que el caso requiere — también son derivaciones del sistema y no excepciones ad hoc. Emergen de los principios que los capítulos anteriores establecieron.

### II.  La regla general: SDO → Prometeo → ECO

La secuencia general del sistema integrado tiene tres pasos que no son opcionales sino secuenciales. Cada paso requiere el anterior para producir resultados de calidad.

Paso 1: El SDO localiza

Antes de que Prometeo pueda calcular con parámetros ontológicamente fundamentados, el SDO debe haber producido la observación de v_t y c de los actores relevantes del caso. Esa observación produce:

Para cada actor del grafo: la distribución P(Hijos) en φ₁ (estado de v_t en el momento del acto analizado, que determina S), la distribución P(Hijos) en φ₂ (estado de v_t actual ante la posibilidad de integrar, que determina α), y la observación del estado de I(t) histórico (estado de c que condiciona φ₁ y permite α_patrón). Para la institución: la localización de IIC (correlación entre valores declarados y comportamiento observable) y el diagnóstico del Origen A o B institucional. Cuando el SDO no puede observar directamente (actor no disponible), la observación es retrospectiva desde las señales históricas disponibles (capítulo 5.1, sección VII). La anchura de los intervalos de S y α que resultan refleja la incertidumbre de esa observación retrospectiva.

Paso 2: Prometeo calcula

Con las distribuciones P(Hijos) del SDO disponibles, Prometeo calcula: La transformación formal

El grafo causal con los pesos w empíricos y el ajuste por IIC cuando corresponde. R* mediante el eigenvector dominante. S para cada nodo mediante la propagación del capítulo 4.2. R*_neta = R* × (1 − S). α desde la distribución P(Hijos) en φ₂. Δ = R* − α con sus rangos combinados. El análisis de sensibilidad extendido que cubre los dos tipos de incertidumbre simultáneamente. Las Declaraciones A-D extendidas con especificación del tipo de incertidumbre que limita la robustez cuando no es Declaración A.

Paso 3: El ECO interviene donde Δ lo indica

Con Δ calculado y el diagnóstico SDO del tipo de Δ (Origen A o B) disponible, el ECO puede orientar su trabajo:

Si Δ es bajo (Δ ≤ 0.15): el equilibrio de asunción es razonablemente alcanzado. El ECO puede verificar que el equilibrio es genuino (integración real vs. adaptación conductual del capítulo 5.2) y trabajar con la sostenibilidad si el equilibrio es frágil. Si el equilibrio es robusto, el trabajo del ECO puede no ser necesario. Si Δ es moderado (0.15 < Δ ≤ 0.45): hay brecha real pero no abrumadora. El ECO trabaja con el bloqueo de v_t (Origen A) o con los primeros pasos de restauración de φ₂ (Origen B). El trabajo es de alcance limitado y con objetivos claros. Si Δ es alto (Δ > 0.45): la brecha es significativa. El ECO trabaja con el diagnóstico completo del tipo de Δ y diseña un proceso de acompañamiento más extenso. Si el diagnóstico es Origen B, la primera fase del trabajo (restauración de φ₂) puede requerir tiempo antes de que el contenido específico de Δ sea abordable.

### III.  Primer caso límite: cuando Prometeo puede calcularse sin SDO previo

Hay casos donde la secuencia completa SDO → Prometeo → ECO no es necesaria porque parte de los insumos ontológicos del SDO pueden inferirse razonablemente desde la evidencia del mundo sin necesidad de observación directa del ego. Estos casos permiten comenzar el análisis con Prometeo y producir resultados útiles, aunque incompletos, que el SDO posterior puede refinar.

La transformación formal

El criterio para determinar si Prometeo puede calcularse sin SDO previo es si la incertidumbre ontológica sobre v_t es suficientemente baja para que S y α produzcan rangos compatibles con una Declaración robusta. Eso puede ocurrir en tres configuraciones:

Configuración 1 — Señales históricas convergentes que permiten inferir P(Hijos)

Cuando la documentación histórica del caso contiene suficientes señales observacionales de los Hijos dominantes — correos que revelan el estado de v_t del actor, testimonios de contemporáneos que describen el comportamiento del actor en el contexto del acto, patrones de comportamiento histórico que son consistentes con un Hijo específico —, el analista puede construir una distribución P(Hijos) razonablemente concentrada sin entrevista SDO directa.

El criterio operativo: si la distribución P(Hijos) inferida desde la evidencia histórica tiene un Hijo con probabilidad > 0.70 y la incertidumbre residual produce rangos de S que son suficientemente estrechos para no invertir la conclusión sobre R*_neta en el análisis de sensibilidad, el análisis puede proceder. Esta configuración es la más frecuente en análisis históricos y en análisis donde el actor no está disponible para observación directa.

Configuración 2 — La pregunta del análisis no requiere R*_neta sino R*

Cuando el objetivo del análisis es la distribución de la responsabilidad causal total (no la idiosincrática), el SDO previo puede omitirse porque R* no depende de S ni de α. La identificación de quién fue la condición necesaria de mayor fracción del resultado no requiere saber qué Hijo dominaba v_t — solo requiere la construcción del grafo causal con los pesos w empíricos.

Esta configuración aplica cuando el propósito del análisis es la distribución de daños para reparación material (el costo del resultado se distribuye según R* total, no según R*_neta), o cuando el caso es de carácter sistémico donde la pregunta es qué nodo del grafo tuvo mayor influencia total independientemente de si fue idiosincrática o estructural.

La transformación formal

Configuración 3 — Todos los Hijos plausibles producen la misma conclusión

Cuando la incertidumbre sobre el Hijo dominante abarca solo Hijos que producen orientaciones de S similares (por ejemplo, Fobos y Deimos — ambos con S ∈ [0.70, 0.95]), la incertidumbre sobre v_t no produce incertidumbre significativa sobre S. El análisis puede proceder con un rango de S estrecho, aunque la distribución P(Hijos) sea difusa.

En todos los casos donde Prometeo procede sin SDO previo, los resultados tienen la misma estructura: Declaraciones A y B son posibles si la incertidumbre inferida es suficientemente baja; Declaración C-O es posible cuando la inferencia produce rangos amplios pero el análisis puede identificar qué observación SDO resolvería la ambigüedad. Declaración D por incertidumbre ontológica pura — sin SDO — es el peor caso, y en ese caso el resultado no es útil sin observación SDO.

### IV.  Segundo caso límite: cuando el SDO no es suficiente para producir robustez

El caso contrario del anterior: hay casos donde la observación SDO es de calidad suficiente pero la incertidumbre empírica sobre w es tan alta que los rangos de R* son demasiado amplios para que la corrección por S produzca una conclusión robusta sobre R*_neta.

Este caso ocurre cuando la evidencia documental es muy escasa o de baja calidad — el grafo tiene pocas aristas con evidencia directa, los testimonios son altamente contradictorios, o los registros relevantes fueron destruidos o nunca existieron. En ese caso, incluso con S bien determinado por el SDO, los rangos de R*_neta de los nodos pueden solaparse significativamente.

La consecuencia: cuando el SDO es de alta calidad, pero la evidencia empírica es insuficiente, el análisis produce Declaración C-E — la incertidumbre empírica es el factor limitante y la intervención indicada es la investigación documental adicional según el Libro 1. El SDO bien hecho no puede compensar la ausencia de evidencia empírica sobre w.

Hay una situación especial de este caso límite que merece señalarse: cuando la observación SDO revela que el Hijo dominante del actor es

La transformación formal

Anteros con S muy baja (alta idiosincrasia) pero los rangos de R* son tan amplios que R*_neta puede ser alto o bajo según el extremo del rango. En ese caso, incluso la certeza sobre S no resuelve el problema porque la incertidumbre sobre R* domina la incertidumbre sobre R*_neta. La investigación documental adicional es el único camino hacia la robustez.

El caso de los archivos destruidos — cuando ningún SDO puede salvar la robustez Una organización fraudulenta destruyó sistemáticamente todos los registros electrónicos antes de que la investigación comenzara. Solo quedan testimonios de tres ex empleados con versiones parcialmente contradictorias. El SDO de los actores disponibles produce localización precisa (Anteros deliberado en el Director con P(Anteros) = 0.88, S ∈ [0.08, 0.28]). Pero los pesos w de las aristas del grafo solo pueden estimarse con rangos muy amplios: w(Director→Protocolo) ∈ [0.30, 0.85]. R* del Director ∈ [0.22, 0.65]. R*_neta_Director ∈ [0.22×0.72, 0.65×0.92] = [0.158, 0.598]. Los rangos se solapan con R*_neta de otros actores. Declaración D empírica. El SDO preciso no puede compensar la falta de documentos.

### V.  Tercer caso límite: cuando ninguno de los tres puede resolver lo que el caso requiere

Hay casos donde el sistema completo — SDO, Prometeo y ECO funcionando correctamente con toda la calidad de observación y evidencia disponible — no puede producir lo que el caso requiere. Reconocer esos casos con precisión es la honestidad epistemológica que el sistema debe mantener.

Estos son los límites reales del paradigma como sistema integrado — no los límites de Prometeo o del SDO individuales (que los capítulos anteriores establecieron) sino los del paradigma como totalidad. Hay tres tipos de casos donde el paradigma completo no puede resolver:

Límite real 1 — Casos donde R* distribuido equivalente existe, pero el campo no puede imputarlo

El sistema puede calcular R* con Declaración A robusta, pero el resultado no puede usarse porque el campo de imputación (el sistema jurídico, la institución, el colectivo) no tiene los mecanismos para actuar sobre esa imputación. El diseñador invisible tiene R*_neta = La transformación formal

### 0.65 con robustez completa, pero el sistema jurídico del caso no tiene una categoría de responsabilidad que corresponda a ese tipo de condición causal necesaria distal.

En ese caso el sistema completó su trabajo — produjo la imputación correcta. Lo que falta no es en el sistema sino en el mecanismo de φ₂ exterior colectivo (el sistema jurídico o institucional) para actuar sobre esa imputación. El sistema puede señalar esa brecha — puede producir el análisis y declarar que el sistema de imputación existente no tiene la categoría para procesarlo — pero no puede crear el mecanismo que falta.

Límite real 2 — Casos donde la brecha empírica es irreducible

El sistema produce Declaración D empírica y la investigación adicional no puede cerrar la brecha porque la evidencia fue destruida, nunca existió, o está protegida por privilegios que el proceso de investigación no puede levantar. En ese caso el sistema no puede producir resultados robustos sobre R*_neta independientemente de la calidad del SDO o del ECO.

El sistema puede declarar con precisión qué evidencia específica cerraría la brecha — eso es la Declaración D bien formulada. Pero no puede obtener esa evidencia. Ese límite no es del paradigma sino del acceso epistémico al caso.

Límite real 3 — Casos donde el ego está en Aego estructural permanente

El sistema puede diagnosticar con el SDO que el ego está en Origen B profundo — Aego que no responde a ninguna intervención del ECO. El ECO trabaja la primera fase con genuino esfuerzo y el Aego no tiene indicadores de movimiento después de un período razonable. En ese caso, la reducción de Δ por integración genuina no es posible para ese ego en ese estado.

El sistema puede declarar con precisión ese estado, puede describir las condiciones hipotéticas bajo las cuales la primera fase del ECO podría eventualmente producir movimiento (si las condiciones del campo del ego cambian de manera que reduzcan la presión que produjo el Aego), y puede orientar el trabajo hacia las consecuencias externas del Δ alto

La transformación formal

### (qué puede el colectivo hacer desde afuera ante la imposibilidad de integración interna). Pero no puede forzar la restauración de φ₂.

Estos tres límites reales no son vergüenzas del paradigma. Son la honestidad que hace posible que el paradigma sea confiable cuando sí funciona. Un sistema que pretende resolver todos los casos produce falsa certeza. Un sistema que sabe exactamente cuáles casos puede resolver y cuáles no produce certeza real en los que puede resolver y transparencia en los que no puede.

### VI.  Los cinco perfiles de casos y sus protocolos de uso del sistema

### Para hacer el mapa más operativo, el capítulo identifica cinco perfiles de casos que el sistema enfrenta con frecuencia y establece el protocolo de uso para cada uno.

Perfil A —  Caso de responsabilidad causal clara con actores disponibles Descripción: El caso tiene suficiente evidencia documental para construir el grafo con rangos w moderados, y los actores están disponibles para observación SDO directa. Instrumento primario: SDO + Prometeo + ECO en secuencia completa Protocolo: SDO directo de todos los actores del grafo → construcción del grafo con ajuste IIC → cálculo de R*, S, R*_neta, α, Δ → análisis de sensibilidad extendido → si Δ > 0.15, diagnóstico del tipo y trabajo del ECO.

Perfil B —  Caso histórico con actores no disponibles y evidencia moderada Descripción: El caso se analiza después del evento, los actores no están disponibles para entrevista SDO, pero hay documentación histórica moderadamente buena que permite inferir P(Hijos). Instrumento primario: SDO retrospectivo + Prometeo Protocolo: SDO retrospectivo desde documentos históricos, testimonios y patrones de comportamiento → P(Hijos) con rangos más amplios → análisis de sensibilidad con incertidumbre ontológica alta → si hay robustez a pesar de la incertidumbre, Declaración A o B; si no, Declaración C-O con especificación de qué observación adicional reduciría la incertidumbre.

Perfil C —  Caso con necesidad de ECO sin análisis de responsabilidad externa Descripción: El trabajo del ECO es el objetivo principal — el ego quiere reducir su Δ sin que haya un proceso externo de imputación. No hay caso de Prometeo porque no hay colectivo que impute. Instrumento primario: SDO + ECO (sin Prometeo externo)

La transformación formal

Protocolo: SDO para localizar v_t y c del ego y diagnosticar el tipo de Δ → el 'R*' es el que el propio ego reconoce como su contribución causal (puede ser informal o basado en el relato del ego) → ECO trabaja desde el Δ_subjetivo = R*_percibido − α_observado.

Perfil D —  Caso institucional con IIC bajo y múltiples actores Descripción: La institución tiene IIC bajo, hay múltiples actores en el grafo con distintas posiciones de v_t, y el objetivo es determinar R*_neta del diseñador institucional vs. los ejecutores. Instrumento primario: SDO institucional + Prometeo con ajuste IIC + ECO institucional Protocolo: SDO institucional (IIC + localización del Eje II de múltiples actores) → construcción del grafo con ajuste por IIC según capítulo 3.2 → cálculo de R*_neta con S ajustada por IIC para ejecutores → si Δ institucional > 0.20, trabajo del ECO institucional con φ₂_col.

Perfil E —  Caso en Declaración D — máxima incertidumbre en los dos tipos Descripción: La evidencia documental es muy escasa y los actores clave no están disponibles. El análisis produce rangos amplios en w Y en P(Hijos). La conclusión sobre R*_neta no es robusta. Instrumento primario: Diagnóstico de ambas incertidumbres + especificación de lo que las resolvería Protocolo: Análisis parcial de ambos tipos de incertidumbre → identificar cuál domina → Declaración D con especificación: (a) qué evidencia documental específica cerraría la brecha empírica y (b) qué observación SDO específica cerraría la brecha ontológica → si ninguno es accesible, declarar el límite del paradigma y especificar qué mecanismo de φ₂ exterior podría operar en ausencia de certeza.

### VII.  El protocolo de coordinación entre practicantes del sistema

El sistema integrado puede ser operado por un solo mediador que domina los tres instrumentos, o por un equipo donde distintos practicantes especializados proveen cada instrumento. El segundo caso requiere un protocolo de coordinación explícito que evite los errores de desconexión.

### Los puntos críticos de la coordinación entre practicantes:

El practicante del SDO debe proveer al practicante de Prometeo la distribución P(Hijos) en el formato operativo que el capítulo 4.2 requiere — no solo la localización cualitativa ('este actor está en Fobos') sino la distribución con probabilidades para los Hijos

La transformación formal

candidatos. Esa distribución es el insumo para la propagación de la incertidumbre ontológica al cálculo. El practicante de Prometeo debe proveer al practicante del ECO R* y Δ actualizados con los rangos del análisis de sensibilidad extendido. No el R* de un análisis empírico anterior sin la corrección por S — el R*_neta que resulta de la integración de la observación SDO en el cálculo. El practicante del ECO debe reportar al practicante del SDO el movimiento de α observado durante el trabajo — los indicadores de avance (capítulo 5.2) que permiten actualizar la distribución P(Hijos) en φ₂. Esa actualización permite al practicante de Prometeo recalcular Δ con el nuevo α.

El ciclo de coordinación — SDO informa a Prometeo, Prometeo informa al ECO, ECO informa al SDO — es el círculo virtuoso del capítulo 5.2 formalizado como protocolo de equipo. Cuando la coordinación funciona, el análisis se vuelve más preciso con cada ciclo: la observación SDO mejora las estimaciones de S y α, Prometeo produce Δ más preciso, el ECO trabaja con mayor orientación, el α sube, el ciclo vuelve a comenzar.

### VIII.  El mapa sintetizado: una tabla de decisiones para el mediador

Sí / aplica No / no aplica Instrumento

Pregunta de diagnóstico

Usar SDO para estimar S. El análisis requiere P(Hijos) en φ₁.

Si el objetivo es R* total (no idiosincrática), SDO para S puede omitirse.

¿El objetivo es determinar responsabilidad idiosincrática (R*_neta)?

SDO + Prometeo

SDO directo. P(Hijos) con mayor certeza. S más precisa.

SDO retrospectivo. P(Hijos) con mayor incertidumbre. Declaración C-O más probable.

¿Los actores están disponibles para observación SDO directa?

SDO modo

directo / retrospectivo

Prometeo puede producir resultados robustos con los dos tipos de incertidumbre bien gestionados.

Declaración C-E o D empírica. Prometeo señala qué evidencia específica resolvería la brecha.

¿La evidencia documental es suficiente para rangos w moderados?

Prometeo /

Libro 1

La transformación formal

Sí / aplica No / no aplica Instrumento

Pregunta de diagnóstico

Ajustar w de aristas estructurales según capítulo 3.2. S de ejecutores puede ser alta.

Sin ajuste IIC. w empírico sin modificación por campo disfórico.

¿El IIC institucional es bajo?

Ajuste IIC en

grafo

ECO

Tipo A: ECO trabaja con v_t para que φ₂ pueda operar. Tipo B: ECO restaura φ₂ primero.

Δ ≤ 0.15: equilibrio razonablemente alcanzado. Verificar autenticidad vs. adaptación conductual.

¿Δ > 0.15 con diagnóstico SDO del tipo?

Origen A: ECO trabaja con Anteros negativo, Fobos o Deimos. Objetivo: mover v_t. Origen B: ECO restaura φ₂ antes del contenido.

Sin diagnóstico del tipo: el trabajo del ECO no puede orientarse correctamente.

¿El Δ alto es Origen A u Origen B?

SDO diagnóstico Origen A/B

Límite del paradigma en este caso. Declarar con precisión qué resolvería cada tipo y si alguno es accesible.

¿El análisis produce Declaración D en los dos tipos?

Límite real del

paradigma

### IX.  Lo que la Parte V estableció y lo que queda para el Volumen II

La Parte V estableció la integración de los tres instrumentos con la precisión que las cuatro partes anteriores hacen posible. El SDO como perspectiva interior que provee los insumos ontológicos. Prometeo como perspectiva exterior que calcula desde esos insumos más la evidencia del mundo. El ECO como perspectiva del proceso mismo que trabaja en el espacio que los otros dos definen, pero ninguno resuelve.

Con la Parte V, el Volumen I está completo. Las derivaciones formales de la Parte II, la escala colectiva de la Parte III, la gestión de la incertidumbre de la Parte IV, y la integración de la Parte V — todo descansa sobre la demostración de la Parte I: el SDO y el Método Prometeo son el mismo sistema visto desde adentro y desde afuera. La transformación formal de ese sistema es lo que este volumen realizó.

La transformación formal

Lo que queda para el Volumen II son exactamente las dimensiones que el Volumen I estableció como necesarias pero que no puede proveer por sí solo: la calibración empírica de los parámetros (los valores de γ, β, IIC_umbral para distintos dominios), los estudios que documentan la precisión del SDO como instrumento de estimación de S y α, y los análisis de casos que verifican que el sistema produce distribuciones de R*_neta que corresponden a la intuición moral de responsabilidad de los expertos en esos dominios.

El Volumen II es el trabajo empírico que el Volumen I hizo posible al establecer exactamente qué necesita ser calibrado, medido y verificado. Sin el Volumen I, el Volumen II no sabría qué medir. Sin el Volumen II, el Volumen I es una estructura formal sin anclaje en el mundo de los casos reales.

Cierre del Volumen I

El SDO y el Método Prometeo son el mismo sistema visto desde adentro y desde afuera. No son dos sistemas paralelos que se iluminan mutuamente porque describen dominios cercanos. Son dos vocabularios que corresponden a dos perspectivas sobre el mismo proceso — la doble mediación del ego. Lo que el SDO observa como Hijo en φ₁, Prometeo lo calcula como S. Lo que el SDO observa como Hijo en φ₂, Prometeo lo calcula como α. Lo que el SDO diagnostica como Δ de asunción, Prometeo lo mide como R* − α. Lo que el SDO localiza como disforia institucional, Prometeo lo captura como IIC. Y la tercera perspectiva — la del proceso mismo — es lo que el ECO acompaña cuando trabaja con φ₂ para que el ego pueda integrar lo que le pertenece.  Eso es lo que este volumen demostró.

La transformación formal

Notas al capítulo 5.3

1 El Perfil C — caso de ECO sin Prometeo externo — puede parecer inusual: ¿cómo puede el ECO trabajar con Δ si no hay un Prometeo que haya calculado R* formalmente? La respuesta es que en ese contexto el 'R*' que el ECO usa es el que el propio ego reconoce o que el campo relacional del ego le señala informalmente. Todo ego tiene alguna percepción de los colapsos que produjo y de cuánto ha asumido de ellos. Δ_subjetivo = R*_percibido − α_observado puede calcularse informalmente en el contexto del ECO sin necesidad de un análisis formal de Prometeo. Cuando el Perfil C evoluciona hacia un caso con implicaciones para terceros (el ego descubre que los colapsos no asumidos afectaron a otros), puede volverse necesario el análisis formal de Prometeo para determinar R*_real en lugar del R*_percibido.

2 La coordinación entre practicantes del sistema tiene implicaciones para la formación de mediadores en el paradigma. El sistema de rangos de Meriadock — Interventor, Didacta, Indagador — con sus cinco especialidades (Organizacional, Estructural, Modelador, Educativo, Crisis) establece perfiles de competencia distintos que corresponden a distintas combinaciones de los tres instrumentos. Un Modelador con rango de Indagador tiene dominio pleno de los tres instrumentos y puede operar el sistema integrado unipersonalmente. Un Interventor puede tener dominio de uno o dos instrumentos y necesitará coordinación con otros practicantes para los casos que requieran el tercer instrumento.

3 El Perfil E — máxima incertidumbre en los dos tipos — no es un fracaso del sistema sino la declaración honesta de sus límites en ese caso específico. La forma correcta de reportar el Perfil E no es 'el análisis no pudo completarse' sino 'el análisis produjo los siguientes resultados parciales, con la siguiente incertidumbre en los dos tipos, y las siguientes condiciones que permitirían reducir cada tipo'. Esa declaración tiene valor para el campo de imputación, aunque no produzca una distribución de R*_neta robusta: delimita exactamente lo que se sabe, lo que no se sabe, y cómo podría saberse.

4 El mapa de uso que este capítulo establece es el mapa del Volumen I — del sistema formal derivado desde la ontología. El Volumen II añadirá al mapa los protocolos específicos por dominio (laboral, organizacional, jurídico, histórico, deportivo), los instrumentos de calibración de los parámetros β, γ e IIC_umbral, y los estudios de validación que permiten evaluar si las Declaraciones del sistema corresponden a las distribuciones de responsabilidad que los expertos del dominio considerarían correctas. El mapa de este capítulo es el esqueleto conceptual; el Volumen II construye la carne sobre ese esqueleto.

La transformación formal

La transformación formal — Volumen I

