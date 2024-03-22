'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

def is_primo(num):
    if num < 2:
        return False
    for index in range(2,num):
        if num % index == 0:
            return False
    return True

for i in range(1, 101):
    if(is_primo(i)):
        print(i)
        
#otra solución
def primo():
    for num in range (1,101):
        if num >= 2:
            is_divisible = False
            for i in range (2, num):
                if num % i == 0:
                    is_divisible = True
                    break
    if not is_divisible:
        print (num)

print(primo())