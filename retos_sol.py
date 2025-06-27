# retos

''' EL FAMOSO FIZZ BUZZ
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''
from retos import fizzbuzz
fizzbuzz(3)

from retos import fizzbuzz1
fizzbuzz1(9)

from retos import fizzbuzz2
fizzbuzz2(100)

'''  ES UN ANAGRAMA
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

from retos import es_anagrama
cadena1 = "Nacionalista"
cadena2 = "Altisonancia"
esanagrama = es_anagrama(cadena1, cadena2)
if es_anagrama:
    print(f"{cadena1} es anagrama de {cadena2}")
else:
    print(f"{cadena1} NO es anagrama de {cadena2}")

# Solicitar al usuario las cadenas
#cadena1 = input("Ingresa una cadena: ")
#cadena2 = input("Ingresa otra cadena: ")
esnagrama = es_anagrama(cadena1, cadena2)
if es_anagrama:
    print(f"{cadena1} es anagrama de {cadena2}")
else:
    print(f"{cadena1} NO es anagrama de {cadena2}")

from retos import es_anagrama2
cadena1 = "Amor"
cadena2 = "rOmA"
esanagrama = es_anagrama2(cadena1, cadena2)
if es_anagrama:
    print(f"{cadena1} es anagrama de {cadena2}")
else:
    print(f"{cadena1} NO es anagrama de {cadena2}")    


''' LA SUCESIÓN DE FIBONACCI
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
'''

from retos import fibonacci
fibonacci(0,10)

from retos import fibonacci_dp
fibonacci_dp(10)

from retos import fibonacci_space_optimized
fibonacci_space_optimized(10)

from retos import fibonacci_backtracking
fibonacci_backtracking(10)

from retos import fibonacc_moure
fibonacc_moure(10)

'''¿ES UN NÚMERO PRIMO?
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''
from retos import num_primos
num_primos(102)

'''INVIRTIENDO CADENAS
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''
from retos import invert_cadena
invert_cadena("Hola Mundo")

from retos import reverse
reverse("Hola Mundo")

from retos import reverse2
reverse2("Hola Mundo Dos")

