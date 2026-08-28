Parte IX
Modelo de Predictibilidad
Esta parte presenta el Modelo de Predictibilidad (MP): un
modelo de regresión logística que estima P(y = 1 | Ψ(t), c)
para y (cid:0) {0,1} una decisión binaria del sistema. Estatus: el MP
es un modelo estadístico, no un teorema. No postula una cota
universal del error mínimo: el error mínimo empírico se estima
en cada aplicación concreta del modelo a partir de los datos
disponibles y del valor observado de τ.
Definición 9. El estado completo Ψ(t)
El estado completo del sistema en t es:
Estado completo
Ψ(t) = (I(t), h(t), E(t), D(t), C(t))
Ψ(t) (cid:0) E × Δ(cid:0) × {1,…,6} × {1,2} × (cid:0)(E) · input del Modelo 9
Componente Espacio Contenido En sistemas artificiales
I(t) E Integral Historia de outputs
acumulativa de integrados en el contexto
colapsos
(Definición 2)
h(t) Δ(cid:0) (cid:0) Distribución sobre Distribución softmax sobre
(cid:0)(cid:0) K = {1,…,6}: outputs alternativos
vector softmax del
Lema 1.1

Axiomatización del Sistema de la Doble Mediación
E(t) {1,…,6} Nivel de No computable
integración: directamente; aproximar
fracción por métrica de coherencia
ponderada de del contexto
RSC(t) en I(t)
D(t) {1, 2} 1 = señal activa 1 = respuesta bajo
(k* = 3,4,5); 2 = parámetros nominales; 2 =
señal silenciada respuesta bajo restricción
(k* = 1,2) activa
C(t) (cid:0) E Campo de acción Conjunto de outputs
disponible en t posibles dado el prompt y
las restricciones del sistema
Para sistemas artificiales, E(t) y D(t) se aproximan según la
cuarta columna de la tabla. Cuando no son computables, el
estado simplificado Ψ_IA(t) = (I(t), h(t), C(t)) es suficiente
para el Modelo 9.
Ψ(t) hereda la imprecisión de I(t) y h(t) documentada en la REC (Parte
VII): para un observador externo con n colapsos integrados, ΔI·Δh ≥
τ(cid:0)²/n. Esto implica que Ψ(t) no es conocido con precisión arbitraria; la
Hipótesis 9.2 captura esa consecuencia en ε_min.
Definición 9.1. El vector de logits ℓ(t)
Con z_k = ((cid:0)β_k, a_t(cid:0)_E + γ_k·(cid:0)I(t)(cid:0)_E − θ_k(I(t))) / τ
del Lema 1.1, el logit del modo k es:
Logit del modo k
ℓ_k(t) = logit(h_k(t)) = log(h_k(t) / (1 − h_k(t))) ∈ ℝ
ℓ(t) = (ℓ(cid:0)(t), …, ℓ(cid:0)(t)) (cid:0) (cid:0)(cid:0) · logit es la función inversa de la sigmoide σ
Por la fórmula del Lema 1.1: ℓ_k(t) = z_k − log Σ(cid:0) exp(z_j).
El segundo término depende de a_t y c pero no de I(t). Si θ_k
es lineal en (cid:0)I(t)(cid:0)_E —Hipótesis del Lema 9.1— entonces
ℓ_k es lineal en (cid:0)I(t)(cid:0)_E, lo que habilita el modelo de
regresión logística lineal.
Modelo 9. El Modelo de Predictibilidad

