from os import system

def cifrado_cesar(frase, desplazamiento=2):
    resultado = ''
    for caracter in frase:
        if caracter.isalpha():
            #la función ord() obtiene el valor ASCII de la letra a o A.
            #Este será el punto de inicio para el cálculo del desplazamiento.
            inicio = ord('a') if caracter.islower() else ord('A')
            # ord(caracter) obtiene el valor ASCII de la letra
            # % 26: Aplica la operación módulo 26 (el número de letras en el alfabeto inglés) para asegurar que si el desplazamiento "se pasa" de la 
            # 'z' o 'Z', vuelva al principio del alfabeto (ejemplo: 'y' con desplazamiento 2 se convierte en 'a').
            desplazamiento_caracter = (ord(caracter) - inicio + desplazamiento) % 26
            resultado += chr(inicio + desplazamiento_caracter)
        else:
            resultado += caracter
    return resultado

def actividad6():
    texto = """
    Actividad 6 Bucle For
    Cifra una frase utilizando el Cifrado César con un desplazamiento dado.
    Solo cifra letras, manteniendo los espacios.
    """
    system('cls')
    print(texto)
    frase_original = input("Introduce una frase a cifrar: ")
    frase_cifrada = cifrado_cesar(frase_original)
    print(f"Frase original: {frase_original}")
    print(f"Frase cifrada: {frase_cifrada}")

def actividad5():
    texto = """
    Actividad 5 Bucle For
    Cuenta la cantidad de vocales en cada palabra de una lista
    y muestra el resultado, incluyendo el total de vocales.
    """
    system('cls')
    print(texto)
    texto_usuario = input("Introduce un texto: ")
    lista_de_palabras = texto_usuario.split()  # Divide el texto en una lista de palabras

    if not lista_de_palabras:
        print("No se introdujeron palabras o esta vacio el texto.")
        return
    # Python es un Lenguaje de Programación que utiliza Bucles For."
    #lista_de_palabras = ["Ordenador", "Python", "Bucle", "Programacion", "Lentejas"]
    vocales = "aeiouAEIOUáéíóú"
    total_vocales = 0

    for palabra in lista_de_palabras:
        contador_vocales = 0
        for letra in palabra:
            if letra in vocales:
                contador_vocales += 1
        print(f"{palabra:<15} → {contador_vocales:>2} vocales")
        total_vocales += contador_vocales

    print(f"Total de vocales: {total_vocales}")

def actividad4():
    texto = """
    Actividad 3 Bucle For
    Cuenta la cantidad de letras en cada palabra de una lista
    y muestra el resultado.
    """
    system('cls')
    print(texto)
    texto_usuario = input("Introduce un texto: ")
    lista_de_palabras = texto_usuario.split()  # Divide el texto en una lista de palabras

    if not lista_de_palabras:
        print("No se introdujeron palabras o esta vacio el texto.")
        return

    #lista_de_palabras = ["Estoy", "aprendiendo", "a", "usar", "el", "bucle", "for"]
    #Estoy aprendiendo a usar el bucle for"
    print(f"\nEl texto introducido contiene un total de {len(lista_de_palabras)} palabras.")
    for palabra in lista_de_palabras:
        cantidad_letras = len(palabra)
        print(f"<{palabra:<15}> tiene {cantidad_letras} letras")

def actividad3(num_filas=5):
    texto = """
    Actividad 3 Bucle For
    Imprimir un triángulo de asteriscos (min 5 filas)
    """
    system('cls')
    print(texto)
    if num_filas < 5:
        num_filas = 5  # Aseguramos un mínimo de 5 filas

    for i in range(1, num_filas + 1):
        print("*" * i)

    print("\n")
    input("Presione Enter para continuar...")
    system('cls')

def actividad2():
    texto = """
    Actividad 2 Bucle For
    Muestra la tabla de multiplicar del número 5 desde el 1 hasta el 10.
    """
    system('cls')
    print(texto)
    numero = 5
    # El bucle for itera sobre un rango de números del 1 al 10 (incluido) con un paso de 1.
    # El primer argumento (1) indica el valor inicial del rango 
    # El segundo argumento (11) indica el valor final del rango (el bucle se detendrá antes de alcanzar este valor, asegurando que el 10 esté incluido).
    # El tercer argumento no esta definido por defecto es 1, lo que significa que avanzamos de 1 en 1.
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def actividad2_1(elementos_por_fila=5):
    texto = """
    Actividad 2 Bucle For
    Muestra la tabla de multiplicar del número 5 desde el 1 hasta el 10.
    """
    system('cls')
    print(texto)
    numero = 5
    # El primer argumento (1) indica el valor inicial del rango 
    # El segundo argumento (11) indica el valor final del rango (el bucle se detendrá antes de alcanzar este valor, asegurando que el 10 esté incluido).
    # El tercer argumento no esta definido por defecto es 1, lo que significa que avanzamos de 1 en 1.
    numero = list(range(1, 11))
    # enumerate() para obtener tanto el índice (i) como el valor (numero) de cada elemento.
    for i, numero in enumerate(numero):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}", end="\t")  # Imprime el número seguido de una tabulación
        if (i + 1) % elementos_por_fila == 0:
            print()  # Imprime una nueva línea al final de cada fila

def actividad1():
    texto = """
    Actividad 1 Bucle For
    Muestra los números pares del 1 al 20 (incluido).
    """
    # El bucle for itera sobre un rango de números del 2 al 20 (incluido) con un paso de 2.
    # El primer argumento (2) indica el valor inicial del rango (el primer número par dentro del intervalo).
    # El segundo argumento (21) indica el valor final del rango (el bucle se detendrá antes de alcanzar este valor, asegurando que el 20 esté incluido).
    # El tercer argumento (2) indica el "paso" o incremento entre cada número generado en el rango. En este caso, avanzamos de 2 en 2, lo que nos da solo los números pares.
    system('cls')
    print(texto)
    for numero in range(2, 21, 2):
        print(numero)

def actividad1_1(elementos_por_fila=5):
    texto = """
    Actividad 1 Bucle For
    Muestra los números pares del 1 al 20 (incluido).
    """
    system('cls')
    print(texto)
    # El primer argumento (2) indica el valor inicial del rango (el primer número par dentro del intervalo).
    # El segundo argumento (21) indica el valor final del rango (el bucle se detendrá antes de alcanzar este valor, asegurando que el 20 esté incluido).
    # El tercer argumento (2) indica el "paso" o incremento entre cada número generado en el rango. En este caso, avanzamos de 2 en 2, lo que nos da solo los números pares.
    pares = list(range(2, 21, 2))
    # enumerate() para obtener tanto el índice (i) como el valor (numero) de cada elemento.
    for i, numero in enumerate(pares):
        print(numero, end="\t")  # Imprime el número seguido de una tabulación
        if (i + 1) % elementos_por_fila == 0:
            print()  # Imprime una nueva línea al final de cada fila

if __name__ == "__main__":
    #actividad1()
    #actividad1_1()
    #actividad2()
    #actividad2_1()
    #actividad3()
    #actividad4()
    #actividad5()
    actividad6()
