import pandas as pd

# --- CONFIGURACIÓN ---
ruta_archivo_entrada = 'financial_risk_assessment.csv'  # Reemplaza con el nombre de tu archivo
delimitador = ','  # Reemplaza con el delimitador correcto

# --- CARGAR LA DATA ---
try:
    # Intentaremos leer la data con el delimitador especificado
    df = pd.read_csv(ruta_archivo_entrada, sep=delimitador, skipinitialspace=True, engine='python')
    print("¡Data cargada exitosamente!")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{ruta_archivo_entrada}'. Asegúrate de que la ruta sea correcta.")
    exit()
except Exception as e:
    print(f"Ocurrió un error al cargar la data: {e}")
    exit()

# --- EXPLORACIÓN INICIAL ---
print("\nPrimeras filas de la data:")
print(df.head())

print("\nInformación general de las columnas:")
df.info()

# --- SELECCIÓN DE COLUMNAS (POR AHORA MANUAL, LUEGO INTERACTIVA) ---
# Aquí listaremos las columnas que nos parezcan interesantes a primera vista.
# ¡Tú también puedes añadir o quitar columnas de esta lista!
columnas_interes = [
    'Age', 'Gender', 'Education Level', 'Marital Status', 'Income',
    'Credit Score', 'Loan Amount', 'Number of Dependents',
    'Previous Defaults', 'Country', 'Risk Rating', 'Employment Status'
]
# Creamos un nuevo DataFrame solo con las columnas de interés
df_seleccionado = df[columnas_interes].copy()
print("\nDataFrame con las columnas seleccionadas:")
print(df_seleccionado.head())

# --- CREACIÓN DE LA COLUMNA 'Edad' ---
df_seleccionado['Edad'] = df_seleccionado['Age'].copy()
print("\nDataFrame con la nueva columna 'Edad':")
print(df_seleccionado.head())

# --- ANALISIS DE LA COLUMNA 'Edad' ---
print("\nAnálisis de la columna 'Edad':")
print(df_seleccionado['Edad'].describe())

# --- ANALISIS DE LA COLUMNA 'Income' ---
print("\nAnálisis de la columna 'Income':")
print("\nPrimeras filas de 'Income':")
print(df_seleccionado['Income'].head())

print("\nEstadísticas descriptivas de 'Income':")
print(df_seleccionado['Income'].describe())

print("\nCantidad de valores nulos en 'Income':")
print(df_seleccionado['Income'].isnull().sum())

# --- ANÁLISIS Y TRANSFORMACIÓN DE 'Income' A 'Ingresos mensuales' ---
print("\nAnálisis y transformación de 'Income' a 'Ingresos mensuales':")

# Imputar valores nulos con la mediana
mediana_ingresos = df_seleccionado['Income'].median()
df_seleccionado['Income_imputado'] = df_seleccionado['Income'].fillna(mediana_ingresos)
print(f"\nMediana de ingresos utilizada para la imputación: {mediana_ingresos:.2f}")
print("\nPrimeras filas de 'Income' e 'Income_imputado':")
print(df_seleccionado[['Income', 'Income_imputado']].head())
print(f"\nCantidad de valores nulos en 'Income_imputado': {df_seleccionado['Income_imputado'].isnull().sum()}")

# Crear la columna 'Ingresos mensuales'
df_seleccionado['Ingresos mensuales'] = df_seleccionado['Income_imputado'] / 12
print("\nPrimeras filas de 'Ingresos mensuales':")
print(df_seleccionado['Ingresos mensuales'].head())

# --- ANÁLISIS Y TRANSFORMACIÓN DE 'Number of Dependents' A 'Dependientes' ---
print("\nAnálisis y transformación de 'Number of Dependents' a 'Dependientes':")

# Crear la columna 'Dependientes'
df_seleccionado['Dependientes'] = df_seleccionado['Number of Dependents'].copy()
print("\nPrimeras filas con 'Dependientes':")
print(df_seleccionado[['Number of Dependents', 'Dependientes']].head())

# Verificar valores nulos en 'Dependientes'
cantidad_nulos_dependientes = df_seleccionado['Dependientes'].isnull().sum()
print(f"\nCantidad de valores nulos en 'Dependientes': {cantidad_nulos_dependientes}")

# Imputar valores nulos con 0
df_seleccionado['Dependientes'] = df_seleccionado['Dependientes'].fillna(0)
print(f"\nCantidad de valores nulos en 'Dependientes' después de la imputación: {df_seleccionado['Dependientes'].isnull().sum()}")

