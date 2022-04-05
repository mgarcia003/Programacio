class persona:
    def __init__(self,nom,fills=[]):
        self.Nom = nom
        self.fills = fills

def descendents(p):
    for fill in p.fills:
        print(fill.Nom)
        descendents(fill)

p1 = persona("Pere")
p2 = persona("Maria")
p3 = persona("Joana")
p4 = persona("Carles")
p5 = persona("Andreu")

p1.fills = [p2,p3]
p3.fills = [p4,p5]

descendents(p1)