import arcade
from arcade.gui import UIManager

import Enumerators
import GUI_Calculations
from Commands_Dirc import Combat, Deck_management
from GUI_Calculations import make_SpriteList_from_numbers
from GUI_Dirc import GUI
from Static_Data import Static_Data

from Static_Data_Bools import Static_Data_Bools


class Combat_View(arcade.View):

    def __init__(self):
        super().__init__()
        self.combat_class = Combat.Combat()
        self.active_dwarf = None
        self.setup_done = False

        self.active_dwarf_pointer = arcade.SpriteList()
        self.mouse_hand = arcade.SpriteList()
        self.end_turn = arcade.SpriteList()

        self.sprites_list_dwarves_energy = arcade.SpriteList()
        self.list_of_dwarf_energy = []
        self.sprites_list_dwarves_defend = arcade.SpriteList()
        self.list_of_dwarf_defend = []
        self.sprites_list_dwarves_health = arcade.SpriteList()
        self.list_of_dwarf_health = []
        self.sprites_list_dwarves = arcade.SpriteList()

        self.sprites_list_cards = arcade.SpriteList()
        self.sprites_list_cards_indicator = arcade.SpriteList()
        self.list_of_cards_text = []

        self.sprites_list_enemies_defend = arcade.SpriteList()
        self.list_of_enemy_defend = []
        self.sprites_list_enemies_health = arcade.SpriteList()
        self.list_of_enemy_health = []
        self.sprites_list_enemies_indicator = arcade.SpriteList()
        self.list_of_enemy_indicator = []
        self.sprites_list_enemies = arcade.SpriteList()

        self.held_card_indicator_original_position = None
        self.held_card_indicator = []
        self.held_card_original_position = None
        self.held_card = []
        self.held_card_text_original_position = None
        self.held_card_text = []

        self.reward_cards = arcade.SpriteList()
        self.reward_cards_indicator = arcade.SpriteList()
        self.reward_item = arcade.SpriteList()
        self.list_of_reward_cards_text = []

        self.width, self.height = arcade.window_commands.get_display_size()
        self.scaling_x = 1920 / self.width
        self.scaling_y = 1080 / self.height
        self.manager = UIManager()
        self.manager.enable()

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def setup(self):

        self.end_turn.append(arcade.Sprite(Enumerators.Sprites.End_Turn.value, 0.10))

        self.active_dwarf = Static_Data.get_list_of_people()[0]
        self.update_enemies()
        self.update_cards()
        self.update_dwarves()

        self.setup_done = True
        # Kan bruke dette til å generate nummere for alle objekter, som er sprites og ikke en primitive

    def change_active_dwarf(self):
        for x in range(len(Static_Data.get_list_of_people())):
            if Static_Data.get_list_of_people()[x].has_energy:
                self.active_dwarf = Static_Data.get_list_of_people()[x]
                break

    def update_dwarves(self):

        self.sprites_list_dwarves_defend.clear()
        self.sprites_list_dwarves_health.clear()
        self.list_of_dwarf_health = []
        self.sprites_list_dwarves.clear()
        self.sprites_list_dwarves_energy.clear()
        self.active_dwarf_pointer.clear()

        self.active_dwarf_pointer.append(arcade.Sprite(Enumerators.Sprites.Active_Dwarf_Pointer.value, 0.10))
        self.change_active_dwarf()
        for x in range(len(Static_Data.get_list_of_people())):
            self.sprites_list_dwarves.append(arcade.Sprite(Static_Data.get_list_of_people()[x].sprite, 0.10))

            self.sprites_list_dwarves_health.append(
                arcade.Sprite(Enumerators.Sprites_Of_Planned_Attack.Healing.value, 0.10))
            self.sprites_list_dwarves_defend.append(
                arcade.Sprite(Enumerators.Sprites_Of_Planned_Attack.Defend.value, 0.10))
            self.sprites_list_dwarves_energy.append(arcade.Sprite(Enumerators.Sprites.Energy.value, 0.02))
        length_divider = self.width / 4
        for x in range(len(self.sprites_list_dwarves)):
            self.sprites_list_dwarves[x].center_x = length_divider * (x + 1) / self.scaling_x
            self.sprites_list_dwarves[x].center_y = 150 / self.scaling_y
            self.sprites_list_dwarves_health[x].center_x = self.sprites_list_dwarves[x].center_x
            self.sprites_list_dwarves_health[x].center_y = self.sprites_list_dwarves[x].center_y + 50
            self.sprites_list_dwarves_defend[x].center_x = self.sprites_list_dwarves[x].center_x
            self.sprites_list_dwarves_defend[x].center_y = self.sprites_list_dwarves[x].center_y + 100
            self.sprites_list_dwarves_energy[x].center_x = self.sprites_list_dwarves[x].center_x - 50
            self.sprites_list_dwarves_energy[x].center_y = self.sprites_list_dwarves[x].center_y
            self.list_of_dwarf_health.append(
                make_SpriteList_from_numbers(Static_Data.get_list_of_people()[x].health,
                                             self.sprites_list_dwarves[x].center_x + 25,
                                             self.sprites_list_dwarves[x].center_y + 50))
            self.list_of_dwarf_defend.append(
                make_SpriteList_from_numbers(Static_Data.get_list_of_people()[x].defend,
                                             self.sprites_list_dwarves[x].center_x + 25,
                                             self.sprites_list_dwarves[x].center_y + 100))
            self.list_of_dwarf_energy.append(
                make_SpriteList_from_numbers(Static_Data.get_list_of_people()[x].amount_energy,
                                             self.sprites_list_dwarves[x].center_x - 65,
                                             self.sprites_list_dwarves[x].center_y))

        self.active_dwarf_pointer[0].center_x = self.sprites_list_dwarves[
            Static_Data.get_list_of_people().index(self.active_dwarf)].center_x
        self.active_dwarf_pointer[0].center_y = self.sprites_list_dwarves[Static_Data.get_list_of_people().index(
            self.active_dwarf)].center_y + 30
        self.end_turn[0].center_x = self.sprites_list_dwarves[0].center_x - 100
        self.end_turn[0].center_y = self.sprites_list_dwarves[0].center_y

    def update_cards(self):
        self.sprites_list_cards.clear()
        self.sprites_list_cards_indicator.clear()
        self.list_of_cards_text = []
        for x in range(len(Static_Data.get_deck_list().hand)):
            self.sprites_list_cards.append(arcade.Sprite(Static_Data.get_deck_list().hand[x].sprite, 0.20))
            self.sprites_list_cards_indicator.append(
                arcade.Sprite(Static_Data.get_deck_list().hand[x].indicator_sprite, 0.10))

        for x in range(len(self.sprites_list_cards)):
            self.sprites_list_cards[x].center_x = ((self.width / 2) + 55 * x) / self.scaling_x
            self.sprites_list_cards[x].center_y = 50 / self.scaling_y
            self.sprites_list_cards_indicator[x].center_x = self.sprites_list_cards[x].center_x
            self.sprites_list_cards_indicator[x].center_y = self.sprites_list_cards[x].center_y + 20
            self.list_of_cards_text.append(make_SpriteList_from_numbers(Static_Data.get_deck_list().hand[x].value,
                                                                        self.sprites_list_cards[x].center_x,
                                                                        self.sprites_list_cards[x].center_y - 15))

    def update_rewards_card(self):
        self.reward_cards.clear()
        self.reward_cards_indicator.clear()
        self.list_of_reward_cards_text = []
        for x in range(len(Static_Data.get_deck_list().list_of_rewards_card)):
            self.reward_cards.append(arcade.Sprite(Static_Data.get_deck_list().list_of_rewards_card[x].sprite, 0.20))
            self.reward_cards_indicator.append(
                arcade.Sprite(Static_Data.get_deck_list().list_of_rewards_card[x].indicator_sprite, 0.10))
        length_divider = self.width / 4
        for x in range(len(self.reward_cards)):
            self.reward_cards[x].center_x = length_divider * (x + 1) / self.scaling_x
            self.reward_cards[x].center_y = 550 / self.scaling_y
            self.reward_cards_indicator[x].center_x = self.reward_cards[x].center_x
            self.reward_cards_indicator[x].center_y = self.reward_cards[x].center_y + 20
            self.list_of_reward_cards_text.append(
                make_SpriteList_from_numbers(Static_Data.get_deck_list().list_of_rewards_card[x].value,
                                             self.reward_cards[x].center_x,
                                             self.reward_cards[x].center_y - 15))

    def update_enemies(self):
        self.sprites_list_enemies.clear()
        self.sprites_list_enemies_indicator.clear()
        self.list_of_enemy_indicator = []
        self.sprites_list_enemies_defend.clear()
        self.list_of_enemy_defend = []
        self.sprites_list_enemies_health.clear()
        self.list_of_enemy_health = []
        for x in range(len(Static_Data.get_enemies_to_defeat())):
            self.sprites_list_enemies.append(arcade.Sprite(Static_Data.get_enemies_to_defeat()[x].sprite, 0.10))
            self.sprites_list_enemies_indicator.append(
                arcade.Sprite(Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack_sprite, 0.10))
            self.sprites_list_enemies_health.append(
                arcade.Sprite(Enumerators.Sprites_Of_Planned_Attack.Healing.value, 0.10))
            self.sprites_list_enemies_defend.append(
                arcade.Sprite(Enumerators.Sprites_Of_Planned_Attack.Defend.value, 0.10))
        length_divider = self.width / 7
        for x in range(len(self.sprites_list_enemies)):
            self.sprites_list_enemies[x].center_x = length_divider * (x + 1) / self.scaling_x
            self.sprites_list_enemies[x].center_y = 700 / self.scaling_y
            self.sprites_list_enemies_indicator[x].center_x = self.sprites_list_enemies[x].center_x
            self.sprites_list_enemies_indicator[x].center_y = self.sprites_list_enemies[x].center_y + 50
            self.sprites_list_enemies_health[x].center_x = self.sprites_list_enemies[x].center_x
            self.sprites_list_enemies_health[x].center_y = self.sprites_list_enemies[x].center_y - 50
            self.sprites_list_enemies_defend[x].center_x = self.sprites_list_enemies[x].center_x
            self.sprites_list_enemies_defend[x].center_y = self.sprites_list_enemies[x].center_y - 100
            self.list_of_enemy_health.append(
                make_SpriteList_from_numbers(Static_Data.get_enemies_to_defeat()[x].health,
                                             self.sprites_list_enemies[x].center_x + 25,
                                             self.sprites_list_enemies[x].center_y - 50))
            self.list_of_enemy_defend.append(
                make_SpriteList_from_numbers(Static_Data.get_enemies_to_defeat()[x].defend,
                                             self.sprites_list_enemies[x].center_x + 25,
                                             self.sprites_list_enemies[x].center_y - 100))
            self.list_of_enemy_indicator.append(
                make_SpriteList_from_numbers(Static_Data.get_enemies_to_defeat()[x].value,
                                             self.sprites_list_enemies[x].center_x + 25,
                                             self.sprites_list_enemies[x].center_y + 50))

    def on_draw(self):
        """ Draw this view """

        self.clear()

        self.sprites_list_enemies.draw()
        self.sprites_list_cards.draw()
        self.sprites_list_dwarves.draw()

        self.sprites_list_cards_indicator.draw()
        for x in range(len(self.list_of_cards_text)):
            self.list_of_cards_text[x].draw()

        self.sprites_list_enemies_indicator.draw()
        for x in range(len(self.list_of_enemy_indicator)):
            self.list_of_enemy_indicator[x].draw()
        self.sprites_list_enemies_defend.draw()
        for x in range(len(self.list_of_enemy_defend)):
            self.list_of_enemy_defend[x].draw()
        self.sprites_list_enemies_health.draw()
        for x in range(len(self.list_of_enemy_health)):
            self.list_of_enemy_health[x].draw()

        self.sprites_list_dwarves_health.draw()
        for x in range(len(self.list_of_dwarf_health)):
            self.list_of_dwarf_health[x].draw()

        self.sprites_list_dwarves_defend.draw()
        for x in range(len(self.list_of_dwarf_defend)):
            self.list_of_dwarf_defend[x].draw()
        self.sprites_list_dwarves_energy.draw()
        for x in range(len(self.list_of_dwarf_energy)):
            self.list_of_dwarf_energy[x].draw()

        self.active_dwarf_pointer.draw()
        self.end_turn.draw()
        self.draw_text()
        self.reward_item.draw()
        if Static_Data_Bools.get_reward():
            self.reward_cards.draw()
            self.reward_cards_indicator.draw()
            for x in range(len(self.list_of_reward_cards_text)):
                self.list_of_reward_cards_text[x].draw()
        self.manager.draw()
    def draw_text(self):

        for x in range(len(Static_Data.get_enemies_to_defeat())):
            if Static_Data.get_enemies_to_defeat()[x].target is not None:
                arcade.draw_line(self.sprites_list_enemies[x].center_x,
                                 self.sprites_list_enemies[x].center_y,
                                 self.sprites_list_dwarves[Static_Data.get_list_of_people().index(
                                     Static_Data.get_enemies_to_defeat()[x].target)].center_x,
                                 self.sprites_list_dwarves[Static_Data.get_list_of_people().index(
                                     Static_Data.get_enemies_to_defeat()[x].target)].center_y,
                                 arcade.color.BLACK,
                                 1)

    # Gjør så lite som mulig, annet enn å tegne
    def on_update(self, delta_time: float):
        self.combat_class.start_combat(self)
        if len(Static_Data.get_enemies_to_defeat()) < 1 and Static_Data_Bools.get_took_reward() is True:
            Static_Data_Bools.set_reward(False)
            Static_Data_Bools.set_took_reward(False)
            Static_Data_Bools.set_combat(False)
            Deck_management.reset_deck()
            map_view = GUI.Map_View()
            self.window.show_view(map_view)
            map_view.setup()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.manager.clear()
        if button == arcade.MOUSE_BUTTON_LEFT:
            card = arcade.get_sprites_at_point((x, y), self.sprites_list_cards)

            if len(card) > 0:
                primary_card = card[-1]
                self.held_card = [primary_card]
                self.held_cards_original_position = primary_card.position

                indicator, distance = arcade.get_closest_sprite(self.held_card[0], self.sprites_list_cards_indicator)

                self.held_card_indicator = [indicator]
                self.held_card_indicator_original_position = indicator.position
                self.closest_card_picking_up = 10000
                for x in range(len(self.list_of_cards_text)):
                    text, distance = arcade.get_closest_sprite(self.held_card[0], self.list_of_cards_text[x])
                    if distance < self.closest_card_picking_up:
                        self.held_card_text = [text]
                        self.closest_card_picking_up = distance

            energy = arcade.get_sprites_at_point((x, y), self.end_turn)
            if len(energy) > 0:
                self.combat_class.end_player_turn()
            active_dwarf = arcade.get_sprites_at_point((x, y), self.sprites_list_dwarves)
            if len(active_dwarf) > 0:
                nr_dwarf = self.sprites_list_dwarves.index(active_dwarf[0])
                print(nr_dwarf)
                self.active_dwarf = Static_Data.get_list_of_people()[nr_dwarf]
                self.update_dwarves()
                # set Active dwarf her
            reward_card = arcade.get_sprites_at_point((x, y), self.reward_cards)
            if len(reward_card):
                print("get card")
                Static_Data.get_deck_list().content.append(
                    Static_Data.get_deck_list().list_of_rewards_card[self.reward_cards.index(reward_card[0])])
                Static_Data.get_deck_list().list_of_rewards_card.clear()
                Static_Data_Bools.set_took_reward(True)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            card_clicked = arcade.get_sprites_at_point((x, y), self.sprites_list_cards)
            if len(card_clicked):
                self.manager.clear()
                card_object = Static_Data.get_deck_list().hand[self.sprites_list_cards.index(card_clicked[0])]
                self.manager.add(GUI_Calculations.make_panel_from_card(x, y, card_object))


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):

        for card in self.held_card:
            card.center_x += dx
            card.center_y += dy

        for x in range(len(self.held_card_indicator)):
            self.held_card_indicator[x].center_x += dx
            self.held_card_indicator[x].center_y += dy

        for x in range(len(self.held_card_text)):
            self.held_card_text[x].center_x += dx
            self.held_card_text[x].center_y += dy

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):

        if len(self.held_card) == 0:
            return

        enemies, distance_enemies = arcade.get_closest_sprite(self.held_card[0], self.sprites_list_enemies)
        dwarfs, distance_dwarfs = arcade.get_closest_sprite(self.held_card[0], self.sprites_list_dwarves)

        if arcade.check_for_collision(self.held_card[0], enemies):
            result = self.combat_class.player_use_card_round(self.sprites_list_cards.index(self.held_card[0]),
                                                             self.sprites_list_enemies.index(enemies),
                                                             self.active_dwarf)
            if result:
                self.change_active_dwarf()
                self.update_cards()
                self.update_enemies()
                self.update_dwarves()
        if arcade.check_for_collision(self.held_card[0], dwarfs):
            result = self.combat_class.player_use_card_round(self.sprites_list_cards.index(self.held_card[0]),
                                                             self.sprites_list_dwarves.index(dwarfs),
                                                             self.active_dwarf)
            if result:
                self.change_active_dwarf()
                self.update_cards()
                self.update_enemies()
                self.update_dwarves()

        # We are no longer holding cards
        self.held_card = []
        self.held_card_indicator = []
        self.held_card_text = []
        self.update_cards()

    def draw_rewards_item(self, random_item):
        length_divider = self.width / 4
        self.reward_item.append(arcade.Sprite(random_item.value, 0.20))
        self.reward_item[0].center_y = 700/self.scaling_y
        self.reward_item[0].center_x = (length_divider * 2)/self.scaling_x