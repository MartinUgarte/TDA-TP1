def merge(arreglo_uno, arreglo_dos):
    arreglo_resultado = []
    i, j = 0, 0

    for _ in range(len(arreglo_uno) + len(arreglo_dos)):
        if i == len(arreglo_uno):
            arreglo_resultado.append(arreglo_dos[j])
            j += 1
        elif j == len(arreglo_dos):
            arreglo_resultado.append(arreglo_uno[i])
            i += 1
        elif arreglo_uno[i] < arreglo_dos[j]:
            arreglo_resultado.append(arreglo_uno[i])
            i += 1
        else:
            arreglo_resultado.append(arreglo_dos[j])
            j += 1 
    
    return arreglo_resultado

def k_merge_dyc(arreglos_ordenados):
    if len(arreglos_ordenados) == 0:
        return []
    if len(arreglos_ordenados) == 1:
        return arreglos_ordenados[0]
    
    medio = len(arreglos_ordenados) // 2
    arreglo_uno = k_merge_dyc(arreglos_ordenados[0: medio])
    arreglo_dos = k_merge_dyc(arreglos_ordenados[medio: len(arreglos_ordenados)])

    return merge(arreglo_uno , arreglo_dos)
