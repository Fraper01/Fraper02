import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re  
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, classification_report
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_score, StratifiedKFold

# Fase 1. Cargar el Dataset

data = pd.read_csv('dataset_riesgo_crediticio_con_riesgo_y_provincia_espana.csv')  

# 1.1. Inspección Inicial se utiliza solo para conocer que tiene la data, su composicion, contenido, etc 
#print("Primeras 5 filas del dataset:")
#print(data.head())  # Muestra las primeras 5 filas

#print("\nInformación general del dataset:")
#data.info()  # Muestra información sobre las columnas, tipos de datos y nulos

#print("\nEstadísticas descriptivas de las columnas numéricas:")
#print(data.describe())  # Muestra estadísticas descriptivas (media, desviación estándar, etc.)

# Fase 2: Limpieza de los Datos

# 2.1 Limpiar el Tipo de Dato Edad
# 2.1.1 Función para limpiar y convertir 'Edad' a numérico
def clean_edad(edad):
    if isinstance(edad, str):
        edad = ''.join(filter(str.isdigit, edad))  # Elimina caracteres no numéricos
        if edad:  # Verifica si la cadena no está vacía después de la limpieza
            return int(edad) # Retorna el Integer
        else:
            return np.nan  # Reorna  "NaN" significa "Not a Number" valor Nulo
    return edad

data['Edad'] = data['Edad'].apply(clean_edad)
data['Edad'] = data['Edad'].astype(int) # Nos aseguramos de que la columna 'Edad' sea de tipo entero.

# 2.2 Limpiar Ingresos Mensuales (Redondeo)
data['Ingresos mensuales'] = data['Ingresos mensuales'].round(2)  # Redondear a 2 decimales

# 2.3 Limpieza Ocupación
data['Ocupación'] = data['Ocupación'].str.strip().str.title()
# 2.3.1 Crear un diccionario para expandir abreviaturas (dinámicamente) y función 
abreviaturas = {'Ing.': 'Ingeniero', 'Abog.': 'Abogado', 'Estud.': 'Estudiante', 'Comerc.': 'Comerciante', 'Técn.': 'Técnico', 'Prof.': 'Profesor'}
def expandir_abreviatura(x):
    if x.group(0) in abreviaturas:
        return abreviaturas[x.group(0)]
    else:
        return x.group(0)

abreviaturas_regex = r'\b(' + '|'.join(re.escape(abreviatura) for abreviatura in abreviaturas.keys()) + r')\b'
data['Ocupación'] = data['Ocupación'].str.replace(abreviaturas_regex, expandir_abreviatura, regex=True)
data['Ocupación'] = data['Ocupación'].str.replace(r' +', ' ', regex=True) # Eliminar espacios múltiples

# 2.4 Función para limpiar una columna categórica (Resto de Columnas String)
def limpiar_categorica(data, columna, mapeo_estandares, mapeo_abreviaturas=None, caracteres_invalidos=None):
    """
    Limpia una columna categórica en un DataFrame, manejando variaciones en la escritura.

    Args:
        data (pd.DataFrame): El DataFrame.
        columna (str): El nombre de la columna a limpiar.
        mapeo_estandares (dict): Diccionario para estandarizar las variaciones (regex como clave).
        mapeo_abreviaturas (dict, opcional): Diccionario para expandir abreviaturas.
        caracteres_invalidos (str, opcional): Regex para eliminar caracteres no válidos.

    Returns:
        pd.Series: La columna limpia.
    """
    # Limpieza
    data[columna] = data[columna].str.strip()  # Eliminar espacios extra (antes de estandarizar)
    data[columna] = data[columna].str.title()  # Estandarizar mayúsculas/minúsculas

    # Estandarizar variaciones
    for patron, estandar in mapeo_estandares.items():
        data[columna] = data[columna].str.replace(patron, estandar, regex=True)

    if mapeo_abreviaturas:
        abreviaturas_regex = r'\b(' + '|'.join(re.escape(abreviatura) for abreviatura in mapeo_abreviaturas.keys()) + r')\b'
        data[columna] = data[columna].str.replace(abreviaturas_regex, lambda x: mapeo_abreviaturas[x.group(0)], regex=True)

    data[columna] = data[columna].str.replace(r' +', ' ', regex=True)  # Eliminar espacios múltiples (después de estandarizar)

    return data[columna]

