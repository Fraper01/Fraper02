import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances
import altair as alt

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

ruta_x_train = 'X_train_riesgo_financiero.joblib'
ruta_y_train = 'y_train_riesgo_financiero.joblib'
try:
    X_train = joblib.load(ruta_x_train)
    y_train = joblib.load(ruta_y_train)
except FileNotFoundError:
    st.error(f"Error: No se encontró el archivo X_train o y_train. Asegúrese de que los archivos estén en la ubicación correcta.")
    st.stop()

continuas_orig = ['Ingreso', 'Puntaje de Crédito', 'Monto del Préstamo',
                    'Relación Deuda-Ingreso', 'Valor de Activos', 'Incumplimientos Previos']
discretas_orig = ['Edad', 'Años en el Empleo Actual',
                    'Número de Dependientes']
categorico_orig = ['Género', 'Nivel Educativo', 'Estado Civil', 'Propósito del Préstamo',
                    'Situación Laboral', 'Historial de Pagos', 'Cambio de Estado Civil']

nuevo_solicitante_input = {}

st.title("Evaluación de Riesgos Crediticios")
st.markdown("Fundación Somo F5 https://www.somosf5.org/")  # Reemplaza con el nombre real
st.markdown("Elaborado: <Fia> Menos dudas. Más Precisión (knn)")  # Reemplaza con los nombres reales

st.write("Ingrese los datos del solicitante:")

# --- Widgets de entrada (igual que antes) ---
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
nuevo_solicitante_input['Cambio de Estado Civil'] = st.selectbox('Incuplimientos Anteriores', [0, 1, 2], index=1)

