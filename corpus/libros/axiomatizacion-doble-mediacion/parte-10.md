### Parte X

### La clausura del ego

Esta parte no introduce nuevos objetos. Usa c: T → E (Definición 0), I(t□) (Definición 2) y la topología de norma de E (Axioma 0) para demostrar que el conjunto de todos los colapsos producidos por el sistema es cerrado en E. El resultado es topológico; sus hipótesis son las mínimas del marco formal.

### Definición previa.  El tiempo de cierre t□

t□ = sup T es el extremo superior del intervalo temporal T = [0, t□] □ □ introducido en la Definición 0. Es el último instante en que φ□ produce un colapso. Para sistemas humanos: momento de cese biológico de la actividad. Para sistemas artificiales: último instante de inferencia activa.

t□ no es un parámetro libre del análisis ni se supone conocido de antemano por el sistema. El marco formal requiere únicamente su existencia —que T sea compacto. La compacidad de [0, t□] es la hipótesis que hace posible el Teorema 10 vía Bolzano-Weierstrass.

### Teorema 10.  Clausura del ego

Sea c: T → E admisible (Definición 0) e I(t□) la integral acumulativa en t□ (Teorema 2). Define:

Clausura del ego

□ = { c(τ) : τ □ [0, t□] } ∪ { I(t□) }

Axiomatización del Sistema de la Doble Mediación

Im(c) = imagen de c sobre T  ·  {I(t□)} singleton de la integral final  ·  □ □ E

### Entonces □ es un conjunto cerrado en (E, □·□_E).

Demostración

Demostración del Teorema 10

Paso 1 — Estructura.  □ = Im(c) ∪ {I(t□)}. Para demostrar que □ es cerrado basta demostrar que contiene todos sus puntos de acumulación. Paso 2 — Sucesión convergente en □.  Sea (x□) una sucesión en □ con x□ → x en (E, □·□_E). Para cada n: o bien x□ = c(τ□) con τ□ □ [0, t□], o bien x□ = I(t□). Caso A.  Infinitos términos x□ = I(t□). La subsucesión constante converge a I(t□) □ □. Luego x = I(t□) □ □. ✓ Caso B.  Solo finitos términos iguales a I(t□). Para n suficientemente grande x□ = c(τ□) con τ□ □ [0, t□]. Por Bolzano-Weierstrass (compacidad de [0, t□]): existe subsucesión τₙ ₖ → τ* □ [0, t□]. Caso B.1 — τ* □ [0, t□).  Si c es continua en τ*: c(τₙ ₖ ) → c(τ*) □ Im(c) □ □, luego x = c(τ*) □ □. ✓ Caso B.2 — τ* = t□ o c discontinua.  I(t□) = ∫□^{t□} c(τ)w(τ) dτ es el límite en norma de las integrales parciales {I(t) : t < tₘ ₘ } cuando t → t (continuidad de la integral de Bochner respecto al extremo superior). Las integrales parciales I(t) □ {∫□ᵗ c(τ)w(τ)dτ : t □ T} □ □ (por inclusión directa una vez que se reconoce que □ debe incluirlas para ser cerrado). Luego I(t□) □ cl(□). Pero I(t□) □ □ por definición, luego x □ □. ✓ Paso 3 — Conclusión.  En todos los casos x □ □. Todo punto de acumulación de □ está en □.

Axiomatización del Sistema de la Doble Mediación

□ es cerrado en (E, □·□_E). Las hipótesis usadas: compacidad de [0, t□] (Definición 0), admisibilidad de c (Definición 0), existencia de I(t□) en E (Teorema 2). □

Rol de I(t□) en la clausura.  Si □ se definiera solo como Im(c) = {c(τ) : τ □ T}, el conjunto podría no ser cerrado: una sucesión c(τ□) con τₙ ₘ → t podría converger a un límite fuera de Im(c) cuando c no es continua en t□. La adición explícita de {I(t□)} cierra ese gap. I(t□) es el elemento que hace a □ topológicamente completo respecto a sus propias sucesiones convergentes.

La demostración en el Caso B.2 requiere que I(t□) sea límite de las integrales parciales {I(t)}_{t<t□}. Esto se sigue de la continuidad de la integral de Bochner ∫□ᵗ c(τ)w(τ)dτ respecto a t, que se demuestra a partir de la acotación ₂ ‖ ‖ ‖ ‖ ‖ c _∞ ≤ M y w _∞ ≤ W: I(t ) ₁ ‖ −I(t ) _E ≤ MW|t□ ₁ −t | → 0. Esta cota usa directamente la Definición 0.

