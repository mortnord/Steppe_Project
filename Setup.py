import random

import Background_Calculations
import Commands_Dirc.Commands as Commands
import Commands_Dirc.Inventory_and_herd_management as Inventory_and_herd_management
import Enumerators
import Landscape
import People
import Sheeps
from Inventory import Inventory
from Static_Data import Static_Data


def initial_Creation(humans, male_sheeps, female_sheeps, male_lambs, female_lambs):
    list_of_people = []
    list_of_sheeps = []
    for x in range(humans):
        list_of_people.append(People.Person())
    for x in range(male_sheeps):
        list_of_sheeps.append(Sheeps.SheepMale())
    for x in range(female_sheeps):
        list_of_sheeps.append(Sheeps.SheepFemale())
    for x in range(male_lambs):
        list_of_sheeps.append(Sheeps.SheepMaleLamb())
    for x in range(female_lambs):
        list_of_sheeps.append(Sheeps.SheepFemaleLamb())
    return list_of_people, list_of_sheeps


def next_map_generation():
    map_type = random.randint(1, 3)
    map_to_return = 0
    if map_type == 1:
        map_to_return = Landscape.Steppes()
    if map_type == 2:
        map_to_return = Landscape.Wooded()
    if map_type == 3:
        map_to_return = Landscape.Hills()
    return map_to_return


def run_Game(next_map):
    running = True
    background_info(next_map)
    while running:
        Commands.check_local_area()
        print(
            "What do you want to do? Write 0 to skip a turn and graze, write 1 to look over the herd of sheeps or manage your inventory, "
            "or 2 to check the local area for resources and potentional actions, press 3 to "
            "migrate, press 4 to ")

        player_command = str(input())
        if player_command == "0":
            take_Action()
        elif player_command == "1":
            Inventory_and_herd_management.inventory_and_herd_management()
        elif player_command == "2":
            Commands.harvest_local_area()
        elif player_command == "3":
            Commands.migrate(Commands.create_next_areas())
            print("You are now in a " + Static_Data.current_map.type_of_landscape.name + " region")


def background_info(next_map):
    Background_Calculations.calculate_grass()
    Background_Calculations.calculate_max_buildings()
    Background_Calculations.has_buildings()


def grow_and_handle_sheep():
    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Male_Lamb or \
                Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Female_Lamb:
            Static_Data.get_list_of_sheeps()[x].age += 1
    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Ewe:
            lamb = random.randint(1, 2)
            if lamb == 1:
                Static_Data.get_list_of_sheeps().append(Sheeps.SheepMaleLamb())
            if lamb == 2:
                Static_Data.get_list_of_sheeps().append(Sheeps.SheepFemaleLamb())
    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Male_Lamb:
            if Static_Data.get_list_of_sheeps()[x].age >= 3:
                Static_Data.get_list_of_sheeps()[x] = Sheeps.SheepMale()

        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Female_Lamb:
            if Static_Data.get_list_of_sheeps()[x].age >= 3:
                Static_Data.get_list_of_sheeps()[x] = Sheeps.SheepFemale()


def take_Action():
    Static_Data.get_current_map().amount_of_grass -= Static_Data.get_Amount_of_Grass_eating_per_action()
    Static_Data.use_Actions_available(1)

    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Ewe:
            Inventory.set_temporary_food_amount(1)
    print("You have " + str(Inventory.get_temporary_food_amount()) + " buckets of milk after milking")
    for x in range(len(Static_Data.get_list_of_people())):
        if Inventory.get_temporary_food_amount() > 0:
            Inventory.set_temporary_food_amount((-1))
        else:
            Inventory.set_food_amount(-1)
    print("You have " + str(Inventory.get_temporary_food_amount()) + " buckets of milk after drinking")

    print("Some time passes, the sheep graze and you have 1 less action")


def setup():
    list_of_people, list_of_sheeps = initial_Creation(2, 2, 5, 3, 3)  # Humans, male sheeps, female sheeps, lambs
    Static_Data.set_list_of_people(list_of_people)
    Static_Data.set_list_of_sheeps(list_of_sheeps)
    Static_Data.set_current_map(next_map_generation())
    next_map = next_map_generation()
    run_Game(next_map)
