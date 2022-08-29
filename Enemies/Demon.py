import random

import Enumerators
from Enemies.Basic_Enemy import Basic_Enemy


class Demon(Basic_Enemy):
    def __init__(self):
        super().__init__()
        self.health = 10  # Demons har 10 liv, og ikke 1
        self.sprite = Enumerators.Sprites.Demon.value
        self.cost = 6

    def plan_attack(self):
        chance = random.randint(1, 2)
        if chance == 2:
            self.value = random.randint(3, 4)
            self.type_of_planned_attack = Enumerators.TypeOfPlannedAttack.Attack  # Her planlegger vi attack
            self.type_of_planned_attack_sprite = Enumerators.Sprites_Of_Planned_Attack.Attack.value
            self.plan_target()
        else:

            self.value = random.randint(1, 1)
            self.type_of_planned_attack = Enumerators.TypeOfPlannedAttack.Defend  # Her planlegger vi
            self.type_of_planned_attack_sprite = Enumerators.Sprites_Of_Planned_Attack.Defend.value

    def on_death(self):
        pass
