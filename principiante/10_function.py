## Funciones ##

#declarar
def funcion(x):
    x += 1
    return x

print(funcion(1))

#los prints dentro de la funcion no salen
def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

# se pueden pasar diferentes tipos de datos
Mult(2, 3)
Mult(2.3, 3.34)
Mult(2 , "Michael") 

#funciones vacias
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)
print(MJ1()) #devuelve Michael Jackson none

#funciones predefinidias
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(sum(album_ratings)) # sum suma los int

len(album_ratings) #longitud

#funcion con if
def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

#con un valor por defecto
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

isGoodRating()      #valor 4
isGoodRating(10)    #valor 10