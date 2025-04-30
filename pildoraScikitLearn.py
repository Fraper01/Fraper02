# scikit-learn
from os import system, path
import time
import pandas as pd
import numpy as np  # Importamos la librería NumPy
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris

def presentar_texto(info_scikitlearn, titulo) -> None:
    #"""Imprime un Texto (Formato Diccionario) por consola."""
    system('cls')
    print(f"\n--- {titulo} ---")
    for clave, valor in info_scikitlearn.items():
        print(f"{clave}:")
        if isinstance(valor, list):
            for item in valor:
                print(f"  - {item}")
        else:
            print(f"  {valor}")
    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

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

def mostrar_scikitlearn()-> None:
    #Muestra el menú de ScikitLearn."""
    system('cls')
    titulo = "Librerias de Python ScikitLearn"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))
    print("1. Definición de ScikitLearn")
    print("2. Conceptos Básicos de ScikitLearn")
    print("3. Ejemplos de ScikitLearn")
    print("4. Consideraciones de ScikitLearn")
    print("5. Recursos Adicionales")
    print("0. Regresar al menú principal")
    print("-" * ancho_linea)

def mostrar_scikitlearn_ejemplos()-> None:
    #Muestra el menú de scikitlearn."""
    system('cls')
    titulo = "Ejemplos de Python ScikitLearn"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))
    print("1. Clasificación con Regresión Logística")
    print("0. Regresar al menú principal")
    print("-" * ancho_linea)

def que_es_ScikitLearn()-> None:
    #"""Muestra información general sobre la librería ScikitLearn."""
    info_scikitlearn = {
        "Nombre": "SciKit-Learn",
        "Descripción": "- Scikit-learn (a menudo abreviado como sklearn) es una biblioteca integral y de código abierto de aprendizaje automático (machine learning) para Python. "
        "\n    Está construida sobre NumPy, SciPy y Matplotlib, y proporciona herramientas eficientes para una amplia gama de tareas de aprendizaje supervisado y no supervisado.",
        "Propósito principal": "- El objetivo principal de scikit-learn es ofrecer una interfaz consistente y fácil de usar para implementar algoritmos de aprendizaje automático "
        "\n    para clasificación, regresión, clustering, reducción de dimensionalidad, selección de modelos, preprocesamiento de datos y más. "
        "\n    Se enfoca en la simplicidad, la eficiencia y la accesibilidad para científicos de datos, ingenieros y desarrolladores.",
        "Cuándo se Utiliza": 
            [
            "Problemas de clasificación: Identificar a qué categoría pertenece un nuevo dato (por ejemplo, detección de spam, clasificación de imágenes).",
            "Problemas de regresión: Predecir un valor numérico continuo (por ejemplo, predicción de precios, pronóstico de ventas).",
            "Agrupamiento (Clustering): Descubrir estructuras inherentes en los datos agrupando puntos similares (por ejemplo, segmentación de clientes).",
            "Reducción de dimensionalidad: Reducir el número de variables en un conjunto de datos manteniendo la información importante "
            "\n    (por ejemplo, visualización de datos de alta dimensión).",
            "Selección de modelos: Comparar y seleccionar el mejor modelo para una tarea específica mediante técnicas como la validación cruzada "
            "\n    y la búsqueda de hiperparámetros.",
            "Preprocesamiento de datos: Limpiar, transformar y escalar datos para mejorar el rendimiento de los modelos de aprendizaje automático "
            "\n    (por ejemplo, normalización, estandarización, manejo de valores faltantes).",
            "Ingeniería de características (Feature Engineering): Crear nuevas características a partir de las existentes para mejorar la capacidad "
            "\n    predictiva de los modelos."
            ],
        "Contexto adicional sobre scikit-learn": "Scikit-learn se distingue por su API limpia y coherente. "
        "\n  Los algoritmos se implementan como clases con métodos estándar como fit() (para entrenar el modelo con datos) y "
        "\n  predict() (para hacer predicciones con datos nuevos). "
        "\n  Esto facilita la experimentación con diferentes modelos y la construcción de flujos de trabajo de aprendizaje automático completos."
        "\n  La biblioteca también incluye amplias herramientas para la evaluación de modelos, la selección de hiperparámetros y el preprocesamiento de datos,"
        "\n  lo que la convierte en una solución integral para muchas tareas de aprendizaje automático. "
        "\n  Su fuerte integración con las bibliotecas numéricas de Python (NumPy y SciPy) garantiza la eficiencia en el manejo de grandes conjuntos de datos."
    }
    presentar_texto(info_scikitlearn, "Definición de scikit-learn")

