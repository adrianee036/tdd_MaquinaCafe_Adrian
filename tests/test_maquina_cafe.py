import unittest


from implementacion.maquinacafe import MaquinaCafe
from implementacion.cafetera import Cafetera
from implementacion.vaso import Vaso
from implementacion.azucarero import Azucarero
class TestMaquinaDeCafe(unittest.TestCase):
    cafetera = Cafetera
    vasosPequeno = Vaso
    vasosMediano = Vaso
    vasosGrande = Vaso
    azucarero = Azucarero
    maquinaDeCafe = MaquinaCafe

    def setUp(self) -> None:
        self.cafetera = Cafetera(50)
        self.vasosPequeno = Vaso(5,10)
        self.vasosMediano = Vaso(5,20)
        self.vasosGrande = Vaso(5,30)
        self.azucarero = Azucarero(20)

        self.maquinaDeCafe = MaquinaCafe()
        self.maquinaDeCafe.setCafetera(self.cafetera)






if __name__ == '__main__':
    unittest.main()