import random
from Enemies import Goblins


def combat_event(): #Kamp event
    enemies = []
    amount_enemies = random.randint(2, 3) #Generer mengden enemies
    for x in range(amount_enemies):
        enemies.append(Goblins.Goblin()) #Lag nye gobling objekter, som er faktiske enemeies.
    return enemies