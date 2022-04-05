from tkinter import *
from tkinter import messagebox

def suma():
    try:
        res = float(entN1.get()) + float(entN2.get())
        lbCalcul.config(text=str(res))
    except ValueError:
        messagebox.showwarning("ERROR","N1 i N2 han de ser números")
    except ZeroDivisionError:
        messagebox.showwarning("ERROR","No es pot dividir per 0")
    except:
        messagebox.showwarning("ERROR","Error variat")

def resta():
    try:
        res = float(entN1.get()) - float(entN2.get())
        lbCalcul.config(text=str(res))
    except ValueError:
        messagebox.showwarning("ERROR","N1 i N2 han de ser números")
    except ZeroDivisionError:
        messagebox.showwarning("ERROR","No es pot dividir per 0")
    except:
        messagebox.showwarning("ERROR","Error variat")

def multip():
    try:
        res = float(entN1.get()) * float(entN2.get())
        lbCalcul.config(text=str(res))
    except ValueError:
        messagebox.showwarning("ERROR","N1 i N2 han de ser números")
    except ZeroDivisionError:
        messagebox.showwarning("ERROR","No es pot dividir per 0")
    except:
        messagebox.showwarning("ERROR","Error variat")

def divisio():
    try:
        res = float(entN1.get()) / float(entN2.get())
        lbCalcul.config(text=str(res))
    except ValueError:
        messagebox.showwarning("ERROR","N1 i N2 han de ser números")
    except ZeroDivisionError:
        messagebox.showwarning("ERROR","No es pot dividir per 0")
    except:
        messagebox.showwarning("ERROR","Error variat")


finestra = Tk()
finestra.title("Calculadora Ex1")

lbN1 = Label(finestra, text="N1:")
lbN1.grid(row=0)

lbN2 = Label(finestra, text="N2:")
lbN2.grid(row=1)

entN1 = Entry(finestra, text="N1")
entN1.grid(row=0,column=1, columnspan=2)

entN2 = Entry(finestra, text="N2")
entN2.grid(row=1,column=1, columnspan=2)

btSuma = Button(finestra, text="SUMA", command=suma)
btSuma.grid(row=3,column=0)

btResta = Button(finestra, text="RESTA", command=resta)
btResta.grid(row=3,column=1)

btMultip = Button(finestra, text="MULTIPLICA", command=multip)
btMultip.grid(row=3,column=2)

btDivisio = Button(finestra, text="DIVIDEIX", command=divisio)
btDivisio.grid(row=3,column=3)

lbCalcul = Label(finestra, text="")
lbCalcul.grid(row=4,column=1)

mainloop()