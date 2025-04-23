from os import system

system('cls')
number1 = int(input("Digite el primer número: "))
number2 = int(input("Digite el segundo número: ")) 

def suma(a, b)-> int | float:
    return a + b

def resta(a, b)-> int | float:
    return a - b

def multiplicacion(a, b)-> int | float:
    return a * b    

def division(a, b)-> int | float | str:
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b


print (f"\nResultado de {number1} + {number2} es  {suma(number1,number2):>5.2f}")
print (f"\nResultado de {number1} - {number2} es  {resta(number1,number2):>5.2f}")
print (f"\nResultado de {number1} * {number2} es  {multiplicacion(number1,number2):>5.2f}")
print (f"\nResultado de {number1} / {number2} es  {division(number1,number2):>5.2f}")


