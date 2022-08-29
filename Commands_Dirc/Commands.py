import Background_Calculations
import Turn_And_Background_Actions.Grow_Sheep

from Inventory import Inventory
from Static_Data import Static_Data


def migrate(next_map):  # Verdien inn er neste region vi skal til
    Inventory.set_temporary_food_amount(
        -Inventory.get_temporary_food_amount())  # Vi fjerner all temporary food (melk enn så leng)
    Inventory.set_food_amount(-len(Static_Data.get_list_of_people()))
    Static_Data.set_current_map(next_map)  # Vi bytter hva som er nåværende map, med det nye
    Background_Calculations.background_info()
    Static_Data.set_growing_time(1)  # Øker verdien på kortid sauer ska vokse / få lam
    if Static_Data.get_growing_time() > 3:  # Vis Større enn 3, så får vi lam og sauer vokser opp
        print(Static_Data.get_growing_time())
        Static_Data.set_growing_time(-Static_Data.get_growing_time())  # Reset growing timen
        Turn_And_Background_Actions.Grow_Sheep.grow_and_handle_sheep()  # Få sauer til å vokse, sjekk implementationen
