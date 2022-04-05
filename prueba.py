def menor_valor():
    valor1=int(input("Ingresar el 1er valor"))
    valor2=int(input("Ingresar el 2do valor"))
    valor3=int(input("Ingresar el 3er valor"))
    print ("El menor es:")
    if valor1<valor2 and valor1<valor3:
        print (valor1)
    else:
        if valor2<valor3:
            print(valor2)
        else:
            print(valor3)

def mayor_valor():
    valor1=int(input("Ingresar el 1er valor"))
    valor2=int(input("Ingresar el 2do valor"))
    valor3=int(input("Ingresar el 3er valor"))
    print ("El mayor es:")
    if valor1>valor2 and valor1>valor3:
        print (valor1)
    else:
        if valor2>valor3:
            print(valor2)
        else:
            print(valor3)

print("Menor valor:",menor_valor())
print("Mayor valor:",mayor_valor())

