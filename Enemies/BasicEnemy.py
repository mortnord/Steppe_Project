import random

from Static_Data import Static_Data


class BasicEnemy():
    def __init__(self): #Basis-klasse for fiende
        self.health = 1
        self.value = 0
        self.type_of_planned_attack = 0
        self.type_of_planned_attack_sprite = None
        self.defend = 0
        self.target = None

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