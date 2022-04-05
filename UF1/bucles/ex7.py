#Recorregut complet d'una string amb While
#El mateix amb una llista

frase= input("Frase: ")

i=0
cEspai=0
ultim = len(frase)-1
while i<=ultim:
    if frase[i]==" ":
        cEspai= cEspai + 1
        
    i=i+1

if cEspai >= 1:
    print(f"Hi ha {cEspai} espais")
else:
    print("No hi ha espai")

