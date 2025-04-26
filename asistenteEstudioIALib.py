# Crear un Sistente de IA para Aprender el manejo de las Lib rerías de Python
import requests
from bs4 import BeautifulSoup   
import pandas as pd
import re   
import os
import ollama
from os import system

class ExtraerInformacionWeb:  
    def __init__(self):
        self.url = None
        self.resumen = ""
        self.modelo = "llama3"
        self.libreria = None
        self.tema = None

    def limpiar_terminal(self):
        # limpiar la terminal
        os.system("cls" if os.name == "nt" else "clear")
    
    def obtener_Informacion(self, alibreria, atema):
        #Le pedimos a la IA la información de la librería y el tema
        prompt = f"""
                    **Instrucciones:**
                    Actúa como un experto asistente en programación de Python. Tu objetivo es proporcionar información detallada y precisa sobre una **librería de Python** específica y un **tema** concreto dentro de esa librería.
                    **Parámetros:**
                    * **Librería:** {alibreria}
                    * **Tema:** {atema}
                    **Formato de la respuesta:**
                    Proporciona la información solicitada de la siguiente manera, asegurándote de que esté bien agrupada y sea fácil de entender:
                    1.  **Definición del Tema:**
                        * Comienza con una definición clara y concisa del **tema** especificado dentro de la **librería**. Explica qué es, cuál es su propósito principal y cuándo se utiliza.
                        * utiliza un nivel de detalle avanzado, pero asegúrate de que sea comprensible para alguien con conocimientos intermedios en programación.
                        * Si es necesario, proporciona un contexto adicional sobre la **librería** en general para ayudar a entender mejor el **tema**.
                    2.  **Conceptos Clave (si aplica):**
                        * Si el tema involucra conceptos clave o relacionados, explícalos brevemente para proporcionar contexto.
                    3.  **Ejemplos de Uso:**
                        * Incluye **ejemplos de código en Python** que ilustren cómo se utiliza el **tema** dentro de la **librería**. Los ejemplos deben ser sencillos, claros y demostrar casos de uso comunes. Si es posible, incluye la salida esperada de los ejemplos.
                        * Asegúrate de que los ejemplos sean funcionales y estén bien comentados para facilitar la comprensión.
                        * Si el tema tiene múltiples formas de uso, proporciona ejemplos variados para mostrar su versatilidad.
                        * Utiliza un estilo de codificación limpio y legible, siguiendo las mejores prácticas de Python.
                    4.  **Consideraciones y Notas Importantes (opcional):**
                        * Si hay consideraciones importantes a tener en cuenta al usar este tema (como mejores prácticas, posibles errores comunes, limitaciones, etc.), inclúyelas en una sección separada.
                    5.  **Recursos Adicionales (opcional):**
                        * Idioma: Responde en español.
                        * Si es relevante, proporciona enlaces a la documentación oficial de la **librería** o recursos adicionales donde los usuarios puedan profundizar más en el tema.
                """
        try:
            self.limpiar_terminal()
            print("🤖 IA: (Buscando Información Solicitada. Por Favor Espere unos minutos...)")
            # Llamar al modelo de lenguaje para obtener la información
            respuesta = ollama.chat(model=self.modelo, messages=
            [
                {
                    'role':'user',
                    'content':prompt
                }
            ])
            self.resumen = respuesta['message']['content'].strip()
            return self.resumen
        except Exception as e:
            print(f"Error al obtener la información: {e}")
            return None 
    def mostrar_respuesta_ia(self, texto):
        self.limpiar_terminal()
        if texto.strip() == "":
            print("🤖 IA: (sin respuesta)")
        else:
            respuesta_estilizada = f"\033[1;96m🤖 IA: {texto}\033[0m"
            print(respuesta_estilizada)
        print("\n--- Fin de la información ---")
        input("Pulse Enter para continuar...")

def mostrar_definicion(alibreria, atema)-> None:
    iExtraer = ExtraerInformacionWeb()
    iExtraer.obtener_Informacion(alibreria=alibreria, atema=atema)
    iExtraer.mostrar_respuesta_ia(iExtraer.resumen)

def mostrar_pandas()-> None:
    #Muestra el menú de Pandas."""
    system('cls')
    titulo = "Librerias de Python Pandas"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))  
    print("1. Definición de Pandas")
    print("2. Que es un DataFrame") 
    print("3. Que es una Series")
    print("4. Crear y visualicar DataFrame")
    print("5. Ejemplos de uso")
    print("9. Regresar al menú principal")
    print("-" * ancho_linea)

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
    print("9. Salir")
    print("-" * ancho_linea)


def menu_pandas()-> None:
    #Muestra el menú de opciones de la librería Pandas
    # Bucle Menu Pandas.
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_pandas()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                mostrar_definicion(alibreria="Pandas", atema="Definición de Pandas")
            elif opcion == '2':
                mostrar_definicion(alibreria="Pandas", atema="DataFrame")
            elif opcion == '3':
                mostrar_definicion(alibreria="Pandas", atema="Series")
            elif opcion == '4':
                mostrar_definicion(alibreria="Pandas", atema="Crear y visualizar DataFrame")
            elif opcion == '5':
                mostrar_definicion(alibreria="Pandas", atema="Ejemplos de uso")
            elif opcion == '9':
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")

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
                menu_pandas()
            elif opcion == '2':
                None
            elif opcion == '3':
                None
            elif opcion == '4':
                None
            elif opcion == '9':
                print("¡Despegando hacia la próxima aventura!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")
