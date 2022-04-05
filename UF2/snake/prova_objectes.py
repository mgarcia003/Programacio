from datetime import date
class alumne:
    def __init__(self,nom,cognoms,dataNaix):
        self.nom=nom
        self.cognoms=cognoms
        self.dataNaixement = dataNaix
        self.materies=[]
    def edat(self):
        return date.today().year - self.dataNaixement.year
    def matricula(self,materia):
        self.materies.append(materia)
        
a1 = alumne("Marc","Garcia",date(2003,10,11))
#a2 = alumne("Pepe ...
print (a1.nom,a1.cognoms,a1.dataNaixement, a1.edat())