from os import system

def Title() -> None:
    system('cls')
    titulo = "Bienvenido al Sistema de Compras"
    ancho_linea = 64
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))  # Centrar el título
    print("-" * ancho_linea)

def cargar_productos():
    vNomArt = []
    vCanArt = []
    vPreArt = []
    while True:
        Title()
        vNombre = input("Ingrese el Nombre del Producto: ")
        if vNombre.lower() == 'fin':
            break
        else:
            try:
                vCant = int(input("Ingrese la Cantidad del Producto : "))
                vPrecio = float(input("Ingrese el Precio del Producto: "))
                if vCant < 0 or vPrecio < 0:
                    print("Error: La cantidad y/o el precio deben ser valores positivos.")
                    input("Presione Enter para continuar...")
                else:
                    AddList(vNomArt,vNombre)
                    AddList(vCanArt,vCant)
                    AddList(vPreArt,vPrecio)
            except ValueError:
                print("Error: Por favor, ingrese valores numéricos válidos para cantidad y precio.")
                input("Presione Enter para continuar...") 
    return vNomArt, vCanArt, vPreArt

def Salida(vNomArt: list, vCanArt: list, vPreArt: list) -> None:
    Title()
    print(f"{'Nº':<4} {'Artículo':<20} {'Cantidad':>10} {'Precio Unit.':>10} {'Total':>10}")  
    print("-" * 64) 
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
    print("\n")

def AddList(vLista: list, vValor) ->None:
    vLista.append(vValor)

def calcular_totales(vAcum):
    total = vAcum
    iva = total * 0.21
    totaliva = total + iva
    return total, iva, totaliva

def Evaluar():
    Title()
    vNomArt, vCanArt, vPreArt = cargar_productos()
    Salida(vNomArt,vCanArt,vPreArt)    

# Realizamos la Llamada a calcular el main.
if __name__ == "__main__":
    Evaluar()
