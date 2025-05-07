import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings

warnings.filterwarnings("ignore")
# Cargar el dataset
df = pd.read_csv('Salary.csv')
# Mostrar las primeras filas del dataset
print(df.head())

# Grafica de dispersión
plt.scatter(df['YearsExperience'], df['Salary'])
plt.title('Experiencia vs Salario')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.show()

# Luego de verificar la correlación entre las variables,
#   se procede a crear el modelo de regresión lineal

modelo = LinearRegression() # Crear el modelo de regresión lineal
modelo.fit(df[['YearsExperience']], df['Salary'])  # Entrenar el modelo

# Generar datos de experiencia para la línea de regresión extendida
años_experiencia_extendido = np.linspace(df['YearsExperience'].min(), 16, 100).reshape(-1, 1)
prediccion_extendida = modelo.predict(años_experiencia_extendido)

print(f"Predicción para 16 años de experiencia: {modelo.predict([[16]])[0]}")  # Mostrar la predicción para un valor específico
input("Presiona Enter para continuar...")  # Esperar a que el usuario presione Enter
# Graficar la línea de regresión extendida

# Creamos un grafico de dispersion en los dos ejes
plt.scatter(df["YearsExperience"], df["Salary"], label='Datos Reales')
# Superponer la linea de regresión del modelo extendida en el grafico
plt.plot(años_experiencia_extendido, prediccion_extendida, color="red", label='Regresión Lineal')

plt.title('Experiencia vs Salario (Regresión Extendida) 2 años mas')  # Título del gráfico
plt.xlabel('Años de Experiencia')  # Etiqueta del eje x
plt.ylabel('Salario')  # Etiqueta del eje y
plt.legend()
plt.show()  # Mostrar el gráfico

# usamos una metrica de evaluacion como el coeficiente de
# determinacion (R^2) que nos permite medir la calidad de
# nuestras prediciones

# coeficiente de determinacion del modelo
# indica cuanta varianza hay en la variable dependiente
# en este caso es salario que puede ser explicada
# por la variable independiente años de experiencia
print("R^2: {}".format(modelo.score(df[["YearsExperience"]], df[["Salary"]])))