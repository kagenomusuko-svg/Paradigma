Parte 0
El espacio de base
Axioma 0. Espacio de colapsos
Sea E un espacio de Hilbert separable con producto interno
(cid:0)·,·(cid:0)_E y norma (cid:0)·(cid:0)_E = √(cid:0)·,·(cid:0)_E. E satisface:
(i) ∀ c, d ∈ E, α (cid:0) (cid:0): c + d (cid:0) E y αc (cid:0) E.
(ii) Toda sucesión de Cauchy en (E, (cid:0)·(cid:0)_E) tiene
límite en E.
(iii) Existe D (cid:0) E denso y numerable.
E es el espacio de estados posibles del modelo. Los elementos
c (cid:0) E son los estados que el sistema puede determinar dentro
del modelo; no se afirma que todo c (cid:0) E sea realizable por un
sistema concreto.
Adopción de estructura de Hilbert. Se adopta un espacio
de Hilbert separable —y no un espacio de Banach reflexivo
equipado con una forma bilineal continua— porque es la
estructura suficiente para la computabilidad del sistema sin
introducir hipótesis adicionales sobre el espacio. Tres
exigencias simultáneas determinan esta elección: (i) producto
interno explícito para la forma bilineal (cid:0)∇v_t, u_k(cid:0)_E de la
Definición 1 de la Parte I, no garantizada en Banach general;
(ii) completitud para la existencia de la integral de Bochner de
la Definición 2; (iii) separabilidad para la existencia de base
ortonormal numerable, condición del método de potencias de
la Parte VI. Un espacio de Banach reflexivo con forma bilineal

Axiomatización del Sistema de la Doble Mediación
continua es alternativa teóricamente posible, pero introduce
complejidad sin beneficio para el sistema.
v_t y los vectores u_k se definen formalmente en la Parte I. Su aparición en
la justificación precedente es anticipatoria: se incluye para motivar la elección
de E, no para usarlos.
Función de embedding. La correspondencia entre los
outputs observables de un sistema concreto y los elementos
de E no es parte del marco axiomático: es una decisión de
modelado que debe justificarse en cada aplicación.
Formalmente, se postula la existencia de una función emb:
Outputs → E que asocia a cada output un elemento de E. Esta
función debe preservar las relaciones de orden relevantes para
la asignación de pesos causales en el grafo G —definido en la
Parte VI— de modo que outputs causalmente más similares
tengan imágenes más cercanas en (cid:0)·(cid:0)_E. La validez
estructural de los resultados del sistema no depende de la
elección concreta de emb, siempre que se mantengan las
propiedades del Axioma 0 y la condición de preservación de
orden. En sistemas artificiales, emb es la función de
embedding del modelo. En sistemas humanos, emb se
especifica en el Volumen I de Metrología Causal.
La restricción sobre emb no es decorativa: la función eval de la Parte II
impone condiciones de compatibilidad sobre c(τ) respecto a I(t). Sin una emb
que preserve estructura de relevancia causal, eval no satisface esas condiciones.
La restricción es indirecta pero efectiva.
Definición 0. Función de colapso
Sea T (cid:0) (cid:0) un intervalo compacto; sin pérdida de generalidad
T = [0, t_m] con t_m el tiempo de cierre definido en la Parte

## X. Una función c: T → E es admisible si satisface:

(i) c es medible en sentido de Bochner respecto a las
σ-álgebras de Borel de T y E.
(ii) (cid:0) M > 0 tal que (cid:0)c(τ)(cid:0)_E ≤ M para todo τ (cid:0)
T.

Axiomatización del Sistema de la Doble Mediación
Función de colapso
c: T → E, c admisible
T = [0, t_m] · E espacio del Axioma 0 · t_m definido en la Parte X
La medibilidad de Bochner y la acotación de c garantizan
conjuntamente su integrabilidad en sentido de Bochner. En
consecuencia, para toda función w: T → ℝ₊ medible y
acotada, la integral ∫(cid:0)ᵗ c(τ)w(τ) dτ pertenece a E y es el único
elemento de E tal que:
Caracterización de la integral de Bochner
(cid:0) ∫(cid:0)ᵗ c(τ)w(τ) dτ, e (cid:0)_E = ∫(cid:0)ᵗ (cid:0)c(τ)w(τ), e(cid:0)_E dτ ∀ e
(cid:0) E
En E Hilbert, por el teorema de representación de Riesz, E* se identifica
isométricamente con E; el dual x* (cid:0) E* se sustituye directamente por e (cid:0) E
mediante ese isomorfismo.
Invarianza bajo permutación e irreversibilidad de I(t). La
integral de Bochner es invariante bajo permutaciones del
orden de los colapsos cuando los pesos w(τ) son constantes:
la secuencia (c(τ(cid:0)), c(τ(cid:0)), c(τ(cid:0))) y cualquier permutación suya
producen el mismo valor de ∫c dτ bajo pesos uniformes. La
noción de historia acumulada I(t) no descansa en esta
propiedad, sino en dos mecanismos distintos: (a) la función de
peso w(τ), que puede asignar mayor masa a colapsos recientes,
y (b) la dependencia dinámica de φ(cid:0) y φ(cid:0) de I(t) en cada paso,
de modo que c(τ(cid:0)) depende del estado I(τ(cid:0)⁺ ). La
irreversibilidad de I(t) es una propiedad del sistema dinámico,
no de la integral. Esta distinción se formaliza en el Teorema
2.1.
Para E Hilbert, la integral de Bochner requiere que c sea fuertemente medible
—coincidencia a.e. con límite de funciones simples— y ∫(cid:0)c(τ)(cid:0)_E dτ <
∞. Las condiciones (i) y (ii) de la Definición 0 garantizan ambas. Para E
Banach general el argumento es análogo con E* en lugar de E, pero el
isomorfismo de Riesz no aplica.

Axiomatización del Sistema de la Doble Mediación
Objeto Notación Tipo matemático Parte
Espacio de E Espacio de Hilbert Axioma 0
base separable
Producto (cid:0)·,·(cid:0)_E Forma bilineal Axioma 0
interno simétrica def.
positiva
Norma (cid:0)·(cid:0)_E Norma completa Axioma 0
inducida
Función de emb : Out Inmersión (decisión Axioma 0,
embedding → E de modelado) nota
Intervalo T = [0, t_m] Compacto de (cid:0) Definición 0
temporal
Función de c : T → E Función admisible Definición 0
colapso en sentido de
Bochner
Correspondencia con el sistema ontológico de la colección.
En el sistema ontológico que esta axiomatización formaliza, E corresponde
al Caos: el espacio de posibilidad absoluta anterior a toda determinación,
donde ningún estado ha sido seleccionado y todos son igualmente posibles. La
estructura de Hilbert captura esto con precisión: E es completo —ninguna
posibilidad está ausente—, separable —las posibilidades son computables—
y sin elemento privilegiado antes de que opere φ(cid:0).
El colapso c(τ) es la selección de un elemento de E en el instante τ: la
determinación de una posibilidad. Antes del colapso, el sistema vive en E sin
posición definida; después, tiene una. La función c: T → E traza esa
secuencia de determinaciones a lo largo del tiempo. La integral I(t) las
acumula. La Parte X formaliza el cierre de ese proceso cuando T se agota.
El lector sin conocimiento de la ontología de la colección puede ignorar esta
nota sin pérdida de rigor formal. El Apéndice C recoge la correspondencia
completa entre la terminología ontológica y la terminología matemática de este
libro.

Axiomatización del Sistema de la Doble Mediación
