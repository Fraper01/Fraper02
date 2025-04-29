from os import system, path 
import time
import pandas as pd
import pildoraNumpy

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

def mostrar_pandas()-> None:
    #Muestra el menú de Pandas."""
    system('cls')
    titulo = "Librerias de Python Pandas"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))  
    print("1. Definición de Pandas")
    print("2. Que es un DataFrame") 
    print("3. Que es un Series")
    print("4. Crear y visualicar DataFrame")
    print("5. Ejemplos de uso")
    print("0. Regresar al menú principal")
    print("-" * ancho_linea)

def mostrar_pandas_dataFrame_Eemplos()-> None:
    #Muestra el menú de Pandas."""
    system('cls')
    titulo = "Ejemplos Pandas DataFrame"
    ancho_linea = 40
    print("Elaborado por: Monica & Francisco")
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))  
    print("1. Media DataFrame de Pandas")
    print("2. Mediana DataFrame de Pandas") 
    print("3. Modal DataFrame de Pandas")
    print("4. Modal con Frecuencia DataFrame de Pandas")
    print("5. Desviación Estándar DataFrame de Pandas") 
    print("6. Crear un DataFrame con SQL") 
    print("7. Crear un DataFrame desde CSV")
    print("0. Regresar al menú principal")
    print("-" * ancho_linea)


def crea_r_csv()-> None:
    #"""Crea un archivo CSV de ejemplo."""
    # Se utiliza un diccionario para almacenar información sobre la librería CSV.
    if not path.exists('ejemplo.csv'):
        data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
                'Sexo': ['F', 'M', 'M', 'M', 'F', 'M', 'F'],
                'Edad': [25, 30, 22, 35, 28, 30, 22],
                'Puntuación': [88, 95, 78, 88, 95, 95, 88]}
        df = pd.DataFrame(data)
        df.to_csv('ejemplo.csv', index=False)
        print("\nArchivo 'ejemplo.csv' creado.") 

