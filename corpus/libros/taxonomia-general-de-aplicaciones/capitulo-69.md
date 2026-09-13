PARTE XI · Arte, Cultura y Medios

Taxonomía General de Aplicaciones

## Capítulo 69

### Videojuegos y diseño de sistemas adictivos

Organ.  Estru.  Model.  Educa.  Crisi.

Para el mediador que busca precisión · Cómo usar este capítulo

Este capítulo es Nivel C y construye el primer marco de responsabilidad causal en diseño de sistemas adictivos digitales de la Taxonomía. Opera en la intersección del cap. 13 (IA y algoritmos: el diseñador de la métrica de engagement) y el cap. 53 (Telecomunicaciones: el amplificador de contenido). El instrumento central es el INCF_adictivo: no pregunta «¿el usuario se enganchó?» sino «¿sin qué decisión de diseño específica el sistema no habría producido la dependencia a esa escala?». La distinción central: el engagement genuino (el usuario vuelve porque el producto le produce valor real) versus la dependencia inducida (el sistema usa técnicas de refuerzo variable — el mismo mecanismo de las máquinas tragamonedas — para capturar el tiempo del usuario más allá de su decisión autónoma informada).

### §1  La distinción central: engagement legítimo versus dependencia inducida

El diseño de videojuegos opera en la intersección de dos posibilidades que el sistema debe distinguir con precisión. El engagement genuino: el juego produce valor al usuario — aprendizaje, entretenimiento, conexión social, expresión creativa — y el usuario vuelve porque ese valor es real. El sistema de recompensas del juego refleja el progreso real del jugador, y la decisión de seguir jugando es una decisión autónoma informada. La dependencia inducida: el juego usa técnicas de diseño que explotan las vulnerabilidades del sistema dopaminérgico del usuario para capturar su tiempo más allá de lo que su decisión autónoma e

Taxonomía General de Aplicaciones

informada produciría. El usuario no vuelve por el valor que recibe sino porque el sistema diseñó un ciclo de activación-recompensa que hace que parar sea más difícil que continuar.

La distinción no es binaria: todos los diseños de productos exitosos usan alguna mecánica de engagement. El límite normativo es la transparencia y la proporcionalidad: el diseño que informa al usuario de las técnicas que usa y que no produce daño proporcional al valor que ofrece opera dentro del espacio del engagement legítimo. El diseño que oculta deliberadamente las mecánicas adictivas, que las orienta específicamente a las poblaciones más vulnerables (menores, personas con predisposición a la adicción), o que produce un daño sistemático a la salud, la economía o las relaciones del usuario desproporcionado al valor que ofrece opera en el espacio de la dependencia inducida.

INCF_adictivo(nodo_i) = P (dependencia_a_esa_escala | sin la

decisión de diseño del nodo_i) El INCF_adictivo del diseñador de la mecánica de engagement es alto cuando la dependencia fue producida por una decisión de diseño idiosincrática que el estándar ético del desarrollo de juegos del período no justificaba — la implementación deliberada de las mecánicas de refuerzo variable de slot machine en un producto orientado a menores. El INCF_adictivo es bajo cuando el engagement producido era el tipo de engagement propio del entretenimiento digital del período y cualquier diseñador del sector habría producido mecánicas similares.

### §2  Escala Ac0–Ac8 en videojuegos y sistemas adictivos

Tipo de evidencia en videojuegos y

Descripción Rango w (candidato)

Nivel

sistemas adictivos

Ac1 Documentos internos de

[0.70, 0.88]

Los documentos internos del proceso de desarrollo que

Taxonomía General de Aplicaciones

Tipo de evidencia en videojuegos y

Descripción Rango w (candidato)

Nivel

sistemas adictivos

diseño que muestran el conocimiento del diseño adictivo + análisis técnico de las mecánicas implementadas + estudios de impacto en los usuarios documentados por el propio desarrollador

muestran que los diseñadores conocían el efecto adictivo de las mecánicas implementadas y tomaron la decisión deliberada de implementarlas. El análisis técnico de las mecánicas establece cuáles son las técnicas de refuerzo variable implementadas.

Ac2 Análisis técnico de las mecánicas de engagement del juego + estudios independientes del impacto en los usuarios + comparación con los estándares del sector

[0.58, 0.76]

El análisis técnico de las mecánicas implementadas que identifica las técnicas de refuerzo variable, combinado con estudios independientes del impacto en la población de usuarios.

Ac3 Análisis comparado de las mecánicas del juego con los patrones documentados de diseño adictivo + estudios epidemiológicos de la prevalencia del uso problemático

[0.44, 0.60]

La comparación sistemática de las mecánicas del juego con los patrones de diseño adictivo identificados en la literatura de psicología del comportamiento.

Taxonomía General de Aplicaciones

Tipo de evidencia en videojuegos y

