# Parte IV. Déficit de asunción e índice de justicia

## 1. Déficit por nodo

El déficit de asunción compara la distribución causal con la distribución de asunción registrada. Para cada nodo \(i\):

\[
\Delta_i=R^*_i-\alpha_i.
\]

La resta se realiza entrada por entrada, conservando el orden de los nodos. El signo describe la relación entre ambas magnitudes:

- \(\Delta_i>0\): la contribución causal supera la asunción registrada;
- \(\Delta_i=0\): ambas magnitudes coinciden;
- \(\Delta_i<0\): la asunción registrada supera la contribución causal.

El motor calcula esta operación como una resta directa. No multiplica \(R^*\) por \((1-\alpha)\).

## 2. Ejemplo exacto con el motor

Se usan los vectores calculados en los capítulos anteriores:

\[
R^*=
\left(\frac{2}{7},\frac{5}{7}\right),
\qquad
\alpha=
\left(\frac{31}{60},\frac{3}{4}\right).
\]

La entrada de la fórmula `delta` en `prometeo-motor-calculo/motor.py` es:

```json
{
  "r_star": [
    {"numerator": 2, "denominator": 7},
    {"numerator": 5, "denominator": 7}
  ],
  "alpha": [
    {"numerator": 31, "denominator": 60},
    {"numerator": 3, "denominator": 4}
  ]
}
```

El motor devuelve exactamente:

```json
[
  {"numerator": -97, "denominator": 420},
  {"numerator": -1, "denominator": 28}
]
```

Por tanto:

\[
\Delta=
\left(-\frac{97}{420},-\frac{1}{28}\right)
\approx(-0.2310,-0.0357).
\]

Ambos componentes son negativos. El primer nodo registra una asunción mayor que su participación causal; el segundo también, con una diferencia de menor magnitud. La traza conserva cada resta como fracción exacta.

## 3. Índice de justicia estructural

Para comparar el conjunto de diferencias, el motor calcula:

\[
J=1-\sum_{i=1}^{n}|R^*_i-\alpha_i|
=1-\sum_{i=1}^{n}|\Delta_i|.
\]

El índice resume la distancia absoluta entre los vectores. Si cada componente coincide, la suma de diferencias absolutas es cero y \(J=1\). Al aumentar la distancia entre causalidad y asunción, \(J\) disminuye.

Cuando \(R^*\) y \(\alpha\) tienen \(n\) componentes en \([0,1]\), el rango algebraico es \(1-n\leq J\leq1\). Un resultado negativo indica que la suma de las diferencias absolutas supera uno. La denominación del índice no convierte por sí misma el número en una sentencia jurídica ni moral: expresa proporcionalidad entre los vectores de entrada.

## 4. Cálculo de \(J\) con el mismo caso

Se ingresan los mismos vectores a la fórmula `justice`:

```json
{
  "r_star": [
    {"numerator": 2, "denominator": 7},
    {"numerator": 5, "denominator": 7}
  ],
  "alpha": [
    {"numerator": 31, "denominator": 60},
    {"numerator": 3, "denominator": 4}
  ]
}
```

El motor calcula las diferencias, toma sus valores absolutos y devuelve:

```json
{"numerator": 11, "denominator": 15}
```

La traza exacta del cálculo es:

\[
|\Delta_1|+|\Delta_2|
=\frac{97}{420}+\frac{1}{28}
=\frac{4}{15},
\]

\[
J=1-\frac{4}{15}=\frac{11}{15}
\approx0.7333.
\]

El valor \(11/15\) corresponde exclusivamente a los dos vectores ingresados. Si cambia \(R^*\), \(\alpha\), el conjunto de nodos o la escala de comparación, también puede cambiar \(J\).

## 5. Procedimiento reproducible

Para calcular ambas magnitudes:

1. verifica que \(R^*\) y \(\alpha\) tengan la misma longitud y orden;
2. ejecuta `delta` para obtener \(\Delta_i=R^*_i-\alpha_i\);
3. ejecuta `justice` para calcular \(1-\sum_i|\Delta_i|\);
4. conserva las entradas racionales y las trazas devueltas;
5. interpreta primero cada componente de \(\Delta\) y luego el resumen \(J\).

El motor exige longitudes iguales para las operaciones vectoriales. La fórmula `justice` devuelve un único escalar; la fórmula `delta` conserva un resultado por nodo.
