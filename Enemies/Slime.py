import random

import Enumerators
from Enemies.Basic_Enemy import Basic_Enemy


class Slime(Basic_Enemy):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.sprite = Enumerators.Sprites.Slime.value
        self.cost = 2

    def plan_attack(self):  # AIen til slime, den er tilfeldig hva den velger å gjøre, med en overvekt på defend
        self.value = random.randint(1, 2)
        self.type_of_planned_attack = Enumerators.TypeOfPlannedAttack.Attack  # Her planlegger vi attack
        self.type_of_planned_attack_sprite = Enumerators.Sprites_Of_Planned_Attack.Attack.value
        self.plan_target()

    def on_death(self):
        print("The slime dies!")
