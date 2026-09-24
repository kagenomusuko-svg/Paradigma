### APÉNDICE B Calibración de los pesos W

### del grafo causal

Guía práctica para asignar valores numéricos a las aristas del

grafo en los 18 dominios del libro

Tabla universal de evidencia · Matrices por dominio ·

Calibración en expediente real · Casos de prueba

Este apéndice cierra la brecha entre la estructura del grafo causal (qué nodos incluir y cómo conectarlos, que los capítulos del libro explican) y el valor numérico de cada arista (qué número asignar a ese peso, que hasta aquí quedaba implícito). A lo largo del libro, cada arista w aparece con un valor específico —w(UCC→resultado) = 0.80, w(ex-gerente→fraude) = 0.00, w(Princip→cascada) = 0.40— sin que en ningún momento se explicara el criterio que produjo ese número en lugar de cualquier otro. Este apéndice hace ese criterio explícito, verificable y replicable.

La calibración de W es un proceso de dos pasos que este apéndice desarrolla en orden: primero la dirección de la arista (qué tipo de relación causal representa), luego su intensidad (qué valor numérico justifica la evidencia disponible). Los dos pasos son independientes: la dirección es una decisión sobre la estructura del grafo; la intensidad es una estimación sobre la fuerza de esa relación causal.

### §1.  Los dos pasos de la calibración: dirección e intensidad

### 1.1 Paso 1: la dirección de la arista

Antes de asignar ningún número, es necesario determinar el tipo de relación causal que la arista representa. El tipo determina el rango de valores posibles y las fuentes de evidencia relevantes. Hay cuatro tipos de arista en el grafo causal:

Tipo Descripción Ejemplo del libro

Rango w habitual

Arista directa

A realizó la acción que produjo directamente el resultado en B.

O-ring → fallo del Challenger. Subordinadas → acceso al expediente.

### 0.65 – 0.95 según evidencia (E1-E2)

Arista estructural

A creó las condiciones bajo las cuales B pudo causar el resultado. A no causó directamente sino que habilitó la causa.

UCC diseñó la tecnología → UCIL operó la planta. Institución diseñó el rol → subordinadas accedieron.

### 0.45 – 0.85 depende del grado de habilitación

Arista de omisión

A tenía la capacidad de impedir el resultado y no lo hizo. La

Regulador no inspeccionó la planta de Bhopal. Gobierno indio

### 0.15 – 0.55 depende del deber y la capacidad

inacción es causalmente relevante.

no inspeccionó condiciones de seguridad.

Arista nula (w = 0)

A no tuvo posición causal en el resultado. La ausencia de arista es una afirmación positiva que requiere evidencia.

Ex-gerente → fraude en el Caso Eje (w = 0 porque la arista no está documentada).

### 0.00 acreditado positivamente

Regla de calibración:  La pregunta de dirección: "Si este nodo no hubiera existido o no hubiera actuado como actuó, ¿habría ocurrido el resultado con la misma probabilidad?" Si la respuesta es sí, la arista es nula. Si es no, la arista existe y su tipo determina el rango de su intensidad.

### 1.2 Paso 2: la intensidad de la arista

La intensidad w ∈ [0, 1] es una función de la fuerza de la evidencia que documenta la relación causal. A mayor calidad y cantidad de evidencia, mayor w. El criterio no es subjetivo: se corresponde con tipos de evidencia que tienen estándares verificables en cada dominio.

### La escala de colores del apéndice usa el mismo código en todas las tablas:

Nivel Descripción general

Rango w

### 0.75 – 0.95 Muy alto Evidencia documental directa o mecanismo técnico peritado. El resultado habría sido muy

significativamente diferente sin este nodo.

### 0.55 – 0.74 Alto Testimonio convergente con corroboración documental, o correlación estadística fuerte controlada.

### 0.35 – 0.54 Moderado Inferencia razonada por posición estructural, o testimonio parcialmente corroborado.

### 0.15 – 0.34 Bajo Correlación sin mecanismo documentado, o testimonio único con contexto consistente.

### 0.05 – 0.14 Muy bajo Dicho único sin corroboración. El resultado puede calcularse pero debe presentarse como rango.

### 0.00 Nulo documentado

Ausencia de arista acreditada positivamente. No es simplemente la ausencia de evidencia: es evidencia de la ausencia.

### §2.  La tabla universal de tipos de evidencia con rangos

Esta tabla es el instrumento central del apéndice. Define los nueve tipos de evidencia que el sistema reconoce, el rango de w que justifica cada uno, y el criterio concreto de uso. Los ejemplos son todos del libro.

Certeza Criterio de uso y ejemplos del libro

Tipo de evidencia

Rango w

