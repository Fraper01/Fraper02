from os import system, path
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def analizar_aguacates(lista_pesos):
    """Calcula estadísticas y muestra la distribución de pesos de aguacates."""
    media_peso = np.mean(lista_pesos)
    mediana_peso = np.median(lista_pesos)
    moda_peso = stats.mode(lista_pesos)
    desviacion_estandar_peso = np.std(lista_pesos)

    # Calcular el coeficiente de variación
    if media_peso != 0:
        coeficiente_variacion = (desviacion_estandar_peso / media_peso) * 100
    else:
        coeficiente_variacion = np.nan  # Indicar si la media es cero (aunque es poco probable para pesos)

    # Identificar aguacates más pesado y más ligero
    aguacate_mas_pesado = max(lista_pesos)
    aguacate_mas_ligero = min(lista_pesos)

    # Contar aguacates dentro del rango ideal
    aguacates_en_rango = sum(1 for peso in lista_pesos if rango_ideal[0] <= peso <= rango_ideal[1])

    print("\n--- Análisis de Peso de Aguacates ---")
    print(f"La media del peso es: {media_peso:.2f} gramos")
    print(f"La mediana del peso es: {mediana_peso} gramos")
    print(f"La moda del peso es: {moda_peso.mode[0]} gramos (aparece {moda_peso.count[0]} veces)")
    print(f"La desviación estándar del peso es: {desviacion_estandar_peso:.2f} gramos")
    print(f"El coeficiente de variación es: {coeficiente_variacion:.2f}%")
    print("\nInterpretación del coeficiente de variación:")
    if not np.isnan(coeficiente_variacion):
        if coeficiente_variacion < 15:
            print("El cultivo de aguacates muestra una alta homogeneidad en el peso.")
        elif coeficiente_variacion < 30:
            print("El cultivo de aguacates muestra una homogeneidad moderada en el peso.")
        else:
            print("El cultivo de aguacates muestra una baja homogeneidad en el peso.")
    else:
        print("No se puede calcular el coeficiente de variación (la media es cero).")
    print(f"El aguacate más pesado pesa: {aguacate_mas_pesado} gramos")
    print(f"El aguacate más ligero pesa: {aguacate_mas_ligero} gramos")
    print(f"Hay {aguacates_en_rango} aguacates dentro del rango ideal de {rango_ideal[0]} - {rango_ideal[1]} gramos")

    input("Presiona Enter para continuar...")

    # 📊 Extra 1: Visualización con Matplotlib
    plt.figure(figsize=(10, 6))
    plt.hist(lista_pesos, bins=10, edgecolor='black', alpha=0.7)
    plt.title('Distribución del Peso de los Aguacates')
    plt.xlabel('Peso (gramos)')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y', alpha=0.5)
    plt.show()

    # Boxplot
    plt.subplot(1, 2, 2)
    plt.boxplot(lista_pesos, vert=False)
    plt.title('Distribución del Peso de los Aguacates (Boxplot)')
    plt.xlabel('Peso (gramos)')
    plt.yticks([1], ['Pesos'])
    plt.grid(axis='x', alpha=0.5)
    plt.tight_layout()
    plt.show()

# 📈 Extra 2: Permitir al usuario ingresar nuevos pesos
def nuevos_aguacates(nuevos_aguacates_lista):
    """Permite al usuario ingresar nuevos pesos de aguacates."""
    while True:
        mostrar_menu()
        print("\n--- Ingreso de Nuevos Aguacates ---")
        nuevo_peso_str = input("Ingrese el peso de un nuevo aguacate (gramos, deje vacío para terminar): ")
        if not nuevo_peso_str:  # Si la cadena ingresada está vacía
            break  # Salir del bucle
        try:
            nuevo_peso = float(nuevo_peso_str)
            nuevos_aguacates_lista.append(nuevo_peso)
        except ValueError:
            print("Por favor, ingrese un número válido para el peso.")
    return nuevos_aguacates_lista

def cargar_rango_ideal():
    """Permite al usuario ingresar el rango ideal de peso."""
    while True:
        mostrar_menu()
        print("\n--- Cargar Rango Ideal de Peso ---")
        try:
            min_peso = float(input("Ingrese el peso mínimo del rango ideal (gramos): "))
            max_peso = float(input("Ingrese el peso máximo del rango ideal (gramos): "))
            if min_peso >= max_peso:
                print("Error: El peso mínimo debe ser menor que el peso máximo.")
            else:
                return [min_peso, max_peso]
        except ValueError:
            print("Por favor, ingrese números válidos para el rango de peso.")

def mostrar_menu()-> None:
    #Muestra el menú de General."""
    system('cls')
    ancho_linea = 40
    print("-" * ancho_linea)
    print("1. Analizar Aguacates")
    print("2. Ingresar Nuevos Aguacates")
    print("3. Ingresar Rango Ideal de Peso")
    print("0. Salir")
    print("-" * ancho_linea)

if __name__ == "__main__":
    # Bucle principal del programa.
    # Se utiliza para mostrar el menú y ejecutar las opciones seleccionadas por el usuario.
    aguacates = [150, 165, 140, 170, 155, 160, 145, 175, 150, 160, 165, 155]
    rango_ideal_peso = [400, 600]  # Rango ideal por defecto
    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_menu()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                analizar_aguacates(aguacates)
            elif opcion == '2':
                aguacates = nuevos_aguacates(aguacates)
            elif opcion == '3':
                rango_ideal_peso = cargar_rango_ideal()
            elif opcion == '0':
                print("¡Hasta la próxima cosecha de aguacates!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción válida.")


  '''  for elemento in mi_lista:
        if elemento == valor_a_buscar:
        encontrado = True
        break  # Podemos salir del bucle una vez que lo encontramos




    def esta_en_rango(peso, rango):
        min_peso = rango[0]
        max_peso = rango[1]
        return min_peso <= peso <= max_peso

    aguacates = [150, 165, 450, 170, 580, 160]
    rango_aceptable = [400, 600]

    for peso in aguacates:
        if esta_en_rango(peso, rango_aceptable):
            print(f"El aguacate de {peso} gramos está en el rango aceptable.")
        else:
            print(f"El aguacate de {peso} gramos está FUERA del rango aceptable.")

'''