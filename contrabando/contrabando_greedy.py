def ordenar_paquetes(mercaderia, reverse):
	return sorted(mercaderia, key=lambda x: (x[0], x[1]), reverse=reverse)
	
def cantidad_productos(mercaderia):
    resultado = {}
    for producto in mercaderia:
        if producto[0] not in resultado:
            resultado[producto[0]] = producto[1]
        else:
            resultado[producto[0]] += producto[1]
    return resultado
    
def obtener_paquetes_greedy(pedidos, mercaderia):
    resultado = []  
    paquetes_ordenados = ordenar_paquetes(mercaderia, True)
    productos = cantidad_productos(mercaderia)
    
    for pedido in pedidos:
        for paquete in paquetes_ordenados:
            if paquete[0] != pedido[0]:
                continue
            elif productos[paquete[0]] - paquete[1] >= pedido[1]:
                productos[paquete[0]] -= paquete[1]
            else: 
                resultado.append(paquete)    
    return resultado