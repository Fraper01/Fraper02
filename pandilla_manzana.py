# Ejercicio las pandilla de las manzanas
from os import system, path
import numpy as np
import statistics as stats

def menu_manzanas():
    # Pesos de las manzanas en gramos
    pesosManzanas = np.array([150, 180, 200, 170, 150, 190, 200, 210, 150, 180])  
    # Estadisticas Descriptivas
    mediaPeso = np.mean(pesosManzanas)  # Media de los pesos promedio
    medianaPeso = np.median(pesosManzanas)  # Mediana de los pesos promedio
    modaPeso = stats.mode(pesosManzanas)  # Moda de los pesos promedio
    desviacionPeso = np.std(pesosManzanas)  # Desviación estándar de los pesos promedio Variabilidad lo que se aleja de la media

    ancho_linea = 75
    titulo = "Estadísticas descriptivas de los pesos de las manzanas"
    system('cls')
    print("-" * ancho_linea)
    print(titulo.center(ancho_linea))  
    print("-" * ancho_linea)
    print("Pesos de las manzanas (gramos):", pesosManzanas)
    print(f"Cantidad de manzanas: {len(pesosManzanas)}  Total de pesos: {sum(pesosManzanas)} gramos")    
    print("-" * ancho_linea)
    print(f"Peso promedio de las manzanas   : {mediaPeso:>10.2f} gramos")
    print(f"Peso mediano de las manzanas    : {medianaPeso:>10.2f} gramos")
    print(f"Peso moda de las manzanas       : {modaPeso:>10.2f} gramos")
    print(f"Desviación estándar de los pesos: {desviacionPeso:>10.2f} gramos")
    print("-" * ancho_linea)
    # Interpretación de la asimetría
    if mediaPeso > medianaPeso:
        print("La distribución de los pesos de las manzanas está sesgada a la derecha "
          "\n(Cola más larga hacia valores más altos).")
    elif mediaPeso < medianaPeso:
        print("La distribución de los pesos de las manzanas está sesgada a la izquierda "
          "\n(Cola más larga hacia valores más bajos).")
    else:
        print("La distribución de los pesos de las manzanas es aproximadamente simétrica.")

    print("-" * ancho_linea)
    print("¡Análisis de pesos de manzanas completado!") 
    input("\nPresiona Enter para continuar...")

'''
if __name__ == "__main__":
    menu_manzanas()
'''