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
#  se procede a crear el modelo de regresión lineal

modelo = LinearRegression() # Crear el modelo de regresión lineal
modelo.fit(df[['YearsExperience']], df['Salary'])  # Entrenar el modelo
# Predecir los valores de salario
#prediccion = modelo.predict(df[['YearsExperience']])  # Predecir los valores de salario
prediccion = modelo.predict([[20]])  # Predecir los valores de salario para un nuevo valor de experiencia
print(f"Predicción para 20 años de experiencia: {prediccion[0]}")  # Mostrar la predicción
input("Presiona Enter para continuar...")  # Esperar a que el usuario presione Enter
# Graficar la línea de regresión    

#Creamos un grafico de dispersion en los dos ejes 
plt.scatter(df["YearsExperience"], df["Salary"])
#Superponer la linea de regresión del modelo en el grafico 
plt.plot(df["YearsExperience"], modelo.predict(df[["YearsExperience"]]), color="red")

#plt.plot(df['YearsExperience'], prediccion, color='red')  # Graficar la línea de regresión
#plt.scatter(df['YearsExperience'], df['Salary'])  # Graficar los puntos de datos    
plt.title('Experiencia vs Salario')  # Título del gráfico
plt.xlabel('Años de Experiencia')  # Etiqueta del eje x 
plt.ylabel('Salario')  # Etiqueta del eje y
plt.show()  # Mostrar el gráfico

#plt.plot(df['YearsExperience'], molelo.predict(df[['YearsExperience']]), color='red', linewidth=2)  # Graficar la línea de regresión
#plt.scatter(df['YearsExperience'], df['Salary'])  # Graficar los puntos de datos

# usamos una metrica de evaluacion como el coeficiente de 
# determinacion (R^2) que nos permite medir la calidad de
# nuestras prediciones

# coeficiente de determinacion del modelo
# indica cuanta varianza hay en la variable dependiente
# en este caso es salario que puede ser explicada
# por la variable independiente años de experiencia
print("R^2: {}".format(modelo.score(df[["YearsExperience"]], df[["Salary"]])))