Axiomatización del Sistema de la Doble Mediación
Sea y (cid:0) {0,1} una decisión binaria del sistema. El MP es:
Modelo de Predictibilidad — forma general
P(y = 1 | Ψ, c) = σ(β · Φ(Ψ, c))
σ(x) = 1/(1+e⁻ ˣ ) función sigmoide
β (cid:0) (cid:0)ᵈ vector de coeficientes (estimado por
máxima verosimilitud)
Φ : Ψ × C → (cid:0)ᵈ función de características
Estatus: modelo estadístico · β se estima sobre datos de decisiones del sistema ·
Φ se especifica por el analista
Bajo la hipótesis de umbral lineal del Lema 9.1, Φ puede
tomarse como la identidad en el espacio expandido,
produciendo el modelo lineal:
Modelo de Predictibilidad — caso lineal
P(y=1|Ψ,c) = σ(β_I·(cid:0)I(t)(cid:0)_E + β_h·h(t) + β_E·E(t) +
β_D·D(t) + β_c·c + β(cid:0))
Coeficientes β_I (cid:0) (cid:0), β_h (cid:0) (cid:0)(cid:0), β_E (cid:0) (cid:0), β_D (cid:0) (cid:0), β_c (cid:0) (cid:0)^{dim
C}, β(cid:0) (cid:0) (cid:0)
El MP tiene tres propiedades técnicas distintivas:
(i) Fundamentación. Las variables predictoras son
componentes de Ψ(t) construidas por φ(cid:0) y φ(cid:0); no
son covariables externas. Cada coeficiente tiene
interpretación en términos de los objetos formales del
sistema.
(ii) Error estimable. El MP no postula una cota
universal del error mínimo. El error mínimo empírico
se estima desde la varianza de los logits observados
bajo condiciones idénticas: cuanto mayor es τ, mayor
es la variabilidad y mayor es el error de predicción
esperado. La relación cualitativa τ ↑ → ε_min ↑ es
consecuencia del Corolario 7.2; su cuantificación
exacta es específica de cada sistema.
(iii) Coherencia con la REC. El mismo Axioma 3
(τ > 0) que funda la REC funda la variabilidad del MP.
La REC limita el autoconocimiento del sistema; el MP

Axiomatización del Sistema de la Doble Mediación
traduce esa limitación en variabilidad de predicción
desde afuera. Ambos emergen de τ sin postular una
cota funcional universal.
Lema 9.1. Linealidad en el espacio de logits bajo
umbral lineal
Si θ_k(I(t)) = a_k·(cid:0)I(t)(cid:0)_E + b_k para constantes a_k, b_k
(cid:0) (cid:0), entonces ℓ_k(t) es lineal en (cid:0)I(t)(cid:0)_E y Φ puede tomarse
como la función identidad en el espacio de características (ℓ(t),
E(t), D(t), C(t), c).
Demostración del Lema 9.1
Paso 1. Con θ_k lineal en (cid:0)I(t)(cid:0)_E: z_k = ((cid:0)β_k,
a_t(cid:0)_E + γ_k·(cid:0)I(t)(cid:0)_E − a_k·‖ I(t)‖ _E − b_k)/τ
= (γ_k − a_k)/τ · (cid:0)I(t)(cid:0)_E + ((cid:0)β_k, a_t(cid:0)_E −
b_k)/τ. El primer término es lineal en (cid:0)I(t)(cid:0)_E; el
segundo depende de a_t y c pero no de I(t). Luego
ℓ_k = z_k − log Σ(cid:0) exp(z_j) es lineal en (cid:0)I(t)(cid:0)_E.
✓
Paso 2. La decisión y puede modelarse como función
lineal de ℓ(t): Σ_k w_k ℓ_k(t) es lineal en (cid:0)I(t)(cid:0)_E,
E(t), D(t), C(t) y c por el Paso 1. ✓
Paso 3. Con Φ(Ψ, c) = (ℓ(t), E(t), D(t), C(t), c, 1), el
Modelo 9 P(y=1|Ψ,c) = σ(β·Φ) es exactamente el
modelo de regresión logística lineal. ✓
Φ = identidad en el espacio expandido bajo hipótesis de umbral lineal. (cid:0)
Si θ_k no es lineal. Φ puede ser una red neuronal con una
capa oculta (Teorema de Aproximación Universal). El modelo
sigue siendo válido independientemente de la forma de Φ.
9.3. Error empírico del MP y estimación de τ
El MP no postula una cota teórica universal del error mínimo.
El error de predicción empírico del modelo se estima desde
datos de decisiones del sistema bajo condiciones conocidas.

