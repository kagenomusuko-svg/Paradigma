### Capítulo U·4

### La Declaración y los resultados del

análisis de sensibilidad Los cuatro tipos de resultado según la robustez del análisis

### I.  Función de este capítulo

El sistema de Prometeo no produce un número: produce una Declaración. El número es un instrumento intermedio; la Declaración es el producto final que el analista entrega al foro —tribunal, consejo de administración, equipo clínico, comité de investigación— y que el foro puede usar directamente.

La diferencia entre un número y una Declaración es la diferencia entre decir ‘el R*_neta de CD es 22.8%’ y decir ‘CD tiene el mayor peso causal idiosincrático del caso en todo el espacio de variación de los parámetros; esa conclusión es robusta e independiente de la incertidumbre de las aristas’. El número informa. La Declaración concluye. Y el foro necesita conclusiones, no números.

Este capítulo establece los cuatro tipos de Declaración que el sistema puede producir, las condiciones exactas que determinan cuál se emite, el formato de redacción de cada una, y lo que el analista y el foro hacen con cada tipo. También establece el análisis de sensibilidad como el instrumento que determina la Declaración: sin sensibilidad no hay Declaración posible.

Taxonomía General de Aplicaciones

### II.  El análisis de sensibilidad como fundamento de la Declaración

Cada peso w de cada arista del grafo es un intervalo [w_mín, w_máx], no un punto. Cada P(Hijos) tiene incertidumbre. Cada α tiene un rango. El espacio de variación es el conjunto de todas las combinaciones posibles de estos parámetros dentro de sus rangos admisibles. El análisis de sensibilidad calcula R*, R*_neta, Δ y D_total en todo ese espacio y determina si la conclusión cambia o se mantiene.

Las dos dimensiones de la sensibilidad

Sensibilidad empírica: variación de los rangos w de las aristas dentro de los límites que la tabla E0–E8 admite para el tipo de evidencia declarado. Esta dimensión responde a la pregunta: ¿la conclusión cambia si los pesos de las aristas se mueven dentro de lo que la evidencia permite?

Sensibilidad ontológica: variación de P(Hijos) dentro de los límites de incertidumbre de la localización del Hijo (cap. U·1), que produce variación en S por la Ruta A (cap. U·3). Esta dimensión responde a la pregunta: ¿la conclusión cambia si el Hijo dominante del actor no es el que el árbol de decisión sugirió?

Las dos dimensiones operan simultáneamente. La Declaración refleja lo que ocurre cuando ambas varían al mismo tiempo. Un análisis de sensibilidad que solo varía los pesos w sin variar P(Hijos) —o viceversa— es incompleto y puede producir una Declaración de robustez mayor de la que el caso soporta.

El espacio de variación Es el producto cartesiano de todos los rangos admisibles de todos los parámetros del análisis: w de cada arista × P(Hijos) de cada actor × α de cada actor. La Declaración se basa en lo que ocurre en TODO ese espacio, no en un escenario seleccionado.

### III.  Las cuatro Declaraciones

Taxonomía General de Aplicaciones

El sistema produce exactamente cuatro tipos de resultado. No hay un quinto tipo ni hay posiciones intermedias. Cada caso produce exactamente una Declaración. La determinación de cuál se emite es algorítmica: depende de lo que el análisis de sensibilidad produce, no del juicio del analista.

Declaración A — Robustez completa

Condición Contenido

El mismo nodo tiene mayor R* (o R*_neta) en todo el espacio de variación de los parámetros — todos los rangos w y todos los Hijos plausibles.

La conclusión es independiente de la incertidumbre. Formato breve: identificación del nodo, valores centrales de R*_neta, afirmación de robustez con cobertura del análisis de sensibilidad.

La Declaración A es la más potente y la menos frecuente. Requiere que ningún punto del espacio de variación cambie la identidad del nodo líder. Es la única Declaración que permite al foro actuar sin cualificación: el nodo identificado tiene el mayor peso causal idiosincrático con independencia de la incertidumbre.

Formato de redacción — Declaración A ‘El análisis de sensibilidad establece que [nodo] tiene el mayor R*_neta del caso, con un valor central de [X]%, en todo el espacio de variación de los parámetros. Esta conclusión es robusta: se mantiene con cualquier combinación admisible de los pesos w de las aristas (rangos E0–E8 declarados) y con cualquier distribución plausible de P(Hijos) para los actores del caso. El R*_neta mínimo de [nodo] en el espacio de variación es [Y]%; el R*_neta máximo del segundo nodo en el espacio de variación es [Z]%. La brecha mínima es [Y−Z]%.’

Qué hace el foro con la Declaración A

El tribunal, el consejo de administración o el comité puede tratar la identidad del nodo líder como establecida. La cuantificación exacta de R*_neta varía dentro del rango declarado, pero esa variación no cambia quién es el