0.75– 0.95 Alta Contrato que diseñó el estándar defectuoso. Correo que instruyó la acción. Registro digital de acceso. Acta de resolución de un consejo. Código de software auditado. Casos: UCC/UCIL (contratos de seguridad), Caso Eje (registro digital de las subordinadas).

E1 — Documento directo que muestra la acción del nodo sobre el resultado

0.70– 0.90 Alta Informe pericial que establece la cadena fallo → daño. Autopsia. Análisis de fallo de ingeniería. Estudio epidemiológico con modelo causal. Casos: O-ring del Challenger (NASA), dispersión del MIC en Bhopal.

E2 — Mecanismo causal físico o técnico documentado pericialmente

0.55– 0.75 Media-alta Varios testigos independientes coinciden y hay al menos un documento corroborante, aunque

E3 — Testimonio múltiple convergente con respaldo

documental parcial

no capture la acción directa. Casos: directivos de Morton Thiokol que recuerdan la misma reunión con el mismo contenido.

0.50– 0.70 Media R² > 0.60 en regresión controlada por las covariables principales. Casos: Informe Coleman (R*_entorno_familiar ≈ 52% a partir de regresión múltiple), Redlining (correlación entre mapas HOLC y tasas de denegación).

E4 — Correlación estadística controlada (estudios longitudinales, regresión)

E5 — Testimonio único con respaldo documental parcial

0.35– 0.55 Media-baja

Un solo testigo que describe la acción del nodo, con al menos un documento que es consistente, aunque no la pruebe directamente. Casos: testimonios internos sobre la cultura de VW antes del Dieselgate.

E6 — Inferencia razonada por posición estructural del nodo

0.25– 0.45 Baja-media

El nodo tenía la posición, los recursos y los incentivos para la acción imputada, aunque no haya documentación directa. La acción es la más plausible dado el diseño del sistema. Casos: gobierno indio en Bhopal (incentivos a bajar costos sin documentación de instrucción directa).

0.10– 0.30 Baja Proximidad temporal o espacial entre la acción del nodo y el resultado, sin evidencia del mecanismo de transmisión. Casos: hecho 2 del Caso Eje (acceso al expediente + fraude dos días después, sin arista documentada). USAR CON NOTACIÓN EXPLÍCITA.

E7 — Correlación temporal o espacial sin mecanismo documentado

0.05– 0.15 Muy baja Un solo testimonio sin ningún corroborante documental, físico ni estadístico. Casos: hecho 1 del Caso Eje (dicho de las subordinadas de que el gerente instruyó, sin respaldo). El sistema puede calcular R* con este peso pero el resultado debe presentarse como rango, no como valor puntual.

E8 — Dicho único sin respaldo de ningún tipo

0.00 Acreditada Se acredita positivamente que el nodo NO fue condición del resultado. El tipo de arista que el Caso Eje usa para la arista ex-gerente → fraude. Requiere evidencia de la ausencia: registros que muestren que la información no salió del sistema, que el nodo no tenía acceso, etc.

E0 — Arista nula documentada (w = 0 explícito)

⚠ La asignación de w NO es un proceso subjetivo libre. Es una estimación fundamentada en el tipo de evidencia disponible, con el rango que ese tipo de evidencia justifica. Si el analista no puede identificar el tipo de evidencia que sustenta cada arista de su grafo, esa arista no debería estar en el grafo.

Cuando hay múltiples fuentes de distintos tipos:  Si para una misma arista hay tanto evidencia de tipo E1 (documento) como E3 (testimonio convergente), el w se asigna al tipo de mayor calidad (E1 en este caso). Si hay evidencia de tipos distintos que apuntan en direcciones opuestas (una fuente dice w alto, otra dice w bajo), se aplica el procedimiento del §4 de contradicción de fuentes.

### §3.  Las matrices de calibración por dominio

Cada dominio del libro tiene una combinación característica de tipos de evidencia disponibles, nodos típicos del grafo, y rangos ajustados por las convenciones probatorias o metodológicas del campo. Esta sección compila esa información dominio por dominio.

Para cada dominio se presenta: (a) los nodos típicos del grafo, (b) el tipo de evidencia dominante, (c) los rangos específicos de cada arista, y (d) los valores usados en los casos del libro como referencia verificable.

### 3.1 Derecho penal y civil (Capítulo 1)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.75– 0.92 E1/E2 Requiere nexo causal documentado entre el acto del autor y el daño. La autoría material es el tipo de arista de mayor w del sistema penal.

Autor material → resultado dañino

0.60– 0.85 E1/E3 Comunicación de la instrucción (correo, grabación) → E1. Testimonio convergente de los receptores → E3.

Autor intelectual → autor material

