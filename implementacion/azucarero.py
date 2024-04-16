class Azucarero:
    def __init__(self, cantidadDeAzucar):
        self.cantidadDeAzucar = cantidadDeAzucar

    def hasAzucar(self, cantidadDeAzucar):
        return cantidadDeAzucar <= self.cantidadDeAzucar
    
    def giveAzucar(self, cantidadDada):
        self.cantidadDeAzucar = self.cantidadDeAzucar - cantidadDada
        return self.cantidadDeAzucar
 
    def getCantidadAzucar(self):
        return self.cantidadDeAzucar
