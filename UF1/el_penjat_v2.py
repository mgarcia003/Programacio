pEndevina = input("Introdueix una paraula: ")
pEndevina = pEndevina.upper()
longitud = len(pEndevina)
lletra = input (f"\nLletra: ")
lletra = lletra.upper()
i = 0
paraulaF = "-" * longitud
v = 8
l = []

while pEndevina != paraulaF and v >= 0:

    while i < longitud:

        if lletra in l:
            l.append(lletra)
        elif lletra == pEndevina[i]:
            paraulaF = paraulaF[:i] + lletra + paraulaF[i+1:]
            l.append(lletra)
            v = v + 1
        i = i + 1
    v = v - 1
    print(f"{paraulaF}")
    print(f"Et queden {v} vides")
    if pEndevina != paraulaF:
        print (f"Lletres dites: {l}")
        lletra = input (f"\nLletra: ")
        lletra = lletra.upper()
    i = 0

if pEndevina == paraulaF:
    print(f"\n\nCORRECTE!!")

elif pEndevina != paraulaF:
    print("INCORRECTE!! t'has quedat sense vides")
