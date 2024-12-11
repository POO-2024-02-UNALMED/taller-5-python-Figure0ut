from .animal import Animal

class Reptil(Animal):
    contador = 0 
    iguanas = 0
    serpientes = 0
    listado = []  

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola, zona=None, zoo=None):
        super().__init__(nombre, edad, habitat, genero, zona, zoo)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.contador += 1
        Reptil.listado.append(self) 

    @classmethod
    def contar(cls):
        return cls.contador

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return cls(nombre, edad, "humedal", genero, colorEscamas="verde", largoCola=3)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return cls(nombre, edad, "jungla", genero, colorEscamas="blanco", largoCola=1)

    @classmethod
    def cantidadReptiles(cls):
        return cls.contador

    def movimiento(self):
        return "reptar"