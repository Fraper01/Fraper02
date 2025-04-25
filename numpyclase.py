import numpy as np
#from scipy import stats

manzana = np.array([1, 2, 2, 3, 4, 2, 5])

media = np.mean(manzana)
print("La media de la manzana es: ", media)

mediana = np.median(manzana)
print("La mediana de la manzana es: ", mediana)

#moda_resultado = stats.mode(manzana)
moda_resultado = np.modo(manzana)

print("La moda de la manzana es: ", moda_resultado.mode[0])
print("La frecuencia de la moda es: ", moda_resultado.count[0])

devst = np.std(manzana)
print("La desviacion estandar de la manzana es: ", devst)

varianza = np.var(manzana)
print("La varianza de la manzana es: ", varianza)