0.50– 0.78 E2/E4 La arista estructural más importante del Cap.1. Ejemplo: el empleador que diseñó condiciones inseguras.

Diseñador del sistema → autor material

0.35– 0.65 E3/E5 Grado de participación documentado. La complicidad requiere evidencia del conocimiento previo del resultado probable.

Cómplice → resultado

0.25– 0.55 E5/E6 Más difícil de documentar. Requiere evidencia de la acción de ocultación, no solo de su resultado.

Encubridor → ocultación del daño

0.05– 0.20 E8 CASO EJE hecho 1. Usar siempre con notación explícita: "w asignado con evidencia E8 sujeta a verificación adicional".

Dicho único sin respaldo → conducta

### 0.00 E0 w = 0 documentado. No existe ninguna evidencia del mecanismo de transmisión. Declaración explícita en el expediente.

Arista ex-gerente → fraude (Caso Eje)

### 3.2 PLD y compliance (Capítulo 2)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.80– 0.95 E1 El registro transaccional es evidencia directa. La arista más sólida del dominio.

Operación inusual → registro REINTE

0.55– 0.80 E2/E3 Requiere acreditar el conocimiento del destino probable de los fondos o activos.

APNFD → lavado consumado

0.40– 0.65 E4/E6 La ausencia de controles se documenta con la brecha entre el programa de compliance declarado y el implementado.

Institución sin controles → operación indebida

0.30– 0.60 E4/E6 Difícil de documentar cuando el beneficiario está detrás de capas corporativas. Se acredita por inferencia estructural.

Beneficiario final → estructura

### 3.3 Derecho internacional y análisis histórico (Capítulos 3 y 16)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.55– 0.80 E1/E4 El documento existe (E1), pero el mecanismo causal entre el acto y la consecuencia histórica requiere evidencia estadística o comparativa (E4).

Tratado/acto legislativo → consecuencia histórica

0.35– 0.65 E4/E6 Análisis comparativo de casos análogos. Sistema de alianzas → WWI: w = 0.42 por comparación con crisis de 1905, 1908, 1911.

Estructura sistémica → evento histórico

0.05– 0.25 E6/E7 S histórica alta. El detonador tiene w bajo precisamente porque la S del sistema es alta. Princip → WWI: w = 0.15.

Detonador individual → cascada

0.20– 0.55 E1/E6 La continuidad jurídica del Estado es E1 (documentable). La proporción del daño heredado requiere análisis estructural (E6).

Estado sucesor → deuda histórica

### 3.4 Epidemiología y salud pública (Capítulo 6)

Arista típica Rango w

Tipo de evidencia

Nota de calibración

0.65– 0.90 E2/E4 Modelo de transmisión calibrado con datos de contacto. El número reproductivo R₀ informa directamente el w.

Vector → infección en red de contactos

0.55– 0.85 E2/E4 Contacto documentado + confirmación de cepa idéntica. El 20% de los individuos produce el 80% de las transmisiones en muchas enfermedades.

Superpropagador → brote

0.40– 0.65 E4/E6 Estudio comparativo de mortalidad entre poblaciones con y sin la política. Diferencia normalizada por covariables.

Política sanitaria deficiente → exceso de mortalidad

0.35– 0.60 E4 Regresión controlada por factores confusos conocidos. La causalidad ambiental requiere dosimetría cuando es posible.

Factor ambiental → incidencia

### 3.5 Ingeniería de sistemas y análisis de fallos (Capítulo 12)

Arista típica Rango w

Tipo de evidencia

Nota de calibración

0.80– 0.95 E1/E2 Informe pericial de ingeniería. El fallo del O-ring del Challenger: w = 0.88 (fallo documentado pericialmente con el análisis de Morton Thiokol).

Componente físico → fallo técnico documentado

0.65– 0.88 E1/E3 El memorándum de Boisjoly es E1. La decisión de lanzar contra el consejo técnico está documentada en las actas.

Decisión directiva → ignorar advertencia técnica

0.55– 0.78 E3/E6 Más difícil de documentar. Requiere testimonios sobre el ambiente de la reunión + la

Presión comercial/institucional → decisión de lanzar

estructura de incentivos de los directivos.

0.60– 0.85 E1/E2 El diseño es un documento (E1). La causalidad entre diseño y fallo requiere análisis de ingeniería (E2).

Diseño original defectuoso → fallo sistémico

0.35– 0.60 E1/E6 Los documentos de aprobación son E1. Pero la arista entre aprobación y fallo requiere demostrar que el regulador tuvo acceso a la información técnica relevante.

Regulador → aprobación del sistema defectuoso

