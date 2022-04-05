# -*- coding: utf-8 -*-
monto_compra=2000
Porcentaje_Descuento=0

if monto_compra > 1000:
    Porcentaje_Descuento=10
elif monto_compra>=750 and monto_compra <= 1000:
    Porcentaje_Descuento=5
elif monto_compra>1500:
    Porcentaje_Descuento=12

Descuento= monto_compra * Porcentaje_Descuento /100
Total= monto_compra - Descuento
print("El total a pagar con el descuento es de:" ,Total)