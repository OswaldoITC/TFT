#Imports
from Campeon import Campeon
from Rasgo import Rasgo

#separaPalabras
#Funcion para crear una lista con las palabras contenidas
#en una linea de texto previamente leida de un archivo
#Palabras contenidas dentro de llaves y separadas por comas entre ellas
def separaPalabras(linea):
    palabras = []
    #eliminar salto de linea que contienen todas excepto la ultima del archivo
    linea = linea.rstrip('\n')

    while len(linea) > 0 and linea != " ":
        #verificar que aún haya una palabra delante
        if linea[1:].find(",") != -1:
            #eliminar primer caracter
            linea = linea[1:]
            comaPos = linea.find(",")
            palabras.append(linea[0:comaPos])
            #print(linea[0:comaPos])
            linea = linea[comaPos:]
        else:
            #eliminar primer caracter
            linea = linea[1:]

            #eliminar llave cierra
            linea = linea[0:len(linea)-1]
            palabras.append(linea)
            linea = ""
    return palabras

#extraerCampeones
#Funcion para pasar los datos de campeones de un archivo txt a una lista
def extraeCampeones(fileName):
    #Open Campeones.txt and ignore first line
    fCampeones = open("Files/Campeones.txt", "r")
    fCampeones.readline()
    #Listas campeones
    campeones = []
    #Extraer campeones de Campeones.txt y guardarlos en lista campeones
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
    #Close file Campeones.txt
    fCampeones.close()
    return campeones

#extraerRasgos
#Funcion para pasar los datos de rasgos de un archivo txt a una lista
def extraerRasgos(fileName):
    #Open Rasgos.txt and ignore first line
    fRasgos = open(fileName, "r")
    fRasgos.readline()
    #Lista rasgos para datos extraidos de txt
    rasgos = []

    #Extraer rasgos de Rasgos.txt y guardarlos en lista rasgos
    rasgo = Rasgo("rasgo",0,"Empty","empty",{})
    for linea in fRasgos:
        #print(linea)
        palabras = separaPalabras(linea)
        r = []

        rasgo.setNombre(palabras[0])
        rasgo.setId(int(palabras[1]))
        rasgo.setDescripcion(palabras[2])
        rasgo.setAlcance(palabras[3])

        #Pendiente niveles
        niveles = []
        nivelesAux = palabras[4]
        while nivelesAux:
            if nivelesAux.find("-") != -1:
                niveles.append(int(nivelesAux[0:nivelesAux.find("-")]))
                nivelesAux = nivelesAux[nivelesAux.find("-")+1:]
            else:
                niveles.append(nivelesAux)
                nivelesAux = ""

        rasgo.setNiveles(niveles)
        rasgos.append(Rasgo(rasgo.getNombre(),rasgo.getId(),rasgo.getDescripcion(),rasgo.getAlcance(),rasgo.getNiveles()))

    #Close file Rasgos.txt
    fRasgos.close()
    return rasgos