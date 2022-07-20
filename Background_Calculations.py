import math

import Enumerators
from Inventory import Inventory
from Static_Data import Static_Data
from Static_Data_Bools import Static_Data_Bools


def calculate_grass():
    grass_needed = 0
    for x in range(len(Static_Data.get_list_of_sheeps())):
        grass_needed += Static_Data.get_list_of_sheeps()[x].eat_amount
    actions_available = math.floor(
        ((int(Static_Data.get_current_map().amount_of_grass) + int(Inventory.get_grass_amount())) / int(grass_needed)))
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

        if Inventory.get_buildings()[x].type_of_building == Enumerators.TypeOfBuilding.Wagon:
            Static_Data_Bools.set_Wagon_bool(True)

        if Inventory.get_buildings()[x].type_of_building == Enumerators.TypeOfBuilding.Cheesery:
            Static_Data_Bools.set_Cheesery_bool(True)


def calculate_max_storage():
    Silos = 0
    Wagons = 0
    Cheesery = 0
    for x in range(len(Inventory.get_buildings())):
        if Inventory.get_buildings()[x].type_of_building == Enumerators.TypeOfBuilding.Silo:
            Silos += Inventory.get_buildings()[x].capacity

        if Inventory.get_buildings()[x].type_of_building == Enumerators.TypeOfBuilding.Wagon:
            Wagons += Inventory.get_buildings()[x].capacity

        if Inventory.get_buildings()[x].type_of_building == Enumerators.TypeOfBuilding.Cheesery:
            Cheesery += Inventory.get_buildings()[x].capacity
    Inventory.set_max_grass_amount(10 + Silos)
    Inventory.set_max_stone_amount(10 + Wagons)
    Inventory.set_max_food_amount(10 + Wagons + Cheesery)
    Inventory.set_max_wood_amount(10 + Wagons)


def handle_input(handle_input):
    handle_input = handle_input.lower()
    handle_input = handle_input.strip()
    return handle_input


def check_local_area():
    print("There is " + str(Static_Data.get_current_map().amount_of_grass) + " grass remaining in this region")
    print("You have " + str(Inventory.get_grass_amount()) + " grass stored")
    print("This gives you " + str(Static_Data.get_Actions_Available()) + " actions left")
    if Static_Data.get_current_map().amount_of_wood > 0:
        print("There is " + str(Static_Data.get_current_map().amount_of_wood) + " wood available")
    if Static_Data.get_current_map().amount_of_stone > 0:
        print("There is " + str(Static_Data.get_current_map().amount_of_stone) + " stone available")
    if Static_Data.get_current_map().has_river:
        print("There is a river here")
