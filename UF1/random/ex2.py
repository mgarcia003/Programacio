import random
alumnes = ["Pere","Joan","Maria"]
repe = []
a = random.choice(alumnes)
i = True

while not (a in repe):
    print(f"{a}")
    repe.append(a)
    a = random.choice(alumnes)
print(f"{a}")
