import random

from Generation import Initial_Generation
from Static_Data import Static_Data


class Region: #Map-objektet som alle kartene består av, ett landskap, posisjoner og connections.
    def __init__(self, x_pos, y_pos, landscape):
        self.landscape = landscape
        self.x_position = x_pos
        self.y_position = y_pos
        self.connections = []
        self.nr_region = landscape.Landscapes_ID
        self.scramble()
        print(x_pos, y_pos)

    def scramble(self):
        self.x_position += random.randint(-20, 20)
        self.y_position += random.randint(-20, 20)
        for x in range(len(self.connections)):
            self.connections[x].own_x = self.x_position
            self.connections[x].own_y = self.y_position