Descripción Rango w (candidato)

Nivel

sistemas adictivos

Ac4 Análisis del comportamiento del usuario en el sistema + datos de uso (tiempo de sesión, frecuencia) sin análisis de las mecánicas de diseño

[0.26, 0.44]

Los datos de comportamiento del usuario que documentan el uso problemático sin el análisis de las mecánicas de diseño que lo produjeron.

Ac0 Análisis Ac1/Ac2 que establece que las mecánicas del juego no tienen características de refuerzo variable o que el uso problemático no es causalmente atribuible al diseño

w = 0.00

El análisis técnico que establece que las mecánicas del juego siguen los estándares de diseño ético del período o que la dependencia del usuario tiene causas no atribuibles al diseño del juego.

### §3  Las mecánicas de diseño adictivo y el INCF por tipo

Las mecánicas de diseño adictivo son las técnicas específicas que el sistema usa para producir dependencia más allá del valor genuino del producto. El análisis establece el INCF de cada mecánica — la contribución causal de esa decisión de diseño específica a la dependencia del usuario — y la S del diseñador de la mecánica: ¿otros diseñadores del sector en el mismo período habrían implementado esa mecánica dado el mismo contexto competitivo?

Taxonomía General de Aplicaciones

Mecánica de

Cómo produce

INCF del diseñador S del diseñador

diseño adictivo

dependencia

Refuerzo variable con recompensas aleatorias (loot boxes, gacha)

La recompensa aleatoria produce el mismo patrón de activación dopaminérgica que las máquinas tragamonedas. La impredictibilidad de la recompensa hace que el sistema sea más difícil de abandonar que si la recompensa fuera predecible.

Alto [0.30–0.52] cuando la mecánica fue diseñada deliberadamente para una población de menores o cuando la varianza de la recompensa fue calibrada específicamente para maximizar el tiempo de sesión.

Moderada [0.38– 0.58]: la mecánica de recompensa variable es ampliamente usada en el sector. S baja cuando fue implementada en un producto orientado a menores sin restricciones de edad.

Sistemas de progresión que imponen costos de salida crecientes (time-gating, streaks)

Los sistemas que penalizan al usuario por no jugar (la racha que se pierde, el bonus que expira) convierten la decisión de dejar de jugar en una pérdida percibida, explotando la aversión a la pérdida.

Moderado-alto [0.25–0.45] cuando el sistema de penalización fue diseñado deliberadamente para reducir las tasas de abandono.

Moderado [0.40– 0.62]: los sistemas de racha son el estándar del sector del período. S baja cuando la penalización fue calibrada para producir ansiedad de separación medible.

Dark patterns de monetización (presión social para el gasto, temporizadores de urgencia)

Los elementos de diseño que presionan al usuario para gastar dinero real explotando la presión social (los otros jugadores tienen

Alto [0.32–0.55] cuando los dark patterns fueron diseñados deliberadamente para producir gasto impulsivo no planificado.

Moderado [0.38– 0.60]: los dark patterns de monetización son frecuentes en el sector. S baja cuando fueron orientados específicamente a

Taxonomía General de Aplicaciones

Mecánica de

Cómo produce

INCF del diseñador S del diseñador

diseño adictivo

dependencia

items que tú no), la urgencia temporal (esta oferta expira en 2 horas), y la asimetría de información.

menores o a personas con historial documentado de compras impulsivas.

Normalización del juego de apuestas en menores de edad

La implementación de mecánicas de apuesta (loot boxes con valor de mercado real, torneos con premio económico) en productos accesibles para menores sin las restricciones que las apuestas requieren en los sistemas regulatorios.

Muy alto [0.40– 0.62] cuando la mecánica de apuesta fue implementada conscientemente en un producto clasificado para menores.

Moderado-bajo [0.28–0.45]: la omisión de restricciones de edad en productos con mecánicas de apuesta era idiosincrática de algunos desarrolladores del período.

### §4  El D_vital del tiempo capturado: la medida del daño

El daño del diseño adictivo tiene la misma estructura del D_vital de los demás dominios, con una particularidad que lo distingue: el componente más significativo frecuentemente no es el daño económico (el dinero gastado en microtransacciones) sino el daño al tiempo de vida — las horas y los años de vida invertidos en el juego más allá del tiempo que la decisión autónoma informada del usuario habría producido. Ese exceso de tiempo es el T_capturado: el tiempo que el diseño adictivo extrae del usuario por encima del engagement genuino.

Taxonomía General de Aplicaciones

D_vital_adictivo = T_capturado + D_oportunidad_actividades_desplazadas + D_salud_mental +

