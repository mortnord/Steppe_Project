import random

import Enumerators
from Equipment.Base_Equipment.Base_Cloak import Base_Cloak


class Cloak_Of_Defend(Base_Cloak):
    def usage_card(self, using_card, using_dwarf):
        roll_nr = random.randint(1,3)
        if roll_nr == 1 and using_card.type_of_card == Enumerators.TypeOfCard.Defend:
            using_dwarf.defend += using_card.value + using_dwarf.bonus_defend
