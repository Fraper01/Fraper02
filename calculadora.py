number1 = int(input("Digite o primer número: "))
number2 = int(input("Digite o segundo número: ")) 

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


print (f"\nResultado de Sumar {number1} y {number2}: {suma(number1,number2)}")
print (f"\nResultado de Restar {number1} y {number2}: {resta(number1,number2)}")
print (f"\nResultado de Multiplicar {number1} y {number2}: {multiplicacion(number1,number2)}")
print (f"\nResultado de División {number1} y {number2}: {division(number1,number2)}")


