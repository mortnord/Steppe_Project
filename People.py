from Static_Data import Static_Data
from Inventory import Inventory


class Person:
    ID = None

    def __init__(self):
        self.eat_amount = float(1)
        self.ID = Static_Data.get_ID()
