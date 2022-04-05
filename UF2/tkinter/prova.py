from functools import partial
from tkinter import *

def saludar(partDia):
    if partDia == "Mati":
        inici = "Bon dia"
    elif partDia == "Tarda":
        inici = "Bona tarda"
    else:
        inici = "Bona nit"
    salutacio = f"{inici} {entNom.get()} {entCognom.get()}"
    lbSalutacio.config(text=salutacio)

finestra = Tk()
finestra.title("PROVA")

lbNom = Label(finestra, text="Nom:")
lbNom.grid(row=0)

lbCognom = Label(finestra, text="Cognom:")
lbCognom.grid(row=1)

entNom = Entry(finestra, text="NOM")
entNom.grid(row=0,column=1)

entCognom = Entry(finestra, text="COGNOM")
entCognom.grid(row=1,column=1)

btSaluda = Button(finestra, text="SALUDA", command=partial(saludar,"Tarda"))

btSaluda = Button(finestra, text="SALUDA", command=lambda: saludar("Tarda"))
lbSalutacio = Label(finestra, text="")





btSaluda.grid(row=3,columnspan=2)
lbSalutacio.grid(row=4,columnspan=2)

mainloop()
