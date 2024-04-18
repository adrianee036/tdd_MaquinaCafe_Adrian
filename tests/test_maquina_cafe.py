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
        self.vasosPequeno = Vaso(5,3)
        self.vasosMediano = Vaso(5,5)
        self.vasosGrande = Vaso(5,7)
        self.azucarero = Azucarero(20)

        self.maquinaDeCafe = MaquinaCafe()
        self.maquinaDeCafe.setCafetera(self.cafetera)
        self.maquinaDeCafe.setVasosPequeno(self.vasosPequeno)
        self.maquinaDeCafe.setVasosMediano(self.vasosMediano)
        self.maquinaDeCafe.setVasosGrande(self.vasosGrande)
        self.maquinaDeCafe.setAzucarero(self.azucarero)

    def test_DeberiaDevolverUnVasoPequeno(self) -> None:

        vaso = self.maquinaDeCafe.getTipoDeVaso("pequeno")

        self.assertEquals(self.maquinaDeCafe.vasosPequenos,vaso)

    def test_DeberiaDevolverUnVasoMediano(self) -> None:

        vaso = self.maquinaDeCafe.getTipoDeVaso("mediano")

        self.assertEquals(self.maquinaDeCafe.vasosMedianos,vaso)
    
    def test_DeberiaDevolverUnVasoGrande(self) -> None:

        vaso = self.maquinaDeCafe.getTipoDeVaso("grande")

        self.assertEquals(self.maquinaDeCafe.vasosGrandes,vaso)

    def test_DeberiaDevolverNoHayVasos(self) -> None:

        vaso = self.maquinaDeCafe.getTipoDeVaso("pequeno")

        resultado = self.maquinaDeCafe.getVasoDeCafe(vaso,10,2)

        self.assertEquals("No hay Vasos",resultado)

    def test_DeberiaDevolverNoHayCafe(self) -> None:

        cafetera = Cafetera(1)
        self.maquinaDeCafe.setCafetera(cafetera)

        vaso = self.maquinaDeCafe.getTipoDeVaso("pequeno")
        
        resultado = self.maquinaDeCafe.getVasoDeCafe(vaso,1,2)

        self.assertEquals("No hay Cafe",resultado)

    def test_DeberiaDevolverNoHayAzucar(self) -> None:

        self.azucarero = Azucarero(2)
        self.maquinaDeCafe.setAzucarero(self.azucarero)

        vaso = self.maquinaDeCafe.getTipoDeVaso("pequeno")
        
        resultado = self.maquinaDeCafe.getVasoDeCafe(vaso,1,3)

        self.assertEquals("No hay Azucar",resultado) 
    
    def test_DeberiaRestarCafe(self) -> None:
        vaso = self.maquinaDeCafe.getTipoDeVaso("grande")
        
        self.maquinaDeCafe.getVasoDeCafe(vaso,1,3)

        resultado = self.maquinaDeCafe.getCafetera().getCantidadCafe()

        self.assertEquals(43,resultado) 
    
    def test_DeberiaRestarVaso(self) -> None:
        vaso = self.maquinaDeCafe.getTipoDeVaso("grande")
        
        self.maquinaDeCafe.getVasoDeCafe(vaso,1,3)

        resultado = self.maquinaDeCafe.getVasosGrande().getCantidadVasos()

        self.assertEquals(4,resultado) 

    def test_DeberiaRestarAzucar(self) -> None:
        vaso = self.maquinaDeCafe.getTipoDeVaso("pequeno")
        
        self.maquinaDeCafe.getVasoDeCafe(vaso,1,3)

        resultado = self.maquinaDeCafe.getAzucarero().getCantidadAzucar()

        self.assertEquals(17,resultado)

    def test_DeberiaDevolverFelicitaciones(self) -> None:
        vaso = self.maquinaDeCafe.getTipoDeVaso("pequeno")

        resultado = self.maquinaDeCafe.getVasoDeCafe(vaso,1,3)

        self.assertEquals("Felicitaciones",resultado) 

    





if __name__ == '__main__':
    unittest.main()