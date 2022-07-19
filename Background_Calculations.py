import math

import Enumerators
from Inventory import Inventory
from Static_Data import Static_Data
from Static_Data_Bools import Static_Data_Bools


def calculate_grass():
    grass_needed = 0
    for x in range(len(Static_Data.get_list_of_sheeps())):
        grass_needed += Static_Data.get_list_of_sheeps()[x].eat_amount
    actions_available = math.floor((int(Static_Data.get_current_map().amount_of_grass) / int(grass_needed)))
    Static_Data.set_Actions_Available(actions_available)
    Static_Data.set_Amount_of_Grass_eating_per_action(grass_needed)


def calculate_max_buildings():
    male_sheep = 0

    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Ram:
            male_sheep += 1
    building_slots_available = int(math.floor(male_sheep / 2))
    Static_Data.set_max_amount_of_buildings(building_slots_available)


def has_buildings():
    for x in range(len(Inventory.get_buildings())):
        if Inventory.get_buildings()[x].type_of_building == Enumerators.TypeOfBuilding.Silo:
            Static_Data_Bools.set_Silo_bool(True)
