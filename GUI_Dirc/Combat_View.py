import arcade
from arcade.gui import UIManager

import Enumerators
import GUI_Calculations
from Commands_Dirc import Combat, Deck_management
from GUI_Calculations import make_SpriteList_from_numbers
from GUI_Dirc import GUI
from Inventory import Inventory
from Static_Data import Static_Data

from Static_Data_Bools import Static_Data_Bools


class Combat_View(arcade.View):

    def __init__(self):
        super().__init__()
        self.list_of_reward_card_indicator_text = []
        self.list_of_reward_card_text = []
        self.list_of_card_sprite_lists = []
        self.list_of_card_text = []
        self.list_of_card_indicator_text = []

        self.list_of_reward_cards = []
        self.random_item = None
        self.combat_class = Combat.Combat()
        self.active_dwarf = None
        self.setup_done = False

        self.active_dwarf_pointer = arcade.SpriteList()
        self.end_turn = arcade.SpriteList()

        self.sprites_list_dwarves_energy = arcade.SpriteList()
        self.list_of_dwarf_energy = []
        self.sprites_list_dwarves_defend = arcade.SpriteList()
        self.list_of_dwarf_defend = []
        self.sprites_list_dwarves_health = arcade.SpriteList()
        self.list_of_dwarf_health = []
        self.sprites_list_dwarves = arcade.SpriteList()

        self.sprites_list_discard_pile = arcade.SpriteList()
        self.sprites_list_discard_pile_indicator = arcade.SpriteList()
        self.sprites_deck = arcade.SpriteList()
        self.sprites_deck_indicator = arcade.SpriteList()

        self.sprites_list_enemies_defend = arcade.SpriteList()
        self.list_of_enemy_defend = []
        self.sprites_list_enemies_health = arcade.SpriteList()
        self.list_of_enemy_health = []
        self.sprites_list_enemies_indicator = arcade.SpriteList()
        self.list_of_enemy_indicator = []
        self.sprites_list_enemies = arcade.SpriteList()

        self.held_card = None
        self.held_info_text = None
        self.held_box_of_text = None
        self.held_card_nr = None

        self.reward_item = arcade.SpriteList()

        self.width, self.height = arcade.window_commands.get_display_size()
        self.scaling_x = 1920 / self.width
        self.scaling_y = 1080 / self.height
        self.manager = UIManager()
        self.manager.enable()

        self.text_manager = UIManager()
        self.text_manager.enable()

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
        for dwarf in Static_Data.get_list_of_people():
            if dwarf.has_energy:
                self.active_dwarf = dwarf
                break

    def update_dwarves(self):

        self.sprites_list_dwarves_defend.clear()
        self.sprites_list_dwarves_health.clear()
        self.list_of_dwarf_health = []
        self.sprites_list_dwarves.clear()
        self.sprites_list_dwarves_energy.clear()
        self.active_dwarf_pointer.clear()

        self.active_dwarf_pointer.append(arcade.Sprite(Enumerators.Sprites.Active_Dwarf_Pointer.value, 0.10))

        for dwarf in Static_Data.get_list_of_people():
            self.sprites_list_dwarves.append(arcade.Sprite(dwarf.sprite, 0.10))

            self.sprites_list_dwarves_health.append(
                arcade.Sprite(Enumerators.Sprites_Of_Planned_Attack.Healing.value))
            self.sprites_list_dwarves_defend.append(
                arcade.Sprite(Enumerators.Sprites_Of_Planned_Attack.Defend.value))

            if dwarf.amount_energy == 0:
                self.sprites_list_dwarves_energy.append(arcade.Sprite(Enumerators.Sprites.Free_Energy.value))
            elif dwarf.amount_energy == 1:
                self.sprites_list_dwarves_energy.append(arcade.Sprite(Enumerators.Sprites.One_Energy.value))
            elif dwarf.amount_energy == 2:
                self.sprites_list_dwarves_energy.append(arcade.Sprite(Enumerators.Sprites.Two_Energy.value))

        length_divider = self.width / 4
        for x in range(len(self.sprites_list_dwarves)):
            self.sprites_list_dwarves[x].center_x = length_divider * (x + 1) / self.scaling_x
            self.sprites_list_dwarves[x].center_y = 350 / self.scaling_y

            self.sprites_list_dwarves_health[x].center_x = self.sprites_list_dwarves[x].center_x
            self.sprites_list_dwarves_health[x].center_y = self.sprites_list_dwarves[x].center_y + 50

            self.sprites_list_dwarves_defend[x].center_x = self.sprites_list_dwarves[x].center_x
            self.sprites_list_dwarves_defend[x].center_y = self.sprites_list_dwarves[x].center_y + 100

            self.sprites_list_dwarves_energy[x].center_x = self.sprites_list_dwarves[x].center_x - 50
            self.sprites_list_dwarves_energy[x].center_y = self.sprites_list_dwarves[x].center_y

            self.list_of_dwarf_health.append(make_SpriteList_from_numbers(Static_Data.get_list_of_people()[x].health,
                                                                          self.sprites_list_dwarves[x].center_x + 25,
                                                                          self.sprites_list_dwarves[x].center_y + 50))
            self.list_of_dwarf_defend.append(make_SpriteList_from_numbers(Static_Data.get_list_of_people()[x].defend,
                                                                          self.sprites_list_dwarves[x].center_x + 25,
                                                                          self.sprites_list_dwarves[x].center_y + 100))
            self.list_of_dwarf_energy.append(
                make_SpriteList_from_numbers(Static_Data.get_list_of_people()[x].amount_energy,
                                             self.sprites_list_dwarves[x].center_x - 85,
                                             self.sprites_list_dwarves[x].center_y))

        self.active_dwarf_pointer[0].center_x = self.sprites_list_dwarves[
            Static_Data.get_list_of_people().index(self.active_dwarf)].center_x
        self.active_dwarf_pointer[0].center_y = self.sprites_list_dwarves[Static_Data.get_list_of_people().index(
            self.active_dwarf)].center_y + 30
        self.end_turn[0].center_x = self.sprites_list_dwarves[0].center_x - 150
        self.end_turn[0].center_y = self.sprites_list_dwarves[0].center_y

    def update_cards(self):

        self.list_of_card_sprite_lists.clear()
        self.list_of_card_text.clear()
        self.list_of_card_indicator_text.clear()
        self.text_manager = UIManager()
        self.text_manager.enable()

        self.sprites_list_discard_pile.clear()
        self.sprites_list_discard_pile_indicator.clear()
        self.sprites_deck.clear()
        self.sprites_deck_indicator.clear()

        for card in Static_Data.get_deck_list().hand:
            self.list_of_card_sprite_lists.append(GUI_Calculations.make_card_sprite_list_from_backend(card))
        for x, sprite_lists in enumerate(self.list_of_card_sprite_lists):
            sprite_lists[0].center_x = ((self.width / 3) + 250 * x) / self.scaling_x
            sprite_lists[0].center_y = 150 / self.scaling_y
            sprite_lists[1].center_x = sprite_lists[0].center_x - 70
            sprite_lists[1].center_y = sprite_lists[0].center_y + 120.5
            sprite_lists[2].center_x = sprite_lists[0].center_x - 23
            sprite_lists[2].center_y = sprite_lists[0].center_y - 12.5
            sprite_lists[3].center_x = sprite_lists[0].center_x + 66
            sprite_lists[3].center_y = sprite_lists[0].center_y - 12.5
            self.list_of_card_text.append(arcade.gui.UILabel(x=sprite_lists[0].center_x - 80,
                                                             y=sprite_lists[0].center_y - 30,
                                                             text=str(Static_Data.get_deck_list().hand[
                                                                          x].value),
                                                             width=50, height=50, font_size=24,
                                                             font_name="Arial",
                                                             text_color=arcade.color.BLACK))

            self.list_of_card_indicator_text.append(arcade.gui.UILabel(x=sprite_lists[0].center_x - 80,
                                                                       y=sprite_lists[0].center_y - 80,
                                                                       text=GUI_Calculations.create_card_text_from_backend(
                                                                           Static_Data.get_deck_list().hand[x]),
                                                                       width=50, height=50, font_size=10,
                                                                       font_name="Arial",
                                                                       text_color=arcade.color.BLACK))
        for text in self.list_of_card_text:
            text.fit_content()
            self.text_manager.add(text)
        for text2 in self.list_of_card_indicator_text:
            text2.fit_content()
            self.text_manager.add(text2)
        self.sprites_deck.append(arcade.Sprite(Enumerators.Sprites.Card.value))
        self.sprites_deck[0].center_x = 100 / self.scaling_x
        self.sprites_deck[0].center_y = 150 / self.scaling_y

        self.sprites_deck_indicator = make_SpriteList_from_numbers(len(Static_Data.get_deck_list().content),
                                                                   self.sprites_deck[0].center_x,
                                                                   self.sprites_deck[0].center_y + 50)

        self.sprites_list_discard_pile.append(arcade.Sprite(Enumerators.Sprites.Card.value))
        self.sprites_list_discard_pile[0].center_x = 1820 / self.scaling_x
        self.sprites_list_discard_pile[0].center_y = 150 / self.scaling_y

        self.sprites_list_discard_pile_indicator = make_SpriteList_from_numbers(
            len(Static_Data.get_deck_list().discard_pile), self.sprites_list_discard_pile[0].center_x,
            self.sprites_list_discard_pile[0].center_y + 50)

    def update_rewards_card(self):
        for card in Static_Data.get_deck_list().list_of_rewards_card:
            self.list_of_reward_cards.append(GUI_Calculations.make_card_sprite_list_from_backend(card))
        length_divider = self.width / 4
        for x, sprite_lists in enumerate(self.list_of_reward_cards):
            sprite_lists[0].center_x = length_divider * (x + 1) / self.scaling_x
            sprite_lists[0].center_y = 650 / self.scaling_y
            sprite_lists[1].center_x = sprite_lists[0].center_x - 70
            sprite_lists[1].center_y = sprite_lists[0].center_y + 120.5
            sprite_lists[2].center_x = sprite_lists[0].center_x - 23
            sprite_lists[2].center_y = sprite_lists[0].center_y - 12.5
            sprite_lists[3].center_x = sprite_lists[0].center_x + 66
            sprite_lists[3].center_y = sprite_lists[0].center_y - 12.5
            self.list_of_reward_card_text.append(arcade.gui.UILabel(x=sprite_lists[0].center_x - 80,
                                                                    y=sprite_lists[0].center_y - 30,
                                                                    text=str(
                                                                        Static_Data.get_deck_list().list_of_rewards_card[
                                                                            x].value),
                                                                    width=50, height=50, font_size=24,
                                                                    font_name="Arial",
                                                                    text_color=arcade.color.BLACK))

            self.list_of_reward_card_indicator_text.append(arcade.gui.UILabel(x=sprite_lists[0].center_x - 80,
                                                                              y=sprite_lists[0].center_y - 80,
                                                                              text=GUI_Calculations.create_card_text_from_backend(
                                                                                  Static_Data.get_deck_list().list_of_rewards_card[
                                                                                      x]),
                                                                              width=50, height=50, font_size=10,
                                                                              font_name="Arial",
                                                                              text_color=arcade.color.BLACK))
        for text in self.list_of_reward_card_text:
            text.fit_content()
            self.text_manager.add(text)
        for text2 in self.list_of_reward_card_indicator_text:
            text2.fit_content()
            self.text_manager.add(text2)

    def update_enemies(self):
        self.sprites_list_enemies.clear()
        self.sprites_list_enemies_indicator.clear()
        self.list_of_enemy_indicator = []
        self.sprites_list_enemies_defend.clear()
        self.list_of_enemy_defend = []
        self.sprites_list_enemies_health.clear()
        self.list_of_enemy_health = []

        for enemy in Static_Data.get_enemies_to_defeat():
            self.sprites_list_enemies.append(arcade.Sprite(enemy.sprite, 0.10))
            self.sprites_list_enemies_indicator.append(arcade.Sprite(enemy.type_of_planned_attack_sprite))
            self.sprites_list_enemies_health.append(
                arcade.Sprite(Enumerators.Sprites_Of_Planned_Attack.Healing.value))
            self.sprites_list_enemies_defend.append(
                arcade.Sprite(Enumerators.Sprites_Of_Planned_Attack.Defend.value))
        length_divider = self.width / 7
        for x in range(len(self.sprites_list_enemies)):
            self.sprites_list_enemies[x].center_x = length_divider * (x + 1) / self.scaling_x
            self.sprites_list_enemies[x].center_y = 900 / self.scaling_y

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
        self.sprites_deck.draw()
        self.sprites_deck_indicator.draw()
        self.sprites_list_discard_pile.draw()
        self.sprites_list_discard_pile_indicator.draw()
        self.sprites_list_dwarves.draw()

        self.sprites_list_enemies_indicator.draw()
        for number in self.list_of_enemy_indicator:
            number.draw()
        self.sprites_list_enemies_defend.draw()
        for number in self.list_of_enemy_defend:
            number.draw()
        self.sprites_list_enemies_health.draw()
        for number in self.list_of_enemy_health:
            number.draw()
        self.sprites_list_dwarves_health.draw()

        for number in self.list_of_dwarf_health:
            number.draw()
        self.sprites_list_dwarves_defend.draw()
        for number in self.list_of_dwarf_defend:
            number.draw()
        self.sprites_list_dwarves_energy.draw()

        for number in self.list_of_dwarf_energy:
            number.draw()

        for sprite_list in self.list_of_card_sprite_lists:
            sprite_list.draw()
        self.active_dwarf_pointer.draw()
        self.end_turn.draw()
        self.draw_text()
        self.reward_item.draw()
        if Static_Data_Bools.get_reward():
            for sprite_list in self.list_of_reward_cards:
                sprite_list.draw()

        self.text_manager.draw()
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
            sprite_list_nr = 0
            for sprite_list in self.list_of_card_sprite_lists:

                card_clicked = arcade.get_sprites_at_point((x, y), sprite_list)
                if card_clicked:
                    self.held_card = self.list_of_card_sprite_lists[sprite_list_nr]
                    self.held_info_text = self.list_of_card_text[sprite_list_nr]
                    self.held_box_of_text = self.list_of_card_indicator_text[sprite_list_nr]
                    self.held_card_nr = sprite_list_nr
                else:
                    sprite_list_nr += 1
            end_turn = arcade.get_sprites_at_point((x, y), self.end_turn)
            if end_turn:
                self.combat_class.end_player_turn()
            active_dwarf = arcade.get_sprites_at_point((x, y), self.sprites_list_dwarves)
            if active_dwarf:
                nr_dwarf = self.sprites_list_dwarves.index(active_dwarf[0])
                self.active_dwarf = Static_Data.get_list_of_people()[nr_dwarf]
                self.update_dwarves()
                # set Active dwarf her
            sprite_list_nr = 0
            for sprite_list in self.list_of_reward_cards:

                card_clicked = arcade.get_sprites_at_point((x, y), sprite_list)
                if card_clicked:
                    Static_Data.get_deck_list().content.append(
                        Static_Data.get_deck_list().list_of_rewards_card[sprite_list_nr])
                    Static_Data.get_deck_list().list_of_rewards_card.clear()
                    Static_Data_Bools.set_took_reward(True)
                else:
                    sprite_list_nr += 1

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            sprite_list_nr = 0
            for sprite_list in self.list_of_card_sprite_lists:

                card_clicked = arcade.get_sprites_at_point((x, y), sprite_list)
                if card_clicked:
                    card_object = Static_Data.get_deck_list().content[sprite_list_nr]
                    self.manager.add(GUI_Calculations.make_panel_from_card(x, y, card_object))
                else:
                    sprite_list_nr += 1
            sprite_list_nr = 0
            for sprite_list in self.list_of_reward_cards:

                card_clicked = arcade.get_sprites_at_point((x, y), sprite_list)
                if card_clicked:
                    card_object = Static_Data.get_deck_list().list_of_rewards_card[sprite_list_nr]
                    self.manager.add(GUI_Calculations.make_panel_from_card(x, y, card_object))
                else:
                    sprite_list_nr += 1
            item_reward_clicked = arcade.get_sprites_at_point((x, y), self.reward_item)
            if item_reward_clicked:
                item_object = Inventory.equipment[len(Inventory.equipment) - 1]
                self.manager.add(GUI_Calculations.make_panel_from_item(x, y, item_object))

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.held_card:
            self.held_card[0].center_x += dx
            self.held_card[0].center_y += dy
            self.held_card[1].center_x += dx
            self.held_card[1].center_y += dy
            self.held_card[2].center_x += dx
            self.held_card[2].center_y += dy
            self.held_card[3].center_x += dx
            self.held_card[3].center_y += dy
            self.held_info_text.move(dx, dy)
            self.held_box_of_text.move(dx, dy)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):

        if not self.held_card:
            return

        enemies, distance_enemies = arcade.get_closest_sprite(self.held_card[0], self.sprites_list_enemies)
        dwarfs, distance_dwarfs = arcade.get_closest_sprite(self.held_card[0], self.sprites_list_dwarves)

        if arcade.check_for_collision(self.held_card[0], enemies):
            result = self.combat_class.player_use_card_round(self.held_card_nr,
                                                             self.sprites_list_enemies.index(enemies),
                                                             self.active_dwarf)
            if result:
                self.change_active_dwarf()
                self.update_enemies()
                self.update_dwarves()
        if arcade.check_for_collision(self.held_card[0], dwarfs):
            result = self.combat_class.player_use_card_round(self.held_card_nr,
                                                             self.sprites_list_dwarves.index(dwarfs),
                                                             self.active_dwarf)
            if result:
                self.change_active_dwarf()
                self.update_enemies()
                self.update_dwarves()

        self.held_card = []
        self.held_box_of_text = []
        self.held_info_text = []
        self.update_cards()

    def draw_rewards_item(self, random_item):
        self.random_item = random_item
        length_divider = self.width / 4
        self.reward_item.append(arcade.Sprite(random_item.value, 0.20))
        self.reward_item[0].center_y = 900 / self.scaling_y
        self.reward_item[0].center_x = (length_divider * 2) / self.scaling_x
