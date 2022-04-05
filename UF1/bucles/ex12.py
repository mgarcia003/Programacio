frase = input("Escriu una frase sense signes de puntuació: ")
i=0
longitud = len(frase) - 1
while i <= longitud:
    if frase[i] != " ":
        print (frase[i],end="")
    else:
        print("")
    i = i + 1
