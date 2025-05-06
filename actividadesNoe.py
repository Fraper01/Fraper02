from os import system

def encontrar_mayor(lnumeros)-> int:
    return max(lnumeros)

def encontrar_menor(lnumeros)-> int:
    return min(lnumeros)

def encontrar_medio(lnumeros)-> float:
    return sum(lnumeros) / len(lnumeros)

def encontrar_mediana(lnumeros)-> float:
    numeros_ordenados = sorted(lnumeros)
    n = len(numeros_ordenados)
    #  Se verifica si la longitud de la lista es par (el resto de la división por 2 es 0). 
    if n % 2 == 0:  
        medio1 = numeros_ordenados[n // 2 - 1]
        medio2 = numeros_ordenados[n // 2]
        mediana = (medio1 + medio2) / 2
    else:  # Si la lista tiene un número impar de elementos
        mediana = numeros_ordenados[n // 2]    
    return mediana

def ingresaDinero(saldo: float, texto) -> float:
    while True:
        system('cls')
        print(texto)
        print("\n--- Cajero Automático ---")
        print(f"Saldo actual: {saldo:.2f} €")
        print("\nIngresar Dinero")
        try:
            cantidad_str = input("\nIntroduce la cantidad a ingresar (o presiona Enter para cancelar): ")
            if cantidad_str == "":  
                print("Operación de ingreso cancelada.")
                input("Presione Enter para continuar...")
                break  
            cantidad_ingresar = float(cantidad_str)
            if cantidad_ingresar > 0:
                saldo += cantidad_ingresar
                print("\nIngreso realizado con éxito.")
                break
            else:
                print("\nLa cantidad a ingresar debe ser mayor que 0.")
        except ValueError:
            print("\Por favor, introduce una Cantidad valida.")
    return saldo

def retiraDinero(saldo: float, texto) -> float:
    while True:
        system('cls')
        print(texto)
        print("\n--- Cajero Automático ---")
        print(f"Saldo actual: {saldo:.2f} €")
        print("\nIngresar Dinero")
        try:
            cantidad_str = input("\nIntroduce la cantidad a retirar (o presiona Enter para cancelar): ")
            if cantidad_str == "":  
                print("Operación de retiro cancelada.")
                input("Presione Enter para continuar...")
                break  
            cantidad_retirar = float(cantidad_str)
            if cantidad_retirar > 0:
                if saldo >= cantidad_retirar:
                    saldo -= cantidad_retirar
                    print("\nRetiro realizado con éxito.")
                    break
                else:
                    print("\nSaldo insuficiente.")
                    input("Presione Enter para continuar...")
            else:
                print("\nLa cantidad a retirar debe ser mayor que 0.")
        except ValueError:
            print("\nPor favor, introduce una Cantidad valida.")
    return saldo

def actividad3():
    texto = """
    Actividad 3 Cajero Automático
    Debe comenzar con un saldo inicial de 1000 €. 
    Permitir al usuario elegir una de las siguientes opciones en cada iteración:
    ingresar: el usuario introduce una cantidad para sumar al saldo.
    retirar: el usuario introduce una cantidad para restar del saldo (solo si hay suficiente dinero).
    salir: finaliza el programa.
    """
    saldo = 1000.0  # Saldo inicial
    opcion = 0
    while opcion != 3:
        system('cls')
        print(texto)
        print("\n--- Cajero Automático ---")
        print(f"Saldo actual: {saldo:.2f} €")
        print("Elige una opción:")
        print("1. Ingresar")
        print("2. Retirar")
        print("3. Salir")
        sopcion = input("Introduce el número de la opción deseada: ")
        try:
            opcion = int(sopcion)
            if opcion == 1:
                saldo = ingresaDinero(saldo,texto)
            elif opcion == 2:
                saldo = retiraDinero(saldo,texto)
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")
    print("\nGracias por utilizar el cajero automático. ¡Hasta luego!")

def actividad2():
    texto = """
    Actividad 2 Bucle While
    Pide al usuario introducir números enteros hasta que escribe 0.
    Al finalizar, muestra el número mayor introducido (excluyendo el 0).
    """
    # Inicializa la lista para almacenar los números
    numeros = []
    numero = None
    while numero != 0:
        system('cls')
        print(texto)
        #try...except ValueError: Maneja los posibles errores si se introduce algo que no se puede convertir a un entero. 
        try:
            numero = int(input("\nIntroduce un número entero (escribe 0 para finalizar): "))
            if numero != 0:
                numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

    # Comprueba si la lista numeros contiene al menos un número. 
    if numeros:
        print(f"\n")
        print(f"La Lista de números introducidos: {numeros}")
        print(f"La Lista de números ordenada    : {sorted(numeros)}")
        print(f"La cantidad de números : {len(numeros):>4.0f}")
        print(f"La sumatoria de números: {sum(numeros):>4.0f}")
        print(f"\n")
        print(f"El número mayor    es: {encontrar_mayor(numeros):>4.0f}")
        print(f"El número menor    es: {encontrar_menor(numeros):>4.0f}")    
        print(f"El número promedio es: {encontrar_medio(numeros):>3.2f}")
        print(f"El número medio    es: {encontrar_mediana(numeros):>3.2f}")
        print(f"\n")
    else:
        print("\nNo se introdujeron números antes del 0.")

def actividad1():
    texto = """
    Actividad 1 Bucle While
    Escribir una contraseña inventada sin cifrar y pedir al usuario que intente acceder 
    al sistema si la contraseña es válida.
    """
    password = None
    password_correcta = "python"
    while password != password_correcta:
        system('cls')
        print(texto)
        password = input("\nIntroduce tu contraseña: ")
        if password != password_correcta:
            print("Contraseña incorrecta. Inténtalo de nuevo.")
    print("Acceso concedido.")

if __name__ == "__main__":
    #actividad1()
    #actividad2()
    actividad3()
