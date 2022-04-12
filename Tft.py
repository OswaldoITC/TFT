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

campeon = Campeon("",0,{""},0)
for linea in fCampeones:
    #print(linea)
    palabras = separaPalabras(linea)
    r = []

    campeon.setNombre(palabras[0])
    campeon.setNRasgos(int(palabras[1]))
    if palabras[1+campeon.getNRasgos()+1] != "":
        campeon.setCosto(int(palabras[1+campeon.getNRasgos()+1]))
    else:
        campeon.setCosto(0)
    #reunir todos los rasgos
    for i in range(2,campeon.getNRasgos()+2):
        r.append(int(palabras[i]))
    campeon.setRasgos(r)
    campeones.append(Campeon(campeon.getNombre(),campeon.getNRasgos(),campeon.getRasgos(),campeon.getCosto()))

#Close files
fCampeones.close()
fRasgos.close()