# Análisis de la columna 'Dependientes'
print("\nAnálisis de la columna 'Dependientes':")
print(df_seleccionado['Dependientes'].describe())

# --- CREACIÓN DE 'Porcentaje de endeudamiento' ---
print("\nCreación de 'Porcentaje de endeudamiento':")
# Dividimos el monto del préstamo por los ingresos anuales imputados
df_seleccionado['Porcentaje de endeudamiento'] = df_seleccionado['Loan Amount'] / df_seleccionado['Income_imputado']
print("\nPrimeras filas con 'Porcentaje de endeudamiento':")
print(df_seleccionado[['Loan Amount', 'Income_imputado', 'Porcentaje de endeudamiento']].head())

# Análisis de la columna 'Porcentaje de endeudamiento'
print("\nAnálisis de la columna 'Porcentaje de endeudamiento':")
print(df_seleccionado['Porcentaje de endeudamiento'].describe())

# --- ANÁLISIS DE 'Employment Status' ---
print("\nAnálisis de 'Employment Status':")
print("\nValores únicos en 'Employment Status':")
print(df_seleccionado['Employment Status'].unique())

print("\nConteo de valores por categoría en 'Employment Status':")
print(df_seleccionado['Employment Status'].value_counts())

# --- ANÁLISIS Y TRANSFORMACIÓN DE 'Employment Status' A 'Situación Laboral' ---
print("\nAnálisis y transformación de 'Employment Status' a 'Situación Laboral':")
print("\nValores únicos en 'Employment Status' antes de la transformación:")
print(df_seleccionado['Employment Status'].unique())
print("\nConteo de valores por categoría en 'Employment Status' antes de la transformación:")
print(df_seleccionado['Employment Status'].value_counts())

# Renombrar la columna
df_seleccionado = df_seleccionado.rename(columns={'Employment Status': 'Situación Laboral'})

# Mapear las categorías
mapeo_situacion_laboral = {
    'Employed': 'Empleado',
    'Unemployed': 'Desempleado',
    'Self-employed': 'Autónomo'
}
df_seleccionado['Situación Laboral'] = df_seleccionado['Situación Laboral'].map(mapeo_situacion_laboral)

print("\nValores únicos en 'Situación Laboral' después de la transformación:")
print(df_seleccionado['Situación Laboral'].unique())
print("\nConteo de valores por categoría en 'Situación Laboral' después de la transformación:")
print(df_seleccionado['Situación Laboral'].value_counts())
print("\nPrimeras filas con la columna 'Situación Laboral':")
print(df_seleccionado.head())

# --- ANÁLISIS DE 'Education Level' ---
print("\nAnálisis de 'Education Level':")
print("\nValores únicos en 'Education Level':")
print(df_seleccionado['Education Level'].unique())
print("\nConteo de valores por categoría en 'Education Level':")
print(df_seleccionado['Education Level'].value_counts())

# --- ANÁLISIS Y TRANSFORMACIÓN DE 'Education Level' A 'Nivel Educativo' ---
print("\nAnálisis y transformación de 'Education Level' a 'Nivel Educativo':")
print("\nValores únicos en 'Education Level' antes de la transformación:")
print(df_seleccionado['Education Level'].unique())
print("\nConteo de valores por categoría en 'Education Level' antes de la transformación:")
print(df_seleccionado['Education Level'].value_counts())

# Renombrar la columna
df_seleccionado = df_seleccionado.rename(columns={'Education Level': 'Nivel Educativo'})

# Mapear las categorías
mapeo_nivel_educativo = {
    'High School': 'Secundario',
    'Bachelor\'s': 'Universitario',
    'Master\'s': 'Universitario',
    'PhD': 'Universitario'
}
df_seleccionado['Nivel Educativo'] = df_seleccionado['Nivel Educativo'].map(mapeo_nivel_educativo)

print("\nValores únicos en 'Nivel Educativo' después de la transformación:")
print(df_seleccionado['Nivel Educativo'].unique())
print("\nConteo de valores por categoría en 'Nivel Educativo' después de la transformación:")
print(df_seleccionado['Nivel Educativo'].value_counts())
print("\nPrimeras filas con la columna 'Nivel Educativo':")
print(df_seleccionado.head())

# --- ANÁLISIS Y TRANSFORMACIÓN DE 'Marital Status' A 'Estado Civil' ---
print("\nAnálisis y transformación de 'Marital Status' a 'Estado Civil':")
print("\nValores únicos en 'Marital Status' antes de la transformación:")
print(df_seleccionado['Marital Status'].unique())
print("\nConteo de valores por categoría en 'Marital Status' antes de la transformación:")
print(df_seleccionado['Marital Status'].value_counts())

