import arcade

import Background_Calculations
import Generation.Initial_Generation
from GUI_Dirc import GUI, Combat_View
from Static_Data_Bools import Static_Data_Bools
from Static_Data import Static_Data


def run_Game(): #Hoved-delen av backend koden.

    if Static_Data_Bools.get_combat():
        pass
    else:
        pass
        # background_info() #Background info som actions osv
        # Background_Calculations.check_local_area()
        # print(
        #     "What do you want to do? Write 0 to skip a turn and graze, write 1 to look over the herd of sheeps or manage your inventory or build, "
        #     "or 2 to check the local area for resources and potential actions, press 3 to "
        #     "migrate, press 4 to ")
        # player_command = str(input())
        # player_command = Background_Calculations.handle_input(player_command)
        # if player_command == "0":#Hva vi skal gjøre
        #     turn_action.take_Action()
        # elif player_command == "1":
        #     Inventory_and_herd_management.inventory_and_herd_management()
        # elif player_command == "2":
        #     Commands.harvest_local_area()

        # elif player_command == "4":
        #     Deck_management.print_deck()
        # else:
        #     print("Invalid command, prøv igjen")




def setup():
    Generation.Initial_Generation.start_initial_creation()
    Background_Calculations.background_info()  # Background info som actions osv
    Background_Calculations.check_local_area()
    window = arcade.Window(600, 600, "TEST")
    Static_Data.set_window(window)
    map_view = GUI.Map_View()
    Static_Data.get_window().show_view(map_view)
    map_view.setup()
    arcade.run()