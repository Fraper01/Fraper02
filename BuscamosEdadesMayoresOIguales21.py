def EdadMayor(vEdad:int, vEdadm=21)->bool:
    return (vEdad >= vEdadm)

def Evaluar():
    print ("Simple Evaluación de Edad")
    print ("-------------------------")
    vEdadm = 21
    vEdad  = int(input("Ingrese la Edad: "))
    #if EdadMayor(vEdad):
    if EdadMayor(vEdad, vEdadm ):
        print (f"\nLa Edad {vEdad} es MayorIgual a 21")
    else:
        print (f"\nLa Edad {vEdad} es Menor a 21")

def Evaluar2():
    print ("Simple Evaluación de Edad2")
    print ("--------------------------")
    vEdades = []
    vCant = int(input("Ingrese la Cantidad de Edades: "))
    for i in range(vCant): # For
        vEdad = int(input(f"Ingrese la Edad Nº {i+1} :"))
        vEdades.append(vEdad)
    
    for e in vEdades: # foreach
        if EdadMayor(e):
            print("\n La {e} es Mayor a 21")
    
def Evaluar3():
    print ("Simple Evaluación de Edad2")
    print ("--------------------------")
    vEdades = []
    vcont = 0
    vCant = int(input("Ingrese la Cantidad de Edades: "))
    for i in range(vCant): # For
        vcont += 1
        vEdad = int(input(f"Ingrese la Edad Nº {vcont} :"))
        vEdades.append(vEdad)
    
    for e in vEdades: # foreach
        if EdadMayor(e):
            print(f"\n La {e} es Mayor a 21")


# Realizamos la Llamada a calcular el main.
if __name__ == "__main__":
    Evaluar2()

