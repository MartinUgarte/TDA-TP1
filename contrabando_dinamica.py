def obtener_paquetes_dinamica(pedidos, mercaderia):
    pass





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