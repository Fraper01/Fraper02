import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import TomekLinks
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import StratifiedKFold
from io import StringIO
from sklearn.tree import _tree  # Importar para obtener información del árbol

# --- Cargar archivos y definir columnas ---
ruta_nombres_preprocesadas = 'nombres_caracteristicas_preprocesadas_arbol.joblib'
ruta_modelo = 'best_pipeline_arbol_decision_riesgo_financiero.joblib'
ruta_x_train = 'X_train_riesgo_financiero_arbol.joblib'
ruta_y_train = 'y_train_riesgo_financiero_arbol.joblib'

try:
    nombres_esperados = joblib.load(ruta_nombres_preprocesadas)
    modelo_cargado = joblib.load(ruta_modelo)
    X_train = joblib.load(ruta_x_train)
    y_train = joblib.load(ruta_y_train)
except FileNotFoundError as e:
    st.error(f"Error: No se encontró uno de los archivos requeridos: {e}")
    st.stop()

continuas_orig = ['Ingreso', 'Puntaje de Crédito', 'Monto del Préstamo',
                    'Relación Deuda-Ingreso', 'Valor de Activos', 'Incumplimientos Previos']
discretas_orig = ['Edad', 'Años en el Empleo Actual',
                    'Número de Dependientes']
categorico_orig = ['Género', 'Nivel Educativo', 'Estado Civil', 'Propósito del Préstamo',
                    'Situación Laboral', 'Historial de Pagos', 'Cambio de Estado Civil']

nuevo_solicitante_input = {}

