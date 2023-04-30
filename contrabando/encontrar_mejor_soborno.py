import random
from contrabando_dinamica import obtener_paquetes_dinamica
from contrabando_greedy import obtener_paquetes_greedy

PRODUCTO_UNO = "cigarrillos"
PRODUCTO_DOS = "vodka"
PRODUCTO_TRES = "naipes"

def ordenar_paquetes(mercaderia, reverse):
    for producto, cantidad in mercaderia.items():
        mercaderia[producto] = sorted(cantidad, reverse=reverse)

def generar():
    mercaderia_ordenada = {PRODUCTO_UNO: [12,7,3,2], PRODUCTO_DOS:[8,6], PRODUCTO_TRES:[54,32,14,2]}
    mercaderia_desordenada = {PRODUCTO_UNO: [3,7,2,12], PRODUCTO_DOS:[6,8], PRODUCTO_TRES:[14,2,32,54]}
    coima_pedida = {PRODUCTO_UNO: 5, PRODUCTO_DOS: 7, PRODUCTO_TRES: 20}
    solucion_optima = {PRODUCTO_UNO: [3,2], PRODUCTO_DOS: [8], PRODUCTO_TRES: [32]}
    return mercaderia_ordenada, mercaderia_desordenada, coima_pedida, solucion_optima


def greedy_es_optimo_ordenado():
    mercaderia_ordenada, _, coima_pedida, solucion_optima = generar()
    resultado_ordenado = obtener_paquetes_greedy(coima_pedida, mercaderia_ordenada)

    return solucion_es_optima(resultado_ordenado, solucion_optima)
    

def greedy_es_optimo_desordenado():
    _, mercaderia_desordenada, coima_pedida, solucion_optima = generar()
    resultado_desordenado = obtener_paquetes_greedy(coima_pedida, mercaderia_desordenada)

    return solucion_es_optima(resultado_desordenado, solucion_optima)

def dinamica_siempre_es_optimo():
    mercaderia_ordenada, mercaderia_desordenada, coima_pedida, solucion_optima = generar()

    resultado_ordenado = obtener_paquetes_dinamica(coima_pedida, mercaderia_ordenada)
    resultado_desordenado = obtener_paquetes_dinamica(coima_pedida, mercaderia_desordenada)

    return solucion_es_optima(resultado_ordenado, solucion_optima) and solucion_es_optima(resultado_desordenado, solucion_optima)
    

def solucion_es_optima(solucion_obtenida, solucion_esperada):
    result = True
    for pedido in solucion_obtenida:
        for unidad in solucion_obtenida[pedido]:
            if unidad not in solucion_esperada[pedido]:
                result = False
    return result

def arreglos_volumen():
    arreglos = []
    soluciones_optimas = []
    return arreglos, soluciones_optimas

def prueba_volumen_greedy():
    pass

def prueba_volumen_dinamica():
    pass


print(greedy_es_optimo_ordenado())
print(greedy_es_optimo_desordenado())
print(dinamica_siempre_es_optimo())