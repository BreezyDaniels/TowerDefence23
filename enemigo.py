import pygame as pg
from pygame.math import Vector2
import math

class Enemigo (pg.sprite.Sprite):
    def __init__(self, waypoints, image): 
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2 
        self.angle = 0
        self.original_image = image
        #lo siguiente es para que la imagen del enemigo pueda rotar sin perder calidad
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.mover()
        self.rotar()

    def mover(self):
        #definir waypoint target
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        #el enemigo llego al final del pathing
        else:
            self.kill()
        #calcular distandcia al objetivo
        dist = self.movement.length()
        #chequear si la distancia es mas grande que la velocidad del enemigo
        if dist >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            self.target_waypoint += 1
       

    def rotar (self):
        #calcular distancia al siguiente waypoint
        dist = self.target - self.pos 
        #usar distancia para calcular el angulo
        self.angle = math.degrees (math.atan2(-dist[1], dist[0]))
        #rotar imagen y actualizar rectangulo
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
      