Taxonomía General de Aplicaciones

responsable principal. El foro delibera sobre la consecuencia, no sobre la identidad.

Declaración B — Nodo líder robusto, magnitudes variables

Condición Contenido

El mismo nodo lidera en todo el espacio de variación pero la magnitud de la diferencia varía significativamente.

La identidad del responsable principal es robusta; la cuantificación exacta no lo es. Especificar el rango de la diferencia y las condiciones de variación.

La Declaración B es la más frecuente en la práctica. El nodo líder no cambia, pero la distancia entre el líder y el segundo nodo oscila. En un extremo del espacio de variación, el líder tiene R*_neta de 35% y el segundo 10%; en el otro extremo, el líder tiene 22% y el segundo 19%. La identidad del responsable es robusta; la cuantificación del ajuste debitor no lo es.

Formato de redacción — Declaración B ‘El análisis de sensibilidad establece que [nodo] tiene el mayor R*_neta del caso en todo el espacio de variación de los parámetros. Esta conclusión sobre la identidad del responsable principal es robusta. Sin embargo, la magnitud de la diferencia varía significativamente: en el escenario más favorable para [nodo], la brecha con el segundo nodo ([nodo2]) es de [X]%; en el escenario más favorable para [nodo2], la brecha es de [Y]%. Las aristas sensibles que producen esta variación son: [lista con tipo E y rango w]. La evidencia adicional que estrecharía el rango es: [especificación concreta].’

Qué hace el foro con la Declaración B

El foro puede tratar la identidad del nodo líder como establecida. Para la cuantificación del ajuste debitor, el foro tiene dos opciones: usar el escenario central como mejor estimación, o solicitar la evidencia adicional que el analista identificó como necesaria para estrechar el rango. La Declaración B frecuentemente produce que el tribunal ordene

Taxonomía General de Aplicaciones

la práctica de la evidencia adicional —y eso es exactamente para lo que está diseñada.

Taxonomía General de Aplicaciones

Declaración C — Candidato sin robustez completa

Condición Contenido

La evidencia base sugiere un candidato pero la conclusión cambia en alguna parte del espacio de variación.

Especificar en cuál parte del espacio cambia la conclusión y por qué. Identificar la evidencia adicional que resolvería la ambigüedad.

La Declaración C es la más informativa para el foro porque nombra con precisión lo que falta. No dice ‘no se puede concluir’: dice ‘la conclusión depende de [esto específico] y la evidencia que lo resolvería es [esto otro específico]’. Transforma la incertidumbre en una pregunta concreta que el foro puede responder.

Formato de redacción — Declaración C ‘El análisis de sensibilidad establece que [nodo1] es el candidato con mayor R*_neta en el escenario base, con un valor central de [X]%. Sin embargo, la conclusión no es robusta: en [descripción específica de la parte del espacio donde cambia], [nodo2] asume el liderazgo con R*_neta de [Y]%. La arista que determina el cambio es [arista] con tipo de evidencia [E…] y rango [a, b]. La evidencia específica que resolvería la ambigüedad es: [descripción concreta y obtenible]. Si esa evidencia clasifica la arista como [tipo superior], la conclusión sería firme a favor de [nodo1]. Si la clasifica como [tipo inferior], a favor de [nodo2].’

Qué hace el foro con la Declaración C

El foro no puede tratar la identidad del nodo líder como establecida. Lo que puede hacer es evaluar si la evidencia adicional identificada es obtenible y, si lo es, ordenar su práctica. La Declaración C convierte la incertidumbre científica en una decisión procesal: ¿practicar la evidencia adicional o decidir con la incertidumbre declarada? Esa decisión es del foro, no del analista.

La diferencia entre B y C es precisa: en B, la identidad del líder no cambia, aunque las magnitudes varíen. En C, la identidad del líder sí cambia en alguna parte del espacio. La frontera entre B y C es operativamente crítica porque

Taxonomía General de Aplicaciones

### determina si el foro puede actuar sobre la identidad o necesita evidencia adicional.

Declaración D — Evidencia insuficiente

Condición Contenido

La incertidumbre es demasiado alta para producir ninguna conclusión sobre la distribución de R*_neta.

Especificar: (a) qué evidencia empírica específica resolvería la brecha, (b) qué observación SDO/ECO adicional resolvería la incertidumbre ontológica, (c) si alguno de los dos es accesible en el caso.

La Declaración D ya fue introducida en el cap. U·2 como el instrumento que orienta la investigación siguiente. Este capítulo la sitúa en el sistema completo de las cuatro Declaraciones. La Declaración D no es el fracaso del análisis: es el sistema funcionando correctamente ante evidencia insuficiente. Un analista que fuerza una Declaración A, B o C cuando la evidencia solo soporta D está produciendo un documento más vulnerable que uno que declara D con precisión.

