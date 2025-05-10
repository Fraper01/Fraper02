import requests
from bs4 import BeautifulSoup   
import os
import ollama

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
    
    def obtener_Informacion(self, atitulo, aparrafos):
        #Le pedimos a la IA la información de la librería y el tema
        prompt = f"""
                    **Instrucciones:**
                    Actúa como un experto asistente en la elaboracion de Poemas. 
                    Tu objetivo es proporcionar. Un Poema
                    **Parámetros:**
                    * **Titulo:** {atitulo}
                    * **Parrafos:** {aparrafos}
                    **Formato de la respuesta:**
                    Proporciona la información solicitada de la siguiente manera, asegurándote de que esté bien agrupada y sea fácil de entender:
                    El contenido del poema debe ser referente al titulo
                    Fraccionar en la cantidad de Parrafos especificasas
                    Se lo bastante original
                    que no exeda de 100 token
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

def mostrar_definicion(atitulo, aparrafos)-> None:
    iExtraer = ExtraerInformacionWeb()
    iExtraer.obtener_Informacion(atitulo=atitulo, aparrafos=aparrafos)
    iExtraer.mostrar_respuesta_ia(iExtraer.resumen)

if __name__ == "__main__":
    # Bucle principal del programa.
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        # Manejo de excepciones para evitar errores de entrada.
        try:
            titulo = input("Indica el titulo del Poema (o 'salir' para terminar): ")
            if titulo.lower() == "salir":
                break
            if len(titulo) < 4:
                print("El titulo debe tener al menos 4 caracteres.")
                input("\nPresiona Enter para continuar...") 
                continue
            parrafos = input("Indica la cantidad de Parrafos: ")
            iparrafos = int(parrafos)
            if 1 <= iparrafos <= 6 and len(titulo) >= 4:
                mostrar_definicion(titulo, parrafos)
                input("\nPresiona Enter para continuar...") # Pausa para ver el resultado
            else:
                if iparrafos < 1 or iparrafos > 6:
                    print("Indique una cantidad de parrafos entre 1 y 6.")
                    input("\nPresiona Enter para continuar...") 
        except ValueError:
            print("Error: La cantidad de parrafos debe ser un número entero. Intente de Nuevo.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}") # Captura otros posibles errores
