Parte II
La segunda mediación φ₂ e I(t)
Axioma 2. La segunda mediación
Existe una función:
Segunda mediación
φ₂: A × E → E
A (cid:0) E subespacio de actos (Axioma 1) · el segundo argumento es el estado
acumulado I(t) (cid:0) E · el valor es I (t + Δt) (cid:0) E
φ₂ (a, I(t)) opera sobre cada colapso a (cid:0) A producido por φ(cid:0)
en tres pasos:
(i) Evaluación. Se computa eval (a, I(t)) (cid:0) (cid:0), donde
eval: A × E → (cid:0) satisface las condiciones del
Teorema 2.2.
(ii) Decisión binaria. Si eval (a, I(t)) > θ, el colapso
es aceptado; si eval (a, I(t)) ≤ θ, es rechazado y se
registra en RSC(t) \ I(t).
(iii) Actualización. I (t + Δt) = φ₂ (a, I(t)) = I(t) +
δ(a) · 1_ {eval (a, I(t)) > θ}, con δ(a) (cid:0) E la
modificación producida por la integración de a.
El Axioma 2 postula la existencia de φ(cid:0) sin fijar la forma de eval ni el
valor de θ. Ambos se precisan en el Teorema 2.2 con las condiciones mínimas
que el núcleo formal requiere. La calibración de eval para cada dominio de
aplicación pertenece a los volúmenes correspondientes de Metrología Causal y
a la Taxonomía.

Axiomatización del Sistema de la Doble Mediación
Definición 2. La integral acumulativa I(t)
Sea w: T → ℝ₊ una función de peso medible y acotada. La
integral acumulativa del sistema hasta el momento t es:
Integral acumulativa
I(t) = ∫(cid:0)ᵗ c(τ) w(τ) dτ ∈ E
c: T → E función de colapso admisible (Definición 0) · w: T → ℝ₊ medible y
acotada · integral en sentido de Bochner · I(t) (cid:0) E para todo t (cid:0) T
La existencia y unicidad de I(t) en E se demuestran en el
Teorema 2. La función de peso w(τ) determina la relevancia
temporal de cada colapso; el núcleo formal no impone
ninguna forma específica a w más allá de la medibilidad y la
acotación.
I(t) no es un número real sino un elemento de E. Tiene estructura vectorial,
norma y producto interno. Esta estructura es la que permite que φ(cid:0), α y la
REC de la Parte VII estén bien definidos. Para familias concretas de w —
decrecimiento exponencial, ventana rectangular, kernel gaussiano— ver el

## Apéndice B de Metrología Causal Vol. I.

Teorema 2. Existencia y unicidad de I(t)
Para toda c: T → E admisible en el sentido de la Definición 0
y toda w: T → ℝ₊ medible y acotada, I(t) existe y es único en
E para todo t (cid:0) T.
Demostración
Demostración del Teorema 2
Paso 1. Por la Definición 0: c es medible en sentido
de Bochner y (cid:0)c(τ)(cid:0)_E ≤ M para algún M > 0 y todo
τ (cid:0) T.
Paso 2. Sea f(τ) = c(τ)w(τ). Como w es medible y
‖ w‖ _∞ ≤ W < ∞, el producto f hereda la
medibilidad de Bochner de c y satisface (cid:0)f(τ)(cid:0)_E ≤
MW para todo τ (cid:0) T.

