import re
from datetime import datetime,date
patroTS = "^[A-Za-z]{4}[0,1][0-9]{2}[0,1][0-9][0-3][0-9][0-9]{4}$"
ts = (input("Targeta Sanitaria: ")).upper()
if int(ts[5:7]) >= 23:
    comprovar_data = ("19"+ts[5:7]+"-"+ts[7:9]+"-"+ts[9:11])
else:
    comprovar_data = ("20"+ts[5:7]+"-"+ts[7:9]+"-"+ts[9:11])
try:
    datetime.strptime(comprovar_data, '%Y-%m-%d')
    dataOK = True
except:
    dataOK = False
while ts != "":
    if re.search(patroTS,ts) and dataOK == True:
        print("Targeta Sanitaria Correcte")
    else:
        print("Targeta Sanitaria Incorrecte!!")
    ts = (input("Targeta Sanitaria: ")).upper()
    if int(ts[5:7]) >= 23:
        comprovar_data = ("19"+ts[5:7]+"-"+ts[7:9]+"-"+ts[9:11])
    else:
        comprovar_data = ("20"+ts[5:7]+"-"+ts[7:9]+"-"+ts[9:11])
    try:
        datetime.strptime(comprovar_data, '%Y-%m-%d')
        dataOK = True
    except:
        dataOK = False