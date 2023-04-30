import random 
MAXIMO_NRO_PAQUETES = 5
MAXIMO_NRO_UNIDADES = 20
CANTIDAD_UNIDADES_MAX = 100

def armar_set_datos(productos, volumen):
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
            if nro_random > max(solucion[producto]):
                mercaderia[producto].append(nro_random)
            if nro_random < min(solucion[producto]):
                continue
                
        for i in range(len(solucion[producto])):
            mercaderia[producto].insert(random.randint(0, len(mercaderia[producto])), solucion[producto][i])
        
    
    return pedido, mercaderia, solucion