import Background_Calculations
import Enumerators
from Cards.Base_Cards import Card
from Static_Data import Static_Data


class Attack(Card):
    def __init__(self):
        super().__init__()
        self.value = 2 #verdien på attacket
        self.type_of_card = Enumerators.TypeOfCard.Attack #Sier at dette er ett attack kort
        self.dwarfs_required = 1 #Kostnaden for å bruke kortet
        self.indicator_sprite = Enumerators.Sprites_of_planned_attack.Attack.value

    def usage(self, card_nr, x): #Card_nr er hva nr kortet var i hånden når man spiller det. X er energi-kostnaden
        print("Choose target enemy")
        nr_enemy_to_target = input() ##Vi skriver her inn ett nr på hvilken fienden vi skal angripe
        nr_enemy_to_target = Background_Calculations.handle_input(nr_enemy_to_target) #Idiothåndterer tallet vi skrev inn, sjekk implementationen
        nr_enemy_to_target = int(nr_enemy_to_target) #Gjør om til tall
        nr_enemy_to_target = nr_enemy_to_target - 1 #Her må vi ta -1 fordi lister starter på 0, mens intuitivt så starter kort 1 på 1 hos oss. Så input 1 blir kort 0
        Static_Data.get_enemies_to_defeat()[nr_enemy_to_target].take_damage(self.value) #Her gjør vi damage på hva vi har valgt, sjekk implementation for detaljer
        print("The goblin has " + str(Static_Data.get_enemies_to_defeat()[nr_enemy_to_target].health) + " health left")
        Static_Data.set_which_dwarf_to_attack(self.dwarfs_required) #Her fjerner vi energien vi har brukt fra potensiell energi
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr)) #her popper vi (tar ut og legger en annen plass) kortet ut fra deck-lista,
                                                                                                    # og legger det i discard-pile lista
