import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns

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

# Fase 5: Preprocesamiento
numeric_cols = X_train.select_dtypes(include=np.number).columns.tolist()
categorical_cols = ['Situación Laboral', 'Nivel Educativo', 'Estado Civil', 'Provincias']

numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore', drop='first')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)])

# Fase 6: Búsqueda de n_neighbors
n_neighbors_values = range(1, 21)
f1_scores = []

for n in n_neighbors_values:
    knn = KNeighborsClassifier(n_neighbors=n)
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('classifier', knn)])
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='f1_weighted')
    f1_scores.append(np.mean(scores))

# Fase 7: Visualización de los resultados
plt.figure(figsize=(10, 6))
plt.plot(n_neighbors_values, f1_scores, marker='o')
plt.title('F1-score vs. Número de Vecinos (n_neighbors)')
plt.xlabel('Número de Vecinos (n_neighbors)')
plt.ylabel('F1-score Promedio (Validación Cruzada)')
plt.xticks(n_neighbors_values)
plt.grid(True)
plt.show()

# Fase 8: Identificar el mejor n_neighbors
best_n_neighbors = n_neighbors_values[np.argmax(f1_scores)]
print(f"\nEl mejor valor de n_neighbors encontrado mediante validación cruzada es: {best_n_neighbors}")

# Fase 9: Entrenar el modelo final con el mejor n_neighbors
best_knn = KNeighborsClassifier(n_neighbors=best_n_neighbors)
best_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('classifier', best_knn)])
best_pipeline.fit(X_train, y_train)

# Fase 10: Evaluar el modelo final en el conjunto de prueba
y_pred_best = best_pipeline.predict(X_test)
print("\nReporte de Clasificación en el conjunto de prueba (con el mejor n_neighbors):\n", classification_report(y_test, y_pred_best))
print("Precisión en el conjunto de prueba (con el mejor n_neighbors):", accuracy_score(y_test, y_pred_best))
print("\nMatriz de Confusión en el conjunto de prueba (con el mejor n_neighbors):\n", confusion_matrix(y_test, y_pred_best))