import pygame as pg
import time
import random
from classesjoc import *
random.seed()


def missatge():
    estilFont = pg.font.SysFont("arialblack",30)
    msgFormatat = estilFont.render("La cagaste",True,colors["vermell"])
    pantalla.blit(msgFormatat,[10,10])

def direccions(tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_a:
        return punt(-gruix,0)
    elif tecla == pg.K_RIGHT or tecla == pg.K_s:
        return punt(+gruix,0)
    elif tecla == pg.K_UP or tecla == pg.K_w:
        return punt(0,-gruix)
    elif tecla == pg.K_DOWN or tecla == pg.K_d:
        return punt(0,+gruix)
    else:
        return None

def foraPantalla(s):
    return s.cap.x<0 or s.cap.y<0 or s.cap.x>amplada or s.cap.y>alcada

def nouMenjar():
    x =random.randint(0,amplada-gruix)//gruix*gruix
    y =random.randint(0,alcada-gruix)//gruix*gruix
    return punt(x,y)

def nyamNyam(s,menjar):
    return s.cap.x == menjar.x and s.cap.y == menjar.y

def mostrarSerp(s):
    pg.draw.rect(pantalla,colors["verd"],[s.cap.x,s.cap.y,gruix,gruix])
    for p in s.cua:
        pg.draw.rect(pantalla,colors["blau"],[p.x,p.y,gruix,gruix])

colors = {"blau"    : (0,0,255),
          "vermell" : (255,0,0),
          "blanc"   : (255,255,255),
          "verd"    : (0,255,0)
         }


pg.init()

amplada = 600
alcada = 400
gruix = 20
velocitat = 10

x = amplada//2
y = alcada//2

vibora = serp(punt(x,y))

temporitzador = pg.time.Clock()
pantalla = pg.display.set_mode((amplada,alcada))
pg.display.set_caption("La víbora")
pg.display.update()

direccio = punt(0,0)
fiJoc = False

menjar = nouMenjar()
while not fiJoc:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fiJoc = True
        if event.type == pg.KEYDOWN:
            direccio = direccions(event.key)
            if direccio:
                delta = direccio

    vibora.mou(direccio)
    
    pantalla.fill(colors["blanc"])
    mostrarSerp(vibora)
    pg.draw.rect(pantalla,colors["vermell"],[menjar.x,menjar.y,gruix,gruix])

    if foraPantalla(vibora) or vibora.esMenja():
        missatge()
        fiJoc = True
        
    if nyamNyam(vibora,menjar):
        menjar = nouMenjar()
        vibora.creix()
        
    pg.display.update()
    temporitzador.tick(velocitat)

time.sleep(2)    
pg.quit()