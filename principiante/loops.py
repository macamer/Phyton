## Bucles

### Ifs ###
age = 18
if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")


# Operadores Lógicos
album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

#if not
album_year = 1983
if not (album_year == 1984):
    print ("Album year is not 1984")


## For ##

dates = [1982,1980,1973]
N = len(dates)

for i in range(N): #en el rango N
    print(dates[i])   

for i in range(0, 8):
    print(i)

#ejemplo de tabla de multiplicar
for i in range (10):
    print("6 x", i, "=", 6*i)

for year in dates:  
    print(year)   

#a partir de una lista
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

for i, square in enumerate(squares):
    print(i, square)


## While ##

count = 1
while count <= 5:
    print(count)
    count += 1

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

#crear nueva lista
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)


Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new_animals = []
i = 0
while i < len(Animals):
    if len(Animals[i]) == 7:
        new_animals.append(Animals[i])
    i += 1
print(new_animals)