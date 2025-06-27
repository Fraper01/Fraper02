# Classes

'''
Identificar un codigo dentro de un Ambito de Actuacion 
Es como una funcion pero con mas elementos objectos, etc
dentro de la clase
'''

class Person:
    def __init__(self, cnombre, capellido) -> None:
    #    pass # se utiliza solo cuando no tiene codigo
    #pass # es necesario lo ideal es con Mayuscula al inicio y todo lo demas en minuscaula
    #el self de definicion debe estar tabulado despues del def inicio
        self.cnombre = cnombre
        self.capellido = capellido
        self.__capellido = capellido # lo convierte en privado no se puede accesar ni cambiar desde fuera de la clase
    def getname(self):
        return self.__capellido

class Person2:
    def __init__(self, cnombre, capellido) -> None:
    #    pass # se utiliza solo cuando no tiene codigo
    #pass # es necesario lo ideal es con Mayuscula al inicio y todo lo demas en minuscaula
        self.cnombre_completo = f"{my_person.cnombre} {my_person.capellido}"
    def caminado(self):
        print(f"{self.cnombre_completo} esta Caminando")

my_person = Person("Francisco","Perez")
print(f"{my_person.cnombre} {my_person.capellido}")
my_person2 = Person2("francisco","Perez") # inicializa la clase la instancia
print(my_person2.cnombre_completo)
my_person2.caminado()
print(my_person.getname())




