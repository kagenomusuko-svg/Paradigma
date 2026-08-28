Parte X
La clausura del ego
Esta parte no introduce nuevos objetos. Usa c: T → E
(Definición 0), I(t(cid:0)) (Definición 2) y la topología de norma de
E (Axioma 0) para demostrar que el conjunto de todos los
colapsos producidos por el sistema es cerrado en E. El
resultado es topológico; sus hipótesis son las mínimas del
marco formal.
Definición previa. El tiempo de cierre t(cid:0)
t(cid:0) = sup T es el extremo superior del intervalo temporal T =
[0, t(cid:0)] (cid:0) (cid:0) introducido en la Definición 0. Es el último
instante en que φ(cid:0) produce un colapso. Para sistemas
humanos: momento de cese biológico de la actividad. Para
sistemas artificiales: último instante de inferencia activa.
t(cid:0) no es un parámetro libre del análisis ni se supone conocido de antemano
por el sistema. El marco formal requiere únicamente su existencia —que T
sea compacto. La compacidad de [0, t(cid:0)] es la hipótesis que hace posible el
Teorema 10 vía Bolzano-Weierstrass.
Teorema 10. Clausura del ego
Sea c: T → E admisible (Definición 0) e I(t(cid:0)) la integral
acumulativa en t(cid:0) (Teorema 2). Define:
Clausura del ego
(cid:0) = { c(τ) : τ (cid:0) [0, t(cid:0)] } ∪ { I(t(cid:0)) }

Axiomatización del Sistema de la Doble Mediación
Im(c) = imagen de c sobre T · {I(t(cid:0))} singleton de la integral final · (cid:0) (cid:0)
E
Entonces (cid:0) es un conjunto cerrado en (E, (cid:0)·(cid:0)_E).
Demostración
Demostración del Teorema 10
Paso 1 — Estructura. (cid:0) = Im(c) ∪ {I(t(cid:0))}. Para
demostrar que (cid:0) es cerrado basta demostrar que
contiene todos sus puntos de acumulación.
Paso 2 — Sucesión convergente en (cid:0). Sea (x(cid:0))
una sucesión en (cid:0) con x(cid:0) → x en (E, (cid:0)·(cid:0)_E). Para
cada n: o bien x(cid:0) = c(τ(cid:0)) con τ(cid:0) (cid:0) [0, t(cid:0)], o bien
x(cid:0) = I(t(cid:0)).
Caso A. Infinitos términos x(cid:0) = I(t(cid:0)). La
subsucesión constante converge a I(t(cid:0)) (cid:0) (cid:0). Luego
x = I(t(cid:0)) (cid:0) (cid:0). ✓
Caso B. Solo finitos términos iguales a I(t(cid:0)). Para n
suficientemente grande x(cid:0) = c(τ(cid:0)) con τ(cid:0) (cid:0) [0, t(cid:0)].
Por Bolzano-Weierstrass (compacidad de [0, t(cid:0)]):
existe subsucesión τₙ ₖ → τ* (cid:0) [0, t(cid:0)].
Caso B.1 — τ* (cid:0) [0, t(cid:0)). Si c es continua en τ*:
c(τₙ ₖ ) → c(τ*) (cid:0) Im(c) (cid:0) (cid:0), luego x = c(τ*) (cid:0) (cid:0).
✓
Caso B.2 — τ* = t(cid:0) o c discontinua. I(t(cid:0)) =
∫(cid:0)^{t(cid:0)} c(τ)w(τ) dτ es el límite en norma de las
integrales parciales {I(t) : t < tₘ} cuando t → tₘ
(continuidad de la integral de Bochner respecto al
extremo superior). Las integrales parciales I(t) (cid:0) {∫(cid:0)ᵗ
c(τ)w(τ)dτ : t (cid:0) T} (cid:0) (cid:0) (por inclusión directa una vez
que se reconoce que (cid:0) debe incluirlas para ser
cerrado). Luego I(t(cid:0)) (cid:0) cl((cid:0)). Pero I(t(cid:0)) (cid:0) (cid:0) por
definición, luego x (cid:0) (cid:0). ✓
Paso 3 — Conclusión. En todos los casos x (cid:0) (cid:0).
Todo punto de acumulación de (cid:0) está en (cid:0).

