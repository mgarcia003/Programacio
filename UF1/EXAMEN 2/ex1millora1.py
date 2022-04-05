i = 1
p = input(f"Paraula {i}: ")
frase = ""
pAturada = ["Stop","Parar","Aturar"]
while i < 10 and p not in pAturada:
    frase = frase + p + " "
    i = i + 1
    p = input(f"Paraula {i}: ")
print(frase)