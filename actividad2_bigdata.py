import pandas as pd
import numpy as np 

# Ruta completa a los Datos de la Actividad
ruta_archivo_excel = 'D:/Curso de Bigdata/Datos/Tabla.xlsx'

try:
    # Cargar los datos desde el archivo de Excel
    df_clientes = pd.read_excel(ruta_archivo_excel)

    print("¡DataFrame cargado exitosamente desde Excel!")
    # Mostrar las primeras filas del DataFrame para verificar
    print("\nPrimeras 5 filas del DataFrame:")
    print(df_clientes.head())

    # Mostrar información general del DataFrame (tipos de datos, valores no nulos)
    print("\nInformación del DataFrame:")
    df_clientes.info()

    # Mostrar estadísticas descriptivas de las columnas numéricas
    print("\nEstadísticas descriptivas:")
    print(df_clientes.describe(include='all')) 

except FileNotFoundError:
    print(f"Error: El archivo no fue encontrado en la ruta '{ruta_archivo_excel}'.")
    print("Por favor, verifica que la ruta y el nombre del archivo sean correctos.")
except ImportError:
    print("Error: La librería 'openpyxl' no está instalada.")
    print("Por favor, instálala ejecutando 'pip install openpyxl' en tu terminal.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo de Excel: {e}")

# Hacemos una copia del DataFrame para no modificar el original directamente si queremos volver atrás
df_limpio = df_clientes.copy()

print("--- Iniciando Proceso de Limpieza de Datos ---")

### 2.1 Completar los valores faltantes:

# 2.1.1 Completar valores faltantes en 'Edad' con la mediana
mediana_edad = df_limpio['Edad'].median()
df_limpio['Edad'].fillna(mediana_edad, inplace=True)
print(f"\nValores faltantes en 'Edad' rellenados con la mediana ({mediana_edad}).")

# 2.1.2 Completar valores faltantes en 'Destino_favorito' con "Desconocido"
df_limpio['Destino_favorito'].fillna("Desconocido", inplace=True)
print(f"Valores faltantes en 'Destino_favorito' rellenados con 'Desconocido'.")

# 2.1.3 Completar valores faltantes en 'Gasto_promedio' con la media
media_gasto = df_limpio['Gasto_promedio'].mean()
df_limpio['Gasto_promedio'].fillna(media_gasto, inplace=True)
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
print("\nEdades fuera de rango (18-90) corregidas.")

# 2.2.2 Corregir nombres incorrectos por "Desconocido"
df_limpio['Nombre'] = df_limpio['Nombre'].replace('###', 'Desconocido')
print("\nNombres incorrectos como '###' reemplazados.")

# Corregir la inconsistencia de ID_cliente 13 (Ana María)
# Asumimos que ID_cliente 13 es un error y debería ser ID_cliente 2 (Ana María)
# Esto implica que sus datos se asociarán al ID 2.
df_limpio.loc[df_limpio['ID_cliente'] == 13, 'ID_cliente'] = 2
print("\nCorregido 'ID_cliente' 13 a '2' (Ana María) para unificar.")

# Verificamos los nombres únicos y sus IDs después de la corrección
print("\nRecuento de clientes por ID después de la corrección de ID 13:")
print(df_limpio['ID_cliente'].value_counts().sort_index())
print("\nNombres únicos y sus IDs correspondientes después de la corrección:")
print(df_limpio[['ID_cliente', 'Nombre']].drop_duplicates().sort_values(by='ID_cliente'))


### 2.3 Manejar outliers en 'Gasto_promedio':
# Recalculamos los límites IQR por si el rellenado de NaNs afectó ligeramente
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
# Esto los "capa" al valor mínimo aceptable según el método IQR.
df_limpio.loc[df_limpio['Gasto_promedio'] < limite_inferior_gasto, 'Gasto_promedio'] = limite_inferior_gasto
print(f"\nOutliers bajos en 'Gasto_promedio' ajustados al límite inferior ({limite_inferior_gasto:.2f}).")

print("\n--- Proceso de Limpieza de Datos Completado ---")
print("\nDataFrame después de la limpieza:")
print(df_limpio.head(10)) # Muestra más filas para ver los cambios
print("\nVerificación final de valores faltantes:")
print(df_limpio.isnull().sum())
print("\nVerificación de tipos de datos finales:")
df_limpio.info()

print("\n--- Iniciando Proceso de Organización de la Tabla ---")

# 3.1 Crear una columna temporal 'Conteo_Viaje' con el valor 1 para cada registro
df_limpio['Conteo_Viaje'] = 1
print("\nColumna 'Conteo_Viaje' añadida con valor 1.")

# 3.2 Agrupar por ID_cliente para obtener el Número_de_viajes y sumar el Gasto_promedio para el Gasto_total
df_clientes_agrupado = df_limpio.groupby('ID_cliente').agg(
    Nombre=('Nombre', 'first'),  # Tomar el primer nombre 
    Edad=('Edad', 'first'),      # Tomar la primera edad 
    # Destino más frecuente para el cliente.
    Destino_favorito=('Destino_favorito', lambda x: x.mode()[0] if not x.mode().empty else 'Desconocido'),
    Numero_de_viajes=('Conteo_Viaje', 'sum'), 
    Gasto_total_por_cliente=('Gasto_promedio', 'sum') 
).reset_index() # Resetear el índice para que ID_cliente vuelva a ser una columna

# 3.3 *** NUEVO CÁLCULO: Gasto promedio por cliente ***
# Calcular el Gasto_promedio_por_cliente = Gasto_total_por_cliente / Numero_de_viajes
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
