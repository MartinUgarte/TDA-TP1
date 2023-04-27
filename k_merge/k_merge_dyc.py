# K-MERGE por División y Conquista
import random

def k_merge_dyc(arreglos_ordenados):
    if len(arreglos_ordenados) == 0:
        return []
    if len(arreglos_ordenados) == 1:
        return arreglos_ordenados[0]
    
    medio = len(arreglos_ordenados) // 2
    arreglo_uno = k_merge_dyc(arreglos_ordenados[0: medio])
    arreglo_dos = k_merge_dyc(arreglos_ordenados[medio: len(arreglos_ordenados)])

    return mergear(arreglo_uno, arreglo_dos)

def mergear(arreglo_uno, arreglo_dos):
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

# - TESTS - #

def main():

    l0 = []
    l1 = [1, 3, 5, 7, 9]
    l2 = [2, 4, 6, 8, 10]
    l3 = [1, 13, 15, 17, 19]

    assert k_merge_dyc(l0) == []
    assert k_merge_dyc([l1]) == l1
    assert k_merge_dyc([l0,l1]) == l1
    assert k_merge_dyc([l1,l2]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert k_merge_dyc([l1, l2, l3]) == [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 17, 19]
    assert k_merge_dyc([l1, l1]) == [1, 1, 3, 3, 5, 5, 7, 7, 9, 9]

main()