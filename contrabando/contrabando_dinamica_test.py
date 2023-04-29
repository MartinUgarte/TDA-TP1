import unittest
from contrabando_dinamica import obtener_paquetes_dinamica

PRODUCTO_UNO = "cigarrillos"
PRODUCTO_DOS = "vodka"
PRODUCTO_TRES = "naipes"

class TestContrabandoDinamica(unittest.TestCase):

    def test_sin_paquetes(self):
        mercaderia = {}
        pedidos = {}
        coima_esperada = {}
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), coima_esperada)
    
    def test_un_paquete(self):
        mercaderia = {PRODUCTO_UNO: [8]}
        pedidos = { PRODUCTO_UNO: 6 } 
        coima_esperada = {PRODUCTO_UNO: [8]}
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), coima_esperada)

    def test_dos_paquetes_mismo_producto(self):
        mercaderia = { PRODUCTO_UNO: [5, 8] }
        pedidos = { PRODUCTO_UNO: 5 }
        coima_esperada = {PRODUCTO_UNO: [5]}
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), coima_esperada)
    
    def test_mismo_producto(self):
        mercaderia = { PRODUCTO_UNO: [8, 3, 2] }
        pedidos = { PRODUCTO_UNO: 5 }
        coima_esperada = { PRODUCTO_UNO: [2, 3] }  
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), coima_esperada)

    def test_diferentes_productos(self):
        mercaderia = { PRODUCTO_UNO: [3, 12], PRODUCTO_DOS: [4, 9] }
        pedidos = { PRODUCTO_UNO: 2, PRODUCTO_DOS: 7 }
        coima_esperada = { PRODUCTO_UNO: [3], PRODUCTO_DOS: [9] }
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), coima_esperada)

    def test_varios_productos(self):
        mercaderia = { PRODUCTO_UNO: [4, 12, 3], PRODUCTO_DOS: [9, 9, 6], PRODUCTO_TRES: [2, 8, 3] }
        pedidos = { PRODUCTO_UNO: 2, PRODUCTO_DOS: 8, PRODUCTO_TRES: 5 }
        coima_esperada = { PRODUCTO_UNO: [3], PRODUCTO_DOS: [9], PRODUCTO_TRES: [3, 2] }
        self.assertEqual(obtener_paquetes_dinamica(pedidos, mercaderia), coima_esperada)
        
if __name__ == "__main__":
    unittest.main()