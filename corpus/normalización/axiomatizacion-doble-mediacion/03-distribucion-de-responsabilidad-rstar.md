# Parte II. Distribución de responsabilidad causal \(R^*\)

## 1. Qué calcula \(R^*\)

Dado un resultado \(D\), el vector \(R^*(D)\) distribuye entre los nodos causales la contribución reconstruida respecto de ese resultado. El cálculo parte de las relaciones causales locales y compone sus efectos a través de la red.

La operación del motor se expresa en cuatro pasos:

1. identificar los nodos causales pertinentes para \(D\);
2. construir \(Q_D\), matriz de relaciones entre esos nodos, y \(b_D\), vector de relaciones directas con \(D\);
3. resolver el sistema lineal \((I-Q_D)r_D=b_D\);
4. normalizar \(r_D\) para obtener \(R^*(D)\).

En forma compacta:

\[
r_D=(I-Q_D)^{-1}b_D,
\qquad
R^*(D)=\frac{r_D}{\sum_i r_i}.
\]

La primera expresión se calcula resolviendo el sistema lineal. La implementación no necesita construir la matriz inversa.

## 2. Construcción de \(Q_D\) y \(b_D\)

Sea \(A_D\) el conjunto de nodos con un camino causal dirigido hacia \(D\). Se conserva el orden de esos nodos en las filas, columnas y vectores.

Para \(i,j\in A_D\):

\[
(Q_D)_{ij}=w_{ij}
\]

si existe una arista primitiva \(i\to j\) dentro del conjunto causal activo. Las entradas inexistentes son cero.

El vector directo se define por:

\[
(b_D)_i=w_{iD},
\]

donde \(w_{iD}\) es el peso de la relación primitiva directa de \(i\) al resultado. Si no existe esa relación, \((b_D)_i=0\).

\(Q_D\) es cuadrada, de dimensión \(n\times n\), y \(b_D\) tiene dimensión \(n\times1\). La matriz causal completa \(W\) puede incluir nodos ajenos a este resultado; el cálculo de \(R^*(D)\) opera sobre el subgrafo pertinente.

## 3. Ecuación por nodo

El sistema lineal equivale a una ecuación para cada nodo:

\[
r_i=(b_D)_i+\sum_{j=1}^{n}(Q_D)_{ij}r_j.
\]

Así, \(r_i\) combina:

- la conexión directa del nodo con \(D\);
- las conexiones del nodo con otros nodos cuya contribución al resultado ya está representada en el sistema.

La ecuación se resuelve simultáneamente para todos los nodos. No se calcula una ronda aislada ni se normaliza cada paso intermedio.

## 4. Ejemplo completo: una rama pertinente y una rama ajena al resultado

Considérese la matriz completa con nodos en el orden \((D_1,E,C,Y)\):

\[
W=
\begin{pmatrix}
0&0.4&0.6&0\\
0&0&0&1\\
0&0&1&0\\
0&0&0&0
\end{pmatrix}.
\]

\(Y\) es el resultado analizado. \(D_1\) influye en \(E\) y en \(C\); \(E\) influye directamente en \(Y\); \(C\) permanece en un circuito que no conduce a \(Y\). Cada fila no terminal suma uno y la fila terminal suma cero.

Para calcular la responsabilidad respecto de \(Y\), se conservan los nodos que tienen camino hacia \(Y\): \(D_1\) y \(E\). El nodo \(C\) no pertenece al conjunto activo de este resultado. En el orden \((D_1,E)\):

\[
Q_Y=
\begin{pmatrix}
0&0.4\\
0&0
\end{pmatrix},
\qquad
b_Y=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
\]

El sistema es:

\[
(I-Q_Y)r_Y=b_Y,
\]

\[
\begin{pmatrix}
1&-0.4\\
0&1
\end{pmatrix}
\begin{pmatrix}
r_{D_1}\\
r_E
\end{pmatrix}
=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
\]

De la segunda fila:

\[
r_E=1.
\]

De la primera:

\[
r_{D_1}-0.4r_E=0,
\qquad
r_{D_1}=0.4.
\]

Por tanto:

\[
r_Y=
\begin{pmatrix}
0.4\\
1
\end{pmatrix},
\qquad
\sum_i r_i=1.4.
\]

La normalización se realiza una vez, al final:

\[
R^*(Y)=
\begin{pmatrix}
0.4/1.4\\
1/1.4
\end{pmatrix}
=
\begin{pmatrix}
2/7\\
5/7
\end{pmatrix}
\approx
\begin{pmatrix}
0.2857\\
0.7143
\end{pmatrix}.
\]

El resultado asigna aproximadamente \(28.57\%\) a \(D_1\) y \(71.43\%\) a \(E\) para la estructura representada. El nodo \(C\) no recibe componente en este cálculo porque no tiene camino causal hacia \(Y\).

## 5. Por qué se restringe el cálculo al resultado

La responsabilidad es relativa a un resultado especificado. Una misma red puede producir vectores distintos para resultados distintos, porque cambia el conjunto de nodos que tiene camino hacia cada resultado y cambian sus conexiones directas.

