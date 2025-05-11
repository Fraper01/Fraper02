import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder
from sklearn.metrics import pairwise_distances

# --- Cargar archivos y definir columnas (igual que antes) ---
ruta_nombres_preprocesadas = 'nombres_caracteristicas_preprocesadas.joblib'
try:
    nombres_esperados = joblib.load(ruta_nombres_preprocesadas)
except FileNotFoundError:
    st.error(f"Error: No se encontró el archivo: {ruta_nombres_preprocesadas}")
    st.stop()

ruta_modelo = 'best_pipeline_riesgo_financiero.joblib'
try:
    modelo_cargado = joblib.load(ruta_modelo)
except FileNotFoundError:
    st.error(f"Error: No se encontró el archivo: {ruta_modelo}")
    st.stop()

continuas_orig = ['Ingreso', 'Puntaje de Crédito', 'Monto del Préstamo',
                  'Relación Deuda-Ingreso', 'Valor de Activos', 'Incumplimientos Previos']
discretas_orig = ['Edad', 'Años en el Empleo Actual',
                  'Número de Dependientes']
categorico_orig = ['Género', 'Nivel Educativo', 'Estado Civil', 'Propósito del Préstamo',
                   'Situación Laboral', 'Historial de Pagos', 'Cambio de Estado Civil']

nuevo_solicitante_input = {}

st.title("Predicción de Riesgo Financiero (KNN)")
st.write("Ingrese los datos del solicitante:")

# --- Widgets de entrada (igual que antes) ---
nuevo_solicitante_input['Ingreso'] = st.number_input('Ingreso', value=40000.0)
nuevo_solicitante_input['Puntaje de Crédito'] = st.number_input('Puntaje de Crédito', value=650.0)
nuevo_solicitante_input['Monto del Préstamo'] = st.number_input('Monto del Préstamo', value=20000.0)
nuevo_solicitante_input['Relación Deuda-Ingreso'] = st.number_input('Relación Deuda-Ingreso', value=0.35)
nuevo_solicitante_input['Valor de Activos'] = st.number_input('Valor de Activos', value=50000.0)
nuevo_solicitante_input['Incumplimientos Previos'] = st.number_input('Incumplimientos Previos', value=1.0)
nuevo_solicitante_input['Edad'] = st.number_input('Edad', step=1, value=40)
nuevo_solicitante_input['Años en el Empleo Actual'] = st.number_input('Años en el Empleo Actual', step=1, value=3)
nuevo_solicitante_input['Número de Dependientes'] = st.number_input('Número de Dependientes', step=1, value=1)
nuevo_solicitante_input['Género'] = st.selectbox('Género', ['Male', 'Female', 'Non-binary'], index=0)
nuevo_solicitante_input['Nivel Educativo'] = st.selectbox('Nivel Educativo', ["Bachelor's", 'High School', "Master's", 'PhD'], index=1)
nuevo_solicitante_input['Estado Civil'] = st.selectbox('Estado Civil', ['Married', 'Single', 'Divorced', 'Widowed'], index=1)
nuevo_solicitante_input['Propósito del Préstamo'] = st.selectbox('Propósito del Préstamo', ['Home', 'Auto', 'Business', 'Personal'], index=0)
nuevo_solicitante_input['Situación Laboral'] = st.selectbox('Situación Laboral', ['Employed', 'Self-employed', 'Unemployed'], index=0)
nuevo_solicitante_input['Historial de Pagos'] = st.selectbox('Historial de Pagos', ['Excellent', 'Good', 'Fair', 'Poor'], index=2)
nuevo_solicitante_input['Cambio de Estado Civil'] = st.selectbox('Cambio de Estado Civil', [0, 1, 2], index=1)