Axiomatización del Sistema de la Doble Mediación
Paso 3. f es esencialmente acotada, luego f (cid:0) L¹ (T;
E): ∫(cid:0)^{t_m} (cid:0)f(τ)‖ _E dτ ≤ MW · t_m < ∞, con
t_m = sup T < ∞ por la Definición 0.
Paso 4. Por el teorema fundamental de integración
de Bochner, toda f (cid:0) L¹ (T; E) con E Banach admite
integral de Bochner I(t) = ∫(cid:0)ᵗ f(τ) dτ (cid:0) E, única como
elemento de E.
Existencia y unicidad de I(t) en E para todo t (cid:0) T. (cid:0)
Teorema 2.1. Irreversibilidad de I(t)
Si w(τ) > 0 para todo τ (cid:0) T y c(τ) ≠ 0 en un conjunto de
medida de Lebesgue positiva en T, entonces para todo par t(cid:0)
> t(cid:0) en T con las mismas hipótesis en [t(cid:0), t(cid:0)]:
Condición de irreversibilidad
(cid:0)I(t(cid:0)) − I(t₁) ‖_E > 0
bajo w(τ) > 0 en [t(cid:0), t(cid:0)] y c(τ) ≠ 0 en conjunto de medida positiva en [t(cid:0),
t(cid:0)]
Demostración
Demostración del Teorema 2.1
Paso 1. I(t(cid:0)) − I(t₁ ) = ∫_{t₁} ^{t(cid:0)} c(τ)w(τ) dτ. Sea
g(τ) = c(τ)w(τ). Por hipótesis: w(τ) > 0 en [t(cid:0), t(cid:0)] y
c(τ) ≠ 0 en un conjunto S (cid:0) [t(cid:0), t(cid:0)] con μ(S) > 0.
Luego g(τ) ≠ 0 en S.
Paso 2. Por la propiedad fundamental de la integral
de Bochner: si g (cid:0) L¹ (T; E) y g(τ) ≠ 0 en un conjunto
de medida positiva, entonces (cid:0)∫ g(τ) dτ(cid:0)_E > 0.
Combinando: (cid:0)I(t(cid:0)) − I(t₁) ‖_E = (cid:0)∫_{t₁} ^{t(cid:0)}
g(τ) dτ(cid:0)_E > 0. (cid:0)
Las hipótesis son necesarias: si w(τ) = 0 en algún subintervalo o c(τ) = 0 a.e., I
puede ser constante en ese período —situación admisible en el marco formal.
Consecuencia para la responsabilidad. El Teorema 2.1
establece que todo colapso no nulo producido bajo w > 0 deja

Axiomatización del Sistema de la Doble Mediación
huella permanente en I(t). El estado del sistema no puede
retornar a su valor anterior por la sola acción del tiempo: solo
colapsos futuros integrados pueden recontextualizar I(t), no
eliminarlo. Esta permanencia es el fundamento matemático de
la imputabilidad en el sistema.
Definición 2.1. El registro de colapsos RSC(t)
El registro de colapsos del sistema hasta t es la imagen de c en
T:
Registro de colapsos
RSC(t) = {c(τ): τ (cid:0) [0, t]} ⊆ E
imagen de la función de colapso en [0, t] · incluye todos los colapsos producidos
por φ(cid:0) con independencia de si φ(cid:0) los integró
La relación entre RSC(t) e I(t) es la siguiente: I(t) es la integral
de Bochner de los colapsos de RSC(t) que φ(cid:0) aceptó,
ponderados por w. La diferencia RSC(t) \ I(t) contiene los
colapsos producidos pero rechazados. El coeficiente de
asunción α de la Parte IV mide la proporción ponderada de
RSC(t) que está integrada en I(t).
La distinción RSC(t) / I(t) es central en la aplicación: RSC(t) corresponde
a los hechos documentados del expediente —todo lo que el actor produjo— e
I(t) a lo que el actor integró como propio —lo que reconoció, reparó o asumió
estructuralmente. La brecha RSC(t) \ I(t) es el espacio que α mide y Δ
cuantifica.
Teorema 2.2. Representación de φ(cid:0) y
condiciones sobre eval
La segunda mediación φ(cid:0) admite la representación:
Representación de φ(cid:0)
φ₂ (a, I(t)) = I(t) + δ(a) · 1_ {eval (a, I(t)) > θ}
eval: A × E → ℝ función de evaluación de compatibilidad