def conceptos_sciketLearn()-> None:
    #"""Muestra información general sobre la librería ScikitLearn."""
    info_sciketlearn = {
        "Nombre": "Scikit-Learn",
        "Conceptos Clave": 
            [
            "Estimadores (Estimators): Son objetos que implementan los algoritmos de aprendizaje automático. "
            "\n    Tienen un método fit(X, y) para aprender de los datos de entrenamiento (X: características, y: variable objetivo) "
            "\n    y un método predict(T) para hacer predicciones sobre nuevos datos (T). "
            "\n    Ejemplos: LinearRegression, LogisticRegression, DecisionTreeClassifier, KMeans.",
            "Transformadores (Transformers): Son objetos utilizados para preprocesar y transformar datos. "
            "\n    Implementan un método fit(X) para aprender los parámetros de la transformación (por ejemplo, la media y la desviación estándar para la estandarización)"
            "\n    y un método transform(X) para aplicar la transformación a los datos. "
            "\n    Algunos transformadores también tienen un método fit_transform(X) que realiza ambas operaciones de manera eficiente. "
            "\n    Ejemplos: StandardScaler, MinMaxScaler, OneHotEncoder, PCA.",
            "Pipelines: Permiten encadenar una secuencia de estimadores y transformadores para automatizar flujos de trabajo de aprendizaje automático comunes "
            "\n    (por ejemplo, preprocesamiento seguido de entrenamiento de un modelo).",
            "Validación Cruzada (Cross-validation): Técnicas para evaluar el rendimiento de un modelo dividiendo los datos en múltiples particiones para "
            "\n    entrenamiento y prueba, proporcionando una estimación más robusta del rendimiento del modelo en datos no vistos",
            "Selección de Hiperparámetros (Hyperparameter Tuning): Métodos para encontrar la mejor combinación de hiperparámetros para un modelo "
            "\n    (parámetros que no se aprenden de los datos sino que se configuran antes del entrenamiento) utilizando técnicas como "
            "\n    la búsqueda en cuadrícula (GridSearchCV) o la búsqueda aleatoria (RandomizedSearchCV).",
            "Métricas de Evaluación (Evaluation Metrics): Funciones para cuantificar el rendimiento de los modelos "
            "\n    (por ejemplo, precisión, recall, F1-score para clasificación; error cuadrático medio, R cuadrado para regresión; coeficiente de silueta para clustering).",
            "Conjuntos de Datos (Datasets): Scikit-learn incluye algunos conjuntos de datos de ejemplo que se pueden utilizar para aprender y experimentar "
            "\n    (por ejemplo, el conjunto de datos Iris para clasificación, el conjunto de datos Boston Housing para regresión)."
            ]
    }
    presentar_texto(info_sciketlearn, "Conceptos de scikit-learn")

def recursos_matplotlib()-> None:
    #"""Muestra información general sobre la librería MatPlotLib."""
    info_matplotlib = {
        "Nombre": "Matplotlib",
        "Recursos Adicionales": 
            [
            "Documentación oficial: https://matplotlib.org/stable/contents.html",
            "Tutoriales y ejemplos: https://matplotlib.org/stable/tutorials/index.html",
            "Ejemplos de gráficos: https://matplotlib.org/stable/gallery/index.html",
            "Galeria de Matplotlib: https://matplotlib.org/stable/gallery/index.html",
            "Comunidad y foros: Stack Overflow, Reddit, etc. para preguntas y respuestas."
            ]
    }
    presentar_texto(info_matplotlib, "Recursos de Matplotlib")  

def consideraciones_matplotlib()-> None:
    #"""Muestra información general sobre la librería MatPlotLib."""
    info_matplotlib = {
        "Nombre": "Matplotlib",
        "Consideraciones y Notas Importantes": 
            [
            "Control granular: Matplotlib ofrece un control muy detallado, lo que puede ser tanto una fortaleza como una debilidad. "
            "\n    Para gráficos simples, la sintaxis puede parecer un poco verbosa en comparación con librerías de nivel superior.",
            "Personalización: La capacidad de personalizar cada aspecto de un gráfico es enorme,"
            "\n    lo que permite crear visualizaciones muy específicas para diferentes necesidades.",
            "Estilos: Matplotlib permite aplicar estilos predefinidos (ej. plt.style.use('seaborn-v0_8-whitegrid')) "
            "\n    o crear estilos personalizados para mantener la consistencia visual.",
            "Backends: La elección del backend puede influir en la interactividad y la forma en que se muestra o guarda el gráfico.",
            "Curva de aprendizaje: Si bien la capa pyplot es relativamente sencilla para gráficos básicos, "
            "\n    dominar la capa Artist para una personalización avanzada requiere una mayor inversión de tiempo."
            ]
    }
    presentar_texto(info_matplotlib, "Consideraciones de Matplotlib")

