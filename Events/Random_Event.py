import Enumerators
from Commands_Dirc import Combat, Deck_management
from Events.Combat_Event import combat_event
from Static_Data import Static_Data


def handle_event():
    if Static_Data.get_current_map().landscape.type_of_landscape == Enumerators.Landscapes.City:
        pass
    else:
        Static_Data.set_enemies_to_defeat(combat_event())
        Deck_management.shuffle_deck()
        Combat.start_combat()