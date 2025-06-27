# Lambdas

'''
La entendemos como una funcion
van a ser funciones anonimas que no poseen nombre
se llama basicamente almacenando en una variable
No hay diferencia entre funciones y modulos
son funciones bien concretas no de proposito general
'''

sum_valores = lambda ini_valor, fin_valor: ini_valor + fin_valor
print(sum_valores(2,4))

mult_valores = lambda ini_valor, fin_valor: ini_valor * fin_valor -5
print(mult_valores(2,4))

def sum_tres_values(valor3):
    return lambda ini_valor, fin_valor: ini_valor + fin_valor + valor3
print(sum_tres_values(5)(2,4))

'''
Funciones de Orden superior de primera clase
Funciones que ejecutan otras funciones internas 
Exiten ya funciones de orden superior definidas en Python
'''
def suma_uno(value):
    return value + 1

def suma_cinco(value):
    return value + 5

def suma_uno_cinco(value, f_suma_cinco):
    return f_suma_cinco(value) + 1

def suma_valores_uno(ini_valor, fin_valor):
    return suma_uno(ini_valor+fin_valor)

print(suma_valores_uno(5,2))

def suma_valores_uno2(ini_valor, fin_valor, f_suma_uno):
    return f_suma_uno(ini_valor+fin_valor)

print(suma_valores_uno2(5,2,suma_uno))
print(suma_valores_uno2(5,2,suma_cinco))

def suma_valores_uno3(ini_valor, fin_valor, f_):
    return f_(ini_valor+fin_valor,suma_uno)

print(suma_valores_uno3(5,2,suma_uno_cinco))

# closure
'''
hace referencia a las funciones de orden superio con una pecualidad
montar paradigmas asincronos, esta funcion retorna otra funcion y es a esa la que trabajamos
'''
def sum_tem():
    def add(value):
        return value + 10
    return add
    
add_closeru = sum_tem() # add_closeru es ahora una funcnion
print(add_closeru(5))

def sum_tem(valor_org):
    def add(value):
        return value + 10 + valor_org
    return add
    
add_closeru = sum_tem(2) # add_closeru es ahora una funcnion
print(add_closeru(5))

# Funciones de Orden superiro que ya existen en Python
# Map

number = [3,4,10,21,3,30] # se crea una lista
def mult_dos(value):
    return value*2

resilt = list(map(mult_dos, number)) # hay que pasarle una lista y la funcion que va aplicar a cada miembro de la lista devuelve un objecto que hay que identificar
print(resilt)
resilt = list(map(lambda number:number+2, number)) # hay que pasarle una lista o una lambda que va aplicar a cada miembro de la lista devuelve un objecto que hay que identificar
print(resilt)

# filter

def num_mayor_10(number):
    if number > 10:
        return True
    return False

def num_mayor_10(number):
    return number > 10

lo_ret = list((filter(num_mayor_10,number)))
print(lo_ret)

lo_ret = list((filter(lambda number:number>10,number)))
print(lo_ret)

# reduce
from functools import reduce

number = [2,5,10,21,3,30] # se crea una lista

def sum_dos_valores(num1,num2):
    return num1 + num2 

print(reduce(sum_dos_valores,number)) # aplica la funcion en este caso suma todos los valores de la lista

































