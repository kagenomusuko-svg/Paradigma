Parte IV
El coeficiente de asunción α
Definición 4. Coeficiente de asunción — versión
continua
Sea w: T → ℝ₊ la función de peso de la Definición 2 y sea p:
T → [0,1] una función de profundidad de integración medible.
El coeficiente de asunción del sistema en t es:
Coeficiente de asunción — versión continua
α(t) = ∫(cid:0)ᵗ 1_{int}(τ) · w(τ) · p(τ) dτ / ∫(cid:0)ᵗ w(τ) dτ
1_{int}(τ) = 1 si c(τ) (cid:0) I(t) (φ(cid:0) integró el colapso)
1_{int}(τ) = 0 si c(τ) (cid:0) RSC(t)\I(t) (φ(cid:0) rechazó el colapso)
p: T → [0,1] medible · p(τ) = 0 para colapsos rechazados · p(τ) > 0 para
colapsos integrados · w la misma función de la Definición 2
El denominador ∫(cid:0)ᵗ w(τ) dτ > 0 bajo w > 0, lo que garantiza
que α(t) esté bien definido. La función p(τ) es el único
elemento que requiere calibración por dominio; el núcleo
formal solo exige p: T → [0,1] con p medible.
La función indicadora 1_{int} opera sobre la distinción RSC(t) / I(t) de
la Definición 2.1: RSC(t) registra todos los colapsos producidos; I(t) solo los
integrados. α(t) mide qué fracción de RSC(t), ponderada por w y p, reside en
I(t). Es la proporción de lo producido que el sistema asumió, no la magnitud
absoluta de lo asumido.

Axiomatización del Sistema de la Doble Mediación
Definición 4.1. Coeficiente de asunción —
versión discreta
Sean {t(cid:0), …, t(cid:0)} (cid:0) T momentos discretos de colapso y sea
w(τ) = Σᵢ δ (τ − tᵢ) la función de peso correspondiente, con δ
la delta de Dirac. Para un colapso aᵢ producido en tᵢ:
Coeficiente de asunción — versión discreta
α(aᵢ) = p_pres · f(τᵢ) · g(τᵢ)
p_pres (cid:0) {0,1}: 1 si aᵢ (cid:0) I(t), 0 si aᵢ (cid:0) RSC(t)\I(t)
f(τᵢ) (cid:0) [0,1]: profundidad de integración en τᵢ (ver Tabla
4.1)
g(τᵢ) (cid:0) [0,1]: alcance de la integración en τᵢ (ver Tabla 4.1)
La versión discreta es el caso particular de la Definición 4 con w(τ) = δ(τ−tᵢ) —
demostrado en la Proposición 4.1
Proposición 4.1 — Derivación desde la versión continua
Proposición 4.1
Paso 1. Con w(τ) = δ(τ−tᵢ), el numerador es ∫(cid:0)ᵗ
1_{int}(τ)·δ(τ−tᵢ) ·p(τ) dτ = 1_{int}(tᵢ)·p(tᵢ) por la
propiedad de muestreo de la delta de Dirac.
Paso 2. El denominador es ∫(cid:0)ᵗ δ(τ−tᵢ) dτ = 1 por la
misma propiedad.
Paso 3. Luego α(aᵢ) = 1_{int}(tᵢ)·p(tᵢ) = p_pres ·
p(tᵢ). La función de profundidad puntual p(tᵢ) se
descompone en el producto f(τᵢ) ·g(τᵢ), donde f
captura el tipo de integración y g su extensión —
ambos definidos en la Tabla 4.1.
La versión discreta es la continua evaluada con w = δ(τ−tᵢ): no son dos
definiciones independientes. (cid:0)
Tabla 4.1 — Funciones f y g: variables observables y
niveles de referencia

Axiomatización del Sistema de la Doble Mediación
Parámetro Variable Función Niveles de n_ref / n_I
observable continua referencia anclados a
subyacente E0–E8
f n_doc(τ) = f(τ) = f ≈ 0.3: E1–E2
(profundidad) número de min(1, n_doc/n_ref (declaración):
documentos n_doc(τ) (cid:0) [0.1, 0.4] f n_ref = 1–2
del / n_ref) ≈ 0.6: E3–E4
expediente n_ref = n_doc/n_ref (documental
que umbral (cid:0) [0.4, 0.8] f básico): n_ref
confirman la derivado ≈ 1.0: = 3–5 E5–E6
integración del nivel n_doc/n_ref (documental
del colapso de (cid:0) [0.8, 1.0] robusto): n_ref
c(τ). evidencia = 6–10 E7–E8
(prueba plena):
n_ref = 11+
n_ref se fija al
inicio del
análisis según el
estándar de
evidencia
declarado para
el dominio.
g (alcance) n_dom(τ) = g(τ) = g ≈ 0.3: n_I = número
número de n_dom(τ) n_dom/n_I de dominios
dominios de / n_I (cid:0) [0.0, 0.4] g identificados en
I(t) ≈ 0.6: I(t) mediante
afectados n_dom/n_I SDO o
por la (cid:0) [0.4, 0.8] g protocolo
integración ≈ 1.0: equivalente
de c(τ), con n_dom/n_I antes del
n_I el total (cid:0) [0.8, 1.0] análisis. No
de dominios varía entre
de I(t). analistas dado
el mismo
expediente y el
mismo
protocolo
SDO.
Las funciones f y g son continuas en sus variables observables
subyacentes n_doc y n_dom. Los tres niveles de referencia
{0.3, 0.6, 1.0} son cuantiles para el uso operativo cuando los
conteos exactos no están disponibles, no valores discretos
intrínsecos. El parámetro n_ref en f ya no es un parámetro
libre: queda fijado por el nivel de evidencia E0–E8 declarado
para el dominio de análisis, según la última columna de la

