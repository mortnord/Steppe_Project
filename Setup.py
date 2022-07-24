import Background_Calculations
import Commands_Dirc.Commands as Commands
import Commands_Dirc.Inventory_and_herd_management as Inventory_and_herd_management
import Commands_Dirc.Migration
import Commands_Dirc.Deck_management
import Generation.Initial_Generation
import Turn_And_Background_Actions.turn_action

from Static_Data import Static_Data


def run_Game():
    running = True
    while running:

        background_info()
        Background_Calculations.check_local_area()
        print(
            "What do you want to do? Write 0 to skip a turn and graze, write 1 to look over the herd of sheeps or manage your inventory or build, "
            "or 2 to check the local area for resources and potential actions, press 3 to "
            "migrate, press 4 to ")

        player_command = str(input())
        if player_command == "0":
            Turn_And_Background_Actions.turn_action.take_Action()
        elif player_command == "1":
            Inventory_and_herd_management.inventory_and_herd_management()
        elif player_command == "2":
            Commands.harvest_local_area()
        elif player_command == "3":
            Commands.migrate(Commands_Dirc.Migration.create_next_areas())
            print("You are now in a " + Static_Data.current_map.type_of_landscape.name + " region")
        elif player_command == "4":
            Commands_Dirc.Deck_management.print_deck()
        else:
            print("Invalid command, prøv igjen")


def background_info():
    Background_Calculations.calculate_grass()
    Background_Calculations.calculate_max_buildings()
    Background_Calculations.has_buildings()
    Background_Calculations.calculate_max_storage()

    print("Your sheep need to graze " + str(Static_Data.get_Amount_of_Grass_eating_per_action()) + " grass per action")


def setup():
    Generation.Initial_Generation.start_initial_creation()
    run_Game()
