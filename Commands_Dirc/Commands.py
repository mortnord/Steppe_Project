import Turn_And_Background_Actions.Grow_Sheep
from Background_Calculations import handle_input
from Commands_Dirc import Harvest_Commands
from Inventory import Inventory
from Static_Data import Static_Data


def harvest_local_area():
    print("What do you want to harvest?")
    amount_harvester = len(Static_Data.get_list_of_people())
    resource_to_gather = input()
    resource_to_gather = handle_input(resource_to_gather)
    if resource_to_gather == "wood" or resource_to_gather == "tree" or resource_to_gather == "trees":
        Harvest_Commands.harvest_wood(amount_harvester)
    elif resource_to_gather == "stone" or resource_to_gather == "rocks" or resource_to_gather == "stones" or resource_to_gather == "rock":
        Harvest_Commands.harvest_stone(amount_harvester)
    elif resource_to_gather == "grass":
        Harvest_Commands.harvest_grass(amount_harvester)
    elif resource_to_gather == "fish" or resource_to_gather == "river":
        Harvest_Commands.fish_in_river()
    else:
        print("Invalid command")
        harvest_local_area()


def migrate(next_map):
    Inventory.set_temporary_food_amount(-Inventory.get_temporary_food_amount())
    Static_Data.set_current_map(next_map)

    Static_Data.set_growing_time(1)
    if Static_Data.get_growing_time() > 3:
        print(Static_Data.get_growing_time())
        Static_Data.set_growing_time(-Static_Data.get_growing_time())
        Turn_And_Background_Actions.Grow_Sheep.grow_and_handle_sheep()
