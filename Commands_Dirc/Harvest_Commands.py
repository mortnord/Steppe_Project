import random

import Turn_And_Background_Actions.turn_action
from Inventory import Inventory
from Static_Data import Static_Data


def harvest_grass(amount_harvester):  # verdien inn er hvor mange som kan høste (i dette tilfellet 1 per dverg)
    amount_harvester = amount_harvester * 5  # Vi høster grass effektivt, så får 5 per høster
    if Inventory.get_grass_amount() < Inventory.get_max_grass_amount():  # Så lenge vi ikke har max mengden så går det fint
        if Static_Data.get_current_map().landscape.amount_of_grass > amount_harvester:  # Så lenge det er nok grass på bakken til å det ikke blir tomt
            Static_Data.get_current_map().landscape.amount_of_grass -= amount_harvester  # så fjernes grass fra landscapet
            amount_harvested = amount_harvester  # og legges i en midlertidig variable på hvor mye vi har høstet
        elif Static_Data.get_current_map().landscape.amount_of_grass == 0:  # Vis tomt
            amount_harvested = 0
            print("Region is out of grass")  # Da er det tomt da...
        else:
            amount_harvested = Static_Data.get_current_map().landscape.amount_of_grass  # Vis ikke tomt, men ikke nok til en full høsting, så får vi alt vi kan.
            Static_Data.get_current_map().landscape.amount_of_grass = 0  # Og så er det tomt etterpå
    else:
        amount_harvested = 0  # Vis vi har fult inventory, så får vi ingenting
        print("You dont have enough space")

    Turn_And_Background_Actions.turn_action.take_Action()  # Å høste grass tar tid, så da går det en runde, sjekk implementation for detaljer
    Inventory.set_grass_amount(amount_harvested) #Så legger vi grasset inn i inventoriet
    print(str(amount_harvested) + " grass harvested") #skriv hvor mye vi høster
    print("You have in total " + str(Inventory.grass_amount) + " grass") #Og hvor mye vi har nå


def harvest_stone(amount_harvester): #Sjekk grass, bare her får vi ikke en 5x effekt siden det er wood
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


def harvest_wood(amount_harvester): #sjekk grass, bare ingen 5x effekt her heller
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


def fish_in_river(): #I områder med elv, kan vi fiske
    for x in range(len(Static_Data.get_list_of_people())): #hver person fisker
        fish_chance = random.randint(1, 5) #Trill en 5 sided terning (heh, internspøk).
        if fish_chance == 1: #Vis 1, får vi fisk, så da får vi 1 mat
            print("caught fish!")
            Inventory.set_food_amount(1)
        elif fish_chance == 3: #Med 3 får vi og fisk
            Inventory.set_food_amount(1)
        elif fish_chance == 5: #med 5 får vi en svær fisk og masse mat
            Inventory.set_food_amount(3)
    Turn_And_Background_Actions.turn_action.take_Action() #Det tar tid å fiske, sjekk implementation for detaljer
