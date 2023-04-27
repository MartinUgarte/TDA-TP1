import unittest
from k_merge_heap import k_merge_heap
import random

l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]

def armar_lista_volumen(cant_listas, cant_digitos):
    lista_final_ordenada = []
    lista_de_listas = []
    for i in range(cant_listas):
        lista_aux = []
        for i in range(cant_digitos):
            nro_random = random.randint(0,999)
            lista_aux.append(nro_random)
            lista_final_ordenada.append(nro_random)
        lista_aux.sort()
        lista_de_listas.append(lista_aux)
    lista_final_ordenada.sort()
    return lista_de_listas, lista_final_ordenada

class TestKMergeHeap(unittest.TestCase):

    def test_listas_vacias(self):
        self.assertEqual(k_merge_heap([[],[]]), [])
    
    def test_una_sola_lista(self):
        self.assertEqual(k_merge_heap([l2]), l2)

    def test_dos_listas(self):
        self.assertEqual(k_merge_heap([l2,l1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dos_listas_iguales(self):
        self.assertEqual(k_merge_heap([l2,l2]), [2, 2, 4, 4, 6, 6, 8, 8, 10, 10])

    def test_volumen(self): 
        lista_de_listas, lista_ordenada = armar_lista_volumen(100,100)
        self.assertEqual(k_merge_heap(lista_de_listas), lista_ordenada)



if __name__ == '__main__':
    unittest.main()