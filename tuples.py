# tuples

tu_var = tuple
tu_var2 = ()
tu_var = (62,1.70,"Francisco", "Perez",62)
print(tu_var)
print(tu_var[0])
li_i = tu_var[0]
print(type(li_i))
print(tu_var[-1])
print(tu_var.count(62))
print(tu_var.index(1.70)) # que indice ocupa el valor pero vio solo el primero conseguido y da error si no esta en la lista

#tu_var[1] = 1.80
print(tu_var)
'''
Las tuplas no permite modificar los valores ni insertar valores
ya los valore colocados no se pueden alterar ni cambiar
son una mierda para que sirven entonces
'''
tu_var2 = (60,30,35)
print(tu_var+tu_var2)

li_var = list(tu_var)
print(li_var)
li_var[4] = "verga"
li_var.insert(1,"azul")
print(li_var)
tu_var = tuple(li_var)
print(tu_var)
print(type(tu_var))

del tu_var  # Elimina de todo la variable que sea no esta definida el clear en lista vacia 
#print(tu_var)