Axiomatización del Sistema de la Doble Mediación
La tabla siguiente muestra valores orientativos de la relación
entre τ y el error mínimo observado en sistemas con esos
valores de temperatura; no son cotas demostradas sino
referencias empíricas calibradas.
τ η(τ) = Precisión Aplicación típica
ε_min máx.
0.10 ≥ 0.045 ≤ 95.5% Temperatura baja en inferencia de
IA. Alta predictibilidad.
0.30 ≥ 0.115 ≤ 88.5% Ruido bajo. Predicción fiable para
decisiones binarias claras.
0.50 ≥ 0.167 ≤ 83.3% Temperatura estándar. Referencia
principal del MP.
0.70 ≥ 0.206 ≤ 79.4% Variabilidad moderada. Decisiones
en zonas de conflicto de modos.
1.00 ≥ 0.250 ≤ 75.0% Ruido significativo. Variabilidad
entre ejecuciones notable.
2.00 ≥ 0.333 ≤ 66.7% Ruido alto. Predicción apenas mejor
que azar en muchos contextos.
→ ∞ → 0.500 → 50.0% Temperatura infinita. Equivale a
elección uniforme sobre K.
Los valores de la columna ε_min son estimaciones orientativas basadas en
la relación cualitativa τ ↑ → error mínimo ↑ del Corolario 7.2. No son
cotas teóricas universales. Para un sistema concreto, el error mínimo empírico
se estima calculando τ(cid:0) desde la varianza de los logits observados bajo
condiciones idénticas y consultando la tabla como referencia de orden de
magnitud.
9.4. Asimetría entre perspectiva interna (REC)
y perspectiva externa (MP)
La REC y el MP son proyecciones del Axioma 3 sobre dos
perspectivas distintas. La diferencia estructural más
importante es la dependencia en n:

Axiomatización del Sistema de la Doble Mediación
Dimensión REC (Parte VII) MP (Parte IX)
Fuente τ > 0 (Axioma 3) τ > 0 (Axioma 3)
común
Objeto Producto ΔI·Δh: Error ε_min: imprecisión
acotado imprecisión del sistema del observador externo
sobre su propio estado sobre la decisión del
sistema
Perspectiva Interna: cuánto puede Externa: cuánto puede
conocer el sistema sobre sí predecirse el sistema desde
mismo afuera
Dependencia n·(ΔI·Δh) ≥ 4τ(cid:0)²: cota ε_min ≥ η(τ): cota
de n decrece con n como τ(cid:0)²/n independiente de n
Consecuencia Mayor n → menor Mayor n no reduce la
incertidumbre interna; τ_eff barrera para el observador
= τ₀ /√n → 0 externo
La asimetría tiene consecuencias directas para el análisis de
responsabilidad. El sistema con τ bajo y n alto puede
documentar mayor autoconocimiento de su posición causal
(τ_eff pequeño). Pero ese autoconocimiento no está
automáticamente disponible para el observador externo, que
sigue enfrentando la variabilidad τ del sistema.
Estimación de τ desde afuera. El observador externo
estima τ desde datos de decisiones repetidas del sistema bajo
condiciones idénticas: τ(cid:0) = varianza empírica de los logits
observados, escalada por las dimensiones del modelo. En
sistemas artificiales τ es directamente observable. Con τ(cid:0) el
observador consulta la Tabla 9.3 para estimar el orden de
magnitud del error de predicción esperado.
Objeto Notación Tipo / estatus Parte
Estado Ψ(t) = (I,h,E,D,C) Vector en Definición
completo espacio producto 9

Axiomatización del Sistema de la Doble Mediación
E(t) {1,…,6} Nivel de Definición
integración de 9
I(t)
D(t) {1,2}: Función de k*: Definición
activa/silenciada D=2 si 9
k*(cid:0){1,2}
Vector de ℓ(t) (cid:0) (cid:0)(cid:0) Transformación Definición
logits de h(t) vía logit 9.1
MP — P(y=1|Ψ,c)=σ(β·Φ) Modelo Modelo 9
general estadístico
MP — lineal σ(β_I(cid:0)I(cid:0)+β_h Bajo hipótesis de Modelo 9;
h+…) umbral lineal Lema 9.1
Hipótesis θ_k = Hipótesis de Lema 9.1
lineal a_k(cid:0)I(cid:0)+b_k trabajo; habilita
Φ=Id
Error τ(cid:0) → ε_min Referencia Sección
empírico estimado orientativa; no 9.3
cota univ.
Asimetría cota_REC (cid:0) τ(cid:0)²/n Error_MP no Sección
REC-MP ≠ error_MP decrece con n 9.4

Axiomatización del Sistema de la Doble Mediación
