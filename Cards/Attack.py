import Background_Calculations
import Enumerators
from Cards.Base_Cards import Card
from Static_Data import Static_Data


class Attack(Card):
    def __init__(self):
        super().__init__()
        self.value = 2 #verdien på attacket
        self.type_of_card = Enumerators.TypeOfCard.Attack #Sier at dette er ett attack kort
        self.type_of_card_general = Enumerators.Type_of_card_general.Attack
        self.dwarfs_required = 1 #Kostnaden for å bruke kortet
        self.indicator_sprite = Enumerators.Sprites_Of_Planned_Attack.Attack.value
        self.text = "This is a basic attack card"


    def usage(self, card_nr, target_enemy, nr_dwarf): #Card_nr er hva nr kortet var i hånden når man spiller det. X er energi-kostnaden

        Static_Data.get_enemies_to_defeat()[target_enemy].take_damage(self.value + nr_dwarf.bonus_attack) #Her gjør vi damage på hva vi har valgt, sjekk implementation for detaljer
        Static_Data.set_energy(self.dwarfs_required) #Her fjerner vi energien vi har brukt fra potensiell energi
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr)) #her popper vi (tar ut og legger en annen plass) kortet ut fra deck-lista,
        nr_dwarf.has_energy = nr_dwarf.use_energy(self.dwarfs_required)                                                                               # og legger det i discard-pile lista
        self.usage_card_equipment(self, nr_dwarf)
        return True
