import pygame as pg

class Boton():
    def __init__(self, x, y, image, single_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.single_click = single_click

    def draw(self, surface):
        action = False
        #obtener posicion del mouse
        pos = pg.mouse.get_pos()
        #chequear condiciones de mouse
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                #si el boton es de tipo 1 solo click entonces clicked = True
                if self.single_click:
                    self.clicked = True
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        #boton en pantalla     
        surface.blit(self.image, self.rect)

        return action