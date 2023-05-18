# Teoría De Algortimos I

### Alumnos

- Martina Victoria Lozano: 106267
- Martin Ugarte: 107870

## Primera Parte: *K-merge*

**Aclaración**: Definimos $k$ como la cantidad de arreglos ordenados, y $h$ como la cantidad de elementos en cada arreglo. La cantidad de elementos total por lo tanto es $n = k * h$

> 1. Determinar, utilizando el Teorema Maestro, cuál sería la complejidad del algoritmo propuesto

La fórmula del Teorema Maestro está dada por

$$T(n)=A*T(\frac{n}{B}) + O(n^c)$$

Donde $A$ representa la cantidad de llamados recursivos, $B$ la proporción del tamaño original de la lista con el que llamamos recursivamente y $O(n^c)$ el costo de las operaciones que no son llamadas recursivas.

En este caso, tenemos dos llamadas recursivas, el arreglo es partido a la mitad por cada uno de estos llamados, y el costo de las demás operaciones son en total $O(n)$ ya que el costo de mergear dos arreglos es $O(n + m) = O(n)$ sabiendo que $n$ y $m$ son las longitudes de cada arreglo “parcial” donde $m$ es la mayor, con lo cual se puede despreciar m como una constante.

Por lo cual, $A = 2$, $B = 2$ y $C = 1$.

Luego, $\log_B(A) = \log_2(2) = 1$

Según el Teorema Maestro, como $logB(A)=C=1$, entonces la complejidad del algoritmo propuesto es $O(n^c \log n)=O(n \log n)$, donde $n$ es la cantidad total de elementos, es decir, $k * h$.

> 2. Describir el algoritmo que utiliza heaps, y determinar su complejidad.

Se tiene el conjunto de arreglos, el heap y un arreglo vacío. En el heap se encolan los primeros datos de cada arreglo de la forma (dato, número_arreglo). Luego, mientras que el heap no esté vacío, se desencola del heap y se agrega el valor en el arreglo solucion. Posteriormente se guarda el siguiente elemento del arreglo al que pertenecía el dato guardado, y de haber ya analizado todo el arreglo no se hace nada. Se continúa así hasta que no queda ningún dato en el heap, y se devuelve el arreglo solucion.

Dado que se crea un heap de tamaño $k$, se insertan los primeros elementos de cada uno de los $k$ lo cual tiene una complejidad de $O(klogk)$ arreglos ordenados en el heap y luego se itera extrayendo un elemento ( $O(1)$ ), e insertando otro ( $O(\log k)$ ), se puede deducir que la complejidad de este algoritmo es $O(n \log k)$, donde $n$ es la cantidad total de elementos y $k$ la cantidad de arreglos.

> 3. Implementar ambos algoritmos, y hacer mediciones (y gráficos) que permitan entender si las complejidades obtenidas para cada uno se condicen con la realidad.

En nuestro caso hicimos dos gráficos distintos: uno que indica la complejidad temporal en base a la cantidad de arreglos en el problema y otro en base a la cantidad de elementos por cada arreglo. Por cada uno, realizamos una curva utilizando nuestra implementación del algoritmo de división y conquista con un arreglo de arreglos ordenado, es decir $[[1,2,3],[4,5,6]...]$, luego otra curva pero que utiliza arreglos con elementos completamente aleatorios, es decir $[[1,3,12...],[24,35,346,...]...]$ ., y finalmente una tercera curva que usa heap como solución.

Las mediciones se encuentran en el archivo **mediciones.py** y la implementación de ambos algoritmos están en **k_merge_dyc.py** y **k_merge_heap.py**. Las conclusiones obtenidas se encuentran en el último inciso.

![](/k_merge/graficos/ambos_graficos.png)

> 4. En caso que la complejidad obtenida en el punto 1 no se condiga con la realidad, indicar por qué (qué condición falla).

La complejidad obtenida en el punto 1, es decir, utilizando el teorema maestro, no se condice con la realidad ya que la condición de que el caso base sea constante falla en este problema. Esto se debe a que queda un solo arreglo de $h$ elementos, lo que hace que el caso base varíe.

> 5. En dicho caso, se requiere llegar a la complejidad correcta (no solamente enunciarla, sino demostrar cuál es).

Construimos a partir de la ecuación de recurrencia

$$
\begin{aligned}
 T(n)&=2T(\frac{n}{2})+O(n)
\end{aligned}
$$

Establecemos