if st.button("Predecir Riesgo"):
    # --- Preprocesamiento (igual que antes) ---
    df_nuevo_solicitante_original = pd.DataFrame([nuevo_solicitante_input])
    scaler_continuas = MinMaxScaler()
    scaled_continuas = scaler_continuas.fit_transform(df_nuevo_solicitante_original[continuas_orig])
    scaler_discretas = StandardScaler()
    scaled_discretas = scaler_discretas.fit_transform(df_nuevo_solicitante_original[discretas_orig])
    encoder_categoricas = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded_categoricas = encoder_categoricas.fit_transform(df_nuevo_solicitante_original[categorico_orig])
    encoded_feature_names = encoder_categoricas.get_feature_names_out(categorico_orig)
    nuevo_solicitante_preprocesado = {}
    for i, col in enumerate(continuas_orig):
        nuevo_solicitante_preprocesado[col] = scaled_continuas[0, i]
    for i, col in enumerate(discretas_orig):
        nuevo_solicitante_preprocesado[col] = scaled_discretas[0, i]
    for i, col_encoded in enumerate(encoded_feature_names):
        nuevo_solicitante_preprocesado[col_encoded] = encoded_categoricas[0, i]
    nuevo_solicitante_final_dict = {col: nuevo_solicitante_preprocesado.get(col, 0) for col in nombres_esperados}
    cambio_estado_civil_original = nuevo_solicitante_input['Cambio de Estado Civil']
    if 'Cambio de Estado Civil' in nuevo_solicitante_final_dict:
        del nuevo_solicitante_final_dict['Cambio de Estado Civil']
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
    df_nuevo_solicitante_final = pd.DataFrame([nuevo_solicitante_final_dict])

    # --- Predicción ---
    prediccion_numerica = modelo_cargado.predict(df_nuevo_solicitante_final)[0]
    mapeo_riesgo = {0: 'Bajo', 1: 'Medio', 2: 'Alto'}
    prediccion_riesgo = mapeo_riesgo[prediccion_numerica]
    st.subheader(f"El riesgo predicho para el solicitante es: {prediccion_riesgo}")
    probabilidades = modelo_cargado.predict_proba(df_nuevo_solicitante_final)[0]
    st.write("Probabilidades:")
    st.write(f"Bajo Riesgo: {probabilidades[0]:.4f}")
    st.write(f"Riesgo Medio: {probabilidades[1]:.4f}")
    st.write(f"Alto Riesgo: {probabilidades[2]:.4f}")

    # --- 1. Interpretación de la Predicción ---
    st.subheader("Interpretación de la Predicción:")
    if prediccion_riesgo == 'Bajo':
        st.write("El modelo predice que este solicitante tiene un bajo riesgo de incumplimiento en el préstamo.")
    elif prediccion_riesgo == 'Medio':
        st.write("El modelo predice que este solicitante tiene un riesgo moderado de incumplimiento en el préstamo.")
    else:
        st.write("El modelo predice que este solicitante tiene un alto riesgo de incumplimiento en el préstamo.")

    # --- 2. Umbrales de Clasificación (KNN no tiene umbrales directos) ---
    st.subheader("Umbrales de Clasificación:")
    st.write("El modelo KNN clasifica el riesgo basándose en la mayoría de los votos de los vecinos más cercanos. No hay umbrales de probabilidad explícitos como en otros modelos.")

# --- 5. Análisis del Solicitante ---
    st.subheader("Análisis del Solicitante:")

    # Predicción del nivel de riesgo (esto ya lo tenemos y funciona)
    nivel_riesgo_predicho = modelo_cargado.predict(df_nuevo_solicitante_final)[0]
    mapeo_riesgo = {0: 'Bajo', 1: 'Medio', 2: 'Alto'}
    st.write(f"Nivel de riesgo predicho: {mapeo_riesgo[nivel_riesgo_predicho]}")

    # Probabilidades de riesgo (esto también lo tenemos y funciona)
    try:
        probabilidades = modelo_cargado.predict_proba(df_nuevo_solicitante_final)[0]
        st.subheader("Probabilidades de Riesgo del Solicitante:")
        st.write(f"Probabilidad de Riesgo Bajo: {probabilidades[0]:.4f}")
        st.write(f"Probabilidad de Riesgo Medio: {probabilidades[1]:.4f}")
        st.write(f"Probabilidad de Riesgo Alto: {probabilidades[2]:.4f}")
    except AttributeError:
        st.warning("El modelo cargado no tiene un método 'predict_proba'. No se pueden mostrar las probabilidades.")
    except Exception as e:
        st.error(f"Ocurrió un error al obtener las probabilidades: {e}")

    # --- Lo que NO vamos a utilizar por ahora ---
    # st.subheader("Explicación de la Predicción (Opcional - SHAP)")
    # if st.checkbox("Mostrar explicación de la predicción (SHAP)"):
    #     try:
    #         explainer = shap.TreeExplainer(modelo_cargado.named_steps['classifier'])
    #         shap_values = explainer.shap_values(df_nuevo_solicitante_final)
    #         st_shap(shap.summary_plot(shap_values, df_nuevo_solicitante_final, plot_type="bar", show=False), height=300)
    #     except Exception as e:
    #         st.error(f"Ocurrió un error al generar la explicación SHAP: {e}")

    # --- Lo que NO vamos a utilizar por ahora (Comparación con Vecinos - pendiente de solucionar) ---
    # st.subheader("Comparación con Vecinos Cercanos:")
    # try:
    #     # ... (Tu código para la comparación con vecinos) ...
    # except Exception as e:
    #     st.error(f"Ocurrió un error al analizar los vecinos cercanos: {e}")
    #     st.warning("Asegúrate de tener los archivos necesarios y que el modelo KNN esté configurado correctamente.")

    # --- Añadimos los valores de las variables preprocesadas ---
    st.subheader("Valores de Variables Preprocesadas del Solicitante:")
    for nombre_col in df_nuevo_solicitante_final.columns:
        valor = df_nuevo_solicitante_final[nombre_col].iloc[0]
        st.write(f"{nombre_col}: {valor:.4f}")        