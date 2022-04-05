llista = [["Joan",145,75],["Marta",128,74],["Paco",120,60],["Maria",185,95],["Anna",165,90]]
c = 0
hipo = 0
nor = 0
pre = 0
hiper1 = 0
hiper2 = 0
crisi = 0
g = "-" * 64
while c < len(llista):
    l = llista[c]
    if l[1] < 80 or l[2] < 60:
        hipo = hipo + 1
    elif (l[1] >= 80 and l[1] <= 119) and (l[2] >= 60 and l[2] <= 79):
        nor = nor + 1
    elif (l[1] >= 120 and l[1] <= 139) or (l[2] >= 80 and l[2] <= 89):
        pre = pre + 1
    elif (l[1] >= 140 and l[1] <= 159) or (l[2] >= 90 and l[2] <= 99):
        hiper1 = hiper1 + 1
    elif (l[1] >= 180) or (l[2] >= 110):
        crisi = crisi + 1
    elif (l[1] >= 160) or (l[2] >= 100):
        hiper2 = hiper2 + 1
    c = c + 1
print(f"Nivell de Tensió                                Núm. de Pacients\n{g}")
print(f"Hipotensió{hipo:>54}\nNormal{nor:>58}\nPrehipertensió{pre:>50}\nHipertensió Grau 1 (HTA1){hiper1:>39}\nHipertensió Grau 2 (HTA2){hiper2:>39}\nCrisis Hipertensiva{crisi:>45}")