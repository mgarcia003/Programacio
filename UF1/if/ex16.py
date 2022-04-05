#Ex16

c1 = int(input("costat 1: "))
c2 = int(input("costat 2: "))
c3 = int(input("costat 3: "))
if c1>0 and c2>0 and c3>0:
    if c1 == c2 == c3:
        print("El triangle es equilàter")
    else:
        print("El triangle no es equilàter")
else:
    print("Numero incorrecte")
