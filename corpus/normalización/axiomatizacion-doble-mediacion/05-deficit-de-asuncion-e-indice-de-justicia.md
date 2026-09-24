# Parte IV. Déficit de asunción e índice de justicia

## 1. Déficit por nodo

El déficit de asunción compara la distribución causal con la distribución de asunción registrada. Para cada nodo \(i\):

\[
\Delta_i=R^*_i-\alpha_i.
\]

La resta se efectúa componente a componente, conservando el mismo orden de nodos.

- Si \(\Delta_i>0\), la contribución causal supera la asunción registrada.
- Si \(\Delta_i=0\), ambas magnitudes coinciden.
- Si \(\Delta_i<0\), la asunción registrada supera la contribución causal.

## 2. Cálculo desarrollado

Tomemos:

\[
R^*=\left(\frac27,\frac57\right),
\qquad
\alpha=\left(\frac{31}{60},\frac34\right).
\]

Para el primer nodo, el mínimo común denominador de \(7\) y \(60\) es \(420\):

\[
\frac27=\frac{120}{420},
\qquad
\frac{31}{60}=\frac{217}{420}.
\]

Entonces:

\[
\Delta_1
=\frac{120}{420}-\frac{217}{420}
=-\frac{97}{420}
\approx-0.2310.
\]

Para el segundo nodo, el mínimo común denominador de \(7\) y \(4\) es \(28\):

\[
\frac57=\frac{20}{28},
\qquad
\frac34=\frac{21}{28}.
\]

Entonces:

\[
\Delta_2
=\frac{20}{28}-\frac{21}{28}
=-\frac1{28}
\approx-0.0357.
\]

El vector resultante es:

\[
\Delta=\left(-\frac{97}{420},-\frac1{28}\right).
\]

Ambos valores son negativos: en las magnitudes registradas, ambos nodos asumieron una proporción mayor que su participación causal. El primero presenta una diferencia de mayor magnitud.

## 3. Índice de justicia estructural

El índice resume la distancia absoluta entre los vectores:

\[
J=1-\sum_{i=1}^{n}|R^*_i-\alpha_i|
=1-\sum_{i=1}^{n}|\Delta_i|.
\]

Si todos los componentes coinciden, cada diferencia es cero y \(J=1\). Conforme aumenta la distancia total entre causalidad y asunción, \(J\) disminuye.

Para vectores con \(n\) componentes en \([0,1]\), cada diferencia absoluta es como máximo uno; por ello:

\[
1-n\leq J\leq1.
\]

Un valor negativo indica que la suma de las diferencias absolutas es mayor que uno. El índice describe proporcionalidad entre los vectores: su nombre no constituye por sí mismo un dictamen jurídico o moral.

## 4. Cálculo de \(J\) para el mismo caso

Se suman los valores absolutos de las diferencias:

\[
|\Delta_1|+|\Delta_2|
=\frac{97}{420}+\frac1{28}.
\]

Se expresa \(1/28\) con denominador \(420\):

\[
\frac1{28}=\frac{15}{420}.
\]

Por tanto:

\[
|\Delta_1|+|\Delta_2|
=\frac{97}{420}+\frac{15}{420}
=\frac{112}{420}
=\frac4{15}.
\]

Se resta esta distancia de uno:

\[
J=1-\frac4{15}
=\frac{15}{15}-\frac4{15}
=\frac{11}{15}
\approx0.7333.
\]

El resultado corresponde a los dos vectores utilizados. Si cambia \(R^*\), \(\alpha\), el conjunto de nodos o la escala de comparación, también puede cambiar \(J\).

## 5. Procedimiento de cálculo

1. Comprueba que \(R^*\) y \(\alpha\) tengan el mismo número y orden de componentes.
2. Calcula cada \(\Delta_i=R^*_i-\alpha_i\).
3. Conserva el signo de cada diferencia para interpretar su dirección.
4. Toma el valor absoluto de cada diferencia.
5. Suma los valores absolutos.
6. Resta esa suma de uno para obtener \(J\).

Primero se interpreta el vector \(\Delta\), que conserva la información por nodo; después se interpreta \(J\), que resume la distancia total.
