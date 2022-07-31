import random
from Cards import Attack, Quick_Attack, Defend, Heavy_Attack

import Commands_Dirc.Deck_management
import Dwarfs_And_Deck.Dwarfs, Dwarfs_And_Deck.Deck
import Sheeps
import Landscape
from Static_Data import Static_Data


def start_initial_creation():
    list_of_people, list_of_sheeps, deck_list = initial_Creation(2, 2, 5, 3,
                                                      3)  # Humans, male sheeps, female sheeps, male lambs, female lambs
    Static_Data.set_list_of_people(list_of_people)
    Static_Data.set_list_of_sheeps(list_of_sheeps)
    Static_Data.set_deck_list(deck_list)

    initial_map_generation()


def initial_Creation(dwarfs, male_sheeps, female_sheeps, male_lambs, female_lambs):
    list_of_people = []
    list_of_sheeps = []
    deck_list = Dwarfs_And_Deck.Deck.Deck()
    for x in range(5):
        deck_list.content.append(Attack.Attack())
        deck_list.content.append(Defend.Defend())

    for x in range(2):
        deck_list.content.append(Quick_Attack.Quick_Attack())
    deck_list.content.append(Heavy_Attack.Heavy_Attack())
    for x in range(dwarfs):
        list_of_people.append(Dwarfs_And_Deck.Dwarfs.Dwarf())
    for x in range(male_sheeps):
        list_of_sheeps.append(Sheeps.SheepMale())
    for x in range(female_sheeps):
        list_of_sheeps.append(Sheeps.SheepFemale())
    for x in range(male_lambs):
        list_of_sheeps.append(Sheeps.SheepMaleLamb())
    for x in range(female_lambs):
        list_of_sheeps.append(Sheeps.SheepFemaleLamb())
    return list_of_people, list_of_sheeps, deck_list


def initial_map_generation():
    map_to_return = Landscape.City()
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
