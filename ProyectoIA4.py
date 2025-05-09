import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, pairwise_distances

# Fase 1. Cargar el Dataset
data = pd.read_csv('data_seleccionada.csv')

# Fase 2: Limpieza de los Datos
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

estado_civil_mapeo = {
    r'\bSol(?:tero)?\b': 'Soltero', 
    r'\bCas(?:ado)?(?:\s?\(?C\)?)?\b': 'Casado', 
    r'\bDiv(?:orciado)?(?:-)?\b': 'Divorciado', 
    r'\bVi(?:udo)?(?:\+)?\b': 'Viudo', 
    r'\bS\b': 'Soltero', 
    r'\bC\b': 'Casado', 
    r'\bD\b': 'Divorciado', 
    r'\bV\b': 'Viudo'}
situacion_laboral_mapeo = {
    r'\bEmp(?:leado)?\b': 'Empleado',
    r'\bDesemp(?:leado)?\b': 'Desempleado',
    r'\bAut(?:ónomo)?\b': 'Autónomo',
    r'\bEmp\.\b': 'Empleado',  # Por si acaso hay abreviaturas
    r'\bDesemp\.\b': 'Desempleado',
    r'\bAut\.\b': 'Autónomo'
}
nivel_educativo_mapeo = {
    r'\bSec(?:undario)?\b': 'Secundario',
    r'\bUniv(?:ersitario)?\b': 'Universitario',
    r'\bBach(?:illerato)?\b': 'Secundario',  # Considerar Bachillerato como Secundario
    r'\bLic(?:enciado)?\b': 'Universitario', # Considerar Licenciado como Universitario
    r'\bGrad(?:uado)?\b': 'Universitario',   # Considerar Graduado como Universitario
    r'\bMaster\b': 'Universitario',
    r'\bPhD\b': 'Universitario'
}

data['Edad'] = data['Edad'].apply(clean_edad).astype(int).fillna(data['Edad'].median())
data['Ingresos mensuales'] = data['Ingresos mensuales'].round(2).fillna(data['Ingresos mensuales'].median())
data['Porcentaje de endeudamiento'] = data['Porcentaje de endeudamiento'].fillna(data['Porcentaje de endeudamiento'].median())
data['Dependientes'] = data['Dependientes'].fillna(data['Dependientes'].median() if data['Dependientes'].nunique() < 20 and pd.api.types.is_numeric_dtype(data['Dependientes']) else data['Dependientes'].mode()[0])

data['Situación Laboral'] = data['Situación Laboral'].str.strip().str.title().replace(r'\b(' + '|'.join(re.escape(ab) for ab in situacion_laboral_mapeo) + r')\b', lambda x: situacion_laboral_mapeo[x.group(0)], regex=True).replace(r' +', ' ', regex=True).fillna(data['Situación Laboral'].mode()[0] if not data['Situación Laboral'].value_counts().empty else '')
data['Nivel Educativo'] = data['Nivel Educativo'].str.strip().str.title().fillna(data['Nivel Educativo'].mode()[0] if not data['Nivel Educativo'].value_counts().empty else '')
data['Estado Civil'] = limpiar_categorica(data, 'Estado Civil', estado_civil_mapeo).fillna(data['Estado Civil'].mode()[0] if not data['Estado Civil'].value_counts().empty else '')
data['Provincias'] = data['Provincias'].str.strip().str.title().fillna(data['Provincias'].mode()[0] if not data['Provincias'].value_counts().empty else '')
data['Calificación de Riesgo'] = data['Calificación de Riesgo'].fillna(data['Calificación de Riesgo'].mode()[0] if not data['Calificación de Riesgo'].value_counts().empty else '')

data = pd.get_dummies(data, columns=['Situación Laboral', 'Nivel Educativo', 'Estado Civil', 'Provincias'], drop_first=True)

# Fase 4 Escalado de Caracteristicas KNN
numeric_cols = data.select_dtypes(include=np.number).columns.tolist()
if 'Calificación de Riesgo' in numeric_cols:
    numeric_cols.remove('Calificación de Riesgo')

scaler = StandardScaler()
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

X = data.drop('Calificación de Riesgo', axis=1)
y = data['Calificación de Riesgo']

# Fase 5 División de Datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Fase 6 Entrenamiento del Modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Escalar el conjunto de entrenamiento DESPUÉS de dividirlo
X_train_scaled = X_train.copy()
X_train_scaled[numeric_cols] = scaler.transform(X_train[numeric_cols]) # Usamos solo transform aquí

