## Strings ##

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))


#concatenar strings
print(my_string + " " + my_other_string)

#carácteres especiales
my_new_line_string = "Este es un String \ncon salto de linea"
print(my_new_line_string)

my_tab_string = "Este es un String \tcon tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\nespacado" #ya no hace caso los carácteres especiales
print(my_scape_string)

#formatear valores
name, surname, age = "Maria", "Cavaller", 31

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age)) 
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))#las s son string, d es int
print("Mi nombre es " + name + " "+surname + " y mi edad es " + str(age)) #no es aconsejable
print(f"Mi nombre es {name} {surname} y mi edad es {age}") 

# Desempaquetado de carácteres
print("Desempaquetado -->")
language = "Python"
a, b, c, d, e, f = language #se guardan las letras (parecido al split)

print(a)
print(b)
print(e)

#División
print("Slice -->")
language_slice = language[1:3] #primer carácter posicion donde inicia, y finaliza (length)
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

name = 'Lizz'
print(name[0:2])
var = '01234567'
print(var[::2]) #los pares

# Reverse 
reversed_language = language[::-1]
print(reversed_language)

#funciones del sistema
language = "Python"
print(language.capitalize()) #pone en mayus la primera letra
print(language.casefold()) #?¿
print(language.upper()) #poner en mayusculas
print(language.lower()) #poner en mayusculas
print(language.isupper()) #saber si esta en mayusculas
print(language.count("t")) #contar cuantas letras "t" tiene