Axiomatización del Sistema de la Doble Mediación
δ(a) (cid:0) E modificación producida por la integración
de a
θ (cid:0) (cid:0) umbral de integración
1_ {···} función indicadora · vale 1 si eval (a, I(t)) > θ, 0 en caso contrario
Para que la representación esté bien definida, eval y δ deben
satisfacer:
(i) Medibilidad. eval es medible como función A ×
E → (cid:0) respecto a las σ-álgebras de Borel de A y E.
(ii) Compatibilidad. eval (a, I(t)) > θ si y solo si el
colapso a es compatible con el estado actual I(t) en el
sentido operativo del dominio. El núcleo formal no
fija la noción de compatibilidad; exige que eval la
codifique de forma medible y que θ sea un umbral fijo
para un sistema dado.
(iii) No-amplificación. (cid:0)δ(a)(cid:0)_E ≤ (cid:0)a(cid:0)_E: la
modificación que produce la integración no supera en
norma al colapso que la produce. Esta condición evita
singularidades en I(t) y es el primer criterio de
validación de cualquier implementación de φ(cid:0).
Demostración
Demostración del Teorema 2.2
Paso 1. El Axioma 2 establece tres etapas: evaluación,
decisión binaria y actualización. La función indicadora
1_ {eval > θ} captura exactamente la decisión binaria:
1 cuando eval > θ (integración), 0 en caso contrario
(rechazo).
Paso 2. El producto δ(a) · 1_ {eval > θ} es δ(a)
cuando hay integración y 0 cuando hay rechazo. La
suma I(t) + δ(a) · 1_ {···} produce I(t) + δ(a) en el
primer caso e I(t) en el segundo.
Paso 3. Ambos resultados están en E: I(t) (cid:0) E por el
Teorema 2; δ(a) (cid:0) E por la condición (iii); luego I(t)
+ δ(a) (cid:0) E. La representación es consistente con el
codominio del Axioma 2. ✓

Axiomatización del Sistema de la Doble Mediación
La representación es válida bajo las condiciones (i)–(iii). (cid:0)
Sobre la familia de funciones eval. Las condiciones (i)–(iii)
son el marco mínimo. Cualquier función eval que las satisfaga
produce una φ(cid:0) bien definida y consistente con el Axioma 2.
Una familia paramétrica natural es eval (a, I(t)) = (cid:0)a, I(t)(cid:0)_E
/ ((cid:0)a(cid:0)_E · (cid:0)I(t)(cid:0)_E), la similitud coseno en E: mide la
alineación direccional entre el colapso y el estado acumulado,
toma valores en [−1, 1], es medible y satisface la no-
amplificación cuando δ(a) se define proporcionalmente. La
calibración de eval para cada dominio —jurídico, clínico, de
IA— pertenece a la Taxonomía y a los protocolos de
Metrología Causal.
La elección de la similitud coseno como familia de referencia resuelve la crítica
de arbitrariedad sobre eval planteada en la revisión externa: eval no es una
caja negra, sino un espacio paramétrico de funciones con condiciones
verificables. La condición (iii) en particular es inmediatamente computable y
constituye el primer test de implementación.
Objeto Notación Tipo Parte
matemático
Segunda φ(cid:0) : A×E → E Función Axioma 2
mediación (existencia
postulada)
Función de w : T → ℝ₊ Medible y Definición
peso acotada 2
Integral I(t) = ∫(cid:0)ᵗ c w dτ (cid:0) E Integral de Definición
acumulativa Bochner en 2; Teorema
E 2
Existencia y Teorema 2 L¹(T;E) + Teorema 2
unicidad Bochner
Irreversibilidad (cid:0)I(t(cid:0))−I(t₁ )‖ _E > Desigualdad Teorema
0 en E 2.1

Axiomatización del Sistema de la Doble Mediación
Registro de RSC(t) = {c(τ): Imagen de c Definición
colapsos τ(cid:0)[0,t]} en [0,t] 2.1
Colapsos RSC(t) \ I(t) Diferencia Definición
rechazados de conjuntos 2.1
Representación I(t)+δ(a)·1_{eval>θ} Suma en E Teorema
de φ(cid:0) con 2.2
indicadora
Función de eval : A×E → (cid:0) Medible; Teorema
evaluación familia: cos. 2.2
sim.
Modificación δ(a) (cid:0) E, (cid:0)δ(cid:0)_E ≤ Vector en E; Teorema
(cid:0)a(cid:0)_E no- 2.2
amplificación
Umbral de θ (cid:0) (cid:0) Parámetro Teorema
integración escalar 2.2

Axiomatización del Sistema de la Doble Mediación
