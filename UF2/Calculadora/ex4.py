from email.policy import default
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
        entOperacio.configure(state='normal')
        entOperacio.delete(0,END)
        entOperacio.configure(state='readonly')
        S = False
    entDisplay.configure(state='normal')
    entDisplay.insert(END, str(d))
    entDisplay.configure(state='readonly')

def afegirOperacio(op):
    entDisplay.configure(state='normal')
    entDisplay.insert(END, str(op))
    entDisplay.configure(state='readonly')

def clearDisplay():
    entOperacio.configure(state='normal')
    entOperacio.delete(0,END)
    entOperacio.configure(state='readonly')
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
        op = entDisplay.get()
        entDisplay.configure(state='normal')
        entDisplay.delete(0,END)
        entDisplay.insert(END, str(res))
        entDisplay.configure(text=eval("res"))
        entDisplay.configure(state='readonly')
        entOperacio.configure(state='normal')
        entOperacio.insert(END, str(op))
        entOperacio.configure(state="readonly")
    except ZeroDivisionError:
        messagebox.showwarning("Error","No es pot dividir per 0")
        entDisplay.configure(state='normal')
        entDisplay.delete(0,END)
        entDisplay.configure(state='readonly')


#FINESTRA
finestra = Tk()
finestra.geometry("330x435")
finestra.title("Calculadora Ex4")
finestra.resizable(0,0)

#ENTRY
entOperacio =Entry(finestra, width=15, font= "Arial 15", justify="right", fg="gray", relief=FLAT)
entOperacio.grid(row=0, column=2, columnspan=4)
entOperacio.configure(state='readonly')
entDisplay = Entry(finestra, width=18, font= "Arial 25", justify="right")
entDisplay.grid(row=1, column=0, columnspan=4)
entDisplay.configure(state='readonly')


#CREACIO DE BOTONS DE NUMEROS
cCols = 0
cRows = 3
Nums = [7,8,9,4,5,6,1,2,3]
for i in Nums:
    i = Button(finestra, text=f"{i}", width=5, height=2, font= "Arial 18", bg="#CCCCCC", command=partial(afegirDigit,f"{i}"), anchor="center").grid(row=cRows, column=cCols)
    cCols += 1
    if cCols >= 3:
        cCols = 0
        cRows += 1


#CREACIO DE BOTOS DE OPERADORS
cCols = 3
cRows = 3
Nums = ["/","*","-","+"]
for i in Nums:
    i = Button(finestra, text=f"{i}", width=5, height=2, font= "Arial 18",command=partial(afegirOperacio,f"{i}"), anchor="center").grid(row=cRows, column=cCols)
    cCols += 1
    if cCols == 4:
        cCols = 3
        cRows += 1


#ALTRES BOTONS
btPar1 = Button(finestra, text="(", width=5, height=2,  font= "Arial 18", command=partial(afegirOperacio,"("), anchor="center").grid(row=2, column=0)
btPar2 = Button(finestra, text=")", width=5, height=2,  font= "Arial 18", command=partial(afegirOperacio,")"), anchor="center").grid(row=2, column=1)
btClear = Button(finestra, text="C", width=5, height=2,  font= "Arial 18", command=partial(clearDisplay), anchor="center").grid(row=2, column=2)
btBorrar = Button(finestra, text="<=", width=5, height=2,  font= "Arial 18", command=partial(popDisplay), anchor="center").grid(row=2, column=3)
btZero = Button(finestra, text="0", width=5, height=2,  font= "Arial 18", bg="#CCCCCC", command=partial(afegirDigit,"0"), anchor="center").grid(row=6, column=0)
btComa = Button(finestra, text=",", width=5, height=2,  font= "Arial 18",command=partial(afegirDigit,"."), anchor="center").grid(row=6, column=1)
btResultat = Button(finestra, text="=", width=5, height=2,  font= "Arial 18",command=partial(calcular), anchor="center").grid(row=6, column=2)
S = False

mainloop()