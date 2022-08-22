import random
from Enemies import Goblins, Slime, Demon
from Static_Data import Static_Data


def combat_event(): #Kamp event
    enemies = []
    event_cost = 0
    while event_cost < Static_Data.get_initial_difficulty():
        type_enemy = random.randint(1,len(Static_Data.get_current_map().landscape.possible_enemies))
        if Static_Data.get_current_map().landscape.possible_enemies[type_enemy - 1] == "Goblin":
            enemies.append(Goblins.Goblin())
            event_cost = add_cost_of_enemies(enemies, event_cost)
        elif Static_Data.get_current_map().landscape.possible_enemies[type_enemy - 1] == "Slime":
            enemies.append(Slime.Slime())
            event_cost = add_cost_of_enemies(enemies, event_cost)
        elif Static_Data.get_current_map().landscape.possible_enemies[type_enemy - 1] == "Demon":
            enemies.append(Demon.Demon())
            event_cost = add_cost_of_enemies(enemies, event_cost)
    enemies.pop()
    return enemies


def add_cost_of_enemies(enemies, event_cost):
    temp_cost = enemies[len(enemies) - 1].cost * len(enemies)
    event_cost += temp_cost
    return event_cost