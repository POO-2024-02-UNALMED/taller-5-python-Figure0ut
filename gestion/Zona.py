from .zoologico import Zoologico

class Zona:
    def __init__(self, nombre, zoo):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def __init__(self):
        pass
    
    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)
