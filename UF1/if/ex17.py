#Ex17

c1 = int(input("costat 1: "))
c2 = int(input("costat 2: "))
c3 = int(input("costat 3: "))
if c1>0 and c2>0 and c3>0:
    if c1 == c2 == c3:
        print("El triangle es equilàter")
    elif c1 == c2 and (c1 + c2) > c3:
        print("El triangle es isòsceles")
    elif c2 == c3 and (c2 + c3) > c1:
        print("El triangle es isòsceles")
    elif c1 == c3 and (c1 + c3) > c2:
        print("El triangle es isòsceles")
    else:
        print("El triangle no es ni equilàter, ni isòsceles")
else:
    print("Numero incorrecte")