def ejemplo_csv_dataFrame() -> None:
    #""Ejemplo de cómo crear un DataFrame de Pandas desde un archivo CSV."""
    crea_r_csv()
    system('cls')
    print("\n--- Crear DataFrame desde CSV con Pandas ---")
    print("Este ejemplo muestra cómo utilizar pd.read_csv() para cargar datos desde un archivo CSV en un DataFrame de Pandas.")

    # 1. Especificar la ruta del archivo CSV
    csv_file_path = 'ejemplo.csv'  
    print(f"\nRuta del archivo CSV: {csv_file_path}")
    print("Syntax: csv_file_path = 'ruta/a/tu/ejemplo.csv'")

    # 2. Intentar leer el archivo CSV y cargarlo en un DataFrame
    df_from_csv = None  # Inicializar df_from_csv para manejar el caso de error
    try:
        df_from_csv = pd.read_csv(csv_file_path)
        print("\nSyntax: df_from_csv = pd.read_csv(csv_file_path)")
        print("\nDataFrame creado a partir del archivo CSV:")
        print(df_from_csv)
    except FileNotFoundError:
        print(f"\nError: No se encontró el archivo CSV en la ruta: {csv_file_path}")
    except pd.errors.EmptyDataError:
        print(f"\nError: El archivo CSV en la ruta: {csv_file_path} está vacío.")
    except pd.errors.ParserError as e:
        print(f"\nError al analizar el archivo CSV en la ruta: {csv_file_path}: {e}")
    except Exception as e:
        print(f"\nOcurrió un error inesperado al leer el archivo CSV: {e}")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def ejemplo_sql_dataFrame()-> None:
    #"""Ejemplo de uso de la función read_sql() en un DataFrame de Pandas."""
    # Se importa la librería Pandas y se le asigna el alias pd.
    # Se utiliza un diccionario para almacenar información sobre la librería SQL.
    # Este diccionario contiene claves y valores que describen la librería, sus estructuras de datos clave, funcionalidades principales y casos de uso comunes.
    system('cls')
    print("\n--- DataFrame de Pandas SQL ---")
    print("Ejemplo de uso de la función read_sql() en un DataFrame de Pandas.")
    print("La función read_sql() se utiliza para leer datos desde una base de datos SQL y cargarlos en un DataFrame.")
    import sqlite3
    # 1. Establecer la conexión a la base de datos
    conn = None  # Inicializar conn fuera del try para poder referenciarlo en finally
    try:
        conn = sqlite3.connect('ejemplo.db')
        print("\nConexión a la base de datos 'ejemplo.db' establecida. syntax: conn = sqlite3.connect('ejemplo.db')")

        # 2. Definir la consulta SQL que deseas ejecutar
        sql_query = "SELECT nombre, sexo, edad, puntuacion FROM estudiantes "
        print(f"\nConsulta SQL a ejecutar: sql_query = '{sql_query}'")

        # 3. Utilizar pd.read_sql_query() para ejecutar la consulta y cargar los resultados en un DataFrame
        df_from_sql = pd.read_sql_query(sql_query, conn)
        print("\nDataFrame creado a partir de la consulta SQL: ")
        print(df_from_sql)

    except sqlite3.Error as e:
        print(f"\nError al ejecutar la consulta SQL o al leer los datos: {e}")

    except pd.errors.DatabaseError as e:
        print(f"\nError específico de Pandas al interactuar con la base de datos: {e}")
        print("\nDataFrame creado a partir de la consulta SQL: ")
        print("\ndf_from_sql = pd.read_sql_query(sql_query, conn)")

    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
    finally:
        # 4. Cerrar la conexión a la base de datos (es importante hacerlo en el bloque finally)
        if 'conn' in locals() and conn:
            conn.close()
            print("\nConexión a la base de datos cerrada.")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def ejemplo_desviacion_dataFrame()-> None:
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
            'Sexo': ['F', 'M', 'M', 'M', 'F', 'M', 'F'],
            'Edad': [25, 30, 22, 35, 28, 30, 22],
            'Puntuación': [88, 95, 78, 88, 95, 95, 88]}
    df = pd.DataFrame(data)

    system('cls')
    print("\n--- DataFrame de Pandas ---")
    print(df)
    print("\n--- Desviación Estándar por Columna Numérica ---")
    # Es una medida de cuánto se dispersan o se alejan los valores individuales de la media (promedio)
    # Calcular la desviación estándar de la columna 'Edad'
    desviacion_estandar_edad = df['Edad'].std()
    print(f"Desviación Estándar de la columna 'Edad': {desviacion_estandar_edad:.2f}"+ " Syntax: desviacion_estandar_edad = df['Edad'].std()")

    # Calcular la desviación estándar de la columna 'Puntuación'
    desviacion_estandar_puntuacion = df['Puntuación'].std()
    print(f"Desviación Estándar de la columna 'Puntuación': {desviacion_estandar_puntuacion:.2f}"+ " Syntax: desviacion_estandar_puntuacion = df['Puntuación'].std()")

    # Intentar calcular la desviación estándar de la columna 'Sexo' (no numérica)
    # Esto devolverá un error o un resultado no significativo, dependiendo de la versión de Pandas.
    # Generalmente, .std() solo opera en columnas numéricas.
    try:
        desviacion_estandar_sexo = df['Sexo'].std()
        print(f"Desviación Estándar de la columna 'Sexo': {desviacion_estandar_sexo}")
    except TypeError as e:
        print(f"\nError al calcular la desviación estándar de la columna 'Sexo': {e}")
        print("La desviación estándar solo se calcula para columnas numéricas.")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def ejemplo_modaFrecuencua()-> None:
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
            'Sexo': ['F', 'M', 'M', 'M', 'F', 'M', 'F'], 
            'Edad': [25, 30, 22, 35, 28, 30, 22],
            'Puntuación': [88, 95, 78, 88, 95, 95, 88]} 
    df = pd.DataFrame(data)

    system('cls')
    print("\n--- DataFrame de Pandas ---")
    print(df)
    print("\n--- Frecuencia de las Modas por Columna ---")

    def obtener_frecuencia_modas(serie):
        #""Calcula la moda de una Serie y su frecuencia."""
        modas = serie.mode()
        frecuencias = serie.value_counts()
        resultado = {}
        if not modas.empty:
            for moda in modas:
                if moda in frecuencias:
                    resultado[moda] = frecuencias[moda]
        return resultado

    # Frecuencia de las modas de la columna 'Edad'
    frecuencia_moda_edad = obtener_frecuencia_modas(df['Edad'])
    print(f"\nFrecuencia de la(s) moda(s) de la columna 'Edad':")
    if frecuencia_moda_edad:
        for moda, frecuencia in frecuencia_moda_edad.items():
            print(f"     La moda {moda} aparece {frecuencia} veces.")
    else:
        print("No se encontraron modas.")

    # Frecuencia de las modas de la columna 'Sexo'
    frecuencia_moda_sexo = obtener_frecuencia_modas(df['Sexo'])
    print(f"\nFrecuencia de la(s) moda(s) de la columna 'Sexo':")
    if frecuencia_moda_sexo:
        for moda, frecuencia in frecuencia_moda_sexo.items():
            print(f"     La moda {moda} aparece {frecuencia} veces.")
    else:
        print("No se encontraron modas.")

    # Frecuencia de las modas de la columna 'Puntuación'
    frecuencia_moda_puntuacion = obtener_frecuencia_modas(df['Puntuación'])
    print(f"\nFrecuencia de la(s) moda(s) de la columna 'Puntuación':")
    if frecuencia_moda_puntuacion:
        for moda, frecuencia in frecuencia_moda_puntuacion.items():
            print(f"     La moda {moda} aparece {frecuencia} veces.")
    else:
        print("No se encontraron modas.")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def ejemplo_moda_dataFrame()-> None:
    #"""Ejemplo de uso de la función moda() en un DataFrame de Pandas."""
    # Se importa la librería Pandas y se le asigna el alias pd.
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
            'Sexo': ['F', 'M', 'M', 'M', 'F', 'M', 'F'], 
            'Edad': [25, 30, 22, 35, 28, 30, 22],
            'Puntuación': [88, 95, 78, 88, 95, 95, 88]} 
    df = pd.DataFrame(data)
    system('cls')
    print("\n--- DataFrame de Pandas ---")
    print(df)
    print("\n--- Moda de cada columna ---")
    # Se utiliza el método mode() para calcular la mediana de cada columna del DataFrame. 
    # La Moda es el valor que aparece con mayor frecuencia.
    moda_edad = df['Edad'].mode()
    moda_sexo = df['Sexo'].mode()
    moda_puntuacion = df['Puntuación'].mode()

    print(f"Moda de la columna 'Edad': "+ " Syntax: moda_edad = df['Edad'].mode()")
    print(f"{moda_edad} ")
    print(f"Moda de la columna 'Puntuación':"+ " Syntax: moda_puntuacion = df['Puntuación'].mode()")
    print(f"{moda_puntuacion} ")
    print(f"Moda de la columna 'Sexo': "+ " Syntax: moda_sexo = df['Sexo'].mode()")
    print(f"{moda_sexo}")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def ejemplo_mediana_dataFrame()-> None:
    #"""Ejemplo de uso de la función mediana() en un DataFrame de Pandas."""
    # Se importa la librería Pandas y se le asigna el alias pd.
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
            'Edad': [25, 30, 22, 35],
            'Puntuación': [85, 92, 78, 88]}
    df = pd.DataFrame(data)
    system('cls')
    print("\n--- DataFrame de Pandas ---")
    print(df)
    print("\n--- Mediana de cada columna Númerica ---")
    # Se utiliza el método median() para calcular la mediana de cada columna del DataFrame. 
    # La mediana es el valor central y es más resistente a los valores atípicos.
    mediana_edad = df['Edad'].median()
    mediana_puntuacion = df['Puntuación'].median()

    print(f"Mediana de la columna 'Edad': {mediana_edad} " + " Syntax: mediana_edad = df['Edad'].median()")
    print(f"Mediana de la columna 'Puntuación': {mediana_puntuacion}"+ " Syntax: mediana_puntuacion = df['Puntuación'].median()")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def ejemplo_media_dataFrame()-> None:
    #"""Ejemplo de uso de la función media() en un DataFrame de Pandas."""
    # Se importa la librería Pandas y se le asigna el alias pd.
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
            'Edad': [25, 30, 22, 35],
            'Puntuación': [85, 92, 78, 88]}
    df = pd.DataFrame(data)
    system('cls')
    print("\n--- DataFrame de Pandas ---")
    print(df)
    print("\n--- Media de cada columna Númerica ---")
    # Se utiliza el método mean() para calcular la media de cada columna del DataFrame. 
    # La media es el promedio aritmético y considera todos los valores.
    media_edad = df['Edad'].mean()
    media_puntuacion = df['Puntuación'].mean()

    print(f"Media de la columna 'Edad': {media_edad} " + " Syntax: media_edad = df['Edad'].mean()")
    print(f"Media de la columna 'Puntuación': {media_puntuacion}"+ " Syntax: media_puntuacion = df['Puntuación'].mean()")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def crear_visualizar_dataframe()->None:
    #"""Crea un DataFrame de Pandas y muestra información básica."""
    # Se importa la librería Pandas y se le asigna el alias pd.
    data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
            'Edad': [25, 30, 22, 35],
            'Puntuación': [85, 92, 78, 88]}
    df = pd.DataFrame(data)
    # Se utiliza un bucle for para iterar sobre las claves y valores del diccionario.
    # Para cada clave, se imprime su nombre y su valor correspondiente.
    system('cls')
    print("\n--- Diccionario Data ---")
    for clave, valor in data.items():
        print(f"{clave}:")
        # Si el valor es una lista, se imprime cada elemento de la lista en una nueva línea.    
        # Si el valor no es una lista, se imprime directamente.
        # Esto permite una presentación clara y estructurada de la información.
        if isinstance(valor, list):
            for item in valor:
                print(f"  - {item}")
        else:
            print(f"  {valor}")
    print("\n--- DataFrame de Pandas ---")
    print(df)
    print("\nInformación del DataFrame:")
    df.info()
    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")


