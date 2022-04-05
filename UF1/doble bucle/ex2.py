l = ["123","458","761","23","44"]
suma = 0
p = []
im = []

for i in l:
    for b in i:
        suma = suma + int(b)
    if suma % 2 == 0:
        p.append(i)
    else:
        im.append(i)
print(f"Parells: Hi ha {len(p)} parells\nSenars: Hi ha {len(im)} senars")