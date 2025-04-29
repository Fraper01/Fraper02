from os import system, path
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import csv
from datetime import datetime

def analizar_aguacates(lista_pesos, rango_ideal):
    """Calcula estadísticas, muestra la distribución y guarda el análisis de pesos de aguacates."""
    media_peso = np.mean(lista_pesos)
    mediana_peso = np.median(lista_pesos)
    moda_peso_result = stats.mode(lista_pesos)
    if isinstance(moda_peso_result.mode, np.ndarray) and moda_peso_result.mode.size > 0:
        moda_peso = moda_peso_result.mode[0]
        frecuencia_moda = moda_peso_result.count[0]
    elif hasattr(moda_peso_result.mode, 'item'): # Para manejar escalares
        moda_peso = moda_peso_result.mode.item()
        frecuencia_moda = moda_peso_result.count.item()
    else:
        moda_peso = "No hay moda clara"
        frecuencia_moda = 0
    
    desviacion_estandar_peso = np.std(lista_pesos)
    asimetria_peso = stats.skew(lista_pesos)

    # Calcular el coeficiente de variación
    if media_peso != 0:
        coeficiente_variacion = (desviacion_estandar_peso / media_peso) * 100
    else:
        coeficiente_variacion = np.nan

    # Identificar aguacates más pesado y más ligero
    aguacate_mas_pesado = max(lista_pesos)
    aguacate_mas_ligero = min(lista_pesos)

    # Contar aguacates dentro del rango ideal
    aguacates_en_rango = sum(1 for peso in lista_pesos if rango_ideal[0] <= peso <= rango_ideal[1])

    mostrar_menu()
    print("\n--- Calcula estadísticas y muestra la distribución ---")

    analisis = {
        "Fecha y Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Cantidad de Aguacates                    ": f"{len(lista_pesos):>7}",
        "Total de Pesos (gramos)                  ": f"{sum(lista_pesos):>7}",
        "Media del Peso (gramos)                  ": f"{media_peso:>7.2f}",
        "Mediana del Peso (gramos)                ": f"{mediana_peso:>7.2f}",
        "Moda del Peso (gramos)                   ": f"{moda_peso:>7} (aparece {frecuencia_moda} veces)" if isinstance(moda_peso, (int, float)) else moda_peso,
        "Desviación Estándar del Peso (gramos)    ": f"{desviacion_estandar_peso:>7.2f}",
        "Coeficiente de Variación (%)             ": f"{coeficiente_variacion:>7.2f}",
        "Asimetría del Peso                       ": f"{asimetria_peso:>7.2f}",
        "Aguacate Más Pesado (gramos)             ": f"{aguacate_mas_pesado:>7}",
        "Aguacate Más Ligero (gramos)             ": f"{aguacate_mas_ligero:>7}",
        f"Aguacates en Rango Ideal ({rango_ideal[0]:>3.0f}-{rango_ideal[1]:>3.0f} gramos)": f"{aguacates_en_rango:>7}",
        "Aguacates Fuera de Rango Ideal           ": f"{(len(lista_pesos) - aguacates_en_rango):>7}",
        "Rango Ideal (gramos)                     ": f"{rango_ideal[0]:>3.0f}-{rango_ideal[1]:>3.0f}"
    }

    print("\n--- Análisis de Peso de Aguacates ---")
    for clave, valor in analisis.items():
        print(f"{clave}: {valor}")

    print("\nInterpretación de la asimetría:")
    if asimetria_peso > 0:
        print("La distribución está sesgada a la derecha (cola más larga hacia valores más altos).")
    elif asimetria_peso < 0:
        print("La distribución está sesgada a la izquierda (cola más larga hacia valores más bajos).")
    else:
        print("La distribución es aproximadamente simétrica.")

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

    ver_graficos = input("\n¿Desea ver los gráficos de distribución? (s/n): ").lower()
    if ver_graficos == 's':
        plt.figure(figsize=(14, 6))

        # Histograma
        plt.subplot(1, 2, 1)
        plt.hist(lista_pesos, bins=10, edgecolor='black', alpha=0.7)
        plt.title('Distribución del Peso de los Aguacates (Histograma)')
        plt.xlabel('Peso (gramos)')
        plt.ylabel('Frecuencia')
        plt.grid(axis='y', alpha=0.5)

        # Boxplot
        plt.subplot(1, 2, 2)
        plt.boxplot(lista_pesos, vert=False)
        plt.title('Distribución del Peso de los Aguacates (Boxplot)')
        plt.xlabel('Peso (gramos)')
        plt.yticks([1], ['Pesos'])
        plt.grid(axis='x', alpha=0.5)

        plt.tight_layout()
        plt.show()

    return analisis

