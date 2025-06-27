# sets parecido a las listas veamos


se_var = set() # se utiliza para la creacion ()
se_var2 = {} # inicialmente lo define igual que los Diccionarios
print(type(se_var))
print(type(se_var2))

se_var2 = {"Francisco","Perez",62}
print(type(se_var2))
print(len(se_var2))

se_var2.add("Verga")
print(se_var2)

'''
Un set no es una structura ordenada ya no existen los index
como la lista o tupla, guarda en forma desordenada
y tampoco admite repetidos valores, ella ordena por su algoritmo interno desconocido
'''
se_var2.add("Verga")
print(se_var2)

print("Francisco" in se_var2)
se_var2.remove("Verga")
print(se_var2)

se_var2.clear()
print(se_var2)

se_var2 = {"Francisco","Perez",62}
se_var = {"Kotlin","Swift","Python"}
se_varu = se_var.union(se_var2)
se_varu = se_varu.union({"Javascript","c#"})
print(se_varu)

print(se_varu.difference(se_var))