if st.button("Predecir Riesgo"):
    # --- Crear DataFrame del nuevo solicitante ---
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

    # --- Preprocesamiento ---
    try:
        # Asegurar que el preprocesamiento se alinee con el entrenamiento
        df_nuevo_solicitante_preprocesado = df_nuevo_solicitante_original.copy()
        
        # Estas operaciones deben realizarse en el mismo orden y con los mismos parámetros
        # que se usaron durante el entrenamiento del modelo.
        
        # Cargar escaladores y encoder
        scaler_continuas = joblib.load('scaler_continuas.joblib')
        scaler_discretas = joblib.load('scaler_discretas.joblib')
        encoder_categoricas = joblib.load('encoder_categoricas.joblib')
        
        # Mostrar los datos de entrada antes del preprocesamiento
        #st.subheader("Datos de entrada del solicitante (originales):")
        #st.write(df_nuevo_solicitante_original)
        
        # Escalar variables continuas y discretas
        df_nuevo_solicitante_preprocesado[continuas_orig] = scaler_continuas.transform(df_nuevo_solicitante_preprocesado[continuas_orig])
        df_nuevo_solicitante_preprocesado[discretas_orig] = scaler_discretas.transform(df_nuevo_solicitante_preprocesado[discretas_orig])
        
        # Codificar variables categóricas
        encoded_categoricas = encoder_categoricas.transform(df_nuevo_solicitante_preprocesado[categorico_orig])
        encoded_feature_names = encoder_categoricas.get_feature_names_out(categorico_orig)
        df_encoded = pd.DataFrame(encoded_categoricas, columns=encoded_feature_names, index=df_nuevo_solicitante_preprocesado.index)
        
        # Mostrar las variables categóricas codificadas
        #st.subheader("Variables categóricas codificadas:")
        #st.write(df_encoded)
        
        df_nuevo_solicitante_preprocesado = pd.concat([df_nuevo_solicitante_preprocesado.drop(categorico_orig, axis=1), df_encoded], axis=1)
        
        # Mostrar los datos despues del preprocesamiento
        #st.subheader("Datos de entrada del solicitante (preprocesados):")
        #st.write(df_nuevo_solicitante_preprocesado)

        df_nuevo_solicitante_final = df_nuevo_solicitante_preprocesado[nombres_esperados]
        
    except Exception as e:
        st.error(f"Error durante el preprocesamiento: {e}")
        st.stop()

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

    # --- Interpretación de la Predicción ---
    st.subheader("Interpretación de la Predicción:")
    if prediccion_riesgo == 'Bajo':
        st.write("El modelo predice que este solicitante tiene un bajo riesgo de incumplimiento en el préstamo.")
    elif prediccion_riesgo == 'Medio':
        st.write("El modelo predice que este solicitante tiene un riesgo moderado de incumplimiento en el préstamo.")
    else:
        st.write("El modelo predice que este solicitante tiene un alto riesgo de incumplimiento en el préstamo.")

    # Mostrar los datos despues del preprocesamiento
    st.subheader("Datos de entrada del solicitante:")
    st.write(df_nuevo_solicitante_preprocesado)

    # --- Análisis de Vecinos ---
    st.subheader("Análisis de Vecinos Cercanos:")
    try:
        distancias = pairwise_distances(df_nuevo_solicitante_final, X_train, metric='euclidean')
        indices_vecinos_cercanos = np.argsort(distancias)[0][:5]
        vecinos_cercanos = X_train.iloc[indices_vecinos_cercanos]
        etiquetas_vecinos_cercanos = y_train.iloc[indices_vecinos_cercanos]

        st.write("Los 5 vecinos más cercanos en el conjunto de entrenamiento son:")
        st.write(vecinos_cercanos)
        #st.write("Etiquetas de riesgo de los vecinos cercanos:")
        #st.write(etiquetas_vecinos_cercanos.map({0: 'Bajo', 1: 'Medio', 2: 'Alto'}))

        distribucion_etiquetas = etiquetas_vecinos_cercanos.value_counts()
        total_vecinos = distribucion_etiquetas.sum()
        #st.write("Distribución de etiquetas de riesgo:")
        #for etiqueta, frecuencia in distribucion_etiquetas.items():
        #    porcentaje = (frecuencia / total_vecinos) * 100
        #    st.write(f"{etiqueta} ({mapeo_riesgo[etiqueta]}): {frecuencia} ({porcentaje:.2f}%)")

        # Visualización de Vecinos Cercanos
        #st.subheader("Visualización de Vecinos Cercanos en el Espacio de Características Preprocesado")
        
        # Asegurarse de que df_nuevo_solicitante_final tenga las mismas columnas que X_train
        #if set(df_nuevo_solicitante_final.columns) == set(X_train.columns):
            # Combinar los datos del solicitante y los vecinos para la visualización
            #datos_visualizacion = pd.concat([df_nuevo_solicitante_final, vecinos_cercanos])
            
            # Añadir una columna para distinguir el solicitante de los vecinos
            #datos_visualizacion['Tipo'] = ['Solicitante'] * len(df_nuevo_solicitante_final) + ['Vecino'] * len(vecinos_cercanos)
            
            # Seleccionar dos características para la visualización (puedes cambiar esto)
            #
            
            #if len(X_train.columns) > 1:
                
            #    feature_x = X_train.columns[0]
            #    feature_y = X_train.columns[1]
                
                # Crear el gráfico de dispersión
            #    chart = alt.Chart(datos_visualizacion).mark_circle().encode(
            #        x=alt.X(feature_x, title=feature_x),
            #        y=alt.Y(feature_y, title=feature_y),
            #        color='Tipo',  # Diferenciar solicitante y vecinos por color
            #        tooltip=[feature_x, feature_y, 'Tipo']  # Información al pasar el ratón
            #    ).properties(
            #        title='Solicitante y sus Vecinos Cercanos'
            #    ).interactive()  # Permitir zoom y desplazamiento
                
                # Mostrar el gráfico en Streamlit
                #st.altair_chart(chart, use_container_width=True)
            #else:
            #    st.warning("El conjunto de datos tiene solo una característica. No se puede crear un gráfico de dispersión bidimensional.")
            #
        #else:
        #    st.error("Error: Las columnas del solicitante preprocesado no coinciden con las columnas del conjunto de entrenamiento.")

    except Exception as e:
        st.error(f"Error al analizar los vecinos cercanos: {e}")

    # --- Añadimos los valores de las variables preprocesadas ---
    #st.subheader("Valores de Variables Preprocesadas del Solicitante:")
    #for nombre_col in df_nuevo_solicitante_final.columns:
    #    valor = df_nuevo_solicitante_final[nombre_col].iloc[0]
    #    st.write(f"{nombre_col}: {valor:.4f}")