# 2.4.1 Definir mapeos
historial_crediticio_mapeo_estandares = {
    r'\bBuen(?:o)?\b': 'Bueno',
    r'\bMal(?:o)?\b': 'Malo',
    r'\bReg(?:ular)?\b': 'Regular',
    r'\bEx(?:celente)?(?:!)?\b': 'Excelente',
    r'\bB\b': 'Bueno',
    r'\bM\b': 'Malo',
    r'\bR\b': 'Regular',
    r'\bE\b': 'Excelente'
}

estado_civil_mapeo_estandares = {
    r'\bSol(?:tero)?\b': 'Soltero',
    r'\bCas(?:ado)?(?:\s?\(?C\)?)?\b': 'Casado',
    r'\bDiv(?:orciado)?(?:-)?\b': 'Divorciado',
    r'\bVi(?:udo)?(?:\+)?\b': 'Viudo',
    r'\bS\b': 'Soltero',
    r'\bC\b': 'Casado',
    r'\bD\b': 'Divorciado',
    r'\bV\b': 'Viudo'
}

# Limpiar las columnas
data['Historial crediticio'] = limpiar_categorica(data, 'Historial crediticio', historial_crediticio_mapeo_estandares, caracteres_invalidos=r'[-+!]')
data['Estado civil'] = limpiar_categorica(data, 'Estado civil', estado_civil_mapeo_estandares)

# 2.2 Manejo de Valores Nulos 
# Asigna la Mediana a la Edad, Ingreso Mensual, Porcentaje de endeudamiento si son Null
data['Edad'] = data['Edad'].fillna(data['Edad'].median())
data['Ingresos mensuales'] = data['Ingresos mensuales'].fillna(data['Ingresos mensuales'].median())
data['Porcentaje de endeudamiento'] = data['Porcentaje de endeudamiento'].fillna(data['Porcentaje de endeudamiento'].median())

# Asigna la Mediana o la Moda a los Dependiente Segun su el tipo de Dato 
if data['Dependientes'].dtype in ['int64', 'float64'] and data['Dependientes'].nunique() < 20:  # Verificar si es discreta
    data['Dependientes'] = data['Dependientes'].fillna(data['Dependientes'].median())
else:
    data['Dependientes'] = data['Dependientes'].fillna(data['Dependientes'].mode()[0])

# Manejo de nulos en columnas categóricas (Imputar con la moda)
for col in ['Ocupación', 'Historial crediticio', 'Nivel educativo', 'Estado civil', 'Provincia', 'Nivel de riesgo']:
    if data[col].value_counts().empty:  # Chequea si esta vacio y asigna espacio vacio
        data[col].fillna('')  
    else:
        data[col].fillna(data[col].mode()[0])

# Aplica a todos los Null restantes para garantizar la limpieza
data = data.apply(lambda x: x.fillna(x.value_counts().index[0] if not x.value_counts().empty else (0 if pd.api.types.is_numeric_dtype(x) else '')))

# Fase 3: Codificación de variables categóricas o string a varias columnas segun la Interprtacion de la Data

# 1. Identificar columnas categóricas
categorical_columns = data.select_dtypes(include=['object']).columns

data = pd.get_dummies(data, columns=['Ocupación', 'Nivel educativo', 'Estado civil', 'Historial crediticio', 'Provincia'], drop_first=True)

# 3. Verificar la codificación
"""
    pd.get_dummies(data, columns=['Ocupación', 'Nivel educativo', 'Estado civil'], drop_first=True):
        drop_first=True: Un argumento muy importante. Elimina la primera columna creada para cada variable categórica. 
        Esto ayuda a evitar la multicolinealidad, que puede ser un problema para algunos modelos.

    Como tenemos una columna 'Ocupación' con los valores únicos: ['Ingeniero', 'Abogado', 'Profesor']

    One-Hot Encoding crearía tres nuevas columnas:

    'Ocupación_Ingeniero' (true si es Ingeniero, false en caso contrario)
    'Ocupación_Abogado' (true si es Abogado, false en caso contrario)
    'Ocupación_Profesor' (true si es Profesor, false en caso contrario)

    KNN calcula distancias entre puntos de datos. One-Hot Encoding convierte las categorías en dimensiones separadas, 
    permitiendo que KNN calcule distancias basadas en la presencia o ausencia de cada categoría.
    Al evitar la asignación arbitraria de números como en Label Encoding, 
    One-Hot Encoding evita que KNN interprete accidentalmente una relación ordinal donde no la hay.
"""

