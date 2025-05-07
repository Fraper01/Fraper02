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
plt.scatter(df['YearsExperience'], df['Salary'], label='Datos Reales')
plt.title('Experiencia vs Salario (con Predicción a 16 años)')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')

# Luego de verificar la correlación entre las variables,
#   se procede a crear el modelo de regresión lineal

modelo = LinearRegression() # Crear el modelo de regresión lineal
modelo.fit(df[['YearsExperience']], df['Salary'])  # Entrenar el modelo

# Generar datos de experiencia para la línea de regresión extendida
años_experiencia_extendido = np.linspace(df['YearsExperience'].min(), 20, 100).reshape(-1, 1)
prediccion_extendida = modelo.predict(años_experiencia_extendido)

# Graficar la línea de regresión extendida
plt.plot(años_experiencia_extendido, prediccion_extendida, color="red", label='Regresión Lineal')

# Predecir el salario para 16 años de experiencia
años_16 = np.array([[16]])
salario_predicho_16 = modelo.predict(años_16)[0]

# Graficar la línea horizontal para el salario predicho a los 16 años
plt.axhline(y=salario_predicho_16, color='green', linestyle='--', label=f'Salario Predicho (16 años: {salario_predicho_16:.2f} €)')

plt.legend()
plt.grid(True)  # Añadir una cuadrícula para mejor visualización
plt.show()  # Mostrar el gráfico

# usamos una metrica de evaluacion como el coeficiente de
# determinacion (R^2) que nos permite medir la calidad de
# nuestras predicciones

# coeficiente de determinacion del modelo
# indica cuanta varianza hay en la variable dependiente
# en este caso es salario que puede ser explicada
# por la variable independiente años de experiencia
print("R^2: {}".format(modelo.score(df[["YearsExperience"]], df[["Salary"]])))