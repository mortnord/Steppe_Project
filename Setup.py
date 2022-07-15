import random

import Commands
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
            "What do you want to do? Write 0 to skip a turn and graze, write 1 to look over the herd of sheeps, "
            "or 2 to look over the humans and "
            "inventory management, or 3 to check the local area for resources and potentional actions, press 4 to "
            "migrate")

        player_command = str(input())
        if player_command == "0":
            take_Action()
        elif player_command == "1":
            Commands.look_over_sheeps(Static_Data.get_list_of_sheeps())
        elif player_command == "2":
            Commands.look_over_humans_and_inventory(Static_Data.get_list_of_people())
            Commands.conserve_food()
        elif player_command == "3":
            Commands.harvest_local_area()
        elif player_command == "4":
            Commands.migrate(next_map_generation())


def background_info(next_map):
    Commands.calculate_grass(Static_Data.get_current_map(), Static_Data.get_list_of_sheeps())




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


def setup():
    list_of_people, list_of_sheeps = initial_Creation(2, 2, 5, 3, 3)  # Humans, male sheeps, female sheeps, lambs
    Static_Data.set_list_of_people(list_of_people)
    Static_Data.set_list_of_sheeps(list_of_sheeps)
    Static_Data.set_current_map(next_map_generation())
    next_map = next_map_generation()
    run_Game(next_map)
