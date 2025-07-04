#Importo la librería pygame con el alias pg para escribir menos,
import pygame as pg
#Importo un archivo llamado constants como c, donde tengo definidas constantes como tamaño de pantalla y FPS,
import constantes as c
#importo clases
from enemigo import Enemigo
from world import World
from torre import Torre
from boton import Boton
#Importo json para poder traer las coordenadas de el pathing de los enemigos desde tile
import json

#Inicializo todos los módulos de pygame antes de usarlos,
pg.init()

#Creo un reloj para poder controlar los FPS del juego,
clock = pg.time.Clock()

#Creo la ventana del juego usando el ancho y alto que definí en el archivo de constantes,
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
#Le pongo un título a la ventana del juego,
pg.display.set_caption("Tower Defence")

#Variables del juego
#poner_torres False esconde boton cancel y no deja poner torres, True muestra boton cancel y permite poner torres
poner_torres = False

#Cargar imagenes
map_image = pg.image.load('levels/map.png').convert_alpha()
enemigo_image = pg.image.load('assets/images/enemigo.png').convert_alpha()
cursor_torre = pg.image.load('assets/images/cursor_torre.png').convert_alpha()
#botones
comprar_torre_image = pg.image.load('assets/images/buy_turret.png').convert_alpha()
cancel_image = pg.image.load('assets/images/cancel.png').convert_alpha()


#Cargo las coordenadas del json exportado de tile  
with open('levels/POLIPOINTS.tmj') as file:
  world_data = json.load(file)

def crear_torre(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  #calcular el numero secuencial del tile
  mouse_tile_num = (mouse_tile_y * c.COLUMNAS) + mouse_tile_x
  #chequear si en ese slot se pueden poner torres
  if world.tile_map[mouse_tile_num] == 0:
    #chequear que no haya ya una torreta en ese slot
    space_is_free = True
    for torre in torre_group:
      if (mouse_tile_x, mouse_tile_y) == (torre.tile_x, torre.tile_y):
        space_is_free = False
    #si el espacio esta libre entonces crea la torre
    if space_is_free == True: 
      nueva_torre = Torre(cursor_torre, mouse_tile_x, mouse_tile_y)
      torre_group.add(nueva_torre)

#Crear mundo
world = World(world_data, map_image)
world.process_data()

#Crear grupos
enemigo_group = pg.sprite.Group()
torre_group = pg.sprite.Group()



enemigo = Enemigo(world.waypoints, enemigo_image)
enemigo_group.add(enemigo)

#Crear botones
boton_torre = Boton(c.SCREEN_WIDTH + 30, 120, comprar_torre_image, True)
boton_cancel = Boton(c.SCREEN_WIDTH + 50, 180, cancel_image, True)

#Mientras run sea True el juego sigue corriendo,
run = True
#Bucle principal del juego,
while run:

  #Hago que el juego corra a la cantidad de FPS que definí (limito los fotogramas por segundo)
  clock.tick(c.FPS)

  ##############################
  # SECCION UPDATE
  ##############################

  #actualizar grupos
  enemigo_group.update()

  ##############################
  # SECCION DRAW
  ##############################

  screen.fill("grey100")

  #Dibujar nivel
  world.draw(screen)

  #dibujar pathing de enemigo
  pg.draw.lines(screen, "grey0", False, world.waypoints)

  #dibujar botones
  #boton de buy tower
  if boton_torre.draw(screen):
    poner_torres = True
  #Si queres poner una torre entonces ahi mostra el boton CANCEL
  #boton cancel
  if poner_torres == True:
    #mostrar torre en el cursor
    cursor_rect = cursor_torre.get_rect()
    cursor_pos = pg.mouse.get_pos()
    cursor_rect.center = cursor_pos
    if cursor_pos[0] <= c.SCREEN_WIDTH:
      screen.blit(cursor_torre, cursor_rect)
    if boton_cancel.draw(screen):
      poner_torres = False

  #dibujar grupos
  enemigo_group.draw(screen)
  torre_group.draw(screen)

  

  # Recorro todos los eventos que suceden (como cerrar la ventana, apretar teclas, etc.)
  for event in pg.event.get():
    # Si el evento es cerrar la ventana, corto el bucle y salgo del juego
    if event.type == pg.QUIT:
      run = False
    #click de mouse
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
      mouse_pos = pg.mouse.get_pos()
      #chequear si el mouse esta en el area del juego
      if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
        if poner_torres == True:
          crear_torre(mouse_pos)

  #actualizar display
  pg.display.flip()

#Cuando salgo del bucle, cierro pygame y libero los recursos,
pg.quit()