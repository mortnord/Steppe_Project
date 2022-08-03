import Background_Calculations
import Enumerators
from Commands_Dirc import Deck_management
from Static_Data import Static_Data


def enemy_indication_round(): #Del 1 av kamp, fienden indikerer og planlegger hva de har tenkt å gjøre
    for x in range(len(Static_Data.get_enemies_to_defeat())):
        Static_Data.get_enemies_to_defeat()[x].plan_attack() #Sjekk implementation for detaljer, men fienden planlegger
        Static_Data.get_enemies_to_defeat()[x].plan_target() #sjekk implementation for detlajer, men fienden velger target
        if Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Attack: #Vis angrip, skriv denne teksten
            print("Goblin " + str(x + 1) + " with health " +
                  str(Static_Data.get_enemies_to_defeat()[x].health) + " and defend " +
                  str(Static_Data.get_enemies_to_defeat()[x].defend) + " has planned an " +
                  str(Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack.value) + " with value " +
                  str(Static_Data.get_enemies_to_defeat()[x].value_attack) + " on target " +
                  str(Static_Data.get_enemies_to_defeat()[x].target.ID))

        if Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Defend: #Vis defend, skriv denne
            print("Goblin " + str(x + 1) + " with health " +
                  str(Static_Data.get_enemies_to_defeat()[x].health) + " and defend " +
                  str(Static_Data.get_enemies_to_defeat()[x].defend) + " has planned an " +
                  str(Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack.value) + " with value " +
                  str(Static_Data.get_enemies_to_defeat()[x].value_defend))


def check_for_deaths():
    for x in range(len(Static_Data.get_list_of_people())): #Sjekker om vi har noen døde dverger
        if Static_Data.get_list_of_people()[x].health <= 0:
            Static_Data.get_list_of_people().remove(Static_Data.get_list_of_people()[x]) #Fjerner døde dverger..RIP
            break

    for x in range(len(Static_Data.get_enemies_to_defeat())): #Samme, bare for fienden
        if Static_Data.get_enemies_to_defeat()[x].health <= 0:
            Static_Data.get_enemies_to_defeat()[x].on_death() #Evnt effekter av døden
            Static_Data.get_enemies_to_defeat().remove(Static_Data.get_enemies_to_defeat()[x]) #Fjern fra lista
            break #Kun en ting kan dø om gangen, så stop, og heller kom tilbake vis flere ting dør.


def player_use_card_round(): #Del 2 av kamp, spilleren gjør actions
    Static_Data.reset_which_dwarf_to_attack() #Først, full energi,
    for x in range(len(Static_Data.get_list_of_people())): #Fjern all defend, det er jo kun for 1 runde
        Static_Data.get_list_of_people()[x].defend = 0
    for x in range(len(Static_Data.get_list_of_people())): #Skriv hvor mye liv ting har igjen
        print("Dwarf " + str(x + 1) + " is ID " + str(Static_Data.get_list_of_people()[x].ID) + " with health " + str(
            Static_Data.get_list_of_people()[x].health))
    Deck_management.draw_cards_until_full() #Trekk kort opp til max verdien for hånda (3 enn så leng)
    while Static_Data.get_which_dwarf_to_attack() < len(Static_Data.get_list_of_people()): #Kort-bruk-loopen, så lenge energien vi har brukt ikke overstiger
                                                #mengden dverger vi har, så kan vi bruke mer kort. Her bør vi finne en bedre løsning, :P
        print("You have " + str((
                                            len(Static_Data.get_list_of_people()) - Static_Data.get_which_dwarf_to_attack())) + " dwarfs remaining to use")
        Deck_management.print_deck() ##Sjekk implementation for detaljer, men kort og godt, print ut hva vi har på hånda
        print("Write number of card to use")
        use_card_nr = input() #hva kort vi skal bruke, sjekk attack-kortet for detaljer rundt de 3 neste linjee
        use_card_nr = Background_Calculations.handle_input(use_card_nr)
        use_card_nr = int(use_card_nr)
        use_card_nr -= 1
        if (len(Static_Data.get_list_of_people()) - Static_Data.get_which_dwarf_to_attack()) >= \
                Static_Data.get_deck_list().hand[use_card_nr].dwarfs_required: #så lenge vi har nok energi til å bruke kortet, så går det fint.
            Static_Data.get_deck_list().hand[use_card_nr].usage(use_card_nr, Static_Data.get_which_dwarf_to_attack()) #Bruk kortet sitt effekt, avhengig av kortet som blir brukt
        check_for_deaths() #Klarte vi å drepe goblins? la oss sjekke

    Deck_management.discard_hand() #Discard alle kort på hånda, slik vi har 0.


def enemy_use_indication_round(): #Del 3 av kamp, motstanderen gjør ting
    for x in range(len(Static_Data.get_enemies_to_defeat())): #hver motstander gjør ting
        Static_Data.get_enemies_to_defeat()[x].usage() #Hver fiende gjør sin ting, sjekk hver fiende
        if len(Static_Data.get_enemies_to_defeat()) > 0: #Vis det fortsatt er fiender igjen
            check_for_deaths() #sjekk om de har daua, hahaha



def end_turn_step(): #Her kan vi legge til effekter som skjer på slutten av en runde, f.eks forgiftning osv
    pass


def start_combat(): #Kamp-loopen.
    while len(Static_Data.get_enemies_to_defeat()) > 0: #Så lenge vi har fiender igjen å sloss mot
        print("You have " + str(len(Static_Data.get_enemies_to_defeat())) + " enemies left")
        enemy_indication_round() ##Første del, Sjekk hver enkel implementation for detaljer.
        player_use_card_round() ##andre del
        enemy_use_indication_round() ##tredje del
        end_turn_step() #end-step.
