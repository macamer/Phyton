## Escribir Ficheros ##

#escribir una linea
exmp2 = "intermedio/fichero2.txt"
with open(exmp2, 'w') as writefile:
    writefile.write('This is line A')

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

#escribir lineas (se sobreescribe)
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n") #write() es similar a .readline()
    writefile.write("This is line B\n")

#escribir a partir de una lista
lines = ["This is line A\n", "This is line B\n","This is line C\n"]
with open(exmp2,'w') as writefile:
    for line in lines:
        print(line)
        writefile.write(line)

'''
r+ : Reading and writing. Cannot truncate the file.
w+ : Writing and reading. Truncates the file.
a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.
'''
#añadir lineas
with open(exmp2,'a+') as testwritefile:
    testwritefile.write('This is line D\n')
    print(testwritefile.read()) #no muestra nada porque lo hemos utilizado con el write, y el cursor no se encuentra al inicio del fichero

'''
.tell() - returns the current position in bytes
.seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. 
From can take the value of 0,1,2 corresponding to the beginning, relative to current position and end
'''
#se puede ver como el cursor se mueve según escribe
with open(exmp2,'a+') as testwritefile:
    print('Initial Location: {}'.format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data): #empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())
    
    testwritefile.seek(0,0) #move 0 bytes from beginning
    print('\nNew Location : {}'.format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)
    
    print('Location after read: {}'.format(testwritefile.tell()))

    #w sobreescribe, pero para eliminar todo el texto nos podemos ayudar del truncate()
    with open(exmp2, 'r+') as testwritefile:
        data = testwritefile.readlines()
        testwritefile.seek(0,0) #write at beginning of file
    
        testwritefile.write("Line 1" + "\n")
        testwritefile.write("Line 2" + "\n")
        testwritefile.write("Line 3" + "\n")
        testwritefile.write("finished\n")
        #Uncomment the line below
        testwritefile.truncate() #para eliminar lo que ha quedado sin sobreescribir
        testwritefile.seek(0,0)
        print(testwritefile.read())

#copiar archivo en otro
with open("intermedio/fichero.txt",'r') as readfile:
    with open("intermedio/fichero3.txt", 'w') as writefile:
        for line in readfile:
            writefile.write(line)

with open("intermedio/fichero3.txt",'r') as testwritefile:
    print(testwritefile.read())