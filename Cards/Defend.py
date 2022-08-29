import Enumerators

from Cards.Base_Cards import Card
from Static_Data import Static_Data


class Defend(Card):
    def __init__(self):
        super().__init__()
        self.value = 2
        self.type_of_card = Enumerators.TypeOfCard.Defend  # Dette er ett defend kort
        self.type_of_card_general = Enumerators.Type_of_card_general.Defend
        self.energy_required = 1
        self.indicator_sprite = Enumerators.Sprites_Of_Planned_Attack.Defend.value
        self.sprite = Enumerators.Type_Card_Sprite.Defend.value

    def usage(self, card_nr, target_dwarf, nr_dwarf):
        Static_Data.get_list_of_people()[target_dwarf].defend += (self.value + nr_dwarf.bonus_defend)  # Her legger vi til defend
        Static_Data.set_energy(self.energy_required)
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr))
        nr_dwarf.has_energy = nr_dwarf.use_energy(self.energy_required)

        self.usage_card_equipment(self, nr_dwarf)

        return True
