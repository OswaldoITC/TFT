#Imports
from Campeon import Campeon
from Lector import separaPalabras

#Open files and ignore first line
fCampeones = open("Files/Campeones.txt", "r")
fCampeones.readline()
fRasgos = open("Files/Rasgos.txt", "r")
fRasgos.readline()

#Listas campeones y rasgos
campeones = []
rasgos = []
#campeon = Campeon("Sylas",2,{"Mercenario","Maton"},3)
##Problema con el constructor pide a fuerza parametros
campeon = Campeon("",0,{""},0)
for linea in fCampeones:
    palabras = separaPalabras(linea)
    r = []

    campeon.setNombre(palabras[0])
    #print(campeon.getNombre())
    campeon.setNRasgos(int(palabras[1]))
    #print(campeon.getNRasgos())
    if palabras[1+campeon.getNRasgos()+1] != "":
        campeon.setCosto(int(palabras[1+campeon.getNRasgos()+1]))
    else:
        campeon.setCosto(0)
    #reunir todos los rasgos
    for i in range(2,campeon.getNRasgos()+2):
        r.append(int(palabras[i]))
    campeon.setRasgos(r)
    #campeon.descripcion()
    campeones.append(campeon)
    #campeon.descripcion()
for champ in campeones:
    print(champ.descripcion())

#Close files
fCampeones.close()
fRasgos.close()