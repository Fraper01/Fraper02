# Execpciones

'''
Siempre que qqueremos manejar un error hay que utilizar la siguiente sintaxis
try:
    Aqui va el codigo basico
except:
    Ejecuta este codigo cuando ocurra el Error, e otros lenguajes es try Cash 
else:
    No hay error ejecuta este codigo
finally:
    Siempre corre este codigo pase lo que pase antes
'''

li_num1, li_num2 = 5, 1

print(li_num1+li_num2)

li_num2 = 1
li_num1 = 5

try:
    if type(li_num2) == str and type(li_num1) == str:
        lsmensaje = "Error los argumentos son Alfanumerico"
        print(lsmensaje)
    else:
        print(li_num1+li_num2)
except:
    if type(li_num1) == str:
        lsmensaje = "Error el primer argumento es Alfanumerico"
    if type(li_num2) == str:
        lsmensaje = "Error el segunto argumento es Alfanumerico"
    if type(li_num2) == str and type(li_num1) == str:
        lsmensaje = "Error los argumentos son Alfanumerico"
    print(lsmensaje)
else:
    print("contuena bien")
finally:
    print("Final para Ambos")








