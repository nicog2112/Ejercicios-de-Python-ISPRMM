friar1 = {"enero": 10000, "febrero": 8500, "marzo": 12500, "abril": 11200}

friar2 = {"enero": 9500, "febrero": 8700, "marzo": 12100, "abril": 14000}

friar3 = {"enero": 11000, "febrero": 9500, "marzo": 12000, "abril": 10200}

sucursales={'friar1':friar1,'friar2':friar2,'friar3':friar3}
menor_recaudacion=999999999
mayor_recaudacion=0
#mes y la recaudacion mayor en la sucursal 3
mes_mayor_recaudacion_f3=''
mayor_recaudacion_f3=0
#Obtener la sumatoria de las recaudaciones  de la sucursal friar2
sum_recaudacion_f2=0
#Obtener la sumatoria , de las 3 sucursales, para el mes de marzo
sum_total=0

for sucursales,lista_recaudacion in sucursales.items():
    for mes,recaudacion in lista_recaudacion.items():
        if recaudacion>mayor_recaudacion:
            mayor_recaudacion=recaudacion
        if recaudacion<menor_recaudacion:
            menor_recaudacion=recaudacion
        if sucursales=='friar3':
            if recaudacion>mayor_recaudacion_f3:
                mayor_recaudacion_f3=recaudacion
                mes_mayor_recaudacion_f3=mes
        if sucursales == 'friar2':
            sum_recaudacion_f2=sum_recaudacion_f2+recaudacion
        sum_total=sum_total+recaudacion

print('MAYOR RECAUDACION={} // MENOR RECAUDACION={}' .format(mayor_recaudacion,menor_recaudacion))
print('MES DE MAYOR RECAUDACION EN LA SUCURSAL 3 ES {} CON ${}' .format(mes_mayor_recaudacion_f3,mayor_recaudacion_f3) )
print('SUMATORIAS DE LAS RECAUDACIONES DE LA SUCURSAL 2 ES DE ${}'.format(sum_recaudacion_f2))
print('RECAUDACION TOTAL ES DE ${}' .format(sum_total))