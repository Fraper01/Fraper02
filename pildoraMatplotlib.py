from os import system, path
import time
import pandas as pd
import numpy as np  # Importamos la librería NumPy
import matplotlib.pyplot as plt
import ejercicio_aguacate2 as ea
import seaborn as sns

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
    print("6. Ejemplo de Aplicación")
    print("7. Ejercicio de Aplicación Estudiante")
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
    print("4. Gráfico de Bloxplot")
    print("5. Multiples Subgráficos")
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

def ejercicios_estudiante()-> None:
    # Definir la ruta del archivo Excel
    ruta_archivo = 'notas_estudiantes.csv'

    # Verificar si el archivo existe
    if path.exists(ruta_archivo):
        system('cls')
        texto = """
        Gráfico de Líneas y Gráfico de Barras con Matplotlib 
        # 1. Calcular la nota media por asignatura
        nota_media_por_asignatura = df.groupby('asignatura')['nota'].mean().sort_values(ascending=False)

        # 2. Elegir un estudiante y obtener sus notas
        estudiante_elegido = 'Estudiante_1'  # Puedes cambiar este nombre
        notas_estudiante = df[df['estudiante'] == estudiante_elegido].sort_values(by='fecha')

        # 3. Crear la figura y los subplots (1 fila, 2 columnas)
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        fig.suptitle('Análisis de Notas', fontsize=16)

        # 4. Gráfico de barras en el primer subplot (axes[0]) ---
        axes[0].bar(nota_media_por_asignatura.index, nota_media_por_asignatura.values, color='skyblue')
        axes[0].set_title('Nota Media por Asignatura (matplotlib)')
        axes[0].set_xlabel('Asignatura')
        axes[0].set_ylabel('Nota Media')
        ...

        # 5. Gráfico de líneas en el segundo subplot (axes[1]) ---
        axes[1].plot(notas_estudiante['asignatura'], notas_estudiante['nota'], marker='o', linestyle='-', color='coral')
        axes[1].set_title(f'Notas de {estudiante_elegido} por Asignatura (matplotlib)')
        axes[1].set_xlabel('Asignatura')
        axes[1].set_ylabel('Nota')
        ...
        plt.show()
        """
        print(texto)
        print("\nElaborado por: Mónica & Francisco")         
        input("Presione Enter para continuar...")

        # Leer el archivo csv
        df = pd.read_csv(ruta_archivo)
    
        # 1. Calcular la nota media por asignatura
        nota_media_por_asignatura = df.groupby('asignatura')['nota'].mean().sort_values(ascending=False)

        # 2. Elegir un estudiante y obtener sus notas
        estudiante_elegido = 'Estudiante_1'  # Puedes cambiar este nombre
        notas_estudiante = df[df['estudiante'] == estudiante_elegido].sort_values(by='fecha')

        try:
            # Crear la figura y los subplots (1 fila, 2 columnas)
            fig, axes = plt.subplots(1, 2, figsize=(15, 6))
            fig.suptitle('Análisis de Notas', fontsize=16)

            # --- Gráfico de barras en el primer subplot (axes[0]) ---
            axes[0].bar(nota_media_por_asignatura.index, nota_media_por_asignatura.values, color='skyblue')
            axes[0].set_title('Nota Media por Asignatura (matplotlib)')
            axes[0].set_xlabel('Asignatura')
            axes[0].set_ylabel('Nota Media')
            axes[0].grid(axis='y', alpha=0.7)
            axes[0].tick_params(axis='x', rotation=45, labelsize=8)
            etiquetas_x_barra = axes[0].get_xticklabels()
            plt.setp(etiquetas_x_barra, rotation=45, ha='right')

            # --- Gráfico de líneas en el segundo subplot (axes[1]) ---
            if not notas_estudiante.empty:
                axes[1].plot(notas_estudiante['asignatura'], notas_estudiante['nota'], marker='o', linestyle='-', color='coral')
                axes[1].set_title(f'Notas de {estudiante_elegido} por Asignatura (matplotlib)')
                axes[1].set_xlabel('Asignatura')
                axes[1].set_ylabel('Nota')
                axes[1].grid(axis='y', alpha=0.7)
                axes[1].tick_params(axis='x', rotation=45, labelsize=8)
                etiquetas_x_linea = axes[1].get_xticklabels()
                plt.setp(etiquetas_x_linea, rotation=45, ha='right')
            else:
                axes[1].text(0.5, 0.5, f'No se encontraron notas para el estudiante \'{estudiante_elegido}\'.', horizontalalignment='center', verticalalignment='center')

            plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar layout para el título principal
            plt.show()
        except Exception as e:
            print(f"Ocurrió un error: {e}")

        input("Presione Enter para continuar...")

        system('cls')
        texto = """
        Gráfico de Líneas y Gráfico de Barras con Seaborn
        # 1. Calcular la nota media por asignatura
        nota_media_por_asignatura = df.groupby('asignatura')['nota'].mean().sort_values(ascending=False).reset_index()

        # 2. Elegir un estudiante y obtener sus notas
        estudiante_elegido = 'Estudiante_2'  # Puedes cambiar este nombre
        notas_estudiante = df[df['estudiante'] == estudiante_elegido].sort_values(by='fecha')

        # Crear la figura y la matriz de subplots (1 fila, 2 columnas)
        fig, axes = plt.subplots(1, 2, figsize=(18, 6))
        fig.suptitle('Análisis de Notas de Estudiantes con Seaborn', fontsize=16)

        # 4. Gráfico de barras en el primer subplot (axes[0]) ---
        sns.barplot(x='asignatura', y='nota', hue='asignatura', data=nota_media_por_asignatura, palette='viridis', ax=axes[0], legend=False)
        axes[0].set_title('Nota Media por Asignatura (seaborn)')
        axes[0].set_xlabel('Asignatura')
        axes[0].set_ylabel('Nota Media')
        ...

        # 5. Gráfico de líneas en el segundo subplot (axes[1]) ---
        sns.lineplot(x='asignatura', y='nota', data=notas_estudiante, marker='o', color='coral', ax=axes[1])
        axes[1].set_title(f'Notas de {estudiante_elegido} por Asignatura (seaborn)')
        axes[1].set_xlabel('Asignatura')
        axes[1].set_ylabel('Nota')
        axes[1].grid(axis='y', alpha=0.7)
        ...
        plt.show()
        """
        print(texto)
        print("\nElaborado por: Mónica & Francisco")         
        input("Presione Enter para continuar...")

        # Crear la figura y la matriz de subplots (1 fila, 2 columnas)
        fig, axes = plt.subplots(1, 2, figsize=(18, 6))
        fig.suptitle('Análisis de Notas de Estudiantes con Seaborn', fontsize=16)

        # 1. Gráfico de barras con Seaborn mostrando la nota media por asignatura (en axes[0])
        nota_media_por_asignatura = df.groupby('asignatura')['nota'].mean().sort_values(ascending=False).reset_index()
        sns.barplot(x='asignatura', y='nota', hue='asignatura', data=nota_media_por_asignatura, palette='viridis', ax=axes[0], legend=False)
        axes[0].set_title('Nota Media por Asignatura (seaborn)')
        axes[0].set_xlabel('Asignatura')
        axes[0].set_ylabel('Nota Media')
        axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45, ha='right')
        axes[0].grid(axis='y', alpha=0.7)

        # 2. Elegir un estudiante y graficar sus notas con un gráfico de líneas con Seaborn (en axes[1])
        estudiante_elegido = 'Estudiante_2'  # Puedes cambiar este nombre
        notas_estudiante = df[df['estudiante'] == estudiante_elegido].sort_values(by='fecha')

        if not notas_estudiante.empty:
            sns.lineplot(x='asignatura', y='nota', data=notas_estudiante, marker='o', color='coral', ax=axes[1])
            axes[1].set_title(f'Notas de {estudiante_elegido} por Asignatura (seaborn)')
            axes[1].set_xlabel('Asignatura')
            axes[1].set_ylabel('Nota')
            axes[1].grid(axis='y', alpha=0.7)
        else:
            axes[1].text(0.5, 0.5, f'No se encontraron notas para {estudiante_elegido}', horizontalalignment='center', verticalalignment='center')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar layout para el título principal
        plt.show()

        system('cls')
        texto = """
        Gráfico de Líneas , Gráfico de Barras y Gráfico de Punto con Seaborn 
        Para 4 estudiantes
        # 1. Calcular la nota media 
        media_global = df['nota'].mean()

        # 2. Elegir 4 estudiante y obtener sus notas
        estudiantes_a_comparar = ['Estudiante_1', 'Estudiante_2', 'Estudiante_3', 'Estudiante_4']
        df_filtrado = df[df['estudiante'].isin(estudiantes_a_comparar)]

        # Crear la figura y la matriz de subplots (2 fila, 2 columnas)
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))
        fig.suptitle('Análisis de Notas de Estudiantes con Seaborn', fontsize=16)

        # 4. Gráfico de linea en el primer subplot (axes[0]) ---
        sns.lineplot(x='asignatura', y='nota', data=notas_estudiantes4, marker='o', label=estudiante, ax=axes[0, 0])
        axes[0, 0].axhline(media_global, color='r', linestyle='--', label=f'Media Global ({media_global:.2f})')
        axes[0, 0].set_xlabel('Asignatura')
        axes[0, 0].set_ylabel('Nota')
        ...

        # 5. Gráfico de Barra en el segundo subplot (axes[1]) ---
        sns.barplot(x='asignatura', y='nota', hue='estudiante', data=df_filtrado, palette='viridis', ax=axes[0, 1])
        axes[0, 1].axhline(media_global, color='r', linestyle='--', label=f'Media Global ({media_global:.2f})')
        axes[0, 1].set_xlabel('Asignatura')
        axes[0, 1].set_ylabel('Nota')
        ...

        # 6. Gráfico de Puntos en el segundo subplot (axes[1]) ---
        sns.pointplot(x='asignatura', y='nota', hue='estudiante', data=df_filtrado, palette='viridis', dodge=True, ax=axes[1, 0])
        axes[1, 0].axhline(media_global, color='r', linestyle='--', label=f'Media Global ({media_global:.2f})')
        axes[1, 0].set_xlabel('Asignatura')
        axes[1, 0].set_ylabel('Nota')
        plt.show()
        """
        print(texto)
        print("\nElaborado por: Mónica & Francisco")         
        input("Presione Enter para continuar...")
        # Seleccionar los cuatro estudiantes
        estudiantes_a_comparar = ['Estudiante_1', 'Estudiante_2', 'Estudiante_3', 'Estudiante_4']
        df_filtrado = df[df['estudiante'].isin(estudiantes_a_comparar)]

        # Seleccionar los cuatro estudiantes Utilizando Metodo isin()
        # y filtrar el DataFrame para obtener solo las filas correspondientes a esos estudiantes
        estudiantes_a_comparar = ['Estudiante_1', 'Estudiante_2', 'Estudiante_3', 'Estudiante_4']
        df_filtrado = df[df['estudiante'].isin(estudiantes_a_comparar)]

        # Seleccionar los cuatro estudiantes Utilizando un bucle for
        # y filtrar el DataFrame para obtener solo las filas correspondientes a esos estudiantes
        # Inicializa un DataFrame vacío para almacenar las notas de los estudiantes seleccionados
        notas_estudiantes4 = pd.DataFrame()
        for estudiante in estudiantes_a_comparar:
            notas_estudiante = df[df['estudiante'] == estudiante].sort_values(by='fecha')
            notas_estudiantes4 = pd.concat([notas_estudiantes4, notas_estudiante], ignore_index=True)

        # Calcular la media de todas las notas
        media_global = df['nota'].mean()

        # Crear la figura y la matriz de subplots (2 filas, 2 columnas)
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))
        fig.suptitle('Comparación de Notas de Cuatro Estudiantes por Asignatura', fontsize=16)

        # 1. Gráfico de líneas (axes[0, 0])
        axes[0, 0].set_title('Gráfico de Líneas')
        if not notas_estudiante.empty:
            sns.lineplot(x='asignatura', y='nota', hue='estudiante', data=notas_estudiantes4, marker='o', ax=axes[0, 0])
            axes[0, 0].axhline(media_global, color='r', linestyle='--', label=f'Media Global ({media_global:.2f})')
            axes[0, 0].set_xlabel('Asignatura')
            axes[0, 0].set_ylabel('Nota')
            etiquetas_x = axes[0, 0].get_xticklabels()
            plt.setp(etiquetas_x, rotation=45, ha='right')
            axes[0, 0].grid(axis='y', alpha=0.7)
            axes[0, 0].legend(title='Estudiante')

        # 2. Gráfico de barras agrupadas (axes[0, 1])
        axes[0, 1].set_title('Gráfico de Barras Agrupadas')
        sns.barplot(x='asignatura', y='nota', hue='estudiante', data=df_filtrado, palette='viridis', ax=axes[0, 1])
        axes[0, 1].axhline(media_global, color='r', linestyle='--', label=f'Media Global ({media_global:.2f})')
        axes[0, 1].set_xlabel('Asignatura')
        axes[0, 1].set_ylabel('Nota')
        etiquetas_x_barras = axes[0, 1].get_xticklabels()
        plt.setp(etiquetas_x_barras, rotation=45, ha='right')
        axes[0, 1].legend(title='Estudiante')
        axes[0, 1].grid(axis='y', alpha=0.7)

        # 3. Gráfico de puntos (axes[1, 0])
        axes[1, 0].set_title('Gráfico de Puntos')
        sns.pointplot(x='asignatura', y='nota', hue='estudiante', data=df_filtrado, palette='viridis', dodge=True, ax=axes[1, 0])
        axes[1, 0].axhline(media_global, color='r', linestyle='--', label=f'Media Global ({media_global:.2f})')
        axes[1, 0].set_xlabel('Asignatura')
        axes[1, 0].set_ylabel('Nota')
        etiquetas_x_puntos = axes[1, 0].get_xticklabels()
        plt.setp(etiquetas_x_puntos, rotation=45, ha='right')
        axes[1, 0].legend(title='Estudiante')
        axes[1, 0].grid(axis='y', linestyle='--')

        # 4. Subplot vacío (axes[1, 1]) - Lo dejamos en blanco o podríamos añadir otra visualización si tuviéramos alguna otra idea
        axes[1, 1].axis('off')  # Desactivar los ejes para que quede en blanco

        plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar layout para el título principal
        plt.show()