def ejemplo_clasif_regresion_logistica()-> None:
    system('cls')
    texto = """\n
    # Ejemplo de clasificación con regresión logística utilizando scikit-learn
    Importaciones: Se importan las herramientas necesarias de scikit-learn:

    train_test_split   : Para dividir los datos en conjuntos de entrenamiento y prueba.
    LogisticRegression : El modelo de clasificación que se va a utilizar.
    accuracy_score     : Para evaluar la precisión del modelo.
    StandardScaler     : Para estandarizar las características (escalar los datos para que tengan media 0 y desviación estándar 1). 
                         Esto es importante para muchos modelos lineales como la regresión logística.
    Pipeline           : Para encadenar múltiples pasos de procesamiento de datos (en este caso, escalado y entrenamiento del modelo) 
                         en un flujo de trabajo coherente.
    load_iris          : Para cargar el famoso conjunto de datos Iris, que es un problema de clasificación de flores en tres especies.
    
    1.- Se carga el conjunto de datos Iris:
        donde X contiene las características (medidas de las flores) 
              Y contiene las etiquetas de las clases (las especies de flores).
    
        Syntax:
            iris = load_iris()
            X, y = iris.data, iris.target
    """
    print(texto)

    # Cargar el conjunto de datos Iris
    iris = load_iris()
    X, y = iris.data, iris.target

    input("Pulse Enter para continuar...")

    system('cls')
    texto = """\n
    2.- División de Datos: 
        Los datos se dividen en un conjunto de entrenamiento (X_train, y_train) que se utiliza para entrenar el modelo, 
        y un conjunto de prueba (X_test, y_test) que se utiliza para evaluar su rendimiento en datos no vistos. 
        test_size=0.3 indica que el 30% de los datos se utilizará para la prueba, 
        y random_state=42 asegura que la división sea la misma cada vez que se ejecuta el código (para reproducibilidad).

        Syntax:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    """
    print(texto)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    input("Pulse Enter para continuar...")

    system('cls')
    texto = """\n
    3.- Creación del Pipeline: 
        Se crea un Pipeline que consta de dos pasos:

        ('scaler', StandardScaler()): Primero, se aplica la estandarización a las características.
        ('logreg', LogisticRegression(random_state=42))
         
        Syntax:
            pipeline = Pipeline([
                    ('scaler', StandardScaler()),
                    ('logreg', LogisticRegression(random_state=42))
    ])
    """
    print(texto)
   
    # Crear un pipeline: escalar los datos y luego entrenar un modelo de regresión logística
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('logreg', LogisticRegression(random_state=42))
    ])

    input("Pulse Enter para continuar...")

    system('cls')
    texto = """\n
    4.- Entrenamiento del Modelo: 
        Entrenamos el modelo (la regresión logística) utilizando los datos de entrenamiento escalados. 
        El Pipeline automáticamente aplica el escalado a X_train antes de entrenar el modelo.

        syntax:
            pipeline.fit(X_train, y_train)
    """ 
    print(texto)

    # Entrenar el modelo utilizando el pipeline
    pipeline.fit(X_train, y_train)

    input("Pulse Enter para continuar...")

    system('cls')
    texto = """\n
    5.- Predicciones: 
        Utilizamos el modelo entrenado (dentro del pipeline, lo que significa que los datos de prueba también se escalan automáticamente primero) 
        para hacer predicciones sobre las etiquetas de las flores en el conjunto de prueba.

        syntax:
            y_pred = pipeline.predict(X_test)
    """
    print(texto)

    # Hacer predicciones en el conjunto de prueba
    y_pred = pipeline.predict(X_test)

    input("Pulse Enter para continuar...")

    system('cls')
    texto = """\n
    6.- Evaluación: 
        Comparamos las etiquetas verdaderas del conjunto de prueba (y_test) 
        con las etiquetas predichas por el modelo (y_pred) y calcula la precisión del modelo 
        (la proporción de predicciones correctas). 

        Syntax:
            accuracy = accuracy_score(y_test, y_pred)
    """
    print(texto)

    # Evaluar el rendimiento del modelo
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Precisión del modelo de regresión logística: {accuracy:.2f}\n")
    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")


def menu_ScikitLearn()-> None:
    #Muestra el menú de opciones de la librería ScikitLearn
    # Bucle Menu scikitlearn.
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_scikitlearn()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                que_es_ScikitLearn()
            elif opcion == '2':
                conceptos_sciketLearn()
            elif opcion == '3':
                menu_scikitlearn_ejemplos()
            elif opcion == '4':
                consideraciones_matplotlib()
            elif opcion == '5':
                recursos_matplotlib()
            elif opcion == '0':
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")

def menu_scikitlearn_ejemplos()-> None:
    #Muestra el menú de opciones de la librería Matplotlib
    # Bucle Menu Matplotlib.
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_scikitlearn_ejemplos()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                ejemplo_clasif_regresion_logistica()
            elif opcion == '2':
                None
            elif opcion == '3':
                None
            elif opcion == '4':
                None
            elif opcion == '0':
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")

#"""
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
                None
            elif opcion == '2':
                None
            elif opcion == '3':
                None
            elif opcion == '4':
                menu_ScikitLearn()
            elif opcion == '0':
                print("¡Despegando hacia la próxima aventura!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")
#"""