def que_es_series()->None:
    #"""Muestra información general sobre la librería Pandas."""
    # Se utiliza un diccionario para almacenar información sobre la librería Series.
    # Este diccionario contiene claves y valores que describen la librería, sus estructuras de datos clave, funcionalidades principales y casos de uso comunes.
    info_serie_pandas = {
        "Nombre": "Serie de Pandas",
        "Descripción": "Estructura de datos unidimensional con etiquetas (índice). Puede considerarse como un array etiquetado o una columna de un DataFrame.",
        "Componentes Clave": [
            "Datos: Un array unidimensional de datos (de cualquier tipo de dato de NumPy: int, float, object, etc.).",
            "Índice: Un array de etiquetas asociado a los datos. Si no se especifica, se utiliza un índice entero por defecto (0, 1, 2, ...)."
        ],
        "Características Principales": [
            "Almacenamiento eficiente de datos unidimensionales.",
            "Acceso a los datos mediante etiquetas (índice) o posición.",
            "Soporte para operaciones vectorizadas y alineación basada en el índice.",
            "Puede convertirse fácilmente en una columna de un DataFrame."
        ],
        "Uso Principal": "Representación y manipulación de secuencias de datos etiquetados en Python para análisis de datos."
    }
    system('cls')
    print("\n--- ¿Qué es Serie? ---")
    # Se utiliza un bucle for para iterar sobre las claves y valores del diccionario.
    # Para cada clave, se imprime su nombre y su valor correspondiente.
    for clave, valor in info_serie_pandas.items():
        print(f"{clave}:")
        # Si el valor es una lista, se imprime cada elemento de la lista en una nueva línea.    
        # Si el valor no es una lista, se imprime directamente.
        # Esto permite una presentación clara y estructurada de la información.
        if isinstance(valor, list):
            for item in valor:
                print(f"  - {item}")
        else:
            print(f"  {valor}")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def que_es_dataFrame()->None:
    #"""Muestra información general sobre la librería Pandas."""
    # Se utiliza un diccionario para almacenar información sobre la librería DataFrame.
    # Este diccionario contiene claves y valores que describen la librería, sus estructuras de datos clave, funcionalidades principales y casos de uso comunes.
    info_dataframe_pandas = {
        "Nombre": "DataFrame de Pandas",
        "Descripción": "Estructura de datos tabular bidimensional con etiquetas en filas (índice) y columnas. Similar a una hoja de cálculo o una tabla SQL.",
        "Componentes Clave": [
            "Datos: Contenido tabular organizado en filas y columnas.",
            "Índice: Etiquetas para identificar las filas (puede ser numérico o basado en tiempo, etc.).",
            "Columnas: Etiquetas para identificar las diferentes variables o series de datos."
        ],
        "Características Principales": [
            "Almacenamiento eficiente de datos heterogéneos.",
            "Facilidad para realizar operaciones de manipulación, filtrado y transformación.",
            "Integración con otras librerías de Python para análisis y visualización."
        ],
        "Uso Principal": "Representación y manipulación de conjuntos de datos tabulares en Python para análisis de datos."
    }
    system('cls')
    print("\n--- ¿Qué es DataFrame? ---")
    # Se utiliza un bucle for para iterar sobre las claves y valores del diccionario.
    # Para cada clave, se imprime su nombre y su valor correspondiente.
    for clave, valor in info_dataframe_pandas.items():
        print(f"{clave}:")
        # Si el valor es una lista, se imprime cada elemento de la lista en una nueva línea.    
        # Si el valor no es una lista, se imprime directamente.
        # Esto permite una presentación clara y estructurada de la información.
        if isinstance(valor, list):
            for item in valor:
                print(f"  - {item}")
        else:
            print(f"  {valor}")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def que_es_pandas()->None:
    #"""Muestra información general sobre la librería Pandas."""
    # Se utiliza un diccionario para almacenar información sobre la librería Pandas.
    # Este diccionario contiene claves y valores que describen la librería, sus estructuras de datos clave, funcionalidades principales y casos de uso comunes.
    info_pandas = {
        "Nombre": "Pandas",
        "Descripción": "Es una librería de Python de código abierto que proporciona herramientas de análisis y manipulación de datos de alto rendimiento y fáciles de usar.",
        "Estructuras de Datos Clave": [
            "DataFrame: Una estructura de datos tabular bidimensional con etiquetas en filas y columnas. Puede pensarse como una hoja de cálculo o una tabla de SQL.",
            "Series: Una estructura de datos unidimensional con etiquetas (un array etiquetado). Es la base de un DataFrame."
        ],
        "Funcionalidades Principales": [
            "Carga y manipulación de datos desde diversos formatos (CSV, Excel, SQL, etc.).",
            "Limpieza y preparación de datos (manejo de valores faltantes, filtrado, ordenamiento, etc.).",
            "Análisis exploratorio de datos (estadísticas descriptivas, agrupamiento, agregación).",
            "Combinación y unión de conjuntos de datos.",
            "Visualización básica de datos (integración con Matplotlib)."
        ],
        "Casos de Uso Comunes": [
            "Análisis de datos financieros.",
            "Procesamiento de datos de series de tiempo.",
            "Limpieza y preparación de datos para modelos de machine learning.",
            "Análisis de datos de encuestas.",
            "Exploración y visualización de datos."
        ]
    }

    system('cls')
    print("\n--- ¿Qué es Pandas? ---")
    # Se utiliza un bucle for para iterar sobre las claves y valores del diccionario.
    # Para cada clave, se imprime su nombre y su valor correspondiente.
    for clave, valor in info_pandas.items():
        print(f"{clave}:")
        # Si el valor es una lista, se imprime cada elemento de la lista en una nueva línea.    
        # Si el valor no es una lista, se imprime directamente.
        # Esto permite una presentación clara y estructurada de la información.
        if isinstance(valor, list):
            for item in valor:
                print(f"  - {item}")
        else:
            print(f"  {valor}")

    print("\n--- Fin de la información ---")
    input("Pulse Enter para continuar...")

