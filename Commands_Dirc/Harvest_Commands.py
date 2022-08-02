import random

import Turn_And_Background_Actions.turn_action
from Inventory import Inventory
from Static_Data import Static_Data


def harvest_grass(amount_harvester):
    amount_harvester = amount_harvester * 5
    if Inventory.get_grass_amount() < Inventory.get_max_grass_amount():
        if Static_Data.get_current_map().landscape.amount_of_grass > amount_harvester:
            Static_Data.get_current_map().landscape.amount_of_grass -= amount_harvester
            amount_harvested = amount_harvester
        elif Static_Data.get_current_map().landscape.amount_of_grass == 0:
            amount_harvested = 0
            print("Region is out of grass")
        else:
            amount_harvested = Static_Data.get_current_map().landscape.amount_of_grass
            Static_Data.get_current_map().landscape.amount_of_grass = 0
    else:
        amount_harvested = 0
        print("You dont have enough space")

    Turn_And_Background_Actions.turn_action.take_Action()
    Inventory.set_grass_amount(amount_harvested)
    print(str(amount_harvested) + " grass harvested")
    print("You have in total " + str(Inventory.grass_amount) + " grass")
def harvest_stone(amount_harvester):
    if Inventory.get_stone_amount() < Inventory.get_max_stone_amount():
        if Static_Data.get_current_map().landscape.amount_of_stone > amount_harvester:
            Static_Data.get_current_map().landscape.amount_of_stone -= amount_harvester
            amount_harvested = amount_harvester
        elif Static_Data.get_current_map().landscape.amount_of_stone == 0:
            amount_harvested = 0
            print("Region is out of stone")
        else:
            amount_harvested = Static_Data.get_current_map().landscape.amount_of_stone
            Static_Data.get_current_map().landscape.amount_of_stone = 0
    else:
        amount_harvested = 0
        print("You dont have enough space")
    while Inventory.get_stone_amount() > Inventory.get_max_stone_amount():
        Inventory.set_stone_amount(-1)
    Turn_And_Background_Actions.turn_action.take_Action()
    Inventory.set_stone_amount(amount_harvested)
    print(str(amount_harvested) + " stone harvested")
    print("You have in total " + str(Inventory.stone_amount) + " stone")


def harvest_wood(amount_harvester):
    if Inventory.get_wood_amount() < Inventory.get_max_wood_amount():
        if Static_Data.get_current_map().landscape.amount_of_wood > amount_harvester:
            Static_Data.get_current_map().landscape.amount_of_wood -= amount_harvester
            amount_harvested = amount_harvester
        elif Static_Data.get_current_map().landscape.amount_of_wood == 0:
            amount_harvested = 0
            print("Region is out of wood")
        else:
            amount_harvested = Static_Data.get_current_map().landscape.amount_of_wood
            Static_Data.get_current_map().landscape.amount_of_wood = 0
    else:
        amount_harvested = 0
        print("You dont have enough space")
    while Inventory.get_wood_amount() > Inventory.get_max_wood_amount():
        Inventory.set_wood_amount(-1)
    Turn_And_Background_Actions.turn_action.take_Action()
    Inventory.set_wood_amount(amount_harvested)
    print(str(amount_harvested) + " wood harvested")
    print("You have in total " + str(Inventory.wood_amount) + " wood")


def fish_in_river():
    for x in range(len(Static_Data.get_list_of_people())):
        fish_chance = random.randint(1, 5)
        if fish_chance == 1:
            print("caught fish!")
            Inventory.set_food_amount(1)
        elif fish_chance == 3:
            Inventory.set_food_amount(1)
        elif fish_chance == 5:
            Inventory.set_food_amount(3)
    Turn_And_Background_Actions.turn_action.take_Action()
