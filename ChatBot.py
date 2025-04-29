import os 
import requests
import json

# Direecion local de la Apiu de Ollama
OLLAMA_URL = "http://localhost:11434/api/chat"

# Ingrese el modelo con el cual vamos a trabajar y el servidor debe estar ejecuntadose
model = input("Ingrese el modelo que desea utilizar: ")

def display_ai_response(text):
    if (text.strip()=="" ):
        print("Ia sin resouesta")
    else:
        recive_response = f"\033[1;96m🤖 IA: {text}\033[0m"
        print(recive_response)

def send_message(historic, user_message=None ): 
    if user_message is not None:
        historic.append({"role":"user","content":user_message})
    #tupla
    payload = {
        "model":model,
        "message":historic,
        "stream":True
    }
    #enviar al modelo la informacion que el usuario define
    response = requests.post(OLLAMA_URL, json=payload, stream=True)
    if response.status_code == 200:
        complete_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    #obtenemos la informacion del json en la linea
                    data = json.load(line.decode("utf-8"))
                    if "message" in data:
                        partial_response = data["message"]["content"]
                        complete_response += partial_response
                except json.JSONDecodeError:
                    continue
        historic.append({"role": "assistant", "content": complete_response})
        return complete_response
    else:
        return f"{response.status_code} : {response.text}"

def chat_consola():
    clean()
    historic = []
    print(f"🧠 Chat con {model} (vía Ollama)\nEscribí 'salir' para finalizar.\n")
    initial_user_messaage = "Eres un asistente empático, hablás en español y saludás de manera breve y amistosa al comenzar una conversación."
    historic.append({"role": "system", "content": initial_user_messaage})
    initial_greeting = send_message(historic,"Hola")
    display_ai_response(initial_greeting)
    while True:
        message = input("😊 Tu ").strip()
        if message.lower() in ["salir","exit","quit"]
            print("Gracias por usar el Chat")
            break
    response = send_message(historic, message)
    display_ai_response(response)

def clean():
    os.system('cls')

if __name__ == "__main__":
    chat_consola()

