import random
random.seed()
lletra = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(lletra)
paraula = input("Paraula: ")
llista = []
c = 0
punts = 0
while lletra != paraula[0] or paraula not in llista:
    llista.append(paraula)
    paraula = input("Paraula: ")
for i in llista:
    while c < len(i):
        c += 1
    punts = punts + c
    c = 0
punts = punts + len(llista)*10
print(f"Punts: {punts}")