#Ex23

codi = input("Introdueix un codi RGB: ")
r = codi[1:3]
g = codi[3:5]
b = codi[5:]

if r == g == b:
    print("Escala de grisos")
elif r > g and r > b:
    print ("Predomina el vermell")
elif g > r and g > b:
    print ("Predomina el verd")
elif b > r and b > g:
    print ("Predomina el blau")
elif r == g and r > b:
    print ("No predomina cap, estem parlant d’un color dintre de l’escala de grisos.")
elif r == b and g > b:
    print ("No predomina cap, estem parlant d’un color dintre de l’escala de grisos.")
elif b == r and b > g:
    print ("No predomina cap, estem parlant d’un color dintre de l’escala de grisos."
elif g == b and b > r:
    print ("No predomina cap, estem parlant d’un color dintre de l’escala de grisos.")