def ejemplo_multi_grafico()-> None:
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))  # Crear una figura con 3x2 subgráficos

    x = np.linspace(0, 10, 100)  # Definimos x aquí
    axs[0, 0].plot(x, np.cos(x))
    axs[0, 0].set_title('Coseno(x)')

    x_scatter = np.random.rand(50)
    y_scatter = np.random.rand(50)
    axs[0, 1].scatter(x_scatter, y_scatter, color='orange')
    axs[0, 1].set_title('Dispersión 2')

    aguacates = [150, 165, 140, 170, 155, 160, 145, 175, 150, 160, 165, 155]
    axs[0, 2].boxplot(aguacates, vert=False)  
    axs[0, 2].set_title('Boxplot')
    axs[0, 2].set_xlabel('Peso (gramos)')
    axs[0, 2].set_yticks([1])
    axs[0, 2].set_yticklabels(['Pesos'])

    # Definimos las variables 'categorias' y 'valores' aquí
    categorias = ['A', 'B', 'C', 'D']
    valores = [25, 40, 30, 55]
    axs[1, 0].bar(categorias, valores, color='cyan')
    axs[1, 0].set_title('Barras 2')

    axs[1, 1].hist(np.random.randn(100), bins=20, color='magenta', alpha=0.7)
    axs[1, 1].set_title('Histograma')

    # Gráfico de Violín para los pesos de los aguacates 
    axs[1, 2].violinplot(aguacates, vert=False, showmeans=True, showmedians=True)
    axs[1, 2].set_title('Violín Plot ')
    axs[1, 2].set_xlabel('Peso (gramos)')
    axs[1, 2].set_yticks([1])
    axs[1, 2].set_yticklabels(['Pesos'])

    fig.suptitle('Múltiples Subgráficos', fontsize=16)
    plt.tight_layout()  # Ajusta el espaciado entre subgráficos
    plt.show()

def ejemplo_graf_boxplot()-> None:
    aguacates = [150, 165, 140, 170, 155, 160, 145, 175, 150, 160, 165, 155]
    # Boxplot
    plt.boxplot(aguacates, vert=False)
    plt.title('Distribución del Peso de los Aguacates (Boxplot)')
    plt.xlabel('Peso (gramos)')
    plt.yticks([1], ['Pesos'])
    plt.grid(axis='x', alpha=0.5)
    plt.tight_layout()
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
    # crea un array NumPy llamado que contiene 50 números flotantes aleatorios, cada uno de ellos entre 0.0 (inclusive) y 1.0 (exclusive).
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
    # crea un array NumPy llamado x que contiene 100 números distribuidos de manera uniforme entre 0 y 10 (inclusive).
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
                consideraciones_matplotlib()
            elif opcion == '5':
                recursos_matplotlib()
            elif opcion == '6':
                ea.ejercicio_aguacate()
            elif opcion == '7':
                ejercicios_estudiante()
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
                ejemplo_graf_boxplot()
            elif opcion == '5':
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