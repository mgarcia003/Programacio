#Ex22

codi = input("Introdueix el codi de l'ou: ")

print("El teu ou es:")
if codi[0] == "0":
    print ("     - Producció ecològica")
elif codi[0] == "1":
    print ("    - Producció Campera")
elif codi[0] == "2":
    print ("    - Producció de Terra")
elif codi[0] == "3":
    print ("    - Producció de Jaula")


if codi[1:3] == "ES":
    print ("    - Criat a España")
    if codi[3:5] == "08":
        print ("    - Criat dins de Catalunya")
        print ("    - Criat a Barcelona")
    elif codi[3:5] == "17":
        print ("    - Criat dins de Catalunya")
        print ("    - Criat a Girona")
    elif codi[3:5] == "25":
        print ("    - Criat dins de Catalunya")
        print ("    - Criat a Lleida")
    elif codi[3:5] == "43":
        print ("    - Criat dins de Catalunya")
        print ("    - Criat a Tarragona")
    else:
        print ("    - Criat fora de Catalunya")
else:
    print ("    - Criat fora d'España")



