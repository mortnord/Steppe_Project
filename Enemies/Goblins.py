import random

import Enumerators
from Enemies.BasicEnemy import BasicEnemy
from Static_Data import Static_Data


class Goblin(BasicEnemy):
    def __init__(self):
        super().__init__()

    def plan_attack(self):
        chance = random.randint(1, 3)
        if chance == 3:
            self.value_attack = 2
            self.type_of_planned_attack = Enumerators.TypeOfPlannedAttack.Attack
        else:
            self.value_defend = 2
            self.type_of_planned_attack = Enumerators.TypeOfPlannedAttack.Defend

    def plan_target(self):
        target = random.randint(1, len(Static_Data.get_list_of_people()))
        target -= 1
        self.target = Static_Data.get_list_of_people()[target]

    def usage(self):
        self.defend = 0
        if self.type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Attack:
            target_nr = Static_Data.get_list_of_people().index(self.target)
            Static_Data.get_list_of_people()[target_nr].take_damage(self.value_attack)
        if self.type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Defend:
            self.defend += self.value_defend

    def take_damage(self, value_damage):
        if self.defend > 0:
            self.defend = self.defend - value_damage
            if self.defend < 0:
                self.health -= self.defend
                self.defend = 0
        else:
            self.health -= value_damage

    def on_death(self):
        print("The goblin dies!")
