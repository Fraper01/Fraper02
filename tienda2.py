from os import system

def Title(inventario_inicial,inventario) -> None:
    system('cls')
    titulo = "Bienvenido al Sistema de Tienda Zapatos (Sale cuando Inventario = 0)"
    ancho_linea = 69
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))  # Centrar el título
    print(f" Inventario Inicio: {inventario_inicial:>10.2f}" + (" " * 10) + f"Inventario Actual: {inventario:>10.2f}") 
    print("-" * ancho_linea)

def SalidaTrans(vInvArt: list, vCanArt: list, inventario_inicial,inventario) -> None:
    print(f"       {'Nº':<4} {'Inv.Ant':>20} {'Pedido':>15} {'Inv.Fin':>20} ")  # Encabezados
    if len(vInvArt) > 0:
        vcont = 0
        for inv, cant in zip(vInvArt, vCanArt):
            vcont += 1
            print(f"       {vcont:<4} {inv:>20.2f} {cant:>15} {inv - cant:>20.2f} ")
        print("-" * 69)
    else:
        print(f"No Hay Articulos Registrados")

def Verficar(inventario,pedido) -> bool:  
    return pedido <= inventario

def cargar_pedido(vInvArt: list, vCanArt: list, inventario_inicial:int, inventario:int) -> int:
    while inventario > 0:
        Title(inventario_inicial,inventario)
        if len(vCanArt) > 0:
            SalidaTrans(vInvArt,vCanArt,inventario_inicial,inventario)
        try:
            vCant = int(input("Ingrese la Cantidad del Pedido : "))
            if (Verficar(inventario,vCant)):
                vInvArt.append(inventario)
                vCanArt.append(vCant)
                inventario -= vCant
                continue
            else:
                print(f'Lo sentimos no hay tantos zapatos en el inventario, solo hay {inventario}')
                input("Presione enter para Continuar")
                continue
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la cantidad.")
            input("Presione enter para Continuar")
            continue #El programa vuelve al inicio del bucle while
    return inventario

def Evaluar():
    vInvArt = []
    vCanArt = []
    inventario = 100
    inventario_inicial = inventario
    Title(inventario_inicial,inventario)
    inventario = cargar_pedido(vInvArt,vCanArt,inventario_inicial,inventario)
    if len(vCanArt) > 0:
        Title(inventario_inicial,inventario)
        SalidaTrans(vInvArt,vCanArt,inventario_inicial,inventario)
        print(f"  Resumen Total de Articulos en Inventario Inicial: {inventario_inicial:>10.2f}") 
        print(f"          Total de Articulos Pedidos              : {sum(vCanArt):>10.2f}")
        print(f"          Total de Articulos en Inventario Final  : {inventario:>10.2f}") 
        print(f"          Total de Transacciones                  : {len(vInvArt):>10.2f}")
        print("-" * 69)
 
    else:
        print(f"No Hay Articulos Registrados")

# Realizamos la Llamada a calcular el main.
if __name__ == "__main__":
    Evaluar()

