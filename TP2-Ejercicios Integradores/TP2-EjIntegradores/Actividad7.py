# -*- coding: utf-8 -*-
#Ingreso de cantidad de filas y columnas de la matriz
n=int(input("Ingrese el numero de filas y columnas de la matriz:"))
fila=n
columna=n

#Creacion de la matriz
matriz=[]
for i in range(fila):
    matriz.append([0]*columna)

#Cambiamos los valores de la fila y columna
for i in range(fila):
    for j in range(columna):
        matriz[i][j]=int(input("Introduce el valor de (%d,%d):" % (i,j)))

#Suma de diagonales de la matriz
for i in range(fila):
    for j in range(columna):
        sum_diagonal1=sum(matriz[i][i] for i in range(fila))
        sum_diagonal2=sum([matriz[i][j] for i in range(fila) for j in range(columna) if i+j==columna-1])
print("La suma de la diagonal 1 es:",str(sum_diagonal1))
print("La suma de la diagonal 2 es:",str(sum_diagonal2))

#Diferencia absoluta
for i in range(fila):
    for j in range(columna):
        diferencia=sum_diagonal1 - sum_diagonal2

print("La diferencia absoluta entre las diagonales de una matriz cuadrada es:",abs(diferencia))