D_económico T_capturado: el tiempo de uso que excede el tiempo que el usuario habría elegido dado información completa sobre las mecánicas adictivas del sistema. Se estima desde la diferencia entre el tiempo de uso real del usuario y el tiempo que usuarios equivalentes invierten en productos con el mismo valor genuino, pero sin las mecánicas adictivas. D_oportunidad_actividades_desplazadas: las actividades de alto valor que el tiempo capturado impidió — el estudio, el ejercicio, las relaciones sociales, el trabajo. D_salud_mental: el impacto documentado de las mecánicas adictivas sobre la salud mental del usuario — especialmente en menores. D_económico: el gasto en microtransacciones más allá del presupuesto planificado.

### §5  Caso resuelto — Loot boxes en juegos de menores: el diseñador del sistema como nodo de mayor INCF

Varios países europeos (Bélgica 2018, Países Bajos 2019, múltiples países desde 2022) han regulado las loot boxes en videojuegos como juego de azar debido a su estructura de recompensa aleatoria de valor real. El análisis del INCF en el caso de un juego AAA orientado a menores que implementó loot boxes con contenido de valor de mercado real establece la distribución del R* sobre el daño documentado a los usuarios menores.

Nodo Actor INCF S Análisis

N1 Diseñador del sistema de monetización (tomó la decisión de implementar loot boxes con valor real en un producto clasificado para menores)

~42% 0.28 INCF alto. S moderado-bajo: la implementación de loot boxes con valor de mercado real en un producto clasificado para menores era idiosincrática — otros desarrolladores del período orientados al mismo segmento implementaron mecánicas de monetización sin la misma estructura de apuesta. La decisión de no implementar

Taxonomía General de Aplicaciones

Nodo Actor INCF S Análisis

restricciones de edad específicas para las mecánicas de apuesta era la decisión de diseño de mayor INCF.

N2 Directivos que aprobaron el modelo de monetización con conocimiento de los estudios de psicología del comportamiento disponibles

~28% 0.38 INCF moderado-alto. Los documentos internos de varios desarrolladores del período muestran que los equipos directivos tenían acceso a la literatura de psicología del comportamiento sobre el impacto de las recompensas variables y eligieron implementar el sistema conociendo ese impacto.

N3 Reguladores (no establecieron restricciones específicas para loot boxes con valor real)

~15% 0.68 INCF moderado. S alta: la mayoría de los reguladores del período no habían establecido restricciones específicas para las loot boxes, lo que hace que la omisión del regulador específico sea el estándar del período.

N4 Plataformas de distribución (facilitaron el acceso sin restricciones de edad específicas para las mecánicas de apuesta)

~10% 0.72 INCF moderado-bajo. S alta.

N5 Usuarios menores y sus familias

~5% 0.85 S muy alta. Cualquier menor bajo las mismas condiciones de exposición al sistema habría producido patrones de uso similares dado las mecánicas de refuerzo variable.

Taxonomía General de Aplicaciones

El resultado central: el nodo de mayor INCF no es el menor que compró las loot boxes sino el diseñador del sistema de monetización que eligió implementar la mecánica de apuesta en un producto orientado a menores con conocimiento de su efecto. El IAS_regulatorio post-decisiones (Bélgica, Países Bajos): las regulaciones que requieren la eliminación de las loot boxes con valor real en productos accesibles para menores actúan sobre el nodo de mayor INCF — el diseño del sistema de monetización — y tienen IAS positivo respecto al marco anterior donde los reguladores no actuaban.

### §6  Preguntas y límites del método

Pregunta Instrumento Nivel de certeza

¿El diseño usa mecánicas adictivas — cuál es el INCF del diseñador?

Análisis técnico de las mecánicas del sistema: ¿hay refuerzo variable, dark patterns, penalizaciones de salida? Comparación con los estándares de diseño ético del sector del período.

Declaración A con documentos Ac1 internos. Declaración B con análisis Ac2 de las mecánicas + comparación con el sector.

¿El daño es proporcional al valor genuino — cuál es el T_capturado?

Comparación del tiempo de uso real con el tiempo de uso de productos con valor equivalente pero sin mecánicas adictivas documentadas.

Declaración B con datos de uso Ac2 + análisis comparado con productos de referencia.

¿La población objetivo incluye menores — eleva esto el INCF del diseñador?

Análisis del sistema de clasificación de edad del producto y de las mecánicas específicas para el segmento de menores.

Declaración A con clasificación verificada Ac1. Declaración B con análisis Ac2 del segmento de usuarios.

Límite central: la distinción entre engagement y dependencia es un continuo, no una dicotomía. El sistema establece el límite en la transparencia y la proporcionalidad, pero la operacionalización de esos criterios requiere juicio que el análisis cuantitativo no puede

Taxonomía General de Aplicaciones

sustituir completamente. El análisis identifica las mecánicas, establece el INCF de cada una, y declara el nivel de incertidumbre en la distinción engagement/dependencia — sin pretender resolver la norma que el sistema jurídico debe establecer.

— Fin del Capítulo 69 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