def menu_pandas_ejercicios()-> None:
    #Muestra el menú de opciones de la librería Pandas Ejercicios
    # Bucle Menu Pandas.
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_pandas_dataFrame_Eemplos()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                ejemplo_media_dataFrame()
            elif opcion == '2':
                ejemplo_mediana_dataFrame()
            elif opcion == '3':
                ejemplo_moda_dataFrame()
            elif opcion == '4':
                ejemplo_modaFrecuencua()
            elif opcion == '5':
                ejemplo_desviacion_dataFrame()
            elif opcion == '6':
                ejemplo_sql_dataFrame()
            elif opcion == '7':
                ejemplo_csv_dataFrame()
            elif opcion == '0':
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")

def menu_pandas()-> None:
    #Muestra el menú de opciones de la librería Pandas
    # Bucle Menu Pandas.
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_pandas()
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                que_es_pandas()
            elif opcion == '2':
                que_es_dataFrame()
            elif opcion == '3':
                que_es_series()
            elif opcion == '4':
                crear_visualizar_dataframe()
            elif opcion == '5':
                menu_pandas_ejercicios()
            elif opcion == '0':
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")

"""
# Este bloque se ejecuta solo si el script se ejecuta directamente, no si se importa como un módulo.
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
                menu_pandas()
            elif opcion == '2':
                pildoraNumpy.menu_numpy()
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
