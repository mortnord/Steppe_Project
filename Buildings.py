import Enumerators
from Static_Data import Static_Data


class Building:
    Building_ID = None
    cost_to_build_wood = 0
    cost_to_build_stone = 0

    def __init__(self):
        self.Building_ID = Static_Data.get_Building_ID()


class Silo(Building):
    def __init__(self):
        super().__init__()
        self.building_slots_used = 1
        self.capacity = 60
        self.type_of_building = Enumerators.TypeOfBuilding.Silo
        self.cost_to_build_wood = 4
        self.cost_to_build_stone = 2