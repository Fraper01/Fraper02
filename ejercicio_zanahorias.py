from os import system, path
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def analizar_zanahorias(lista_pesos):
    """Calcula estadísticas y muestra la distribución de pesos de zanahorias."""
    media_peso = np.mean(lista_pesos)
    mediana_peso = np.median(lista_pesos)
    moda_peso = stats.mode(lista_pesos)
    desviacion_estandar_peso = np.std(lista_pesos)

    print("\n--- Análisis de Peso de Zanahorias ---")
    print(f"La media del peso es: {media_peso:.2f} gramos")
    print(f"La mediana del peso es: {mediana_peso} gramos")
    #print(f"La moda del peso es: {moda_peso:.2f} gramos")
    print(f"La desviación estándar del peso es: {desviacion_estandar_peso:.2f} gramos")

    # 📊 Extra 1: Visualización con Matplotlib
    plt.figure(figsize=(10, 6))
    plt.hist(lista_pesos, bins=10, edgecolor='black', alpha=0.7)
    plt.title('Distribución del Peso de las Zanahorias')
    plt.xlabel('Peso (gramos)')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y', alpha=0.5)
    plt.show()

# 📈 Extra 2: Permitir al usuario ingresar nuevos pesos
def nuevas_zanahorias(nuevas_zanahorias):
    """Permite al usuario ingresar nuevos pesos de zanahorias."""
    while True:
        mostrar_menu()
        print("\n--- Ingreso de Nuevas Zanahorias ---")
        nuevo_peso_str = input("Ingrese el peso de una nueva zanahoria (gramos): ")
        if not nuevo_peso_str:  # Si la cadena ingresada está vacía
            break  # Salir del bucle        
        if (nuevo_peso_str != False):
            try:
                nuevo_peso = float(nuevo_peso_str)
                nuevas_zanahorias.append(nuevo_peso)
            except ValueError:
                print("Por favor, ingrese un número válido para el peso.")
    return nuevas_zanahorias

def mostrar_menu()-> None:
    #Muestra el menú de General."""
    system('cls')
    ancho_linea = 40
    print("-" * ancho_linea)
    print("1. Analizar Zanahorias")
    print("2. Ingresar Nuevas Zanahorias")
    print("0. Salir")
    print("-" * ancho_linea)

if __name__ == "__main__":
    # Bucle principal del programa.
    # Se utiliza para mostrar el menú y ejecutar las opciones seleccionadas por el usuario. 
    zanahorias = [300, 280, 290, 310, 275, 290, 295, 315, 290, 280, 310, 305]
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_menu()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                analizar_zanahorias(zanahorias)
            elif opcion == '2':
                zanahorias = nuevas_zanahorias(zanahorias)
            elif opcion == '0':
                print("¡Despegando hacia la próxima aventura!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción valida.")

