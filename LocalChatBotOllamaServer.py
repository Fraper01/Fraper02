import os
import requests
import json

# 🌐 Dirección local de la API de Ollama
OLLAMA_URL = "http://localhost:11434/api/chat"

# ✅ Modelo a utilizar

MODEL = input(f"Que modelo deceas utilizar: ")

def limpiar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def enviar_mensaje(historial, mensaje_usuario=None):
    if mensaje_usuario is not None:
        historial.append({"role": "user", "content": mensaje_usuario})

    payload = {
        "model": MODEL,
        "messages": historial,
        "stream": True
    }

    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    if response.status_code == 200:
        respuesta_completa = ""
        for linea in response.iter_lines():
            if linea:
                try:
                    data = json.loads(linea.decode("utf-8"))
                    if "message" in data:
                        respuesta_parcial = data["message"]["content"]
                        respuesta_completa += respuesta_parcial
                except json.JSONDecodeError:
                    continue

        historial.append({"role": "assistant", "content": respuesta_completa})
        return respuesta_completa
    else:
        return f"❌ Error {response.status_code}: {response.text}"

def mostrar_respuesta_ia(texto):
    """
    Muestra la respuesta de la IA con estilo ANSI: negrita + color cian brillante.
    """
    if texto.strip() == "":
        print("🤖 IA: (sin respuesta)")
    else:
        respuesta_estilizada = f"\033[1;96m🤖 IA: {texto}\033[0m"
        print(respuesta_estilizada)
    print()

def chat_consola():
    limpiar_terminal()

    print(f"🧠 Chat con {MODEL} (vía Ollama)\nEscribí 'salir' para finalizar.\n")

    historial = []

    mensaje_usuario_inicial = (
        "Sos un asistente empático, hablás en español y saludás de manera breve y amistosa "
        "al comenzar una conversación."
    )

    historial.append({"role": "system", "content": mensaje_usuario_inicial})

    saludo_inicial = enviar_mensaje(historial, "Hola")
    mostrar_respuesta_ia(saludo_inicial)

    while True:
        mensaje = input("😊 Tú: ").strip()

        if mensaje.lower() in ["salir", "exit", "quit"]:
            print("\n👋 ¡Gracias por usar el chat! Hasta luego.")
            break

        respuesta = enviar_mensaje(historial, mensaje)
        mostrar_respuesta_ia(respuesta)

if __name__ == "__main__":
    chat_consola()
