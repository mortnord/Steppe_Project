import random

import Background_Calculations
from Commands_Dirc import Deck_management
from Static_Data import Static_Data
from Static_Data_Bools import Static_Data_Bools


class Combat:

    def enemy_indication_round(self):  # Del 1 av kamp, fienden indikerer og planlegger hva de har tenkt å gjøre
        for enemy in Static_Data.get_enemies_to_defeat():
            enemy.plan_attack()
        Static_Data.set_turn_phase(-1)

    def check_for_deaths(self):

        for dwarf in Static_Data.get_list_of_people():
            if dwarf.health <= 0:
                Static_Data.get_list_of_people().remove(dwarf)
                break
        for enemy in Static_Data.get_enemies_to_defeat():
            if enemy.health <= 0:
                enemy.on_death()
                Static_Data.get_enemies_to_defeat().remove(enemy)
                break

    def player_use_card_round(self, card_nr, target, nr_dwarf):  # Del 2 av kamp, spilleren gjør actions
        if nr_dwarf.has_energy or Static_Data.get_deck_list().hand[card_nr].energy_required == 0:
            result = Static_Data.get_deck_list().hand[card_nr].usage(card_nr, target, nr_dwarf)
            self.check_for_deaths()
            return result
        else:
            return False

    def end_player_turn(self):
        Deck_management.discard_hand()
        Static_Data.set_turn_phase(2)

    def enemy_use_indication_round(self):  # Del 3 av kamp, motstanderen gjør ting
        for enemy in Static_Data.get_enemies_to_defeat():
            if enemy.stunned:
                enemy.stunned = False
            else:
                enemy.usage()
            if Static_Data.get_list_of_people():
                self.check_for_deaths()
        Static_Data.set_turn_phase(3)

    def end_turn_step(self,
                      view):  # Her kan vi legge til effekter som skjer på slutten av en runde, f.eks forgiftning osv
        Static_Data.set_turn_phase(0)
        view.change_active_dwarf()
        for dwarf in Static_Data.get_list_of_people():
            dwarf.weapon.usage(dwarf)
            dwarf.armor.usage(dwarf)
            dwarf.ring.usage(dwarf)
            dwarf.cloak.usage(dwarf)
        for enemy in Static_Data.get_enemies_to_defeat():
            if enemy.debuff_list:
                for debuff in list(enemy.debuff_list):
                    if debuff.active is not True:
                        enemy.debuff_list.remove(debuff)
                for debuff in enemy.debuff_list:
                    debuff.usage(enemy)
        self.check_for_deaths()

    def start_step(self, view):
        for dwarf in Static_Data.get_list_of_people():
            dwarf.has_energy = True
        view.change_active_dwarf()
        Deck_management.draw_cards_until_full(view)
        for dwarf in Static_Data.get_list_of_people():
            if dwarf.amount_energy < dwarf.max_energy:
                dwarf.amount_energy += 1
        for dwarf in Static_Data.get_list_of_people():
            dwarf.defend = 0
        Static_Data.set_turn_phase(1)

    def start_combat(self, view):  # Kamp-loopen.
        if Static_Data.get_enemies_to_defeat():
            if Static_Data.get_turn_phase() == 0:
                self.start_step(view)
                view.update_enemies()
                view.update_dwarves()
            if Static_Data.get_turn_phase() == 1:
                self.enemy_indication_round()  # Første del, Sjekk hver enkel implementation for detaljer.

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
                chance_for_item = random.randint(1, 1)
            else:
                chance_for_item = random.randint(1, 3)
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
