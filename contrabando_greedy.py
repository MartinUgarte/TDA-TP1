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

# Caso 0
mercaderia = []
pedidos = []
assert obtener_paquetes_greedy(pedidos, mercaderia) == []

# Caso 1
mercaderia = [("cigarrillo", 8)]
pedidos = [("cigarrillo", 6)]
assert obtener_paquetes_greedy(pedidos, mercaderia) == [("cigarrillo", 8)]

# Caso 2
mercaderia = [("cigarrillo", 8), ("cigarrillo", 5)]
pedidos = [("cigarrillo", 5)]
assert obtener_paquetes_greedy(pedidos, mercaderia) == [("cigarrillo", 5)]

# Caso 3
mercaderia = [("cigarrillo", 5), ("cigarrillo", 8)]
pedidos = [("cigarrillo", 5)]
assert obtener_paquetes_greedy(pedidos, mercaderia) == [("cigarrillo", 5)]

# Caso 4
mercaderia = [("cigarrillo", 8), ("cigarrillo", 3), ("cigarrillo", 2)]
pedidos = [("cigarrillo", 5)]
assert obtener_paquetes_greedy(pedidos, mercaderia) == [("cigarrillo", 3), ("cigarrillo", 2) ]

# Caso 5
mercaderia = [("cigarrillo", 8), ("cigarrillo", 3), ("cigarrillo", 2), ("cigarrillo", 6)]
pedidos = [("cigarrillo", 5)]
assert obtener_paquetes_greedy(pedidos, mercaderia) == [("cigarrillo", 3), ("cigarrillo", 2) ]

# Caso 6
mercaderia = [("cigarrillo", 9), ("cigarrillo", 3), ("cigarrillo", 2), ("cigarrillo", 6)]
pedidos = [("cigarrillo", 8)]
assert obtener_paquetes_greedy(pedidos, mercaderia) == [("cigarrillo", 6), ("cigarrillo", 2)]

# Caso 7
mercaderia = [("cigarrillo", 8), ("vodka", 5)]
pedidos = [("cigarrillo", 8)]
assert obtener_paquetes_greedy(pedidos, mercaderia) == [("cigarrillo", 8)]

# Caso 8
mercaderia = [("cigarrillo", 8), ("vodka", 5)]
pedidos = [("cigarrillo", 8), ("vodka", 4)]
assert obtener_paquetes_greedy(pedidos, mercaderia) == [("cigarrillo", 8), ("vodka", 5)]

# Caso 9
mercaderia = [("cigarrillo", 8), ("cigarrillo", 3), ("cigarrillo", 2), ("vodka", 5)]
pedidos = [("cigarrillo", 5), ("vodka", 4)]
assert obtener_paquetes_greedy(pedidos, mercaderia) == [("cigarrillo", 3), ("cigarrillo", 2), ("vodka", 5)]