# Renombrar la columna
df_seleccionado = df_seleccionado.rename(columns={'Marital Status': 'Estado Civil'})

# Mapear las categorías
mapeo_estado_civil = {
    'Divorced': 'Divorciado',
    'Widowed': 'Viudo',
    'Single': 'Soltero',
    'Married': 'Casado'
}
df_seleccionado['Estado Civil'] = df_seleccionado['Estado Civil'].map(mapeo_estado_civil)

print("\nValores únicos en 'Estado Civil' después de la transformación:")
print(df_seleccionado['Estado Civil'].unique())
print("\nConteo de valores por categoría en 'Estado Civil' después de la transformación:")
print(df_seleccionado['Estado Civil'].value_counts())
print("\nPrimeras filas con la columna 'Estado Civil':")
print(df_seleccionado.head())


# --- ANÁLISIS DE 'Credit Score' ---
print("\nAnálisis de 'Credit Score':")
print("\nPrimeras filas de 'Credit Score':")
print(df_seleccionado['Credit Score'].head())
print("\nEstadísticas descriptivas de 'Credit Score':")
print(df_seleccionado['Credit Score'].describe())
print(f"\nCantidad de valores nulos en 'Credit Score': {df_seleccionado['Credit Score'].isnull().sum()}")


# --- ANÁLISIS DE 'Previous Defaults' ---
print("\nAnálisis de 'Previous Defaults':")
print("\nValores únicos en 'Previous Defaults':")
print(df_seleccionado['Previous Defaults'].unique())
print("\nConteo de valores por categoría en 'Previous Defaults':")
print(df_seleccionado['Previous Defaults'].value_counts())
print(f"\nCantidad de valores nulos en 'Previous Defaults': {df_seleccionado['Previous Defaults'].isnull().sum()}")



# --- ANÁLISIS Y TRANSFORMACIÓN DE 'Credit Score' ---
print("\nAnálisis y transformación de 'Credit Score':")
mediana_credit_score = df_seleccionado['Credit Score'].median()
df_seleccionado['Puntaje de Crédito'] = df_seleccionado['Credit Score'].fillna(mediana_credit_score)
print("\nValores nulos en 'Puntaje de Crédito' imputados con la mediana.")

# --- ANÁLISIS Y TRANSFORMACIÓN DE 'Previous Defaults' ---
print("\nAnálisis y transformación de 'Previous Defaults' a 'Incumplimientos Previos':")
moda_previous_defaults = df_seleccionado['Previous Defaults'].mode()[0]
df_seleccionado['Incumplimientos Previos'] = df_seleccionado['Previous Defaults'].fillna(moda_previous_defaults)
print(f"\nValores nulos en 'Incumplimientos Previos' imputados con la moda: {moda_previous_defaults}")

# --- ANÁLISIS Y TRANSFORMACIÓN DE 'Risk Rating' A 'Calificación de Riesgo' (en español) ---
print("\nAnálisis y transformación de 'Risk Rating' a 'Calificación de Riesgo':")
print("\nValores únicos en 'Risk Rating' antes de la transformación:")
print(df_seleccionado['Risk Rating'].unique())
print("\nConteo de valores por categoría en 'Risk Rating' antes de la transformación:")
print(df_seleccionado['Risk Rating'].value_counts())

# Renombrar la columna
df_seleccionado = df_seleccionado.rename(columns={'Risk Rating': 'Calificación de Riesgo'})

# Mapear las categorías a español
mapeo_riesgo = {
    'Low': 'Bajo',
    'Medium': 'Medio',
    'High': 'Alto'
}
df_seleccionado['Calificación de Riesgo'] = df_seleccionado['Calificación de Riesgo'].map(mapeo_riesgo)

print("\nValores únicos en 'Calificación de Riesgo' después de la transformación:")
print(df_seleccionado['Calificación de Riesgo'].unique())
print("\nConteo de valores por categoría en 'Calificación de Riesgo' después de la transformación:")
print(df_seleccionado['Calificación de Riesgo'].value_counts())
print("\nPrimeras filas con la columna 'Calificación de Riesgo':")
print(df_seleccionado[['Calificación de Riesgo']].head())


print("\nColumnas en el DataFrame final antes de eliminar:")
print(df_seleccionado.columns)


# --- ANÁLISIS DE 'Loan Amount' ---
print("\nAnálisis de 'Loan Amount':")
print("\nPrimeras filas de 'Loan Amount':")
print(df_seleccionado['Loan Amount'].head())
print("\nEstadísticas descriptivas de 'Loan Amount':")
print(df_seleccionado['Loan Amount'].describe())
print(f"\nCantidad de valores nulos en 'Loan Amount': {df_seleccionado['Loan Amount'].isnull().sum()}")

