# -*- coding: utf-8 -*-
n=int(input("Ingresar un numero:"))
if not n%2==0:
    print("Numero Extraño")
elif n%2==0 and n>=2 and n<=5:
    print("Numero NO Extraño")
elif n%2==0 and n>=6 and n<=20:
    print("Numero Extraño")
elif n%2==0 and n>20:
    print("Numero NO Extraño")