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

    def usage(self, card_nr, x):
        print("Choose target dwarf") #Sjekk attack kort
        nr_enemy_to_target = input()
        nr_enemy_to_target = Background_Calculations.handle_input(nr_enemy_to_target)
        nr_enemy_to_target = int(nr_enemy_to_target)
        nr_enemy_to_target = nr_enemy_to_target - 1
        Static_Data.get_list_of_people()[nr_enemy_to_target].defend += self.value #Her legger vi til defend
        print("The dwarf has " + str(Static_Data.get_list_of_people()[nr_enemy_to_target].defend) + " armor now")
        Static_Data.set_which_dwarf_to_attack(self.dwarfs_required)
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr))