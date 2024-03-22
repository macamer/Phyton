##Dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

print(Dict["key1"])

print(Dict[(0,1)]) #hay un key (0,1) --> no es necesario que todos los keys sean iguales

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict

#ver todas las keys
print(release_year_dict.keys())
#ver todos los values
print(release_year_dict.values())

#añadir datos al diccionario
release_year_dict['Graduation'] = '2007'

#eliminar datos
del(release_year_dict['Graduation'])

#comprobar si existe
'The Bodyguard' in release_year_dict #true o false