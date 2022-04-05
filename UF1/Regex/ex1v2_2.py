import re
patroTS = "^[A-Za-z]{4}[0,1][0-9]{2}[0,1][0-9][0-3][0-9][0-9]{4}$"
ts = ["CULO17812110001","CACA09911300002","CAGA00403050001"]
tsCorrecte = []
tsIncorrecte = []
for i in ts:
    if re.search(patroTS,i):
        print("Targeta Sanitaria Correcte")
        tsCorrecte.append(i)
    else:
        print("Targeta Sanitaria Incorrecte!!")
        tsIncorrecte.append(i)
print(f"\nTargetes Correctes:")
for c in tsCorrecte:
    print(f"{c}")
print(f"\nTargetes Incorrectes:")
for u in tsIncorrecte:
    print(f"{u}")