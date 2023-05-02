import unittest
from contrabando_greedy import obtener_paquetes_greedy
from armar_set import armar_set_datos
from constantes import *

class TestContrabandoGreedy(unittest.TestCase):

    def test_sin_paquetes(self):
        mercaderia = {}
        pedidos = {}
        coima_esperada = {}
        self.assertEqual(obtener_paquetes_greedy(pedidos, mercaderia), coima_esperada)

    def test_un_paquete(self):
        mercaderia = { PRODUCTO_UNO: [8] }
        pedidos = { PRODUCTO_UNO: 6 }
        self.assertTrue(sum(obtener_paquetes_greedy(pedidos, mercaderia)[PRODUCTO_UNO]) >= pedidos[PRODUCTO_UNO])

    def test_dos_paquetes_mismo_producto(self):
        mercaderia = { PRODUCTO_UNO: [5, 8] }
        pedidos = { PRODUCTO_UNO: 5 }
        self.assertTrue(sum(obtener_paquetes_greedy(pedidos, mercaderia)[PRODUCTO_UNO]) >= pedidos[PRODUCTO_UNO])

    def test_mismo_producto(self):
        mercaderia = { PRODUCTO_UNO: [2, 8, 3] }
        pedidos = { PRODUCTO_UNO: 5 }
        self.assertTrue(sum(obtener_paquetes_greedy(pedidos, mercaderia)[PRODUCTO_UNO]) >=  pedidos[PRODUCTO_UNO])
    
    def test_diferentes_productos(self):
        mercaderia = { PRODUCTO_UNO: [3, 12], PRODUCTO_DOS: [4, 9] }
        pedidos = { PRODUCTO_UNO: 2, PRODUCTO_DOS: 7 }
        for producto in pedidos:
            self.assertTrue(sum(obtener_paquetes_greedy(pedidos, mercaderia)[producto]) >= pedidos[producto])

    def test_varios_productos(self):
        mercaderia = { PRODUCTO_UNO: [4, 12, 3], PRODUCTO_DOS: [9, 9, 6], PRODUCTO_TRES: [2, 8, 3] }
        pedidos = { PRODUCTO_TRES: 5, PRODUCTO_UNO: 2, PRODUCTO_DOS: 8 }
        for producto in pedidos:
            self.assertTrue(sum(obtener_paquetes_greedy(pedidos, mercaderia)[producto]) >= pedidos[producto])

    def test_volumen(self):
        pedido, mercaderia, solucion = armar_set_datos(PRODUCTOS, VOLUMEN)
        obtenido = obtener_paquetes_greedy(pedido, mercaderia)
        for producto in pedido:
            self.assertTrue(sum(obtenido[producto]) >= sum(solucion[producto]))
        
    def test_super_volumen(self):
        for _ in range(ITERACIONES_VOLUMEN):
            pedido, mercaderia, solucion = armar_set_datos(PRODUCTOS, VOLUMEN)
            obtenido = obtener_paquetes_greedy(pedido, mercaderia)
            for producto in pedido:
                self.assertTrue(sum(obtenido[producto]) >= sum(solucion[producto]))

if __name__ == "__main__":
    unittest.main()