# retos

'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''
def es_multiplo(numero, multiplo):
    # Si el residuo es 0, es múltiplo
    if numero % multiplo == 0:
        return True
    else:
        return False
    
def es_multiplo2(numero, multiplo):
    return numero % multiplo == 0     # Simplifica la funcion retorna solo true

def ret_palabra(num):
    es_tres = es_multiplo2(num,3) 
    es_cinc = es_multiplo2(num,5) 
    if es_tres and not es_cinc :
        ls_var = "fizz"
    elif not es_tres and es_cinc:
        ls_var = "buzz"
    elif es_tres and es_cinc:
        ls_var = "fizzbuzz"
    else:
        ls_var = num
    return ls_var

def fizzbuzz(ahasta):
    ivar = 1
    ivar2 = ahasta
    print("Primera solicion")
    while ivar <= ivar2:
        print(ret_palabra(ivar))
        ivar +=1

def fizzbuzz1(ahasta):
    print("Segunda solicion")
    ivar = 1
    ivar2 = ahasta
    my_list = [ret_palabra(i) for i in range(ivar,ivar2+1)]
    for element in my_list:
        print(element)

def fizzbuzz2(ahasta):
    print("MoreDev solicion")
    ivar = 1
    ivar2 = ahasta
    for index in range(ivar,ivar2+1):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


'''  ES UN ANAGRAMA
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

def es_anagrama(palabra1 , palabra2):
    if isinstance(palabra1, str) and isinstance(palabra2, str):
        palabra1 = palabra1.lower()
        palabra2 = palabra2.lower()
        if palabra1 == palabra2:
            return False
        else:
            palabra1_lista = list(palabra1)
            palabra2_lista = list(palabra2)
            palabra1_lista.sort()
            palabra2_lista.sort()
            palabra1 = "".join(palabra1_lista)
            palabra2 = "".join(palabra2_lista)
            return palabra1 == palabra2
    else:
        return False
    
def es_anagrama2(palabra1, palabra2):
    if isinstance(palabra1, str) and isinstance(palabra2, str):
        if palabra1.lower() == palabra2.lower():
            return False
        else:
            return sorted(palabra1.lower()) == sorted(palabra2.lower()) # el sorted convierte en lista es ma rapida la que la otra solucion va al grano
    else:
        return False

''' LA SUCESIÓN DE FIBONACCI
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
'''
def fibonacci(inic,cant):  
    for i in range(inic,cant+1):
        print(fibonacci_recursive(i), end=" ")

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dp(n):
    fib_array = [0, 1]
    for i in range(2, n):
        fib_array.append(fib_array[-1] + fib_array[-2])
    return fib_array

def fibonacci_space_optimized(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_memoization(n):
    if n <= 1:
        return n
    return fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)

def fibonacci_backtracking(n, memo={}):
    if n <= 1:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_backtracking(n - 1) + fibonacci_backtracking(n - 2)
        return memo[n]


def fibonacc_moure(n):
    print("incio maure")
    prev = 0
    next = 1
    for _ in range(0,n):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
    
'''¿ES UN NÚMERO PRIMO?
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''
def es_primo(numero):
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, numero//2, 2):
        if numero % i == 0:
            return False
    return True 

def num_primos(n):
    print("Inicia primos")
    for index in range(1,n):
        if es_primo(index):
            print(index)

'''INVIRTIENDO CADENAS
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''
def invert_cadena(cadena):
    cadena_lista = list(cadena)
    cadena_resul = list()
    for i in reversed(cadena_lista):
        cadena_resul.append(i)
    #print(cadena_resul)
    print("".join(cadena_resul))

def reverse(cadena):
    text_len = len(cadena)
    reverse_text = ""
    for index in range(0,len(cadena)):
        reverse_text += cadena[text_len - index -1]
    print(reverse_text)

def reverse2(cadena):
    reverse_text = ""
    for index in reversed(cadena):
        reverse_text += index
    print(reverse_text)

