class MaquinaCafe:
    vasoPequeno = ""

    def __init__(self, cafe, vasosPequenos, vasosMedianos, vasosGrandes, azucar):
        self.cafe = cafe
        self.vasosPequenos = vasosPequenos
        self.vasosMedianos = vasosMedianos
        self.vasosGrandes = vasosGrandes
        self.azucar = azucar

    def setCafetera(self, vasosPequenos):
        self.vasoPequeno = vasosPequenos

