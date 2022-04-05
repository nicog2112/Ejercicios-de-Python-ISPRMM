# -*- coding: utf-8 -*-
def evaluar_monto(monto,descuento=0):
    monto_porcentaje_descuento=monto*descuento/100
    monto_final=monto-monto_porcentaje_descuento
    return monto_final

monto_a_pagar=evaluar_monto(1000,20)
print(monto_a_pagar)