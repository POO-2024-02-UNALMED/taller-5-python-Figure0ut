from .Animal import Animal

class Anfibio(Animal):
    contador = 0
    ranas = 0
    salamandras = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso, zona=None, zoo=None):
        super().__init__(nombre, edad, habitat, genero, zona, zoo)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.contador += 1
        Anfibio.listado.append(self) 

    @classmethod
    def contar(cls):
        return cls.contador

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return cls(nombre, edad, "selva", genero, colorPiel="rojo", venenoso=True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return cls(nombre, edad, "selva", genero, colorPiel="negro y amarillo", venenoso=False)

    @classmethod
    def cantidadAnfibios(cls):
        return cls.contador

    def movimiento(self):
        return "saltar"