Formato de redacción — Declaración D ‘El análisis de sensibilidad establece que la incertidumbre de los parámetros es demasiado alta para producir ninguna conclusión sobre la identidad del nodo de mayor R*_neta. En el espacio de variación, [N] nodos distintos asumen el liderazgo según la combinación de parámetros. La evidencia empírica que resolvería la brecha: [especificación concreta, obtenible, con referencia a la arista o nodo sensible]. La observación SDO/ECO que resolvería la incertidumbre ontológica: [especificación: qué localización en presencia, qué Hijo necesita confirmarse, qué α necesita evaluarse]. Accesibilidad: [evaluación de si la evidencia identificada es obtenible en el caso específico. Si es obtenible, la Declaración D es provisional. Si no es obtenible, la Declaración D es terminal].’

Qué hace el foro con la Declaración D

Taxonomía General de Aplicaciones

Si la evidencia adicional es obtenible, el foro ordena su práctica y el analista recalcula cuando llegue. La Declaración D provisional puede convertirse en A, B o C. Si la evidencia no es obtenible, el foro debe decidir si procede con la incertidumbre declarada o si la incertidumbre impide la resolución del caso. Esa es una decisión del foro, no del analista.

Taxonomía General de Aplicaciones

### IV.  El árbol de determinación de la Declaración

La determinación de cuál Declaración emitir sigue una secuencia algorítmica que el analista no puede alterar con criterio propio. La secuencia opera de arriba hacia abajo: si la condición de A se cumple, se emite A y el proceso termina; si no, se evalúa B; si no, C; si no, D.

Paso 1: Ejecutar el análisis de sensibilidad completo

Calcular R*_neta para cada nodo en múltiples puntos del espacio de variación. Mínimo: tres escenarios —central, más favorable para el candidato líder, más favorable para el segundo candidato—. Óptimo: barrido sistemático del espacio de variación con la plantilla de cálculo del Apéndice A3.

Paso 2: Identificar si el nodo líder cambia

No cambia en ningún punto → ir al Paso 3.

Cambia en alguna parte del espacio → Declaración C si hay un candidato base identificable; Declaración D si hay más de dos nodos que asumen el liderazgo en distintas partes del espacio sin un patrón claro.

Paso 3: Evaluar la variación de la magnitud

La brecha entre el líder y el segundo es estable (variación < 30% del valor central) → Declaración A.

La brecha varía significativamente (variación ≥ 30% del valor central) → Declaración B.

Criterio del 30% El umbral del 30% de variación de la brecha es orientativo, no absoluto. Un analista puede justificar un umbral diferente si las condiciones del caso lo requieren, siempre que documente el umbral utilizado y el razonamiento. Lo que no puede hacer es no especificar un umbral: la diferencia entre A y B debe ser operativamente clara.

Taxonomía General de Aplicaciones

Resumen del árbol

Declaración Condición del análisis de

Acción del foro

sensibilidad

A El nodo líder no cambia y la brecha es estable.

Actuar sobre la identidad y la cuantificación. La conclusión es firme.

B El nodo líder no cambia pero la brecha varía significativamente.

Actuar sobre la identidad. Para la cuantificación, usar el escenario central o solicitar evidencia adicional.

C El nodo líder cambia en alguna parte del espacio. Hay un candidato base.

No actuar sobre la identidad sin evidencia adicional. Evaluar si la evidencia es obtenible.

D Múltiples nodos asumen el liderazgo sin patrón claro. Incertidumbre demasiado alta.

Ordenar la evidencia adicional identificada o decidir que la incertidumbre impide la resolución.

### V.  Errores frecuentes en la emisión de Declaraciones

Los errores de emisión son sistemáticos y anticipables. Cada uno tiene una dirección específica: o sobreestima la robustez (emite A o B cuando debería emitir C o D) o la subestima (emite C o D cuando la evidencia soporta A o B).

Error 1: Emitir A cuando la sensibilidad no cubre P(Hijos)

El analista ejecutó el análisis de sensibilidad variando los pesos w, pero no varió P(Hijos). El nodo líder no cambió en el espacio de variación empírico, pero podría cambiar si la localización del Hijo fuera diferente. La Declaración A requiere robustez en las dos dimensiones de sensibilidad (empírica y ontológica). Sin la segunda, la Declaración correcta es B o C, no A.

Taxonomía General de Aplicaciones

Error 2: Emitir D por comodidad

El analista emite D porque no quiere comprometerse con una conclusión que podría ser atacada. La Declaración D no es un refugio: es un instrumento con contenido obligatorio específico. Una Declaración D que dice ‘la evidencia es insuficiente’ sin especificar qué evidencia resolvería la brecha es una Declaración D incompleta e inutilizable por el foro.

