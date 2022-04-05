#Exercici 3 Canvi d'unitats

nom = input ("Nom: ")
pes = float(input ("Pes (Kg): "))
alçada = float(input ("Alçada (cm):"))


if nom == "" or pes <= 0 or alçada <= 0:
    print("Les dades no son correctes")
else:
    pes = pes / 0.45359237

    peus = alçada // 30

    polsades = alçada % 30

    polsadess = polsades/2.54

    print(f"Hola {nom}, peses {pes:.0f} Lbs i tens com alçada {peus:.0f}'{polsadess:.0f}\"")



