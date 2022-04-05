#Actividad7
m_c= int(input("Ingrese el monto total de la compra:"))
p_d= 0

if m_c >=1500 and m_c <=2000:
    p_d=20
elif m_c>=1000 and m_c<=1499:
    p_d=15
elif m_c>=700 and m_c<=999:
    p_d=10
else:
    print("No hay descuento")

descuento= m_c*p_d/100
p_f=m_c-descuento
print("El precio final es:",p_f)