
#Actividad4
M="M"
F="F"
edad=int(input("Ingresar la edad:"))
sexo=input("Ingresar el sexo *M* para masculino y *F* para femenino:")
if edad<13 and sexo==M:
    print("Es un niño")
elif edad<13 and sexo ==F:
    print("Es una niña")
elif edad>13 and edad<18 and sexo==M:
    print("Es un adolescente")
elif edad>13 and edad<=18 and sexo==F:
    print("Es una adolescente")
else:
    print("Es Mayor de edad")

