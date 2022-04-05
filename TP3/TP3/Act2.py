# -*- coding: utf-8 -*-
def evaluar_numero(numero):
    resultado=""
    if numero % 2 == 0 :
        resultado="Es par"
    else:
        resultado= "Es impar"
    return resultado

r=evaluar_numero(14)
print (r)