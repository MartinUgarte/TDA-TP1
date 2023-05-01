# Teoría De Algortimos I

### Alumnos

- Martina Victoria Lozano: 106267
- Martin Ugarte: 107870

## Primera Parte: *K-merge*

**Aclaración**: Definimos $k$ como la cantidad de arreglos ordenados, y $h$ como la cantidad de elementos en cada arreglo. La cantidad de elementos total por lo tanto es $n = k * h$

> 1. Determinar, utilizando el Teorema Maestro, cuál sería la complejidad del algoritmo propuesto

La fórmula del Teorema Maestro está dada por

$$T(n)=A*T(n/B) + O(n^c)$$

Donde $A$ representa la cantidad de llamados recursivos, $B$ la proporción del tamaño original de la lista con el que llamamos recursivamente y $O(n^c)$ el costo de las operaciones que no son llamadas recursivas.

En este caso, tenemos dos llamadas recursivas, el arreglo es partido a la mitad por cada uno de estos llamados, y el costo de las demás operaciones es $O(n)$ ya que el costo de mergear dos arreglos es $O(n + m) = O(n)$ sabiendo que $n$ y $m$ son las longitudes de cada arreglo “parcial” donde $l$ es la mayor, con lo cual se puede despreciar m como una constante.

Por lo cual, $A = 2$, $B = 2$ y $C = 1$.

Luego, $logB(A) = log_2(2) = 1$

Según el Teorema Maestro, como $logB(A)=C=1$, entonces la complejidad del algoritmo propuesto es $O(n^c log n)=O(n logn)$, donde $n$ es la cantidad total de elementos, es decir, $k * h$.

> 2. Describir el algoritmo que utiliza heaps, y determinar su complejidad.

Se tiene el conjunto de arreglos, el heap y un arreglo vacío, en el heap se encolan los primeros datos de cada arreglo de la forma (dato, número_arreglo). Mientras que el heap no esté vacío, se desencola del heap y se agrega el valor en el arreglo. Posteriormente se guarda el siguiente elemento del arreglo al que pertenecía el dato guardado. Se continúa así hasta que no queda ningún dato en el heap. 
Por lo tanto, se puede deducir que la complejidad de este algoritmo es O(n log k)

> 3. Implementar ambos algoritmos, y hacer mediciones (y gráficos) que permitan entender si las complejidades obtenidas para cada uno se condicen con la realidad.

Las mediciones se encuentran en el archivo *graficos.py*

> 4. En caso que la complejidad obtenida en el punto 1 no se condiga con la realidad, indicar por qué (qué condición falla).

- El teorema Maestro contempla el caso en el que se ordena un solo arreglo --> mergesort, cuando nuestro metodo de ordenamiento aplica mergesort reiteradamente.

> 5. En dicho caso, se requiere llegar a la complejidad correcta (no solamente enunciarla, sino demostrar cuál es).

TODO

> 6. Indicar cualquier conclusión adicional que les parezca relevante en base a lo analizado.

TODO

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

En el algoritmo greedy nos inspiramos en la implementacion de Dijkstra, y en lugar de un diccionario de distancias, decidimos modelarlo usando un diccionario que al inicio contiene la cantidad total de las unidades de cada producto. El algoritmo recorre por producto su lista de paquetes, y se fija si al quitarle a la _cantidad_ el numero de unidades del paquete, _cantidad_ sigue cumpliendo la condicion minima de unidades dada por el agente de la aduana.En caso de cumplir, actualiza la _cantidad_ para reflejar que no requiere esas unidades. En caso de no cumplir, agrega ese paquete a la solucion de ese producto. Repite este proceso por cada producto, y devuelve un diccionario, donde por cada productio tiene una lista con los paquetes solucion. El algoritmo es greedy porque solo considera su estado actual, y se fija si las unidades que esta evaluando son necesarias o no. Luego de la evaluacion, no vuelve a considerar las unidades ya evaluadas. Decidimos no usar un _heap_ para asegurarnos que siempre se analice el paquete con mas unidades disponible, porque aunque eso mejora la probabilidad de obtener una solucion optima, no la asegura, y nos parecio valioso poder mostrar en el punto _4_ estas diferencias, lo cual puede hacerse ordenando los paquetes de menor a mayor de antemano. En ambos casos, usar un _heap_ u ordenar, incrementarian la complejidad en $O(nlogn)$. (Suponiendo que se hace uso de las funciones ```heapsort``` y ```sorted()``` respectivamente). Y en el caso del _heap_ hay que tener en cuenta que _desencolar_ es $O(logn)$. 

