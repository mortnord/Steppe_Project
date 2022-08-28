import random

import Enumerators
from Equipment.Base_Equipment.Base_Weapon import Base_Weapon
from Static_Data import Static_Data


class Hammer(Base_Weapon):
    text = "A basic hammer"
    sprite = Enumerators.Equipment_Weapon_Sprite.Steel_Axe.value

    def usage_card_enemy(self, using_card, using_dwarf, using_enemy):
        chance = random.randint(1, 10)
        if chance == 10:
            Static_Data.get_enemies_to_defeat()[using_enemy].stunned = True
