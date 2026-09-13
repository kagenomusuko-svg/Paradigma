### Parte II

### La segunda mediación φ₂ e I(t)

### Axioma 2.  La segunda mediación

Existe una función:

Segunda mediación

φ₂: A × E → E A □ E subespacio de actos (Axioma 1) · el segundo argumento es el estado acumulado I(t) □ E · el valor es I (t + Δt) □ E

φ₂ (a, I(t)) opera sobre cada colapso a □ A producido por φ□ en tres pasos:

(i)  Evaluación. Se computa eval (a, I(t)) □ □, donde eval: A × E → □ satisface las condiciones del Teorema 2.2. (ii)  Decisión binaria. Si eval (a, I(t)) > θ, el colapso es aceptado; si eval (a, I(t)) ≤ θ, es rechazado y se registra en RSC(t) \ I(t). (iii)  Actualización. I (t + Δt) = φ₂ (a, I(t)) = I(t) + δ(a) · 1_ {eval (a, I(t)) > θ}, con δ(a) □ E la modificación producida por la integración de a.

El Axioma 2 postula la existencia de φ□ sin fijar la forma de eval ni el valor de θ. Ambos se precisan en el Teorema 2.2 con las condiciones mínimas que el núcleo formal requiere. La calibración de eval para cada dominio de aplicación pertenece a los volúmenes correspondientes de Metrología Causal y a la Taxonomía.

Axiomatización del Sistema de la Doble Mediación

### Definición 2.  La integral acumulativa I(t)

Sea w: T → ℝ₊ una función de peso medible y acotada. La integral acumulativa del sistema hasta el momento t es:

Integral acumulativa

I(t) = ∫□ᵗ c(τ) w(τ) dτ ∈ E c: T → E función de colapso admisible (Definición 0) · w: T → ℝ₊ medible y acotada · integral en sentido de Bochner · I(t) □ E para todo t □ T

La existencia y unicidad de I(t) en E se demuestran en el Teorema 2. La función de peso w(τ) determina la relevancia temporal de cada colapso; el núcleo formal no impone ninguna forma específica a w más allá de la medibilidad y la acotación.

I(t) no es un número real sino un elemento de E. Tiene estructura vectorial, norma y producto interno. Esta estructura es la que permite que φ□, α y la REC de la Parte VII estén bien definidos. Para familias concretas de w — decrecimiento exponencial, ventana rectangular, kernel gaussiano— ver el Apéndice B de Metrología Causal Vol. I.

### Teorema 2.  Existencia y unicidad de I(t)

Para toda c: T → E admisible en el sentido de la Definición 0 y toda w: T → ℝ₊ medible y acotada, I(t) existe y es único en E para todo t □ T.

Demostración

Demostración del Teorema 2

Paso 1.  Por la Definición 0: c es medible en sentido de Bochner y □c(τ)□_E ≤ M para algún M > 0 y todo τ □ T. Paso 2.  Sea f(τ) = c(τ)w(τ). Como w es medible y ‖ ‖ w _∞ ≤ W < ∞, el producto f hereda la medibilidad de Bochner de c y satisface □f(τ)□_E ≤ MW para todo τ □ T.

Axiomatización del Sistema de la Doble Mediación

Paso 3.  f es esencialmente acotada, luego f □ L¹ (T; E): ∫□^{t_m} □f( ‖ τ) _E dτ ≤ MW · t_m < ∞, con t_m = sup T < ∞ por la Definición 0. Paso 4.  Por el teorema fundamental de integración de Bochner, toda f □ L¹ (T; E) con E Banach admite integral de Bochner I(t) = ∫□ᵗ f(τ) dτ □ E, única como elemento de E. Existencia y unicidad de I(t) en E para todo t □ T. □

### Teorema 2.1.  Irreversibilidad de I(t)

Si w(τ) > 0 para todo τ □ T y c(τ) ≠ 0 en un conjunto de medida de Lebesgue positiva en T, entonces para todo par t□ > t□ en T con las mismas hipótesis en [t□, t□]:

Condición de irreversibilidad

□I(t□) − I(t₁) ‖_E > 0 bajo w(τ) > 0 en [t□, t□] y c(τ) ≠ 0 en conjunto de medida positiva en [t□, t□]

Demostración

Demostración del Teorema 2.1

Paso 1.  I(t□) ₁ − I(t ) = ∫_{t₁} ^{t□} c(τ)w(τ) dτ. Sea g(τ) = c(τ)w(τ). Por hipótesis: w(τ) > 0 en [t□, t□] y c(τ) ≠ 0 en un conjunto S □ [t□, t□] con μ(S) > 0. Luego g(τ) ≠ 0 en S. Paso 2.  Por la propiedad fundamental de la integral de Bochner: si g □ L¹ (T; E) y g(τ) ≠ 0 en un conjunto de medida positiva, entonces □∫ g(τ) dτ□_E > 0. Combinando: □I(t□) − I(t₁) ‖_E = □∫_{t₁} ^{t□} g(τ) dτ□_E > 0. □ Las hipótesis son necesarias: si w(τ) = 0 en algún subintervalo o c(τ) = 0 a.e., I puede ser constante en ese período —situación admisible en el marco formal.

Consecuencia para la responsabilidad.  El Teorema 2.1 establece que todo colapso no nulo producido bajo w > 0 deja

Axiomatización del Sistema de la Doble Mediación

huella permanente en I(t). El estado del sistema no puede retornar a su valor anterior por la sola acción del tiempo: solo colapsos futuros integrados pueden recontextualizar I(t), no eliminarlo. Esta permanencia es el fundamento matemático de la imputabilidad en el sistema.

