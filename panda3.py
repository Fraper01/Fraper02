
# Ejercicio 4
# Limpieza de datos
# 4.1 Eliminar filas duplicadas
print("Ejercicio 4.1 ELiminar filas duplicadas")

#Métodos para eliminar filas duplicadas:
#drop_duplicates(): Este método es el más utilizado para eliminar filas duplicadas.

import pandas as pd

# Crear un DataFrame de ejemplo con filas duplicadas
data = {'Columna1': [1, 2, 2, 4], 'Columna2': ['A', 'B', 'B', 'C']}
df = pd.DataFrame(data)
print(df)
# Eliminar filas duplicadas, manteniendo la primera ocurrencia
df_sin_duplicados = df.drop_duplicates()
print(df_sin_duplicados)

#Opciones adicionales de drop_duplicates():
# keep='first': (por defecto) Mantiene la primera ocurrencia de cada conjunto de filas duplicadas.
# keep='last': Mantiene la última ocurrencia.
# keep=False': Elimina todas las ocurrencias de filas duplicadas.
# subset=[cols]: Especifica las columnas que se utilizarán para identificar duplicados. 
# Si solo quieres considerar ciertas columnas para determinar si una fila es duplicada, 
# puedes usar este argumento.

# Ejemplo con subset:
print("Ejemplo con subset")
data = {'Columna1': [1, 2, 2, 4], 'Columna2': ['A', 'B', 'B', 'C']}
df = pd.DataFrame(data)
print(df)
# Eliminar duplicados solo considerando la columna 'Columna1'
df_sin_duplicados_col1 = df.drop_duplicates(subset=['Columna1'])
#¿Cuándo usar cada opción?
# keep='first': Útil cuando el orden de los datos es importante y quieres mantener la primera aparición.
# keep='last': Útil si te interesa la última ocurrencia de un valor.
# keep=False': Si quieres eliminar todas las ocurrencias de filas duplicadas, sin importar el orden.
# subset: Cuando solo te interesan duplicados en un subconjunto de columnas.
print(df_sin_duplicados_col1)

#Ejemplo más complejo:
# Crear un DataFrame con más columnas
data = {'Nombre': ['Ana', 'Juan', 'Ana', 'Pedro'], 
        'Edad': [25, 30, 25, 28],
        'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla']}
df = pd.DataFrame(data)
print(df)
# Eliminar duplicados considerando solo las columnas 'Nombre' y 'Edad'
df_sin_duplicados = df.drop_duplicates(subset=['Nombre', 'Edad'])
print(df_sin_duplicados)

# Ejercicio 4.2
# Eliminando Datos Faltantes en un DataFrame de Python
# Métodos para eliminar datos faltantes en Pandas:
# dropna(): Este método es el más común y directo para eliminar filas o columnas que contienen al menos un valor faltante.
print("Ejercicio 4.2 Eliminar Datos faltantes")
import pandas as pd

# Crear un DataFrame de ejemplo con valores faltantes
data = {'Columna1': [1, 2, None, 4], 'Columna2': ['A', None, 'C', 'D']}
df = pd.DataFrame(data)
print(df)

# Eliminar filas con al menos un valor faltante
df_sin_faltantes = df.dropna()

print(df_sin_faltantes)

#Opciones adicionales de dropna():
# axis=0: Elimina filas (por defecto).
# axis=1: Elimina columnas.
# how='any': Elimina filas o columnas si hay al menos un valor faltante (por defecto).
# how='all': Elimina filas o columnas solo si todos los valores son faltantes.
# thresh=n : Elimina filas o columnas que tengan menos de n valores no nulos.

# Eliminar filas que tengan al menos dos valores faltantes
df_sin_faltantes = df.dropna(thresh=2)

#¿Cuándo usar cada opción?
# how='any': Útil cuando la presencia de un solo valor faltante en una fila o columna 
#   es suficiente para considerarla como "faltante".
# how='all': Útil cuando quieres eliminar solo las filas o columnas que estén completamente vacías.
# thresh: Flexible para definir un umbral mínimo de valores no nulos.

# Alternativas a la eliminación:
# Imputación: Rellenar los valores faltantes con un valor estimado (media, mediana, moda, etc.).
# Modelado de valores faltantes: Utilizar técnicas de aprendizaje automático para predecir los valores faltantes.

