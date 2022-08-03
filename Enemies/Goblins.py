import random

import Enumerators
from Enemies.BasicEnemy import BasicEnemy
from Static_Data import Static_Data


class Goblin(BasicEnemy): #Goblins arver masse info fra enemies
    def __init__(self):
        super().__init__()
        self.health = 5 #Goblins har 5 liv, og ikke 1

    def plan_attack(self): #AIen til goblin, den er tilfeldig hva den velger å gjøre, med en overvekt på defend
        chance = random.randint(1, 3)
        if chance == 3:
            self.value_attack = 2
            self.type_of_planned_attack = Enumerators.TypeOfPlannedAttack.Attack #Her planlegger vi attack
        else:
            self.value_defend = 2
            self.type_of_planned_attack = Enumerators.TypeOfPlannedAttack.Defend #Her planlegger vi defend

    def usage(self): #Koden for hvordan goblin angriper eller defender.
        self.defend = 0 #først fjerner vi armor, siden det er dens tur til å angripe
        if self.type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Attack: #Vis vi skal gjøre skade
            target_nr = Static_Data.get_list_of_people().index(self.target) #finner vi først ut hva dwarf vi skal skade
            Static_Data.get_list_of_people()[target_nr].take_damage(self.value_attack) #Så skader vi dwarfen
        if self.type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Defend: #For defend,
            self.defend += self.value_defend #Så bare får vi defend


    def on_death(self):
        print("The goblin dies!")
