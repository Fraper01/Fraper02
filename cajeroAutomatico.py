from os import system

class Cajero:
    def __init__(self, saldo_inicial=1000):
        # Constructor de la clase Cajero
        # Inicializa el saldo de la cuenta con un valor predeterminado de 1000 euros
       self.saldo = saldo_inicial

    def mostrar_saldo(self):
        # Mostrar el saldo actual de la cuenta
        return self.saldo

    def ingresar(self, cantidad, ok=False):
        # Método para ingresar dinero en la cuenta  """
        if cantidad > 0:
            self.saldo += cantidad
            ok = True  
        return ok

    def retirar(self, cantidad, ok=False):
        # Método para retirar dinero en la cuenta  """
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                ok = True  
        return ok
    
def ingresaDinero(mi_cajero: Cajero, texto):
    while True:
        system('cls')
        print(texto)
        print("\n--- Cajero Automático ---")
        print(f"Saldo actual: {mi_cajero.mostrar_saldo():.2f} €")
        print("\nIngresar Dinero")
        try:
            cantidad_str = input("\nIntroduce la cantidad a ingresar (o presiona Enter para cancelar): ")
            if cantidad_str == "":
                print("Operación de ingreso cancelada.")
                input("Presione Enter para continuar...")
                break
            cantidad_ingresar = float(cantidad_str)
            ret = mi_cajero.ingresar(cantidad_ingresar)  # Usamos el método del objeto Cajero
            if ret:
                print("\nIngreso realizado con éxito.")
                input("Presione Enter para continuar...")
                break
            else:
                print("\nLa cantidad a ingresar debe ser mayor que 0.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("\nPor favor, introduce una Cantidad valida.")

def retiraDinero(mi_cajero: Cajero, texto):
    while True:
        system('cls')
        print(texto)
        print("\n--- Cajero Automático ---")
        print(f"Saldo actual: {mi_cajero.mostrar_saldo():.2f} €")
        print("\nRetirar Dinero")
        try:
            cantidad_str = input("\nIntroduce la cantidad a retirar (o presiona Enter para cancelar): ")
            if cantidad_str == "":
                print("Operación de retiro cancelada.")
                input("Presione Enter para continuar...")
                break
            cantidad_retirar = float(cantidad_str)
            ret = mi_cajero.retirar(cantidad_retirar)  # Usamos el método del objeto Cajero
            if ret:
                print("\nRetiro realizado con éxito.")
                input("Presione Enter para continuar...")
                break
            else:
                print("\nSaldo insuficiente o cantidad no válida.")
                input("Presione Enter para continuar...")
            break
        except ValueError:
            print("\nPor favor, introduce una Cantidad valida.")

def actividad3():
    texto = """
    Actividad 3 Cajero Automático
    Debe comenzar con un saldo inicial de 1000 €.
    Permitir al usuario elegir una de las siguientes opciones en cada iteración:
    ingresar: el usuario introduce una cantidad para sumar al saldo.
    retirar: el usuario introduce una cantidad para restar del saldo (solo si hay suficiente dinero).
    salir: finaliza el programa.
    """
    mi_cajero = Cajero()  # ¡Aquí instanciamos la clase Cajero!
    opcion = 0
    while opcion != 3:
        system('cls')
        print(texto)
        print("\n--- Cajero Automático ---")
        print(f"Saldo actual: {mi_cajero.mostrar_saldo():.2f} €")
        print("Elige una opción:")
        print("1. Ingresar")
        print("2. Retirar")
        print("3. Salir")
        sopcion = input("Introduce el número de la opción deseada: ")
        try:
            opcion = int(sopcion)
            if opcion == 1:
                ingresaDinero(mi_cajero, texto)  # Pasamos el objeto Cajero a la función
            elif opcion == 2:
                retiraDinero(mi_cajero, texto)  # Pasamos el objeto Cajero a la función
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")
            
    print("\nGracias por utilizar el cajero automático. ¡Hasta luego!")
    input("Presione Enter para continuar...")

if __name__ == "__main__":
    actividad3()
    system('cls')
