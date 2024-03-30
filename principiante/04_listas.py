### Listas ###

my_list = list()
my_other_list = [] #esto también es una lista

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

#ahora se actualiza -- len = 7
print(my_list)
print(len(my_list))

#mezclar diferentes tipos de datos
my_other_list = [35, 1.77, "Maria", "Cavaller"]
print(type(my_other_list)) #resultado -- list

print(type(my_list))
print(type(my_other_list))

#para acceder a un dato de la lista (0 es el primero)
print(my_other_list[1])
print(my_other_list[3])
print(my_other_list[-1]) #accede al último
print(my_other_list[-3])
#print(my_other_list[4]) -- IndexError
#print(my_other_list[-5]) -- IndexError

#retorna el número de ocurrencias de un valor
print(my_list.count(30))
print(my_other_list.count("Maria"))

#concatenar listas
print(my_list + my_other_list)

#maneras de definir datos (no la más correcta)
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[-1]
print(age)