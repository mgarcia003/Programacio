class punt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class serp:
    midaCua=0

    def __init__(self,p):
        self.cap = p
        self.cua = list()

    def creix(self):
        self.midaCua += 1

    def esMenja(self):
        for p in self.cua:
            if p.x == self.cap.x and p.y == self.cap.y:
                return True
            return False

    def mou(self,direccio):
        self.cua.append(self.cap)
        self.cap = punt (self.cap.x+direccio.x,self.cap.y+direccio.y)
        if len(self.cua) > self.midaCua:
            self.cua.pop(0)

