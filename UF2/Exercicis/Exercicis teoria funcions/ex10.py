def eliminaAccents(nom):
    nomNet = ""
    i = 0
    while i < len(nom):
        if nom[i] != " ":
            nomNet = nomNet + nom[i]
        i += 1
    return nomNet