# Fase 7 Evaluación del Modelo
y_pred = knn.predict(X_test)
print("Reporte de Clasificación en el conjunto de prueba:\n", classification_report(y_test, y_pred))

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
f1_scores_cv = cross_val_score(knn, X, y, cv=cv, scoring='f1_weighted')
print(f"F1-score promedio en validación cruzada: {np.mean(f1_scores_cv):.4f}")

"""

# Simulación de un nuevo solicitante
nuevo_solicitante = {
    'Edad': 20.0, 'Ingresos mensuales': 500.0, 'Dependientes': 4.0, 'Porcentaje de endeudamiento': 0.45,
    'Ocupación_Comerciante': False, 'Ocupación_Estudiante': True, 'Ocupación_Ingeniero': False, 'Ocupación_Profesor': False, 'Ocupación_Técnico': False,
    'Nivel educativo_Secundario': False, 'Nivel educativo_Universitario': True,
    'Estado civil_Soltero': False,
    'Historial crediticio_Excelente': False, 'Historial crediticio_Malo': False,
    'Provincia_Alicante': False, 'Provincia_Badajoz': False, 'Provincia_Badalona': False, 'Provincia_Barcelona': False, 'Provincia_Bilbao': False, 'Provincia_Ceuta': False, 'Provincia_Cáceres': False, 'Provincia_Córdoba': False, 'Provincia_Elche': False, 'Provincia_Gijón': False, "Provincia_L'Hospitalet de Llobregat": False, 'Provincia_Las Palmas': False, 'Provincia_Madrid': True, 'Provincia_Melilla': False, 'Provincia_Murcia': False, 'Provincia_Málaga': False, 'Provincia_Palma': False, 'Provincia_Sevilla': False, 'Provincia_Valencia': False, 'Provincia_Valladolid': False, 'Provincia_Vigo': False, 'Provincia_Vitoria-Gasteiz': False, 'Provincia_Zaragoza': False
}

nuevo_solicitante_df = pd.DataFrame([nuevo_solicitante])
nuevo_solicitante_df = nuevo_solicitante_df.reindex(columns=X_train.columns, fill_value=False)

# Escalar el nuevo solicitante usando el scaler AJUSTADO con X_train
nuevo_solicitante_scaled = scaler.transform(nuevo_solicitante_df[numeric_cols])

nuevo_solicitante_final = pd.concat([pd.DataFrame(nuevo_solicitante_scaled, columns=numeric_cols, index=[0]),
                                     nuevo_solicitante_df.drop(columns=numeric_cols, errors='ignore', axis=1)], axis=1)

# --- INSERTA LOS PRINTS AQUÍ ---
distancias = pairwise_distances(nuevo_solicitante_final, X_train_scaled)
indice_vecino_mas_cercano = np.argmin(distancias)
riesgo_vecino_mas_cercano = y_train.iloc[indice_vecino_mas_cercano]

k = knn.n_neighbors
indices_vecinos_cercanos = np.argsort(distancias)[0][:k]
riesgos_vecinos_cercanos = y_train.iloc[indices_vecinos_cercanos].values

#print(f"\n--- Análisis del Nuevo Solicitante ---")
#print(f"Índice del vecino más cercano en X_train: {indice_vecino_mas_cercano}")
#print(f"Nivel de riesgo del vecino más cercano: {riesgo_vecino_mas_cercano}")
#print(f"Índices de los {k} vecinos más cercanos en X_train: {indices_vecinos_cercanos}")
#print(f"Niveles de riesgo de los {k} vecinos más cercanos: {riesgos_vecinos_cercanos}")
#print(f"Predicción del modelo: {knn.predict(nuevo_solicitante_final)}")
#print(f"\nValores escalados del nuevo solicitante (solo numéricas):\n", nuevo_solicitante_scaled)
#print(f"Nombres de las columnas numéricas (escaladas):\n", numeric_cols)
#print(f"\nPrimeras filas de X_train_scaled:\n", X_train_scaled.head())
# --- FIN DE LA INSERCIÓN DE PRINTS ---

prediccion = knn.predict(nuevo_solicitante_final)
print("\nPredicción del nivel de riesgo para el nuevo solicitante:", prediccion)

# (El código de Streamlit se comenta para mantener la funcionalidad principal)

import joblib

# Guardar el modelo KNN entrenado
joblib.dump(knn, 'modelo_knn.joblib')
print("Modelo KNN guardado como modelo_knn.joblib")

# Guardar el objeto StandardScaler ajustado
joblib.dump(scaler, 'scaler.joblib')
print("Scaler guardado como scaler.joblib")

# (Opcional) Guardar los nombres de las columnas de X_train
joblib.dump(X_train.columns.tolist(), 'feature_names.joblib')
print("Nombres de las características guardados como feature_names.joblib")

# ... (El resto de tu código) ..
"""