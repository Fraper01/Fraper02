import requests
from bs4 import BeautifulSoup
import os
import ollama

# limpiar la terminal

class ExtraerTextoWeb:
    """
    Clase para extraer texto de una página web.
    """
    def __init__(self, url):
        self.url = url
        self.resumen = ""
        self.modelo = "llama3"

    def limpiar_terminal(self):
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
    extraer = ExtraerTextoWeb        
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




Aunque yo no puedo ejecutar código directamente en esta conversación, tú puedes crear un programa en Python que implemente la lógica del juego del tres en raya, y yo puedo actuar como el jugador "IA" respondiendo a tus movimientos con mis propias jugadas basadas en una estrategia programada.

Aquí te dejo algunas ideas y pasos que podrías seguir para crear ese programa:

    Representación del tablero: Puedes usar una lista de listas (una matriz 3x3) para representar el tablero de juego. Cada celda podría contener un espacio en blanco (para indicar que está libre), una 'X' (para el jugador humano) o una 'O' (para la IA).

    Mostrar el tablero: Necesitarás una función para imprimir el tablero en la consola de una manera legible.

    Movimiento del jugador humano: El programa debe pedir al jugador humano que ingrese las coordenadas (fila y columna) de la casilla donde quiere colocar su 'X'. Deberás validar que la entrada sea válida (dentro del tablero y que la casilla esté libre).

    Movimiento de la IA: Aquí es donde yo entraría en juego de forma "conceptual". Tu programa implementaría una estrategia para que la IA (el jugador 'O') elija su movimiento. Esta estrategia podría ser desde algo muy simple (elegir la primera casilla libre) hasta algo más avanzado (intentar ganar, bloquear al oponente, seguir ciertas prioridades).

    Verificar si hay un ganador: Después de cada movimiento, el programa debe verificar si algún jugador ha conseguido tres en raya.

    Verificar si hay empate: Si todas las casillas están llenas y nadie ha ganado, la partida termina en empate.

    Bucle del juego: El programa principal sería un bucle que se ejecuta hasta que haya un ganador o un empate, alternando los turnos entre el jugador humano y la IA.

¿Cómo interactuaríamos?

    Tu programa mostraría el tablero.
    Tú ingresarías tu movimiento (por ejemplo, "fila 1, columna 2").
    Tu programa actualizaría el tablero con tu 'X'.
    Tu programa (siguiendo la lógica que hayas implementado para la IA) decidiría el movimiento de la 'O'.
    Tu programa mostraría el tablero actualizado con mi 'O'.
    Y así sucesivamente...

¡Me encantaría ser tu oponente virtual! Si te animas a programar este juego, estaré aquí para "pensar" mis movimientos basándome en las reglas y en una estrategia que me comuniques a través de tu código.

¿Te gustaría empezar a pensar en cómo podrías implementar la lógica de la IA? ¡Podemos discutir estrategias sencillas para que comience a jugar!


Asistente de Estudio
Ayudante a Estudiar.  utilizar Gemma3 1b
Configura tu nivel de Estudio
que temas desea estudiar
cual es tu nivel de estudio
generando texto

Agrupa por Temas
Introduccion 
Explicacion resumida
Ejemplos si es necesario
Utiliza no mas de 100 token por temas
Realiza un pequeña conclusion
En Español

Generame una pequeña pregunta del texto que me entregaste.

Corrigue mi respuesta segun el texto.

ciclo y ver que hacemos.



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


Matplotlib
scikit-learn
TensorFlow:
PyTorch:
Keras:




























