# -*- coding: utf-8 -*-
notas={"Liza":7, "Ariel":6 , "Ana":4 ,"Julio":8 , "Javier":2 , "Clara":9}
lista_aprobados=[]

for nombre,nota in notas.items():
    if nota>=6:
        lista_aprobados.append(nombre)
print("Los alumnos aprobados son:",lista_aprobados)

