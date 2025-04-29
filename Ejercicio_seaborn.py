# Ejercicio carga de seaborn
# Importar librerías    
import pandas as pd
import os
import matplotlib.pyplot as plt 
import seaborn as sns

os.system('cls')

# Definir la ruta del archivo Excel
ruta_archivo = 'notas_estudiantes.csv'

# Verificar si el archivo existe
if os.path.exists(ruta_archivo):
    # Leer el archivo csv
    df = pd.read_csv(ruta_archivo)
    
    # Mostrar información del DataFrame
    print(df.info())

    # Mostrar las primeras filas del DataFrame
    print(df.head())

    # Mostrar estadísticas descriptivas
    print(df.describe())    
    
    # 1. Agrupar por asignatura y calcular la nota media
    nota_media_por_asignatura = df.groupby('asignatura')['nota'].mean().sort_values(ascending=False)
    print("\n--- Nota Media por Asignatura ---")
    print(nota_media_por_asignatura)

    # 2. Crear un gráfico de barras con plt.bar() mostrando las notas medias por asignatura
    plt.figure(figsize=(10, 6))
    plt.bar(nota_media_por_asignatura.index, nota_media_por_asignatura.values, color='skyblue')
    plt.title('Nota Media por Asignatura (matplotlib)')
    plt.xlabel('Asignatura')
    plt.ylabel('Nota Media')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # 3. Elegir un estudiante y graficar sus notas con un gráfico de líneas (plt.plot())
    estudiante_elegido = 'Estudiante_1'  # Puedes cambiar este nombre por otro estudiante presente en el DataFrame
    notas_estudiante = df[df['estudiante'] == estudiante_elegido].sort_values(by='fecha')

    if not notas_estudiante.empty:
        plt.figure(figsize=(10, 6))
        plt.plot(notas_estudiante['asignatura'], notas_estudiante['nota'], marker='o', linestyle='-', color='coral')
        plt.title(f'Notas de {estudiante_elegido} por Asignatura (matplotlib)')
        plt.xlabel('Asignatura')
        plt.ylabel('Nota')
        plt.grid(axis='y', alpha=0.7)
        plt.tight_layout()
        plt.show()
    else:
        print(f"\nNo se encontraron notas para el estudiante '{estudiante_elegido}'.")

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

    # Crear la figura comparando cuatro estudiantes
    # 4. Comparar las notas de cuatro estudiantes en un gráfico de líneas
    plt.figure(figsize=(12, 7))
    plt.title('Comparación de Notas de cuatro Estudiantes por Asignatura', fontsize=16)

    # Seleccionar los dos estudiantes que queremos comparar
    estudiante1 = 'Estudiante_1'  # Puedes cambiar este nombre
    estudiante2 = 'Estudiante_2'  # Puedes cambiar este nombre
    estudiante3 = 'Estudiante_3'  # Puedes cambiar este nombre
    estudiante4 = 'Estudiante_4'  # Puedes cambiar este nombre

    # Filtrar las notas del primer estudiante y ordenarlas por fecha
    notas_estudiante1 = df[df['estudiante'] == estudiante1].sort_values(by='fecha')

    # Filtrar las notas del segundo estudiante y ordenarlas por fecha
    notas_estudiante2 = df[df['estudiante'] == estudiante2].sort_values(by='fecha')

    # Filtrar las notas del tercer estudiante y ordenarlas por fecha
    notas_estudiante3 = df[df['estudiante'] == estudiante3].sort_values(by='fecha')

    # Filtrar las notas del tercer estudiante y ordenarlas por fecha
    notas_estudiante4 = df[df['estudiante'] == estudiante4].sort_values(by='fecha')

    # Graficar las notas del primer estudiante
    if not notas_estudiante1.empty:
        sns.lineplot(x='asignatura', y='nota', data=notas_estudiante1, marker='o', label=estudiante1)

    # Graficar las notas del segundo estudiante
    if not notas_estudiante2.empty:
        sns.lineplot(x='asignatura', y='nota', data=notas_estudiante2, marker='o', label=estudiante2)

    # Graficar las notas del tercer estudiante
    if not notas_estudiante3.empty:
        sns.lineplot(x='asignatura', y='nota', data=notas_estudiante3, marker='o', label=estudiante3)

    # Graficar las notas del segundo estudiante
    if not notas_estudiante4.empty:
        sns.lineplot(x='asignatura', y='nota', data=notas_estudiante4, marker='o', label=estudiante4)

    plt.xlabel('Asignatura')
    plt.ylabel('Nota')
    plt.grid(axis='y', alpha=0.7)
    plt.legend()  # Mostrar la leyenda para identificar a cada estudiante
    plt.tight_layout()
    plt.show()

    # Seleccionar los cuatro estudiantes
    estudiantes_a_comparar = ['Estudiante_1', 'Estudiante_2', 'Estudiante_3', 'Estudiante_4']
    df_filtrado = df[df['estudiante'].isin(estudiantes_a_comparar)]

    plt.figure(figsize=(12, 7))
    sns.barplot(x='asignatura', y='nota', hue='estudiante', data=df_filtrado, palette='viridis')
    plt.title('Comparación de Notas de Cuatro Estudiantes por Asignatura (Barras Agrupadas)', fontsize=16)
    plt.xlabel('Asignatura')
    plt.ylabel('Nota')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Estudiante')
    plt.tight_layout()
    plt.show()    

    plt.figure(figsize=(12, 7))
    sns.pointplot(x='asignatura', y='nota', hue='estudiante', data=df_filtrado, palette='viridis', dodge=True)
    plt.title('Comparación de Notas de Cuatro Estudiantes por Asignatura (Puntos)', fontsize=16)
    plt.xlabel('Asignatura')
    plt.ylabel('Nota')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Estudiante')
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

    
    # Seleccionar los cuatro estudiantes
    estudiantes_a_comparar = ['Estudiante_1', 'Estudiante_2', 'Estudiante_3', 'Estudiante_4']
    df_filtrado = df[df['estudiante'].isin(estudiantes_a_comparar)]

    # Calcular la media de todas las notas
    media_global = df['nota'].mean()

    # Crear la figura y la matriz de subplots (2 filas, 2 columnas)
    fig, axes = plt.subplots(2, 2, figsize=(18, 14))
    fig.suptitle('Comparación de Notas de Cuatro Estudiantes por Asignatura', fontsize=16)

    # 1. Gráfico de líneas (axes[0, 0])
    axes[0, 0].set_title('Gráfico de Líneas')
    for estudiante in estudiantes_a_comparar:
        notas_estudiante = df[df['estudiante'] == estudiante].sort_values(by='fecha')
        if not notas_estudiante.empty:
            sns.lineplot(x='asignatura', y='nota', data=notas_estudiante, marker='o', label=estudiante, ax=axes[0, 0])
    axes[0, 0].axhline(media_global, color='r', linestyle='--', label=f'Media Global ({media_global:.2f})')
    axes[0, 0].set_xlabel('Asignatura')
    axes[0, 0].set_ylabel('Nota')
    #axes[0, 0].tick_params(axis='x', rotation=45, ha='right')
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
    #axes[0, 1].tick_params(axis='x', rotation=45, ha='right')
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
    #axes[1, 0].tick_params(axis='x', rotation=45, ha='right')
    etiquetas_x_puntos = axes[1, 0].get_xticklabels()
    plt.setp(etiquetas_x_puntos, rotation=45, ha='right')
    axes[1, 0].legend(title='Estudiante')
    axes[1, 0].grid(axis='y', linestyle='--')

    # 4. Subplot vacío (axes[1, 1]) - Lo dejamos en blanco o podríamos añadir otra visualización si tuviéramos alguna otra idea
    axes[1, 1].axis('off')  # Desactivar los ejes para que quede en blanco

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar layout para el título principal
    plt.show()
