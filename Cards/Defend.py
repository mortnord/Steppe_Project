import Background_Calculations

import Enumerators

from Cards.Base_Cards import Card
from Static_Data import Static_Data


class Defend(Card):
    def __init__(self):
        super().__init__()
        self.value = 2
        self.type_of_card = Enumerators.TypeOfCard.Defend #Dette er ett defend kort
        self.dwarfs_required = 1
        self.indicator_sprite = Enumerators.Sprites_of_planned_attack.Defend.value

    def usage(self, card_nr, target_dwarf,nr_dwarf):

        Static_Data.get_list_of_people()[target_dwarf].defend += self.value #Her legger vi til defend
        Static_Data.set_energy(self.dwarfs_required)
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr))
        nr_dwarf.has_energy = nr_dwarf.use_energy(self.dwarfs_required)
        return True