class Cafetera:
    def __init__(self, cantidadCafe):
        self.cantidadCafe = cantidadCafe

    def hasCafe(self, cantidadCafe):
        return cantidadCafe <= self.cantidadCafe
    
    def giveCafe(self, cantidadDada):
        self.cantidadCafe = self.cantidadCafe - cantidadDada
        return self.cantidadCafe
 
    def getCantidadCafe(self):
        return self.cantidadCafe
