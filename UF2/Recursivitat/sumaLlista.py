def suma(llista):
    if len(llista)==1:
        return llista[0]
    else:
        return suma(llista[0:len(llista)//2]) + suma(llista[len(llista)//2:])

print(suma([1,2,3,4,5]))