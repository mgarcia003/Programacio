votacio = {}
nom = input("Quin nom apareix a la papereta? ")
while nom != "":
    if nom in votacio:
        votacio[nom] += 1
    else:
        votacio[nom] = 1
    nom = input("Quin nom apareix a la papereta? ")
result, val = 0, ''
for nom,quantitat in votacio.items():
    if result < quantitat:
        result = quantitat
        val = nom
del votacio[val]
delegat = val
result, val = 0, ''
for nom,quantitat in votacio.items():
    if result < quantitat:
        result = quantitat
        val = nom
subdelegat = val
print(f"El delegat/da es en/a {delegat} i el subdelegat/da es en/a {subdelegat}")