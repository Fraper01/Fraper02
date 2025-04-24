from os import system, path
import time
import pandas as pd
import numpy as np  # Importamos la librería NumPy

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

def mostrar_numpy()-> None:
    #Muestra el menú de NumPy."""
    system('cls')
    titulo = "Librerias de Python NumPy"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))
    print("1. Definición de NumPy")
    print("2. ¿Qué es un Array de NumPy?")
    print("3. Crear Arrays de NumPy")
    print("4. Operaciones Básicas con Arrays")
    print("5. Indexación y Slicing de Arrays")
    print("6. Funciones Universales (ufuncs)")
    print("7. Álgebra Lineal con NumPy")
    print("9. Regresar al menú principal")
    print("-" * ancho_linea)

def que_es_numpy()-> None:
    #"""Muestra información general sobre la librería NumPy."""
    info_numpy = {
        "Nombre": "NumPy",
        "Descripción": "Es una librería fundamental para la computación numérica en Python. Proporciona soporte para arrays multidimensionales y una gran colección de funciones matemáticas de alto nivel para operar con estos arrays.",
        "Estructura de Datos Clave": [
            "ndarray (N-dimensional array): Un array multidimensional eficiente que puede contener elementos del mismo tipo."
        ],
        "Funcionalidades Principales": [
            "Creación de arrays n-dimensionales.",
            "Operaciones matemáticas eficientes (elemento a elemento y matriciales).",
            "Funciones para álgebra lineal, transformadas de Fourier y generación de números aleatorios.",
            "Indexación y slicing avanzados.",
            "Integración con otras librerías científicas de Python."
        ],
        "Casos de Uso Comunes": [
            "Cálculos científicos y de ingeniería.",
            "Análisis de datos numéricos.",
            "Implementación de algoritmos de machine learning.",
            "Procesamiento de imágenes y sonido.",
            "Simulaciones numéricas."
        ]
    }
    system('cls')
    print("\n--- ¿Qué es NumPy? ---")
    for clave, valor in info_numpy.items():
        print(f"{clave}:")
        if isinstance(valor, list):
            for item in valor:
                print(f"  - {item}")
        else:
            print(f"  {valor}")
    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

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

def menu_numpy()-> None:
    #Muestra el menú de opciones de la librería NumPy
    # Bucle Menu NumPy.
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_numpy()
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                que_es_numpy()
            elif opcion == '2':
                que_es_array_numpy()
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
            elif opcion == '9':
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")

"""
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
                menu_numpy()
            elif opcion == '3':
                None
            elif opcion == '4':
                None
            elif opcion == '9':
                print("¡Despegando hacia la próxima aventura!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")
"""