## Set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1) #los elementos duplicados se borran

#Convert list to set
album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list) 
print(album_list)

A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

#Add element to set
A.add("NSYNC")
print(A)
A.add("NSYNC")
print(A) #no ha pasado nada porque no se puede repetir

#Eliminar elemento
A.remove("NSYNC")
print(A)

#Verificar si existe un elemento en el set
"AC/DC" in A # devuelte true o false

## Comparación de dos sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])


intersection = album_set1 & album_set2
print(intersection) #los elementos comunes entre los dos sets

different = album_set1.difference(album_set2) #los elementos diferentes
print(different) 

intersection = album_set1.intersection(album_set2) #los elementos comunes
print(intersection)

union = album_set1.union(album_set2) #los comunes junto con los elementos del album_set2
print(album_set2)

#comprobar si es superset o subset
set(album_set1).issuperset(album_set2) #true o false
set(album_set1).issubset(album_set2) #true o false
set({"Back in Black", "AC/DC"}).issubset(album_set1) 
album_set1.issuperset({"Back in Black", "AC/DC"}) 