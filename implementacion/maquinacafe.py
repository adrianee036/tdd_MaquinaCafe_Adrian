from implementacion.vaso import Vaso
from implementacion.cafetera import Cafetera
from implementacion.azucarero import Azucarero

class MaquinaCafe:

    cafe = Cafetera(0)
    vasosPequenos = Vaso(0,0)
    vasosMedianos = Vaso(0,0)
    vasosGrandes = Vaso(0,0)
    azucar = Azucarero(0)


    def setCafetera(self, cantidadCafe):
        self.cafe = cantidadCafe
    
    def setVasosPequeno(self, vasosPequenos):
        self.vasosPequenos = vasosPequenos

    def setVasosMediano(self, vasosMedianos):
        self.vasosMedianos = vasosMedianos
    
    def setVasosGrande(self, vasosGrandes):
        self.vasosGrandes = vasosGrandes

    def setAzucarero(self, cantidadAzucar):
        self.azucar = cantidadAzucar
    
    
    def getCafetera(self):
        return self.cafe
    
    def getVasosPequeno(self):
        return self.vasosPequenos
    
    def getAzucarero(self):
        return self.azucar
    
    def getTipoDeVaso(self, tipo):
        if tipo == "pequeno":
            return self.vasosPequenos
        elif tipo == "mediano":
            return self.vasosMedianos
        elif tipo == "grande":
            return self.vasosGrandes
        else:
            return None
    
    def getVasoDeCafe(self, vaso, cantidadDeVasos, cantidadDeAzucar):        

        if self.vasosPequenos == vaso:
            if cantidadDeVasos > self.vasosPequenos.cantidadVasos:
                return "No hay Vasos"
            elif self.cafe.cantidadCafe < self.vasosPequenos.contenido:
                return "No hay Cafe"
            elif cantidadDeAzucar > self.azucar.cantidadDeAzucar:
                return "No hay Azucar" 
            else: 
                self.cafe.cantidadCafe =  self.cafe.cantidadCafe - self.vasosPequenos.contenido
                self.vasosPequenos.cantidadVasos =  self.vasosPequenos.cantidadVasos - cantidadDeVasos
                self.azucar.cantidadDeAzucar =  self.azucar.cantidadDeAzucar - cantidadDeAzucar
                return "Felicitaciones"
            
        elif self.vasosMedianos == vaso:
            if cantidadDeVasos > self.vasosMedianos.cantidadVasos:
                return "No hay Vasos"
            elif self.cafe.cantidadCafe < self.vasosMedianos.contenido:
                return "No hay Cafe"
            elif cantidadDeAzucar > self.azucar.cantidadDeAzucar:
                return "No hay Azucar" 
                
            
        elif self.vasosGrandes == vaso:
            if cantidadDeVasos > self.vasosGrandes.cantidadVasos:
                return "No hay Vasos"
            elif self.cafe.cantidadCafe < self.vasosGrandes.contenido:
                return "No hay Cafe"
            elif cantidadDeAzucar > self.azucar.cantidadDeAzucar:
                return "No hay Azucar" 
            
        
            

    
    


