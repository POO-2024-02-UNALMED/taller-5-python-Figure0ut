from .animal import Animal

class Ave(Animal):
    contador = 0 
    halcones = 0
    aguilas = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPlumas, zona=None, zoo=None):
        super().__init__(nombre, edad, habitat, genero, zona, zoo)
        self.colorPlumas = colorPlumas
        Ave.contador += 1
        Ave.listado.append(self)

    @classmethod
    def contar(cls):
        return cls.contador

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return cls(nombre, edad, "montañas", genero, colorPlumas="café glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return cls(nombre, edad, "montañas", genero, colorPlumas="blanco y amarillo")

    @classmethod
    def cantidadAves(cls):
        return cls.contador

    def movimiento(self):
        return "volar"

    def getColorPlumas(self):
        return self._color_plumas

    def setColorPlumas(self, color_plumas):
        self._color_plumas = color_plumas

    def toString(self):
        return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}"