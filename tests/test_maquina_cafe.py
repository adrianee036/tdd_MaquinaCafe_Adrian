import unittest


from implementacion.vaso import Vaso
class TestVaso(unittest.TestCase):
    
    def test_DeberiaDevolverVerdaderoSiExistenVasos(self) -> None:
        vasosPequenos = Vaso(5,10)

        resultado = vasosPequenos.hasVasos(1)
         
        self.assertEquals(True, resultado)

    def test_DeberiaDevolverFalsoSiNoExistenVasos(self) -> None:
        vasosPequenos = Vaso(1,10)

        resultado = vasosPequenos.hasVasos(2)
         
        self.assertEquals(False, resultado)

    def test_DeberiaRestarCantidadDeVasos(self) -> None:
        vasosPequenos = Vaso(5,10)

        vasosPequenos.giveVasos(1)
         
        self.assertEquals(4, vasosPequenos.getCantidadVasos())



if __name__ == '__main__':
    unittest.main()
    

    