# Parte II. Distribución de responsabilidad causal \(R^*\)

## 1. Qué calcula \(R^*\)

Dado un resultado \(D\), el vector \(R^*(D)\) distribuye entre los nodos causales la contribución reconstruida respecto de ese resultado. El cálculo compone las relaciones locales a través de la red y normaliza las contribuciones al final.

La secuencia es:

1. identificar los nodos con camino causal hacia \(D\);
2. construir \(Q_D\), matriz de relaciones entre esos nodos, y \(b_D\), vector de relaciones directas con \(D\);
3. resolver el sistema lineal \((I-Q_D)r_D=b_D\);
4. dividir cada componente de \(r_D\) entre la suma de sus componentes.

En forma compacta:

\[
r_D=(I-Q_D)^{-1}b_D,
\qquad
R^*(D)=\frac{r_D}{\sum_i r_i}.
\]

La inversa es una forma de escribir la solución del sistema. En los cálculos desarrollados se despejan las incógnitas mediante operaciones matriciales.

## 2. Construcción de \(Q_D\) y \(b_D\)

Sea \(A_D\) el conjunto de nodos que tienen un camino dirigido hacia \(D\). Se conserva el mismo orden de estos nodos en las filas, las columnas y los vectores.

Para \(i,j\in A_D\):

\[
(Q_D)_{ij}=w_{ij}
\]

si existe una arista primitiva \(i\to j\) entre nodos activos. Si no existe esa arista, la entrada es cero.

El vector directo se define mediante:

\[
(b_D)_i=w_{iD},
\]

donde \(w_{iD}\) es el peso de la relación directa de \(i\) con el resultado. Si no existe esa relación, \((b_D)_i=0\).

Con \(n\) nodos activos, \(Q_D\) tiene dimensión \(n\times n\) y \(b_D\) dimensión \(n\times1\).

## 3. Ecuación por nodo

El sistema matricial equivale a una ecuación para cada nodo:

\[
r_i=(b_D)_i+\sum_{j=1}^{n}(Q_D)_{ij}r_j.
\]

Cada \(r_i\) reúne la relación directa del nodo con \(D\) y las contribuciones transmitidas por los nodos con los que se conecta. Las ecuaciones se resuelven simultáneamente.

## 4. Ejemplo: selección del subgrafo pertinente

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

\(Y\) es el resultado analizado. \(D_1\) influye en \(E\) y en \(C\); \(E\) influye directamente en \(Y\); \(C\) permanece en un circuito que no conduce a \(Y\). Las filas de los nodos no terminales suman uno y la fila de \(Y\) suma cero.

Para calcular la responsabilidad respecto de \(Y\), se conservan los nodos que tienen camino hacia ese resultado: \(D_1\) y \(E\). En el orden \((D_1,E)\):

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

El nodo \(C\) no forma parte de este cálculo porque no tiene camino hacia \(Y\).

## 5. Resolución del sistema lineal

Se plantea:

\[
(I-Q_Y)r_Y=b_Y.
\]

Al restar \(Q_Y\) de la matriz identidad:

\[
I-Q_Y=
\begin{pmatrix}
1&-0.4\\
0&1
\end{pmatrix}.
\]

El sistema aumentado es:

\[
\left[
\begin{array}{cc|c}
1&-0.4&0\\
0&1&1
\end{array}
\right].
\]

La segunda fila da:

\[
r_E=1.
\]

La primera fila representa:

\[
r_{D_1}-0.4r_E=0.
\]

Sustituyendo \(r_E=1\):

\[
r_{D_1}=0.4.
\]

Por tanto, antes de normalizar:

\[
r_Y=
\begin{pmatrix}
0.4\\
1
\end{pmatrix}
=
\begin{pmatrix}
2/5\\
1
\end{pmatrix}.
\]

## 6. Normalización final

Se suman las contribuciones obtenidas:

\[
Z_Y=\frac25+1=\frac75.
\]

Cada componente se divide entre \(Z_Y\):

\[
R^*_{D_1}(Y)=\frac{2/5}{7/5}=\frac27,
\qquad
R^*_E(Y)=\frac{1}{7/5}=\frac57.
\]

Así:

\[
R^*(Y)=
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

La comprobación de la normalización es:

\[
\frac27+\frac57=1.
\]

En la estructura representada, \(D_1\) recibe \(2/7\) y \(E\) recibe \(5/7\) de la distribución causal relativa a \(Y\).

## 7. Existencia y unicidad

El sistema tiene solución única cuando \(I-Q_D\) es invertible. Si es singular, las ecuaciones no determinan un único vector \(r_D\).

Una vez obtenido \(r_D\), la normalización requiere que:

\[
Z_D=\sum_i r_i\ne0.
\]

Si \(Z_D=0\), no existe un vector normalizado por esta fórmula. Las dimensiones también deben coincidir: \(Q_D\) debe ser cuadrada y su dimensión debe igualar la longitud de \(b_D\).

## 8. Lectura por rutas

Al sustituir reiteradamente la ecuación por nodo, aparecen las contribuciones directas y las transmitidas por rutas:

\[
r_D=b_D+Q_Db_D+Q_D^2b_D+Q_D^3b_D+\cdots
\]

cuando esta serie converge. \(b_D\) recoge las relaciones directas con el resultado; cada producto adicional por \(Q_D\) incorpora otro tramo causal.

La expresión por rutas ayuda a interpretar la solución. Para obtener el resultado se resuelve el sistema lineal y se normaliza una sola vez al final.

Si existen ciclos, sus relaciones quedan incluidas en \(Q_D\). La solución única depende de que \(I-Q_D\) sea invertible; la expansión en serie requiere además que la serie converja.

## 9. Distinción entre los objetos

| Objeto | Qué representa |
| --- | --- |
| \(W\) | Pesos de las relaciones locales de la representación completa. |
| \(Q_D\) | Relaciones entre los nodos activos respecto del resultado \(D\). |
| \(b_D\) | Relaciones directas de esos nodos con \(D\). |
| \(r_D\) | Contribuciones obtenidas al resolver el sistema lineal. |
| \(R^*(D)\) | Vector \(r_D\) dividido entre la suma de sus componentes. |

\(R^*\) se calcula antes de \(\alpha\). La comparación entre causalidad y asunción se desarrolla mediante:

\[
\Delta=R^*-\alpha.
\]

## 10. Procedimiento de cálculo

1. Fija el resultado \(D\).
2. Identifica todos los nodos con camino dirigido hacia \(D\).
3. Declara el orden de esos nodos.
4. Construye \(Q_D\) y \(b_D\).
5. Forma \(I-Q_D\).
6. Resuelve \((I-Q_D)r_D=b_D\) mediante eliminación o sustitución.
7. Suma las componentes de \(r_D\).
8. Divide cada componente entre esa suma.
9. Comprueba que las componentes de \(R^*\) sumen uno.

El desarrollo conserva las ecuaciones, los despejes, los valores intermedios y la normalización, de modo que cada componente pueda revisarse desde las entradas originales.