>2. Con las mismas consideraciones que en el punto anterior, describir e implementar un algoritmo (que sea óptimo) que resuelva el problema utilizando programación dinámica.

Para resolver el problema de forma dinamica, nos inspiramos en los problemas _Subset-Sum_ y por consecuencia _Knapsack_. Como en Subset-Sum, el _valor_ y el _peso_ son iguales, en nuestro caso representan las unidades de un producto a contrabanddear dentro de un paquete. Una de las ventajas que encontramos en utilizar programacion dinamica en esta solucion es que no dependemos del orden de las unidades de cada producto para encontrar la solucion optima. A diferencia de los problemas que usamos de inspiracion, nuestro algoritmo no determina el optimo por el maximo entre usar o no el elemento, sino que armamos una funcion ```min_condicionado()``` la cual permite aplicar las condiciones particulares del problema: queremos la minima cantidad de unidades que cumplen la cantidad requerida por el agente aduanero. 

En un principio, pensamos que podiamos solucionar el problema inspirandonos en los problemas de _Juan el vago_ y el de _Scheduling_, pero al igual que nos ocurria al intentar plantear el problema de _Knapsack_ uni-dimencional, comparar las posibles soluciones en busca del optimo nos quedaba un algoritmo de _Fuerza Bruta_ porque nunca encontrabamos un "optimo parcial" con el cual comparar, sino que debiamos comparar todas las combinaciones posibles de sumas entre si. 

Al igual que en _Knapsack_, decidimos usar una matriz con los _elementos_ como fila y los _pesos_ como columnas. A diferencia de en los problemas mencinados, el elemento puede ser usado por si solo, es devir, el _valor actual_ puede ser solucion por si solo, y en ese caso, no seria parte de una solucion encontrada al sumar paquetes. 

El algoritmo se repite por cada elemento pedido por el agente aduanero, encontrando la mejor combinacion de paquetes para minimizar la perdida de mercancia. 

El algoritmo es dinamico, porque evalua todas las posibles soluciones. 

La ecuacion de recurrencia es: $OPT(n, W) = min_condicionado(a, b)$, donde a = no usar el elemento: $OPT(n-1, W)$ y b = usar el elemento: $OPT(n-1, W-Pi) + Vi$ o solo $Vi$

> 3. Indicar y justificar la complejidad de ambos algoritmos propuestos. Indicar casos (características y ejemplos) de deficiencias en el algoritmo greedy propuesto, para los cuales este no obtenga una solución óptima.

El algoritmo greedy tiene una complejidad de O(n * m), donde _n_ representa la canidad de productos que estamos contrabandeando y _m_ representa la cantidad de paquetes que poseemos de cada producto. Ambas funciones usadas, ```cantidad_productos()``` y ```obtener_paquetes_greedy()```, tienen esta complejidad, porque en ambas se ven todos los productos, y por cada paquete se analizan todos los productos.

Este algoritmo siempre llega a una solucion que cumple las condiciones, pero esta no siempre es optima. Cuando los paquetes no estan ordenados por unidades de mayor a menor, no se puede asegurar que la solucion encontrada sea optima. 

    ```py
    mercaderia = {
    "cajas de cigarrillos": [3, 2, 8]
    }

    pedido = {
        "cajas de cigarrillos": 5
    }

    resultado_optimo = {
        "cajas de cigarrillos": [3, 2]
    }
     resultado_obtenido_sin_ordenar = {
        "cajas de cigarrillos": [8]
     }

    ```
