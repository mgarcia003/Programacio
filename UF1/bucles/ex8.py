#Ex8

frase = input("Introdueix una frase amb numeros i lletres: ")
i=0
ultim = len(frase)-1
numeros = ""

while i <= ultim:
    if frase[i] >= "0" and frase[i] <= "9":
        numeros = numeros + frase[i]
    i = i + 1
print(numeros)