# Fase 4 Escalado de Caracteristicas KNN
"""
    Estandarización (StandardScaler): Modelo de Escaldo Seleccionado

    Transforma los datos para que tengan una media de 0 y una desviación estándar de 1.
    Útil cuando los datos siguen una distribución gaussiana (o normal).
    Fórmula: z = (x - μ) / σ (donde x es el valor original, μ es la media y σ es la desviación estándar).
"""

# Identificar las columnas numéricas
numeric_cols = data.select_dtypes(include=np.number).columns.tolist()
# Excluir la variable objetivo si es numérica
if 'Nivel de riesgo' in numeric_cols:
    numeric_cols.remove('Nivel de riesgo')

# Inicializar el StandardScaler
scaler = StandardScaler()

# Escalar las columnas numéricas
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

X = data.drop('Nivel de riesgo', axis=1)   # Características (todas las columnas excepto 'Nivel de riesgo')
y = data['Nivel de riesgo']   # Variable objetivo
X_scaled = X.copy() # Crear una copia de X para evitar modificar X directamente
X_scaled[numeric_cols] = data[numeric_cols].copy() # Asignar los valores escalados a X_scaled

# Fase 5 División de Datos
"""
    Separar los datos en conjuntos de entrenamiento y prueba: 
    X_scaled: Las características escaladas (la matriz de características).
    y: La variable objetivo (Nivel de Riesgo).
    test_size=0.2: Especifica que el 20% de los datos se utilizarán para la prueba, y el 80% para el entrenamiento.
    random_state=42: Es una semilla para el generador de números aleatorios. 
    Usar una semilla asegura que obtengas la misma división de datos cada vez que ejecutes el código. 
    Esto es importante para la reproducibilidad. Puedes usar cualquier número entero como semilla.
"""
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

print("Columnas numéricas para escalar:\n", numeric_cols)
print("Columnas de X_train ANTES del fit del scaler:\n", X_train.columns.tolist())

input("nuevo")

# Fase 6 Entrenamiento del Modelo KNN
"""
    El entrenamiento de un modelo KNN es bastante sencillo en comparación con otros algoritmos. 
    KNN es un algoritmo "perezoso", lo que significa que no aprende una función explícita a partir de los datos de entrenamiento. 
    En cambio, simplemente almacena los datos de entrenamiento y realiza las predicciones basándose en la similitud 
    entre los nuevos datos y los datos de entrenamiento almacenados
"""
scaler.fit(X_train[numeric_cols]) # Ajustamos el scaler SOLO a las columnas numéricas de X_train

X_train_scaled_numeric = scaler.transform(X_train[numeric_cols])
X_train_scaled_df = pd.DataFrame(X_train_scaled_numeric, columns=numeric_cols, index=X_train.index)

# Combinar las columnas numéricas escaladas con las columnas categóricas no escaladas
X_train_scaled = pd.concat([X_train_scaled_df, X_train.drop(columns=numeric_cols)], axis=1)

print("Columnas de X_train DESPUÉS del escalado (reconstruido):\n", X_train_scaled.columns.tolist())
print("Tipo de datos de X_train DESPUÉS del escalado (reconstruido):\n", X_train_scaled.dtypes)

#X_train_scaled_df = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns) # Reconstruimos X_train después del escalado

#print("Columnas de X_train DESPUÉS del fit y transform del scaler:\n", X_train_scaled_df.columns.tolist())
#print("Tipo de datos de X_train DESPUÉS del fit y transform del scaler:\n", X_train_scaled_df.dtypes)

input("nuevo2")
# Crear una instancia del modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)  # Puedes ajustar el valor de n_neighbors

