#Recorregut complet d'una string amb While
#El mateix amb una llista
frase = input("Frase: ")
#Inicialitem índex
i=0
ultim = len(frase)-1
while i<=ultim:
    #Tractem frase[i]
    print(frase[i])
    #Incrementem index
    i=i+1
