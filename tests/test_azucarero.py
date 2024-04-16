import unittest


from implementacion.azucarero import Azucarero

class TestAzucarero(unittest.TestCase):
     
    azuquero = Azucarero  

    def setUp(self):
        self.azuquero = Azucarero(10)
    
    def test_DeberiaDevolverVerdaderoSiHaySuficienteAzucarEnElAzuquero(self) -> None:

        resultado = self.azuquero.hasAzucar(5)
         
        self.assertEquals(True, resultado)

        resultado = self.azuquero.hasAzucar(10)

        self.assertEquals(True, resultado)

    def test_DeberiaDevolverFalsoPorqueNoHaySuficienteAzucarEnElAzuquero(self) -> None:

        resultado = self.azuquero.hasAzucar(15)
         
        self.assertEquals(False, resultado)
    
    def test_DeberiaRestarAzucarAlAzuquero(self) -> None:

        self.azuquero.giveAzucar(5)
         
        self.assertEquals(5, self.azuquero.getCantidadAzucar())

        self.azuquero.giveAzucar(2)
         
        self.assertEquals(3, self.azuquero.getCantidadAzucar())

  


if __name__ == '__main__':
    unittest.main()
    

    