# Diccionarios

di_var = dict()
print(type(di_var))
di_var2 = {}
print(type(di_var))
di_var2 ={"Nombre":"Francisco","Apellido":"Perez","Edad":62}
print(di_var2)
di_var2 ={"Nombre":"Francisco","Apellido":"Perez","Edad":62,1:"Python"}
print(di_var2)
'''
Los dicionario tienen la etiqueta y el valor , no utilizan index sino la Etiqueta como busqueda y asignacion
'''
di_var = {
    "Nombre":"Francisco",
    "Apellido":"Perez",
    "Edad":62,
    "Lenguaje": {"Python","Shitf","Coldin"},
    1:1.72
    }
print(di_var)

print(len(di_var))
print(len(di_var2)) # la longitud es por las claves o Etiquetas
print(di_var2["Nombre"])
#print(di_var2["nombre"]) # Error de CLave no Existe debe ser Igual como fue definido
di_var2["Nombre"] = "Francella"
print(di_var2) 
di_var2["Calle"] = "EL Foso"
print(di_var2) 
del di_var2["Calle"]
print(di_var2) 
di_var2[2] = "EL Foso"
print(di_var2) 
print("Francisco" in di_var2)
print("Francella" in di_var2)
print("Nombre" in di_var2)
print("Francella" in di_var2["Nombre"])

print(di_var2.items())
print(di_var2.keys())
print(di_var2.values())
print(di_var2["Nombre"])
#print(di_var2.fromkeys())
di_new = di_var2.fromkeys(di_var2.keys()) # me creo un diccionario igual pero vacio
print(di_new)







