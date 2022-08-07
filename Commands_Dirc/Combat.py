import Background_Calculations
import Enumerators
from Commands_Dirc import Deck_management
from Static_Data import Static_Data
from Static_Data_Bools import Static_Data_Bools


class Combat:

    def enemy_indication_round(self):  # Del 1 av kamp, fienden indikerer og planlegger hva de har tenkt å gjøre
        for x in range(len(Static_Data.get_enemies_to_defeat())):
            Static_Data.get_enemies_to_defeat()[
                x].plan_attack()  # Sjekk implementation for detaljer, men fienden planlegger
            Static_Data.get_enemies_to_defeat()[
                x].plan_target()  # sjekk implementation for detlajer, men fienden velger target
            if Static_Data.get_enemies_to_defeat()[
                x].type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Attack:  # Vis angrip, skriv denne teksten
                print("Goblin " + str(x + 1) + " with health " +
                      str(Static_Data.get_enemies_to_defeat()[x].health) + " and defend " +
                      str(Static_Data.get_enemies_to_defeat()[x].defend) + " has planned an " +
                      str(Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack.value) + " with value " +
                      str(Static_Data.get_enemies_to_defeat()[x].value) + " on target " +
                      str(Static_Data.get_enemies_to_defeat()[x].target.ID))

            if Static_Data.get_enemies_to_defeat()[
                x].type_of_planned_attack == Enumerators.TypeOfPlannedAttack.Defend:  # Vis defend, skriv denne
                print("Goblin " + str(x + 1) + " with health " +
                      str(Static_Data.get_enemies_to_defeat()[x].health) + " and defend " +
                      str(Static_Data.get_enemies_to_defeat()[x].defend) + " has planned an " +
                      str(Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack.value) + " with value " +
                      str(Static_Data.get_enemies_to_defeat()[x].value))
        Static_Data.set_turn_phase(1)

    def check_for_deaths(self):
        for x in range(len(Static_Data.get_list_of_people())):  # Sjekker om vi har noen døde dverger
            if Static_Data.get_list_of_people()[x].health <= 0:
                Static_Data.get_list_of_people().remove(
                    Static_Data.get_list_of_people()[x])  # Fjerner døde dverger..RIP
                break

        for x in range(len(Static_Data.get_enemies_to_defeat())):  # Samme, bare for fienden
            if Static_Data.get_enemies_to_defeat()[x].health <= 0:
                Static_Data.get_enemies_to_defeat()[x].on_death()  # Evnt effekter av døden
                Static_Data.get_enemies_to_defeat().remove(Static_Data.get_enemies_to_defeat()[x])  # Fjern fra lista
                break  # Kun en ting kan dø om gangen, så stop, og heller kom tilbake vis flere ting dør.

    def player_use_card_round(self, card_nr, target):  # Del 2 av kamp, spilleren gjør actions
        result = Static_Data.get_deck_list().hand[card_nr].usage(card_nr,target)
        self.check_for_deaths()
        if Static_Data.get_energy() == 0:
            Static_Data.set_turn_phase(2)
        return result

    def end_player_turn(self):
        Static_Data.set_turn_phase(2)
        Deck_management.discard_hand()

    def enemy_use_indication_round(self):  # Del 3 av kamp, motstanderen gjør ting
        for x in range(len(Static_Data.get_enemies_to_defeat())):  # hver motstander gjør ting
            Static_Data.get_enemies_to_defeat()[x].usage()  # Hver fiende gjør sin ting, sjekk hver fiende
            if len(Static_Data.get_enemies_to_defeat()) > 0:  # Vis det fortsatt er fiender igjen
                self.check_for_deaths()  # sjekk om de har daua, hahaha
        Static_Data.set_turn_phase(3)
    def end_turn_step(self):  # Her kan vi legge til effekter som skjer på slutten av en runde, f.eks forgiftning osv
        self.check_for_deaths()
        Static_Data.set_turn_phase(0)

    def start_step(self):
        Static_Data.full_energy()
        Deck_management.draw_cards_until_full()  # Trekk kort opp til max verdien for hånda (3 enn så leng)
        for x in range(len(Static_Data.get_list_of_people())):  # Fjern all defend, det er jo kun for 1 runde
            Static_Data.get_list_of_people()[x].defend = 0

    def start_combat(self, view):  # Kamp-loopen.
        if len(Static_Data.get_enemies_to_defeat()) > 0:  # Så lenge vi har fiender igjen å sloss mot
            pass
            if Static_Data.get_turn_phase() == 0:
                self.start_step()
                self.enemy_indication_round()  ##Første del, Sjekk hver enkel implementation for detaljer.

                view.update_cards()
                view.update_enemies()
                view.update_dwarves()
            if Static_Data.get_turn_phase() == 2:
                self.enemy_use_indication_round()
                view.update_cards()
                view.update_enemies()
                view.update_dwarves()
            if Static_Data.get_turn_phase() == 3:
                self.end_turn_step()
                view.update_cards()
                view.update_enemies()
                view.update_dwarves()
        else:
            Static_Data_Bools.set_combat(False)
