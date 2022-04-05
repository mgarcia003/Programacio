import re
import pygame as pg
import time
import random
from class_punt import *
random.seed()

def missatge():
    estilFont = pg.font.SysFont("arialblack",30)
    msgFormatat = estilFont.render("BOT",True,(255,0,0))
    pantalla.blit(msgFormatat,[10,10])

def direccions(tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_a:
        return {"x":-gruix,"y":0}
    elif tecla == pg.K_RIGHT or tecla == pg.K_d:
        return {"x":+gruix,"y":0}
    elif tecla == pg.K_UP or tecla == pg.K_w:
        return {"x":0,"y":-gruix}
    elif tecla == pg.K_DOWN or tecla == pg.K_s:
        return {"x":0,"y":+gruix}
    else:
        return None

def laPalmao(x,y):
    return x < 0 or y < 0 or x > amplada or y > alcada

def nouMenjar():
    x = random.randint(0,amplada-gruix) // gruix * gruix
    y = random.randint(0,alcada-gruix) // gruix * gruix
    return {"x":x,"y":y}

def nyamNyam(x,y,m):

    return x == m["x"] and y == m["y"]

def mostrarSerp(s):
    for x,y in serp:
        pg.draw.rect(pantalla,(0,0,255),[x,y,gruix,gruix])

def serpEsMenja(s):
    cap = s[-1]
    cua = s[0:-1]
    return cap in cua

pg.init()
amplada = 600
alcada = 400
gruix = 20
velocitat = 10
serp = []
longitudSerp = 1

temporizador=pg.time.Clock()

pantalla = pg.display.set_mode((amplada,alcada))
pg.display.set_caption("SNAKE GAME")
pg.display.update()
fiJoc = False

x=amplada//2
y=alcada//2
deltaX = 0
deltaY = 0

menjar=nouMenjar()

while not fiJoc:
    for event in pg.event.get():
        if event .type == pg.QUIT:
            fiJoc = True
        if event.type == pg.KEYDOWN:
            d = direccions(event.key)
            if d:
                deltaX = d["x"]
                deltaY = d["y"]
    serp.append([x,y])
    if len(serp) > longitudSerp:
        serp.pop(0)
    x += deltaX
    y += deltaY

    pantalla.fill(color=(255,255,255))
    mostrarSerp(serp)
    pg.draw.rect(pantalla,(255,0,0),[menjar["x"],menjar["y"],gruix,gruix])

    if laPalmao(x,y) or serpEsMenja(serp):
        missatge()
        fiJoc=True
    if nyamNyam(x,y,menjar):
        menjar = nouMenjar()
        longitudSerp += 1
    pg.display.update()
    temporizador.tick(velocitat)

time.sleep(2)
pg.quit()