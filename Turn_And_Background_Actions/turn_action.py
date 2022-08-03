import Enumerators
from Inventory import Inventory
from Static_Data import Static_Data


def take_Action(): #Dette skjer når en runde går.
    Static_Data.use_Actions_available(1) #Først, bruke en action.

    milk() #melke sauer

    graze() #sauer beite


def milk(): #Man får 1 midlertidig mat per søya man har
    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Ewe:
            Inventory.set_temporary_food_amount(1)
    print("You have " + str(Inventory.get_temporary_food_amount()) + " buckets of milk after milking")
    for x in range(len(Static_Data.get_list_of_people())): #men man spiser 2 temporary food, siden de ikke er like gode, versus 1 vanlig
        if Inventory.get_temporary_food_amount() > 0:
            Inventory.set_temporary_food_amount((-2)) #burde kanskje gjøre spising av food en annen plass...
        else:
            Inventory.set_food_amount(-1)
    print("You have " + str(Inventory.get_temporary_food_amount()) + " buckets of milk after drinking")


def graze():
    Static_Data.get_current_map().landscape.amount_of_grass -= Static_Data.get_Amount_of_Grass_eating_per_action() #her spiser vi grass
    if Static_Data.get_current_map().landscape.amount_of_grass < 0: #Vis tomt for grass, så begynner de å spise fra silo-grass
        Inventory.set_grass_amount(Static_Data.get_current_map().landscape.amount_of_grass)
        Static_Data.get_current_map().landscape.amount_of_grass = 0
        print("Your sheeps could not graze due to lack of grass, and had to eat your stored grass to graze, and you have 1 less action")
    else:
        print("Some time passes, the sheep graze and you have 1 less action")