def nuevos_aguacates(nuevos_aguacates_lista):
    """Permite al usuario ingresar nuevos pesos de aguacates."""
    while True:
        mostrar_menu()
        print("\n--- Ingreso de Nuevos Aguacates ---")
        nuevo_peso_str = input("Ingrese el peso de un nuevo aguacate (gramos, deje vacío para terminar): ")
        if not nuevo_peso_str:
            break
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

def guardar_analisis(analisis):
    """Guarda el análisis en un archivo .txt o .csv."""
    while True:
        mostrar_menu_guardar()
        opcion_guardar = input("Seleccione una opción para guardar el análisis: ")
        if opcion_guardar == '1':
            nombre_archivo = input("Ingrese el nombre del archivo .txt para guardar el análisis: ")
            try:
                with open(f"{nombre_archivo}.txt", 'w') as archivo:
                    for clave, valor in analisis.items():
                        archivo.write(f"{clave}: {valor}\n")
                print(f"Análisis guardado exitosamente en {nombre_archivo}.txt")
                break
            except Exception as e:
                print(f"Error al guardar el archivo .txt: {e}")
        elif opcion_guardar == '2':
            nombre_archivo = input("Ingrese el nombre del archivo .csv para guardar el análisis: ")
            try:
                with open(f"{nombre_archivo}.csv", 'w', newline='') as archivo_csv:
                    writer = csv.writer(archivo_csv)
                    writer.writerow(analisis.keys())
                    writer.writerow(analisis.values())
                print(f"Análisis guardado exitosamente en {nombre_archivo}.csv")
                break
            except Exception as e:
                print(f"Error al guardar el archivo .csv: {e}")
        elif opcion_guardar == '0':
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

def mostrar_menu_guardar():
    """Muestra el menú para guardar el análisis."""
    system('cls')
    ancho_linea = 40
    print("-" * ancho_linea)
    print("¿Cómo desea guardar el análisis?")
    print("1. Guardar en archivo .txt")
    print("2. Guardar en archivo .csv")
    print("0. Volver al menú principal")
    print("-" * ancho_linea)

def mostrar_menu()-> None:
    #Muestra el menú de General."""
    system('cls')
    ancho_linea = 40
    print("-" * ancho_linea)
    print("1. Analizar Aguacates")
    print("2. Ingresar Nuevos Aguacates")
    print("3. Cargar Rango Ideal de Peso")
    print("4. Guardar Análisis")  
    print("0. Salir")
    print("-" * ancho_linea)

def ejercicio_aguacate():
    """Función principal para ejecutar el análisis de aguacates."""
    aguacates = [150, 165, 140, 170, 155, 160, 145, 175, 150, 160, 165, 155, 140, 170, 155, 160, 145, 175, 150, 160, 165, 155]
    rango_ideal_peso = [150, 160]  # Rango ideal por defecto

    while True:
        try:
            mostrar_menu()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                analisis_completo = analizar_aguacates(aguacates, rango_ideal_peso)
            elif opcion == '2':
                aguacates = nuevos_aguacates(aguacates)
            elif opcion == '3':
                rango_ideal_peso = cargar_rango_ideal()
            elif opcion == '4':
                if 'analisis_completo' in locals():
                    guardar_analisis(analisis_completo)
                else:
                    print("Primero debes realizar un análisis (opción 1).")
            elif opcion == '0':
                print("¡Hasta la próxima cosecha de aguacates!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción válida.")

if __name__ == "__main__":
    # Bucle principal del programa.
    # Se utiliza para mostrar el menú y ejecutar las opciones seleccionadas por el usuario.
    aguacates = [150, 165, 140, 170, 155, 160, 145, 175, 150, 160, 165, 155]
    rango_ideal_peso = [150, 160]  # Rango ideal por defecto

    while True:
        # Manejo de excepciones para evitar errores de entrada.
        # Se utiliza para asegurarse de que el usuario introduce un valor válido.
        try:
            mostrar_menu()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                analisis_completo = analizar_aguacates(aguacates, rango_ideal_peso)
            elif opcion == '2':
                aguacates = nuevos_aguacates(aguacates)
            elif opcion == '3':
                rango_ideal_peso = cargar_rango_ideal()
            elif opcion == '4':
                if 'analisis_completo' in locals():
                    guardar_analisis(analisis_completo)
                else:
                    print("Primero debes realizar un análisis (opción 1).")
            elif opcion == '0':
                print("¡Hasta la próxima cosecha de aguacates!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce una opción válida.")