### 3.6 Inteligencia artificial y algoritmos (Capítulo 13)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.60– 0.88 E1/E4 El documento de especificación de la métrica es E1. La conexión entre esa métrica y el DI observado se demuestra con el análisis de sensibilidad del §6.2 del Cap. 13.

Diseñador de la métrica → disparate impact

0.50– 0.75 E4 Comparación del DI con dataset original vs. dataset debiased. La diferencia de DI es el w de la arista dataset.

Dataset histórico sesgado → resultado del modelo

0.05– 0.15 E4 S del modelo ≈ 1.0. El w de la arista modelo es bajo precisamente porque cualquier modelo competente habría aprendido el mismo patrón. COMPAS: w(modelo→sesgo) = 0.08.

Modelo (algoritmo) → resultado sesgado

0.25– 0.55 E1/E6 La decisión de desplegar es documentable (E1). El grado de conocimiento previo del sesgo (α del desplegador) modifica el w.

Desplegador → daño de las decisiones

### 3.7 Medio ambiente y ecología (Capítulo 14)

Arista típica Rango w

Tipo de evidenci a

Nota de calibración

0.70– 0.92 E1/E2 Registros de producción + análisis ambiental pericial. La cantidad de contaminante emitida es en principio medible.

Operador directo → emisión documentada

0.45– 0.78 E1/E6 Los documentos de aprobación

Casa matriz → estándares deficientes → daño

de estándares son E1 (arista casa matriz → estándares). La arista estándares → daño es E2 pericial.

E2/E4 USAR SHAPLEY. La función v(S) se estima con datos periciales de superposición de contaminació n. Chevron-Ecuador: φ_Texaco = 0.237 × D_total.

Causalidad acumulativa (múltiples actores)

Shaple

### y

0.05– 0.25 E2 S muy alta. El factor es exógeno y no controlable. Se incluye en el grafo para completitud pero no produce AD.

Factor meteorológico/geográfic o → amplificación

### 3.8 Gobierno corporativo y ego colectivo (Capítulo 11)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.72– 0.92 E1/E3 Actas del consejo (E1). Correos internos

CEO/directivo → decisión con

impacto documentado

(E1). En ausencia: testimonios convergentes de participantes en la reunión (E3).

0.50– 0.78 E1/E4 Los documentos de compensación son E1. La arista cultura → daño requiere análisis longitudinal de comportamiento (E4).

Diseño del sistema de incentivos → cultura → daño

0.25– 0.55 E1/E6 Lo que el consejo NO hizo es más difícil de documentar. Se calibra por el deber fiduciario documentado y la evidencia de que la información estaba disponible.

Consejo de administración → omisión de supervisión

0.40– 0.70 E4 El IIC se calcula con datos públicos. La arista IIC → colapso es estadística, calibrada con el predictor logístico del Cap. 11.

IIC bajo → probabilidad de colapso

### 3.9 Quiebra y riesgo sistémico (Capítulo 9)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.65– 0.88 E1/E4 Estados financieros auditados (E1). La relación ICRS→P(quiebra) es el modelo predictor calibrado del Cap. 9.

Concentración de riesgo (ICRS) → probabilidad de quiebra

0.55– 0.80 E1/E4 Contratos documentados (E1).

Proveedor único/cliente

concentrado → fragilidad

El análisis de sensibilidad de los flujos (E4) mide la arista.

0.50– 0.75 E4 El w del contagio sistémico se estima con modelos de correlación de activos y análisis de red del sistema financiero.

Fallo de una institución sistémica → contagio

### 3.10 Score crediticio y discriminación sistémica (Capítulo 8)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.70– 0.90 E1/E4 Los documentos de política de HOLC/FHA son E1. La correlación entre mapas y datos de denegación es E4. Redlining: w = 0.82.

Política institucional discriminatoria → dataset sesgado

0.60– 0.82 E4 DI antes vs. después del control por el dataset. La arista se mide con la diferencia de DI entre modelo con dataset original y con dataset debiased.

Dataset sesgado → score discriminatorio

0.40– 0.65 E3/E6 La evidencia de que el directivo conocía el sesgo es clave. Con conocimiento confirmado: E3/E1 → rango superior. Sin él: E6 → rango inferior.

Directivo que perpetuó el sesgo → daño continuado

### 3.11 Seguros y actuaría (Capítulo 10)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.65– 0.88 E1/E2 La arista estructural más importante del dominio. Los estándares documentados del lugar de trabajo son E1. El nexo con el siniestro es E2 pericial.

Empleador → condición de riesgo → siniestro

0.55– 0.78 E1 El contrato es un documento (E1). El análisis actuarial del sesgo entre riesgo real y cobertura provista es E4.

Diseño del contrato → exclusión injustificada del riesgo

