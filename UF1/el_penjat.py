pEndevina = input("Introdueix una paraula: ")
longitud = len(pEndevina)
lletra = input (f"\nLletra: ")q
i = 0
paraulaF = "-" * longitud
v = 10

while pEndevina != paraulaF and v >= 0:

    while i < longitud:

        if lletra == pEndevina[i]:
            paraulaF = paraulaF[:i] + lletra + paraulaF[i+1:]
            v = v + 1  
        i = i + 1
    v = v - 1
    print(f"{paraulaF}")
    print(f"Et queden {v} vides")
    if pEndevina != paraulaF:
        lletra = input (f"\nLletra: ")    
    i = 0
    
if pEndevina == paraulaF:
    print(f"\n\nCORRECTE!!")

elif pEndevina != paraulaF:
    print("INCORRECTE!! t'has quedat sense vides")
