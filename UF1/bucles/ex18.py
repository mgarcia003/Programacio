paraula = input("Paraula: ")
c = 0
i = 0

cA = False
cE = False
cI = False
cO = False
cU = False

while c <= len(paraula) -1:
    if paraula[c] == "a":
        cA = True
        i = i + 1
    elif paraula[c] == "e":
        cE = True
        i = i + 1
    elif paraula[c] == "i":
        cI = True
        i = i + 1
    elif paraula[c] == "o":
        cO = True
        i = i + 1
    elif paraula[c] == "u":
        cU = True
        i = i + 1
    c = c + 1


if cA == True and cE == True and cI == True and cO == True and cU == True:
    print("La paraula conte les 5 vocals")
else:
    print("La paraula no conte les 5 vocals")
    
