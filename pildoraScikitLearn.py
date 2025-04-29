# scikit-learn
from os import system, path
import time
import pandas as pd
import numpy as np  # Importamos la librería NumPy
import matplotlib.pyplot as plt

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
    titulo = "Librerias de Python SciketLearn"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))
    print("1. Definición de SciketLearn")
    print("2. Conceptos Básicos de SciketLearn")
    print("3. Ejemplos de Gráficas")
    print("4. Consideraciones de SciketLearn")
    print("5. Recursos Adicionales")
    print("0. Regresar al menú principal")
    print("-" * ancho_linea)

def mostrar_matplotlib_ejemplos()-> None:
    #Muestra el menú de Matplotlib."""
    system('cls')
    titulo = "Ejemplos de Python Matplotlib"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))
    print("1. Gráfico de Líneas")
    print("2. Gráfico de Dispersión")
    print("3. Gráfico de Barras")
    print("4. Multiples Subgráficos")
    print("0. Regresar al menú principal")
    print("-" * ancho_linea)

def que_es_SciketLearn()-> None:
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

def conceptos_matplotlib()-> None:
    #"""Muestra información general sobre la librería MatPlotLib."""
    info_matplotlib = {
        "Nombre": "Matplotlib",
        "Conceptos Clave": 
            [
            "Figure: Es la ventana o la página completa donde se dibuja el gráfico. Puede contener uno o varios subgráficos (axes).",
            "Axes (Subplot): Es un área de trazado individual dentro de una figura. Cada Axes tiene sus propios objetos de coordenadas (x-axis, y-axis), "
            "\n    un título, etiquetas, etc. "
            "\n    La mayoría de los comandos de trazado se dirigen a un objeto Axes.",
            "Artist: Todo lo que se dibuja en una figura es un Artist. Esto incluye objetos Text, Line2D, Rectangle, Axes, Figure, etc. "
            "\n    Los Artist tienen propiedades que controlan su apariencia (por ejemplo, color, estilo de línea, grosor).",
            "Plotting Functions (en pyplot): Funciones como plot(), scatter(), bar(), hist(), imshow() proporcionan una forma sencilla de crear diferentes tipos de gráficos.",
            "Properties: Casi todos los elementos de un gráfico tienen propiedades que se pueden personalizar utilizando argumentos en las funciones de trazado o "
            "\n    mediante métodos de los objetos Artist.",
            "Backend: El motor que renderiza el gráfico. Diferentes backends son adecuados para diferentes entornos y propósitos "
            "\n    (por ejemplo, agg para archivos estáticos, TkAgg para ventanas interactivas con Tkinter, WebAgg para visualizaciones en navegadores web)."
            ]
    }
    presentar_texto(info_matplotlib, "Conceptos de Matplotlib")

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

def ejemplo_multi_grafico()-> None:
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Crear una figura con 2x2 subgráficos

    x = np.linspace(0, 10, 100)  # Definimos x aquí si no está definido globalmente
    axs[0, 0].plot(x, np.cos(x))
    axs[0, 0].set_title('Coseno(x)')

    x_scatter = np.random.rand(50)
    y_scatter = np.random.rand(50)
    axs[0, 1].scatter(x_scatter, y_scatter, color='orange')
    axs[0, 1].set_title('Dispersión 2')

    # Definimos las variables 'categorias' y 'valores' aquí
    categorias = ['A', 'B', 'C', 'D']
    valores = [25, 40, 30, 55]
    axs[1, 0].bar(categorias, valores, color='cyan')
    axs[1, 0].set_title('Barras 2')

    axs[1, 1].hist(np.random.randn(100), bins=20, color='magenta', alpha=0.7)
    axs[1, 1].set_title('Histograma')

    fig.suptitle('Múltiples Subgráficos', fontsize=16)
    plt.tight_layout()  # Ajusta el espaciado entre subgráficos
    plt.show()

def ejemplo_graf_barra()-> None:
    categorias = ['A', 'B', 'C', 'D']
    valores = [25, 40, 30, 55]

    plt.figure(figsize=(8, 6))
    plt.bar(categorias, valores, color=['red', 'green', 'blue', 'purple'])
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.title('Gráfico de Barras')
    plt.show()
    print("\n--- Fin de la información ---")

def ejemplo_graf_diagrama_dispersión()-> None:
    np.random.seed(0)
    x_scatter = np.random.rand(50)
    y_scatter = np.random.rand(50)
    colores = np.random.rand(50)
    tamanios = 100 * np.random.rand(50)

    plt.figure(figsize=(8, 6))
    plt.scatter(x_scatter, y_scatter, c=colores, s=tamanios, alpha=0.7, cmap='viridis')
    plt.colorbar(label='Intensidad del color')
    plt.xlabel('Variable A')
    plt.ylabel('Variable B')
    plt.title('Diagrama de Dispersión')
    plt.show()
    print("\n--- Fin de la información ---")

def ejemplo_graf_linea()-> None:
    #"""Muestra ejemplo de graficación de línea."""
    system('cls')
    print("\n--- Grafico de línea Matplotlib ---")
    # Ejemplo básico de un gráfico de líneas
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure(figsize=(8, 6))  # Crear una nueva figura con un tamaño específico
    plt.plot(x, y, label='Seno(x)', color='blue', linestyle='-', linewidth=2)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfico de la función Seno')
    plt.legend()
    plt.grid(True)
    plt.show()
    print("\n--- Fin de la información ---")

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
                que_es_SciketLearn()
            elif opcion == '2':
                conceptos_matplotlib()
            elif opcion == '3':
                menu_matplotlib_ejemplos()
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

def menu_matplotlib_ejemplos()-> None:
    #Muestra el menú de opciones de la librería Matplotlib
    # Bucle Menu Matplotlib.
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_matplotlib_ejemplos()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                ejemplo_graf_linea()
            elif opcion == '2':
                ejemplo_graf_diagrama_dispersión()
            elif opcion == '3':
                ejemplo_graf_barra()
            elif opcion == '4':
                ejemplo_multi_grafico()
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