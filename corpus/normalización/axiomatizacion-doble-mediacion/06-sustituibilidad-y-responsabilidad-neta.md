# Parte V. Sustituibilidad y responsabilidad neta

## 1. El objeto de \(S\)

La sustituibilidad expresa cuánto del resultado asociado a un nodo podría reproducirse si otro elemento ocupara su posición o si se mantuviera la configuración que hizo posible el resultado. La pregunta aplicada es:

> Si este nodo se reemplaza bajo las condiciones definidas, ¿con qué frecuencia o intensidad se conserva el resultado?

El motor ofrece varias operaciones para representar este objeto. Cada operación tiene entradas y una interpretación propias. Sus resultados no son intercambiables sin declarar qué estimador se utilizó.

## 2. Score aplicado de tres componentes

La operación `s_discrete` promedia tres componentes de evidencia, denominados \(A\), \(B\) y \(C\):

\[
S_{\mathrm{app}}=\frac{A+B+C}{3}.
\]

En la escala implementada, cada componente toma uno de estos valores:

\[
A,B,C\in\left\{0,\frac12,1\right\}.
\]

En la aplicación jurídica, los criterios corresponden a la formalización del procedimiento, las consecuencias de desobedecer y la proporción de pares que habría actuado igual bajo la misma configuración.

### Ejemplo ejecutado

Entrada de `s_discrete`:

```json
{"components": ["1", "1/2", "0"]}
```

Salida exacta del motor:

```json
{"numerator": 1, "denominator": 2}
```

Por tanto, el score aplicado es \(S_{\mathrm{app}}=1/2\).

## 3. Estimación por sustituciones observadas

Cuando se realizan ensayos o comparaciones de reemplazo, la operación `substitutability_probability` calcula la proporción de ensayos elegibles en los que se conservó el mismo resultado:

\[
S_{\mathrm{prob}}=
\frac{n_{\mathrm{mismo\ resultado}}}
{n_{\mathrm{ensayos\ elegibles}}}.
\]

El número de ensayos elegibles debe ser mayor que cero, y el conteo de resultados iguales debe estar entre cero y el total de ensayos.

### Ejemplo ejecutado

Entrada:

```json
{"same_result_count": 2, "eligible_trials": 4}
```

Salida del motor:

```json
{"numerator": 1, "denominator": 2}
```

En cuatro sustituciones elegibles, dos conservaron el resultado; el estimador es \(1/2\). Si tres de cuatro lo conservaran, el motor devolvería \(3/4\).

## 4. Razón entre peso causal y volitivo

La operación `s_ratio` calcula la fracción causal respecto de la suma del peso causal y el peso volitivo:

\[
S_{\mathrm{ratio}}=
\frac{w_{\mathrm{causal}}}
{w_{\mathrm{causal}}+w_{\mathrm{volitivo}}}.
\]

La suma del denominador debe ser distinta de cero. La razón requiere que ambos pesos estén expresados en escalas comparables.

### Ejemplo ejecutado

Entrada:

```json
{"causal_weight": "3", "volitional_weight": "2"}
```

Salida exacta:

```json
{"numerator": 3, "denominator": 5}
```

El resultado es \(3/5\). Esta operación compara dos pesos; no cuenta reemplazos observados ni promedia los tres criterios del score aplicado.

## 5. Intervalo de sustituibilidad

Cuando cada escenario aporta un intervalo posible de \(S\), la operación `s_interval` calcula los extremos mediante una suma ponderada. Con probabilidades \(p_j\) e intervalos \([S_{j,\min},S_{j,\max}]\):

\[
S_{\min}=\sum_j p_jS_{j,\min},
\qquad
S_{\max}=\sum_j p_jS_{j,\max}.
\]

Las listas de probabilidades e intervalos deben tener la misma longitud.

### Ejemplo ejecutado

Entrada:

```json
{
  "probabilities": ["1/4", "3/4"],
  "s_intervals": [["1/2", "3/4"], ["0", "1/4"]]
}
```

El motor devuelve exactamente:

```json
[
  {"numerator": 1, "denominator": 8},
  {"numerator": 3, "denominator": 8}
]
```

Por tanto, el intervalo ponderado es \([1/8,3/8]\).

## 6. Sensibilidad estructural implementada

