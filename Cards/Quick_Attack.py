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

    def usage(self, card_nr, target_enemy):
        Static_Data.get_enemies_to_defeat()[target_enemy].take_damage(
            self.value)  # Her gjør vi damage på hva vi har valgt, sjekk implementation for detaljer
        Static_Data.set_energy(self.dwarfs_required)  # Her fjerner vi energien vi har brukt fra potensiell energi
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr))
        return True

