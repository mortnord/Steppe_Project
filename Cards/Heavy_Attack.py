import Background_Calculations
import Enumerators
from Cards.Base_Cards import Card
from Static_Data import Static_Data


class Heavy_Attack(Card):
    def __init__(self):
        super().__init__()
        self.value = 5
        self.type_of_card = Enumerators.TypeOfCard.Heavy_Attack
        self.dwarfs_required = 2

    def usage(self, card_nr, x):
        print("Choose target enemy")

        nr_enemy_to_target = input()
        nr_enemy_to_target = Background_Calculations.handle_input(nr_enemy_to_target)
        nr_enemy_to_target = int(nr_enemy_to_target)
        nr_enemy_to_target = nr_enemy_to_target - 1
        Static_Data.get_enemies_to_defeat()[nr_enemy_to_target].take_damage(self.value)
        print("The goblin has " + str(
            Static_Data.get_enemies_to_defeat()[nr_enemy_to_target].health) + " health left")

        Static_Data.set_which_dwarf_to_attack(self.dwarfs_required)
        Static_Data.get_deck_list().one_time_used_cards.append(Static_Data.get_deck_list().hand.pop(card_nr))


