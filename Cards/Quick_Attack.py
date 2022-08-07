import Background_Calculations
import Enumerators
from Cards.Base_Cards import Card
from Static_Data import Static_Data


class Quick_Attack(Card):
    def __init__(self):
        super().__init__()
        self.value = 1
        self.type_of_card = Enumerators.TypeOfCard.Quick_Attack
        self.dwarfs_required = 0 #Forskjellen er at dette kortet er gratis å bruke
        self.indicator_sprite = Enumerators.Sprites_of_planned_attack.Attack.value

    def usage(self, card_nr, x):
        print("Choose target enemy")

        nr_enemy_to_target = input() #Sjekk attack kort
        nr_enemy_to_target = Background_Calculations.handle_input(nr_enemy_to_target)
        nr_enemy_to_target = int(nr_enemy_to_target)
        nr_enemy_to_target = nr_enemy_to_target - 1
        Static_Data.get_enemies_to_defeat()[nr_enemy_to_target].take_damage(self.value)
        print("The goblin has " + str(
            Static_Data.get_enemies_to_defeat()[nr_enemy_to_target].health) + " health left")
        Static_Data.set_which_dwarf_to_attack(self.dwarfs_required)
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr))