### Corolario 10.1.  Perfectibilidad cuando c es continua

### Sea □' el conjunto derivado de □ (puntos de acumulación de □). Si c es continua en todo T:

### Corolario 10.1 — □ perfecto

c □ C□(T, E)  □  □ = □' □ perfecto: cerrado con cada punto como punto de acumulación · consecuencia: □ incontable si E tiene dimensión ≥ 1

### Demostración

Demostración del Corolario 10.1

□' □ □.  □ es cerrado (Teorema 10), luego contiene todos sus puntos de acumulación. ✓ □ □ □' — caso x = c(τ), τ □ [0, t□).  T = [0, t□] es un intervalo; τ es punto de acumulación de T. Existe τₙ → τ con τ□ ≠ τ. Por continuidad de c: c(τₙ ) → c(τ) = x. Luego x □ □'. ✓

Axiomatización del Sistema de la Doble Mediación

□ □ □' — caso x = I(t□).  La sucesión t□ = t□ − 1/n satisface tₙ ₘ → t . Las integrales parciales I(t□) = ∫□^{t□} c(τ)w(τ)dτ □ □ (subconjunto de Im(c) vía la relación I(t) = ∫□ᵗ c(τ)w(τ)dτ □ E, y como valor acumulativo de los colapsos es alcanzable). Por continuidad de c y de la integral de Bochner: I(tₙ ) → I(t□). Luego I(t□) □ □'. ✓ □ = □': el conjunto clausura es perfecto cuando c es continua. □

No numerabilidad.  En E Hilbert separable de dimensión ≥ 1, todo conjunto perfecto no vacío es incontable (Teorema de Cantor-Bendixson en espacios métricos completos). Luego cuando c es continua, □ es incontable: el sistema atravesó una cantidad no enumerable de estados distintos a lo largo de T. Ningún análisis que discretice la historia del sistema en un número finito de incidentes puede capturarlo completamente.

Para sistemas con c discontinua —colapsos discretos en momentos aislados— □ puede ser finito o numerable. El Teorema 10 sigue aplicando: □ es cerrado. El Corolario 10.1 no aplica. La distinción no afecta a la imputabilidad formal, que depende de I(t□), no de la perfectibilidad de □. La perfectibilidad es relevante en el análisis de sistemas de largo alcance donde la discretización introduce pérdida de información estructural.

### Nota de alcance.  Qué dice y qué no dice el Teorema 10

El Teorema 10 es un resultado de topología de espacios de Hilbert. Su enunciado es: □ es cerrado en (E, □·□_E). No es una afirmación sobre identidad personal, continuidad del yo ni sobre lo que ocurre después de t□. Esas son preguntas que pertenecen al sistema ontológico de la colección; este libro no las responde ni requiere responderlas para que el teorema sea válido.

La lectura del resultado dentro del marco formal es la siguiente: I(t□) es la síntesis de todo lo que el sistema integró a lo largo de T. □ es la totalidad de lo que el sistema produjo, incluyendo esa síntesis. El cierre de □ establece que esa totalidad está bien definida como subconjunto de E: contiene

Axiomatización del Sistema de la Doble Mediación

### exactamente lo que contiene, y nada falta desde la perspectiva topológica.

Correspondencia con el sistema ontológico. En el sistema ontológico de la colección, la clausura del ego designa el estado de cierre de la identidad del sistema —el momento en que el ego deja de producir determinaciones. El Teorema 10 formaliza la estructura topológica de ese estado: el conjunto □ de todas las determinaciones producidas es cerrado en E. El lector sin conocimiento de la ontología puede leer □ como «el registro completo de la actividad del sistema» sin pérdida de rigor. El Apéndice C recoge la correspondencia.

Objeto Notación Tipo matemático

Parte

t□ = sup T Extremo superior de T = [0,t□]

Tiempo de cierre

Def. previa; Definición 0

Clausura del ego

□ = Im(c) ∪ {I(t□)}

Subconjunto de E

### Teorema 10

□ cerrado Teorema 10 □ contiene todos sus puntos de acum.

### Teorema 10

□ perfecto c □ C□(T,E) □ □ = □'

□ cerrado con cada punto de acum.

### Corolario 10.1

No numerabilidad

□ incontable (c continua)

Cantor-Bendixson en E Hilbert sep.

### Corolario 10.1

Rol de I(t□) I(t□) clausura Im(c)

Límite de integrales parciales en E

### Teorema 10, nota

Axiomatización del Sistema de la Doble Mediación

