import random


class Region:  # Map-objektet som alle kartene består av, ett landskap, posisjoner og connections.
    def __init__(self, x_pos, y_pos, landscape, zoom_multiplier):
        self.landscape = landscape
        self.x_position = x_pos
        self.y_position = y_pos
        self.connections = []
        self.nr_region = landscape.Landscapes_ID
        self.scramble(zoom_multiplier)

    def scramble(self, zoom_multiplier):
        zoom_multiplier = zoom_multiplier / 10
        self.x_position += random.randint(-int(zoom_multiplier), zoom_multiplier)
        self.y_position += random.randint(-int(zoom_multiplier), zoom_multiplier)
        for connections in self.connections:
            connections.own_x = self.x_position
            connections.own_y = self.y_position
