# -*- coding: utf-8 -*-
caceres={"yerba":5500 , "leche":8000 , "galletitas":8750}
apa={"yerba":5500 , "leche":7200 , "galletitas":9200}
chango={"yerba":5300 , "leche":7800 , "galletitas":8400}

supermercados_lista={"caceres":caceres , "apa":apa , "chango":chango}

menor_valor_leche=99999999
supermercado_menor_valor=""

sumatoria_total_galletitas=0

menor_valor_yerba=999999999
supermercado_menor_valor_yerba=""

suma_total_chango=0

suma_leche=0

for supermercado , lista_recaudacion in supermercados_lista.items():
    for producto , recaudacion in lista_recaudacion.items():
        if producto =="leche":
            suma_leche+=recaudacion

            if recaudacion < menor_valor_leche:
                menor_valor_leche = recaudacion
                supermercado_menor_valor = supermercado
        if producto == "galletitas":
            sumatoria_total_galletitas=sumatoria_total_galletitas+recaudacion

        if producto == "yerba":
            if recaudacion < menor_valor_yerba:
                menor_valor_yerba= recaudacion
                supermercado_menor_valor_yerba=supermercado

        if supermercado =="chango":
            suma_total_chango=suma_total_chango+recaudacion



cantidad=len(supermercados_lista)
promedio_recaudacion_leche=suma_leche/cantidad

print("El menor valor es:",menor_valor_leche,"y pertenece al supermercado:",supermercado_menor_valor)
print("La sumatoria total del producto galletitas es:", sumatoria_total_galletitas)
print("El menor valor del producto yerba es:",menor_valor_yerba,"y pertenece al supermercado:",supermercado_menor_valor_yerba)
print("La suma total de ventas de chango es:",suma_total_chango)
print("El promedio de ventas del producto leche es:",promedio_recaudacion_leche)