La restricción a \(A_D\) evita incluir nodos que no contribuyen al resultado analizado. Las relaciones hacia nodos excluidos no se convierten en relaciones hacia \(D\); simplemente quedan fuera de \(Q_D\) y \(b_D\).

## 6. Normalización final

Una vez resuelto \(r_D\), sea:

\[
Z_D=\sum_{i=1}^{n}r_i.
\]

Si \(Z_D\ne0\), cada componente normalizado es:

\[
R^*_i(D)=\frac{r_i}{Z_D}.
\]

Por construcción:

\[
\sum_{i=1}^{n}R^*_i(D)=1.
\]

La normalización convierte las contribuciones reconstruidas en proporciones comparables entre nodos. Se hace después de resolver el sistema; no se normalizan las filas de la solución ni cada iteración.

## 7. Resolución por eliminación gaussiana

El motor resuelve \((I-Q_D)r_D=b_D\) mediante eliminación gaussiana. Para el ejemplo anterior, la matriz aumentada es:

\[
\left[
\begin{array}{cc|c}
1&-0.4&0\\
0&1&1
\end{array}
\right].
\]

Se despeja desde la última fila y se sustituyen los valores hacia arriba:

\[
r_E=1,
\qquad
r_{D_1}=0.4r_E=0.4.
\]

La implementación conserva fracciones exactas cuando las entradas se proporcionan como enteros, fracciones o cadenas decimales. Por ejemplo, \(0.4\) se puede ingresar como \(2/5\); el resultado intermedio permanece exacto hasta su presentación decimal.

## 8. Existencia de solución y unicidad

El sistema tiene una solución única cuando \(I-Q_D\) es invertible. Si la matriz es singular, el motor detiene el cálculo e informa que no existe una solución única para las entradas proporcionadas.

Una vez obtenida la solución, la normalización requiere \(Z_D\ne0\). Si la suma es cero, no se puede formar el vector normalizado.

Estas comprobaciones son parte del cálculo: las dimensiones de \(Q_D\) deben coincidir con \(b_D\), \(Q_D\) debe ser cuadrada y las entradas deben ser valores numéricos válidos.

## 9. Rutas y ciclos

Al desarrollar la ecuación por sustitución sucesiva aparecen contribuciones directas y contribuciones transmitidas por rutas. Cuando la serie de potencias converge, la solución también puede escribirse:

\[
r_D=b_D+Q_Db_D+Q_D^2b_D+Q_D^3b_D+\cdots.
\]

Cada producto matricial incorpora una longitud adicional de ruta. Esta expansión ofrece una lectura de la propagación causal; el cálculo operativo del motor resuelve el sistema lineal directamente.

Si la red contiene ciclos, su efecto queda representado en \(Q_D\). La condición computacional que aplica el motor es la invertibilidad de \(I-Q_D\): si es singular, no devuelve un vector único. La expansión infinita anterior, cuando se use como interpretación de rutas, requiere además que converja.

## 10. Distinciones entre magnitudes

No se deben confundir estos objetos:

| Objeto | Qué contiene |
| --- | --- |
| \(W\) | Pesos de relaciones locales entre nodos de la representación. |
| \(Q_D\) | Relaciones entre los nodos activos para el resultado \(D\). |
| \(b_D\) | Relaciones directas de los nodos activos con \(D\). |
| \(r_D\) | Contribuciones obtenidas al resolver el sistema lineal. |
| \(R^*(D)\) | Vector \(r_D\) normalizado para sumar uno. |

\(R^*\) es independiente de \(\alpha\). La asunción se incorpora después, al calcular el déficit:

\[
\Delta=R^*-\alpha.
\]

## 11. Procedimiento reproducible

Para ejecutar el cálculo:

1. fija el resultado \(D\);
2. identifica los nodos con camino causal hacia \(D\);
3. construye \(Q_D\) y \(b_D\) con el mismo orden de nodos;
4. comprueba dimensiones y valores de entrada;
5. resuelve \((I-Q_D)r_D=b_D\);
6. verifica que el sistema tenga solución única;
7. calcula \(Z_D=\sum_i r_i\);
8. si \(Z_D\ne0\), divide cada componente de \(r_D\) entre \(Z_D\);
9. verifica que las componentes de \(R^*\) sumen uno.

El informe del cálculo conserva \(Q_D\), \(b_D\), las operaciones de resolución, \(r_D\), \(Z_D\) y \(R^*\). Así puede revisarse tanto la representación inicial como cada transformación posterior.


## 12. Comprobación con el motor Prometeo

La entrada exacta del ejemplo anterior se ejecutó con la fórmula `rstar` de `prometeo-motor-calculo/motor.py`:

```json
{
  "q_d": [["0", "2/5"], ["0", "0"]],
  "b_d": ["0", "1"]
}
```

El motor devolvió:

```json
[
  {"numerator": 2, "denominator": 7},
  {"numerator": 5, "denominator": 7}
]
```

El vector es \((2/7,5/7)\). La traza del motor conserva la eliminación gaussiana, el vector previo a la normalización \((2/5,1)\) y la suma de normalización \(7/5\).
