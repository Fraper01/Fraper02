# Crear Cuento .py

import os
import ollama


class Crear_Poema:
    def __init__(self):
        self.modelo = 'llama3:8b'


    def limpiar_pantalla(self):
        #Limpiamos la pantalla de la terminal
        os.system("cls")


    def generar_texto_poema(self,titulo,parrafos):
       prompt=f"""
            - Crea el texto de un poema relacionado con el título.
            - El título es: {titulo} 
            - El número de párrafos debe ser: {parrafos}
            - Debe tener máximo 100 palabras (tokens). 
        """
       
       texto = ollama.chat(model=self.modelo, messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ])
       
       self.poema = texto['message']['content'].strip()
       return self.poema


if __name__ == "__main__":
    crear = Crear_Poema()


    crear.limpiar_pantalla()
    
    print("== Crear un poema por IA ==\n")
    titulo = input("Ingresa el título del poema: \n")
    parrafos = input("Ingresa el número de párrafos (1 a 6): \n")
    
    poema = crear.generar_texto_poema(titulo,parrafos)


    print (f"\n== Poema: {titulo} ==\n")
    print(poema)