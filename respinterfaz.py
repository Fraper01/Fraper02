import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import joblib  # Para guardar y cargar el modelo y el scaler
from sklearn.metrics import pairwise_distances

# --- Paso 1: Cargar el modelo KNN y los datos preprocesados ---
# Asegúrate de que las rutas a tus archivos sean correctas y coincidan
# con los nombres que usaste al guardarlos con joblib.dump()
try:
    knn = joblib.load('ProyectoIAGrupo4modelo.joblib')
    scaler = joblib.load('ProyectoIAGrupo4scaler.joblib')
    feature_names = joblib.load('ProyectoIAGrupo4columns.joblib')
    X_train_scaled = joblib.load('ProyectoIAGrupo4_X_train_scaled.joblib')
    y_train = joblib.load('ProyectoIAGrupo4_y_train.joblib')
    numeric_cols = joblib.load('ProyectoIAGrupo4_numeric_cols.joblib')
    k = knn.n_neighbors  # Obtener k del modelo
except FileNotFoundError:
    st.error("Error: No se encontraron los archivos del modelo. Asegúrate de que estén en el mismo directorio o especifica la ruta correcta.")
    st.stop()

# --- Paso 2: Crear la interfaz de usuario con Streamlit ---
st.title("Evaluador de Riesgo Crediticio")
st.markdown("Introduce los datos del solicitante para predecir el **nivel de riesgo crediticio**.")

# Crear campos de entrada para las características del solicitante
edad = st.number_input("Edad", min_value=18, max_value=100, value=30)
ingresos = st.number_input("Ingresos mensuales (€)", min_value=0, value=2000)
dependientes = st.number_input("Número de dependientes", min_value=0, value=0)
endeudamiento = st.number_input("Porcentaje de endeudamiento", min_value=0.0, max_value=1.0, value=0.1, format="%.2f")

# Campos para las variables categóricas (¡importante que coincidan con tus columnas one-hot!)
ocupacion = st.selectbox("Ocupación", ['Comerciante', 'Estudiante', 'Ingeniero', 'Profesor', 'Técnico'])
nivel_educativo = st.selectbox("Nivel educativo", ['Secundario', 'Universitario'])
estado_civil = st.selectbox("Estado civil", ['Soltero', 'Casado'])
historial_crediticio = st.selectbox("Historial crediticio", ['Excelente', 'Bueno', 'Regular', 'Malo'])
provincia = st.selectbox("Provincia", ['Alicante', 'Badajoz', 'Badalona', 'Barcelona', 'Bilbao', 'Ceuta', 'Cáceres', 'Córdoba', 'Elche', 'Gijón', "L'Hospitalet de Llobregat", 'Las Palmas', 'Madrid', 'Melilla', 'Murcia', 'Málaga', 'Palma', 'Sevilla', 'Valencia', 'Valladolid', 'Vigo', 'Vitoria-Gasteiz', 'Zaragoza'])

