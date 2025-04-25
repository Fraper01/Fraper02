# crear un vector y mostrar su logitud
vector  = [3,8,2]
print("El vector es: ", vector)
print("La longitud del vector es: ", len(vector))

# sumar dos vectores
vector1 = [1,2,3]
vector2 = [4,5,6]
suma = [vector1[i] + vector2[i] for i in range(len(vector1))]
print("La suma de los vectores es: ", suma)

vector1 = [1,2,3]
vector2 = [4,5,6]
suma = []
for i in range(len(vector1)):
    vsuma = vector1[i] + vector2[i]
    suma.append(vsuma)
print("La suma de los vectores es: ", suma) 

# otro comparar dos vectores que representan peliculas
# 0 = no vista, 1 = vista
matrix = [1,0,1,0,1] # [accion, comedia, drama, terror, ciencia ficcion]
elpadrino = [0,0,0,1,0] # [accion, comedia, drama, terror, ciencia ficcion]

similitud = sum([a * b for a, b in zip(matrix, elpadrino)])
print("La similitud entre Matrix y elpadrino es: ", similitud)

similitud2=0
mult = []
for i in range(len(matrix)):    
    if matrix[i] == elpadrino[i]:
        vmultiplicacion = matrix[i] * elpadrino[i]
        mult.append(vmultiplicacion)
similitud2 = sum(mult)
print("La similitud entre Matrix y elpadrino es: ", similitud2)


# Matizes
matriz = [[1,2], [3,4]]
print("La matriz es: ", matriz)
print("La longitud de la matriz es: ", len(matriz))

for fila in matriz:
    for elemento in fila:
        print(elemento)

# suma de Matrices
matriz1 = [[1,2],
           [3,4]]    
matriz2 = [[5,6],
           [7,8]]

suma = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

print("La suma de las matrices es: ", suma)

