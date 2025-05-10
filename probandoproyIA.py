import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder

# Cargar los nombres de las columnas preprocesadas
ruta_nombres_preprocesadas = 'nombres_caracteristicas_preprocesadas.joblib'
nombres_esperados = joblib.load(ruta_nombres_preprocesadas)
print("Nombres de las características preprocesadas cargados exitosamente.")

# Datos del nuevo solicitante
nuevo_solicitante_original = {
    'Edad': 35,
    'Género': 'Male',
    'Nivel Educativo': "Bachelor's",
    'Estado Civil': 'Married',
    'Ingreso': 60000,
    'Puntaje de Crédito': 720,
    'Monto del Préstamo': 15000,
    'Propósito del Préstamo': 'Home',
    'Situación Laboral': 'Employed',
    'Años en el Empleo Actual': 5,
    'Historial de Pagos': 'Excellent',
    'Relación Deuda-Ingreso': 0.25,
    'Valor de Activos': 100000,
    'Número de Dependientes': 2,
    'Cambio de Estado Civil': 0,
    'Incumplimientos Previos': 0
}
df_nuevo_solicitante_original = pd.DataFrame([nuevo_solicitante_original])

# Definir las listas de columnas ORIGINALES
continuas = ['Ingreso', 'Puntaje de Crédito', 'Monto del Préstamo',
             'Relación Deuda-Ingreso', 'Valor de Activos', 'Incumplimientos Previos']
discretas = ['Edad', 'Años en el Empleo Actual',
             'Número de Dependientes']
categorico = ['Género', 'Nivel Educativo', 'Estado Civil', 'Propósito del Préstamo',
             'Situación Laboral', 'Historial de Pagos', 'Cambio de Estado Civil']

# Preprocesar las características (como lo hicimos antes)
scaler_continuas = MinMaxScaler()
scaled_continuas = scaler_continuas.fit_transform(df_nuevo_solicitante_original[continuas])

scaler_discretas = StandardScaler()
scaled_discretas = scaler_discretas.fit_transform(df_nuevo_solicitante_original[discretas])

encoder_categoricas = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded_categoricas = encoder_categoricas.fit_transform(df_nuevo_solicitante_original[categorico])
encoded_feature_names = encoder_categoricas.get_feature_names_out(categorico)

# Crear el diccionario base con todas las columnas esperadas inicializadas en 0.0
nuevo_solicitante_final_dict = {col: 0.0 for col in nombres_esperados}

# Asignar los valores preprocesados al diccionario
for i, col in enumerate(continuas):
    nuevo_solicitante_final_dict[col] = scaled_continuas[0, i]

for i, col in enumerate(discretas):
    nuevo_solicitante_final_dict[col] = scaled_discretas[0, i]

for i, col_encoded in enumerate(encoded_feature_names):
    nuevo_solicitante_final_dict[col_encoded] = encoded_categoricas[0, i]

# Manejar la columna 'Cambio de Estado Civil' manualmente
cambio_estado_civil_original = nuevo_solicitante_original['Cambio de Estado Civil']
if cambio_estado_civil_original == 0:
    nuevo_solicitante_final_dict['Cambio de Estado Civil_0'] = 1.0
    nuevo_solicitante_final_dict['Cambio de Estado Civil_1'] = 0.0
    nuevo_solicitante_final_dict['Cambio de Estado Civil_2'] = 0.0
elif cambio_estado_civil_original == 1:
    nuevo_solicitante_final_dict['Cambio de Estado Civil_0'] = 0.0
    nuevo_solicitante_final_dict['Cambio de Estado Civil_1'] = 1.0
    nuevo_solicitante_final_dict['Cambio de Estado Civil_2'] = 0.0
elif cambio_estado_civil_original == 2:
    nuevo_solicitante_final_dict['Cambio de Estado Civil_0'] = 0.0
    nuevo_solicitante_final_dict['Cambio de Estado Civil_1'] = 0.0
    nuevo_solicitante_final_dict['Cambio de Estado Civil_2'] = 1.0

# Asegurarnos de que la columna original 'Cambio de Estado Civil' NO esté en el diccionario final
if 'Cambio de Estado Civil' in nuevo_solicitante_final_dict:
    del nuevo_solicitante_final_dict['Cambio de Estado Civil']

print("\nDiccionario FINAL creado manualmente:")
print(nuevo_solicitante_final_dict)

# Ahora podemos crear un DataFrame a partir de este diccionario para la predicción
df_nuevo_solicitante_final = pd.DataFrame([nuevo_solicitante_final_dict])

# Cargar el mejor pipeline
ruta_cargado = 'best_pipeline_riesgo_financiero.joblib'
modelo_cargado = joblib.load(ruta_cargado)

# Realizar la predicción
prediccion_numerica = modelo_cargado.predict(df_nuevo_solicitante_final)[0]
mapeo_riesgo = {0: 'Low', 1: 'Medium', 2: 'High'}
prediccion_riesgo = mapeo_riesgo[prediccion_numerica]

print(f"\nLa predicción de riesgo para el nuevo solicitante (creado manualmente) es: {prediccion_riesgo}")

# Probabilidades (opcional)
probabilidades = modelo_cargado.predict_proba(df_nuevo_solicitante_final)[0]
print("\nProbabilidades de cada clase:")
print(f"Bajo Riesgo (0): {probabilidades[0]:.4f}")
print(f"Riesgo Medio (1): {probabilidades[1]:.4f}")
print(f"Alto Riesgo (2): {probabilidades[2]:.4f}")