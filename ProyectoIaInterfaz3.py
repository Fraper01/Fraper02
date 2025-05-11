import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder

# --- Cargar archivos y definir columnas ---
ruta_nombres_preprocesadas = 'nombres_caracteristicas_preprocesadas.joblib'
ruta_modelo = 'best_pipeline_riesgo_financiero.joblib'

try:
    nombres_esperados = joblib.load(ruta_nombres_preprocesadas)
    modelo_cargado = joblib.load(ruta_modelo)
except FileNotFoundError as e:
    st.error(f"Error: No se encontró el archivo: {e.filename}")
    st.stop()
except Exception as e:
    st.error(f"Error inesperado al cargar los archivos: {e}")
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

# --- Widgets de entrada ---
nuevo_solicitante_input['Ingreso'] = st.number_input('Ingreso', value=40000.0)
nuevo_solicitante_input['Puntaje de Crédito'] = st.number_input('Puntaje de Crédito', value=650.0)
nuevo_solicitante_input['Monto del Préstamo'] = st.number_input('Monto del Préstamo', value=20000.0)
nuevo_solicitante_input['Relación Deuda-Ingreso'] = st.number_input('Relación Deuda-Ingreso', value=0.35)
nuevo_solicitante_input['Valor de Activos'] = st.number_input('Valor de Activos', value=50000.0)
nuevo_solicitante_input['Incumplimientos Previos'] = st.number_input('Incumplimientos Previos', value=1.0)
nuevo_solicitante_input['Edad'] = st.number_input('Edad', step=1, value=40)
nuevo_solicitante_input['Años en el Empleo Actual'] = st.number_input('Años en el Empleo Actual', value=3)
nuevo_solicitante_input['Número de Dependientes'] = st.number_input('Número de Dependientes', value=1)
nuevo_solicitante_input['Género'] = st.selectbox('Género', ['Male', 'Female', 'Non-binary'], index=0)
nuevo_solicitante_input['Nivel Educativo'] = st.selectbox('Nivel Educativo', ["Bachelor's", 'High School', "Master's", 'PhD'], index=1)
nuevo_solicitante_input['Estado Civil'] = st.selectbox('Estado Civil', ['Married', 'Single', 'Divorced', 'Widowed'], index=1)
nuevo_solicitante_input['Propósito del Préstamo'] = st.selectbox('Propósito del Préstamo', ['Home', 'Auto', 'Business', 'Personal'], index=0)
nuevo_solicitante_input['Situación Laboral'] = st.selectbox('Situación Laboral', ['Employed', 'Self-employed', 'Unemployed'], index=0)
nuevo_solicitante_input['Historial de Pagos'] = st.selectbox('Historial de Pagos', ['Excellent', 'Good', 'Fair', 'Poor'], index=2)
nuevo_solicitante_input['Cambio de Estado Civil'] = st.selectbox('Cambio de Estado Civil', [0, 1, 2], index=1)

# --- Preprocesamiento ---
st.write("--- Inspección de Datos de Entrada ---")
st.subheader("1. `nuevo_solicitante_input`:")
st.write(nuevo_solicitante_input)

st.subheader("2. Listas de nombres de columnas originales:")
st.write(f"`continuas_orig`: {continuas_orig}")
st.write(f"`discretas_orig`: {discretas_orig}")
st.write(f"`categorico_orig`: {categorico_orig}")

# Creamos el DataFrame directamente usando las listas de nombres de las columnas
data = {
    'Ingreso': nuevo_solicitante_input['Ingreso'],
    'Puntaje de Crédito': nuevo_solicitante_input['Puntaje de Crédito'],
    'Monto del Préstamo': nuevo_solicitante_input['Monto del Préstamo'],
    'Relación Deuda-Ingreso': nuevo_solicitante_input['Relación Deuda-Ingreso'],
    'Valor de Activos': nuevo_solicitante_input['Valor de Activos'],
    'Incumplimientos Previos': nuevo_solicitante_input['Incumplimientos Previos'],
    'Edad': nuevo_solicitante_input['Edad'],
    'Años en el Empleo Actual': nuevo_solicitante_input['Años en el Empleo Actual'],
    'Número de Dependientes': nuevo_solicitante_input['Número de Dependientes'],
    'Género': nuevo_solicitante_input['Género'],
    'Nivel Educativo': nuevo_solicitante_input['Nivel Educativo'],
    'Estado Civil': nuevo_solicitante_input['Estado Civil'],
    'Propósito del Préstamo': nuevo_solicitante_input['Propósito del Préstamo'],
    'Situación Laboral': nuevo_solicitante_input['Situación Laboral'],
    'Historial de Pagos': nuevo_solicitante_input['Historial de Pagos'],
    'Cambio de Estado Civil': nuevo_solicitante_input['Cambio de Estado Civil'],
}
df_nuevo_solicitante_original = pd.DataFrame([data])

st.subheader("3. Columnas en `df_nuevo_solicitante_original`:")
st.write(f"{df_nuevo_solicitante_original.columns.tolist()}")
st.write("--- Fin de la Inspección ---")


