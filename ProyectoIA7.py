import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, f1_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

# Fase 1. Cargar el Dataset
data = pd.read_csv('data_seleccionada.csv')

# Fase 2: Limpieza de los Datos (manteniendo tus funciones)
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

# Fase 4: División de Datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Fase 5: Identificar columnas numéricas y categóricas
numeric_cols = X_train.select_dtypes(include=np.number).columns
categorical_cols = X_train.select_dtypes(include='object').columns

# Fase 6: Aplicar SMOTE SOLO a las características numéricas del conjunto de entrenamiento
smote = SMOTE(random_state=42)
X_train_numeric = X_train[numeric_cols]
y_train_smote = y_train
X_train_numeric_smote, y_train_smote = smote.fit_resample(X_train_numeric, y_train)

# Fase 7: Crear DataFrames para las características numéricas sobremuestreadas y las categóricas originales
X_train_numeric_smote_df = pd.DataFrame(X_train_numeric_smote, columns=numeric_cols)
X_train_categorical = X_train[categorical_cols].reset_index(drop=True)

# Fase 8: Concatenar las características numéricas sobremuestreadas con las categóricas originales
X_train_smote_full = pd.concat([X_train_numeric_smote_df, X_train_categorical], axis=1)

# Fase 9: Preprocesamiento
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', drop='first'), categorical_cols)])

X_train_processed_smote = preprocessor.fit_transform(X_train_smote_full)
X_test_processed = preprocessor.transform(X_test)

# Fase 10: Definir el modelo KNN y los parámetros para GridSearchCV
knn = KNeighborsClassifier(weights='uniform') # Mantenemos weights='uniform'
param_grid = {'n_neighbors': range(1, 21)} # Probaremos diferentes valores de n_neighbors

# Fase 11: Realizar la búsqueda de cuadrícula con validación cruzada
grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='f1_weighted') # Usamos F1-score ponderado
grid_search.fit(X_train_processed_smote, y_train_smote)

# Fase 12: Obtener el mejor modelo y sus parámetros
best_knn = grid_search.best_estimator_
best_params = grid_search.best_params_
print(f"Mejores parámetros encontrados por GridSearchCV: {best_params}")

# Fase 13: Evaluar el mejor modelo en el conjunto de prueba
y_pred_best = best_knn.predict(X_test_processed)
print("\nReporte de Clasificación en el conjunto de prueba (con SMOTE y GridSearchCV):\n", classification_report(y_test, y_pred_best))
print("Precisión en el conjunto de prueba (con SMOTE y GridSearchCV):", accuracy_score(y_test, y_pred_best))
print("\nMatriz de Confusión en el conjunto de prueba (con SMOTE y GridSearchCV):\n", confusion_matrix(y_test, y_pred_best))

# Fase 14: Evaluar el mejor modelo en el conjunto de entrenamiento sobremuestreado
y_train_pred_best = best_knn.predict(X_train_processed_smote)
print("\nReporte de Clasificación en el conjunto de entrenamiento (con SMOTE y GridSearchCV):\n", classification_report(y_train_smote, y_train_pred_best))
print("Precisión en el conjunto de entrenamiento (con SMOTE y GridSearchCV):", accuracy_score(y_train_smote, y_train_pred_best))
print("\nMatriz de Confusión en el conjunto de entrenamiento (con SMOTE y GridSearchCV):\n", confusion_matrix(y_train_smote, y_train_pred_best))