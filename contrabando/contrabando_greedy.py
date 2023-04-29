def ordenar_paquetes(mercaderia, reverse):
    for producto, cantidad in mercaderia.items():
        mercaderia[producto] = sorted(cantidad, reverse=reverse)
	
def cantidad_productos(mercaderia):
    cantidades = {}
    for producto, cantidad in mercaderia.items():
        cantidades[producto] = sum(cantidad)

    return cantidades
    
def obtener_paquetes_greedy(pedidos, mercaderia):
    resultado = {}  
    ordenar_paquetes(mercaderia, True)

    productos = cantidad_productos(mercaderia)

    for coima, cantidad in pedidos.items():
        solucion = []
        for paquete in mercaderia[coima]:
            if productos[coima] - paquete >= cantidad:
                productos[coima] -= paquete
            else: 
                solucion.append(paquete)
        resultado[coima] = solucion    

    return resultado