# Entrenar el modelo con los datos de entrenamiento

knn.fit(X_train, y_train)

# Fase 7 Evaluación del Modelo
# Predicciones en el conjunto de Prueba
y_pred = knn.predict(X_test)

# Validación cruzada (para evaluar la robustez del modelo):
scores = cross_val_score(knn, X_scaled, y, cv=5, scoring='f1_weighted')  # 5-fold cross-validation

# Matriz de Confusión
cm = confusion_matrix(y_test, y_pred)

# F1-score en el conjunto de Prueba
f1 = f1_score(y_test, y_pred, average='weighted')

# Validación Cruzada (con estratificación y características escaladas)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
f1_scores_cv = cross_val_score(knn, X_scaled, y, cv=cv, scoring='f1_weighted')


"""
SIMULACION DE DATOS PARA LA PRUEBA
Para probar el modelo, necesitamos crear algunos ejemplos de datos nuevos que el modelo nunca haya visto durante el entrenamiento o la prueba. 
Estos datos deben tener las mismas características (columnas) que nuestro conjunto de entrenamiento (X_train).

Vamos a crear un ejemplo simulado. 
Recuerda los nombres y el orden de las columnas en X_train. 
"""

print(X_train.columns)

#Ahora, vamos a crear un ejemplo de un nuevo solicitante de crédito como un diccionario de Datos
print(X_train.columns.tolist()) # Imprime la lista de columnas de entrenamiento

print("Primer registro de X_test (escalado):\n", X_test.iloc[[0]])
print("\nNombres de las columnas de X_test:\n", X_test.columns.tolist())

input("nada2")

"""

nuevo_solicitante = {
    'Edad': 35,
    'Ingresos mensuales': 5000,
    'Dependientes': 2,
    'Porcentaje de endeudamiento': 0.15,
    'Ocupación_Comerciante': False,
    'Ocupación_Estudiante': False,
    'Ocupación_Ingeniero': True,
    'Ocupación_Profesor': False,
    'Ocupación_Técnico': False,
    'Nivel educativo_Secundario': False,
    'Nivel educativo_Universitario': True,
    'Estado civil_Soltero': False,
    'Historial crediticio_Excelente': False,
    'Historial crediticio_Malo': False,
    'Provincia_Alicante': False,
    'Provincia_Badajoz': False,
    'Provincia_Badalona': False,
    'Provincia_Barcelona': False,
    'Provincia_Bilbao': False,
    'Provincia_Ceuta': False,
    'Provincia_Cáceres': False,
    'Provincia_Córdoba': False,
    'Provincia_Elche': False,
    'Provincia_Gijón': False,
    "Provincia_L'Hospitalet de Llobregat": False,
    'Provincia_Las Palmas': False,
    'Provincia_Madrid': True,
    'Provincia_Melilla': False,
    'Provincia_Murcia': False,
    'Provincia_Málaga': False,
    'Provincia_Palma': False,
    'Provincia_Sevilla': False,
    'Provincia_Valencia': False,
    'Provincia_Valladolid': False,
    'Provincia_Vigo': False,
    'Provincia_Vitoria-Gasteiz': False,
    'Provincia_Zaragoza': False
}

nuevo_solicitante_df = pd.DataFrame([nuevo_solicitante], columns=X_train.columns) # Especificamos el orden de las columnas
"""

columnas_esperadas = X_train.columns.tolist()
nuevo_solicitante_data = [[
    35.0, 5000.0, 2.0, 0.15, False, 
    False, True, False, False, False,
    True, False, False, False, False,
    False, False, False, False, False,
    False, False, False, False, False,
    False, True, False, False, False,
    False, False, False, False, False,
    False, False, False
]] # Los valores deben estar en el MISMO ORDEN que columnas_esperadas

#nuevo_solicitante_df = pd.DataFrame(nuevo_solicitante_data, columns=columnas_esperadas)
nuevo_solicitante_df = pd.DataFrame(nuevo_solicitante_data, columns=X_train_scaled.columns)

# Crear un nuevo scaler
nuevo_scaler = StandardScaler()