0.15– 0.45 E2/E4 La contribución causal del asegurado al siniestro es la PAC (Prima Actuarial Justa). S alta del asegurado → w bajo.

Asegurado → riesgo propio (contribución causal)

### 3.12 Educación y evaluación docente (Capítulo 15)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.65– 0.85 E4 Datos longitudinales controlados por covariables. El Informe Coleman produce w =

Entorno familiar → resultado educativo

### 0.72 con R² > 0.65 en regresión múltiple.

0.20– 0.40 E4 Valor agregado docente calibrado por entorno. El rango es intencionalmente modesto: refleja que R*_docente ≈ 10-15% según la evidencia acumulada desde Coleman.

Docente → resultado educativo (efecto VAM)

0.15– 0.35 E4 El efecto de la escuela como institución (sin el docente individual) es pequeño según la evidencia. La excepción: liderazgo directivo de alta calidad puede alcanzar w = 0.45.

Escuela como institución → resultado

0.10– 0.30 E4/E6 Efecto difuso y de largo plazo. Se estima con estudios de reforma educativa natural (variaciones exógenas en la política).

Política educativa → estructura del sistema → resultado

### 3.13 Deportes y valor de contribución (Capítulo 17)

Arista típica Rango w

Nota de calibración

Tipo de evidencia

0.35– 0.65 E4 El rango moderado refleja que, en equipos de calidad, la S del jugador estrella es moderada (Brasil ganó sin Pelé en 1962). El w se calibra con la diferencia de P(victoria)

Jugador estrella → resultado (R*_B)

en períodos de ausencia documentada.

0.30– 0.55 E4 Análisis de rendimiento bajo distintas formaciones. El efecto del sistema es real pero requiere varios partidos para estimarse con precisión.

Sistema táctico → resultado del equipo

0.25– 0.50 E4 Comparación de rendimiento antes/después del cambio de entrenador con calidad del rival controlada.

Entrenador → resultado del equipo

0.10– 0.25 Residual El residual no explicado por los otros nodos. En fútbol es mayor que en baloncesto o béisbol por la menor densidad de scoring.

Factor azar (fútbol)

### 3.14 Literatura y análisis narrativo (Capítulo 18)

Tipo de evidencia Nota de calibración

Arista típica

Rango w

0.55– 0.85 Textual El análisis textual de la causalidad narrativa es el equivalente literario de la evidencia documental. La pregunta: "¿Sin este personaje/decisión, el evento habría ocurrido en el mundo del relato?"

Nodo narrativo de diseño → evento central

Tywin → Boda Roja: w = 0.78.

0.30– 0.55 Textual Walder Frey → Boda Roja: w = 0.55. La ejecución es visible pero la S del ejecutor es moderada: otro señor con los mismos agravios habría podido actuar igual bajo las mismas condiciones.

Personaje ejecutor (visible) → evento

N/A Análisis de hijos Los hijos no son aristas del grafo: son el análisis de la disposición de voluntad del personaje en cada nodo de decisión. Se aplica el módulo 4 del Apéndice B.

Hijos del personaje → decisión en el relato

0.60– 0.90 Textual/intertextual El w del autor como nodo de segundo nivel refleja qué tan idiosincrático era el diseño: Dostoievski diseñó el arco Anteros→Harmonía con S baja (pocos autores habrían construido ese arco específico con esa precisión).

Autor como meta-nodo → diseño del arco

### §4.  Calibración cuando hay contradicción entre fuentes

La situación más frecuente en los casos reales no es la ausencia de evidencia sino la contradicción entre fuentes: un documento apunta a w alto y un testimonio apunta a w bajo, o dos estudios estadísticos producen estimaciones distintas. El sistema tiene un procedimiento estándar para ese caso.

### 4.1 El principio de la evidencia de mayor calidad

Cuando hay contradicción entre fuentes de distinto tipo, el w se asigna según la fuente de mayor tipo (menor número en la escala E0-E8), no según el promedio. La razón es que las evidencias de menor calidad son fuentes de ruido, no de información adicional que promedia con la de mayor calidad.

Situación Procedimiento Ejemplo del libro

E1 contradice E3 (documento vs. testimonio)

Usar E1. Documentar la contradicción y su resolución.

Caso Eje: el registro digital (E1) muestra que las subordinadas accedieron al expediente. El dicho de que el gerente instruyó (E8) no contradice E1 sino que lo complementa con una afirmación adicional no acreditada.

E4 contradice E4 (dos

Usar el estudio de mayor calidad metodológica. Si

Informe Coleman: varias réplicas producen R*_entorno entre 40% y

estudios estadísticos)

son comparables, presentar el rango.

55%. El análisis usa el rango con el valor central de 52% del estudio original.

