import math
import Setup
from Commands_Dirc import Harvest_Commands
from Inventory import Inventory
from Static_Data import Static_Data


def calculate_grass(current_map, list_of_sheeps):
    grass_needed = 0
    for x in range(len(list_of_sheeps)):
        grass_needed += list_of_sheeps[x].eat_amount
    actions_available = math.floor((int(current_map.amount_of_grass) / int(grass_needed)))
    Static_Data.set_Actions_Available(actions_available)
    Static_Data.set_Amount_of_Grass_eating_per_action(grass_needed)


def check_local_area():
    print(
        "There is " + str(Static_Data.get_current_map().amount_of_grass) + " grass available and this gives you " + str(
            Static_Data.get_Actions_Available()) + " turns remaining")
    if Static_Data.get_current_map().amount_of_wood > 0:
        print("There is " + str(Static_Data.get_current_map().amount_of_wood) + " wood available")
    if Static_Data.get_current_map().amount_of_stone > 0:
        print("There is " + str(Static_Data.get_current_map().amount_of_stone) + " stone available")
    if Static_Data.get_current_map().has_river:
        print("There is a river here")


def handle_input(handle_input):
    handle_input = handle_input.lower()
    handle_input = handle_input.strip()
    return handle_input


def harvest_local_area():
    print("What do you want to harvest?")
    amount_harvester = len(Static_Data.get_list_of_people())
    resource_to_gather = input()
    resource_to_gather = handle_input(resource_to_gather)
    if resource_to_gather == "wood" or resource_to_gather == "tree" or resource_to_gather == "trees":
        Harvest_Commands.harvest_wood(amount_harvester)
    elif resource_to_gather == "stone" or resource_to_gather == "rocks" or resource_to_gather == "stones" or resource_to_gather == "rock":
        Harvest_Commands.harvest_stone(amount_harvester)
    elif resource_to_gather == "fish" or resource_to_gather == "river":
        Harvest_Commands.fish_in_river()


def migrate(next_map):
    Inventory.set_temporary_food_amount(-Inventory.get_temporary_food_amount())
    Static_Data.set_current_map(next_map)
    Setup.background_info(next_map)


def create_next_areas():
    possible_areas = []
    for x in range(3):
        possible_areas.append(Setup.next_map_generation())
    for x in range(len(possible_areas)):
        if possible_areas[x].has_river:
            print("You can migrate to a " + possible_areas[x].type_of_landscape.name + " region with a river")
        else:
            print("You can migrate to a " + possible_areas[x].type_of_landscape.name + " region")
    print("Write 1 2 or 3 to migrate to that region")
    choice = input()
    if choice == "1":
        return possible_areas[0]
    elif choice == "2":
        return possible_areas[1]
    elif choice == "3":
        return possible_areas[2]
