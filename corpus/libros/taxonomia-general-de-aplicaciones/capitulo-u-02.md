PARTE U · Protocolo Universal

### Capítulo U·2

### El protocolo de decisión para evidencia

contradictoria Qué hacer cuando la evidencia no converge

### I.  Función de este capítulo

Cuando distintos tipos de evidencia sobre la misma arista o el mismo nodo apuntan en direcciones distintas, el analista necesita reglas explícitas para resolver la contradicción. No intuición, no experiencia acumulada, no sentido común: protocolo documentable. Este capítulo provee ese protocolo.

El problema no es infrecuente. Un documento directo (E1) indica que el actor instruyó la operación; un testimonio convergente (E3) indica que el actor no tenía conocimiento de ella. Un peritaje forense (E2) reconstruye una cadena causal; otro peritaje igualmente calificado reconstruye una cadena distinta. Un actor contradice sistemáticamente su propia versión de los hechos en distintas fuentes. En todos estos casos, la contradicción no es un defecto del análisis sino información que el análisis debe procesar.

El capítulo establece cuatro instrumentos: la jerarquía general de tipos de evidencia, la regla de intersección para rangos compatibles, la regla de prioridad para rangos incompatibles, y el protocolo para cuando la contradicción misma es

Taxonomía General de Aplicaciones

### evidencia diagnóstica. Cierra con el formato de la Declaración D —el instrumento que el analista produce cuando la evidencia es insuficiente para concluir.

Lo que este capítulo no resuelve Las jerarquías específicas de evidencia por dominio —esas las establece el §2 de cada capítulo de las Partes I–XIII. Este capítulo establece los principios generales de jerarquía; los capítulos de dominio los concretan. Tampoco resuelve cómo se propaga la incertidumbre al cálculo de R* —eso es el Libro 2, cap. 4.2.

### II.  La jerarquía general de tipos de evidencia

Toda evidencia no pesa lo mismo. La tabla E0–E8 del Método Prometeo establece la referencia de calibración central: para cada tipo de evidencia, un rango de peso admisible [w_mín, w_máx] dentro del cual el peso de una arista es técnicamente razonable. Los rangos no son franjas de certeza subjetiva del analista: son límites derivados de la estructura epistémica del tipo de evidencia. Asignar un peso fuera del rango admisible para el tipo declarado es el error de calibración más frecuente y el más fácil de detectar.

La jerarquía compacta

Tipo Rango

Descripción

w

E1 [0.75, 0.95] Documento directo que registra la instrucción o la decisión causal: contrato, correo explícito, acta de acuerdo, orden de compra, plano firmado.

E2 [0.55, 0.75] Análisis pericial que reconstruye la cadena causal a partir de documentos: dictamen contable, análisis forense, peritaje de materiales.

E3 [0.40, 0.60] Testimonios convergentes de fuentes independientes con documentación parcial. Dos o más testigos que no se coordinaron y cuyas versiones son compatibles.

Taxonomía General de Aplicaciones

E4 [0.35, 0.55] Correlación estadística documentada: datos que muestran asociación sistemática entre la acción del nodo y el resultado, sin cadena causal completa.

E5 [0.30, 0.50] Testimonio único con documentación parcial que lo corrobora. Un testigo cuya versión tiene sustento documental parcial.

E6 [0.25, 0.45] Posición estructural del nodo en el sistema: el actor tenía la posición jerárquica para haber sido causa necesaria, aunque no hay documento que lo pruebe.

E7 [0.15, 0.35] Correlación débil o indicio circunstancial: la evidencia sugiere pero no establece conexión directa ni testimonial.

E8 [0.05, 0.20] Dicho único sin corroboración o ausencia documentada de acción esperada. La evidencia es mínima.

E0 [0.00] Ausencia total de evidencia para la arista. La arista se excluye del análisis con declaración explícita.

Esta tabla es la referencia de calibración central. Cada dominio de las Partes I–XIII adapta la tabla a su tipo específico de evidencia en el §2 de cada capítulo: qué cuenta como E1 en derecho laboral no es lo mismo que qué cuenta como E1 en epidemiología. Pero la jerarquía se preserva: un documento directo siempre pesa más que un testimonio, que siempre pesa más que una correlación, que siempre pesa más que un indicio. Los rangos pueden ajustarse por dominio; la jerarquía no.

Taxonomía General de Aplicaciones

