p = input("Introdueix la paraula: ")
pFinal = ""
for c in p:
    if c < "0" or c > "9":
        pFinal = pFinal + c
print(f"{pFinal}")
