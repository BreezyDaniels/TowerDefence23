#Importo la librería pygame con el alias pg para escribir menos,
import pygame as pg
#Importo un archivo llamado constants como c, donde tengo definidas constantes como tamaño de pantalla y FPS,
import constantes as c
#importo clases
from enemigo import Enemigo
from world import World
#Importo json para poder traer las coordenadas de el pathing de los enemigos desde tile
import json

#Inicializo todos los módulos de pygame antes de usarlos,
pg.init()

#Creo un reloj para poder controlar los FPS del juego,
clock = pg.time.Clock()

#Creo la ventana del juego usando el ancho y alto que definí en el archivo de constantes,
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
#Le pongo un título a la ventana del juego,
pg.display.set_caption("Tower Defence")

#Cargar imagenes
map_image = pg.image.load('levels/map.png').convert_alpha()
enemigo_image = pg.image.load('assets/images/enemigo.png').convert_alpha()

#Cargo las coordenadas del json exportado de tile  
with open('levels/POLIPOINTS.tmj') as file:
  world_data = json.load(file)

#Crear mundo
world = World(world_data, map_image)
world.process_data()

#Crear grupos
enemigo_group = pg.sprite.Group()



enemigo = Enemigo(world.waypoints, enemigo_image)
enemigo_group.add(enemigo)


#Mientras run sea True el juego sigue corriendo,
run = True
#Bucle principal del juego,
while run:

  # Hago que el juego corra a la cantidad de FPS que definí (limito los fotogramas por segundo)
  clock.tick(c.FPS)

  screen.fill("grey100")

  #Dibujar nivel
  world.draw(screen)

  #dibujar pathing de enemigo
  pg.draw.lines(screen, "grey0", False, world.waypoints)

  #actualizar grupos
  enemigo_group.update()

  #dibujar grupos
  enemigo_group.draw(screen)

  

  # Recorro todos los eventos que suceden (como cerrar la ventana, apretar teclas, etc.)
  for event in pg.event.get():
    # Si el evento es cerrar la ventana, corto el bucle y salgo del juego
    if event.type == pg.QUIT:
      run = False

  #actualizar display
  pg.display.flip()

#Cuando salgo del bucle, cierro pygame y libero los recursos,
pg.quit()