#Clase Campeon
#Objeto para guardar descripcion de campeones de tft
class Campeon:
    #Constructor sin parametros
    def __init__(self):
        self.nombre = "Champ"
        self.nRasgos = 0
        self.rasgos = {"Empty"}
        self.costo = 0

    #Constructor con parametros
    def __init__(self, nombre, nRasgos, rasgos, costo):
        self.nombre = nombre
        self.nRasgos = nRasgos
        self.rasgos = rasgos
        self.costo = costo
    #sets y gets
    def setNombre(self, nombre):
        self.nombre = nombre
    def setNRasgos(self, nRasgos):
        self.nRasgos = nRasgos
    def setRasgos(self, rasgos):
        self.rasgos = rasgos
    def setCosto(self, costo):
        self.costo = costo
    def getNombre(self):
        return self.nombre
    def getNRasgos(self):
        return self.nRasgos
    def getRasgos(self):
        return self.rasgos
    def getCosto(self):
        return self.costo

    #Funcion imprime descripcion del campeon
    def descripcion(self):
        print("Nombre: " + self.nombre)
        print(str(self.nRasgos) + " rasgos:")
        for rasgo in self.rasgos:
            print("      ",rasgo)
        print("Costo: " + str(self.costo))