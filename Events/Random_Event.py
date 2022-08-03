import Enumerators
from Commands_Dirc import Combat, Deck_management
from Events.Combat_Event import combat_event
from Static_Data import Static_Data


def handle_event(): #Vis vi er i en by, skip event
    if Static_Data.get_current_map().landscape.type_of_landscape == Enumerators.Landscapes.City:
        pass
    else: #Ellers, finn ut hvor mange fiender og hva vi skal sloss mot, og stokk kort.
        #kan ha alternative events her (f.eks skattekister osv)
        Static_Data.set_enemies_to_defeat(combat_event())
        Deck_management.shuffle_deck()
        Combat.start_combat() #Start selve combat.