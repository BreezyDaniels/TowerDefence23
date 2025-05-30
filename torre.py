import pygame as pg
import constantes as c

class Torre(pg.sprite.Sprite):
    def __init__(self, image, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.tile_x = tile_x
        self.tile_y = tile_y
        #calcular las coordenadas del centro
        self.x = (self.tile_x + 0.5) * c.TILE_SIZE
        self.y = (self.tile_y + 0.5) * c.TILE_SIZE
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)