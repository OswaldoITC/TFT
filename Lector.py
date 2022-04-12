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