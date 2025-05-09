import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import joblib  # Para guardar y cargar el modelo y el scaler
from sklearn.metrics import pairwise_distances

# --- Paso 1: Cargar el modelo KNN y los datos preprocesados ---
# Asegúrate de que las rutas a tus archivos sean correctas
try:
    knn = joblib.load('ProyectoIAGrupo4modelo.joblib')
    scaler = joblib.load('ProyectoIAGrupo4scaler.joblib')
    feature_names = joblib.load('ProyectoIAGrupo4columns.joblib')  # Cargar los nombres de las columnas
    X_train_scaled = joblib.load('ProyectoIAGrupo4_X_train_scaled.joblib')
    y_train = joblib.load('ProyectoIAGrupo4_y_train.joblib')
    numeric_cols = joblib.load('ProyectoIAGrupo4_numeric_cols.joblib')
    k = knn.n_neighbors
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

# Campos para las variables categóricas
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

    # *** SOLUCIÓN: Reindexar con los nombres de las columnas guardadas ***
    nuevo_solicitante_final = nuevo_solicitante_df.reindex(columns=feature_names, fill_value=False)
    print("Forma de nuevo_solicitante_final después de reindexar:", nuevo_solicitante_final.shape)

    # Seleccionar solo las columnas numéricas para escalar
    nuevo_solicitante_scaled = scaler.transform(nuevo_solicitante_final[numeric_cols])
    print("Forma de nuevo_solicitante_scaled:", nuevo_solicitante_scaled.shape)


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
    distancias = pairwise_distances(nuevo_solicitante_final, X_train_scaled) # Cambio aquí

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
    