
	
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

# variables:
# cant_productos: cantidad de productos que hay en el pedido --> "cigarrillo", "vodka" = 2
# cant_paquetes: cantidad de paquetes que hay por cada producto --> "cigarrillo" = [3,4,6,7] --> 4 "vodkas" = [2,3,4,5] --> 4
 
# O(cant_productos * cant_paquetes)