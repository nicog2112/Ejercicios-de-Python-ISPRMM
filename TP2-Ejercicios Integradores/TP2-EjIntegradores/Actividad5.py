# -*- coding: utf-8 -*-
lista=[10,24,53,21,9,55,66,98,12,32,47,71,85]
mayor_valor=0

for x in lista:
    if x > mayor_valor:
        mayor_valor=x
print("El mayor valor de la lista es:",mayor_valor)

menor_valor=mayor_valor

for x in lista:
    if x < menor_valor:
        menor_valor=x
print("El menor valor de la lista es:",menor_valor)

diferencia= mayor_valor - menor_valor
print("La diferencia entre el mayor valor y el menor valor es:",diferencia)