Esto sucede porque el algoritmo obtiene la suma total de las unidades de un producto, luego recorre cada paquete y se pregunta si al sacarlo las unidades que quedan son suficientes para cumplir la demanda del oficial de aduana, si lo son actualiza el valor de las unidades quitando las que no considera necesarias. En el caso del ejemplo, se otiene una ```cantidad_unidades = 13```, al evaluar el ```3``` nota que sin esas unidades se sigue cumpliendo la condicion y actualiza ```cantidad_unidades = 10```, repite el proceso con el ```2```, llegando a ```cantidad_unidades = 8```. Cuando el algoritmo llega al paquete de ```8``` unidades, nota que no cumpliria la condicion sin el, y lo agrega a la lista ```solucion```. Ahora, mientras que la solucion cumple con el requerimiento de tener al menos ```5``` unidades, habia una mejor solucion posible: ```[2, 3]```. De haber ordenado las "cajas de cigarrillos" de mayor a menor, [8, 3, 2], el algoritmo hubiese llegado a la solucion optima. Aun asi, mientras que el orden aumenta la probabilidad de encontrar una solucion optima, esto no esta asegurado: a veces la suma de los paquetes con menos unidades es mayor que un solo paquete de muchas unidades, pero al sacar el paquete de muchas unidades no podemos mejorar la suma sin incumplir la cantidad demandada. 

Nuestro algoritmo dinamico tiene una complejidad O(d*(n * peso)), donde _n_ representa la cantidad de elementos a evaluar, _peso_ es la cantidad maxima de unidades disponibles, y _d_ es la cantidad de elementos pedidos como soborno. Y reconstruir la solucion es O(n), porque recorres una fila maximo una sola vez.

> 4. Implementar un programa que utilice ambos algoritmos, realizar mediciones y presentar resultados comparativos de ambas soluciones, en lo que refiere a su optimalidad de la solución (no de su complejidad). Incluir en la entrega del tp los sets de datos utilizados para estas simulaciones (que deben estar explicados en el informe). Estos deben incluir al menos una prueba de volumen, indicando cómo es que fueron generadas.

Implementamos un programa ```encontrar_mejor_soborno```, el cual compara que tan optimos son los algoritmos implementados. Para el analisis de ambos decidimos mostrar como se comportan frente a recibir los paquetes ordenados de mayor a menor por cada producto y recibirlos desordenados. Para un analisis mas puro, armamos una funcion ```armar_set_datos()``` que utilizando la biblioteca random, genera un array de unidades random para los paquetes de cada produto. Tambien se genera una solucion optima y se la incluye en el array de unidades. Por otro lado, al generar una solucion cuya suma total pueda ser superior al elemento maximo del array, incluimos el valor de la suma como un elemento mas al final. El proposito de este elemento no es ser solucion, sino que permitir a la matriz del algoritmo de dinamica contar con todos los pesos requeridos. 

Para poder comparar ambos algoritmos, decidimos armar una funcion que nos indique si el algoritmo es o no optimo, y valiendonos de que los booleanos en python tienen valor ```0``` y ```1```, los usamos para calcular el porcentaje sobre la cantidad de veces en las que cada algoritmo fue optimo. Como era de esperarse, ejecutar greedy de forma desordenada dio siempre ```0.0``` y ejecutar dinamica dio siempre ```1.0```, mientras que ejecutar greedy con los datos ordenados dio diferentes valores en ```[0.50, 0.75]```. 

En los archivos ```_test``` de cada algoritmo se encuentran dos pruebas de volumen. Estas se realizaron usando la funcion ```armar_set_datos()```. Para el algoritmo dinamico se requiere que la suma de la solucion obtenida sea igual a la suma de la solucion optima proporcionada por ```armar_set_datos()```, se trabaja con la suma en ambos casos porque al usar valores random, no podemos asegurar que el algoritmo no llegue a un resultado igual de optimo pero utilizando diferentes paquetes a los pensados en un principio. Para el algoritmo greedy se requiere que la suma de la solucion obtenida sea mayou-igual a la suma de la solucion optima, porque se preusme que greedy no va a ser optimo, pero si va a dar una solucion que cumpla las condiciones dadas. 