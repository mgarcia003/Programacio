import pygame as pg
pg.init()
pantalla = pg.display.set_mode((400,400))
pg.display.set_caption("SNAKE GAME")
pg.display.update()
fiJoc = False
while not fiJoc:
    for event in pg.event.get():
        if event .type == pg.QUIT:
            fiJoc = True
pg.quit()