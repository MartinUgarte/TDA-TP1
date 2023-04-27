import unittest
from contrabando_dinamica import obtener_paquetes_dinamica

PRODUCTO_UNO = "cigarrillos"
PRODUCTO_DOS = "vodka"
PRODUCTO_TRES = "naipes"

class TestContrabandoDinamica(unittest.TestCase):

    def test_sin_paquetes(self):
        mercaderia = []
        pedidos = []
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), [])
    
    def test_un_paquete(self):
        mercaderia = [(PRODUCTO_UNO, 8)]
        pedidos = [(PRODUCTO_UNO, 6)]
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), [(PRODUCTO_UNO, 8)])

    def test_dos_paquetes_mismo_producto(self):
        mercaderia = [(PRODUCTO_UNO, 5), (PRODUCTO_UNO, 8)]
        pedidos = [(PRODUCTO_UNO, 5)]
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), [(PRODUCTO_UNO, 5)])
    
    @unittest.skip("No implementado")
    def test_mismo_producto(self):
        mercaderia = [(PRODUCTO_UNO, 2), (PRODUCTO_UNO, 8), (PRODUCTO_UNO, 3), (PRODUCTO_UNO, 6)]
        pedidos = [(PRODUCTO_UNO, 5)]
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), [(PRODUCTO_UNO, 3), (PRODUCTO_UNO, 2)])

if __name__ == "__main__":
    unittest.main()