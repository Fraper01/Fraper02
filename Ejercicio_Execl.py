# Ejercicio carga de Excel
# Importar librerías    
import pandas as pd
import os
import matplotlib.pyplot as plt 

os.system('cls')

# Definir la ruta del archivo Excel
ruta_archivo = 'ventas.csv'

# Verificar si el archivo existe
if os.path.exists(ruta_archivo):
    # Leer el archivo Excel
    df = pd.read_csv(ruta_archivo)
    
    # Mostrar información del DataFrame
    print(df.info())

    # Mostrar las primeras filas del DataFrame
    print(df.head())

    # Mostrar estadísticas descriptivas
    print(df.describe())    

    df['total'] = df['precio'] * df['unidades']  # Calcular el total
    print("\n--- Total de Ventas ---")

    print(df[['producto', 'total']])
    print("\n--- Total de Ventas por Producto ---")
    
    print(df.groupby('producto')['total'].sum())

    print("\n--- Productos con más de 3 unidades vendidas ---")
    print(df[df['unidades'] > 3])# Filtrar productos con más de 3 unidades vendidas

    df['fecha'] = pd.to_datetime(df['fecha'])  # Convertir la columna 'fecha' a tipo datetime
    df['mes'] = df['fecha'].dt.month  # Extraer el mes de la fecha
    df['año'] = df['fecha'].dt.year  # Extraer el año de la fecha

    df.head()  # Mostrar las primeras filas del DataFrame actualizado
    print("\n--- Ventas por Mes y Año ---")
    print(df.groupby(['año', 'mes'])['total'].sum())  # Agrupar por año y mes y calcular el total de ventas
    print("\n--- Ventas por Mes  ---")
    print(df.groupby(['mes'])['total'].sum())  # Agrupar por año y mes y calcular el total de ventas
    print("\n--- Ventas por Producto ---")
    print(df.groupby('producto')['total'].sum())  # Agrupar por producto y calcular el total de ventas

    # --- Gráfico de Líneas (plot) ---
    if 'fecha' in df.columns and 'total' in df.columns:
        plt.figure(figsize=(10, 6))
        ventas_por_fecha = df.groupby('fecha')['total'].sum()
        plt.plot(ventas_por_fecha.index, ventas_por_fecha.values, marker='o', linestyle='-')
        plt.title('Total de Ventas por Fecha')
        plt.xlabel('Fecha')
        plt.ylabel('Total de Ventas')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No se pueden crear el gráfico de líneas: faltan las columnas 'fecha' o 'total'.")

    # --- Gráfico de Barras (bar) ---
    if 'producto' in df.columns and 'total' in df.columns:
        plt.figure(figsize=(10, 6))
        ventas_por_producto = df.groupby('producto')['total'].sum().sort_values(ascending=False)
        plt.bar(ventas_por_producto.index, ventas_por_producto.values, color='skyblue')
        plt.title('Total de Ventas por Producto')
        plt.xlabel('Producto')
        plt.ylabel('Total de Ventas')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("No se pueden crear el gráfico de barras: faltan las columnas 'producto' o 'total'.")

    # --- Gráfico de Dispersión (scatter) ---
    if 'unidades' in df.columns and 'precio' in df.columns:
        plt.figure(figsize=(8, 6))
        plt.scatter(df['unidades'], df['precio'], color='coral', alpha=0.7)
        plt.title('Relación entre Unidades Vendidas y Precio')
        plt.xlabel('Unidades Vendidas')
        plt.ylabel('Precio')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("No se pueden crear el gráfico de dispersión: faltan las columnas 'unidades' o 'precio'.")

    # --- Histograma (hist) ---
    if 'precio' in df.columns:
        plt.figure(figsize=(8, 6))
        plt.hist(df['precio'], bins=10, color='lightgreen', edgecolor='black')
        plt.title('Distribución de Precios')
        plt.xlabel('Precio')
        plt.ylabel('Frecuencia')
        plt.grid(axis='y', alpha=0.5)
        plt.tight_layout()
        plt.show()
    else:
        print("No se puede crear el histograma: falta la columna 'precio'.")

    # Crear la figura y la matriz de subplots (2 filas, 2 columnas)
    fig, axs = plt.subplots(1, 2, figsize=(15, 10))
    fig.suptitle('Análisis de Ventas', fontsize=16)

    # --- Gráfico de Líneas (plot) en axs[0, 0] ---
    if 'fecha' in df.columns and 'total' in df.columns:
        ventas_por_fecha = df.groupby('fecha')['total'].sum()
        axs[0, 0].plot(ventas_por_fecha.index, ventas_por_fecha.values, marker='o', linestyle='-')
        axs[0, 0].set_title('Ventas por Fecha')
        axs[0, 0].set_xlabel('Fecha')
        axs[0, 0].set_ylabel('Total Ventas')
        axs[0, 0].tick_params(axis='x', rotation=45, labelsize=8)
        axs[0, 0].grid(True)
    else:
        axs[0, 0].text(0.5, 0.5, 'Faltan datos para el gráfico de líneas', horizontalalignment='center', verticalalignment='center')

    # --- Gráfico de Barras (bar) en axs[0, 1] ---
    if 'producto' in df.columns and 'total' in df.columns:
        ventas_por_producto = df.groupby('producto')['total'].sum().sort_values(ascending=False)
        axs[0, 1].bar(ventas_por_producto.index, ventas_por_producto.values, color='skyblue')
        axs[0, 1].set_title('Ventas por Producto')
        axs[0, 1].set_xlabel('Producto')
        axs[0, 1].set_ylabel('Total Ventas')
        #axs[0, 1].xticks(rotation=45, ha='right')
        axs[0, 1].grid(axis='y', alpha=0.7)
        fig.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar layout para el título principal
    else:
        axs[0, 1].text(0.5, 0.5, 'Faltan datos para el gráfico de barras', horizontalalignment='center', verticalalignment='center')

    # --- Gráfico de Dispersión (scatter) en axs[1, 0] ---
    if 'unidades' in df.columns and 'precio' in df.columns:
        axs[1, 0].scatter(df['unidades'], df['precio'], color='coral', alpha=0.7)
        axs[1, 0].set_title('Unidades vs Precio')
        axs[1, 0].set_xlabel('Unidades')
        axs[1, 0].set_ylabel('Precio')
        axs[1, 0].grid(True)
    else:
        axs[1, 0].text(0.5, 0.5, 'Faltan datos para el gráfico de dispersión', horizontalalignment='center', verticalalignment='center')

    # --- Histograma (hist) en axs[1, 1] ---
    if 'precio' in df.columns:
        axs[1, 1].hist(df['precio'], bins=10, color='lightgreen', edgecolor='black')
        axs[1, 1].set_title('Distribución de Precios')
        axs[1, 1].set_xlabel('Precio')
        axs[1, 1].set_ylabel('Frecuencia')
        axs[1, 1].grid(axis='y', alpha=0.5)
    else:
        axs[1, 1].text(0.5, 0.5, 'Falta la columna "precio" para el histograma', horizontalalignment='center', verticalalignment='center')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar layout para evitar superposición
    plt.show()
    input("Presione Enter para continuar...")
        
else:
    print(f"El archivo {ruta_archivo} no existe.")

