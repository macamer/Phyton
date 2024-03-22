#Variables -------------->

#se ponen en minuscula y separados con _
my_string_variable = 'My String variable'
print(my_string_variable)
my_int_variable = 5
print(my_int_variable)
my_bool_variable = False
print(my_bool_variable)

#Ver tipo de variable
type(my_string_variable) #str
type(my_int_variable) #int
type(my_bool_variable) #bool

#Concatenación de variable en un print
print( my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de : ", my_bool_variable)

#Algunas funciones del sistema
print(len(my_string_variable)) #indica la longitud de la variable

# Variables en una sola línea
name, surname, alias, age = "Maria" , "Cavaller", "Maca" , 31
print(name, surname, age, "Y mi alias es: ", alias)

'''
#Input en la terminal - No es muy habitual
first_name = input("What's your name? ")
age = input("How old are you? ")
print(first_name)
print(age)
'''

# Forzamos el tipo -- el tipado es dinámico
address: str = "Mi dirección"
address = 32
print(type(address)) #se cambia a int de todas formas