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
        self.indicator_sprite = Enumerators.Sprites_Of_Planned_Attack.Healing.value

    def usage(self, card_nr, target_dwarf,nr_dwarf):

        Static_Data.get_list_of_people()[target_dwarf].health += self.value
        if Static_Data.get_list_of_people()[target_dwarf].health > Static_Data.get_list_of_people()[target_dwarf].max_health:
            Static_Data.get_list_of_people()[target_dwarf].health = Static_Data.get_list_of_people()[target_dwarf].max_health
        Static_Data.set_energy(self.dwarfs_required)
        if self.one_time:        #Vis kortet fortsatt er engangsbruk, legg det i en annen bunke som ikke blir stokket inn
                                #når man er tom for kort
            Static_Data.get_deck_list().one_time_used_cards.append(Static_Data.get_deck_list().hand.pop(card_nr))
        else: #Vis man av en eller annen grunn har gjort kortet ikke engangs, legg det i discard-bunka som normalt
            Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(
                card_nr))
        nr_dwarf.has_energy = nr_dwarf.use_energy(self.dwarfs_required)
        return True