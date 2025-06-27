# variables
svar = "Este es un string"
print(svar)
ivar = 1
print(ivar)
bvar = True
print(bvar)
print(svar, ivar, bvar) # print varias vaviables 
# concadenacion de varialbes
if bvar == True:
    svar2 = "Verdadero"
else:
    svar2 = "Falso"

sMensaje = svar + ";" + str(ivar) + ";" + svar2

print(sMensaje)

# the name 'Jack'
person1 = 'Jack'
# just a name
person2 = 'John'
# name and age in a dict
person3 = {'name': 'Jim', 'age': 42}
# name in a dict, but no age
person4 = {'name': 'Walter', 'email': 'walter.white@example.com'}
# tuple of first and last name
person5 = ('Walther', 'White')

def greet_person(person):
    if isinstance(person, str):
        if person == 'Jack':
            print('Jack himself has arrived')
        else:
            print(f"Hola Amigo, {person}")
    elif isinstance(person, dict) and 'name' in person and 'age' in person:
        print(f"It's, {person['name']}. Born {person['age']} years ago")
    elif isinstance(person, dict) and 'name' in person:
        print(f"It's {person['name']}")
    elif isinstance(person, tuple) and len(person) == 2:
        first, last = person
        print(f"Hello, {first} {last}")
    else:
        print('Not sure what kind of person this is')
        print("FIN")

greet_person(person1)
greet_person(person2)
greet_person(0)
greet_person(person3)
greet_person(person4)
greet_person(person5)

sNombre = input("Indica tu nombre?")
sAnos = input("Indica tu Edad?")
print("Tu Nombre es:" + sNombre, "y tienes " + str(sAnos) + " años")
greet_person(sNombre)