### III.  Regla de intersección: evidencia compatible con rangos distintos

Cuando dos o más tipos de evidencia sobre la misma arista producen rangos compatibles —es decir, rangos que se solapan—, el rango resultante es la intersección de los rangos individuales. La intersección estrecha el rango sin salirse de ninguno de los dos: es más precisa que cualquiera de los dos rangos individuales porque incorpora la información de ambas fuentes.

Regla de intersección Si la evidencia tipo A produce el rango [a, b] y la evidencia tipo B produce el rango [c, d], el rango resultante es [max (a, c), min (b, d)]. Condición de aplicabilidad: max (a, c) ≤ min (b, d). Si se cumple, la intersección es no vacía y el rango resultante es válido. Si no se cumple, hay contradicción genuina —ir a la Sección IV.

Ejemplo de aplicación

Una arista tiene evidencia E1 (documento directo) con rango [0.75, 0.95] y evidencia E3 (testimonios convergentes) con rango [0.40, 0.60]. La intersección es [max (0.75, 0.40), min (0.95, 0.60)] = [0.75, 0.60]. Como 0.75 > 0.60, la intersección es vacía. Esto no es un problema aritmético: es una contradicción genuina entre el documento directo y los testimonios. El analista no puede forzar la convergencia: debe ir a la Sección IV.

Otro caso: una arista tiene evidencia E2 (peritaje, [0.55, 0.75]) y evidencia E3 (testimonios convergentes, [0.40, 0.60]). La intersección es [max (0.55, 0.40), min (0.75, 0.60)] = [0.55, 0.60]. La intersección es no vacía: las dos fuentes convergen en el rango [0.55, 0.60], que es más estrecho que cualquiera de los dos rangos originales. Usar este rango como peso de la arista.

Regla de documentación de la convergencia

Taxonomía General de Aplicaciones

Cuando la intersección es no vacía, el analista registra: los dos tipos de evidencia que convergieron, sus rangos individuales, el rango resultante, y una nota de que la convergencia refuerza la solidez de la estimación. La convergencia entre fuentes independientes es información positiva sobre la calidad del análisis y debe documentarse explícitamente como factor de solidez.

### IV.  Regla de prioridad: evidencia incompatible

Cuando la intersección es vacía —cuando dos tipos de evidencia producen rangos que no se solapan—, hay contradicción genuina que el analista no puede resolver por fusión. La regla de prioridad establece cómo proceder.

Regla de prioridad Cuando el tipo de evidencia de rango superior contradice al de rango inferior, el rango del tipo superior prevalece, pero se desplaza hacia su extremo más conservador según el grado de contradicción. El desplazamiento se documenta explícitamente. Magnitud del desplazamiento: proporcional a la distancia entre los rangos. Si el rango superior es [a, b] y el inferior es [c, d] con d < a (contradicción), el rango ajustado es [a − k (a − d), b] donde k ∈ [0.1, 0.3] según la calidad de la fuente inferior.

Lógica del desplazamiento

El principio es este: la evidencia de nivel superior tiene mayor peso epistémico, pero la existencia de evidencia de nivel inferior que la contradice es información que no puede ignorarse. El desplazamiento no invalida el tipo superior: lo modera en la dirección de mayor cautela. Un documento directo (E1) que dice una cosa, contradicho por testimonios convergentes (E3) que dicen otra, sigue produciendo un rango E1 —pero un rango E1 desplazado hacia su extremo inferior porque la contradicción existe y hay que reflejarla.

Los tres niveles de contradicción

Taxonomía General de Aplicaciones

Nivel Condición Acción del analista

Contradicción leve

Los rangos están separados por menos de 0.10. La brecha es pequeña.

Desplazamiento k = 0.1. El rango superior se desplaza ligeramente. Nota de contradicción leve en la hoja de calibración.

Contradicción moderada

Los rangos están separados por 0.10 a 0.25. La brecha es significativa.

Desplazamiento k = 0.2. El rango superior se desplaza significativamente. Nota de contradicción moderada. Investigar la fuente de la discrepancia.

Contradicción severa

Los rangos están separados por más de 0.25. Las fuentes dicen cosas incompatibles.

Desplazamiento k = 0.3 o Declaración D si la contradicción es irresoluble. El analista no puede simplemente elegir un rango: debe declarar la contradicción y especificar qué evidencia adicional la resolvería.

