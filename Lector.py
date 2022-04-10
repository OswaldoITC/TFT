from cv2 import line


def separaPalabras(linea):
    palabras = []
    

    while len(linea) > 1:
        #verificar que aún haya una palabra delante
        if linea[1:].find(",") != -1:
            #eliminar primer caracter
            linea = linea[1:]
            comaPos = linea.find(",")
            palabras.append(linea[0:comaPos])
            #print(linea[0:comaPos])
            linea = linea[comaPos:]
        else:
            #print("print 1")
            #print(linea)
            #eliminar primer caracter
            linea = linea[1:len(linea)]
            #print("print 2")
            #print(linea)
            #eliminar llave cierra
            linea = linea[0:len(linea)-2]
            #print("print 3")
            #print(linea)
            palabras.append(linea)
            linea = ""
    #regresar una lista con las palabras encontradas
    return palabras