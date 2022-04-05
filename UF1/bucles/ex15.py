frase= input("Frase: ")
trobatEspai = 0

i=0
ultim = len(frase)-1
while i<=ultim  and trobatEspai < 3:
    if frase[i]==" ":
        trobatEspai = trobatEspai + 1
        posEspai = i
    i=i+1

if trobatEspai >= 3:
    print(f"El 3 espai esta a la posició {posEspai}")
else:
    print("No hi han 3 espais")
