class Vaso:
    def __init__(self, cantidadVasos, contenido):
        self.cantidadVasos = cantidadVasos
        self.contenido = contenido

    def hasVasos(self, cantidadVasos):
        return cantidadVasos <= self.cantidadVasos
    
    def giveVasos(self, cantidadDada):
        self.cantidadVasos = self.cantidadVasos - cantidadDada
        return self.cantidadVasos
 
    def getCantidadVasos(self):
        return self.cantidadVasos
