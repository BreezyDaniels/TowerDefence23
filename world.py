import pygame as pg

class World():
    def __init__(self, data, map_image):
        #esta lista vacia recibe los x e y del process waypoints
        self.waypoints = []
        self.level_data = data
        self.image = map_image

    def draw(self, surface):
        #el mapa va a empezar a dibujarse de la esquina superior izquierda
        surface.blit(self.image, (0, 0))

    def process_data(self):
        #ver data para extraer la info que quiero
        for layer in self.level_data["layers"]:
            if layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    waypoints_data = obj["polyline"]
                    self.process_waypoints(waypoints_data)
    def process_waypoints(self, data):
        #iterar entre los waypoints para extraer las coordenadas X e Y
        for point in data:
            temp_x = point.get("x") + 600 #Se tuvo que hacer un arreglo para ajustar el pathing a la pantalla por razones desconocidas
            temp_y = point.get("y") + 1
            self.waypoints.append((temp_x, temp_y))