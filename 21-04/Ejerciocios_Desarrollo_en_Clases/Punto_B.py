# -*- coding: utf-8 -*-
Cantidad_Libros =10
Costo=200
Porcentaje_Descuento= 0

if Cantidad_Libros > 10:
    Porcentaje_Descuento=16
elif Cantidad_Libros>=6 and Cantidad_Libros<= 10:
    Porcentaje_Descuento=7
elif Cantidad_Libros>=3 and Cantidad_Libros<=5:
    Porcentaje_Descuento=3

Descuento=Costo*Porcentaje_Descuento/100
Total=Costo-Descuento
print("El total a pagar con el descuento es de:", Total)
