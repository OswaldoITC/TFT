#Clase Campeon
#Objeto para guardar descripcion de campeones de tft
class Rasgo:
    #Constructor sin parametros
    def __init__(self):
        self.nombre = "Rasgo"
        self.id = 0
        self.descripcion = "Empty"
        self.alcance = "Empty"
        self.niveles = {}

    #Constructor con parametros
    def __init__(self, nombre, id, descripcion, alcance, niveles):
        self.nombre = nombre
        self.id = id
        self.descripcion = descripcion
        self.alcance = alcance
        self.niveles = niveles
    #sets y gets
    def setNombre(self, nombre):
        self.nombre = nombre
    def setId(self, id):
        self.id = id
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    def setAlcance(self, alcance):
        self.alcance = alcance
    def setNiveles(self, niveles):
        self.niveles = niveles
    def getNombre(self):
        return self.nombre
    def getId(self):
        return self.id
    def getDescripcion(self):
        return self.descripcion
    def getAlcance(self):
        return self.alcance
    def getNiveles(self):
        return self.niveles

    #Funcion imprime descripcion del rasgo
    def funcDescripcion(self):
        print("Nombre: " + self.nombre)
        print("Id: " + str(self.id))
        print("Descripcion: " + self.descripcion)
        print("Alcance: " + self.alcance)
        print("Niveles:")
        for nivel in self.niveles:
            print("      ", nivel)