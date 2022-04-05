# -*- coding: utf-8 -*-

#EJERCICIO 1

#-Cosntruir una Aplicación cuyo algoritmo muestre una lista de alumnos Aprobados.
#Ingresando los Nombres y las notas por Teclado.

def cargar():
    notas={}
    for x in range(5):
        nombre=raw_input("Ingrese el nombre del alumno:")
        calificacion=int(raw_input("Ingrese el calificacion:"))
        notas[nombre]=calificacion
    return notas


def imprimir(notas):
    print("Listado de todos los alumnos")
    for nombre in notas:
        print(nombre, notas[nombre])


def imprimir_mayor(notas):
    print("Listado de alumnos aprobados")
    for nombre in notas:
        if notas[nombre]>4:
            print(nombre)