if st.button("Evaluar Riesgo"):
    # --- Paso 3: Preparar los datos del nuevo solicitante ---
    nuevo_solicitante = {
        'Edad': edad,
        'Ingresos mensuales': ingresos,
        'Dependientes': dependientes,
        'Porcentaje de endeudamiento': endeudamiento,
        f'Ocupación_{ocupacion}': True,
        f'Nivel educativo_{nivel_educativo}': True,
        f'Estado civil_{estado_civil}': True,
        f'Historial crediticio_{historial_crediticio}': True,
        f'Provincia_{provincia}': True
    }

    # Crear un DataFrame con el nuevo solicitante
    nuevo_solicitante_df = pd.DataFrame([nuevo_solicitante])

    # Asegurarse de que el DataFrame tenga todas las columnas esperadas por el modelo
    if feature_names is not None:
        nuevo_solicitante_df = nuevo_solicitante_df.reindex(columns=feature_names, fill_value=False)
    else:
        # Si no guardaste los nombres, debes definir las columnas manualmente
        # ¡Asegúrate de que esta lista coincida PERFECTAMENTE con el orden y los nombres
        # de las columnas que tu modelo espera después del one-hot encoding!
        columnas_esperadas = ['Edad', 'Ingresos mensuales', 'Dependientes', 'Porcentaje de endeudamiento',
                             'Ocupación_Comerciante', 'Ocupación_Estudiante', 'Ocupación_Ingeniero', 'Ocupación_Profesor', 'Ocupación_Técnico',
                             'Nivel educativo_Secundario', 'Nivel educativo_Universitario',
                             'Estado civil_Casado', 'Estado civil_Soltero', 'Estado civil_Viudo',
                             'Historial crediticio_Bueno', 'Historial crediticio_Excelente', 'Historial crediticio_Malo', 'Historial crediticio_Regular',
                             'Provincia_Alicante', 'Provincia_Badajoz', 'Provincia_Badalona', 'Provincia_Barcelona', 'Provincia_Bilbao', 'Provincia_Ceuta', 'Provincia_Cáceres', 'Provincia_Córdoba', 'Provincia_Elche', 'Provincia_Gijón', "Provincia_L'Hospitalet de Llobregat", 'Provincia_Las Palmas', 'Provincia_Madrid', 'Provincia_Melilla', 'Provincia_Murcia', 'Provincia_Málaga', 'Provincia_Palma', 'Provincia_Sevilla', 'Provincia_Valencia', 'Provincia_Valladolid', 'Provincia_Vigo', 'Provincia_Vitoria-Gasteiz', 'Provincia_Zaragoza']
        nuevo_solicitante_df = nuevo_solicitante_df.reindex(columns=columnas_esperadas, fill_value=False)

    # Seleccionar solo las columnas numéricas para escalar
    nuevo_solicitante_scaled = scaler.transform(nuevo_solicitante_df[numeric_cols])
    nuevo_solicitante_scaled_df = pd.DataFrame(nuevo_solicitante_scaled, columns=numeric_cols)

    # Combinar las columnas numéricas escaladas con las columnas categóricas
    nuevo_solicitante_final = pd.concat([nuevo_solicitante_scaled_df, nuevo_solicitante_df.drop(columns=numeric_cols, errors='ignore')], axis=1)

    # --- Paso 4: Realizar la predicción ---
    prediccion = knn.predict(nuevo_solicitante_final)

    # --- Paso 5: Mostrar el resultado ---
    st.subheader("Resultado de la Evaluación:")
    if prediccion[0] == 'Bajo':
        st.success(f"El nivel de riesgo crediticio estimado es: **{prediccion[0]}**")
        st.balloons()
    elif prediccion[0] == 'Medio':
        st.warning(f"El nivel de riesgo crediticio estimado es: **{prediccion[0]}**")
    else:
        st.error(f"El nivel de riesgo crediticio estimado es: **{prediccion[0]}**")

    # --- Paso 6: Análisis del Nuevo Solicitante ---
    st.subheader("Análisis Detallado del Solicitante:")

    # Calcular las distancias del nuevo solicitante (escalado) a todos los puntos en X_train_scaled
    distancias = pairwise_distances(nuevo_solicitante_scaled, X_train_scaled)

    # Obtener los índices de los k vecinos más cercanos
    indices_vecinos_cercanos = np.argsort(distancias[0])[:k]

    # Obtener los niveles de riesgo de los k vecinos más cercanos
    riesgos_vecinos_cercanos = y_train.iloc[indices_vecinos_cercanos].tolist()

    # Obtener el índice y el nivel de riesgo del vecino más cercano
    indice_vecino_mas_cercano = indices_vecinos_cercanos[0]
    riesgo_vecino_mas_cercano = y_train.iloc[indice_vecino_mas_cercano]

    st.write(f"Índice del vecino más cercano en el conjunto de entrenamiento: {indice_vecino_mas_cercano}")
    st.write(f"Nivel de riesgo del vecino más cercano: {riesgo_vecino_mas_cercano}")
    st.write(f"Índices de los {k} vecinos más cercanos en el conjunto de entrenamiento: {indices_vecinos_cercanos}")
    st.write(f"Niveles de riesgo de los {k} vecinos más cercanos: {riesgos_vecinos_cercanos}")
    st.write(f"Predicción del modelo: {prediccion[0]}")
    st.write("Valores escalados del nuevo solicitante (solo numéricas):")
    st.write(nuevo_solicitante_scaled)
    st.write("Nombres de las columnas numéricas (escaladas):")
    st.write(numeric_cols)
    st.write("Primeras 5 filas del conjunto de entrenamiento escalado:")
    st.write(X_train_scaled.head())


"""
```python
!pip install streamlit
!pip install pyngrok

import streamlit as st
from pyngrok import ngrok

# Tu código de Streamlit aquí
st.title("Mi Aplicación Streamlit en Colab")
st.write("¡Hola desde Streamlit en Google Colab!")
x = st.slider('Selecciona un valor')
st.write(x, 'al cuadrado es', x*x)

if __name__ == '__main__':
    # Iniciar ngrok
    # Configura tu authtoken de ngrok.  Obténlo de https://dashboard.ngrok.com/get-started/your-authtoken
    ngrok.set_auth_token("2wr7ZTUGE10YbDkBKhSkDImYr1S_88R59Ux1V1Eua6j6pL42p")  # Reemplaza con tu authtoken
    try:
        ngrok_tunnel = ngrok.connect()
        print('URL pública:', ngrok_tunnel.public_url)
        st.write(f'La aplicación está disponible en: {ngrok_tunnel.public_url}') #muestra la url en la interfaz
    except Exception as e:
        print(f"Error al iniciar ngrok: {e}")
        ngrok.kill()
    # Ejecutar la aplicación Streamlit
    !streamlit run --server.port 8501 {sys.argv[0]}
    ngrok.kill()}
"""