import unittest
from contrabando_greedy import obtener_paquetes_greedy

PRODUCTO_UNO = "cigarrillos"
PRODUCTO_DOS = "vodka"
PRODUCTO_TRES = "hojas de menta"

class TestContrabandoGreedy(unittest.TestCase):

    def test_sin_paquetes(self):
        mercaderia = []
        pedidos = []
        self.assertEqual(obtener_paquetes_greedy(pedidos, mercaderia), [])

    def test_un_paquete(self):
        mercaderia = [(PRODUCTO_UNO, 8)]
        pedidos = [(PRODUCTO_UNO, 6)]
        self.assertEqual(obtener_paquetes_greedy(pedidos, mercaderia), [(PRODUCTO_UNO, 8)])

    def test_dos_paquetes_mismo_producto(self):
        mercaderia = [(PRODUCTO_UNO, 5), (PRODUCTO_UNO, 8)]
        pedidos = [(PRODUCTO_UNO, 5)]
        self.assertEqual(obtener_paquetes_greedy(pedidos, mercaderia), [(PRODUCTO_UNO, 5)])

    def test_mismo_producto(self):
        mercaderia = [(PRODUCTO_UNO, 2), (PRODUCTO_UNO, 8), (PRODUCTO_UNO, 3), (PRODUCTO_UNO, 6)]
        pedidos = [(PRODUCTO_UNO, 5)]
        self.assertEqual(obtener_paquetes_greedy(pedidos, mercaderia), [(PRODUCTO_UNO, 3), (PRODUCTO_UNO, 2)])
    
    def test_diferentes_productos(self):
        mercaderia = [(PRODUCTO_UNO, 3), (PRODUCTO_DOS, 4), (PRODUCTO_DOS, 9), (PRODUCTO_UNO, 12)]
        pedidos = [(PRODUCTO_UNO,2), (PRODUCTO_DOS, 7)]
        self.assertEqual(obtener_paquetes_greedy(pedidos, mercaderia), [(PRODUCTO_UNO, 3), (PRODUCTO_DOS, 9)])

    def test_varios_productos(self):
        mercaderia = [(PRODUCTO_DOS, 9), (PRODUCTO_TRES, 2), (PRODUCTO_UNO, 4), (PRODUCTO_UNO, 12), (PRODUCTO_DOS, 9), (PRODUCTO_TRES, 8), (PRODUCTO_TRES, 3), (PRODUCTO_DOS, 6), (PRODUCTO_UNO, 3)]
        pedidos = [(PRODUCTO_TRES, 5), (PRODUCTO_UNO, 2), (PRODUCTO_DOS, 8)]
        self.assertEqual(obtener_paquetes_greedy(pedidos, mercaderia), [(PRODUCTO_TRES, 3), (PRODUCTO_TRES, 2), (PRODUCTO_UNO, 3), (PRODUCTO_DOS, 9)])

if __name__ == "__main__":
    unittest.main()