Error 3: Confundir la identidad del líder con la magnitud del AD

La Declaración B dice que la identidad del líder es robusta. No dice que la cuantificación del ajuste debitor sea precisa. Un foro que lee B como si fuera A y usa la cifra central del AD sin considerar el rango puede producir una resolución que la contraparte puede impugnar con éxito mostrando que la cifra varía significativamente dentro del espacio declarado.

Error 4: Emitir C cuando la evidencia soporta B

El analista identifica una pequeña región del espacio de variación donde el líder cambia, pero esa región corresponde a combinaciones de parámetros que son técnicamente admisibles, pero empíricamente implausibles. La pregunta crítica: ¿la parte del espacio donde cambia el líder corresponde a combinaciones de parámetros que el caso podría razonablemente soportar, o son combinaciones extremas? Si solo las combinaciones extremas producen el cambio, la Declaración correcta puede ser B, no C. El analista debe justificar esta evaluación explícitamente.

Taxonomía General de Aplicaciones

### VI.  La Declaración como documento del expediente

La Declaración es el tercer documento del expediente de Prometeo —después de la hoja de calibración (Documento 1) y la tabla de sensibilidad (Documento 2). No es un resumen del análisis: es un documento autónomo que el foro puede leer sin necesidad de examinar los documentos anteriores y que contiene toda la información necesaria para que el foro tome una decisión.

Componentes obligatorios de toda Declaración

### 1. Tipo de Declaración: A, B, C o D, con la condición que la produce enunciada explícitamente.

### 2. Identificación de nodos: el nodo líder (en A y B), el candidato base (en C), o la lista de nodos que compiten (en D).

### 3. Valores numéricos centrales: R*_neta, S, α y Δ del nodo líder o candidato, con rangos del análisis de sensibilidad.

### 4. Cobertura de la sensibilidad: enumeración de qué se varió (pesos w, P(Hijos), α), en qué rangos, y cuántos escenarios se evaluaron.

### 5. Aristas sensibles: identificación de las aristas cuya variación tiene mayor impacto en la conclusión. Solo en B, C y D.

### 6. Evidencia adicional: especificación de qué evidencia estrecharía los rangos o resolvería la ambigüedad. Solo en B, C y D.

### 7. Firma del analista: nombre, credenciales, fecha, y declaración de que el análisis se realizó con la metodología del Método Prometeo.

Lo que la Declaración no contiene

Taxonomía General de Aplicaciones

La Declaración no contiene recomendaciones sobre qué hacer con el resultado. No dice ‘CD debe pagar $8M’: dice ‘el ajuste debitor de CD oscila entre $5.2M y $8.4M según el escenario de calibración’. La determinación de la consecuencia es del foro. La Declaración provee el mapa; el foro decide qué hacer con el territorio.

### VII.  Recapitulación operativa

Cuatro Declaraciones, no más: A (robustez completa), B (identidad robusta, magnitudes variables), C (candidato sin robustez), D (evidencia insuficiente). Cada caso produce exactamente una.

El análisis de sensibilidad determina la Declaración: la identidad del líder cambia o no cambia en el espacio de variación. Si no cambia, la brecha es estable o no. Esta secuencia es algorítmica.

Las dos dimensiones de la sensibilidad: empírica (variación de w) y ontológica (variación de P(Hijos)). Las dos deben cubrirse simultáneamente.

La Declaración D no es fracaso: es orientación. Especifica qué evidencia resolvería la brecha y si es obtenible. Un D con contenido es más útil que un B forzado.

La Declaración es un documento autónomo del expediente: el foro puede leerla sin examinar la hoja de calibración ni la tabla de sensibilidad. Contiene todo lo necesario para que el foro tome una decisión.

El analista produce el mapa; el foro decide sobre el territorio: la Declaración no recomienda consecuencias. Provee la distribución causal, la robustez de esa distribución, y la evidencia que la mejoraría. Lo demás es del foro.

Taxonomía General de Aplicaciones

Nota de cierre de la Parte U. Con los cuatro capítulos de la Parte U —el árbol de decisión del Hijo (U·1), el protocolo de evidencia contradictoria (U·2), las dos rutas hacia S con el mapa SDO → modelo (U·3), y las Declaraciones A–D (U·4)—, el analista tiene el núcleo metodológico completo del Libro 1. Cualquier capítulo de las Partes I–XIII puede leerse con la Parte U como referencia. La Parte U no se repite en cada capítulo de dominio: se referencia. El analista entrenado en la Parte U puede trabajar con cualquier subcampo.

— Fin del Capítulo U·4 —

— Fin de la Parte U · Protocolo Universal —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

