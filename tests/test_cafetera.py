import unittest


from implementacion.cafetera import Cafetera
class TestCafetera(unittest.TestCase):
    
    def test_DeberiaDevolverVerdaderoSiExisteCafe(self) -> None:
        cafetera = Cafetera(10)

        resultado = cafetera.hasCafe(5)
         
        self.assertEquals(True, resultado)

    def test_DeberiaDevolverFalsoSiNoExisteCafe(self) -> None:
        cafetera = Cafetera(10)

        resultado = cafetera.hasCafe(11)
         
        self.assertEquals(False, resultado)
    
    def test_DeberiaRestarCantidadDeVasos(self) -> None:
        cafetera = Cafetera(10)

        cafetera.giveCafe(7)
         
        self.assertEquals(3, cafetera.getCantidadCafe())

        
if __name__ == '__main__':
    unittest.main()
    

    