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
    print("9. Salir")
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
    print("2. Conceptos Básicos de Matplotlib")
    print("3. Ejemplos de Gráficas")
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

def que_es_array_numpy()-> None:
    #"""Explica qué es un array de NumPy."""
    system('cls')
    print("\n--- ¿Qué es un Array de NumPy? ---")
    print("Un array de NumPy (ndarray) es la estructura de datos principal de la librería. Se trata de un array n-dimensional que contiene elementos del mismo tipo.")
    print("\nCaracterísticas clave de los arrays de NumPy:")
    print("- **Homogeneidad:** Todos los elementos del array deben ser del mismo tipo de dato (por ejemplo, todos enteros o todos floats). Esto permite operaciones más eficientes en memoria y velocidad.")
    print("- **Multidimensional:** Pueden ser unidimensionales (vectores), bidimensionales (matrices) o tener más dimensiones (tensores).")
    print("- **Tamaño fijo:** Una vez creado, el tamaño de un array de NumPy no se puede cambiar.")
    print("- **Indexación basada en 0:** Los elementos se acceden mediante índices que comienzan en 0.")
    print("- **Eficiencia:** Las operaciones en arrays de NumPy están optimizadas y son mucho más rápidas que las operaciones equivalentes en listas de Python, especialmente para grandes conjuntos de datos.")
    print("\nEjemplo de un array unidimensional (vector):")
    print("  [1, 2, 3, 4, 5]")
    print("\nEjemplo de un array bidimensional (matriz):")
    print("  [[1, 2, 3],")
    print("   [4, 5, 6]]")
    print("\nTensor de 3 dimensiones (2 'imágenes', 2 filas, 3 columnas")
    print("[# Primera 'imagen' (matriz 2x3)")
    print("  [10, 20, 30]")
    print("  [40, 50, 60]")
    print("]")  
    print("[# Segunda 'imagen' (matriz 2x3)")
    print("  [70, 80, 90]") 
    print("  [100, 110, 120]")
    print("]")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def crear_arrays_numpy()-> None:
    #"""Muestra cómo crear arrays de NumPy."""
    system('cls')
    print("\n--- Crear Arrays de NumPy ---")
    print("NumPy proporciona varias funciones para crear arrays:")
    print("\n1. **np.array():** Crea un array a partir de una lista o tupla de Python.")
    print("   Ejemplo:")
    print("     `mi_array = np.array([1, 2, 3])`")
    print("     `mi_matriz = np.array([[1, 2], [3, 4]])`")
    print("\n2. **np.zeros():** Crea un array lleno de ceros.")
    print("   Ejemplo:")
    print("     `ceros = np.zeros(5)` (array unidimensional de 5 ceros)")
    print("     `matriz_ceros = np.zeros((2, 3))` (matriz de 2x3 llena de ceros)")
    print("\n3. **np.ones():** Crea un array lleno de unos.")
    print("   Ejemplo:")
    print("     `unos = np.ones(3)`")
    print("     `matriz_unos = np.ones((3, 2))`")
    print("\n4. **np.arange():** Crea secuencias numéricas (similar a `range` de Python).")
    print("   Ejemplo:")
    print("     `secuencia = np.arange(10)` (de 0 a 9)")
    print("     `secuencia_paso = np.arange(0, 10, 2)` (de 0 a 9 con paso de 2)")
    print("\n5. **np.linspace():** Crea secuencias numéricas con un número específico de elementos dentro de un rango.")
    print("   Ejemplo:")
    print("     `lineal = np.linspace(0, 1, 5)` (5 números igualmente espaciados entre 0 y 1)")
    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def operaciones_basicas_numpy()-> None:
    #"""Muestra operaciones básicas con arrays de NumPy."""
    system('cls')
    print("\n--- Operaciones Básicas con Arrays de NumPy ---")
    print("NumPy permite realizar operaciones elemento a elemento de forma eficiente:")
    print("\n- **Suma, resta, multiplicación, división:** Se aplican a cada elemento del array (o entre arrays del mismo tamaño).")
    print("  Ejemplo:")
    print("    `a = np.array([1, 2, 3])`")
    print("    `b = np.array([4, 5, 6])`")
    print("    `suma = a + b` (result: [5, 7, 9])")
    print("    `multiplicacion = a * 2` (result: [2, 4, 6])")
    print("\n- **Funciones matemáticas:** NumPy proporciona funciones como `np.sin()`, `np.cos()`, `np.sqrt()`, etc., que se aplican a cada elemento.")
    print("  Ejemplo:")
    print("    `angulos = np.array([0, np.pi/2, np.pi])`")
    print("    `senos = np.sin(angulos)`")
    print("\n- **Operaciones de agregación:** Funciones como `np.sum()`, `np.mean()`, `np.max()`, `np.min()`, etc., para calcular estadísticas sobre los arrays.")
    print("  Ejemplo:")
    print("    `datos = np.array([10, 20, 30, 40])`")
    print("    `promedio = np.mean(datos)`")
    print("    `maximo = np.max(datos)`")
    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def indexacion_slicing_numpy()-> None:
    #"""Muestra cómo indexar y hacer slicing en arrays de NumPy."""
    system('cls')
    print("\n--- Indexación y Slicing de Arrays de NumPy ---")
    print("La indexación y el slicing en arrays de NumPy son similares a las listas de Python, pero con más poder para arrays multidimensionales:")
    print("\n- **Indexación:** Acceder a elementos individuales usando sus índices (comenzando en 0). Para arrays multidimensionales, se usan múltiples índices separados por comas.")
    print("  Ejemplo:")
    print("    `vector = np.array([10, 20, 30, 40])`")
    print("    `primer_elemento = vector[0]` (result: 10)")
    print("    `matriz = np.array([[1, 2, 3], [4, 5, 6]])`")
    print("    `elemento_2_1 = matriz[1, 0]` (fila 1, columna 0, result: 4)")
    print("\n- **Slicing:** Obtener subconjuntos de arrays utilizando la notación `inicio:fin:paso`.")
    print("  Ejemplo:")
    print("    `vector = np.array([10, 20, 30, 40, 50])`")
    print("    `sub_vector = vector[1:4]` (elementos desde el índice 1 hasta el 3, result: [20, 30, 40])")
    print("    `sub_matriz_fila = matriz[0, :]` (primera fila completa, result: [1, 2, 3])")
    print("    `sub_matriz_columna = matriz[:, 1]` (segunda columna completa, result: [2, 5])")
    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def funciones_universales_numpy()-> None:
    #"""Explica las funciones universales (ufuncs) de NumPy."""
    system('cls')
    print("\n--- Funciones Universales (ufuncs) de NumPy ---")
    print("Las funciones universales (ufuncs) son funciones que operan elemento a elemento en los arrays de NumPy. Son muy eficientes y rápidas.")
    print("\nEjemplos de ufuncs comunes:")
    print("- **Funciones matemáticas:** `np.sin()`, `np.cos()`, `np.tan()`, `np.log()`, `np.exp()`, `np.sqrt()`, etc.")
    print("- **Funciones de comparación:** `np.equal()`, `np.not_equal()`, `np.greater()`, `np.less()`, etc.")
    print("- **Funciones lógicas:** `np.logical_and()`, `np.logical_or()`, `np.logical_not()`.")
    print("\nLas ufuncs pueden operar entre un escalar y un array, o entre dos arrays del mismo tamaño.")
    print("\nEjemplo:")
    print("  `array = np.array([1, 2, 3])`")
    print("  `raiz_cuadrada = np.sqrt(array)` (result: [1.        , 1.41421356, 1.73205081])")
    print("  `array_bool = array > 1` (result: [False,  True,  True])")
    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def algebra_lineal_numpy()-> None:
    #"""Muestra ejemplos de álgebra lineal con NumPy."""
    system('cls')
    print("\n--- Álgebra Lineal con NumPy ---")
    print("NumPy proporciona un submódulo `linalg` para realizar operaciones de álgebra lineal:")
    print("\n- **Multiplicación de matrices:** `np.dot(a, b)`")
    print("- **Cálculo de la matriz transpuesta:** `a.T`")
    print("- **Cálculo del determinante de una matriz:** `np.linalg.det(a)`")
    print("- **Cálculo de la inversa de una matriz:** `np.linalg.inv(a)`")
    print("- **Cálculo de autovalores y autovectores:** `np.linalg.eig(a)`")
    print("\nEjemplo:")
    print("  `matriz_a = np.array([[1, 2], [3, 4]])`")
    print("  `matriz_b = np.array([[5, 6], [7, 8]])`")
    print("  `producto = np.dot(matriz_a, matriz_b)`")
    print("  `determinante = np.linalg.det(matriz_a)`")
    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def ejemplo_graf_linea()-> None:
    #"""Muestra ejemplo de graficación de línea."""
    system('cls')
    print("\n--- Grafico de línea Matplotlib ---")
import matplotlib.pyplot as plt
import numpy as np

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
    input("Pulse Enter para continuar...")

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
                crear_arrays_numpy()
            elif opcion == '4':
                operaciones_basicas_numpy()
            elif opcion == '5':
                indexacion_slicing_numpy()
            elif opcion == '6':
                funciones_universales_numpy()
            elif opcion == '7':
                algebra_lineal_numpy()
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
                conceptos_matplotlib()
            elif opcion == '3':
                crear_arrays_numpy()
            elif opcion == '4':
                operaciones_basicas_numpy()
            elif opcion == '5':
                indexacion_slicing_numpy()
            elif opcion == '6':
                funciones_universales_numpy()
            elif opcion == '7':
                algebra_lineal_numpy()
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