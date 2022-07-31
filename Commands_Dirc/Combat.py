import Background_Calculations
import Enumerators
from Commands_Dirc import Deck_management
from Static_Data import Static_Data


def enemy_indication_round():
    for x in range(len(Static_Data.get_enemies_to_defeat())):
        Static_Data.get_enemies_to_defeat()[x].plan_attack()
        Static_Data.get_enemies_to_defeat()[x].plan_target()
        if Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Attack:
            print("Goblin " + str(x + 1) + " with health " +
                  str(Static_Data.get_enemies_to_defeat()[x].health) + " and defend " +
                  str(Static_Data.get_enemies_to_defeat()[x].defend) + " has planned an " +
                  str(Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack.value) + " with value " +
                  str(Static_Data.get_enemies_to_defeat()[x].value_attack) + " on target " +
                  str(Static_Data.get_enemies_to_defeat()[x].target.ID))

        if Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Defend:
            print("Goblin " + str(x + 1) + " with health " +
                  str(Static_Data.get_enemies_to_defeat()[x].health) + " and defend " +
                  str(Static_Data.get_enemies_to_defeat()[x].defend) + " has planned an " +
                  str(Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack.value) + " with value " +
                  str(Static_Data.get_enemies_to_defeat()[x].value_defend))


def check_for_deaths():
    for x in range(len(Static_Data.get_list_of_people())):
        if Static_Data.get_list_of_people()[x].health <= 0:
            Static_Data.get_list_of_people().remove(Static_Data.get_list_of_people()[x])
            break

    for x in range(len(Static_Data.get_enemies_to_defeat())):
        if Static_Data.get_enemies_to_defeat()[x].health <= 0:
            Static_Data.get_enemies_to_defeat()[x].on_death()
            Static_Data.get_enemies_to_defeat().remove(Static_Data.get_enemies_to_defeat()[x])
            break


def player_use_card_round():
    Static_Data.reset_which_dwarf_to_attack()
    for x in range(len(Static_Data.get_list_of_people())):
        Static_Data.get_list_of_people()[x].defend = 0
    for x in range(len(Static_Data.get_list_of_people())):
        print("Dwarf " + str(x + 1) + " is ID " + str(Static_Data.get_list_of_people()[x].ID) + " with health " + str(
            Static_Data.get_list_of_people()[x].health))
    Deck_management.draw_cards_until_full()
    while Static_Data.get_which_dwarf_to_attack() < len(Static_Data.get_list_of_people()):
        print("You have " + str((
                                            len(Static_Data.get_list_of_people()) - Static_Data.get_which_dwarf_to_attack())) + " dwarfs remaining to use")
        Deck_management.print_deck()
        print("Write number of card to use")
        use_card_nr = input()
        use_card_nr = Background_Calculations.handle_input(use_card_nr)
        use_card_nr = int(use_card_nr)
        use_card_nr -= 1
        if (len(Static_Data.get_list_of_people()) - Static_Data.get_which_dwarf_to_attack()) >= \
                Static_Data.get_deck_list().hand[use_card_nr].dwarfs_required:
            Static_Data.get_deck_list().hand[use_card_nr].usage(use_card_nr, Static_Data.get_which_dwarf_to_attack())
        check_for_deaths()

    Deck_management.discard_hand()


def enemy_use_indication_round():
    for x in range(len(Static_Data.get_enemies_to_defeat())):
        Static_Data.get_enemies_to_defeat()[x].usage()
        if len(Static_Data.get_enemies_to_defeat()) > 0:
            check_for_deaths()


def end_turn_step():
    pass


def start_combat():
    while len(Static_Data.get_enemies_to_defeat()) > 0:
        print("You have " + str(len(Static_Data.get_enemies_to_defeat())) + " enemies left")
        enemy_indication_round()
        player_use_card_round()
        enemy_use_indication_round()
        end_turn_step()