El motor también implementa `s_structural`, que compara una distribución causal original \(P\) con una distribución obtenida después de sustituir un nodo, \(Q\):

\[
S_{\mathrm{structural}}
=1-\frac{D_{\mathrm{KL}}(P\|Q)}{\ln(m)},
\qquad
D_{\mathrm{KL}}(P\|Q)
=\sum_{i=1}^{m}p_i\ln\left(\frac{p_i}{q_i}\right).
\]

La operación requiere vectores de igual longitud, al menos dos componentes y valores estrictamente positivos. El motor evalúa logaritmos con aritmética decimal de alta precisión. Para la interpretación como comparación de distribuciones, las entradas se proporcionan como distribuciones normalizadas.

### Ejemplo ejecutado

Entrada:

```json
{
  "r_star": [".6", ".4"],
  "r_star_substituted": [".5", ".5"]
}
```

Salida del motor:

```text
0.97095059445466863899807606312070027060894274840910
```

La salida pertenece a esta operación estructural y no debe sustituirse por el score aplicado ni por la frecuencia de ensayos.

La fórmula implementada no impone por sí sola que el resultado esté entre cero y uno. Por ejemplo, para \(P=(0.99,0.01)\) y \(Q=(0.01,0.99)\), el motor devuelve:

\[
-5.4967694876780174267247041159289974566984031342454.
\]

Así, el resultado de esta operación se conserva tal como lo calcula el motor y se interpreta con su expresión matemática completa; no se recorta al intervalo \([0,1]\).

## 7. Qué operación elegir

| Operación del motor | Entradas | Resultado |
| --- | --- | --- |
| `s_discrete` | Tres criterios en \(\{0,1/2,1\}\) | Promedio aplicado |
| `substitutability_probability` | Reemplazos con resultado igual / ensayos elegibles | Frecuencia observada |
| `s_ratio` | Peso causal y peso volitivo comparables | Razón local |
| `s_interval` | Probabilidades de escenarios e intervalos de \(S\) | Intervalo ponderado |
| `s_structural` | Distribución original y distribución sustituida | Complemento normalizado de divergencia KL |

La elección se declara junto con el resultado. Un valor de \(1/2\) producido por el promedio de tres criterios no representa el mismo procedimiento que un valor de \(1/2\) obtenido en dos reemplazos de cuatro, aunque las salidas numéricas coincidan.

## 8. Responsabilidad neta

Una vez seleccionado y calculado el valor de \(S_i\), el motor obtiene la responsabilidad neta del nodo:

\[
R^*_{\mathrm{neta},i}=R^*_i(1-S_i).
\]

En forma vectorial, el producto se calcula componente a componente:

\[
R^*_{\mathrm{neta}}=R^*\odot(\mathbf{1}-S).
\]

La entrada de \(R^*\) y la de \(S\) deben tener la misma longitud. \(S_i\) debe corresponder al estimador elegido y al mismo nodo que \(R^*_i\).

### Ejemplo ejecutado

Para ilustrar el cálculo, se ingresan \(R^*=(2/7,5/7)\) y dos valores de sustituibilidad obtenidos con el estimador por ensayos: \(S=(1/2,3/4)\).

Entrada de `rnet`:

```json
{
  "r_star": [
    {"numerator": 2, "denominator": 7},
    {"numerator": 5, "denominator": 7}
  ],
  "s": [
    {"numerator": 1, "denominator": 2},
    {"numerator": 3, "denominator": 4}
  ]
}
```

El motor devuelve:

```json
[
  {"numerator": 1, "denominator": 7},
  {"numerator": 5, "denominator": 28}
]
```

La primera componente es \((2/7)(1-1/2)=1/7\); la segunda es \((5/7)(1-3/4)=5/28\). El vector neto conserva el orden de nodos de \(R^*\).

## 9. Registro mínimo del cálculo

Todo resultado de sustituibilidad se acompaña de:

1. nombre de la operación del motor;
2. definición de sus entradas;
3. fuente de los datos o criterios;
4. vector o escalar de salida exacto;
5. correspondencia entre cada componente de \(S\) y su nodo;
6. operación usada para obtener \(R^*_{\mathrm{neta}}\), cuando corresponda.

Este registro permite reproducir el score y distinguir una comparación de criterios de un resultado experimental o estructural.
