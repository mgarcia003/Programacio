#Recorregut complet d'una string amb While
#El mateix amb una llista

comptaA = 0
frase = input("Frase: ")

#Inicialitem índex
i = 0
ultim = len(frase)-1
while i<=ultim:
    #Tractem frase[i]
    print(frase[i])
    if frase[i] == "a":
        comptaA = comptaA + 1
    print(f"{i:0}: {frase[i]} -> {comptaA}")
    #Incrementem index
    i=i+1
print("Hi ha {comptaA} aes")
