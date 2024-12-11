from .animal import Animal

class Pez(Animal):
    contador = 0 
    salmones = 0
    bacalaos = 0
    listado = [] 

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas, zona=None, zoo=None):
        super().__init__(nombre, edad, habitat, genero, zona, zoo)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.contador += 1
        Pez.listado.append(self) 

    @classmethod
    def contar(cls):
        return cls.contador

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return cls(nombre, edad, "océano", genero, colorEscamas="rojo", cantidadAletas=6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return cls(nombre, edad, "océano", genero, colorEscamas="gris", cantidadAletas=6)

    @classmethod
    def cantidadPeces(cls):
        return cls.contador

    def movimiento(self):
        return "nadar"