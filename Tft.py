#Imports
from Campeon import Campeon

#Open files and ignore first line
campeones = open("Files/Campeones.txt", "r")
campeones.readline()
rasgos = open("Files/Rasgos.txt", "r")
rasgos.readline()

campeon = Campeon("Sylas",2,{"Mercenario","Maton"},3)
campeon.descripcion()