# --- ANÁLISIS Y TRANSFORMACIÓN DE 'Loan Amount' A 'Monto del Préstamo' ---
print("\nAnálisis y transformación de 'Loan Amount' a 'Monto del Préstamo':")
mediana_loan_amount = df_seleccionado['Loan Amount'].median()
df_seleccionado['Monto del Préstamo'] = df_seleccionado['Loan Amount'].fillna(mediana_loan_amount)
print(f"\nValores nulos en 'Monto del Préstamo' imputados con la mediana: {mediana_loan_amount}")


#--- RENOMBRAR 'Country' A 'Provincias' ---
#  df_seleccionado = df_seleccionado.rename(columns={'Country': 'Provincias'})
# print("'Country' renombrado a 'Provincias'.")

# --- MOSTRAR INFORMACIÓN DE 'Provincias' ---
# print("\n--- INFORMACIÓN DE 'Provincias' ---")
#print("\nValores únicos en 'Provincias':")
#print(df_seleccionado['Provincias'].unique())
#print("\nConteo de valores por categoría en 'Provincias':")
#print(df_seleccionado['Provincias'].value_counts())



# --- IMPRIMIR LAS COLUMNAS RESTANTES ---
print("\nColumnas restantes en el DataFrame:")
print(df_seleccionado.columns)

# --- ELIMINAR COLUMNAS ORIGINALES Y AUXILIARES ---
columnas_a_eliminar = ['Age', 'Gender', 'Income', 'Number of Dependents', 'Credit Score', 'Previous Defaults', 'Employment Status', 'Education Level', 'Marital Status', 'Loan Amount', 'Income_imputado']
df_seleccionado = df_seleccionado.drop(columns=columnas_a_eliminar, errors='ignore')
print(f"\nColumnas originales y auxiliares eliminadas: {columnas_a_eliminar}")

# --- IMPRIMIR LAS COLUMNAS RESTANTES ---
print("\nColumnas restantes en el DataFrame preparado:")
print(df_seleccionado.columns)

# --- RENOMBRAR 'Country' A 'Provincias' ---
df_seleccionado = df_seleccionado.rename(columns={'Country': 'Provincias'})
print("'Country' renombrado a 'Provincias'.")

# --- OBTENER TODAS LAS PROVINCIAS ÚNICAS DEL DATASET ---
provincias_dataset = df_seleccionado['Provincias'].unique().tolist()
print("\nTodas las provincias únicas en el dataset:")
print(provincias_dataset)

# --- LISTA DE TODAS LAS PROVINCIAS DE ESPAÑA POR POBLACIÓN ---
# --- REEMPLAZAR TODAS LAS 'Provincias' CON PROVINCIAS DE ESPAÑA ---
import random
provincias_espanolas = [
    'Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Alicante',
    'Málaga', 'Murcia', 'Cádiz', 'Vizcaya', 'A Coruña',
    'Zaragoza', 'Pontevedra', 'Granada', 'Tarragona', 'Córdoba',
    'Girona', 'Almería', 'Toledo', 'Badajoz', 'Navarra',
    'Jaén', 'Castellón', 'Huelva', 'Valladolid', 'Islas Baleares',
    'Las Palmas', 'Santa Cruz de Tenerife', 'Álava', 'León', 'Ciudad Real',
    'Lugo', 'Cáceres', 'Ourense', 'Guadalajara', 'Burgos', 'Salamanca',
    'Asturias', 'Cantabria', 'La Rioja', 'Albacete', 'Huesca', 'Segovia',
    'Ávila', 'Teruel', 'Soria', 'Palencia', 'Zamora', 'Melilla', 'Ceuta'
]

num_filas = len(df_seleccionado)
provincias_asignadas = []

if num_filas <= len(provincias_espanolas):
    provincias_asignadas = provincias_espanolas[:num_filas]