E3 contradice E3 (testimonios convergentes que se contradicen)

Reducir el w al rango E5-E6 y documentar la inconsistencia.

Testigos de la reunión de Morton Thiokol que recuerdan el contenido de manera distinta. El w de esa arista cae al rango E5 y se presenta como rango, no como valor puntual.

Caso Eje hecho 2: el registro digital muestra que la información no salió del sistema (E1 → w = 0). La proximidad temporal de dos días (E7) no revierte la arista nula.

E1 apunta a w = 0 pero E6 apunta a w positivo

Documentar la arista nula explícitamente y señalar que E6 es insuficiente para revertirla.

### 4.2 El procedimiento de rango cuando la contradicción no se puede resolver

Cuando la contradicción entre fuentes es genuina y no resoluble con el principio de la evidencia de mayor calidad, el sistema usa el procedimiento de rango: en lugar de asignar un valor puntual w, se asigna un intervalo [w_min, w_max] y se calcula R* para ambos extremos del intervalo.

### R*_rango = [R*(W con w_min), R*(W con w_max)]

Si los dos extremos producen el mismo nodo de mayor R*, el resultado es robusto a la contradicción. Si producen nodos distintos, la contradicción es sustantiva y debe documentarse explícitamente: el análisis produce dos distribuciones de responsabilidad que corresponden a las dos interpretaciones de la evidencia.

Regla de calibración:  Un análisis que asigna valores puntuales cuando la evidencia es contradictoria es menos honesto que uno que asigna rangos. El rango no es una señal de debilidad metodológica: es la representación correcta de la incertidumbre real del análisis.

### §5.  La W = 0 explícita: cuándo se justifica y cómo se documenta

La arista nula w = 0 es la declaración más poderosa del grafo causal: afirma que un nodo no tiene posición causal en el resultado. En el Caso Eje, la arista w (ex-gerente → fraude) = 0 es la declaración que hace que el tipo penal no se configure. Por eso requiere el estándar de documentación más alto del apéndice.

### 5.1 La diferencia entre ausencia de evidencia y evidencia de ausencia

La arista nula no es simplemente la ausencia de evidencia de que el nodo causó el resultado. Es evidencia positiva de que no lo causó. Esa distinción es fundamental para el análisis en expedientes reales:

Situación Interpretación correcta

w correcto

No hay evidencia de que el nodo causó el resultado

Incertidumbre. El w no puede determinarse con la evidencia disponible.

Rango bajo: E6-E7, con w ∈ [0.05–0.25]. NO w = 0.

Hay evidencia de que el nodo actuó pero no de que esa acción causó el resultado

La arista existe pero su intensidad es baja.

E7: w ∈ [0.10– 0.30]. Solo se usa w = 0 si hay evidencia del mecanismo alternativo.

E0: w = 0. Requiere documentar la evidencia de la ausencia, no solo la ausencia de evidencia.

Hay evidencia de que la acción del nodo no pudo haber causado el resultado (alternativa documentada)

Arista nula documentada. w = 0 explícito.

### 5.2 Los cuatro tipos de evidencia que justifican w = 0

1. Evidencia de la imposibilidad técnica: el nodo no tenía acceso técnico al mecanismo de transmisión. En el Caso Eje: si el registro digital muestra que el ex-gerente no accedió al expediente (a diferencia del registro que muestra que las subordinadas sí lo hicieron), esa arista tiene w = 0 por imposibilidad técnica. 2. Evidencia del mecanismo alternativo: existe un mecanismo alternativo que explica completamente el resultado sin necesidad del nodo. En el hecho 2 del Caso Eje: si el tercero que intentó el fraude tenía una fuente alternativa de la información (robo de cartera, darkweb, filtración de otra sucursal), el mecanismo alternativo elimina la necesidad de la arista gerente → fraude. 3. Evidencia de la separación temporal o espacial que excluye el mecanismo: la distancia entre el acto del nodo y el resultado es tan grande que ningún mecanismo causal plausible puede conectarlos. Requiere análisis del mecanismo específico para cada caso. 4. Evidencia directa de la no-acción: un registro que documenta positivamente que el nodo no realizó la acción que se le imputa. El más sólido y el más frecuentemente ausente en los expedientes reales.

⚠ La asignación de w = 0 sin documentación explícita es el error más grave de calibración del grafo causal. Si el análisis usa w = 0 para exonerar a un nodo, esa declaración debe estar tan documentada como cualquier otra arista del grafo. Un w = 0 sin fundamento es tan injustificado como un w = 0.90 sin evidencia.

### §6.  Cómo documentar la calibración en un expediente real

