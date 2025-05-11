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
        self.historic = []
        self.entrevistado = ""
        self.puestosolicita = ""
        self.palabras_clavesP = ["progm", "pytho"]
        self.palabras_clavesA = ["analis", "dato"]

    def detectar_puesto(self)->bool:
        puesto_lower = self.puestosolicita.lower()
        retorna = False
        for palabra in self.palabras_clavesP:
            if palabra in puesto_lower:
                self.puestosolicita = "desarrollador Python"
                retorna = True

        for palabra in self.palabras_clavesA:
            if palabra in puesto_lower:
                self.puestosolicita = "analista de datos"
                retorna = True
        return retorna

    def Inicia_Entrevista(self)->bool:
        while True:
            self.limpiar_terminal()
            self.entrevistado = input("Buenos dias me Indica Por Favor su nombre para dirigirme a Usted (o 'bye' para salir): ? ")
            self.entrevistado = self.entrevistado.strip()  
            if self.entrevistado.lower() == "bye":
                print("Gracias por su tiempo.")
                return False  

            if self.entrevistado:  # Verifica si la cadena no está vacía
                print(f"Buenas tardes Sr(a). {self.entrevistado} Saludos")
                break  
            else:
                print("Por favor, Indiqueme su nombre para poder iniciar la Entrevista.")

        while True:
            #self.limpiar_terminal()
            self.puestosolicita = input(f"Sr(a). {self.entrevistado} Por Favor me indica para cual puesto usted esta aspirando (o 'bye' para salir): ? ")
            self.puestosolicita = self.puestosolicita.strip()
            if self.puestosolicita.lower() == "bye":
                print("Gracias por su tiempo.")
                return False  
            if self.puestosolicita:
                if self.detectar_puesto():
                    print(f"Usted está aspirando al puesto de: {self.puestosolicita}")
                    return True
                else:
                    print("No Identifico bien a que puesto esta Usted Aspirando.")
            else:
                print("Por favor, indique el puesto al que aspira.")

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

    def preguntar_entrevistado(self, texto):
        self.limpiar_terminal()
        

def mostrar_definicion(atitulo, aparrafos)-> None:
    iExtraer = ExtraerInformacionWeb()
    if iExtraer.Inicia_Entrevista():
        iExtraer.obtener_Informacion(atitulo=atitulo, aparrafos=aparrafos)
        iExtraer.mostrar_respuesta_ia(iExtraer.resumen)

if __name__ == "__main__":
    # Bucle principal del programa.
    os.system("cls" if os.name == "nt" else "clear")
    titulo = ""
    parrafos = ""
    mostrar_definicion(titulo,parrafos)
    input("Presione cualquier tecla para continuar.")
