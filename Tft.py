#Imports
from Campeon import Campeon
from Rasgo import Rasgo
from Lector import extraerRasgos, separaPalabras
from Lector import extraeCampeones

#Extracción de campeones
campeones = extraeCampeones("Files/Campeones.txt")

#Extraer rasgos de Rasgos.txt y guardarlos en lista rasgos
rasgos = extraerRasgos("Files/Rasgos.txt")

for rasgo in rasgos:
    rasgo.funcDescripcion()