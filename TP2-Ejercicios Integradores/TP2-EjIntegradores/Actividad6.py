# -*- coding: utf-8 -*-
formosa={"2015": 5500 , "2016":8200 ,"2017":7350, "2018":4650}
espinillo={"2015": 6600 , "2016":4800 ,"2017":4950, "2018":2500}
clorinda={"2015": 5300 , "2016":7500 ,"2017":2200, "2018":3200}

sucursales={"formosa": formosa , "espinillo":espinillo ,"clorinda":clorinda}

#MENOR RECAUDACION GENERAL
menor_valor=999999999999999999999

for ciudad , sucursal in sucursales.items():
    for anio , recaudacion in sucursal.items():
        if recaudacion < menor_valor:
            menor_valor=recaudacion
print("El menor valor de toda la recaudacion es:",menor_valor)

#MENOR RECAUDACION EN 2018
menor_valor_2018=99999
sucursal_2018=""

for ciudad , sucursal in sucursales.items():
    for anio , recaudacion in sucursal.items():
        if anio =="2018"and recaudacion<menor_valor_2018:
            menor_valor_2018=recaudacion
            sucursal_2018=ciudad
print("La menor recaudacion en el año 2018 fue de:",menor_valor_2018,"En la sucursal:",sucursal_2018)

#TOTAL RECAUDACION ESPINILLO
suma_total_espinillo=0
for ciudad , sucursal in sucursales.items():
    for anio , recaudacion in sucursal.items():
        if ciudad=="espinillo":
            suma_total_espinillo=suma_total_espinillo+recaudacion
print("La suma total de la sucursal espinillo da:",suma_total_espinillo)

#MAYOR VALOR SUCURSAL CLORINDA
mayor_valor_clorinda=0
for ciudad , sucursal in sucursales.items():
    for anio , recaudacion in sucursal.items():
        if ciudad=="clorinda" and recaudacion>mayor_valor_clorinda:
            mayor_valor_clorinda=recaudacion
print("El mayor valor de la sucursal clorinda es:",mayor_valor_clorinda)

#Total de recaudacion en 2017
suma_total_2017=0
for ciudad , sucursal in sucursales.items():
    for anio , recaudacion in sucursal.items():
        if anio=="2017":
            suma_total_2017=suma_total_2017+recaudacion
print("La suma total de todas las sucursales en el año 2017 fue de:",suma_total_2017)


