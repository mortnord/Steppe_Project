import random
from Enemies import Goblins, Slime
from Static_Data import Static_Data


def combat_event(): #Kamp event
    enemies = []
    amount_enemies = random.randint(2, 3) #Generer mengden enemies
    for x in range(amount_enemies):
        type_enemy = random.randint(1,len(Static_Data.get_current_map().landscape.possible_enemies))
        if (Static_Data.get_current_map().landscape.possible_enemies[type_enemy-1] == "Goblin"):
            enemies.append(Goblins.Goblin())
        if (Static_Data.get_current_map().landscape.possible_enemies[type_enemy-1] == "Slime"):
            enemies.append(Slime.Slime())
    return enemies