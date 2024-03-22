### Classes ##

#las clases van en la primera letra mayusculas
class Person:
    #constructor de clase --> asi ya se puede instanciar
    #alias -- ejemplo de valor por defecto
    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name #definido como privado... con __
        self.__surname = surname
        self.full_name = f"{name} {surname} {alias}"
    def get_name (self):
        return self.__name
    #se puede llamar al propio objeto para acceder a sus datos
    def walk(self):
        print(f"{self.full_name} está caminando")
        #pass # constructor que no hace nada, por eso pass

my_person = Person("Maria","Cavaller")
#print(f"{my_person.name} {my_person.surname}")
#print(my_person.__name) # error, no puedes acceder porque es privado
print(my_person.get_name()) # para acceder a los datos privados se accede al metodo get
my_person.walk()

my_other_person = Person("Maria","Cavaller", "maca")
print(f"{my_other_person.full_name}")
my_other_person.walk()
#se puede cambiar el atributo de esta forma
my_other_person.full_name = "Marina Castell marca"
print(my_other_person.full_name)