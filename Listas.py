# Listas

li_lista = list()
li_listao = []
li_listaa = list()
print(len(li_lista))
li_lista = [35,34,62,52,30,30,17]
print(li_lista)
print(len(li_lista))
li_listao = [62,1.70,"Francisco","Perez"]
print(li_listao)
print(len(li_listao))

inum1 = 5
inum2 = 10
inum3 = 15

li_listaa.insert(0,inum1) 
li_listaa.insert(1,inum2)
li_listaa.insert(2,inum3)
print(li_listaa)
print(li_listaa[2]) # las listas comienzan con el indice 0
print(li_listaa.count(10))

print(li_lista)
print(li_lista[2]) # las listas comienzan con el indice 0
print(li_lista.count(30))
print(li_lista[-1]) # las listas comienzan con el indice 0 y no funciona restando (restando inicia en 1)

iedad, daltura, snombre, sapellido = li_listao
print(daltura)
print(type(daltura))
print(li_lista+li_listaa+li_listao) # concadena listas
"""
mensaje varias lineas no sirve para una
"""
print(sum(li_listaa))
print(len(li_listaa))
print(max(li_listaa))
print(min(li_listaa))
print(sum(li_listaa)/len(li_listaa))

li_listaa.append(40)
li_listaa.append(40)
li_listaa.append(8)
print(li_listaa)
print(sum(li_listaa))
print(len(li_listaa))
print(max(li_listaa))
print(min(li_listaa))
print(sum(li_listaa)/len(li_listaa))

li_listaa.remove(40)
li_listaa.remove(40) # solo lo hace una vez el primer valor encontrado
print(li_listaa)
print(sum(li_listaa))
print(len(li_listaa))
print(max(li_listaa))
print(min(li_listaa))
print(sum(li_listaa)/len(li_listaa))

print(li_listaa)
print(li_listaa.pop())
print(li_listaa)

print(li_listaa)
print(li_listaa.pop(1)) # sin argumento elimina el ultimo index con arguemnto el index indicado pop sirve para almacenar el valor eliminado
print(li_listaa)

del li_listaa[0] # elimina un elemento de la lista sin almacenar
print(li_listaa)

li_listaa.clear()
print(li_listaa)

li_listaa.append(inum2)
li_listaa.append(inum1)
li_listaa.append(inum3)
print(li_listaa)
li_listaa.sort()
print(li_listaa)
li_listaa.reverse()
print(li_listaa)

li_listar = list
print(li_listaa[0])
inumr = li_listaa[0]
print(inumr)
#li_listar.append(100)
#li_listar.insert(0,li_listaa[0])
print(li_listar)


