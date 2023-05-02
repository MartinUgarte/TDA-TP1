import random 
from constantes import PRODUCTOS

VOLUMEN = 200
MAXIMO_NRO_PAQUETES = 5
MAXIMO_NRO_UNIDADES = 20
CANTIDAD_UNIDADES_MAX = 100

def armar_set_datos(productos, volumen):
    """
    Genera un set de datos aleatorio para el problema de contrabando, con la solución óptima esperada
    """

    solucion = {}
    pedido = {}
    mercaderia = {}
    for producto in productos:
        solucion[producto] = []
        for _ in range(random.randint(1, MAXIMO_NRO_PAQUETES)):
            solucion[producto].append(random.randint(1, MAXIMO_NRO_UNIDADES))

        pedido[producto] = sum(solucion[producto])
        mercaderia[producto] = []

        for _ in range(volumen):
            nro_random = random.randint(1, CANTIDAD_UNIDADES_MAX)
            mercaderia[producto].append(nro_random)
                
        for i in range(len(solucion[producto])):
            mercaderia[producto].insert(random.randint(0, len(mercaderia[producto])), solucion[producto][i])
        
        mercaderia[producto].insert(random.randint(0, len(mercaderia[producto])), sum(solucion[producto]))
        
    return pedido, mercaderia, solucion

def escribir_archivo(nombre_archivo):
    """
    Genera un archivo con un set de datos aleatorio para el problema de contrabando, con la solución óptima esperada
    """

    pedidos, mercaderia, solucion = armar_set_datos(PRODUCTOS, VOLUMEN)
    with open(nombre_archivo, 'w') as archivo:
        for producto, paquetes in solucion.items():
            archivo.write(producto + ";")
            for i in range(len(paquetes)):
                if i == len(paquetes) - 1:
                    archivo.write(str(paquetes[i]))
                else:
                    archivo.write(str(paquetes[i]) + ";")
            archivo.write(",")
        archivo.write("\n")

        for pedido, cantidad in pedidos.items():
            archivo.write(pedido + ";" + str(cantidad))
            archivo.write(",")
        archivo.write("\n")

        for producto, paquetes in mercaderia.items():
            for paquete in paquetes:
                archivo.write(f"{producto};{str(paquete)}\n")