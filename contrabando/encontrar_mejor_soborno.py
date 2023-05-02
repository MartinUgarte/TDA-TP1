from contrabando_dinamica import obtener_paquetes_dinamica
from contrabando_greedy import obtener_paquetes_greedy
from armar_set import escribir_archivo
from constantes import *

def leer_archivo(nombre_archivo):
    """
    Lee el archivo y devuelve un diccionario con los pedidos, otro con la mercadería y otro con la solución esperada
    """
    coima_pedida = {}
    solucion = {}
    mercaderia = {}
    with open(nombre_archivo, 'r') as archivo:
        
        linea_solucion = archivo.readline()
        productos = linea_solucion.rstrip().split(",")
        for i in range(len(productos)-1):
            paquetes = productos[i].split(";")
            solucion[paquetes[0]] = []
            for j in range(1, len(paquetes)):
                solucion[paquetes[0]].append(int(paquetes[j]))
                
        linea_coima_pedida = archivo.readline()
        pedidos = linea_coima_pedida.rstrip().split(",")
        for i in range(len(pedidos)-1):
            pedido = pedidos[i].split(";")
            coima_pedida[pedido[0]] = int(pedido[1])

        for linea_mercaderia in archivo:
            linea_mercaderia = linea_mercaderia.rstrip().split(";")
            mercaderia[linea_mercaderia[0]] = mercaderia.get(linea_mercaderia[0], []) + [int(linea_mercaderia[1])]

    return coima_pedida, mercaderia, solucion           

def ordenar_paquetes(mercaderia):
    """
    Ordena los paquetes en la mercadería de mayor a menor
    """
    for producto, cantidad in mercaderia.items():
        mercaderia[producto] = sorted(cantidad, reverse=True)
    return mercaderia

def algoritmo_es_optimo(nombre_archivo, funcion, ordenar = False):
    """
    Lee el dataset, aplica el algoritmo requerido y devuelve True si la solución obtenida por el algoritmo es óptima.
    Si se quisiese generar nuevos datasets, descomentar la linea con la funcion escribir_archivo()
    """
    # escribir_archivo(nombre_archivo)
    coima_pedida, mercaderia, solucion_optima = leer_archivo(nombre_archivo)

    if ordenar:
        mercaderia = ordenar_paquetes(mercaderia)
    solucion_obtenida = funcion(coima_pedida, mercaderia)

    return solucion_es_optima(solucion_obtenida, solucion_optima)   

def solucion_es_optima(solucion_obtenida, solucion_esperada):
    """
    Devuelve True si la solución obtenida es óptima.
    """
    result = True
    for pedido in solucion_obtenida:
        if sum(solucion_obtenida[pedido]) != sum(solucion_esperada[pedido]):
            result = False
    return result

def main():
    porcentaje_greedy_ordenado, porcentaje_greedy_desordenado = 0, 0
    porcentaje_dinamica_ordenado, porcentaje_dinamica_desordenado = 0, 0
    
    for n in range(VOLUMEN):
        porcentaje_greedy_ordenado += algoritmo_es_optimo(f"./datasets/datos{n}.csv", obtener_paquetes_greedy, True)
        porcentaje_greedy_desordenado += algoritmo_es_optimo(f"./datasets/datos{n}.csv", obtener_paquetes_greedy)
        porcentaje_dinamica_ordenado += algoritmo_es_optimo(f"./datasets/datos{n}.csv", obtener_paquetes_dinamica, True)
        porcentaje_dinamica_desordenado += algoritmo_es_optimo(f"./datasets/datos{n}.csv", obtener_paquetes_dinamica)

    print("Porcentaje de veces que greedy es optimo con mercaderia ordenada: ", porcentaje_greedy_ordenado/VOLUMEN)
    print("Porcentaje de veces que greedy es optimo con mercaderia desordenada: ", porcentaje_greedy_desordenado/VOLUMEN)
    print("Porcentaje de veces que dinamica es optimo con mercaderia ordenada: ", porcentaje_dinamica_ordenado/VOLUMEN)
    print("Porcentaje de veces que dinamica es optimo con mercaderia desordenada: ", porcentaje_dinamica_desordenado/VOLUMEN)
    
main()
