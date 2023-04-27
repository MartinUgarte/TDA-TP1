import heapq

def k_merge_heap(arreglos_ordenados):
    h = []
    arreglo_resultado = []
    
    for i in range(len(arreglos_ordenados)):
        if len(arreglos_ordenados[i]) == 0: continue
        heapq.heappush(h,[arreglos_ordenados[i][0],i , 0])
     
    while len(h) != 0:
        minimo = heapq.heappop(h)
        arreglo_resultado.append(minimo[0])
        if minimo[2] < len(arreglos_ordenados[0]) -1:
            heapq.heappush(h,[arreglos_ordenados[minimo[1]][minimo[2]+1], minimo[1], minimo[2]+1]) 

    return arreglo_resultado
