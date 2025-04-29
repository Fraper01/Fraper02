from os import system

def Title() -> None:
    system('cls')
    titulo = "Bienvenido al Sistema de Compras (fin)"
    ancho_linea = 64
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))  # Centrar el título
    print("-" * ancho_linea)

def Entrada(vCompras: list) -> None:
    vCant = int(input("Ingrese la Cantidad de Articulos: "))
    Title()
    for i in range(vCant): # For
        vMonto = float(input(f"Ingrese el Monto del Articulo Nº {i+1} :"))
        AddMonto(vCompras, vMonto)

def Salida(vNomArt: list, vCanArt: list, vPreArt: list) -> None:
    Title()
    print(f"{'Nº':<4} {'Artículo':<20} {'Cantidad':>10} {'Precio Unit.':>10} {'Total':>10}")  # Encabezados
    print("-" * 64) #separador
    vAcumCompra = 0
    vcont = 0
    if len(vNomArt) > 0:
        for prod, cant, prec in zip(vNomArt, vCanArt, vPreArt):
            vAcumCompra += prec * cant
            vcont += 1
            print(f"{vcont:<4} {prod:<20} {cant:>10} {prec:>10.2f} {prec * cant:>10.2f} €")
        print("-" * 64)
        vtotal, viva, vtotalIva = calcular_totales(vAcumCompra)
        print(" " *37 + f"Sub Total: {vtotal:>10.2f} €")
        print(" " *37 + f"      Iva: {viva:>10.2f} €")
        print(" " *37 + f"    Total: {vtotalIva:>10.2f} €")
    else:
        print(f"No Hay Articulos Registrados")
def AddMonto(vPreArt: list, vMonto:float) -> None:
    vPreArt.append(vMonto)
def Addtitle(vNomArt: list, vTitle:str) -> None:
    vNomArt.append(vTitle)
def AddCant(vPreArt: list, vCantidad:int) -> None:
    vPreArt.append(vCantidad)

def cargar_productos(vNomArt: list, vCanArt: list, vPreArt: list):
    while True:
        Title()
        vNombre = input("Ingrese el Nombre del Producto: ")
        if vNombre.lower() == 'fin':
            break
        else:
            try:
                vCant = int(input("Ingrese la Cantidad del Producto : "))
                vPrecio = float(input("Ingrese el Precio del Producto: "))
                Addtitle(vNomArt,vNombre)
                AddCant(vCanArt,vCant)
                AddMonto(vPreArt,vPrecio)
            except ValueError:
                print("Error: Por favor, ingrese un número válido para la cantidad y el precio.")
                input("Presione enter para Continuar")
                continue #El programa vuelve al inicio del bucle while

def GuardarDatos(vNomArt: list, vNombre, vCanArt: list, vCantidad, vPreArt: list, vMonto) -> None:
    vNomArt.append(vNombre)
    vCanArt.append(vCantidad)
    vPreArt.append(vMonto)

def calcular_totales(vAcum):
    total = vAcum
    iva = total * 0.21
    totaliva = total + iva
    return total, iva, totaliva

def Evaluar():
    Title()
    vNomArt = []
    vCanArt = []
    vPreArt = []
    cargar_productos(vNomArt,vCanArt,vPreArt)
    #Entrada(vCompras)
    Salida(vNomArt,vCanArt,vPreArt)    

# Realizamos la Llamada a calcular el main.
if __name__ == "__main__":
    Evaluar()
