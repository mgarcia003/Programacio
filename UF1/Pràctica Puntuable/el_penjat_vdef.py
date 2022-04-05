import random
z = "-" * 15
#TRIAR IDIOMA
idioma = input("En quin idioma vols jugar? [CAS|CAT|ANG]: ")
idioma = idioma.upper()

#TRIAR NIVELL
nivell = int(input(f"\nNivells\n{z}\nNivell 1: 10 vides\nNivell 2: 8 vides\nNivell 3: 7 vides\nNivell 4: 6 vides\nNivell 5: 5 vides\n{'-'*20}\nAmb quina dificultat vols jugar?: "))
if nivell == 1:
    v = 10
elif nivell == 2:
    v = 8
elif nivell == 3:
    v = 7
elif nivell == 4:
    v = 6
elif nivell == 5:
    v = 5

#CASTELLA
if idioma == "CAS":
    pEndevina = random.choice(open("cas.txt").readlines())
    longitud = len(pEndevina)
    lletra = input (f"\nLetra: ")
    lletra = lletra.upper()
    i = 0
    paraulaF = "-" * longitud
    l = []

    while pEndevina != paraulaF and v > 0:
            while i < longitud:
                if lletra == pEndevina[i]:
                    paraulaF = paraulaF[:i] + lletra + paraulaF[i+1:]
                    if lletra not in l:
                        v = v + 1
                i = i + 1
            v = v - 1
            if lletra not in l:
                l.append(lletra)
            print(f"{paraulaF}")
            print(f"Te quedan {v} vidas")
            if pEndevina != paraulaF:
                print (f"Lletras dichas: {l}")
                lletra = input (f"\nLetra: ")
                lletra = lletra.upper()
            i = 0

    if pEndevina == paraulaF:
        print(f"\n\nCORRECTO!!")

    elif pEndevina != paraulaF:
        print(f"\n\nINCORRECTE!! t'has quedat sense vides, la paraula era {pEndevina}")

#CATALA
elif idioma == "CAT":
        pEndevina = random.choice(open("cat.txt").readlines())
        pEndevina = pEndevina.upper()
        longitud = len(pEndevina)
        lletra = input (f"\nLletra: ")
        lletra = lletra.upper()
        i = 0
        paraulaF = "-" * longitud
        l = []

        while pEndevina != paraulaF and v > 0:
            while i < longitud:
                if lletra == pEndevina[i]:
                    paraulaF = paraulaF[:i] + lletra + paraulaF[i+1:]
                    if lletra not in l:
                        v = v + 1
                i = i + 1
            v = v - 1
            if lletra not in l:
                l.append(lletra)
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
            print(f"\n\nINCORRECTE!! t'has quedat sense vides, la paraula era {pEndevina}")

#ANGLES
elif idioma == "ANG":
        pEndevina = random.choice(open("ang.txt").readlines())
        pEndevina = pEndevina.upper()
        longitud = len(pEndevina)
        lletra = input (f"\nWord: ")
        lletra = lletra.upper()
        i = 0
        paraulaF = "-" * longitud
        l = []

        while pEndevina != paraulaF and v > 0:
            while i < longitud:
                if lletra == pEndevina[i]:
                    paraulaF = paraulaF[:i] + lletra + paraulaF[i+1:]
                    if lletra not in l:
                        v = v + 1
                i = i + 1
            v = v - 1
            if lletra not in l:
                l.append(lletra)
            print(f"{paraulaF}")
            print(f"You have {v} lives left")
            if pEndevina != paraulaF:
                print (f"spoken letters: {l}")
                lletra = input (f"\nWord: ")
                lletra = lletra.upper()
            i = 0

        if pEndevina == paraulaF:
            print(f"\n\nCORRECTE!!")

        elif pEndevina != paraulaF:
            print(f"\n\nINCORRECTE!! t'has quedat sense vides, la paraula era {pEndevina}")