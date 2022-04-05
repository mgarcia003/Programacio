from tkinter import *
from tkinter import messagebox

def operacio(operador):
    if operador == "+":
        try:
            res = float(entN1.get()) + float(entN2.get())
            entRes.configure(state='normal')
            entRes.delete(0,END)
            entRes.insert(0,str(res))
            entRes.configure(state='readonly')
        except ValueError:
            messagebox.showwarning("ERROR","N1 i N2 han de ser números")
        except ZeroDivisionError:
            messagebox.showwarning("ERROR","No es pot dividir per 0")
        except:
            messagebox.showwarning("ERROR","Error variat")
    elif operador == "-":
        try:
            res = float(entN1.get()) - float(entN2.get())
            entRes.configure(state='normal')
            entRes.delete(0,END)
            entRes.insert(0,str(res))
            entRes.configure(state='readonly')
        except ValueError:
            messagebox.showwarning("ERROR","N1 i N2 han de ser números")
        except ZeroDivisionError:
            messagebox.showwarning("ERROR","No es pot dividir per 0")
        except:
            messagebox.showwarning("ERROR","Error variat")
    elif operador == "*":
        try:
            res = float(entN1.get()) * float(entN2.get())
            entRes.configure(state='normal')
            entRes.delete(0,END)
            entRes.insert(0,str(res))
            entRes.configure(state='readonly')
        except ValueError:
            messagebox.showwarning("ERROR","N1 i N2 han de ser números")
        except ZeroDivisionError:
            messagebox.showwarning("ERROR","No es pot dividir per 0")
        except:
            messagebox.showwarning("ERROR","Error variat")
    elif operador == "/":
        try:
            res = float(entN1.get()) / float(entN2.get())
            entRes.configure(state='normal')
            entRes.delete(0,END)
            entRes.insert(0,str(res))
            entRes.configure(state='readonly')
        except ValueError:
            messagebox.showwarning("ERROR","N1 i N2 han de ser números")
        except ZeroDivisionError:
            messagebox.showwarning("ERROR","No es pot dividir per 0")
        except:
            messagebox.showwarning("ERROR","Error variat")
    else:
        finestra.destroy()

finestra = Tk()
finestra.title("Calculadora Ex2")

lbN1 = Label(finestra, text="N1:")
lbN1.grid(row=0)

lbN2 = Label(finestra, text="N2:")
lbN2.grid(row=1)

entN1 = Entry(finestra, text="N1")
entN1.grid(row=0,column=1, columnspan=4)

entN2 = Entry(finestra, text="N2")
entN2.grid(row=1,column=1, columnspan=4)

lbRes = Label(finestra, text="Resultat")
lbRes.grid(row=2)

entRes = Entry(finestra)
entRes.grid(row=2, column=1, columnspan=4)
entRes.configure(state='readonly')

btSortir = Button(finestra, text="Sortir", command=lambda: operacio(""))
btSortir.grid(row=3, column=0)

btSuma = Button(finestra, text="+", command=lambda: operacio("+"))
btSuma.grid(row=3,column=1)

btResta = Button(finestra, text="-", command=lambda: operacio("-"))
btResta.grid(row=3,column=2)

btMultip = Button(finestra, text="*", command=lambda: operacio("*"))
btMultip.grid(row=3,column=3)

btDivisio = Button(finestra, text="/", command=lambda: operacio("/"))
btDivisio.grid(row=3,column=4)

mainloop()