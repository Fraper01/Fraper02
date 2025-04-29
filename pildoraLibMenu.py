from os import system, path 
import pildoraPanda
import pildoraNumpy
import pildoraMatplotlib
import pildoraScikitLearn

def mostrar_menu()-> None:
    #Muestra el menú de General."""
    #Limpia la consola y muestra el menú de opciones. se encuentra en la libreria os
    system('cls')
    titulo = "Librerias de Python"
    titulo2= "para la Ciencia de Datos"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))  
    print(titulo2.center(ancho_linea))  
    print("1. Pandas")
    print("2. NumPy")
    print("3. Matplotlib")
    print("4. Scikit-learn")
    print("0. Salir")
    print("-" * ancho_linea)

if __name__ == "__main__":
    # Bucle principal del programa.
    # Se utiliza para mostrar el menú y ejecutar las opciones seleccionadas por el usuario. 
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_menu()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                pildoraPanda.menu_pandas()
            elif opcion == '2':
                pildoraNumpy.menu_numpy()
            elif opcion == '3':
                pildoraMatplotlib.menu_matplotlib()
            elif opcion == '4':
                pildoraScikitLearn.menu_ScikitLearn()
            elif opcion == '0':
                print("¡Despegando hacia la próxima aventura!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")
       