Este es el apartado más práctico del apéndice. Responde a la pregunta: "Apliqué el sistema a mi caso, asigné los pesos W, obtuve los R* y Δ. Ahora tengo que presentar ese análisis ante un juez / árbitro / consejo de administración / regulador. ¿Cómo lo documento para que sea verificable y defendible?"

### 6.1 El estándar de documentación por nivel de foro

Foro Estándar de presentación

Qué debe documentar el analista

Proceso penal Estándar probatorio de "más allá de duda razonable" para la arista directa. El análisis causal apoya pero no sustituye la prueba del tipo penal.

(1) Cada arista con su tipo de evidencia E1-E8 identificado. (2) El w asignado y el rango del tipo de evidencia. (3) La fuente documental específica que justifica cada arista. (4) Las aristas nulas con su fundamento explícito.

Litigio civil / arbitraje

Estándar de "balance de probabilidades". El análisis causal puede ser presentado como peritaje experto.

(1) -(4) del proceso penal. Adicionalmente: (5) Análisis de sensibilidad que muestre que el resultado es robusto a variaciones razonables del w. (6) Comparación con valores análogos usados

en el libro para casos similares.

Regulatorio / administrativo

El estándar varía por regulador. En general: preponderancia de evidencia + razonabilidad del método.

(1) -(6) anteriores. Adicionalmente: (7) Descripción del método de cálculo de R* suficiente para que el regulador lo replique independientemente.

Versión simplificada: (1) Grafo con los pesos visibles. (2) Tabla de R* y Δ. (3) Fuentes de cada peso en lenguaje ejecutivo (no técnico). El código Python del Apéndice B como respaldo.

Consejo de administración / directorio

Estándar de razonabilidad empresarial. El análisis debe ser comprensible para directores no técnicos.

### 6.2 La hoja de calibración: el documento de trabajo que justifica la W

### Para cada expediente, el analista debe producir una "hoja de calibración" que documente cada arista del grafo. Este es el formato estándar:

Arista Nodo origen → destino

w asigna do

Tip o E

Fuente documen tal / evidenci a

Observaci ones y limitacion es

### 0.80 E1 Diseño del sistema de acceso document ado en el

Ej. Caso Eje

Institució n → Subordin adas

El w refleja la arista estructural: la institución habilitó el

manual del usuario (ref. Anexo 3). Contrato laboral de las subordina das (ref. Anexo 1).

acceso, no lo ejecutó directament e. Si fuera E1 directo: w = 0.88.

0.00 E0 Registro de salida de informaci ón: ningún registro muestra transmisi ón al exterior (ref. Pericial informáti ca, Anexo 7). Fraude en estado diferente sin rastro de conexión.

Ej. Caso Eje

Ex-gerente → Fraude (hecho 2)

Arista nula documenta da. La proximidad temporal de 2 días (E7) es insuficiente para revertir la evidencia técnica. Ver §5 de este apéndice.

... ... ... ... ...

Compl etar por caso

Para el expediente:  La hoja de calibración debe acompañar como anexo técnico al análisis de R*. Sin ella, el resultado numérico es un número sin fundamento. Con ella, cada w es una afirmación verificable que el adversario puede impugnar con evidencia contraria — que es exactamente el tipo de debate

que el sistema busca producir: uno sobre los hechos, no sobre la metodología.

### 6.3 Cómo responder la impugnación del w

### En cualquier foro adversarial, la contraparte intentará impugnar los valores w del grafo. Hay tres tipos de impugnación y una respuesta estándar para cada uno:

Respuesta estándar

Tipo de impugnación

Argumento típico de la contraparte

Impugnación del tipo de evidencia

"El peso E3 que usó es especulativo; debería ser E7."

Mostrar el criterio de clasificación del §2 de este apéndice. Señalar que el w asignado es el rango inferior del tipo E3 (0.55), no el superior. Ofrecer hacer el análisis con E7 y mostrar que el resultado cualitativo es el mismo (análisis de sensibilidad).

Impugnación del valor puntual

"El w = 0.80 es arbitrario; debería ser 0.55."

Presentar el análisis de sensibilidad: calcular R* con w = 0.55 y con w = 0.80 y mostrar la diferencia. Si el nodo de mayor R* es el mismo en ambos casos, el argumento de la contraparte no cambia la conclusión. Si produce nodos distintos, documentar el rango.

Impugnación de la arista nula

"La ausencia de evidencia no prueba que la arista sea cero."

La respuesta correcta: una arista nula requiere evidencia de la ausencia, no solo ausencia de evidencia (§5.1). Si la documentación incluye evidencia positiva de la imposibilidad técnica o del

mecanismo alternativo, la impugnación no tiene base. Si no la incluye, el w debe subirse a E7 y documentarse la incertidumbre.

