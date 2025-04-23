from os import system
import random
import datetime

def Title(max_intentos,intentos,num_minutos) -> None:
    system('cls')
    titulo = "¡Bienvenido al juego de adivinanza!"
    titulo2= "Estoy pensando en un número entre 1 y 100."
    titulo3= (f"Tienes {max_intentos} intentos ó {num_minutos} seg. ¡Buena suerte!")
    ancho_linea = 69
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))  
    print(titulo3.center(ancho_linea))
    print(titulo2.center(ancho_linea))
    print(f" Maximo Intentos: {max_intentos:>10.2f}" + (" " * 10) + f"Intentos Realizados: {intentos:>10.2f}") 
    print("-" * ancho_linea)

def SalidaIntentos(vMensaje: list, vNumero: list, rangi: int, rangf: int, numero_secreto: int ) -> None:
    print(f"    {'Intento':<4} {'Tu Número':>20}    {'Mensaje':<20} {'Sugerencia':<20}")  # Encabezados
    if len(vNumero) > 0:
        vcont = 0
        for num, mens in zip(vNumero, vMensaje):
            vcont += 1
            if (vcont == len(vNumero)) and (num != numero_secreto): 
                print(f"    {vcont:<4}{num:>20}        {mens:<20}  [{rangi}-{rangf}]")
            else:
                print(f"    {vcont:<4}{num:>20}        {mens:<20}  ")
        print("-" * 69)
    else:
        print(f"No Hay Números Registrados")

def juego_adivinanza(vMensaje: list, vNumero: list) -> None:
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 7
    num_minutos = 30
    rangi = 1
    rangf = 100
    hora_inicio = datetime.datetime.now()
    hora_final = hora_inicio + datetime.timedelta(seconds=num_minutos)  

    while intentos < max_intentos and datetime.datetime.now() < hora_final:
        Title(max_intentos,intentos,num_minutos)
        if len(vNumero) > 0:
            SalidaIntentos(vMensaje,vNumero,rangi,rangf,numero_secreto)
        try:
            adivinanza = int(input(f" ¿Cuál es tu adivinanza? "))

            if datetime.datetime.now() >= hora_final:
                print(f"Lo siento, has agotado tu tiempo. El número era {numero_secreto}.")  
                break
            
            vNumero.append(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                rangi = adivinanza + 1
                vMensaje.append("Demasiado bajo.")
            elif adivinanza > numero_secreto:
                vMensaje.append("Demasiado alto.")
                rangf = adivinanza - 1
            else:
                vMensaje.append(f"¡Felicidades! Adivinaste el número en {(datetime.datetime.now() - hora_inicio).seconds} segundos.")
                Title(max_intentos,intentos,num_minutos)
                SalidaIntentos(vMensaje,vNumero,rangi,rangf,numero_secreto)
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    if intentos == max_intentos and adivinanza != numero_secreto:
        Title(max_intentos,intentos,num_minutos)
        SalidaIntentos(vMensaje,vNumero,rangi,rangf,numero_secreto)
        print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.")  

def inicioJuego():
    while True:
        try:
            vMensaje = []
            vNumero = []
            juego_adivinanza(vMensaje,vNumero)
            jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
            if jugar_de_nuevo != 's':
                print("Gracias por jugar. ¡Hasta luego!")
                break
        except ValueError:
            print("Por favor, ingresa una opción válida.")  

# Realizamos la Llamada a main.
if __name__ == "__main__":
    inicioJuego()

# Fin del juego de adivinanza
# Este código es un juego de adivinanza donde el usuario tiene que adivinar un número entre 1 y 100.
