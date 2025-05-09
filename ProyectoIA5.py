import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Fase 1. Cargar el Dataset
#data = pd.read_csv('data_seleccionada.csv')
data = pd.read_csv('data_mas_aumentada.csv')

# Fase 2: Limpieza de los Datos (las funciones clean_edad y limpiar_categorica)
def clean_edad(edad):
    if isinstance(edad, str):
        edad = ''.join(filter(str.isdigit, edad))
        return int(edad) if edad else np.nan
    return edad

def limpiar_categorica(data, columna, mapeo_estandares, mapeo_abreviaturas=None, caracteres_invalidos=None):
    data[columna] = data[columna].str.strip().str.title()
    for patron, estandar in mapeo_estandares.items():
        data[columna] = data[columna].str.replace(patron, estandar, regex=True)
    if mapeo_abreviaturas:
        abreviaturas_regex = r'\b(' + '|'.join(re.escape(abreviatura) for abreviatura in mapeo_abreviaturas.keys()) + r')\b'
        data[columna] = data[columna].str.replace(abreviaturas_regex, lambda x: mapeo_abreviaturas[x.group(0)], regex=True)
    data[columna] = data[columna].str.replace(r' +', ' ', regex=True)
    return data[columna]

estado_civil_mapeo = {r'\bSol(?:tero)?\b': 'Soltero', r'\bCas(?:ado)?(?:\s?\(?C\)?)?\b': 'Casado', r'\bDiv(?:orciado)?(?:-)?\b': 'Divorciado', r'\bVi(?:udo)?(?:\+)?\b': 'Viudo', r'\bS\b': 'Soltero', r'\bC\b': 'Casado', r'\bD\b': 'Divorciado', r'\bV\b': 'Viudo'}
situacion_laboral_mapeo = {r'\bEmp(?:leado)?\b': 'Empleado', r'\bDesemp(?:leado)?\b': 'Desempleado', r'\bAut(?:ónomo)?\b': 'Autónomo', r'\bEmp\.\b': 'Empleado', r'\bDesemp\.\b': 'Desempleado', r'\bAut\.\b': 'Autónomo'}
nivel_educativo_mapeo = {r'\bSec(?:undario)?\b': 'Secundario', r'\bUniv(?:ersitario)?\b': 'Universitario', r'\bBach(?:illerato)?\b': 'Secundario', r'\bLic(?:enciado)?\b': 'Universitario', r'\bGrad(?:uado)?\b': 'Universitario', r'\bMaster\b': 'Universitario', r'\bPhD\b': 'Universitario'}

data['Edad'] = data['Edad'].apply(clean_edad).astype(int).fillna(data['Edad'].median())
data['Ingresos mensuales'] = data['Ingresos mensuales'].round(2).fillna(data['Ingresos mensuales'].median())
data['Porcentaje de endeudamiento'] = data['Porcentaje de endeudamiento'].fillna(data['Porcentaje de endeudamiento'].median())
data['Dependientes'] = data['Dependientes'].fillna(data['Dependientes'].median() if data['Dependientes'].nunique() < 20 and pd.api.types.is_numeric_dtype(data['Dependientes']) else data['Dependientes'].mode()[0])
data['Situación Laboral'] = data['Situación Laboral'].str.strip().str.title().replace(r'\b(' + '|'.join(re.escape(ab) for ab in situacion_laboral_mapeo) + r')\b', lambda x: situacion_laboral_mapeo[x.group(0)], regex=True).replace(r' +', ' ', regex=True).fillna(data['Situación Laboral'].mode()[0] if not data['Situación Laboral'].value_counts().empty else '')
data['Nivel Educativo'] = data['Nivel Educativo'].str.strip().str.title().fillna(data['Nivel Educativo'].mode()[0] if not data['Nivel Educativo'].value_counts().empty else '')
data['Estado Civil'] = limpiar_categorica(data, 'Estado Civil', estado_civil_mapeo).fillna(data['Estado Civil'].mode()[0] if not data['Estado Civil'].value_counts().empty else '')
data['Provincias'] = data['Provincias'].str.strip().str.title().fillna(data['Provincias'].mode()[0] if not data['Provincias'].value_counts().empty else '')
data['Calificación de Riesgo'] = data['Calificación de Riesgo'].fillna(data['Calificación de Riesgo'].mode()[0] if not data['Calificación de Riesgo'].value_counts().empty else '')

# Fase 3: Separación de Características y Variable Objetivo
X = data.drop('Calificación de Riesgo', axis=1)
y = data['Calificación de Riesgo']

# Fase 4: División de Datos (ANTES del preprocesamiento dentro del pipeline)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Fase 5: Preprocesamiento
numeric_cols = X_train.select_dtypes(include=np.number).columns.tolist()
categorical_cols = ['Situación Laboral', 'Nivel Educativo', 'Estado Civil', 'Provincias']

# Crear transformadores
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore', drop='first') # drop='first' para evitar multicolinealidad

# Crear el preprocesador
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)])

# Fase 6: Entrenamiento del Modelo KNN con Pipeline
knn = KNeighborsClassifier(n_neighbors=8)

pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', knn)])

pipeline.fit(X_train, y_train)

# Fase 7: Evaluación del Modelo
y_pred = pipeline.predict(X_test)
print("Reporte de Clasificación en el conjunto de prueba:\n", classification_report(y_test, y_pred))
print("Precisión en el conjunto de prueba:", accuracy_score(y_test, y_pred))
print("\nMatriz de Confusión en el conjunto de prueba:\n", confusion_matrix(y_test, y_pred))

y_train_pred = pipeline.predict(X_train)
print("\nReporte de Clasificación en el conjunto de entrenamiento:\n", classification_report(y_train, y_train_pred))
print("Precisión en el conjunto de entrenamiento:", accuracy_score(y_train, y_train_pred))
print("\nMatriz de Confusión en el conjunto de entrenamiento:\n", confusion_matrix(y_train, y_train_pred))

# Fase 8: Validación Cruzada (usando el pipeline completo)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
f1_scores_cv = cross_val_score(pipeline, X, y, cv=cv, scoring='f1_weighted')
print(f"\nF1-score promedio en validación cruzada: {np.mean(f1_scores_cv):.4f}")

"""

# Fase 9: Simulación de un nuevo solicitante (aplicando el preprocesamiento del pipeline)
nuevo_solicitante = {
    'Edad': 20.0, 'Ingresos mensuales': 500.0, 'Dependientes': 4.0, 'Porcentaje de endeudamiento': 0.45,
    'Situación Laboral': 'Estudiante', 'Nivel Educativo': 'Universitario', 'Estado Civil': 'Soltero', 'Provincias': 'Madrid'
}
nuevo_solicitante_df = pd.DataFrame([nuevo_solicitante])

prediccion = pipeline.predict(nuevo_solicitante_df)
print("\nPredicción del nivel de riesgo para el nuevo solicitante:", prediccion)

# Fase 10: Guardar el modelo y el preprocesador
joblib.dump(pipeline, 'pipeline_knn.joblib')
print("Pipeline KNN (con preprocesador) guardado como pipeline_knn.joblib")
"""