import re
patroTS = "^[A-Za-z]{4}[0,1][0-9]{2}[0,1][0-9][0-3][0-9][0-9]{4}$"
ts = (input("Targeta Sanitaria: ")).upper()
while ts != "":
    if re.search(patroTS,ts):
        print("Targeta Sanitaria Correcte")
    else:
        print("Targeta Sanitaria Incorrecte!!")
    ts = (input("Targeta Sanitaria: ")).upper()