if st.button("Predecir Riesgo"):
    df_nuevo_solicitante_original = df_nuevo_solicitante_original.copy()
    st.subheader("4. DataFrame Original antes del preprocesamiento:")
    st.write(df_nuevo_solicitante_original)

    try:
        scaler_continuas = MinMaxScaler()
        st.subheader("5. Valores de Continuas antes de la transformación:")
        st.write(df_nuevo_solicitante_original[continuas_orig])
        scaled_continuas = scaler_continuas.fit_transform(df_nuevo_solicitante_original[continuas_orig])
        st.subheader("6. Valores de Continuas después de la transformación:")
        st.write(scaled_continuas)

        scaler_discretas = StandardScaler()
        st.subheader("7. Valores de Discretas antes de la transformación:")
        st.write(df_nuevo_solicitante_original[discretas_orig])
        scaled_discretas = scaler_discretas.fit_transform(df_nuevo_solicitante_original[discretas_orig])
        st.subheader("8. Valores de Discretas después de la transformación:")
        st.write(scaled_discretas)

        encoder_categoricas = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        st.subheader("9. Valores de Categoricas antes de la codificación:")
        st.write(df_nuevo_solicitante_original[categorico_orig])
        encoded_categoricas = encoder_categoricas.fit_transform(df_nuevo_solicitante_original[categorico_orig])
        encoded_feature_names = encoder_categoricas.get_feature_names_out(categorico_orig)
        st.subheader("10. Valores de Categoricas después de la codificación:")
        st.write(encoded_categoricas)
    except Exception as e:
        st.error(f"Error durante el preprocesamiento: {e}")
        st.stop()

    # Crear un diccionario con los valores escalados y codificados
    nuevo_solicitante_preprocesado = {}
    try:
        for i, col in enumerate(continuas_orig):
            nuevo_solicitante_preprocesado[col] = scaled_continuas[0, i]
        for i, col in enumerate(discretas_orig):
            nuevo_solicitante_preprocesado[col] = scaled_discretas[0, i]
        for i, col_encoded in enumerate(encoded_feature_names):
            nuevo_solicitante_preprocesado[col_encoded] = encoded_categoricas[0, i]
    except IndexError:
        st.error("Error: Los datos preprocesados no tienen la forma esperada.  Verifique las dimensiones de los datos después del escalamiento y la codificación.")
        st.stop()
    except KeyError as e:
        st.error(f"Error de clave: La columna '{e.args[0]}' no se encuentra en los datos preprocesados.  Asegúrese de que los nombres de las columnas coincidan con los nombres esperados por el modelo.")
        st.stop()
    except Exception as e:
        st.error(f"Error inesperado al crear el diccionario de datos preprocesados: {e}")
        st.stop()

    st.subheader("Contenido de `nuevo_solicitante_preprocesado`:")
    st.write(nuevo_solicitante_preprocesado)

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

    # Verificar si el diccionario final tiene el número correcto de columnas
    if len(nuevo_solicitante_final_dict) != len(nombres_esperados):
        st.error(f"Error: El número de columnas en el diccionario final ({len(nuevo_solicitante_final_dict)}) no coincide con el número de columnas esperadas ({len(nombres_esperados)}).")
        st.stop()

    # Verificar si faltan columnas en el diccionario final
    columnas_faltantes = [col for col in nombres_esperados if col not in nuevo_solicitante_final_dict]
    if columnas_faltantes:
        st.error(f"Error: Faltan las siguientes columnas en el diccionario final: {columnas_faltantes}")
        st.stop()
    try:
        df_nuevo_solicitante_final = pd.DataFrame([nuevo_solicitante_final_dict])
    except ValueError as e:
        st.error(f"Error al crear el DataFrame: {e}. Verifique que el diccionario tenga la estructura correcta y que los valores sean del tipo esperado.")
        st.stop()
    except Exception as e:
        st.error(f"Error inesperado al crear el DataFrame: {e}")
        st.stop()

    # --- Mostrar el DataFrame antes de la predicción ---
    st.subheader("DataFrame `df_nuevo_solicitante_final` antes de la predicción:")
    st.write(df_nuevo_solicitante_final)

    # --- Predicción ---
    try:
        prediccion_numerica = modelo_cargado.predict(df_nuevo_solicitante_final)[0]
        mapeo_riesgo = {0: 'Bajo', 1: 'Medio', 2: 'Alto'}
        prediccion_riesgo = mapeo_riesgo[prediccion_numerica]
        st.subheader(f"El riesgo predicho para el solicitante es: {prediccion_riesgo}")
        probabilidades = modelo_cargado.predict_proba(df_nuevo_solicitante_final)[0]
        st.write("Probabilidades:")
        st.write(f"Bajo Riesgo: {probabilidades[0]:.4f}")
        st.write(f"Riesgo Medio: {probabilidades[1]:.4f}")
        st.write(f"Alto Riesgo: {probabilidades[2]:.4f}")
    except Exception as e:
        st.error(f"Error al realizar la predicción: {e}")
        st.stop()

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

    # --- Añadimos los valores de las variables preprocesadas ---
    st.subheader("Valores de Variables Preprocesadas del Solicitante:")
    for nombre_col in df_nuevo_solicitante_final.columns:
        valor = df_nuevo_solicitante_final[nombre_col].iloc[0]
        st.write(f"{nombre_col}: {valor:.4f}")
