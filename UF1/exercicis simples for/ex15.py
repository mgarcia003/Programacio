paraula = input("Paraula: ")
i = 0
parell = ""
senar = ""

for c in paraula:
    if i % 2 == 0:
        parell = parell + paraula[i]
    else:
        senar = senar + paraula[i]
    i = i + 1
print(f"{parell}\n{senar}")