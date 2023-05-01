import random
from contrabando_dinamica import obtener_paquetes_dinamica
from contrabando_greedy import obtener_paquetes_greedy
from armar_set import armar_set_datos

PRODUCTO_UNO = "cigarrillos"
PRODUCTO_DOS = "vodka"
PRODUCTO_TRES = "naipes"
VOLUMEN = 100

def ordenar_paquetes(mercaderia):
    for producto, cantidad in mercaderia.items():
        mercaderia[producto] = sorted(cantidad, reverse=True)
    return mercaderia


def greedy_es_optimo_ordenado():
    coima_pedida, mercaderia, solucion_optima = armar_set_datos([PRODUCTO_UNO, PRODUCTO_DOS, PRODUCTO_TRES], VOLUMEN)
    resultado_ordenado = obtener_paquetes_greedy(coima_pedida, ordenar_paquetes(mercaderia))

    return solucion_es_optima(resultado_ordenado, solucion_optima)
    

def greedy_es_optimo_desordenado():
    coima_pedida, mercaderia, solucion_optima = armar_set_datos([PRODUCTO_UNO, PRODUCTO_DOS, PRODUCTO_TRES], VOLUMEN)
    resultado_desordenado = obtener_paquetes_greedy(coima_pedida, mercaderia)

    return solucion_es_optima(resultado_desordenado, solucion_optima)

def dinamica_siempre_es_optimo():
    coima_pedida, mercaderia, solucion_optima = armar_set_datos([PRODUCTO_UNO, PRODUCTO_DOS, PRODUCTO_TRES], VOLUMEN)

    resultado_ordenado = obtener_paquetes_dinamica(coima_pedida, ordenar_paquetes(mercaderia))
    resultado_desordenado = obtener_paquetes_dinamica(coima_pedida, mercaderia)

    return solucion_es_optima(resultado_ordenado, solucion_optima) and solucion_es_optima(resultado_desordenado, solucion_optima)
    

def solucion_es_optima(solucion_obtenida, solucion_esperada):
    result = True
    for pedido in solucion_obtenida:
        if sum(solucion_obtenida[pedido]) != sum(solucion_esperada[pedido]):
            result = False
    return result


def main():
    porcentaje_greedy_ordenado = 0
    porcentaje_greedy_desordenado = 0
    porcentaje_dinamica = 0
    for n in range(VOLUMEN):
        porcentaje_greedy_ordenado += greedy_es_optimo_ordenado()
        porcentaje_greedy_desordenado += greedy_es_optimo_desordenado()
        porcentaje_dinamica += dinamica_siempre_es_optimo()
    print("Porcentaje de veces que greedy es optimo con mercaderia ordenada: ", porcentaje_greedy_ordenado/VOLUMEN)
    print("Porcentaje de veces que greedy es optimo con mercaderia desordenada: ", porcentaje_greedy_desordenado/VOLUMEN)
    print("Porcentaje de veces que dinamica es optimo: ", porcentaje_dinamica/VOLUMEN)
main()
