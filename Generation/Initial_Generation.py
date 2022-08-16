import random

from Cards import Attack, Quick_Attack, Defend, Heavy_Attack, Healing
import Dwarfs_And_Deck.Dwarfs, Dwarfs_And_Deck.Deck
import Sheeps
from Map_Dirc import Landscape, Map
from Static_Data import Static_Data
from Equipment import Steel_Axe, Steel_Armor, Healing_Ring

def start_initial_creation():  # Her lager vi oppsettet av objekter
    list_of_people, list_of_sheeps, deck_list = initial_Creation(2, 2, 5, 3,
                                                                 3)  # Humans, male sheeps, female sheeps, male lambs, female lambs
    Static_Data.set_list_of_people(list_of_people)  # Dwarfs i dwarfs lista
    Static_Data.set_list_of_sheeps(list_of_sheeps)  # sauer i sauelista
    Static_Data.set_deck_list(deck_list)  # kort i kortstokken

    initial_map_generation()  # Lag map


def initial_Creation(dwarfs, male_sheeps, female_sheeps, male_lambs, female_lambs):
    list_of_people = []
    list_of_sheeps = []
    deck_list = Dwarfs_And_Deck.Deck.Deck()  # Lag ett nytt deck-objekt
    for x in range(5):  # Legg til 5 av hver attack og defend
        deck_list.content.append(Attack.Attack())
        deck_list.content.append(Defend.Defend())

    for x in range(3):  # 2 Quick attacks
        deck_list.content.append(Quick_Attack.Quick_Attack())
    deck_list.content.append(Heavy_Attack.Heavy_Attack())  # Og en heavy attack
    deck_list.content.append(Healing.Healing())  #
    for x in range(dwarfs):  # legg til ønsket mengde dwarfs
        list_of_people.append(Dwarfs_And_Deck.Dwarfs.Dwarf())
    list_of_people[0].weapon = Steel_Axe.Steel_Axe()
    list_of_people[1].armor = Steel_Armor.Steel_Armor()
    list_of_people[0].ring = Healing_Ring.Healing_Ring()
    for x in range(male_sheeps):  # Ønsket mengde sauer og sauetyper
        list_of_sheeps.append(Sheeps.SheepMale())
    for x in range(female_sheeps):
        list_of_sheeps.append(Sheeps.SheepFemale())
    for x in range(male_lambs):
        list_of_sheeps.append(Sheeps.SheepMaleLamb())
    for x in range(female_lambs):
        list_of_sheeps.append(Sheeps.SheepFemaleLamb())
    return list_of_people, list_of_sheeps, deck_list  # returner alt dette


def initial_map_generation():
    Map.map_generation()  # lag selve mappet, sjekk implementation for detaljer

    # Finn første punktet (alså byen man starter i)
    Static_Data.set_current_map(Static_Data.get_map_with_regions()[0])


# Temporary
def next_map_generation():
    map_type = random.randint(1, 10)  # Tilfeldig generert hva landskap det blir
    map_to_return = 0

    if map_type == 2:
        map_to_return = Landscape.Wooded()
    elif map_type == 1:
        map_to_return = Landscape.Hills()
    else:
        map_to_return = Landscape.Steppes()
    return map_to_return
