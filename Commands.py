import math
import random

import Enumerators
import Setup
from Inventory import Inventory
from Static_Data import Static_Data


def look_over_sheeps(list_of_sheeps):
    male_sheep = 0
    female_sheep = 0
    male_lambs = 0
    female_lambs = 0
    for x in range(len(list_of_sheeps)):
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Ram:
            male_sheep += 1
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Ewe:
            female_sheep += 1
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Male_Lamb:
            male_lambs += 1
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Female_Lamb:
            female_lambs += 1

    print("You have " + str(male_sheep) + " rams")

    print("You have " + str(female_sheep) + " ewes")

    print("You have " + str(male_lambs) + " young rams")

    print("You have " + str(female_lambs) + " young ewes")

    print("You have " + str(len(list_of_sheeps)) + " sheep in total")


def look_over_humans_and_inventory(list_of_people):
    for x in range(len(list_of_people)):
        print(str(list_of_people[x].ID) + " is ID ")
    Inventory.print_inventory()


def calculate_grass(current_map, list_of_sheeps):
    grass_needed = 0
    for x in range(len(list_of_sheeps)):
        grass_needed += list_of_sheeps[x].eat_amount
    actions_available = math.floor((int(current_map.amount_of_grass) / int(grass_needed)))
    Static_Data.set_Actions_Available(actions_available)
    Static_Data.set_Amount_of_Grass_eating_per_action(grass_needed)


def check_local_area():
    print("There is " + str(Static_Data.get_current_map().amount_of_grass) + " grass available and this gives you " + str(Static_Data.get_Actions_Available()) + " turns remaining")
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


def fish_in_river():
    for x in range(len(Static_Data.get_list_of_people())):
        fish_chance = random.randint(1,3)
        if fish_chance == 1:
            print("caught fish!")
            Inventory.set_food_amount(1)
    Setup.take_Action()

def harvest_local_area():
    print("What do you want to harvest?")
    amount_harvester = len(Static_Data.get_list_of_people())
    resource_to_gather = input()
    resource_to_gather = handle_input(resource_to_gather)
    if resource_to_gather == "wood" or resource_to_gather == "tree" or resource_to_gather == "trees":
        harvest_wood(amount_harvester)
    elif resource_to_gather == "stone" or resource_to_gather == "rocks" or resource_to_gather == "stones" or resource_to_gather == "rock":
        harvest_stone(amount_harvester)
    elif resource_to_gather == "fish" or resource_to_gather == "river":
        fish_in_river()


def harvest_wood(amount_harvester):
    if Static_Data.get_current_map().amount_of_wood > amount_harvester:
        Static_Data.get_current_map().amount_of_wood -= amount_harvester
        amount_harvested = amount_harvester
    elif Static_Data.get_current_map().amount_of_wood == 0:
        amount_harvested = 0
        print("Region is out of wood")
    else:
        amount_harvested = Static_Data.get_current_map().amount_of_wood
        Static_Data.get_current_map().amount_of_wood = 0
    Setup.take_Action()
    Inventory.set_wood_amount(amount_harvested)
    print(str(amount_harvested) + " wood harvested")
    print("You have in total " + str(Inventory.wood_amount) + " wood")
    print("You have " + str(Static_Data.get_Actions_Available()) + " actions available due to grass")


def harvest_stone(amount_harvester):
    if Static_Data.get_current_map().amount_of_stone > amount_harvester:
        Static_Data.get_current_map().amount_of_stone -= amount_harvester
        amount_harvested = amount_harvester
    elif Static_Data.get_current_map().amount_of_stone == 0:
        amount_harvested = 0
        print("Region is out of stone")
    else:
        amount_harvested = Static_Data.get_current_map().amount_of_stone
        Static_Data.get_current_map().amount_of_stone = 0
    Setup.take_Action()
    Inventory.set_stone_amount(amount_harvested)
    print(str(amount_harvested) + " stone harvested")
    print("You have in total " + str(Inventory.stone_amount) + " stone")
    print("You have " + str(Static_Data.get_Actions_Available()) + " actions available due to grass")


def migrate(next_map):
    Inventory.set_temporary_food_amount(-Inventory.get_temporary_food_amount())
    Static_Data.set_current_map(next_map)
    Setup.background_info(next_map)
    print(Static_Data.get_current_map().type_of_landscape)



def conserve_food():
    print(
        "Do you want to use an action to conserve temporary food (buckets of milk) into cheese? 3 buckets gives 1 cheese. Y/N")
    answer = input()
    if answer == "Y":
        Setup.take_Action()
        buckets_conserved = math.floor((int(Inventory.get_temporary_food_amount()) / 3))
        Inventory.set_food_amount(buckets_conserved)
        Inventory.set_temporary_food_amount(-(buckets_conserved * 3))
    Inventory.print_inventory()
