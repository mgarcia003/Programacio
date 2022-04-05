#Ex 21

dni= input("Introdueix el teu DNI: ")

lletra = "TRWAGMYFPDXBNJZSQVHLCKE"

num = int(dni[0:8])

pos = num%23

lletraT = lletra[pos]

lletraE = dni[-1]

if lletraE == lletraT:
    print ("El DNI introduit es correcte")
else:
    print ("El DNI introduit es incorrecte")
