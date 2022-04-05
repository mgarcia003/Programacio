def eliminaLletra(p,l):
    novaparaula = ""
    i = 0
    while i < len(p):
        if p[i] == l:
            novaparaula = novaparaula + "*"
        else:
            novaparaula = novaparaula + p[i]
        i += 1
    return novaparaula

print(eliminaLletra("Hola","a"))








