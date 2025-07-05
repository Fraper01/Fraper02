import pandas as pd
import numpy as np
import sys 

def run_data_cleansing(ruta_archivo_excel):
    df_clientes = None # Inicializar df_clientes para asegurar su existencia

    # --- Carga de Datos (Paso 0) ---
    print("--- Iniciando Carga de Datos desde Excel ---")
    try:
        df_clientes = pd.read_excel(ruta_archivo_excel)
        print("¡DataFrame cargado exitosamente desde Excel!")
        print("\nPrimeras 5 filas del DataFrame original:")
        print(df_clientes.head())
        print("\nInformación del DataFrame original:")
        df_clientes.info()
        print("\nEstadísticas descriptivas del DataFrame original:")
        print(df_clientes.describe(include='all'))

    except FileNotFoundError:
        print(f"Error CRÍTICO: El archivo no fue encontrado en la ruta '{ruta_archivo_excel}'.")
        print("Verifica que la ruta y el nombre del archivo sean correctos. Abortando la ejecución.")
        return None # Abortar la función si el archivo no existe
    except ImportError:
        print("Error CRÍTICO: La librería 'openpyxl' no está instalada.")
        print("Por favor, instálala ejecutando 'pip install openpyxl' en tu terminal. Abortando la ejecución.")
        return None # Abortar la función si openpyxl no está instalado
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo de Excel: {e}. Abortando la ejecución.")
        return None # Abortar por otros errores de lectura

    # Hacemos una copia del DataFrame para trabajar con ella
    # Esto asegura que df_limpio siempre empiece desde el df_clientes recién cargado
    df_limpio = df_clientes.copy()
    print("\n--- Iniciando Proceso de Limpieza de Datos ---")

    ### 2.1 Completar los valores faltantes:

    # 2.1.1 Completar valores faltantes en 'Edad' con la mediana
    mediana_edad = df_limpio['Edad'].median()
    df_limpio['Edad'] = df_limpio['Edad'].fillna(mediana_edad)
    print(f"\nValores faltantes en 'Edad' rellenados con la mediana ({mediana_edad}).")

    # 2.1.2 Completar valores faltantes en 'Destino_favorito' con "Desconocido"
    df_limpio['Destino_favorito'] = df_limpio['Destino_favorito'].fillna("Desconocido")
    print(f"Valores faltantes en 'Destino_favorito' rellenados con 'Desconocido'.")

    # 2.1.3 Completar valores faltantes en 'Gasto_promedio' con la media
    media_gasto = df_limpio['Gasto_promedio'].mean()
    df_limpio['Gasto_promedio'] = df_limpio['Gasto_promedio'].fillna(media_gasto)    
    print(f"Valores faltantes en 'Gasto_promedio' rellenados con la media ({media_gasto:.2f}).")

    # Verificar si aún quedan valores faltantes después de la limpieza
    print("\nValores faltantes después de rellenar:")
    print(df_limpio.isnull().sum())

    ### 2.2 Corregir los valores erróneos:

    # 2.2.1 Corregir edades fuera de rango (18-90 años):
    edad_minima_aceptable = 18
    edad_maxima_aceptable = 90
    df_limpio.loc[df_limpio['Edad'] < edad_minima_aceptable, 'Edad'] = mediana_edad
    df_limpio.loc[df_limpio['Edad'] > edad_maxima_aceptable, 'Edad'] = mediana_edad
    print("\nEdades fuera de rango (18-90) corregidas (si existían).")

    # 2.2.2 Corregir nombres incorrectos por "Desconocido" (ej. "###")
    df_limpio['Nombre'] = df_limpio['Nombre'].replace('###', 'Desconocido')
    print("\nNombres incorrectos como '###' reemplazados (si existían).")

    # Corregir la inconsistencia de ID_cliente 13 (Ana María)
    df_limpio.loc[df_limpio['ID_cliente'] == 13, 'ID_cliente'] = 2
    print("\nCorregido 'ID_cliente' 13 a '2' (Ana María) para unificar.")

    # Verificamos los nombres únicos y sus IDs después de la corrección
    print("\nRecuento de clientes por ID después de la corrección de ID 13:")
    print(df_limpio['ID_cliente'].value_counts().sort_index())
    print("\nNombres únicos y sus IDs correspondientes después de la corrección:")
    print(df_limpio[['ID_cliente', 'Nombre']].drop_duplicates().sort_values(by='ID_cliente'))


    ### 2.3 Manejar outliers en 'Gasto_promedio':
    # Recalculamos los límites IQR ya que los NaNs ya fueron rellenados
    Q1_gasto = df_limpio['Gasto_promedio'].quantile(0.25)
    Q3_gasto = df_limpio['Gasto_promedio'].quantile(0.75)
    IQR_gasto = Q3_gasto - Q1_gasto

    limite_inferior_gasto = Q1_gasto - 1.5 * IQR_gasto
    limite_superior_gasto = Q3_gasto + 1.5 * IQR_gasto

    print(f"\nNuevos límites para Gasto_promedio (IQR) después de rellenar NaNs:")
    print(f"  Límite inferior: {limite_inferior_gasto:.2f}")
    print(f"  Límite superior: {limite_superior_gasto:.2f}")

    # Identificar los outliers inferiores
    outliers_bajos = df_limpio[df_limpio['Gasto_promedio'] < limite_inferior_gasto]
    print(f"\nOutliers bajos en 'Gasto_promedio' ({len(outliers_bajos)} encontrados) antes del ajuste:")
    print(outliers_bajos[['ID_cliente', 'Gasto_promedio']])

    # Estrategia de manejo: Reemplazar los outliers bajos por el límite inferior del IQR.
    df_limpio.loc[df_limpio['Gasto_promedio'] < limite_inferior_gasto, 'Gasto_promedio'] = limite_inferior_gasto
    print(f"\nOutliers bajos en 'Gasto_promedio' ajustados al límite inferior ({limite_inferior_gasto:.2f}).")

    # Identificar los outliers superiores
    outliers_altos = df_limpio[df_limpio['Gasto_promedio'] > limite_superior_gasto]
    print(f"\nOutliers altos en 'Gasto_promedio' ({len(outliers_altos)} encontrados) antes del ajuste:")
    print(outliers_altos[['ID_cliente', 'Gasto_promedio']])

    # Estrategia de manejo: Reemplazar los outliers altos por el límite superior del IQR.
    df_limpio.loc[df_limpio['Gasto_promedio'] > limite_superior_gasto, 'Gasto_promedio'] = limite_superior_gasto
    print(f"\nOutliers altos en 'Gasto_promedio' ajustados al límite superior ({limite_superior_gasto:.2f}).")

    print("\n--- Proceso de Limpieza de Datos Completado ---")
    print("\nDataFrame después de la limpieza (primeras 10 filas):")
    print(df_limpio.head(10))
    print("\nVerificación final de valores faltantes en df_limpio:")
    print(df_limpio.isnull().sum())
    print("\nVerificación de tipos de datos finales en df_limpio:")
    df_limpio.info()

    # --- Organización de la Tabla (Paso 3) ---
    print("\n--- Iniciando Proceso de Organización de la Tabla ---")

    # 3.1 Crear una columna temporal 'Conteo_Viaje' con el valor 1 para cada registro
    df_limpio['Conteo_Viaje'] = 1
    print("\nColumna 'Conteo_Viaje' añadida con valor 1.")

    # 3.2 Agrupar por ID_cliente para obtener el Número_de_viajes y sumar el Gasto_promedio para el Gasto_total
    df_clientes_agrupado = df_limpio.groupby('ID_cliente').agg(
        Nombre=('Nombre', 'first'),
        Edad=('Edad', 'first'),
        Destino_favorito=('Destino_favorito', lambda x: x.mode()[0] if not x.mode().empty else 'Desconocido'),
        Numero_de_viajes=('Conteo_Viaje', 'sum'),
        Gasto_total_por_cliente=('Gasto_promedio', 'sum')
    ).reset_index()

    # 3.3 Calcular el Gasto_promedio_por_cliente = Gasto_total_por_cliente / Numero_de_viajes
    df_clientes_agrupado['Gasto_promedio_por_cliente'] = df_clientes_agrupado['Gasto_total_por_cliente'] / df_clientes_agrupado['Numero_de_viajes']
    print("\nColumna 'Gasto_promedio_por_cliente' calculada.")

    # 3.4 Ordenar los datos por el número de viajes (de mayor a menor)
    df_clientes_agrupado = df_clientes_agrupado.sort_values(by='Numero_de_viajes', ascending=False)
    print("\nDataFrame agrupado y ordenado por 'Numero_de_viajes' (descendente):")

    # Mostrar el nuevo DataFrame agrupado
    print(df_clientes_agrupado.head(15))
    print("\nInformación del DataFrame agrupado:")
    df_clientes_agrupado.info()
    print("\nEstadísticas descriptivas del DataFrame agrupado:")
    print(df_clientes_agrupado.describe(include='all'))

    print("\n--- Proceso de Organización de la Tabla Completado ---")

    return df_clientes_agrupado

if __name__ == "__main__":
    # Define la ruta completa a tu archivo de Excel
    ruta_del_excel_de_clientes = 'D:/Curso de Bigdata/Datos/Tabla.xlsx'

    df_final_limpio_y_organizado = run_data_cleansing(ruta_del_excel_de_clientes)

    if df_final_limpio_y_organizado is not None:
        print("\nEl DataFrame final limpio y organizado está disponible en la variable 'df_final_limpio_y_organizado'.")

