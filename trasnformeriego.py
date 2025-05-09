import pandas as pd

import pandas as pd
import numpy as np
import random

# Nombre del archivo original
archivo_original = 'data_seleccionada.csv'
# Nombre del archivo aumentado
archivo_mas_aumentada = 'data_mas_aumentada.csv'

# Parámetros de transformación (rangos aleatorios)
factor_ingresos = random.uniform(0.70, 0.85)  # Disminuir ingresos entre 15% y 30%
aumento_endeudamiento = random.uniform(7, 15)  # Aumentar endeudamiento entre 7 y 15 puntos
reduccion_edad = random.randint(2, 7)         # Disminuir edad entre 2 y 7 años

# Porcentaje de registros a transformar (20%)
porcentaje_a_transformar = 0.20

# Fase 1: Leer el archivo original
try:
    data = pd.read_csv(archivo_original)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_original}'.")
    exit()

# Fase 2: Identificar registros de "Bajo" riesgo
bajo_riesgo_data = data[data['Calificación de Riesgo'] == 'Bajo'].copy()
num_bajo_riesgo = len(bajo_riesgo_data)
num_total_registros = len(data)
num_a_transformar = int(num_total_registros * porcentaje_a_transformar)

# Asegurarse de no transformar más registros de los que existen en la clase "Bajo" riesgo
num_a_transformar = min(num_a_transformar, num_bajo_riesgo)

registros_transformados_lista = []

if num_a_transformar > 0:
    # Fase 3: Seleccionar y transformar hasta num_a_transformar registros
    registros_a_transformar = bajo_riesgo_data.sample(n=num_a_transformar, random_state=42).copy()

    for index, row in registros_a_transformar.iterrows():
        registro_transformado = row.copy() # Crear una copia para no modificar el original directamente
        # Disminuir ingresos
        if pd.api.types.is_numeric_dtype(registro_transformado['Ingresos mensuales']):
            registro_transformado['Ingresos mensuales'] = registro_transformado['Ingresos mensuales'] * factor_ingresos
        # Aumentar porcentaje de endeudamiento
        if pd.api.types.is_numeric_dtype(registro_transformado['Porcentaje de endeudamiento']):
            registro_transformado['Porcentaje de endeudamiento'] = registro_transformado['Porcentaje de endeudamiento'] + aumento_endeudamiento
        # Disminuir edad
        if pd.api.types.is_numeric_dtype(registro_transformado['Edad']):
            registro_transformado['Edad'] = max(18, int(registro_transformado['Edad']) - reduccion_edad) # Asegurar edad mínima de 18
        # Cambiar la etiqueta a "Alto" riesgo
        registro_transformado['Calificación de Riesgo'] = 'Alto'
        registros_transformados_lista.append(registro_transformado)

    # Fase 4: Convertir la lista de diccionarios a un DataFrame
    nuevos_registros_alto_riesgo_df = pd.DataFrame(registros_transformados_lista)

    # Fase 5: Concatenar los nuevos registros de "Alto" riesgo con el DataFrame original
    data_mas_aumentada = pd.concat([data, nuevos_registros_alto_riesgo_df], ignore_index=True)

    # Fase 6: Guardar el DataFrame aún más aumentado en un nuevo archivo
    data_mas_aumentada.to_csv(archivo_mas_aumentada, index=False)
    print(f"Se han seleccionado y transformado hasta el {porcentaje_a_transformar*100:.0f}% ({num_a_transformar} registros) de 'Bajo' riesgo a 'Alto' riesgo y se han añadido al conjunto de datos en '{archivo_mas_aumentada}'.")
else:
    print(f"No hay suficientes registros de 'Bajo' riesgo en '{archivo_original}' para realizar la transformación.")
    # En caso de no haber suficientes, guardamos el archivo original con otro nombre para seguir el flujo
    data.to_csv(archivo_mas_aumentada, index=False)
    print(f"Se ha guardado una copia del archivo '{archivo_original}' en '{archivo_mas_aumentada}' sin modificaciones.")

print(f"Por favor, utiliza el archivo '{archivo_mas_aumentada}' para continuar con el resto de tu código.")

archivo_aumentada = 'data_aumentada.csv'
archivo_mas_aumentada = 'data_mas_aumentada.csv'

try:
    data_original = pd.read_csv(archivo_aumentada)
    num_filas_original = len(data_original)
    print(f"Número de filas en '{archivo_aumentada}': {num_filas_original}")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_aumentada}'.")
    exit()

try:
    data_aumentada = pd.read_csv(archivo_mas_aumentada)
    num_filas_aumentada = len(data_aumentada)
    print(f"Número de filas en '{archivo_mas_aumentada}': {num_filas_aumentada}")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_mas_aumentada}'.")
    exit()