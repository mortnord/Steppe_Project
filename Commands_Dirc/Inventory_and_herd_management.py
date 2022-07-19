import math

import Background_Calculations
import Buildings
import Enumerators
import Setup
from Commands_Dirc import Commands
from Inventory import Inventory
from Static_Data import Static_Data


def conserve_food():
    print(
        "Do you want to use an action to conserve temporary food (buckets of milk) into cheese? 3 buckets gives 1 "
        "cheese. Y/N")
    answer = input()
    if answer == "Y":
        Setup.take_Action()
        buckets_conserved = math.floor((int(Inventory.get_temporary_food_amount()) / 3))
        Inventory.set_food_amount(buckets_conserved)
        Inventory.set_temporary_food_amount(-(buckets_conserved * 3))
    Inventory.print_inventory()


def slaughter_sheep(sheep, number):
    temp_list = []
    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == sheep:
            temp_list.append(Static_Data.get_list_of_sheeps()[x])
            Inventory.set_food_amount(Static_Data.get_list_of_sheeps()[x].meat_amount)
            if len(temp_list) == number:
                break
    for x in range(len(temp_list)):
        Static_Data.get_list_of_sheeps().remove(temp_list[x])


def slaughter_Sheep_choice():
    print("Do you want to slaughter rams or ewes?")

    resource_to_gather = input()
    print("How many?")
    number = int(input())
    resource_to_gather = Commands.handle_input(resource_to_gather)
    if resource_to_gather == "ram" or resource_to_gather == "rams":
        slaughter_sheep(Enumerators.TypeOfSheep.Ram, number)
    elif resource_to_gather == "ewe" or resource_to_gather == "ewes":
        slaughter_sheep(Enumerators.TypeOfSheep.Ewe, number)


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

    print("Do you want to slaughter some sheep? Y/N")
    player_command = str(input())
    if player_command == "Y":
        slaughter_Sheep_choice()


def look_over_humans_and_inventory(list_of_people):
    for x in range(len(list_of_people)):
        print(str(list_of_people[x].ID) + " is ID ")
    Inventory.print_inventory()


def build_building(type_building):
    if Static_Data.get_max_amount_of_buildings() > Static_Data.get_current_amount_of_buildings():
        if Inventory.get_wood_amount() >= type_building.cost_to_build_wood and Inventory.get_stone_amount() >= type_building.cost_to_build_stone:
            print("Built building")
            Inventory.buildings.append(type_building)
        else:
            print("Not enough resources")
    else:
        print("Not enough building slots")

def build_options():
    print("What do you want to build? Options are")
    for type_building in Enumerators.TypeOfBuilding:
        print(type_building.value)
    building_choice = input()
    building_choice = Commands.handle_input(building_choice)
    if building_choice == "silo":
        build_building(Buildings.Silo())


def inventory_and_herd_management():
    print("Press 1 to check the sheep herd, or 2 to check the inventory, press 3 to conserve food in inventory, press 4 to enter build option")
    player_command = str(input())
    if player_command == "1":
        look_over_sheeps(Static_Data.get_list_of_sheeps())
    elif player_command == "2":
        look_over_humans_and_inventory(Static_Data.get_list_of_people())
    elif player_command == "3":
        conserve_food()
    elif player_command == "4":
        build_options()
