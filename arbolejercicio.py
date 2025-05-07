#Ejemplo práctico: Árbol de decisión con el dataset Iris
#Paso 1: Importar bibliotecas y cargar los datos

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Cargar el dataset
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Clases (setosa, versicolor, virginica)


#Paso 2: Crear y entrenar el modelo

# Crear el clasificador (CART por defecto en scikit-learn)
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf.fit(X, y)

#Paso 3: Visualizar el árbol de decisión


plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Árbol de decisión para clasificar flores Iris")
plt.show()

#Paso 4: Realizar una predicción

# Clasificar una flor con valores específicos
sample = [[5.1, 3.5, 1.4, 0.2]]  # Ejemplo de flor tipo setosa
predicted_class = clf.predict(sample)
print("Clase predicha:", iris.target_names[predicted_class[0]])

"""
Este ejemplo:

Usa el criterio Gini para dividir nodos (como hace CART).

Limita la profundidad del árbol a 3 para evitar sobreajuste.

Muestra un diagrama claro del árbol resultante.
"""
