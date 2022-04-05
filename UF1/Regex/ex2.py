import re
password = input("Password: ")
minus = "[a-z].*[a-z].*[a-z]"
mayus3 = "[A-Z]"
digits = "[0-9]"
#minim 3 minúcules
if len(password) >= 8 and len(re.findall(minus,password))>=3 and re.search(mayus3,password) and re.search(digits,password):
    print("ok")
else:
    print("ko")