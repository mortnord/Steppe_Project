import Background_Calculations
import Enumerators
from Inventory import Inventory
from Static_Data import Static_Data


def take_Action():  # Dette skjer når en runde går.
    Static_Data.use_Actions_available(1)  # Først, bruke en action.
    Background_Calculations.background_info()  # Background info som actions osv
    milk()  # melke sauer

    graze()  # sauer beite


def milk():  # Man får 1 midlertidig mat per søya man har
    for sheep in Static_Data.get_list_of_sheeps():
        if sheep.type_of_sheep == Enumerators.TypeOfSheep.Ewe:
            Inventory.set_temporary_food_amount(1)
    for dwarf in Static_Data.get_list_of_people():  # men man spiser 2 temporary food, siden de ikke er like gode,
        # versus 1 vanlig
        if Inventory.get_temporary_food_amount() > 0:
            Inventory.set_temporary_food_amount((-2))  # burde kanskje gjøre spising av food en annen plass...
        else:
            Inventory.set_food_amount(-1)


def graze():
    Static_Data.get_current_map().landscape.amount_of_grass -= Static_Data.get_Amount_of_Grass_eating_per_action()
    # her spiser vi grass
    if Static_Data.get_current_map().landscape.amount_of_grass < 0:  # Vis tomt for grass, så begynner de å spise fra
        # silo-grass
        Inventory.set_grass_amount(Static_Data.get_current_map().landscape.amount_of_grass)
        Static_Data.get_current_map().landscape.amount_of_grass = 0
