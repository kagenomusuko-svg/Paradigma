## PARTE XI · Arte, Cultura y Medios

Taxonomía General de Aplicaciones

### Capítulo 69
Videojuegos y diseño de sistemas adictivos
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Nivel C y construye el primer marco de responsabilidad causal
en diseño de sistemas adictivos digitales de la Taxonomía. Opera en la
intersección del cap. 13 (IA y algoritmos: el diseñador de la métrica de
engagement) y el cap. 53 (Telecomunicaciones: el amplificador de contenido). El
instrumento central es el INCF_adictivo: no pregunta «¿el usuario se enganchó?»
sino «¿sin qué decisión de diseño específica el sistema no habría producido la
dependencia a esa escala?». La distinción central: el engagement genuino (el
usuario vuelve porque el producto le produce valor real) versus la dependencia
inducida (el sistema usa técnicas de refuerzo variable — el mismo mecanismo de
las máquinas tragamonedas — para capturar el tiempo del usuario más allá de
su decisión autónoma informada).
§1 La distinción central: engagement legítimo
versus dependencia inducida
El diseño de videojuegos opera en la intersección de dos
posibilidades que el sistema debe distinguir con precisión. El
engagement genuino: el juego produce valor al usuario —
aprendizaje, entretenimiento, conexión social, expresión creativa —
y el usuario vuelve porque ese valor es real. El sistema de
recompensas del juego refleja el progreso real del jugador, y la
decisión de seguir jugando es una decisión autónoma informada. La
dependencia inducida: el juego usa técnicas de diseño que explotan
las vulnerabilidades del sistema dopaminérgico del usuario para
capturar su tiempo más allá de lo que su decisión autónoma e

Taxonomía General de Aplicaciones
informada produciría. El usuario no vuelve por el valor que recibe
sino porque el sistema diseñó un ciclo de activación-recompensa que
hace que parar sea más difícil que continuar.
La distinción no es binaria: todos los diseños de productos exitosos
usan alguna mecánica de engagement. El límite normativo es la
transparencia y la proporcionalidad: el diseño que informa al usuario
de las técnicas que usa y que no produce daño proporcional al valor
que ofrece opera dentro del espacio del engagement legítimo. El
diseño que oculta deliberadamente las mecánicas adictivas, que las
orienta específicamente a las poblaciones más vulnerables (menores,
personas con predisposición a la adicción), o que produce un daño
sistemático a la salud, la economía o las relaciones del usuario
desproporcionado al valor que ofrece opera en el espacio de la
dependencia inducida.
INCF_adictivo(nodo_i) = P (dependencia_a_esa_escala | sin la
decisión de diseño del nodo_i)
El INCF_adictivo del diseñador de la mecánica de engagement es alto cuando la
dependencia fue producida por una decisión de diseño idiosincrática que el estándar
ético del desarrollo de juegos del período no justificaba — la implementación deliberada
de las mecánicas de refuerzo variable de slot machine en un producto orientado a
menores. El INCF_adictivo es bajo cuando el engagement producido era el tipo de
engagement propio del entretenimiento digital del período y cualquier diseñador del
sector habría producido mecánicas similares.
§2 Escala Ac0–Ac8 en videojuegos y sistemas
adictivos
Tipo de
evidencia en
Rango w
Nivel videojuegos y Descripción
(candidato)
sistemas
adictivos
Ac1 Documentos Los documentos internos del [0.70, 0.88]
internos de proceso de desarrollo que

Taxonomía General de Aplicaciones
Tipo de
evidencia en
Rango w
Nivel videojuegos y Descripción
(candidato)
sistemas
adictivos
diseño que muestran que los diseñadores
muestran el conocían el efecto adictivo de las
conocimiento mecánicas implementadas y
del diseño tomaron la decisión deliberada de
adictivo + implementarlas. El análisis
análisis técnico técnico de las mecánicas establece
de las mecánicas cuáles son las técnicas de refuerzo
implementadas variable implementadas.
+ estudios de
impacto en los
usuarios
documentados
por el propio
desarrollador
Ac2 Análisis técnico El análisis técnico de las [0.58, 0.76]
de las mecánicas mecánicas implementadas que
de engagement identifica las técnicas de refuerzo
del juego + variable, combinado con estudios
estudios independientes del impacto en la
independientes población de usuarios.
del impacto en
los usuarios +
comparación
con los
estándares del
sector
Ac3 Análisis La comparación sistemática de las [0.44, 0.60]
comparado de mecánicas del juego con los
las mecánicas del patrones de diseño adictivo
juego con los identificados en la literatura de
patrones psicología del comportamiento.
documentados
de diseño
adictivo +
estudios
epidemiológicos
de la prevalencia
del uso
problemático

