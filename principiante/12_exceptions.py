## Exceptions ##
numUno = 5
numDos = 1
numDos = '1'

#try - except
try:
    print(numUno + numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

#try - except -else
try:
    print(numUno + numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #se ejecuta si no hay excepción
    print("La ejecución continúa correctamente") 

#try - except -else - finally
try:
    print(numUno + numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #se ejecuta si no hay excepción
    print("La ejecución continúa correctamente") 
finally:
    #se ejecuta de todas formas
    print("La ejecución continúa")

#Excepciones por tipo
try:
    print(numUno + numDos)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un error de tipo")

#Captura de la información de la excepción
try:
    print(numUno + numDos)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as ex:
    print(ex)

