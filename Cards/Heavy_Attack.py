import Background_Calculations
import Enumerators
from Cards.Base_Cards import Card
from Static_Data import Static_Data


class Heavy_Attack(Card):
    def __init__(self):
        super().__init__()
        self.value = 5
        self.type_of_card = Enumerators.TypeOfCard.Heavy_Attack
        self.type_of_card_general = Enumerators.Type_of_card_general.Attack
        self.dwarfs_required = 1
        self.one_time = True #Dette kortet er engangsbruk per kamp
        self.indicator_sprite = Enumerators.Sprites_Of_Planned_Attack.Attack.value

    def usage(self, card_nr, target_enemy,nr_dwarf):
        Static_Data.get_enemies_to_defeat()[target_enemy].take_damage(
            self.value  + nr_dwarf.bonus_attack)  # Her gjør vi damage på hva vi har valgt, sjekk implementation for detaljer
        Static_Data.set_energy(self.dwarfs_required)  # Her fjerner vi energien vi har brukt fra potensiell energi


        if self.one_time:        #Vis kortet fortsatt er engangsbruk, legg det i en annen bunke som ikke blir stokket inn
                                #når man er tom for kort
            Static_Data.get_deck_list().one_time_used_cards.append(Static_Data.get_deck_list().hand.pop(card_nr))
        else: #Vis man av en eller annen grunn har gjort kortet ikke engangs, legg det i discard-bunka som normalt
            Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(
                card_nr))
        nr_dwarf.has_energy = nr_dwarf.use_energy(self.dwarfs_required)
        self.usage_card_equipment(self, nr_dwarf)
        return True


