import random

import Background_Calculations
import Enumerators
from Enemies.Basic_Enemy import Basic_Enemy
from Static_Data import Static_Data


class Goblin(Basic_Enemy): #Goblins arver masse info fra enemies
    def __init__(self):
        super().__init__()
        self.health = 5 #Goblins har 5 liv, og ikke 1
        self.sprite = Enumerators.Sprites.Goblin.value
        self.cost = 2

    def plan_attack(self): #AIen til goblin, den er tilfeldig hva den velger å gjøre, med en overvekt på defend
        chance = random.randint(1, 3)
        if chance == 3:
            self.value = random.randint(1,2)
            self.type_of_planned_attack = Enumerators.TypeOfPlannedAttack.Attack #Her planlegger vi attack
            self.type_of_planned_attack_sprite = Enumerators.Sprites_Of_Planned_Attack.Attack.value
            self.plan_target()
        else:

            self.value = random.randint(1,2)
            self.type_of_planned_attack = Enumerators.TypeOfPlannedAttack.Defend #Her planlegger vi
            self.type_of_planned_attack_sprite = Enumerators.Sprites_Of_Planned_Attack.Defend.value


    def on_death(self):
        print("The goblin dies!")