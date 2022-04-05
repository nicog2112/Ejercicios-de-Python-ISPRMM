# -*- coding: utf-8 -*-
x=1
contador_a=0
contador_b=0
contador_c=0
gastos_a=0
gastos_b=0
gastos_c=0

n=int(input("Ingresar cantidad de empleados:"))
while x<=n:
    sueldo=float(input("Ingresar sueldo neto:"))
    if sueldo>=100 and sueldo<=500:
        contador_a=contador_a+1
        gastos_a=gastos_a+sueldo
    elif sueldo>=100 and sueldo<=300:
        contador_b=contador_b+1
        gastos_b=gastos_b+sueldo
    elif sueldo > 300:
        contador_c=contador_c+1
        gastos_c=gastos_c+sueldo
    x=x+1
print ("a")
print(contador_a)
print(gastos_a)
print("-------------")
print ("b")
print(contador_b)
print(gastos_b)
print("-------------")
print ("c")
print(contador_c)
print(gastos_c)