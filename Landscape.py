import random

import Enumerators
from Static_Data import Static_Data


class Landscape:
    Landscapes_ID = None
    amount_of_grass = 0
    amount_of_wood = 0
    amount_of_stone = 0

    def __init__(self):
        self.Landscapes_ID = Static_Data.get_Landscape_ID()
        self.has_river = river_generation()


class Steppes(Landscape):
    def __init__(self):
        super().__init__()
        self.amount_of_grass = 40 + random.randint(0, 30)
        self.type_of_landscape = Enumerators.Landscapes.Steppes


class Wooded(Landscape):
    def __init__(self):
        super().__init__()
        self.amount_of_grass = 10 + random.randint(0, 30)
        self.amount_of_wood = 3 + random.randint(0, 6)
        self.type_of_landscape = Enumerators.Landscapes.Wooded


class Hills(Landscape):
    def __init__(self):
        super().__init__()
        self.amount_of_grass = 20 + random.randint(0, 30)
        self.amount_of_stone = 5 + random.randint(3, 10)
        self.type_of_landscape = Enumerators.Landscapes.Hills


def river_generation():
    river_chance = random.randint(1, 5)
    if river_chance == 3:
        return True
    else:
        return False
