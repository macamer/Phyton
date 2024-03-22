## Ficheros ##
''' LEER FICHERO EN WEB (no funciona)
from pyodide.http import pyfetch

import pandas as pd

filename = "fichero.txt"

async def download(url, filename):

    response = await pyfetch(url)

    if response.status == 200:

        with open(filename, "wb") as f:

            f.write(await response.bytes())

await download(filename, "fichero.txt")

print("done")
'''
#leer fichero local 
filename = "intermedio/fichero.txt"

def read_local_file(filename):
    with open(filename, "r") as f: #si solo se pone open, habrá que cerrar después el archivo (el with lo hace automatico)
        contents = f.read()
    return contents
try:
    file_contents = read_local_file(filename)
    print(file_contents)
except Exception as ex:
    print(ex)

#ver info del archivo
file1 = open(filename, "r")
print(file1.name)
print(file1.mode) #si es 'r' o 'w'

#se pueden asignar a una variable
fileContent = file1.read()
print(fileContent)
print(type(fileContent))

#y se cierra -- siempre se debe cerrar (con el with se hace solo)
file1.close()

#verificar que se ha cerrado
file1.closed

#se puede leer parte del archivo
with open(filename, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

#leer una linea
with open(filename, "r") as file1:
    print("first line: " + file1.readline())

#seleccionar caracteres de esa linea
with open(filename, "r") as file1:
    print(file1.readline(4)) #no lee hasta el final
    print(file1.read(6)) #lee los siguientes carácteres

#se puede usar un loop para leer el fichero
with open(filename, "r") as file1:
    i = 0
    for line in file1:
        print("Iteration", str(i), " :", line)
        i = i + 1

#cuando se guarda como una lista se puede acceder a cada linea de esta forma
with open(filename, "r") as file1:
    FileasList = file1.readlines()

print(FileasList[0])