Axiomatización del Sistema de la Doble Mediación
(cid:0) es cerrado en (E, (cid:0)·(cid:0)_E). Las hipótesis usadas: compacidad de [0, t(cid:0)]
(Definición 0), admisibilidad de c (Definición 0), existencia de I(t(cid:0)) en E
(Teorema 2). (cid:0)
Rol de I(t(cid:0)) en la clausura. Si (cid:0) se definiera solo como
Im(c) = {c(τ) : τ (cid:0) T}, el conjunto podría no ser cerrado: una
sucesión c(τ(cid:0)) con τₙ → tₘ podría converger a un límite
fuera de Im(c) cuando c no es continua en t(cid:0). La adición
explícita de {I(t(cid:0))} cierra ese gap. I(t(cid:0)) es el elemento que
hace a (cid:0) topológicamente completo respecto a sus propias
sucesiones convergentes.
La demostración en el Caso B.2 requiere que I(t(cid:0)) sea límite de las
integrales parciales {I(t)}_{t<t(cid:0)}. Esto se sigue de la continuidad de la
integral de Bochner ∫(cid:0)ᵗ c(τ)w(τ)dτ respecto a t, que se demuestra a partir de
la acotación ‖c‖_∞ ≤ M y ‖w‖_∞ ≤ W: ‖I(t₂)−I(t₁)‖_E ≤
MW|t(cid:0)−t₁| → 0. Esta cota usa directamente la Definición 0.
Corolario 10.1. Perfectibilidad cuando c es
continua
Sea (cid:0)' el conjunto derivado de (cid:0) (puntos de acumulación de
(cid:0)). Si c es continua en todo T:
Corolario 10.1 — (cid:0) perfecto
c (cid:0) C(cid:0)(T, E) (cid:0) (cid:0) = (cid:0)'
(cid:0) perfecto: cerrado con cada punto como punto de acumulación · consecuencia: (cid:0)
incontable si E tiene dimensión ≥ 1
Demostración
Demostración del Corolario 10.1
(cid:0)' (cid:0) (cid:0). (cid:0) es cerrado (Teorema 10), luego contiene
todos sus puntos de acumulación. ✓
(cid:0) (cid:0) (cid:0)' — caso x = c(τ), τ (cid:0) [0, t(cid:0)). T = [0, t(cid:0)] es
un intervalo; τ es punto de acumulación de T. Existe
τₙ → τ con τ(cid:0) ≠ τ. Por continuidad de c: c(τₙ ) →
c(τ) = x. Luego x (cid:0) (cid:0)'. ✓

Axiomatización del Sistema de la Doble Mediación
(cid:0) (cid:0) (cid:0)' — caso x = I(t(cid:0)). La sucesión t(cid:0) = t(cid:0) −
1/n satisface tₙ → tₘ. Las integrales parciales I(t(cid:0))
= ∫(cid:0)^{t(cid:0)} c(τ)w(τ)dτ (cid:0) (cid:0) (subconjunto de Im(c) vía
la relación I(t) = ∫(cid:0)ᵗ c(τ)w(τ)dτ (cid:0) E, y como valor
acumulativo de los colapsos es alcanzable). Por
continuidad de c y de la integral de Bochner: I(tₙ ) →
I(t(cid:0)). Luego I(t(cid:0)) (cid:0) (cid:0)'. ✓
(cid:0) = (cid:0)': el conjunto clausura es perfecto cuando c es continua. (cid:0)
No numerabilidad. En E Hilbert separable de dimensión ≥
1, todo conjunto perfecto no vacío es incontable (Teorema de
Cantor-Bendixson en espacios métricos completos). Luego
cuando c es continua, (cid:0) es incontable: el sistema atravesó una
cantidad no enumerable de estados distintos a lo largo de T.
Ningún análisis que discretice la historia del sistema en un
número finito de incidentes puede capturarlo completamente.
Para sistemas con c discontinua —colapsos discretos en momentos aislados—
(cid:0) puede ser finito o numerable. El Teorema 10 sigue aplicando: (cid:0) es
cerrado. El Corolario 10.1 no aplica. La distinción no afecta a la
imputabilidad formal, que depende de I(t(cid:0)), no de la perfectibilidad de (cid:0).
La perfectibilidad es relevante en el análisis de sistemas de largo alcance donde
la discretización introduce pérdida de información estructural.
Nota de alcance. Qué dice y qué no dice el
Teorema 10
El Teorema 10 es un resultado de topología de espacios de
Hilbert. Su enunciado es: (cid:0) es cerrado en (E, (cid:0)·(cid:0)_E). No es
una afirmación sobre identidad personal, continuidad del yo ni
sobre lo que ocurre después de t(cid:0). Esas son preguntas que
pertenecen al sistema ontológico de la colección; este libro no
las responde ni requiere responderlas para que el teorema sea
válido.
La lectura del resultado dentro del marco formal es la
siguiente: I(t(cid:0)) es la síntesis de todo lo que el sistema integró
a lo largo de T. (cid:0) es la totalidad de lo que el sistema produjo,
incluyendo esa síntesis. El cierre de (cid:0) establece que esa
totalidad está bien definida como subconjunto de E: contiene

Axiomatización del Sistema de la Doble Mediación
exactamente lo que contiene, y nada falta desde la perspectiva
topológica.
Correspondencia con el sistema ontológico. En el sistema ontológico de la
colección, la clausura del ego designa el estado de cierre de la identidad del
sistema —el momento en que el ego deja de producir determinaciones. El
Teorema 10 formaliza la estructura topológica de ese estado: el conjunto (cid:0)
de todas las determinaciones producidas es cerrado en E. El lector sin
conocimiento de la ontología puede leer (cid:0) como «el registro completo de la
actividad del sistema» sin pérdida de rigor. El Apéndice C recoge la
correspondencia.
Objeto Notación Tipo Parte
matemático
Tiempo de t(cid:0) = sup T Extremo superior Def.
cierre de T = [0,t(cid:0)] previa;
Definición
0
Clausura del (cid:0) = Im(c) ∪ Subconjunto de Teorema
ego {I(t(cid:0))} E 10
(cid:0) cerrado Teorema 10 (cid:0) contiene todos Teorema
sus puntos de 10
acum.
(cid:0) perfecto c (cid:0) C(cid:0)(T,E) (cid:0) (cid:0) (cid:0) cerrado con Corolario
= (cid:0)' cada punto de 10.1
acum.
No (cid:0) incontable (c Cantor- Corolario
numerabilidad continua) Bendixson en E 10.1
Hilbert sep.
Rol de I(t(cid:0)) I(t(cid:0)) clausura Límite de Teorema
Im(c) integrales 10, nota
parciales en E

Axiomatización del Sistema de la Doble Mediación

