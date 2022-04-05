lista_menores=[]
lista_potencias= []
n=int(input("Ingresar un numero que sea menor o igual a 10:"))
nmenor=n-1
for x in range(n):
    lista_menores.append(nmenor)
    nmenor=nmenor-1
lista_menores.reverse()
print ("Los numeros menores al ingresado son:",lista_menores)
for n in lista_menores:
    lista_potencias.append(n**2)
print("Numeros menores elevados al cuadrado:",lista_potencias)
