import math
import Setup
from Commands_Dirc import Harvest_Commands
from Inventory import Inventory
from Static_Data import Static_Data


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
    elif resource_to_gather == "grass":
        Harvest_Commands.harvest_grass(amount_harvester)
    elif resource_to_gather == "fish" or resource_to_gather == "river":
        Harvest_Commands.fish_in_river()
    else:
        print("Invalid command")
        harvest_local_area()


def migrate(next_map):
    Inventory.set_temporary_food_amount(-Inventory.get_temporary_food_amount())
    Static_Data.set_current_map(next_map)

    Static_Data.set_growing_time(1)
    if Static_Data.get_growing_time() > 3:
        print(Static_Data.get_growing_time())
        Static_Data.set_growing_time(-Static_Data.get_growing_time())
        Setup.grow_and_handle_sheep()


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
