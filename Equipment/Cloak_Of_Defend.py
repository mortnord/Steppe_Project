import random

import Enumerators
from Equipment.Base_Equipment.Base_Cloak import Base_Cloak


class Cloak_Of_Defend(Base_Cloak):
    text = "Gives a 25% chance to duplicate Defend cards on self"
    sprite = Enumerators.Equipment_Cloak_Sprite.Cloak_of_Defend.value

    def usage_card(self, using_card, using_dwarf):
        roll_nr = random.randint(1, 4)
        if roll_nr == 1 and using_card.type_of_card == Enumerators.TypeOfCard.Defend:
            using_dwarf.defend += using_card.value + using_dwarf.bonus_defend
