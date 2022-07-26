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


def do_damage(value, card_nr):
    print("Choose target enemy")
    nr_enemy_to_target = input()
    nr_enemy_to_target = Background_Calculations.handle_input(nr_enemy_to_target)
    nr_enemy_to_target = int(nr_enemy_to_target)
    nr_enemy_to_target = nr_enemy_to_target - 1
    Static_Data.get_enemies_to_defeat()[nr_enemy_to_target].take_damage(value)
    print("The goblin has " + str(Static_Data.get_enemies_to_defeat()[nr_enemy_to_target].health) + " health left")
    Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr))


def do_defend(value, card_nr):
    print("Choose target dwarf")
    nr_enemy_to_target = input()
    nr_enemy_to_target = Background_Calculations.handle_input(nr_enemy_to_target)
    nr_enemy_to_target = int(nr_enemy_to_target)
    nr_enemy_to_target = nr_enemy_to_target - 1
    Static_Data.get_list_of_people()[nr_enemy_to_target].defend += value
    print("The dwarf has " + str(Static_Data.get_list_of_people()[nr_enemy_to_target].defend) + " armor now")
    Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop(card_nr))


def player_use_card_round():

    for x in range(len(Static_Data.get_list_of_people())):
        Static_Data.get_list_of_people()[x].defend = 0
    print("You have " + str(len(Static_Data.get_list_of_people())) + " combat-trained dwarves, and can use " + str(
        len(Static_Data.get_list_of_people())) + " cards this round")
    for x in range(len(Static_Data.get_list_of_people())):
        print("Dwarf " + str(x + 1) + " is ID " + str(Static_Data.get_list_of_people()[x].ID) + " with health " + str(Static_Data.get_list_of_people()[x].health))
    Deck_management.draw_cards_until_full()
    for x in range(len(Static_Data.get_list_of_people())):

        Deck_management.print_deck()
        print("Write number of card to use")
        use_card_nr = input()
        use_card_nr = Background_Calculations.handle_input(use_card_nr)
        use_card_nr = int(use_card_nr)
        use_card_nr -= 1
        value, type_of_card = Static_Data.get_deck_list().hand[use_card_nr].usage()
        if type_of_card == Enumerators.TypeOfCard.Attack:
            do_damage(value, use_card_nr)
        if type_of_card == Enumerators.TypeOfCard.Defend:
            do_defend(value, use_card_nr)
    Deck_management.discard_hand()

def enemy_use_indication_round():
    for x in range(len(Static_Data.get_enemies_to_defeat())):
        Static_Data.get_enemies_to_defeat()[x].usage()


def end_turn_step():
    pass


def start_combat():
    while len(Static_Data.get_enemies_to_defeat()) > 0:
        print("You have " + str(len(Static_Data.get_enemies_to_defeat())) + " enemies left")
        enemy_indication_round()
        player_use_card_round()
        enemy_use_indication_round()
        end_turn_step()
