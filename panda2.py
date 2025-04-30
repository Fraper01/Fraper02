import pandas as pd

# Crea una lista de listas (cada lista interna representa una fila)
# Ejercicio 1
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# Crea el DataFrame
df = pd.DataFrame(data)

print("Ejercicio 1")
print(df)

import pandas as pd

# Crear un DataFrame de ejemplo
# Ejercio 2.1
data = {'Columna1': [1, 2, 3, 4, 5, 6 ],
        'Columna2': [7, 8, 9, 10,11,12]}
df = pd.DataFrame(data)

# Obtener el tamaño del DataFrame
print("Ejercicio 2.1")
print("DataFrame",df)
print("Forma del DataFrame:", df.shape)  # Imprime: (3, 2)
print("Número total de elementos:", df.size)  # Imprime: 6
print("Número de filas:", len(df))  # Imprime: 3

# Ejercio 2.2
# Mostrar las 3 primera filas del DataFrame
print("Ejercicio 2.2")
print (df.head(3))


# Ejercio 3.1
print("Ejercio 3.1")
# seleccionar datos del DataFrame por etiqueta (loc)
import pandas as pd
# Crear un DataFrame
data = {'Columna1': [1, 2, 3], 'Columna2': [4, 5, 6]}
df = pd.DataFrame(data)

# Seleccionar la fila con índice 1 y la columna 'Columna2'
valor = df.loc[1, 'Columna2']  
print("Ejercicio 3.1")
print(df)
print("Valor indice 1 columna 2 =",valor)

# Seleccionar las primeras dos filas y todas las columnas por el indice 
primeras_dos_filas = df.iloc[:2]
print(primeras_dos_filas)

# Seleccionar filas donde el contenido de la 'Columna1' sea mayor que 2
filas_filtradas = df[df['Columna1'] > 2]
print(filas_filtradas)

# Seleccionar filas donde el contenido de la 'Columna1' sea mayor que 2 y 'Columna2' sea par
#Operadores lógicos: Utiliza operadores como & (y), | (o) y ~ (no) para combinar condiciones.
filas_filtradas = df.loc[(df['Columna1'] >= 1) & (df['Columna2'] % 2 == 0)]
print(filas_filtradas)

#Ejemplos más detallados:
print("Seleccionar una columna") #Seleccionar una columna:
print(df['Columna1'])

print("Seleccionar varias columnas") #Seleccionar varias columnas:
print(df[['Columna1', 'Columna2']])

print("Seleccionar un rango de filas") #Seleccionar un rango de filas:
print(df[1:3])  # Filas con índice 1 y 2

print("Seleccionar filas por un valor específico") #Seleccionar filas por un valor específico:
print(df[df['Columna1'] == 3])

# Ejercio 3.2
print("Ejercio 3.2")
# Métodos para agregar una nueva columna:
# Asignación directa:
# La forma más sencilla es asignar una lista o serie a una nueva etiqueta de columna.
print(" Asignación directa")
import pandas as pd
# Crear un DataFrame de ejemplo
data = {'Columna1': [1, 2, 3], 'Columna2': [4, 5, 6]}
df = pd.DataFrame(data)
print(df)
# Agregar una nueva columna
df['NuevaColumna'] = [7, 8, 9]
print(df)

#Usando el método assign():
#Este método crea una copia del DataFrame con la nueva columna agregada.
print("Usando el método assign()")
df_nuevo = df.assign(NuevaColumna=[7, 8, 9])
print(df_nuevo)

#Calculando valores:
#Puedes crear una nueva columna basada en cálculos sobre otras columnas.
print("Caculando valores")
df['ColumnaSuma'] = df['Columna1'] + df['Columna2'] + df['NuevaColumna']
print(df)

#Aplicando funciones:
#Utiliza la función apply para aplicar una función a cada fila o columna y crear una nueva columna.
print("Aplicando funciones")
def cuadrado(x):
    return x**2
df['CuadradoColumna1'] = df['Columna1'].apply(cuadrado)
df['CuadradoColumna2'] = df['Columna2'].apply(cuadrado)
print(df)


#Ejemplo más completo:
print("Ejemplo más completo")
import pandas as pd
# Crear un DataFrame de ejemplo
data = {'Nombre': ['Ana', 'Juan', 'Pedro'], 'Edad': [25, 30, 28]}
df = pd.DataFrame(data)

# Agregar una columna 'Categoría' basada en la edad
def categorizar_edad(edad):
    if edad < 30:
        return 'Joven'
    else:
        return 'Adulto'

df['Categoría'] = df['Edad'].apply(categorizar_edad)

print(df)
print (df.describe())