# En resumen:
# La decisión de eliminar o imputar datos faltantes depende del contexto específico del problema y 
# de la cantidad y distribución de los valores faltantes. 
# Es importante evaluar cuidadosamente las implicaciones de cada enfoque antes de tomar una decisión.

# Identificación de valores faltantes: Utilizando isnull() y notnull().
# Imputación de valores faltantes: Con fillna(), interpolate(), o técnicas de aprendizaje automático.

# Ejercicio 4.3
# Modificar columnas
print("Ejercicio 4.3 Modificar Columnas")
#Métodos para Modificar Columnas
#1. Asignación directa:
print("Asignacion directa")
import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Columna1': [1, 2, 3], 'Columna2': [4, 5, 6]}
df = pd.DataFrame(data)
print(df)
# Modificar todos los valores de 'Columna1'
df['Columna1'] = df['Columna1'] * 2
print(df)

#2. Utilizando loc:
print("Utilizando loc")
print(df)
# Modificar un valor específico
df.loc[0, 'Columna2'] = 10
print(df)

#3. Aplicando funciones:
print("Aplicando funciones")
# Crear una nueva columna aplicando una función
def cuadrado(x):
    return x**2
print(df)
df['Columna1_cuadrado'] = df['Columna1'].apply(cuadrado)
print(df)

#4. Utilizando map:
# map es similar a apply, pero generalmente es más rápido para operaciones elemento a elemento.
# Mapear valores a una nueva columna
print("Utilizando map")
print(df)
df['Columna2'] = df['Columna2'].map({10: 'A', 5: 'B', 6: 'C'})
print(df)

# 5. Creando nuevas columnas basadas en cálculos:
# Crear una nueva columna sumando dos columnas
print("Creando nuevas columnas basadas en cálculos")
print(df)
#df['Suma'] = df['Columna1'] + df['Columna2']
print(df)

# 6. Renombrando columnas:
# Renombrar la columna 'Columna1'
print("Renombrando columnas")
print(df)
df = df.rename(columns={'Columna1': 'Columna1R'})
print(df)

# Ejemplos más Complejos
# Modificar valores condicionalmente:
# Cambiar los valores de 'Columna1' mayores a 2 por 0
print("Modificar valores condicionalmente")
print(df)
df.loc[df['Columna1R'] > 2, 'Columna1R'] = 0
print(df)

# Crear columnas categóricas:
# Crear una columna categórica basada en otra columna
print("Crear columnas categóricas")
print(df)
#df['Categoría'] = pd.cut(df['Columna1R'], bins=[0, 1, 2], labels=['Bajo', 'Medio', 'Alto'])
print(df)

#Consideraciones Importantes
# Modificación in-place: Al asignar directamente a una columna, se modifica el DataFrame original.
# Copias vs. vistas: Si quieres crear una copia del DataFrame antes de realizar modificaciones, utiliza copy().

# Crear una columna categórica basada en otra columna
#df['Categoría'] = pd.cut(df['Columna1R'], bins=[0, 2, 4], labels=['Bajo', 'Medio', 'Alto'])

# Ejercicio 4.3
# Renombrar columnas
# Métodos para cambiar los nombres de las columnas:
# Usando el método rename():

import pandas as pd
print("Ejercicio 4.3 Renombrar columnas")
# Crear un DataFrame de ejemplo
data = {'Columna1': [1, 2, 3], 'Columna2': [4, 5, 6]}
df = pd.DataFrame(data)
print(df)
# Renombrar las columnas
df = df.rename(columns={'Columna1': 'NuevaColumna1', 'Columna2': 'NuevaColumna2'})
print(df)

#Puedes usar un diccionario para especificar el mapeo de los nombres antiguos a los nuevos:
data = {'Columna1': [1, 2, 3], 'Columna2': [4, 5, 6]}
df = pd.DataFrame(data)
nuevo_nombre = {'Columna1': 'NuevaColumna1', 'Columna2': 'NuevaColumna2'}
print(df)
df = df.rename(columns=nuevo_nombre)
print(df)

# Asignado directamente a columns:
# Puedes asignar una nueva lista con los nombres de las columnas directamente a la propiedad columns del DataFrame.
print(df)
df.columns = ['ColumnaA', 'ColumnaB']
print(df)

