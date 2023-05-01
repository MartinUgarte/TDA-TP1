
	
def cantidad_productos(mercaderia):
    cantidades = {}
    for producto, cantidad in mercaderia.items():
        cantidades[producto] = sum(cantidad)

    return cantidades
    
def obtener_paquetes_greedy(pedidos, mercaderia):
    resultado = {}  
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

