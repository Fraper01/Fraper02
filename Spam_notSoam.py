import requests
# Procesamiendo de datos y entrenamiento de un modelo de clasificación de spam
import pandas as pd
# Para el procesamiento de texto
from sklearn.model_selection import train_test_split
# Para la division de los datos
from sklearn.feature_extraction.text import CountVectorizer
# Algoritmo de clasificación
from sklearn.naive_bayes import MultinomialNB
# Para la evaluacion del Modelo
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Descargar el dataset
import os
# Verificar si el archivo ya existe
if os.path.exists('sms.tsv'):
    print("El archivo sms.tsv ya existe. No es necesario descargarlo nuevamente.")
else:
    print("Descargando el dataset...")
    # URL del dataset
    url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la descarga falla (código de error 4xx o 5xx)
        with open('sms.tsv', 'wb') as f:
            f.write(response.content)
        print("Dataset descargado correctamente como sms.tsv")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el dataset: {e}")
        # Aquí podrías añadir código para manejar el error, como salir del script
        exit()

# Cargar el dataset
df = pd.read_csv('sms.tsv', sep='\t', names=['label', 'message'])   
# Mostrar las primeras filas del dataset
print(df.head())

# convertir las etiquetas a valores numericos
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
# Vectorizar el texto
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message']).toarray()
y = df['label_num'].values

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
print("Precisión del Modelo Accuracy:", accuracy_score(y_test, y_pred))
print("\nReporte de Clasificacón:\n", classification_report(y_test, y_pred))    
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

input("Presiona Enter para continuar...")
# Guardar el modelo entrenado y el vectorizador
import joblib
joblib.dump(model, 'spam_classifier_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

input("Presiona Enter para continuar...")
# Ejemplo de prueba
example = ["Congratulations!","You've won a $1,000 Walmart gift card. Click here to claim your prize."]
example_vectorized = vectorizer.transform(example).toarray()
example_pred = model.predict(example_vectorized)
print("\nEjemplo de prueba:\n", example)

for mensaje, pred in zip(example, example_pred):
    if pred == 1:
        print(f"Mensaje: {mensaje} - Predicción: Spam")
    else:
        print(f"Mensaje: {mensaje} - Predicción: Ham")
    print(f"Mensaje: {mensaje} - Predicción: {'Spam' if pred == 1 else 'Ham'}")

input("Presiona Enter para continuar...")
# Ejemplo de prueba2
mensajes = ["Free money!!!", "Hola, ¿quieres almorzar hoy?", "Win a new iPhone now! Click here"]
mensajes_transformados = vectorizer.transform(mensajes)
predicciones = model.predict(mensajes_transformados)

for mensaje, pred in zip(mensajes, predicciones):
    print(f"'{mensaje}' --> {'Spam' if pred == 1 else 'No Spam'}")

input("Presiona Enter para continuar...")
# Ejemplo de prueba3
mensajes = ["¡Felicidades! Has ganado un viaje a Cancún.", "¿Te gustaría salir a cenar esta noche?", "Gana dinero desde casa. ¡Es fácil!"]  
mensajes_transformados = vectorizer.transform(mensajes)
predicciones = model.predict(mensajes_transformados)

for mensaje, pred in zip(mensajes, predicciones):
    print(f"'{mensaje}' --> {'Spam' if pred == 1 else 'No Spam'}")