#Ejemplo más completo:
import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Edad': [25, 30, 28], 'CIUdad': ['Madrid', 'Barcelona', 'Sevilla']}
df = pd.DataFrame(data)
print(df)
# Renombrar las columnas y convertirlas a minúsculas
df.columns = [col.lower() for col in df.columns]
print(df)
# Renombrar 'edad' a 'edad_años'
df = df.rename(columns={'edad': 'edad_años'})
print(df)

# Ejercicio 4.4
# Cambiando el tipo de dato de una columna 
print("Ejercicio 4.4")
# Pandas proporciona el método astype() para convertir el tipo de dato de una columna.

import pandas as pd

# Crear un DataFrame de ejemplo
data = {'edad': ['25', '30', '28'], 'ciudad': ['Madrid', 'Barcelona', 'Sevilla']}
df = pd.DataFrame(data)

print("Convertir Edad en int")
# Convertir la columna 'edad' a tipo entero
df['edad'] = df['edad'].astype(int)

print(df)

# Tipos de datos comunes en Pandas:
# int64: Enteros.
# float64: Números de punto flotante.
# bool: Valores booleanos (True/False).
# object: Tipo general que puede contener cualquier tipo de dato, incluyendo cadenas, números, etc.
# datetime64: Fechas y horas.
#category: Datos categóricos.

#Convertir a flotante:
print("Convertir Precio en float")

df['precio'] = df['edad'] + 10
df['precio'] = df['precio'].astype(float)
print(df)

#Convertir a cadena:
df['código'] = df['edad'].astype(str)

#Convertir a fecha:
#df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], format='%Y-%m-%d')

# Ejercicio 4.5
print("Ejercicio 4.5")
# Completando Datos Faltantes 
# Métodos para completar datos faltantes en Pandas:
# Pandas ofrece varias funciones para manejar datos faltantes, siendo fillna() la más común.
print("Rellenar con un valor específico")
import pandas as pd
import numpy as np

# Crear un DataFrame con valores faltantes
data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8]}
df = pd.DataFrame(data)
print(df)
# Rellenar los valores faltantes con 0
df.fillna(0, inplace=True)
print(df)

# Rellenar hacia adelante o hacia atrás:
# ffill: Rellena los valores faltantes hacia adelante, utilizando el último valor válido.
# bfill: Rellena los valores faltantes hacia atrás, utilizando el siguiente valor válido.
# Rellenar hacia adelante
print("Rellenar hacia adelante")
data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8]}
df = pd.DataFrame(data)
print(df)
df.fillna(method='ffill', inplace=True)
print(df)

# Rellenar hacia atrás
print("Rellenar hacia atras")
data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8]}
df = pd.DataFrame(data)
print(df)
df.fillna(method='bfill', inplace=True)
print(df)

# 3. Rellenar con la media, mediana o moda:
print("Rellenar con la media")
data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8]}
df = pd.DataFrame(data)
print(df)
# Rellenar con la media de la columna
df['A'].fillna(df['A'].mean(), inplace=True)
print(df)

# Rellenar con la mediana de la columna
print("Rellenar con la mediana")
data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8]}
df = pd.DataFrame(data)
print(df)
df['B'].fillna(df['B'].median(), inplace=True)
print(df)

# 4. Interpolación:
# Interpolación lineal
print("Rellenar con interpolacion lineal")
data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8]}
df = pd.DataFrame(data)
print(df)
df.interpolate(method='linear', inplace=True)
print(df)

# 5. Imputación basada en modelos:
# Para casos más complejos, se pueden utilizar modelos de machine learning para predecir los valores faltantes. 
# Por ejemplo, utilizando KNN (K-Nearest Neighbors), regresión lineal o redes neuronales.

# Ejemplo más completo:

import pandas as pd
import numpy as np

# Crear un DataFrame con valores faltantes
data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8], 'C': ['a', 'b', np.nan, 'd']}
df = pd.DataFrame(data)
print(df)
# Rellenar los valores faltantes numéricos con la media
#df.fillna(df.mean(), inplace=True)
df['A'].fillna(df['A'].mean(), inplace=True)
df['B'].fillna(df['B'].median(), inplace=True)

# Rellenar los valores faltantes de la columna 'C' con la moda
df['C'].fillna(df['C'].mode()[0], inplace=True)
print(df)

