from functools import partial
from tkinter import *
from tkinter import messagebox

#FUNCIONS
def afegirDigit(d):
    global S
    if S == True:
        entDisplay.configure(state='normal')
        entDisplay.delete(0,END)
        entDisplay.configure(state='readonly')
        S = False
    entDisplay.configure(state='normal')
    entDisplay.insert(END, str(d))
    entDisplay.configure(state='readonly')

def afegirOperacio(op):
    entDisplay.configure(state='normal')
    entDisplay.insert(END, str(op))
    entDisplay.configure(state='readonly')

def clearDisplay():
    entDisplay.configure(state='normal')
    entDisplay.delete(0,END)
    entDisplay.configure(state='readonly')

def popDisplay():
    entDisplay.configure(state='normal')
    entDisplay.delete(len(entDisplay.get())-1)
    entDisplay.configure(state='readonly')

def calcular():
    try:
        global S
        S = True
        res = eval(entDisplay.get())
        entDisplay.configure(state='normal')
        entDisplay.delete(0,END)
        entDisplay.insert(END, str(res))
        entDisplay.configure(text=eval("res"))
        entDisplay.configure(state='readonly')
    except ZeroDivisionError:
        messagebox.showwarning("Error","No es pot dividir per 0")


#FINESTRA
finestra = Tk()
finestra.title("Calculadora Ex3")


#ENTRY
entDisplay = Entry(finestra)
entDisplay.grid(row=0, column=0, columnspan=4)
entDisplay.configure(state='readonly')


#CREACIO DE BOTONS DE NUMEROS
cCols = 0
cRows = 2
Nums = [7,8,9,4,5,6,1,2,3]
for i in Nums:
    i = Button(finestra, text=f"{i}", command=partial(afegirDigit,f"{i}")).grid(row=cRows, column=cCols)
    cCols += 1
    if cCols >= 3:
        cCols = 0
        cRows += 1


#CREACIO DE BOTOS DE OPERADORS
cCols = 3
cRows = 1
Nums = ["/","*","-","+"]
for i in Nums:
    i = Button(finestra, text=f"{i}", command=partial(afegirOperacio,f"{i}")).grid(row=cRows, column=cCols)
    cCols += 1
    if cCols == 4:
        cCols = 3
        cRows += 1


#ALTRES BOTONS
btClear = Button(finestra, text="C", command=partial(clearDisplay)).grid(row=1, column=1)
btBorrar = Button(finestra, text="<=", command=partial(popDisplay)).grid(row=1, column=2)
btZero = Button(finestra, text="0", command=partial(afegirDigit,"0")).grid(row=5, column=1)
btComa = Button(finestra, text=",", command=partial(afegirDigit,".")).grid(row=5, column=2)
btResultat = Button(finestra, text="=", command=partial(calcular)).grid(row=5, column=3)
S = False

mainloop()