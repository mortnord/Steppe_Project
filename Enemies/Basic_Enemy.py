import random

import Enumerators
from Static_Data import Static_Data


class Basic_Enemy():
    def __init__(self): #Basis-klasse for fiende
        self.health = 1
        self.value = 0
        self.type_of_planned_attack = 0
        self.type_of_planned_attack_sprite = None
        self.defend = 0
        self.target = None
        self.cost = 0
        self.stunned = False

    def take_damage(self, value_damage): #En basisklasse av ta skade, samme som dwarf sin.
        if self.defend > 0:
            self.defend = self.defend - value_damage
            if self.defend < 0:
                self.health += self.defend
                self.defend = 0
        else:
            self.health -= value_damage

    def plan_target(self): #Her velger vi target tilfeldig av lista over dwarfs
        target = random.randint(1, len(Static_Data.get_list_of_people()))
        target -= 1
        self.target = Static_Data.get_list_of_people()[target]
    def usage(self):
        self.defend = 0  # først fjerner vi armor, siden det er dens tur til å angripe
        if self.type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Attack:  # Vis vi skal gjøre skade
            target_nr = Static_Data.get_list_of_people().index(
                self.target)  # finner vi først ut hva dwarf vi skal skade
            Static_Data.get_list_of_people()[target_nr].take_damage(self.value)  # Så skader vi dwarfen
        if self.type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Defend:  # For defend,
            self.defend += self.value  # Så bare får vi defend
    def plan_attack(self):
        pass
    def on_death(self):
        pass