$$
\begin{aligned}
 n=2^x
\end{aligned}
$$

Entonces

$$
\begin{gather*}
 T(2^x)=2T(\frac{2^x}{2})+O(2^x) \\
 \\
 T(2^x)=2T(2^{x-1})+O(2^x) \\
 \\
 T(2^{x-1})=2T(2^{x-2})+O(2^{x-1}) \\
\end{gather*}
$$

Aquí el caso base es $O(1)$ ya que lo que se hace es devolver el único arreglo restante, por lo que se puede ignorar de la sumatoria.

$$
\begin{gather*}
 T(n)=2\sum_{i=0}^{\log_k-1}(2^iO(2^{x-i-1}))+O(2^x) \\
 \\
 T(n)=2\sum_{i=0}^{\log_k-1}O(2^{x-1})+O(2^x) \\
 \\
 T(n)=\sum_{i=0}^{\log_k-1}2O(2^{x-1})+O(2^x) \\
 \\
 T(n)=\sum_{i=0}^{\log_k-1}O(2^x)+O(2^x) \\
 \\
 T(n)=\sum_{i=0}^{\log_k}O(2^x) \\
\end{gather*}
$$

Por lo tanto la complejidad estaría quedando

$$
\begin{gather*}
 \log_kO(2^x) \\
 \\
 \log_kO(n) \\
 \\
 O(n \log_k)
\end{gather*}
$$

> 6. Indicar cualquier conclusión adicional que les parezca relevante en base a lo analizado.

Como la complejidad de ambos algortimos es la misma, se puede visualizar que la forma de crecimiento es la misma, por lo que está bien que las curvas se parezcan (lo único que difieren es el tiempo exacto que tarda cada uno de ellos)

## Segunda Parte: *Contrabando*

**Aclaración**: Decidimos modelar la **mercadería** como un diccionario, donde las claves corresponden a los tipos de producto y los valores a listas que representan los distintos paquetes de contrabando. Por otra parte, los **pedidos** del aduanero son también un diccionario pero los valores están dados simplemente por la cantidad pedida por cada producto. El resultado del problema tiene el mismo formato que la mercadería.

**Ejemplo**:

```py
mercaderia = {
    "cajas de cigarrillos": [3, 8, 2],
    "botellas de vodka": [7]
}

pedido = {
    "cajas de cigarrillos": 5
}

resultado = {
    "cajas de cigarrillos": [3, 2]
}
```

> 1. Describir e implementar un algoritmo greedy que, dado un input con los productos que se tienen, y lo pedido como soborno, nos permita salir airosos de la situación, con la mayor cantidad de productos posibles. Justificar por qué el algoritmo es, efectivamente, greedy. Considerar que siempre se nos pedirá una cantidad de productos en existencias (en nuestro ejemplo anterior, no nos habrían pedido que dejemos 7 botellas de vodka radioactivo, ni tampoco mandarinas del Sahara).

Nuestro algorimo greedy recibe la mercaderia pedida como soborno y la disponible, a partir de la mercaderia disponible obtiene el total de unidades de cada producto. Por cada tipo de producto pedido como soborno, se revisan todos los paquetes para determinar el/los optimos. La forma de determinar los paquetes optimos es haciendo uso de la cantidad total de ese producto: se evalua si al quitar el producto la cantidad restante sigue cumpliendo los requerimientos del agente de aduana.

En el caso del ejemplo, tenemos que el pedido es al menos `5` unidades de `cigarrillos`, y el total de cigarrillos a disposicion es de `13` unidades, para seguir con la solucion presentada en el ejemplo vamos a tomar la mercaderia como ordenada de mayor a menor, las diferencias de tener la mercaderia o no ordenada se explican en detalle en las siguientes preguntas. De esta forma el algoritmo va a iterar por los paquetes de `cigarrillos` disponibles `[8,3,2]`, al evaluar que sin el paquete con `8` unidades se sigue cumpliendo con el pedido, va a restar estas unidades del total, quedando este en `5`, al evaluar el `3` y el `2` el algoritmo determina que estas unidades son escenciales y las agrega al arreglo solucion. Como el algoritmo itera en un principio por la mercaderia que se encuentra en el pedido del agente de aduana, en este caso no se evaluaria el `vodka`.

Es un algoritmo _greedy_ porque en cada iteracion evalua si el paquete es necesario en ese momento o no, no evalua el impacto que tendria quitar o dejar el paquete en una solucion futura. En el ejemplo anterior, de estar el arreglo desordenado, el algoritmo no evaluaria que sacar el `3` antes que el `8` daria una solucion que cumpla los requerimientos pero no la solucion optima que los cumple.

