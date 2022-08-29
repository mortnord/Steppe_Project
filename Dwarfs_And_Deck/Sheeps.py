import Enumerators
from Static_Data import Static_Data


class Sheep:
    ID = None

    def __init__(self):
        self.ID = Static_Data.get_ID()


class SheepFemale(Sheep):  # Info om sauer og typer av de
    def __init__(self):
        super().__init__()
        self.eat_amount = float(1)
        self.type_of_sheep = Enumerators.TypeOfSheep.Ewe
        self.meat_amount = 3


class SheepMaleLamb(Sheep):
    def __init__(self):
        super().__init__()
        self.eat_amount = 0.5
        self.type_of_sheep = Enumerators.TypeOfSheep.Male_Lamb
        self.age = 0


class SheepFemaleLamb(Sheep):
    def __init__(self):
        super().__init__()
        self.eat_amount = 0.5
        self.type_of_sheep = Enumerators.TypeOfSheep.Female_Lamb
        self.age = 0


class SheepMale(Sheep):
    def __init__(self):
        super().__init__()
        self.eat_amount = 1.5
        self.type_of_sheep = Enumerators.TypeOfSheep.Ram
        self.meat_amount = 4
