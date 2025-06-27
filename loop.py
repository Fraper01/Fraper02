# Loops

# while

ivar = 0

while ivar < 10:
    print(ivar)
    ivar += 2
else:
    print("mi condicion no ya no cumple")

print("la ejecucion continua")

while ivar < 20:
    ivar +=1
    if ivar == 15:
        print("se detine en 15")
        break
    print(ivar)
    
# For

llis_var = [35,24,62,52,30,30,17]

for element in llis_var:
    print(element)

ldu_var = (62,1.70,"Francisco","Perez","Axul")
for element in ldu_var: # Imprime los Elementos
    print(element)

lse_var = {"Francisco","Perez",62}
for element in lse_var: # Imprime los Elementos
    print(element)

ldi_var = {"Nombre":"Francisco","Apellido":"Perez","Edad":62,1:("Python","c++")}
for element in ldi_var: # Imprime las Etiquetas
    print(element)

for element in ldi_var.values(): # Imprime los valores
    print(element)
    if element == 62:
        print("ojo todo es en minuscula")
        break # rompe el ciclo
else:
    print("finalizo el bucle")

for element in ldi_var.values(): # Imprime los valores
    print(element)
    if element == 62:
        print("ojo todo es en minuscula")
        continue # Manda a Evaluar de nuevo el For no ejecuta mas nada a bajo del continue un concepto Desacualizado igual al Goto NO UTILIZAR
else:
    print("finalizo el bucle")