>2. Con las mismas consideraciones que en el punto anterior, describir e implementar un algoritmo (que sea óptimo) que resuelva el problema utilizando programación dinámica.

Para resolver el problema de forma dinamica, nos inspiramos en los problemas _Subset-Sum_ y por consecuencia _Knapsack_. Como en Subset-Sum, el _valor_ y el _peso_ son iguales, en nuestro caso representan las unidades de un producto a contrabanddear dentro de un paquete. Una de las ventajas que encontramos en utilizar programacion dinamica en esta solucion es que no dependemos del orden de las unidades de cada producto para encontrar la solucion optima. A diferencia de los problemas que usamos de inspiracion, nuestro algoritmo no determina el óptimo por el maximo entre usar o no el elemento, sino que armamos una funcion ```min_condicionado()``` la cual permite aplicar las condiciones particulares del problema: queremos la minima cantidad de unidades que cumplen la cantidad requerida por el agente aduanero.

En un principio, pensamos que podiamos solucionar el problema inspirandonos en los problemas de _Juan el vago_ y el de _Scheduling_, pero al igual que nos ocurria al intentar plantear el problema de _Knapsack_ uni-dimencional, comparar las posibles soluciones en busca del optimo nos quedaba un algoritmo de _Fuerza Bruta_ porque nunca encontrabamos un "óptimo parcial" con el cual comparar, sino que debiamos comparar todas las combinaciones posibles de sumas entre si.

Al igual que en _Knapsack_, decidimos usar una matriz con los _elementos_ como fila y los _pesos_ como columnas. A diferencia de en los problemas mencinados, el elemento puede ser usado por si solo, es decir, el _valor actual_ puede ser solucion por si solo, y en ese caso, no seria parte de una solucion encontrada al sumar paquetes. Finalmente el algoritmo se repite por cada elemento pedido por el agente aduanero, encontrando la mejor combinacion de paquetes para minimizar la perdida de mercancia. De esta forma, el algoritmo es dinámico porque evalua todas las posibles soluciones óptimas.

La ecuación de recurrencia es: $\text{OPT}(n, W) = \text{min-condicionado}(a, b)$, donde $a$ = no usar el elemento: $\text{OPT}(n-1, W)$ y $b$ = usar el elemento: $\text{OPT}(n-1, W-P_i) + Vi$ o solo $V_i$

> 3. Indicar y justificar la complejidad de ambos algoritmos propuestos. Indicar casos (características y ejemplos) de deficiencias en el algoritmo greedy propuesto, para los cuales este no obtenga una solución óptima.

El algoritmo greedy tiene una complejidad de $O(n * m)$, donde _n_ representa la canidad de productos que estamos contrabandeando y _m_ representa la cantidad de paquetes que poseemos de cada producto. Ambas funciones usadas, ```cantidad_productos()``` y ```obtener_paquetes_greedy()```, tienen esta complejidad, porque en ambas se ven todos los productos, y por cada paquete se analizan todos los productos.

Este algoritmo siempre llega a una solucion que cumple las condiciones, pero esta no siempre es optima. Cuando los paquetes no estan ordenados por unidades de mayor a menor, no se puede asegurar que la solucion encontrada sea optima.

```py
mercaderia_desordenada = {
"cajas de cigarrillos": [3, 2, 8]
}

pedido = {
    "cajas de cigarrillos": 5
}

resultado_optimo = {
    "cajas de cigarrillos": [3, 2]
}
    resultado_obtenido = {
    "cajas de cigarrillos": [8]
    }

```

Esto sucede porque el algoritmo obtiene la suma total de las unidades de un producto, luego recorre cada paquete y se pregunta si al sacarlo las unidades que quedan son suficientes para cumplir la demanda del oficial de aduana, si lo son actualiza el valor de las unidades quitando las que no considera necesarias. En el caso del ejemplo, se otiene una ```cantidad_unidades = 13```, al evaluar el ```3``` nota que sin esas unidades se sigue cumpliendo la condicion y actualiza ```cantidad_unidades = 10```, repite el proceso con el ```2```, llegando a ```cantidad_unidades = 8```. Cuando el algoritmo llega al paquete de ```8``` unidades, nota que no cumpliria la condicion sin el, y lo agrega a la lista ```solucion```. Ahora, mientras que la solucion cumple con el requerimiento de tener al menos ```5``` unidades, habia una mejor solucion posible: ```[2, 3]```. De haber ordenado las "cajas de cigarrillos" de mayor a menor, [8, 3, 2], el algoritmo hubiese llegado a la solucion optima.

