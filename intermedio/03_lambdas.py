## Lambdas ##

#son como funciones pero anónimas, sin nombre -- palabra reservada lambda
sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(1,2))

multiply_values = lambda first_value, second_value: first_value * second_value -3

#utilizar una lambda en una función
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))