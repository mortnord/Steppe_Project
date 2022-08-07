import Background_Calculations
import Enumerators
from Cards.Base_Cards import Card
from Static_Data import Static_Data

class Healing(Card):
    def __init__(self):
        super().__init__()
        self.value = 6
        self.type_of_card = Enumerators.TypeOfCard.Healing
        self.dwarfs_required = 1
        self.one_time = True
        self.indicator_sprite = Enumerators.Sprites_of_planned_attack.Healing.value
    def usage(self, card_nr, x):
        print("Choose target dwarf")
        nr_dwarf_to_target = input()
        nr_dwarf_to_target = Background_Calculations.handle_input(nr_dwarf_to_target)
        nr_dwarf_to_target = int(nr_dwarf_to_target)
        nr_dwarf_to_target = nr_dwarf_to_target - 1
        Static_Data.get_list_of_people()[nr_dwarf_to_target].health += self.value
        print("The dwarf has " + str(Static_Data.get_list_of_people()[nr_dwarf_to_target].health) + " health now")
        Static_Data.set_which_dwarf_to_attack(self.dwarfs_required)
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr))
        if self.one_time:        #Vis kortet fortsatt er engangsbruk, legg det i en annen bunke som ikke blir stokket inn
                                #når man er tom for kort
            Static_Data.get_deck_list().one_time_used_cards.append(Static_Data.get_deck_list().hand.pop(card_nr))
        else: #Vis man av en eller annen grunn har gjort kortet ikke engangs, legg det i discard-bunka som normalt
            Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(
                card_nr))