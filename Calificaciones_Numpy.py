import os
import numpy as np


def analizar_calificaciones():
    #Limpiamos pantalla
    limpiar()


    #Crear el array de calificaciones
    calificaciones=[]


    #Pedir ingresar las 5 calificaciones de usuario
    for i in range(5):
        nota = float(input(f"Ingrese la {i+1}º calificacion: "))
        calificaciones.append(nota)


    #Guardar el array inicial en un array de numpy
    notas = np.array(calificaciones)


    #Mostrar las calificaciones
    print("Analisis de las calificaciones")
    print(f"Calificaciones: {notas}")
    print(f"Promedio: {np.mean(notas):.2f}")
    print(f"Máximo: {np.max(notas):.2f}")
    print(f"Minimo: {np.min(notas):.2f}")



def limpiar():
    os.system("cls")


if __name__ == "__main__":
    analizar_calificaciones()