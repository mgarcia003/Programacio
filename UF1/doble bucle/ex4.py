numero = int(input("Introdueix un numero: "))
while numero != "":
    if numero <= 4:
        print("Insuficient")
    elif numero <= 5:
        print("Suficient")
    elif numero <= 6:
        print("Bé")
    elif numero <= 8:
        print("Notable")
    elif numero <= 10:
        print("Excel·lent")
    numero = int(input("Introdueix un numero: "))