st.title("Evaluación de Riesgos Crediticios")
st.markdown("Fundación Somo F5 https://www.somosf5.org/")
st.markdown("Elaborado: <Fia> Menos dudas. Más Precisión (Árbol de Decisión)")

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
nuevo_solicitante_input['Número de Dependientes'] = st.number_input('Número de Dependientes', value=7)  # Cambiado a 7
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
        df_nuevo_solicitante_preprocesado = df_nuevo_solicitante_original.copy()

        # Cargar escaladores y encoder
        scaler_continuas = joblib.load('scaler_continuas_arbol.joblib')
        scaler_discretas = joblib.load('scaler_discretas_arbol.joblib')
        encoder_categoricas = joblib.load('encoder_categoricas_arbol.joblib')

        # Escalar variables continuas y discretas
        df_nuevo_solicitante_preprocesado[continuas_orig] = scaler_continuas.transform(df_nuevo_solicitante_preprocesado[continuas_orig])
        df_nuevo_solicitante_preprocesado[discretas_orig] = scaler_discretas.transform(df_nuevo_solicitante_preprocesado[discretas_orig])

        # Codificar variables categóricas
        encoded_categoricas = encoder_categoricas.transform(df_nuevo_solicitante_preprocesado[categorico_orig])
        encoded_feature_names = encoder_categoricas.get_feature_names_out(categorico_orig)
        df_encoded = pd.DataFrame(encoded_categoricas, columns=encoded_feature_names, index=df_nuevo_solicitante_preprocesado.index)

        df_nuevo_solicitante_preprocesado = pd.concat([df_nuevo_solicitante_preprocesado.drop(categorico_orig, axis=1), df_encoded], axis=1)

        df_nuevo_solicitante_final = df_nuevo_solicitante_preprocesado[nombres_esperados]


    except Exception as e:
        st.error(f"Error durante el preprocesamiento: {e}")
        st.stop()

    # --- Predicción ---
    try:
        # Obtener el árbol de decisión del pipeline
        arbol_decision = modelo_cargado.named_steps['decisiontreeclassifier']
        feature_names = nombres_esperados
        class_names = ['Bajo', 'Medio', 'Alto']

        def predict_with_path(tree, sample, feature_names, class_names):
            """
            Predice la clase de una muestra recorriendo el árbol de decisión,
            y devuelve el nombre de la clase correspondiente a la hoja alcanzada.

            Args:
                tree: El objeto DecisionTreeClassifier.tree_.
                sample: La muestra de datos preprocesada (array numpy).
                feature_names: Lista de nombres de las características.
                class_names: Lista de nombres de las clases.

            Returns:
                El nombre de la clase predicha (string).
            """
            node_id = 0
            while True:
                # Si es un nodo hoja, obtener la clase y retornar
                if tree.children_left[node_id] == tree.children_right[node_id]:
                    class_index = np.argmax(tree.value[node_id])
                    return class_names[class_index]
                # Si no es hoja, decidir izquierda o derecha
                feature_index = tree.feature[node_id]
                threshold = tree.threshold[node_id]
                if sample[feature_index] <= threshold: # Corrección:  sample[feature_index]
                    node_id = tree.children_left[node_id]
                else:
                    node_id = tree.children_right[node_id]

        # Predecir usando la función de recorrido del árbol
        nuevo_solicitante_array = df_nuevo_solicitante_final.values
        prediccion_riesgo = predict_with_path(arbol_decision.tree_, nuevo_solicitante_array[0], feature_names, class_names) # Cambio aquí
        # nuevo_solicitante_array es un array 2D.  Necesitamos pasarle una sola muestra (1D) a predict_with_path
        st.subheader(f"El riesgo predicho para el solicitante es: {prediccion_riesgo}")

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

    # --- Visualización del árbol de decisión ---
    st.subheader("Visualización del Árbol de Decisión:")
    try:
        # Obtener el árbol de decisión del pipeline
        arbol_decision = modelo_cargado.named_steps['decisiontreeclassifier']
        feature_names = nombres_esperados
        class_names = ['Bajo', 'Medio', 'Alto']

        # Función para imprimir el camino de la decisión
        def get_decision_path(decision_tree, sample, feature_names, class_names):
            """
            Obtiene el camino de decisión seguido por una muestra a través del árbol.

            Args:
                decision_tree: El objeto DecisionTreeClassifier entrenado.
                sample: La muestra de datos para la cual se quiere el camino.
                feature_names: Lista de nombres de las características.
                class_names: Lista de nombres de las clases objetivo.

            Returns:
                Una lista de strings, donde cada string describe un paso en el camino de la decisión.
            """
            tree = decision_tree.tree_
            node_indicator = tree.decision_path(sample.astype(np.float32))
            branch_index = node_indicator.indices[node_indicator.indptr[0]:node_indicator.indptr[1]]

            path_description = []
            for node_id in branch_index:
                # Si el nodo es un nodo hoja, no hay decisión
                if tree.children_left[node_id] == tree.children_right[node_id]:
                    # Obtener la clase predicha en la hoja
                    clase_hoja_index = np.argmax(tree.value[node_id])
                    clase_hoja = class_names[clase_hoja_index]
                    path_description.append(f"Llegó a la hoja (Nodo: {node_id}, Clase: {clase_hoja})")  # Agregar Nodo ID
                else:
                    # Feature para la división
                    feature_name = feature_names[tree.feature[node_id]]
                    threshold = tree.threshold[node_id]
                    # Ir a la izquierda o a la derecha
                    if sample[0, tree.feature[node_id]] <= threshold:
                        direction = "izquierda"
                        symbol = "<="
                    else:
                        direction = "derecha"
                        symbol = ">"
                    path_description.append(f"Nodo {node_id}: {feature_name} {symbol} {threshold:.2f}, ir a la {direction}")
            return path_description

        # Obtener el camino de decisión para el nuevo solicitante
        nuevo_solicitante_array = df_nuevo_solicitante_final.values
        decision_path = get_decision_path(arbol_decision, nuevo_solicitante_array, feature_names, class_names)

        # Mostrar el camino de decisión en Streamlit
        st.subheader("Camino de Decisión del Solicitante:")
        for step in decision_path:
            st.write(f"- {step}")

        # Visualización completa del árbol
        st.markdown("Árbol de Decisión Completo:")
        plt.figure(figsize=(20, 10))
        plot_tree(arbol_decision, filled=True, feature_names=feature_names, class_names=class_names, max_depth=4)
        plt.tight_layout()
        st.pyplot(plt.gcf())

        # Visualización del árbol truncado a 2 niveles
        st.markdown("Árbol de Decisión (Truncado a 2 niveles):")
        plt.figure(figsize=(20, 10))
        plot_tree(arbol_decision, filled=True, feature_names=feature_names, class_names=class_names, max_depth=2)
        plt.tight_layout()
        st.pyplot(plt.gcf())

    except Exception as e:
        st.error(f"Error al visualizar el árbol de decisión: {e}")