Taxonomía General de Aplicaciones
Tipo de
evidencia en
Rango w
Nivel videojuegos y Descripción
(candidato)
sistemas
adictivos
Ac4 Análisis del Los datos de comportamiento del [0.26, 0.44]
comportamiento usuario que documentan el uso
del usuario en el problemático sin el análisis de las
sistema + datos mecánicas de diseño que lo
de uso (tiempo produjeron.
de sesión,
frecuencia) sin
análisis de las
mecánicas de
diseño
Ac0 Análisis El análisis técnico que establece w = 0.00
Ac1/Ac2 que que las mecánicas del juego
establece que las siguen los estándares de diseño
mecánicas del ético del período o que la
juego no tienen dependencia del usuario tiene
características de causas no atribuibles al diseño del
refuerzo variable juego.
o que el uso
problemático no
es causalmente
atribuible al
diseño
§3 Las mecánicas de diseño adictivo y el INCF por
tipo
Las mecánicas de diseño adictivo son las técnicas específicas que el
sistema usa para producir dependencia más allá del valor genuino del
producto. El análisis establece el INCF de cada mecánica — la
contribución causal de esa decisión de diseño específica a la
dependencia del usuario — y la S del diseñador de la mecánica:
¿otros diseñadores del sector en el mismo período habrían
implementado esa mecánica dado el mismo contexto competitivo?

Taxonomía General de Aplicaciones
Mecánica de
Cómo produce INCF del
diseño S del diseñador
dependencia diseñador
adictivo
Refuerzo La recompensa Alto [0.30–0.52] Moderada [0.38–
variable con aleatoria cuando la 0.58]: la mecánica
recompensas produce el mecánica fue de recompensa
aleatorias (loot mismo patrón de diseñada variable es
boxes, gacha) activación deliberadamente ampliamente usada
dopaminérgica para una en el sector. S baja
que las máquinas población de cuando fue
tragamonedas. menores o implementada en
La cuando la un producto
impredictibilidad varianza de la orientado a
de la recompensa fue menores sin
recompensa calibrada restricciones de
hace que el específicamente edad.
sistema sea más para maximizar
difícil de el tiempo de
abandonar que si sesión.
la recompensa
fuera predecible.
Sistemas de Los sistemas que Moderado-alto Moderado [0.40–
progresión que penalizan al [0.25–0.45] 0.62]: los sistemas
imponen usuario por no cuando el de racha son el
costos de salida jugar (la racha sistema de estándar del sector
crecientes que se pierde, el penalización fue del período. S baja
(time-gating, bonus que diseñado cuando la
streaks) expira) deliberadamente penalización fue
convierten la para reducir las calibrada para
decisión de dejar tasas de producir ansiedad
de jugar en una abandono. de separación
pérdida medible.
percibida,
explotando la
aversión a la
pérdida.
Dark patterns Los elementos Alto [0.32–0.55] Moderado [0.38–
de de diseño que cuando los dark 0.60]: los dark
monetización presionan al patterns fueron patterns de
(presión social usuario para diseñados monetización son
para el gasto, gastar dinero real deliberadamente frecuentes en el
temporizadores explotando la para producir sector. S baja
de urgencia) presión social gasto impulsivo cuando fueron
(los otros no planificado. orientados
jugadores tienen específicamente a

Taxonomía General de Aplicaciones
Mecánica de
Cómo produce INCF del
diseño S del diseñador
dependencia diseñador
adictivo
items que tú no), menores o a
la urgencia personas con
temporal (esta historial
oferta expira en documentado de
2 horas), y la compras
asimetría de impulsivas.
información.
Normalización La Muy alto [0.40– Moderado-bajo
del juego de implementación 0.62] cuando la [0.28–0.45]: la
apuestas en de mecánicas de mecánica de omisión de
menores de apuesta (loot apuesta fue restricciones de
edad boxes con valor implementada edad en productos
de mercado real, conscientemente con mecánicas de
torneos con en un producto apuesta era
premio clasificado para idiosincrática de
económico) en menores. algunos
productos desarrolladores del
accesibles para período.
menores sin las
restricciones que
las apuestas
requieren en los
sistemas
regulatorios.
§4 El D_vital del tiempo capturado: la medida del
daño
El daño del diseño adictivo tiene la misma estructura del D_vital de
los demás dominios, con una particularidad que lo distingue: el
componente más significativo frecuentemente no es el daño
económico (el dinero gastado en microtransacciones) sino el daño al
tiempo de vida — las horas y los años de vida invertidos en el juego
más allá del tiempo que la decisión autónoma informada del usuario
habría producido. Ese exceso de tiempo es el T_capturado: el tiempo
que el diseño adictivo extrae del usuario por encima del engagement
genuino.

