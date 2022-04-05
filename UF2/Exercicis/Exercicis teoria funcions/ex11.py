def eliminaEspais(s):
    novaS = ""
    s = s.lower()
    i = 0
    while i < len(s):
        if s[i] in ("à","á","è","é","ì","í","ò","ó","ù","ú","ç","ñ"):
            if s[i] in "àá":
                novaS = novaS + "a"
            elif s[i] in "èé":
                novaS = novaS + "e"
            elif s[i] in "ìí":
                novaS = novaS + "i"
            elif s[i] in "òó":
                novaS = novaS + "o"
            elif s[i] in "ùú":
                novaS = novaS + "u"
            elif s[i] == "ç":
                novaS = novaS + "c"
            elif s[i] == "ñ":
                novaS = novaS + "n"
        else:
            novaS = novaS + s[i]
        i += 1
    return novaS

print(eliminaEspais("Holñá què tàlç"))