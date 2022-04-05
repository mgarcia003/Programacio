import re
lletresDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
patroDNI = "^[0-9]{8}["+lletresDNI+"]$"

while True:
    dni = (input("DNI: ")).upper()
    if re.search(patroDNI,dni):
        numero = int(dni[0:8])
        lletra = dni[8]
        posicio = numero%23
        lletraTeorica = lletresDNI[posicio]
        if lletra!=lletraTeorica:
            print("DNI incorrecte")
        else:
            print("DNI correcte")
    else:
        print("DNI incorrecte")