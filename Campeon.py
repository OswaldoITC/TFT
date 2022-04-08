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

    #Funcion imprime descripcion del campeon
    def descripcion(self):
        print("Nombre: " + self.nombre)
        print("Cantidad de rasgos: " + str(self.nRasgos))
        print("Rasgos:")
        for rasgo in self.rasgos:
            print("      ",rasgo)
        print("Costo: " + str(self.costo))