### Definición 2.1.  El registro de colapsos RSC(t)

El registro de colapsos del sistema hasta t es la imagen de c en T:

Registro de colapsos

RSC(t) = {c(τ): τ □ [0, t]} ⊆ E imagen de la función de colapso en [0, t] · incluye todos los colapsos producidos por φ□ con independencia de si φ□ los integró

La relación entre RSC(t) e I(t) es la siguiente: I(t) es la integral de Bochner de los colapsos de RSC(t) que φ□ aceptó, ponderados por w. La diferencia RSC(t) \ I(t) contiene los colapsos producidos pero rechazados. El coeficiente de asunción α de la Parte IV mide la proporción ponderada de RSC(t) que está integrada en I(t).

La distinción RSC(t) / I(t) es central en la aplicación: RSC(t) corresponde a los hechos documentados del expediente —todo lo que el actor produjo— e I(t) a lo que el actor integró como propio —lo que reconoció, reparó o asumió estructuralmente. La brecha RSC(t) \ I(t) es el espacio que α mide y Δ cuantifica.

### Teorema 2.2.  Representación de φ□ y condiciones sobre eval

La segunda mediación φ□ admite la representación:

Representación de φ□

φ₂ (a, I(t)) = I(t) + δ(a) · 1_ {eval (a, I(t)) > θ} eval: A × E → ℝ función de evaluación de compatibilidad

Axiomatización del Sistema de la Doble Mediación

δ(a) □ E          modificación producida por la integración de a θ □ □             umbral de integración 1_ {···} función indicadora · vale 1 si eval (a, I(t)) > θ, 0 en caso contrario

Para que la representación esté bien definida, eval y δ deben satisfacer:

(i) Medibilidad.  eval es medible como función A × E → □ respecto a las σ-álgebras de Borel de A y E. (ii) Compatibilidad.  eval (a, I(t)) > θ si y solo si el colapso a es compatible con el estado actual I(t) en el sentido operativo del dominio. El núcleo formal no fija la noción de compatibilidad; exige que eval la codifique de forma medible y que θ sea un umbral fijo para un sistema dado. (iii) No-amplificación.  □δ(a)□_E ≤ □a□_E: la modificación que produce la integración no supera en norma al colapso que la produce. Esta condición evita singularidades en I(t) y es el primer criterio de validación de cualquier implementación de φ□.

Demostración

Demostración del Teorema 2.2

Paso 1.  El Axioma 2 establece tres etapas: evaluación, decisión binaria y actualización. La función indicadora 1_ {eval > θ} captura exactamente la decisión binaria: 1 cuando eval > θ (integración), 0 en caso contrario (rechazo). Paso 2.  El producto δ(a) · 1_ {eval > θ} es δ(a) cuando hay integración y 0 cuando hay rechazo. La suma I(t) + δ(a) · 1_ {···} produce I(t) + δ(a) en el primer caso e I(t) en el segundo. Paso 3.  Ambos resultados están en E: I(t) □ E por el Teorema 2; δ(a) □ E por la condición (iii); luego I(t) + δ(a) □ E. La representación es consistente con el codominio del Axioma 2. ✓

Axiomatización del Sistema de la Doble Mediación

La representación es válida bajo las condiciones (i)–(iii). □

Sobre la familia de funciones eval.  Las condiciones (i)–(iii) son el marco mínimo. Cualquier función eval que las satisfaga produce una φ□ bien definida y consistente con el Axioma 2. Una familia paramétrica natural es eval (a, I(t)) = □a, I(t)□_E / (□a□_E · □I(t)□_E), la similitud coseno en E: mide la alineación direccional entre el colapso y el estado acumulado, toma valores en [−1, 1], es medible y satisface la no-amplificación cuando δ(a) se define proporcionalmente. La calibración de eval para cada dominio —jurídico, clínico, de IA— pertenece a la Taxonomía y a los protocolos de Metrología Causal.

La elección de la similitud coseno como familia de referencia resuelve la crítica de arbitrariedad sobre eval planteada en la revisión externa: eval no es una caja negra, sino un espacio paramétrico de funciones con condiciones verificables. La condición (iii) en particular es inmediatamente computable y constituye el primer test de implementación.

Objeto Notación Tipo matemático

Parte

φ□ : A×E → E Función (existencia postulada)

Axioma 2

Segunda mediación

w : T → ℝ₊ Medible y acotada

Función de peso

Definición 2

I(t) = ∫□ᵗ c w dτ □ E Integral de Bochner en E

Integral acumulativa

Definición 2; Teorema 2

Teorema 2 L¹(T;E) + Bochner

### Teorema 2

Existencia y unicidad

Irreversibilidad □I(t□) ₁ ‖ −I(t ) _E > 0 Desigualdad en E

### Teorema 2.1

Axiomatización del Sistema de la Doble Mediación

Registro de colapsos

RSC(t) = {c(τ): τ□[0,t]}

Imagen de c en [0,t]

Definición 2.1

RSC(t) \ I(t) Diferencia de conjuntos

Colapsos rechazados

Definición 2.1

I(t)+δ(a)·1_{eval>θ} Suma en E con indicadora

Representación de φ□

### Teorema 2.2

eval : A×E → □ Medible; familia: cos. sim.

Función de evaluación

### Teorema 2.2

Modificación δ(a) □ E, □δ□_E ≤ □a□_E

Vector en E; no-amplificación

### Teorema 2.2

θ □ □ Parámetro escalar

### Teorema 2.2

Umbral de integración

Axiomatización del Sistema de la Doble Mediación

