frase = input("Escriu una frase sense signes de puntuació: ")
c=0
for i in frase:
    if frase[c] != " ":
        print (frase[c],end="")
    else:
        print("")
    c = c + 1