#Ex7.3
formt = input("Aquin format vols pasar? (k=Kelvin, f=Fahrenheit) ")
celsius = float(input("Graus Celsius? "))
if formt == "k":
    k = celsius + 274.15
    print (k)
elif formt == "f":
    f = celsius * 2
    print (f)