El sistema es transparente: el Apéndice A demuestra la convergencia. El Apéndice B contiene el código ejecutable. Ofrecer al foro ejecutar el código con los datos del expediente para replicar el resultado. La replicabilidad es la mejor defensa del método.

Impugnación del método

"El eigenvector dominante no es el único método para calcular R*."

### §7.  Casos de prueba con solución

Esta sección permite al lector verificar su comprensión del sistema de calibración. Para cada caso se presenta un grafo con los nodos y la descripción de la evidencia disponible, pero sin los valores w. El lector asigna sus propios valores y luego compara con la calibración del libro.

### Caso de prueba 1 — Accidente laboral

Descripción:

Un trabajador de una empresa de manufactura sufre una lesión grave al operar una máquina. Los hechos documentados son: (a) el manual de operación de la máquina indica que debe usarse con protección específica; (b) el supervisor del turno no verificó que el trabajador usara la protección al inicio del turno, lo cual está documentado en el registro de seguridad firmado por el supervisor; (c) el trabajador declaró que nunca recibió capacitación formal sobre el uso de la protección; (d) el área de RRHH tiene un registro de que el trabajador completó el módulo de seguridad en plataforma digital, pero el trabajador argumenta que lo completó sin haber operado nunca la máquina real.

Nodos del grafo:

• N1 — Empresa (diseño del programa de capacitación) • N2 — Supervisor del turno (verificación de seguridad) • N3 — Trabajador (uso de la máquina) • Nf — Lesión

### Asigne w para las aristas: N1→Nf, N2→Nf, N3→Nf

### Solución calibrada (valores del sistema):

Arista w calibrado

Fundamento

Tipo E

0.72 E1/E6 E1: el manual existe y requiere protección. E6: la evidencia de que la capacitación real era insuficiente (módulo digital vs. práctica real) es una inferencia estructural. w = 0.72 = extremo superior de la arista estructural bien documentada.

N1 → Nf (empresa → lesión)

0.65 E1 E1 directo: el registro firmado por el supervisor documenta que no verificó la protección. Esta es la arista más sólida del grafo porque la omisión está documentada en un registro institucional.

N2 → Nf (supervisor → lesión)

0.35 E5/E6 S alta: cualquier trabajador sin capacitación práctica habría actuado igual. La contribución del trabajador existe pero es la de menor R* neto porque la S es alta y la capacitación era responsabilidad de N1.

N3 → Nf (trabajador → lesión)

### R*_N1 ≈ 42% · R*_N2 ≈ 35% · R*_N3 ≈ 23%

### El resultado más importante: el nodo de mayor R* es la empresa (diseño del programa de capacitación), no el supervisor ni el trabajador. Eso no exonera al supervisor (Δ

positivo si su α es bajo) pero distribuye la responsabilidad de manera proporcional a la posición causal real.

### Caso de prueba 2 — Decisión financiera con información asimétrica

Descripción:

Un cliente de un banco contrata un producto de inversión estructurado que resulta en pérdida del 60% del capital. Los hechos documentados son: (a) el contrato incluye una cláusula de riesgo en letra pequeña en la página 14 de 18; (b) el asesor financiero firmó un formulario de idoneidad en el que marcó que el cliente tenía "perfil de riesgo moderado" aunque el cliente era jubilado con ingresos fijos; (c) el asesor tenía un esquema de comisión que era el doble para este producto que para los alternativos equivalentes; (d) el cliente no leyó el contrato completo.

Nodos: N1 = banco (diseño del producto), N2 = asesor (venta), N3 = esquema de incentivos, N4 = cliente

Solución calibrada:

Arista w calibrado

Fundamento

Tipo E

### 0.68 E1/E6 El diseño del producto con riesgo no divulgado adecuadamente (cláusula en pág. 14 de 18) es E1 parcial. La causalidad entre

N1 → Pérdida del cliente

ese diseño y la pérdida requiere E6.

0.75 E1 El esquema de comisiones es un documento E1. La arista es alta porque el incentivo doble es una condición estructural que determina el comportamiento del asesor con alta S.

N3 (incentivos) → N2 (comportamiento asesor)

### 0.60 E1 El formulario de idoneidad mal completado es E1 directo. El w es alto pero la S también es moderada (otro asesor bajo el mismo esquema habría actuado igual).

N2 → Venta inadecuada

0.18 E6 El cliente no leyó el contrato. Pero la S es altísima: la asimetría de información era tan marcada que cualquier cliente razonable habría tomado la misma decisión.

N4 (cliente) → pérdida propia

### R*_N1 ≈ 38% · R*_N3+N2 ≈ 45% · R*_N4 ≈ 17%
