import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier  # Importar DecisionTreeClassifier
from sklearn.pipeline import Pipeline
import joblib
import warnings
warnings.filterwarnings("ignore")

# Importar SMOTE y TomekLinks desde imblearn
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import TomekLinks
from imblearn.pipeline import make_pipeline  # Importar make_pipeline de imblearn


# Cargar los datos
df = pd.read_csv('financial_risk_assessment.csv')

# Diccionario de traducción de columnas al español
nombres_es = {
    'Age': 'Edad',
    'Gender': 'Género',
    'Education Level': 'Nivel Educativo',
    'Marital Status': 'Estado Civil',
    'Income': 'Ingreso',
    'Credit Score': 'Puntaje de Crédito',
    'Loan Amount': 'Monto del Préstamo',
    'Loan Purpose': 'Propósito del Préstamo',
    'Employment Status': 'Situación Laboral',
    'Years at Current Job': 'Años en el Empleo Actual',
    'Payment History': 'Historial de Pagos',
    'Debt-to-Income Ratio': 'Relación Deuda-Ingreso',
    'Assets Value': 'Valor de Activos',
    'Number of Dependents': 'Número de Dependientes',
    'City': 'Ciudad',
    'State': 'Estado',
    'Country': 'País',
    'Previous Defaults': 'Incumplimientos Previos',
    'Marital Status Change': 'Cambio de Estado Civil',
    'Risk Rating': 'Calificación de Riesgo'
}

# Renombrar columnas
df.rename(columns=nombres_es, inplace=True)

# Eliminar filas con valores nulos
df = df.dropna()

# Definir las columnas de características
continuas = ['Ingreso', 'Puntaje de Crédito', 'Monto del Préstamo',
             'Relación Deuda-Ingreso', 'Valor de Activos', 'Incumplimientos Previos']
discretas = ['Edad', 'Años en el Empleo Actual',
             'Número de Dependientes']
categorico = ['Género', 'Nivel Educativo', 'Estado Civil', 'Propósito del Préstamo',
              'Situación Laboral', 'Historial de Pagos', 'Cambio de Estado Civil']

# Separar las características y la variable objetivo
X = df[continuas + discretas + categorico]
y = df['Calificación de Riesgo'].map({'Low': 0, 'Medium': 1, 'High': 2})  # Codificar la variable objetivo



# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Preprocesamiento de las características
preprocessor = ColumnTransformer(transformers=[
    ('cont', MinMaxScaler(), continuas),
    ('disc', StandardScaler(), discretas),
    ('cat', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), categorico)
])

# Preprocesar los datos de entrenamiento y prueba por separado
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Obtener los nombres de las columnas después del OneHotEncoding
feature_names = list(preprocessor.transformers_[0][2]) + \
                list(preprocessor.transformers_[1][2]) + \
                list(preprocessor.transformers_[2][1].get_feature_names_out(categorico))

# Convertir los datos preprocesados a DataFrame
X_train_df = pd.DataFrame(X_train_processed, columns=feature_names)
X_test_df = pd.DataFrame(X_test_processed, columns=feature_names)


# Guardar los nombres de las características preprocesadas
joblib.dump(feature_names, 'nombres_caracteristicas_preprocesadas_arbol.joblib') # Cambiado el nombre del archivo
# Guardar los DataFrames de entrenamiento y prueba preprocesados
joblib.dump(X_train_df, 'X_train_riesgo_financiero_arbol.joblib') # Cambiado el nombre del archivo
joblib.dump(X_test_df, 'X_test_riesgo_financiero_arbol.joblib')   # Cambiado el nombre del archivo

# Guardar las etiquetas de entrenamiento y prueba
joblib.dump(y_train, 'y_train_riesgo_financiero_arbol.joblib')     # Cambiado el nombre del archivo
joblib.dump(y_test, 'y_test_riesgo_financiero_arbol.joblib')       # Cambiado el nombre del archivo

# Guardar los objetos de preprocesamiento
joblib.dump(preprocessor.named_transformers_['cont'], 'scaler_continuas_arbol.joblib')   # Cambiado el nombre del archivo
joblib.dump(preprocessor.named_transformers_['disc'], 'scaler_discretas_arbol.joblib')   # Cambiado el nombre del archivo
joblib.dump(preprocessor.named_transformers_['cat'], 'encoder_categoricas_arbol.joblib') # Cambiado el nombre del archivo

# Guardar los datos preprocesados para el análisis en la interfaz
joblib.dump(X_train_processed, 'X_train_arbol.joblib')
joblib.dump(X_test_processed, 'X_test_arbol.joblib')
joblib.dump(y_train, 'y_train_arbol.joblib')
joblib.dump(y_test, 'y_test_arbol.joblib')

# Definir el pipeline SMOTETomek con Árbol de Decisión
best_pipeline = make_pipeline(
    StandardScaler(),
    SMOTE(random_state=42),  # Sobremuestrear con SMOTE
    TomekLinks(),          # Submuestrear con TomekLinks
    DecisionTreeClassifier(random_state=42)  # Usar DecisionTreeClassifier
)

# Validación cruzada estratificada
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Entrenar el modelo
best_pipeline.fit(X_train_df, y_train)

# Guardar el modelo entrenado (el pipeline completo)
joblib.dump(best_pipeline, 'best_pipeline_arbol_decision_riesgo_financiero.joblib') # Cambiado el nombre del archivo

print("Modelo de árbol de decisión entrenado y guardado exitosamente. Grupo 4")
