from Generation import Initial_Generation


class Region:
    def __init__(self, x_pos, y_pos, landscape):
        self.landscape = landscape
        self.x_position = x_pos
        self.y_position = y_pos
        self.connections = []
        print(x_pos, y_pos)