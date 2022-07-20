import random

import People
import Sheeps
import Landscape
from Static_Data import Static_Data


def start_initial_creation():
    list_of_people, list_of_sheeps = initial_Creation(2, 2, 5, 3,
                                                      3)  # Humans, male sheeps, female sheeps, male lambs, female lambs
    Static_Data.set_list_of_people(list_of_people)
    Static_Data.set_list_of_sheeps(list_of_sheeps)

    initial_map_generation()


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


def initial_map_generation():
    map_type = random.randint(1, 3)
    map_to_return = 0
    if map_type == 1:
        map_to_return = Landscape.Steppes()
    if map_type == 2:
        map_to_return = Landscape.Wooded()
    if map_type == 3:
        map_to_return = Landscape.Hills()
    Static_Data.set_current_map(map_to_return)


# Temporary
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
