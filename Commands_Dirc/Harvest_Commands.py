import random

import Setup
from Inventory import Inventory
from Static_Data import Static_Data


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


def fish_in_river():
    for x in range(len(Static_Data.get_list_of_people())):
        fish_chance = random.randint(1,5)
        if fish_chance == 1:
            print("caught fish!")
            Inventory.set_food_amount(1)
        elif fish_chance == 3:
            Inventory.set_food_amount(1)
        elif fish_chance == 5:
            Inventory.set_food_amount(3)
    Setup.take_Action()