Axiomatización del Sistema de la Doble Mediación
Tabla 4.1. Dos analistas que apliquen el mismo nivel de
evidencia sobre el mismo expediente obtendrán el mismo
n_ref y, por tanto, valores de f comparables entre sí.
El anclaje de n_ref a la escala E0–E8 resuelve la variabilidad entre
analistas que surgía cuando n_ref era un parámetro libre. El nivel de
evidencia requerido para el dominio se declara antes del análisis —por
protocolo o por acuerdo de las partes— y n_ref se deriva directamente de esa
declaración. En casos jurídicos el estándar probatorio del juicio determina el
nivel E; en sistemas artificiales el protocolo de evaluación determina el número
mínimo de registros. Ambos son externos al analista que aplica el sistema.
El coeficiente de asunción agregado para un conjunto de
colapsos A_D (cid:0) RSC(t) es:
Coeficiente de asunción agregado
α_D(t) = (1/|A_D|) · Σ_ {aᵢ (cid:0) A_D ∩ I(t)} α(aᵢ)
A_D conjunto de colapsos del dominio D · A_D ∩ I(t) colapsos de A_D
integrados · si A_D ∩ I(t) = (cid:0) entonces α_D(t) = 0
Teorema 4. α(t) (cid:0) [0, 1] por construcción
Para toda c: T → E admisible, toda w: T → ℝ₊ medible y
acotada con ∫w > 0, y toda p: T → [0,1] medible:
Acotación de α
α(t) (cid:0) [0, 1] para todo t (cid:0) T
Demostración
Demostración del Teorema 4
α(t) ≥ 0. Numerador: 1_{int} (cid:0) {0,1} ≥ 0, w (cid:0) ℝ₊
≥ 0, p (cid:0) [0,1] ≥ 0. El producto de tres factores no
negativos es no negativo; su integral también.
Denominador: ∫(cid:0)ᵗ w(τ) dτ > 0 por hipótesis. Razón
de no negativo sobre positivo: α(t) ≥ 0. ✓
α(t) ≤ 1. Para todo τ (cid:0) T: 1_{int}(τ) · p(τ) ≤ 1
(producto de factores en [0,1]). Multiplicando por

Axiomatización del Sistema de la Doble Mediación
w(τ) ≥ 0: 1_{int}(τ)·w(τ)·p(τ) ≤ w(τ). Integrando: ∫(cid:0)ᵗ
1_{int}·w·p dτ ≤ ∫(cid:0)ᵗ w dτ. Dividiendo por el
denominador positivo: α(t) ≤ 1. ✓
Casos extremos. α(t) = 1 (cid:0) 1_{int}(τ)·p(τ) = 1 para
w-casi todo τ: todos los colapsos integrados con p =
1. α(t) = 0 (cid:0) 1_{int}(τ)·p(τ) = 0 para w-casi todo τ:
ningún colapso integrado o todos con p = 0.
α(t) (cid:0) [0,1] sin restricciones adicionales sobre c, w o p más allá de las ya
establecidas. (cid:0)
Corolario 4.1 — Independencia de α respecto al dolo. α(t)
está definido exclusivamente en términos de acciones
observables posteriores al colapso —lo que φ(cid:0) integró en I(t),
medido por 1_{int}, w y p— y no en términos de la intención
con que φ(cid:0) produjo el colapso. En consecuencia, el valor de
α(t) es invariante bajo cualquier descripción de la intención del
sistema en τ: el dolo, la culpa o la ausencia de ambos no alteran
1_{int}(τ), w(τ) ni p(τ).
Esta independencia tiene dos consecuencias operativas.
Primera: α es compatible con la definición de S —que captura
el estado de la voluntad a través de k*(v_t)— sin
contradicción: S informa sobre el determinismo del acto en
φ(cid:0); α informa sobre la asunción efectiva en φ(cid:0). Son medidas
de objetos distintos. Segunda: α puede crecer por asunción
voluntaria, forzada o impuesta; el efecto sobre el déficit Δ =
R* − α es idéntico en los tres casos.
La invariancia de α respecto al dolo distingue el sistema de los sistemas de
imputación jurídica clásicos, que anclan la responsabilidad en la intención.
El sistema no niega que la intención sea relevante para el derecho:
simplemente la coloca en un objeto distinto —el modo k* del Lema 1.1—
y no en α. La compatibilidad formal entre ambos objetos es consecuencia de
su independencia matemática.

Axiomatización del Sistema de la Doble Mediación
Objeto Notación Tipo Parte
matemático
Coeficiente de α(t) (cid:0) [0,1] Integral de Definición
asun. Lebesgue 4
normalizada
Función de p : T → [0,1] Medible; Definición
profund. requiere 4
calibración
Versión α(aᵢ) = p_pres·f·g Caso δ(τ−tᵢ) de Definición
discreta la Definición 4 4.1; Prop.
4.1
Profundidad f f(τ) = Función Tabla 4.1
min(1,n_doc/n_ref) continua en
n_doc (cid:0) (cid:0)
Alcance g g(τ) = n_dom/n_I Función Tabla 4.1
continua en
n_dom (cid:0) (cid:0)
Asunción α_D = Media aritmética Definición
agregada (1/|A_D|)Σα(aᵢ) sobre A_D∩I(t) 4.1
Acotación Teorema 4 α (cid:0) [0,1] sin Teorema
hipótesis extra 4
Indep. del Corolario 4.1 α invariante bajo Corolario
dolo descripción de 4.1
φ(cid:0)

Axiomatización del Sistema de la Doble Mediación
