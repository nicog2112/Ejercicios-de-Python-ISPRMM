# -*- coding: utf-8 -*-
productos= {"yerba":1500, "leche":1250, "gaseosa":1650, "galletitas":1100}
#MAYOR RECAUDACION
mayor_recaudacion=0
producto_mayor_valor= ""

for producto, monto_venta in productos.items():
    if monto_venta>mayor_recaudacion:
        mayor_recaudacion= monto_venta
        producto_mayor_valor=producto

print("El producto que mas recaudo fue:",producto_mayor_valor,"coun un monto de venta de:",mayor_recaudacion)
#MENOR RECAUDACION

menor_recaudacion=mayor_recaudacion
producto_menor_valor= ""


for producto, monto_venta in productos.items():
    if monto_venta<menor_recaudacion:
        menor_recaudacion= monto_venta
        producto_menor_valor=producto

print("El producto que menos recaudo fue:",producto_menor_valor,"coun un monto de venta de:",menor_recaudacion)
#SUMA TOTAL

suma_total=0
for producto, monto_venta in productos.items():
    suma_total=suma_total+monto_venta

print("La suma total de todos los montos es:",suma_total)
