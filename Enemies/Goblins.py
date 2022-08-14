import random

import Background_Calculations
import Enumerators
from Enemies.BasicEnemy import BasicEnemy
from Static_Data import Static_Data


class Goblin(BasicEnemy): #Goblins arver masse info fra enemies
    def __init__(self):
        super().__init__()
        self.health = 5 #Goblins har 5 liv, og ikke 1
        self.sprite = Enumerators.Sprites.Goblin.value


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

    def usage(self): #Koden for hvordan goblin angriper eller defender.
        self.defend = 0 #først fjerner vi armor, siden det er dens tur til å angripe
        if self.type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Attack: #Vis vi skal gjøre skade
            target_nr = Static_Data.get_list_of_people().index(self.target) #finner vi først ut hva dwarf vi skal skade
            Static_Data.get_list_of_people()[target_nr].take_damage(self.value) #Så skader vi dwarfen
        if self.type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Defend: #For defend,
            self.defend += self.value #Så bare får vi defend


    def on_death(self):
        print("The goblin dies!")