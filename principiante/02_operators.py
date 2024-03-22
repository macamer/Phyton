## Operadores ##

print(3 + 4)
print(3 - 4)
print(3 + 4)
print(3 / 4)
print(10 % 2)
print(10 // 3) # siempre va a sacar un entero.. es una flor division
print(2 ** 3) # exponiente

print("Hola"+"Python")
print("Hola" + str(5)) #para operar deben ser del mismo tipo 
print("Hola " *5) #se multiplica el string

"""
my_int = 2.5 * 2
print("Hola " * my_int)#no funciona porque lo reconoce como float
"""

my_float = 2.5 * 2
print("Hola "* int(my_float))

## Operadores comparativos ##

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print("Hola" > "Python")
print("Hola" < "Python") # ordenación alfabética por ASCII


## Operadores Lógicos ##
print("\nOperadores lógicos -->")
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(not(3 > 4))
#print(3 > 4 "Hola" > "Python")