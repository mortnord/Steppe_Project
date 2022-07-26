import random
from Enemies import Goblins


def combat_event():
    enemies = []
    amount_enemies = random.randint(1, 3)
    for x in range(amount_enemies):
        enemies.append(Goblins.Goblin())
    print("You find " + str(amount_enemies) + " goblins" )
    return enemies