Taxonomía General de Aplicaciones
D_vital_adictivo = T_capturado +
D_oportunidad_actividades_desplazadas + D_salud_mental +
D_económico
T_capturado: el tiempo de uso que excede el tiempo que el usuario habría elegido dado
información completa sobre las mecánicas adictivas del sistema. Se estima desde la
diferencia entre el tiempo de uso real del usuario y el tiempo que usuarios equivalentes
invierten en productos con el mismo valor genuino, pero sin las mecánicas adictivas.
D_oportunidad_actividades_desplazadas: las actividades de alto valor que el tiempo
capturado impidió — el estudio, el ejercicio, las relaciones sociales, el trabajo.
D_salud_mental: el impacto documentado de las mecánicas adictivas sobre la salud
mental del usuario — especialmente en menores. D_económico: el gasto en
microtransacciones más allá del presupuesto planificado.
§5 Caso resuelto — Loot boxes en juegos de
menores: el diseñador del sistema como nodo de
mayor INCF
Varios países europeos (Bélgica 2018, Países Bajos 2019, múltiples
países desde 2022) han regulado las loot boxes en videojuegos como
juego de azar debido a su estructura de recompensa aleatoria de valor
real. El análisis del INCF en el caso de un juego AAA orientado a
menores que implementó loot boxes con contenido de valor de
mercado real establece la distribución del R* sobre el daño
documentado a los usuarios menores.
Nodo Actor INCF S Análisis
N1 Diseñador del ~42% 0.28 INCF alto. S moderado-bajo: la
sistema de implementación de loot boxes
monetización con valor de mercado real en un
(tomó la producto clasificado para
decisión de menores era idiosincrática —
implementar otros desarrolladores del
loot boxes con período orientados al mismo
valor real en un segmento implementaron
producto mecánicas de monetización sin
clasificado para la misma estructura de apuesta.
menores) La decisión de no implementar

Taxonomía General de Aplicaciones
Nodo Actor INCF S Análisis
restricciones de edad específicas
para las mecánicas de apuesta
era la decisión de diseño de
mayor INCF.
N2 Directivos que ~28% 0.38 INCF moderado-alto. Los
aprobaron el documentos internos de varios
modelo de desarrolladores del período
monetización muestran que los equipos
con directivos tenían acceso a la
conocimiento de literatura de psicología del
los estudios de comportamiento sobre el
psicología del impacto de las recompensas
comportamiento variables y eligieron
disponibles implementar el sistema
conociendo ese impacto.
N3 Reguladores (no ~15% 0.68 INCF moderado. S alta: la
establecieron mayoría de los reguladores del
restricciones período no habían establecido
específicas para restricciones específicas para las
loot boxes con loot boxes, lo que hace que la
valor real) omisión del regulador
específico sea el estándar del
período.
N4 Plataformas de ~10% 0.72 INCF moderado-bajo. S alta.
distribución
(facilitaron el
acceso sin
restricciones de
edad específicas
para las
mecánicas de
apuesta)
N5 Usuarios ~5% 0.85 S muy alta. Cualquier menor
menores y sus bajo las mismas condiciones de
familias exposición al sistema habría
producido patrones de uso
similares dado las mecánicas de
refuerzo variable.

Taxonomía General de Aplicaciones
El resultado central: el nodo de mayor INCF no es el menor que
compró las loot boxes sino el diseñador del sistema de monetización
que eligió implementar la mecánica de apuesta en un producto
orientado a menores con conocimiento de su efecto. El
IAS_regulatorio post-decisiones (Bélgica, Países Bajos): las
regulaciones que requieren la eliminación de las loot boxes con valor
real en productos accesibles para menores actúan sobre el nodo de
mayor INCF — el diseño del sistema de monetización — y tienen
IAS positivo respecto al marco anterior donde los reguladores no
actuaban.
§6 Preguntas y límites del método
Pregunta Instrumento Nivel de certeza
¿El diseño usa Análisis técnico de las Declaración A con
mecánicas mecánicas del sistema: ¿hay documentos Ac1
adictivas — cuál refuerzo variable, dark internos. Declaración B
es el INCF del patterns, penalizaciones de con análisis Ac2 de las
diseñador? salida? Comparación con los mecánicas +
estándares de diseño ético del comparación con el
sector del período. sector.
¿El daño es Comparación del tiempo de Declaración B con datos
proporcional al uso real con el tiempo de uso de uso Ac2 + análisis
valor genuino — de productos con valor comparado con
cuál es el equivalente pero sin productos de referencia.
T_capturado? mecánicas adictivas
documentadas.
¿La población Análisis del sistema de Declaración A con
objetivo incluye clasificación de edad del clasificación verificada
menores — eleva producto y de las mecánicas Ac1. Declaración B con
esto el INCF del específicas para el segmento análisis Ac2 del
diseñador? de menores. segmento de usuarios.
Límite central: la distinción entre engagement y dependencia es un
continuo, no una dicotomía. El sistema establece el límite en la
transparencia y la proporcionalidad, pero la operacionalización de
esos criterios requiere juicio que el análisis cuantitativo no puede

Taxonomía General de Aplicaciones
sustituir completamente. El análisis identifica las mecánicas,
establece el INCF de cada una, y declara el nivel de incertidumbre
en la distinción engagement/dependencia — sin pretender resolver
la norma que el sistema jurídico debe establecer.
— Fin del Capítulo 69 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

