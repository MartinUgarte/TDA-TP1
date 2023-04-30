def obtener_paquetes_dinamica(pedido, mercaderia):
	solucion = {}
	for coima, cantidad in pedido.items():
		m = [[0 for _ in range(max(mercaderia[coima])+1)] for _ in range(len(mercaderia[coima])+1)]
		for i in range(1, len(m)):
			valor_elemento = mercaderia[coima][i-1] 
			for j in range(1, len(m[i])):
				if m[i][j-1] == cantidad:
					m[i][j] = cantidad
				elif valor_elemento > j:
					m[i][j] = m[i-1][j] 
				elif valor_elemento >= cantidad: 
					m[i][j] = min_condicionado( valor_elemento, m[i-1][j], cantidad)
				else:
					m[i][j] = min_condicionado(m[i-1][j-valor_elemento] + valor_elemento, m[i-1][j], cantidad)
		solucion[coima] = reconstruir_solucion(m, mercaderia[coima])

	return solucion

def reconstruir_solucion(m, paquetes):
	solucion = []
	i, j = len(m)-1, len(m[0])-1
	while m[i][j] != 0:
		if m[i][j] == m[i-1][j]:
			i -= 1
			continue
		elif m[i][j] == m[i-1][j-paquetes[i-1]] + paquetes[i-1]:
			j -= paquetes[i-1]
		else: 
			j = m[i][j] - paquetes[i-1]
		solucion.append(paquetes[i-1])
		i -= 1

	return solucion

def min_condicionado(optimo_a_evaluar, optimo_anterior, condicion): 
	# los dos optimos son iguales
	if optimo_a_evaluar == optimo_anterior: return optimo_a_evaluar

	if optimo_anterior == condicion: return optimo_anterior
	
	# ninguno de los dos cumple la condición
	if optimo_a_evaluar < condicion and optimo_anterior < condicion: return optimo_a_evaluar
	
	# optimo_a_evaluar es mejor y cumple
	if optimo_a_evaluar < optimo_anterior and optimo_a_evaluar >= condicion: return optimo_a_evaluar
	
	# optimo_anterior es mejor y cumple
	if optimo_a_evaluar > optimo_anterior and optimo_anterior >= condicion: return optimo_anterior

	# optimo_anterior no cumple y optimo_a_evaluar si pero optimo_a_evaluar es mas grande
	if optimo_a_evaluar > optimo_anterior and optimo_a_evaluar >= condicion and optimo_anterior < condicion: 
		return optimo_a_evaluar
	
	# optimo_anterior no cumple y optimo_a_evaluar si pero optimo_a_evaluar es mas grande
	if optimo_a_evaluar < optimo_anterior and optimo_a_evaluar < condicion and optimo_anterior >= condicion: 
		return optimo_anterior


# def imprimir_matriz(m):
# 	for f in range(len(m)):
# 		for c in range(len(m[0])):
# 			print('|', str(m[f][c]).center(0), '|', end='')
# 		print()
# 	print()