else:
    provincias_asignadas = provincias_espanolas * (num_filas // len(provincias_espanolas))
    provincias_restantes = num_filas % len(provincias_espanolas)
    provincias_asignadas.extend(provincias_espanolas[:provincias_restantes])
    # Si aún faltan, seleccionar aleatoriamente de la lista de España
    if len(provincias_asignadas) < num_filas:
        faltantes = num_filas - len(provincias_asignadas)
        provincias_aleatorias = random.choices(provincias_espanolas, k=faltantes)
        provincias_asignadas.extend(provincias_aleatorias)

df_seleccionado['Provincias'] = provincias_asignadas

print("\nColumna 'Provincias' reemplazada con provincias de España.")

# --- MOSTRAR EL CONTEO DE LAS 'Provincias' DESPUÉS DEL REEMPLAZO ---
print("\nConteo de valores por categoría en 'Provincias' después del reemplazo:")
print(df_seleccionado['Provincias'].value_counts())
# --- MOSTRAR EL CONTEO DE LAS 'Provincias' DESPUÉS DEL MAPPING ---
print("\nConteo de valores por categoría en 'Provincias' después del mapping (top 25):")
print(df_seleccionado['Provincias'].value_counts().nlargest(25))


# --- LISTA DE TODAS LAS PROVINCIAS DE ESPAÑA (PARA VERIFICACIÓN) ---
provincias_validas_espanolas = [
    'Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Alicante',
    'Málaga', 'Murcia', 'Cádiz', 'Vizcaya', 'A Coruña',
    'Zaragoza', 'Pontevedra', 'Granada', 'Tarragona', 'Córdoba',
    'Girona', 'Almería', 'Toledo', 'Badajoz', 'Navarra',
    'Jaén', 'Castellón', 'Huelva', 'Valladolid', 'Islas Baleares',
    'Las Palmas', 'Santa Cruz de Tenerife', 'Álava', 'León', 'Ciudad Real',
    'Lugo', 'Cáceres', 'Ourense', 'Guadalajara', 'Burgos', 'Salamanca',
    'Asturias', 'Cantabria', 'La Rioja', 'Albacete', 'Huesca', 'Segovia',
    'Ávila', 'Teruel', 'Soria', 'Palencia', 'Zamora', 'Melilla', 'Ceuta'
]

# --- OBTENER LAS PROVINCIAS ÚNICAS EN LA COLUMNA 'Provincias' DESPUÉS DE LA TRANSFORMACIÓN ---
provincias_en_df = df_seleccionado['Provincias'].unique().tolist()
print("\nProvincias únicas encontradas en el DataFrame después de la transformación:")
print(provincias_en_df)

# --- IDENTIFICAR PROVINCIAS QUE NO ESTÁN EN LA LISTA DE PROVINCIAS VÁLIDAS DE ESPAÑA ---
provincias_fuera_de_lista = [provincia for provincia in provincias_en_df if provincia not in provincias_validas_espanolas]

if provincias_fuera_de_lista:
    print("\n¡ATENCIÓN! Se encontraron las siguientes provincias que NO están en la lista de provincias válidas de España:")
    print(provincias_fuera_de_lista)
else:
    print("\n¡VERIFICACIÓN EXITOSA! Todas las provincias en el DataFrame son válidas de la lista de provincias de España.")


# --- ELIMINAR COLUMNAS ORIGINALES Y AUXILIARES ---
columnas_a_eliminar = ['Age', 'Gender', 'Income', 'Number of Dependents', 'Credit Score', 'Previous Defaults', 'Employment Status', 'Education Level', 'Marital Status', 'Loan Amount', 'Income_imputado']
df_seleccionado = df_seleccionado.drop(columns=columnas_a_eliminar, errors='ignore')
print(f"\nColumnas originales y auxiliares eliminadas: {columnas_a_eliminar}")

# --- IMPRIMIR LAS COLUMNAS RESTANTES ---
print("\nColumnas restantes en el DataFrame preparado:")
print(df_seleccionado.columns)

# --- DEFINIR EL ORDEN DESEADO DE LAS COLUMNAS PARA EL CSV ---
orden_columnas_deseado = [
    'Edad',
    'Ingresos mensuales',
    'Dependientes',
    'Porcentaje de endeudamiento',
    'Situación Laboral',
    'Nivel Educativo',
    'Estado Civil',
    'Puntaje de Crédito',
    'Incumplimientos Previos',
    'Monto del Préstamo',
    'Provincias',
    'Calificación de Riesgo'
]

# --- SELECCIONAR LAS COLUMNAS EN EL ORDEN DESEADO ---
df_seleccionado = df_seleccionado[orden_columnas_deseado]
print("\nDataFrame con las columnas en el orden deseado para el CSV:")
print(df_seleccionado.head())

# --- GUARDAR A CSV ---
ruta_archivo_salida = 'data_seleccionada.csv'
df_seleccionado.to_csv(ruta_archivo_salida, index=False)
print(f"\n¡Data seleccionada y guardada en '{ruta_archivo_salida}'!")

print("\n¡Listo para la siguiente fase!")
