class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def __init__(self):
        pass
    
    def agregarZona(self, zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for zona in self.zonas:
            totalAnimales += zona.cantidadAnimales() 
        return totalAnimales