import unittest
from k_merge_dyc import k_merge_dyc
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

class TestKMerge(unittest.TestCase):

    def test_solo_una_lista(self):
        self.assertEqual(k_merge_dyc([l1]), l1)

    def test_dos_listas_vacias(self):
        self.assertEqual(k_merge_dyc([[],[]]), [])

    def test_dos_listas(self):
        self.assertEqual(k_merge_dyc([l1,l2]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dos_listas_iguales(self):
        self.assertEqual(k_merge_dyc([l1,l1]), [1, 1, 3, 3, 5, 5, 7, 7, 9, 9])
    
    def test_volumen(self):
        lista_de_listas, lista_ordenada = armar_lista_volumen(100,100)
        self.assertEqual(k_merge_dyc(lista_de_listas), lista_ordenada) 


if __name__ == '__main__':
    unittest.main()