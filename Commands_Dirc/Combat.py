import random

import Background_Calculations
from Commands_Dirc import Deck_management
from Static_Data import Static_Data
from Static_Data_Bools import Static_Data_Bools



class Combat:
    def enemy_indication_round(self):  # Del 1 av kamp, fienden indikerer og planlegger hva de har tenkt å gjøre
        for x in range(len(Static_Data.get_enemies_to_defeat())):
            Static_Data.get_enemies_to_defeat()[
                x].plan_attack()  # Sjekk implementation for detaljer, men fienden planlegger
        Static_Data.set_turn_phase(-1)

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

    def player_use_card_round(self, card_nr, target, nr_dwarf):  # Del 2 av kamp, spilleren gjør actions
        if nr_dwarf.has_energy:
            result = Static_Data.get_deck_list().hand[card_nr].usage(card_nr, target, nr_dwarf)
            self.check_for_deaths()
            return result
        else:
            return False

    def end_player_turn(self):
        Deck_management.discard_hand()
        Static_Data.set_turn_phase(2)

    def enemy_use_indication_round(self):  # Del 3 av kamp, motstanderen gjør ting
        for x in range(len(Static_Data.get_enemies_to_defeat())):  # hver motstander gjør ting
            Static_Data.get_enemies_to_defeat()[x].usage()  # Hver fiende gjør sin ting, sjekk hver fiende
            if len(Static_Data.get_enemies_to_defeat()) > 0:  # Vis det fortsatt er fiender igjen
                self.check_for_deaths()  # sjekk om de har daua, hahaha
        Static_Data.set_turn_phase(3)

    def end_turn_step(self,
                      view):  # Her kan vi legge til effekter som skjer på slutten av en runde, f.eks forgiftning osv
        self.check_for_deaths()
        Static_Data.set_turn_phase(0)
        view.change_active_dwarf()
        for x in range(len(Static_Data.get_list_of_people())):
            Static_Data.get_list_of_people()[x].weapon.usage(Static_Data.get_list_of_people()[x])
            Static_Data.get_list_of_people()[x].armor.usage(Static_Data.get_list_of_people()[x])
            Static_Data.get_list_of_people()[x].ring.usage(Static_Data.get_list_of_people()[x])
            Static_Data.get_list_of_people()[x].cloak.usage(Static_Data.get_list_of_people()[x])

    def start_step(self, view):
        for x in range(len(Static_Data.get_list_of_people())):
            Static_Data.get_list_of_people()[x].has_energy = True
        Static_Data.full_energy()
        view.change_active_dwarf()
        Deck_management.draw_cards_until_full(view)
        for x in range(len(Static_Data.get_list_of_people())):
            Static_Data.get_list_of_people()[x].amount_energy = Static_Data.get_list_of_people()[x].max_energy

        for x in range(len(Static_Data.get_list_of_people())):  # Fjern all defend, det er jo kun for 1 runde
            Static_Data.get_list_of_people()[x].defend = 0
        Static_Data.set_turn_phase(1)

    def start_combat(self, view):  # Kamp-loopen.
        if len(Static_Data.get_enemies_to_defeat()) > 0:  # Så lenge vi har fiender igjen å sloss mot

            if Static_Data.get_turn_phase() == 0:
                self.start_step(view)
                view.update_enemies()
                view.update_dwarves()
            if Static_Data.get_turn_phase() == 1:
                self.enemy_indication_round()  ##Første del, Sjekk hver enkel implementation for detaljer.

                view.update_enemies()
                view.update_dwarves()
            if Static_Data.get_turn_phase() == 2:
                self.enemy_use_indication_round()
            if Static_Data.get_turn_phase() == 3:
                self.end_turn_step(view)
                view.update_cards()
                view.update_enemies()
                view.update_dwarves()
        elif Static_Data_Bools.get_took_reward() is False and Static_Data_Bools.get_reward() is False:
            print("gi premie")
            list_of_cards = Background_Calculations.generate_rewards()
            if Static_Data.get_current_map().landscape.elite_difficulty:
                chance_for_item = random.randint(1,1)
            else:
                chance_for_item = random.randint(1,3)
            random_item = None
            if chance_for_item == 1:
                random_item = Background_Calculations.generate_item_rewards()
                Background_Calculations.generate_reward_for_inventory(random_item)

            Background_Calculations.generate_cards(list_of_cards)
            if random_item is not None:
                view.draw_rewards_item(random_item)
            view.update_rewards_card()
            Static_Data_Bools.set_reward(True)
            Static_Data.set_turn_phase(0)
        else:
            pass
