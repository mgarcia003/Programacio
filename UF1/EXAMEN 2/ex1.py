i = 1
p = input(f"Paraula {i}: ")
frase = ""
while i < 10:
    frase = frase + p + " "
    i = i + 1
    p = input(f"Paraula {i}: ")
print(frase)