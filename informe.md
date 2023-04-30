# Teoría De Algortimos I

### Alumnos

- Martina Lozano: 106267
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

TODO

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

En primer lugar, para la solución Greedy nos aseguramos que los paquetes queden ordenados por cantidad de mayor a menor y también disponemos de un diccionario que informa la cantidad pedida como soborno para cada tipo de producto. Gracias a esto, podemos recorrer los paquetes de nuestra mercadería disponible, por cada tipo de producto pedido, y ser capaces de decidir si agregar ese paquete a nuestro conjunto de soluciones o no. Esta acción se realiza de forma instantánea (por eso es Greedy) viendo si la diferencia entre la cantidad total hasta ese momento para ese producto puntual y la cantidad que provee el paquete es mayor o igual a la cantidad solicitada. De serlo, entonces esa solución no nos sirve y reducimos el problema a encontrar la cantidad deseada menos el valor de ese paquete. De lo contrario, agregamos ese paquete al conjunto de soluciones.

>2. Con las mismas consideraciones que en el punto anterior, describir e implementar un algoritmo (que sea óptimo) que resuelva el problema utilizando programación dinámica.

Para resolver el problema de forma dinamica, nos inspiramos en los problemas _Subset-Sum_ y por consecuencia _Knapsack_. Como en Subset-Sum, el _valor_ y el _peso_ son iguales, en nuestro caso representan las unidades de un producto a contrabanddear dentro de un paquete. Una de las ventajas que encontramos en utilizar programacion dinamica en esta solucion es que no dependemos del orden de las unidades de cada producto para encontrar la solucion optima. A diferencia de los problemas que usamos de inspiracion, nuestro algoritmo no determina el optimo por el maximo entre usar o no el elemento, sino que armamos una funcion ```min_condicionado()``` la cual permite aplicar las condiciones particulares del problema: queremos la minima cantidad de unidades que cumplen la cantidad requerida por el agente aduanero. 
En un principio, pensamos que podiamos solucionar el problema inspirandonos en los problemas de _Juan el vago_ y el de _Scheduling_, pero al igual que nos ocurria al intentar plantear el problema de _Knapsack_ uni-dimencional, comparar las posibles soluciones en busca del optimo nos quedaba un algoritmo de _Fuerza Bruta_ porque nunca encontrabamos un "optimo parcial" con el cual comparar, sino que debiamos comparar todas las combinaciones posibles de sumas entre si. 
Al igual que en _Knapsack_, decidimos usar una matriz con los _elementos_ como fila y los _pesos_ como columnas. A diferencia de en los problemas mencinados, el elemento puede ser usado por si solo, es devir, el _valor actual_ puede ser solucion por si solo, y en ese caso, no seria parte de una solucion encontrada al sumar paquetes. 
El algoritmo se repite por cada elemento pedido por el agente aduanero, encontrando la mejor combinacion de paquetes para minimizar la perdida de mercancia. 
El algoritmo es dinamico, porque evalua todas las posibles soluciones. 
La complejidad del algoritmo es O(...)
La ecuacion de recurrencia es: $OPT(n, W) = min_condicionado(a, b)$, donde a = no usar el elemento: $OPT(n-1, W)$ y b = usar el elemento: $OPT(n-1, W-Pi) + Vi$ o solo $Vi$



> 3. Indicar y justificar la complejidad de ambos algoritmos propuestos. Indicar casos (características y ejemplos) de deficiencias en el algoritmo greedy propuesto, para los cuales este no obtenga una solución óptima.
 
TODO
- El de greedy va a ser O(nlogn) + O(el alg greedy) --> el costo de ordenar mas el del algoritmo en si.
- Por ahi en nuestra implementacion no deberiamos ordenar, para mostrar que no siempre es optimo, y al fijanos las comparaciones, mostramos que ordenando si encuentra el optimo. 

- Nuestro algoritmo dinamico tiene una complejidad O(d*(n * peso)), donde _n_ representa la cantidad de elementos a evaluar, _peso_ es la cantidad maxima de unidades disponibles, y _d_ es la cantidad de elementos pedidos como soborno. 

> 4. Implementar un programa que utilice ambos algoritmos, realizar mediciones y presentar resultados comparativos de ambas soluciones, en lo que refiere a su optimalidad de la solución (no de su complejidad). Incluir en la entrega del tp los sets de datos utilizados para estas simulaciones (que deben estar explicados en el informe). Estos deben incluir al menos una prueba de volumen, indicando cómo es que fueron generadas.

TODO
- creo que en lugar de test, tenemos las simulaciones. 
- mi idea para una prueba de volumen es basicamente, plantear el resultado, generar arreglos random, y meterles el resultado. 
- teniendo en cuenta el pedido de analisis de optimalidad, ordenar en greedy le saca proposito a las simulaciones.
