from os import system, path
import time
import pandas as pd
import numpy as np  # Importamos la librería NumPy
import matplotlib.pyplot as plt

def presentar_texto(info_matplotlib, titulo) -> None:
    #"""Imprime un Texto (Formato Diccionario) por consola."""
    system('cls')
    print(f"\n--- {titulo} ---")
    for clave, valor in info_matplotlib.items():
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

def mostrar_matplotlib()-> None:
    #Muestra el menú de NumPy."""
    system('cls')
    titulo = "Librerias de Python Matplotlib"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))
    print("1. Definición de Matplotlib")
    print("2. Conceptos Básicos de Matplotlib")
    print("3. Ejemplos de Gráficas")
    print("4. Consideraciones de Matplotlib")
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
    print("4. Consideraciones de Matplotlib")
    print("5. Recursos Adicionales")
    print("0. Regresar al menú principal")
    print("-" * ancho_linea)

def que_es_matplotlib()-> None:
    #"""Muestra información general sobre la librería MatPlotLib."""
    info_matplotlib = {
        "Nombre": "Matplotlib",
        "Descripción": "- Matplotlib es la biblioteca fundamental para la visualización de datos en 2D (y algunas capacidades en 3D) en Python."
            "\n  - Proporciona una forma flexible y poderosa de crear gráficos estáticos, interactivos y animados de calidad de publicación."
            "\n  - Es la base sobre la que se construyen muchas otras bibliotecas de visualización de datos de nivel superior en Python, como Seaborn.",
        "Propósito principal": "- El objetivo principal de Matplotlib es permitir a los científicos de datos, ingenieros, investigadores y programadores "
            "generar visualizaciones significativas \n    y personalizables de sus datos. "
            "\n  - Ofrece un control granular sobre cada aspecto de un gráfico, desde los marcadores y las líneas hasta las etiquetas, los títulos, las leyendas y los ejes.",
        "Cuándo se Utiliza": 
            [
            "Exploración de datos (EDA): Crear histogramas, diagramas de dispersión, gráficos de líneas, gráficos de barras y otros tipos de visualizaciones "
            "\n    para comprender las características y las relaciones dentro de los conjuntos de datos.",
            "Presentación de resultados: Generar figuras de alta calidad para informes, publicaciones científicas, presentaciones y dashboards.",
            "Comunicación: Visualizar tendencias, patrones y comparaciones de manera clara y efectiva para audiencias diversas.",
            "Desarrollo de interfaces gráficas (GUI): Integrar gráficos dentro de aplicaciones de escritorio utilizando sus backends.",
            "Creación de animaciones: Visualizar datos que cambian con el tiempo o iteraciones."
            ],
        "Contexto adicional sobre Matplotlib: \n    El diseño de Matplotlib se inspiró en MATLAB, un popular entorno de programación numérica."
            "\n    Esto hace que la transición para los usuarios familiarizados con MATLAB sea más sencilla. "
            "\n    Matplotlib ofrece una arquitectura modular con varias capas:": 
        [
            "Backend: La capa backend se encarga de renderizar el gráfico en un dispositivo de salida específico "
            "\n    (por ejemplo, una ventana en pantalla, un archivo PNG, un documento PDF). "
            "\n    Matplotlib soporta múltiples backends.",
            "Artist Layer: Esta es la capa de programación orientada a objetos que proporciona un control completo sobre los elementos"
            "\n    del gráfico (los 'artistas' como líneas, rectángulos, texto, ejes, etc.).",
            "Scripting Layer (pyplot): Esta es una interfaz de conveniencia basada en el estado que proporciona una forma más rápida y similar a MATLAB"
            "\n    de crear gráficos para tareas comunes. "
            "\n    La mayoría de los usuarios principiantes e intermedios interactúan principalmente con esta capa."
        ]
    }
    presentar_texto(info_matplotlib, "Definición de Matplotlib")

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

def menu_matplotlib()-> None:
    #Muestra el menú de opciones de la librería NumPy
    # Bucle Menu NumPy.
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_matplotlib()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                que_es_matplotlib()
            elif opcion == '2':
                conceptos_matplotlib()
            elif opcion == '3':
                menu_matplotlib_ejemplos()
            elif opcion == '4':
                None
            elif opcion == '5':
                None
            elif opcion == '6':
                None
            elif opcion == '7':
                None
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
                None
            elif opcion == '5':
                None
            elif opcion == '6':
                None
            elif opcion == '7':
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
                menu_matplotlib()
            elif opcion == '4':
                None
            elif opcion == '0':
                print("¡Despegando hacia la próxima aventura!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")
#"""