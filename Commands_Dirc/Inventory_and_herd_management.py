import math

import Enumerators
import Setup
from Inventory import Inventory
from Static_Data import Static_Data


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


def inventory_and_herd_management():
    print("Press 1 to check the sheep herd, or 2 to check the inventory, press 3 to conserve food in inventory")
    player_command = str(input())
    if player_command == "1":
        look_over_sheeps(Static_Data.get_list_of_sheeps())
    elif player_command == "2":
        look_over_humans_and_inventory(Static_Data.get_list_of_people())
    elif player_command == "3":
        conserve_food()
