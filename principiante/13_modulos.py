## Modulos##

#es una especie de librería. Se exporta e importa para poder reutilizar código
'''
import module
#from 10_function import Mult --> no permite acceder a este tipo de ficheros, tiene que llevar en su nombre module

from module import sumValues

module.sumValues(1,2,3)
module.imprimir("Hola Python")
'''
#al importar una función en concreto, no es necesario añadir module delante
from module import sumValues, imprimir

sumValues(1,2,3)

#hay modulos del sistema
import math 
print(math.pi)
print(math.pow(4,2))

#crear un alias
from math import pi as pi_value
print(pi_value)