Regla cardinal: el analista nunca fuerza la convergencia. Si la evidencia dice cosas distintas, el análisis debe reflejar esa divergencia, no ocultarla. Forzar la convergencia produce un análisis que parece más sólido de lo que es —y esa apariencia es exactamente lo que la contraparte puede atacar con mayor eficacia.

Taxonomía General de Aplicaciones

### V.  Cuando la contradicción es evidencia en sí misma

Hay un caso especial que el analista debe reconocer porque transforma el problema: cuando un actor contradice sistemáticamente en distintas fuentes su propia versión del acto. Esa inconsistencia no es un problema de calibración de la arista: es una señal diagnóstica sobre el estado de v_t del actor. La contradicción sistemática en la propia narrativa es una señal de IIC personal bajo y orienta la distribución P(Hijos).

Las dos lecturas de la contradicción propia

Anteros negativo: el actor construyó deliberadamente versiones distintas para distintos interlocutores. La contradicción no es confusión sino estrategia: el eje propio del actor se afirmó produciendo narrativas múltiples que servían a sus intereses. La firma documental de esta lectura: las versiones no son aleatorias, sino que cada una sirve un propósito identificable según el destinatario.

Fobos estratégico: el actor produjo versiones distintas como respuesta defensiva ante la percepción de amenaza: cada versión fue un intento de proteger algo sin la distancia que Anteros requiere para producir una respuesta proporcional. La firma documental: las versiones no muestran coherencia estratégica sino reactividad —cada una responde a una amenaza percibida en el momento, sin consistencia a través del tiempo.

Protocolo para la contradicción propia como evidencia diagnóstica 1. Documentar las versiones contradictorias con fuente, fecha y destinatario. 2. Evaluar si las contradicciones muestran coherencia estratégica (Anteros negativo) o reactividad (Fobos estratégico). 3. Incorporar la señal a P(Hijos) del actor con justificación observacional. 4. Registrar el IIC personal bajo como información que afecta la estimación de α: un actor que contradice sistemáticamente su narrativa tiene mayor probabilidad de α bajo, porque la asunción genuina es incompatible con la producción de versiones múltiples.

Taxonomía General de Aplicaciones

La contradicción entre fuentes externas

Cuando la contradicción no es del actor sino entre fuentes externas —dos peritajes que llegan a conclusiones distintas, testimonios que no convergen—, la contradicción no es diagnóstica del actor sino de la calidad de la evidencia. En ese caso, la regla de prioridad de la Sección IV se aplica normalmente: el tipo superior prevalece con desplazamiento, y la contradicción se documenta como factor de incertidumbre de la arista, no como señal sobre v_t.

### VI.  La Declaración D: evidencia insuficiente

Cuando la incertidumbre es demasiado alta para producir ninguna conclusión sobre la distribución de R*_neta, el analista produce una Declaración D. La Declaración D no es el reconocimiento de fracaso del análisis: es el instrumento que orienta la investigación siguiente hacia lo que concretamente necesita obtenerse.

Cuándo declarar D

La Declaración D se produce cuando se cumple al menos una de las siguientes condiciones:

(a) Contradicción severa irresoluble: dos fuentes de nivel similar producen rangos incompatibles que no pueden resolverse con la regla de prioridad porque ninguna tiene preeminencia clara sobre la otra.

(b) Aristas críticas con evidencia E7 o E8: las aristas que determinan el orden de R* entre los nodos principales están sustentadas solo con indicios circunstanciales o dichos únicos sin corroboración.

(c) El análisis de sensibilidad produce cambio de conclusión: el nodo líder cambia de identidad dentro del espacio de variación de los parámetros —lo que el cap. U·4 llamará Declaración C— y la evidencia adicional para resolver la ambigüedad no está disponible.

Taxonomía General de Aplicaciones

(d) Localización del Hijo no concluyente: P(Hijos) es no concluyente (ningún Hijo supera 0.40) para un actor cuyo Hijo dominante tiene impacto significativo en la estimación de S, y la presencia del sujeto no es accesible.

Formato de la Declaración D

