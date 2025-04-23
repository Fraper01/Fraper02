import datetime
from os import system

def Title() -> None:
    system('cls')
    ancho_linea = 69
    print("-" * ancho_linea)

while True:
    try:
        Title()
        nombre = input("Por favor, introduce tu nombre: ")
        año_nacimiento_str = input("Introduce tu año de nacimiento: ")
        año_nacimiento = int(año_nacimiento_str)
        if año_nacimiento > 0:
            break
        else:
            print("Por favor, introduce un año de nacimiento válido (mayor que 0).")
    except ValueError:
        print("Por favor, introduce un número entero para el año de nacimiento.")

año_actual = datetime.datetime.now().year
edad = año_actual - año_nacimiento

print(f"\nHola, {nombre}.")
print(f"Naciste en el año {año_nacimiento}.")
print(f"Tu edad a la fecha de hoy es de {edad} años.")