class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona=None, zoo=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = zona
        self.zoo = zoo
        Animal.totalAnimales += 1  

    @classmethod
    def totalPorTipo(cls):
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .pez import Pez
        from .anfibio import Anfibio

        return {
            "Mamíferos": Mamifero.contar(),
            "Aves": Ave.contar(),
            "Reptiles": Reptil.contar(),
            "Peces": Pez.contar(),
            "Anfibios": Anfibio.contar()
        }
    def toString(self):
        if self.zona and self.zoo:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}, la zona en la que me ubico es {self.zona.nombre}, en el {self.zoo.nombre}."
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}."

    def movimiento(self):
        return "desplazarse"
    
