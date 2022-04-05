#Ex20
dia = int(input("Quin dia es: "))
Mes = int(input("En quin mes estem: "))
Any = int(input("En quin any estem: "))

a = (14 - Mes) / 12
y = Any - a
m = Mes + 12 * a - 2

d = (5 + dia + y + y/4 + (31*m)/12) % 7
d = int(d)
if d == 0:
    print ("Diumenge")
elif d == 1:
    print ("Dilluns")
elif d == 2:
    print ("Dimarts")
elif d == 3:
    print ("Dimecres")
elif d == 4:
    print ("Dijous")
elif d == 5:
    print ("Divendres")
elif d == 6:
    print ("Disabte")
else:
    print("Error")