Contenido obligatorio de la Declaración D (a) Qué evidencia empírica específica resolvería la brecha: qué documento, qué peritaje, qué testimonio permitiría al analista pasar de D a una Declaración A, B o C. Esta especificación debe ser concreta y obtenible: no ‘más evidencia’ sino ‘el análisis documental especializado del correo de folio 89 para determinar si la instrucción era específica o general’. (b) Qué observación SDO/ECO adicional resolvería la incertidumbre ontológica: si la brecha es sobre P(Hijos) o sobre la estimación de S desde la Ruta A, qué localización en presencia del sujeto permitiría cerrar la incertidumbre. (c) Si alguna de las dos es accesible en el caso: la Declaración D termina con una evaluación explícita de si la evidencia adicional identificada es obtenible o no. Si es obtenible, la Declaración D es provisional —puede convertirse en A, B o C cuando la evidencia llegue. Si no es obtenible, la Declaración D es terminal y el analista debe declararlo.

La Declaración D tiene una función procesal que las Declaraciones A, B y C no tienen: orienta la investigación. En un proceso judicial, la Declaración D le dice al tribunal exactamente qué evidencia adicional necesita para que el análisis pueda concluir. En una auditoría interna, le dice a la organización qué información debe recabarse. En un análisis histórico, declara los límites de lo que el expediente disponible permite afirmar.

Taxonomía General de Aplicaciones

### VII.  La interacción entre evidencia empírica y evidencia ontológica

El documento editorial del libro (Sección III) establece que cada entrada requiere dos columnas de evidencia que operan en niveles distintos y que ninguna puede reemplazar a la otra. La Columna A es la lectura ontológica del SDO: localización del Hijo, distribución P(Hijos), α_clínico. La Columna B es la evidencia del mundo: documentos, peritajes, testimonios, con rangos w asignados según la tabla E0–E8.

### La contradicción entre columnas es un caso especial que merece tratamiento explícito:

Situación Interpretación Acción

Columnas A y B convergen

Robustez. La lectura ontológica y la evidencia empírica apuntan en la misma dirección.

Documentar la convergencia como factor de solidez del análisis. Estrechar rangos.

Columna A contradicha por Columna B

La localización del Hijo o la estimación de α no coincide con la evidencia documental del caso.

No forzar convergencia. Revisar la localización (U·1). Si la localización es confirmable y la contradicción persiste, declarar la incompatibilidad.

Solo Columna B disponible

Análisis parcial. No hay lectura ontológica porque el sujeto no es accesible.

Usar Columna B con nota explícita de que la validación ontológica (Ruta A) no pudo ejecutarse. Mayor rango de incertidumbre.

Solo Columna A disponible

Análisis limitado. Hay lectura ontológica pero la evidencia documental es insuficiente.

Evaluar si la Columna A sola soporta una Declaración C o D. Sin Columna B, los rangos w no tienen sustento empírico.

Taxonomía General de Aplicaciones

La incompatibilidad entre columnas es información diagnóstica valiosa. Si la localización del Hijo (Columna A) sugiere que el actor estaba en Anteros, pero la evidencia documental (Columna B) muestra un patrón de Fobos, hay tres posibilidades: la localización necesita revisión, la evidencia documental está incompleta, o el caso tiene una particularidad que el modelo aún no ha capturado. Las tres posibilidades deben evaluarse antes de forzar la convergencia.

### VIII.  Recapitulación operativa

La jerarquía de evidencia: documento directo > peritaje > testimonios convergentes > correlación > testimonio único > posición estructural > indicio circunstancial > dicho único. Cada dominio la adapta; la jerarquía se preserva.

Regla de intersección: cuando dos rangos son compatibles, el rango resultante es [max (a, c), min (b, d)]. Si la intersección es vacía, hay contradicción genuina.

Regla de prioridad: cuando hay contradicción, el tipo superior prevalece con desplazamiento conservador. El analista nunca fuerza la convergencia.

Contradicción propia como diagnóstico: la inconsistencia sistemática de un actor en su narrativa es señal de IIC personal bajo y orienta P(Hijos) hacia Anteros negativo o Fobos estratégico. Es información sobre v_t, no sobre la arista.

Declaración D: no es fracaso sino orientación. Especifica qué evidencia empírica y qué observación ontológica resolverían la brecha, y si alguna de las dos es accesible en el caso.

La contradicción nunca se oculta: se documenta, se clasifica (leve, moderada, severa), se procesa con las reglas del protocolo, y se refleja en el rango final. Un análisis que oculta contradicción es más vulnerable que uno que la declara.

Taxonomía General de Aplicaciones

— Fin del Capítulo U·2 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