# Establecer la media y la desviación estándar del scaler con los valores aprendidos de X_train
nuevo_scaler.mean_ = scaler.mean_
nuevo_scaler.scale_ = scaler.scale_

# Escalar SOLO las columnas numéricas del nuevo solicitante
nuevo_solicitante_scaled_numeric = nuevo_scaler.transform(nuevo_solicitante_df[numeric_cols])

# Crear un DataFrame con las columnas numéricas escaladas
nuevo_solicitante_scaled_df = pd.DataFrame(nuevo_solicitante_scaled_numeric, columns=numeric_cols)

# Combinar con las columnas categóricas
nuevo_solicitante_final = pd.concat([nuevo_solicitante_scaled_df, nuevo_solicitante_df.drop(columns=numeric_cols)], axis=1)

prediccion = knn.predict(nuevo_solicitante_final)
print("Predicción del nivel de riesgo:", prediccion)

print("Tipo de datos de nuevo_solicitante_df ANTES del escalado:\n", nuevo_solicitante_df.dtypes) # <--- AÑADE ESTA LÍNEA
input("antes escalado")

#nuevo_solicitante_scaled = scaler.transform(nuevo_solicitante_df)

#prediccion = knn.predict(nuevo_solicitante_scaled)

#print("Predicción del nivel de riesgo:", prediccion)
"""
¡Importante! Asegúrate de que las claves del diccionario coincidan exactamente con los nombres de las columnas en X_train, 
y que los valores representen la codificación correcta (0 o 1 para las variables One-Hot).
"""

#print(nuevo_solicitante)

"""

# Convertir a DataFrame y Escalar:
# Nuestro modelo fue entrenado con datos escalados, por lo que también debemos escalar los nuevos datos antes de hacer la predicción.

nuevo_solicitante_df = pd.DataFrame([nuevo_solicitante])
nuevo_solicitante_scaled = scaler.transform(nuevo_solicitante_df)

# Hacer la Predicción
# Ahora podemos usar nuestro modelo KNN entrenado (knn) para predecir el nivel de riesgo para este nuevo solicitante

prediccion = knn.predict(nuevo_solicitante_scaled)
print("Predicción del nivel de riesgo:", prediccion)

"""

#Usa streamlit (en Python) para hacer una interfaz interactiva: el usuario introduce datos y ve el resultado del modelo.
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

"""

# Simulación de un modelo previamente entrenado (aquí lo entrenamos en el mismo script)
def entrenar_modelo():
    np.random.seed(42)
    n = 500
    X = pd.DataFrame({
        'Edad': np.random.randint(18, 70, n),
        'Ingresos': np.random.randint(1000, 5000, n),
        'Dependientes': np.random.randint(0, 5, n),
        'Endeudamiento': np.random.randint(0, 100, n)
    })
    y = np.select(
        [
            (X['Ingresos'] < 2000) | (X['Endeudamiento'] > 60),
            (X['Ingresos'] > 3500) & (X['Endeudamiento'] < 30)
        ],
        ['Alto', 'Bajo'],
        default='Medio'
    )
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model

model = entrenar_modelo()

# INTERFAZ STREAMLIT
st.title("Evaluador de Riesgo Crediticio")

st.markdown("Introduce los datos del solicitante para clasificar el nivel de **riesgo crediticio**.")

edad = st.slider("Edad", 18, 70, 30)
ingresos = st.number_input("Ingresos mensuales (€)", min_value=500, max_value=10000, value=2500)
dependientes = st.slider("Número de dependientes", 0, 5, 1)
endeudamiento = st.slider("Porcentaje de endeudamiento (%)", 0, 100, 25)

if st.button("Evaluar Riesgo"):
    entrada = pd.DataFrame({
        'Edad': [edad],
        'Ingresos': [ingresos],
        'Dependientes': [dependientes],
        'Endeudamiento': [endeudamiento]
    })
    prediccion = model.predict(entrada)[0]
    st.success(f"**Nivel de riesgo estimado: {prediccion.upper()}**")

    # Feedback visual
    if prediccion == 'Bajo':
        st.balloons()
    elif prediccion == 'Alto':
        st.warning("⚠️ Riesgo alto detectado.")
"""
