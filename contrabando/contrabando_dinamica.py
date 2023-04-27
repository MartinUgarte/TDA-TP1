C = "cigarrillo"

def cumple_pedido(paquete, productoPedido):
	return paquete[0] == productoPedido[0] and paquete[1] >= productoPedido[1]

def obtener_paquete_de_menor_cantidad(paquete_uno, paquete_dos, pedido):
	if paquete_uno[1] < paquete_dos[1] and paquete_uno[1] > pedido[1]:
		return paquete_uno
	elif paquete_dos[1] > pedido[1]:
		return paquete_dos
	# TODO: ver que hacer si ninguno cumple con ser mayor al minimo

def obtener_paquetes_dinamica(pedidos, mercaderia):
	if len(mercaderia) == 0 or len(pedidos) == 0:
		return []

	if len(mercaderia) == 1 and len(pedidos) == 1:
		return mercaderia[0]            

	## ASUMO POR AHORA QUE SON TODOS CIGARRILLOS ------------------------
	G = [None] * len(mercaderia) # G es una lista de sumas parciales
	G[0] = mercaderia[0] # Si hay un solo paquete, usamos esa cantidad

	G[1] = obtener_paquete_de_menor_cantidad(mercaderia[0], mercaderia[1], pedidos[0]) # Si hay dos paquetes, nos quedamos con el minimo
	
	for d in range(2, len(mercaderia)):
		G[d] = obtener_paquete_de_menor_cantidad(mercaderia[d] + G[d-2], G[d-1])

	return construir_elecciones(G, mercaderia)

def construir_elecciones(G, mercaderia):
	elecciones = []
	d = len(G) - 1 # Empiezo con el último paquete del arreglo de soluciones
	while ( d > 1 ):
		if mercaderia[d][1] + G[d-2][1] >= G[d-1][1]:
			elecciones.insert(0, mercaderia[d]) # hay un insert para que quede ordenado
			d -= 2
		else:
			d -= 1

	if G[1] == mercaderia[0]: # chequeo si el óptimo es el primer paquete
		elecciones.insert(0, mercaderia[0]) 
	else:
		elecciones.insert(0, mercaderia[1])
	
	return elecciones


# [(0,0), (1,1)]

mercaderia = [(C,2)  , (C,3), (C,8)]
# [(-1,-1), (0,1), (2,2)]

# [(C,1)  , (C,2)  , (C,2), (C,8)] -> 5
# [(-1,-1), (-1,-1), (0,1), (3,3)]

