import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import joblib  # Para guardar y cargar el modelo y el scaler
import streamlit as st
from sklearn.metrics import classification_report, pairwise_distances

# --- Paso 1: Cargar el modelo KNN y el scaler entrenados ---
# Asegúrate de que la ruta a tus archivos sea correcta
try:
    knn = joblib.load('modelo_knn.joblib')
    scaler = joblib.load('scaler.joblib')
    feature_names = joblib.load('ProyectoIAKnnGrupo4.joblib') # Si guardaste los nombres de las columnas
except FileNotFoundError:
    st.error("Error: No se encontraron los archivos del modelo o del scaler. Asegúrate de haberlos guardado.")
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
    # y en el mismo orden. Si guardaste los nombres de las características, úsalos aquí.
    if feature_names is not None:
        nuevo_solicitante_df = nuevo_solicitante_df.reindex(columns=feature_names, fill_value=False)
    else:
        # Si no guardaste los nombres, asegúrate de que las columnas creadas coincidan manualmente
        # Esto es un ejemplo, AJUSTA LAS COLUMNAS EXACTAS DE TU MODELO
        columnas_esperadas = ['Edad', 'Ingresos mensuales', 'Dependientes', 'Porcentaje de endeudamiento',
                              'Ocupación_Comerciante', 'Ocupación_Estudiante', 'Ocupación_Ingeniero', 'Ocupación_Profesor', 'Ocupación_Técnico',
                              'Nivel educativo_Secundario', 'Nivel educativo_Universitario',
                              'Estado civil_Casado', 'Estado civil_Soltero', 'Estado civil_Viudo',
                              'Historial crediticio_Bueno', 'Historial crediticio_Excelente', 'Historial crediticio_Malo', 'Historial crediticio_Regular',
                              'Provincia_Alicante', 'Provincia_Badajoz', 'Provincia_Badalona', 'Provincia_Barcelona', 'Provincia_Bilbao', 'Provincia_Ceuta', 'Provincia_Cáceres', 'Provincia_Córdoba', 'Provincia_Elche', 'Provincia_Gijón', "Provincia_L'Hospitalet de Llobregat", 'Provincia_Las Palmas', 'Provincia_Madrid', 'Provincia_Melilla', 'Provincia_Murcia', 'Provincia_Málaga', 'Provincia_Palma', 'Provincia_Sevilla', 'Provincia_Valencia', 'Provincia_Valladolid', 'Provincia_Vigo', 'Provincia_Vitoria-Gasteiz', 'Provincia_Zaragoza']
        nuevo_solicitante_df = nuevo_solicitante_df.reindex(columns=columnas_esperadas, fill_value=False)

    # Seleccionar solo las columnas numéricas para escalar
    numeric_cols = ['Edad', 'Ingresos mensuales', 'Dependientes', 'Porcentaje de endeudamiento']
    nuevo_solicitante_scaled = scaler.transform(nuevo_solicitante_df[numeric_cols])
    nuevo_solicitante_scaled_df = pd.DataFrame(nuevo_solicitante_scaled, columns=numeric_cols)

    # Combinar las columnas numéricas escaladas con las columnas categóricas (que ya están en el DataFrame)
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

    # Calcular las distancias del nuevo solicitante a todos los puntos en X_train_scaled
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