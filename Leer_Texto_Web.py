#Extraer un texto desde la web
#Importar librerias 
import requests
from bs4 import BeautifulSoup   
import pandas as pd
import re   
import os
import ollama


class ExtraerTextoWeb:
    """
    Clase para extraer texto de una página web.
    """
    def __init__(self):
        self.url = None
        self.resumen = ""
        self.modelo = "llama3"

    def limpiar_terminal(self):
    # limpiar la terminal
        os.system("cls" if os.name == "nt" else "clear")
    
    def extraer_texto_web(self, url):
        """
        Extrae el texto de una página web dada su URL.
        """
        try:
            # Realizar la solicitud HTTP GET a la URL
            response = requests.get(url)
            response.raise_for_status()  # Lanza un error si la solicitud falla si el estado no es 200 (OK) 
            soup = BeautifulSoup(response.text, 'html.parser')
            # Buscamos todos los elementos <script> y <style> y los eliminamos
            # Esto es útil para limpiar el HTML de contenido no deseado
            # que no es texto visible para el usuario.
            for script in soup(["script", "style"]):
                # Eliminar los scripts y estilos
                script.decompose()
        
            # Extraer todo el texto de la página
            texto = soup.get_text(separator='\n', strip=True)
        
            return texto
        except requests.exceptions.RequestException as e:
            print(f"Error al acceder a la URL: {e}")
            return None
    
    def resumir_texto(self, texto):
        """
        Resume el texto extraído utilizando un modelo de lenguaje.
        """
        try:
            prompt = """
            Eres un asistente experto en resumir textos de manera clara y precisa. Cuando recibas un texto a continuación, genera un resumen de hasta 500 tokens. Sigue estas indicaciones:
            1. Mantén la coherencia y la fluidez: el resumen debe leerse de forma natural.  
            2. Conserva la información más relevante: identifica ideas principales, hechos clave y conclusiones.  
            3. Omite ejemplos o detalles secundarios que no sean esenciales para la comprensión global.  
            4. Estructura el resumen en uno o varios párrafos cortos según convenga.  
            5. NO EXCEDAS 500 TOKENS en total.  
            6. Devuélvelo en el mismo idioma del texto original (o en español si el texto está en otro idioma y así se solicita).
            """
            # Llamar al modelo de lenguaje para resumir el texto
            respuesta = ollama.chat(model=self.modelo, messages=[
                {
                    "role": "user", 
                    "content": prompt + '\n' + texto
                }
                ]
                ) 
            self.resumen = respuesta['message']['content'].strip()
            return self.resumen
        
        except Exception as e:
            print(f"Error al resumir el texto: {e}")
            return None 

if __name__ == "__main__":
    # Limpiar la terminal
    extraer = ExtraerTextoWeb()        
    extraer.limpiar_terminal()

    # URL de
    #  ejemplo
    url = "https://www.example.com"
        
    # Extraer texto de la web
    print("Extrayendo texto de la web...")
    url = input("Introduce la URL de la página web: ")

    if not url.startswith("http://") and not url.startswith("https://"):
        print("La URL debe comenzar con 'http://' o 'https://'")
    else:
        # Llamar a la función para extraer el texto
        texto_extraido = extraer.extraer_texto_web(url)
        
    if texto_extraido:
        print("Texto extraído de la web:")
        print(texto_extraido)
    else:
        print("No se pudo extraer el texto de la web.")     

    # Resumir el texto extraído
    resumen = extraer.resumir_texto(texto_extraido)
    if resumen:
        print("Resumen del texto extraído:")
        print(resumen)
    else:
        print("No se pudo resumir el texto extraído.")

    # Guardar el resumen en un archivo de texto
    with open("resumen.txt", "w", encoding="utf-8") as f:
        f.write(resumen)
    print("Resumen guardado en resumen.txt") 




