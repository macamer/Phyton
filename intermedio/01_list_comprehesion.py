## List Comprehension ##

my_original_list=[0, 1, 2, 3, 4, 5, 6, 7]

#crear lista rango del 0 al 6
my_list = [i for i in range(7)]
print(my_list)

#se puede operar mientras se crea la lista
my_list = [i * 2 for i in my_original_list]
print(my_list)

#a partir de una funcion
def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in my_original_list]
print(my_list)