Aun asi, mientras que el orden aumenta la probabilidad de encontrar una solucion optima, esto no esta asegurado: a veces la suma de los paquetes con menos unidades es mayor que un solo paquete de muchas unidades, pero al sacar el paquete de muchas unidades no podemos mejorar la suma sin incumplir la cantidad demandada. Como se muestra en el ejemplo a continuacion.

```py
mercaderia_ordenada = {
"cajas de cigarrillos": [8, 4, 3, 2]
}

pedido = {
    "cajas de cigarrillos": 8
}

resultado_optimo = {
    "cajas de cigarrillos": [8]
}
    resultado_obtenido = {
    "cajas de cigarrillos": [4, 3, 2] 
    }

```

Por otra parte, nuestro algoritmo dinamico tiene una complejidad O(d*(n * peso)), donde _n_ representa la cantidad de elementos a evaluar, _peso_ es la cantidad maxima de unidades disponibles, y _d_ es la cantidad de elementos pedidos como soborno. Y reconstruir la solucion es $O(n)$, porque recorre cada fila una única vez.

> 4. Implementar un programa que utilice ambos algoritmos, realizar mediciones y presentar resultados comparativos de ambas soluciones, en lo que refiere a su optimalidad de la solución (no de su complejidad). Incluir en la entrega del tp los sets de datos utilizados para estas simulaciones (que deben estar explicados en el informe). Estos deben incluir al menos una prueba de volumen, indicando cómo es que fueron generadas.

Implementamos un programa ```encontrar_mejor_soborno```, el cual compara que tan óptimos son los algoritmos implementados. Para el analisis de ambos decidimos mostrar como se comportan frente a recibir los paquetes ordenados de mayor a menor por cada producto y recibirlos desordenados. Para un analisis mas puro, armamos una funcion ```armar_set_datos()``` que utilizando la biblioteca random, genera un array de unidades random para los paquetes de cada produto. Tambien se genera una solución óptima y se la incluye en el array de unidades. Por otro lado, al generar una solución cuya suma total pueda ser superior al elemento maximo del array, incluimos el valor de la suma como un elemento mas al final. El próposito de este elemento no es ser solución, sino que permitir a la matriz del algoritmo de dinamica contar con todos los pesos requeridos.

Para poder comparar ambos algoritmos, decidimos armar una funcion que nos indique si el algoritmo es o no optimo, y valiéndonos de que los booleanos en python tienen valor ```0``` y ```1```, los usamos para calcular el porcentaje sobre la cantidad de veces en las que cada algoritmo fue optimo. Con los datasets adjuntos llegamos a la siguiente solucion:

```
>>> python3 encontrar_mejor_soborno.py
>>> Porcentaje de veces que greedy es optimo con mercaderia ordenada:  0.85
>>> Porcentaje de veces que greedy es optimo con mercaderia desordenada:  0.0
>>> Porcentaje de veces que dinamica es optimo con mercaderia ordenada:  1.0
>>> Porcentaje de veces que dinamica es optimo con mercaderia desordenada:  1.0
```

Para un análisis más interesante, graficamos cómo varían las soluciones en función del tamaño de la entrada. Con esto también se puede ver la eficiencia: queremos ver por cuanto le "erra" en los casos cuando no resulta óptimo. El análisis más detallado se encuentra en el archivo `graficos.ipynb`

![](/contrabando/graficos/graficos.png)

En los archivos ```_test``` de cada algoritmo se encuentran dos pruebas de volumen. Estas se realizaron usando la funcion ```armar_set_datos()```. Para el algoritmo dinámico se requiere que la suma de la solucion obtenida sea igual a la suma de la solucion optima proporcionada por ```armar_set_datos()```, se trabaja con la suma en ambos casos porque al usar valores random, no podemos asegurar que el algoritmo no llegue a un resultado igual de óptimo pero utilizando diferentes paquetes a los pensados en un principio. Para el algoritmo greedy se requiere que la suma de la solucion obtenida sea mayor o igual a la suma de la solución óptima, porque se presume que greedy no va a ser óptimo, pero si va a dar una solución que cumpla las condiciones dadas.