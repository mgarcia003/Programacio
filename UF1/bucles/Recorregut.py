#Recorregut complet d'una string amb While
#El mateix amb una llista

frase= input("Frase: ")
trobatEspai = False


#Inicialitzem índex
i=0
ultim = len(frase)-1
while i<=ultim  and not trobatEspai:
    #tractem frase[i]
    if frase[i]==" ":
        trobatEspai=True
        posEspai=i
    #Incremetem l'índex
    i=i+1

if trobatEspai:
    print(f"Hi ha espai a la posició {posEspai}")
else:
    print("No hi ha espai")
