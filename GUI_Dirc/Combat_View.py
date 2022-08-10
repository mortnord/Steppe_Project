import arcade

import Enumerators
import Setup
from Commands_Dirc import Combat, Deck_management
from GUI_Dirc import GUI
from Static_Data import Static_Data

from Static_Data_Bools import Static_Data_Bools


class Combat_View(arcade.View):
    combat_class = Combat.Combat()
    active_dwarf = None
    setup_done = False

    def __init__(self):
        super().__init__()
        self.active_dwarf_pointer = arcade.SpriteList()
        self.mouse_hand = arcade.SpriteList()
        self.end_turn = arcade.SpriteList()

        self.sprites_list_dwarves_energy = arcade.SpriteList()
        self.sprites_list_dwarves_defend = arcade.SpriteList()
        self.sprites_list_dwarves_health = arcade.SpriteList()
        self.sprites_list_dwarves = arcade.SpriteList()

        self.sprites_list_cards = arcade.SpriteList()
        self.sprites_list_cards_indicator = arcade.SpriteList()

        self.sprites_list_enemies_defend = arcade.SpriteList()
        self.sprites_list_enemies_health = arcade.SpriteList()
        self.sprites_list_enemies_indicator = arcade.SpriteList()
        self.sprites_list_enemies = arcade.SpriteList()

        self.held_card_indicator_original_position = None
        self.held_card_indicator = []
        self.held_card_original_position = None
        self.held_card = []

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def setup(self):

        self.generate_enemy_sprites()
        self.generate_card_sprites()
        self.generate_dwarf_sprites()

        self.active_dwarf = Static_Data.get_list_of_people()[0]
        self.end_turn.append(arcade.Sprite(Enumerators.Sprites.End_Turn.value, 0.10))
        self.setup_done = True
        #Kan bruke dette til å generate nummere for alle objekter, som er sprites og ikke en primitive
        self.test_list = self.make_SpriteList_from_numbers(60534, 100, 150)

    def change_active_dwarf(self):
        for x in range(len(Static_Data.get_list_of_people())):
            if Static_Data.get_list_of_people()[x].has_energy:
                self.active_dwarf = Static_Data.get_list_of_people()[x]
                break

    def generate_dwarf_sprites(self):
        for x in range(len(Static_Data.get_list_of_people())):
            self.sprites_list_dwarves.append(arcade.Sprite(Static_Data.get_list_of_people()[x].sprite, 0.10))

        for x in range(len(self.sprites_list_dwarves)):
            self.sprites_list_dwarves[x].center_x = 150 * x + 150
            self.sprites_list_dwarves[x].center_y = 150

    def generate_card_sprites(self):
        for x in range(len(Static_Data.get_deck_list().hand)):
            self.sprites_list_cards.append(arcade.Sprite(Static_Data.get_deck_list().hand[x].sprite, 0.20))
        for x in range(len(self.sprites_list_cards)):
            self.sprites_list_cards[x].center_x = 150 * x + 150
            self.sprites_list_cards[x].center_y = 100

    def generate_enemy_sprites(self):
        for x in range(len(Static_Data.get_enemies_to_defeat())):
            self.sprites_list_enemies.append(arcade.Sprite(Static_Data.get_enemies_to_defeat()[x].sprite, 0.10))
        for x in range(len(self.sprites_list_enemies)):
            self.sprites_list_enemies[x].center_x = 150 * x + 150
            self.sprites_list_enemies[x].center_y = 400

    def update_dwarves(self):

        self.sprites_list_dwarves_defend.clear()
        self.sprites_list_dwarves_health.clear()
        self.sprites_list_dwarves.clear()
        self.sprites_list_dwarves_energy.clear()
        self.active_dwarf_pointer.clear()

        self.active_dwarf_pointer.append(arcade.Sprite(Enumerators.Sprites.Active_Dwarf_Pointer.value, 0.10))
        for x in range(len(Static_Data.get_list_of_people())):
            self.sprites_list_dwarves.append(arcade.Sprite(Static_Data.get_list_of_people()[x].sprite, 0.10))

            self.sprites_list_dwarves_health.append(
                arcade.Sprite(Enumerators.Sprites_of_planned_attack.Healing.value, 0.10))
            self.sprites_list_dwarves_defend.append(
                arcade.Sprite(Enumerators.Sprites_of_planned_attack.Defend.value, 0.10))
            self.sprites_list_dwarves_energy.append(arcade.Sprite(Enumerators.Sprites.Energy.value, 0.02))
        for x in range(len(self.sprites_list_dwarves)):
            self.sprites_list_dwarves[x].center_x = 150 * x + 150
            self.sprites_list_dwarves[x].center_y = 150
            self.sprites_list_dwarves_health[x].center_x = self.sprites_list_dwarves[x].center_x
            self.sprites_list_dwarves_health[x].center_y = self.sprites_list_dwarves[x].center_y + 50
            self.sprites_list_dwarves_defend[x].center_x = self.sprites_list_dwarves[x].center_x
            self.sprites_list_dwarves_defend[x].center_y = self.sprites_list_dwarves[x].center_y + 100
            self.sprites_list_dwarves_energy[x].center_x = self.sprites_list_dwarves[x].center_x - 50
            self.sprites_list_dwarves_energy[x].center_y = self.sprites_list_dwarves[x].center_y
        self.active_dwarf_pointer[0].center_x = self.sprites_list_dwarves[
            Static_Data.get_list_of_people().index(self.active_dwarf)].center_x
        self.active_dwarf_pointer[0].center_y = self.sprites_list_dwarves[Static_Data.get_list_of_people().index(
            self.active_dwarf)].center_y + 30
        self.end_turn[0].center_x = self.sprites_list_dwarves[0].center_x - 100
        self.end_turn[0].center_y = self.sprites_list_dwarves[0].center_y

    def update_cards(self):
        self.sprites_list_cards.clear()
        self.sprites_list_cards_indicator.clear()
        for x in range(len(Static_Data.get_deck_list().hand)):
            print(Static_Data.get_deck_list().hand[x].sprite + " is problemet" + str(x))
            self.sprites_list_cards.append(arcade.Sprite(Static_Data.get_deck_list().hand[x].sprite, 0.20))
            self.sprites_list_cards_indicator.append(
                arcade.Sprite(Static_Data.get_deck_list().hand[x].indicator_sprite, 0.10))
        for x in range(len(self.sprites_list_cards)):
            self.sprites_list_cards[x].center_x = 150 * x + 150
            self.sprites_list_cards[x].center_y = 50
            self.sprites_list_cards_indicator[x].center_x = self.sprites_list_cards[x].center_x
            self.sprites_list_cards_indicator[x].center_y = self.sprites_list_cards[x].center_y

    def update_enemies(self):
        self.sprites_list_enemies.clear()
        self.sprites_list_enemies_indicator.clear()
        self.sprites_list_enemies_defend.clear()
        self.sprites_list_enemies_health.clear()
        for x in range(len(Static_Data.get_enemies_to_defeat())):
            self.sprites_list_enemies.append(arcade.Sprite(Static_Data.get_enemies_to_defeat()[x].sprite, 0.10))
            self.sprites_list_enemies_indicator.append(
                arcade.Sprite(Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack_sprite, 0.10))
            self.sprites_list_enemies_health.append(
                arcade.Sprite(Enumerators.Sprites_of_planned_attack.Healing.value, 0.10))
            self.sprites_list_enemies_defend.append(
                arcade.Sprite(Enumerators.Sprites_of_planned_attack.Defend.value, 0.10))
        for x in range(len(self.sprites_list_enemies)):
            self.sprites_list_enemies[x].center_x = 150 * x + 150
            self.sprites_list_enemies[x].center_y = 400
            self.sprites_list_enemies_indicator[x].center_x = self.sprites_list_enemies[x].center_x
            self.sprites_list_enemies_indicator[x].center_y = self.sprites_list_enemies[x].center_y + 50
            self.sprites_list_enemies_health[x].center_x = self.sprites_list_enemies[x].center_x
            self.sprites_list_enemies_health[x].center_y = self.sprites_list_enemies[x].center_y - 50
            self.sprites_list_enemies_defend[x].center_x = self.sprites_list_enemies[x].center_x
            self.sprites_list_enemies_defend[x].center_y = self.sprites_list_enemies[x].center_y - 100

    def on_draw(self):
        """ Draw this view """
        if self.setup_done:
            self.clear()

            self.sprites_list_enemies.draw()
            self.sprites_list_cards.draw()
            self.sprites_list_dwarves.draw()

            self.sprites_list_cards_indicator.draw()

            self.sprites_list_enemies_indicator.draw()
            self.sprites_list_enemies_defend.draw()
            self.sprites_list_enemies_health.draw()

            self.sprites_list_dwarves_health.draw()
            self.sprites_list_dwarves_defend.draw()
            self.sprites_list_dwarves_energy.draw()

            self.active_dwarf_pointer.draw()
            self.end_turn.draw()
            self.test_list.draw()
            self.draw_text()

    def draw_text(self):

        self.draw_enemy_text()
        self.draw_dwarf_text()
        if len(Static_Data.get_deck_list().hand) > 0:
            for x in range(len(self.sprites_list_cards)):
                arcade.draw_text(Static_Data.get_deck_list().hand[x].value,
                                 self.sprites_list_cards[x].center_x,
                                 self.sprites_list_cards[x].center_y - 30,
                                 arcade.color.BLACK,
                                 10)
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

    def draw_dwarf_text(self):
        for x in range(len(self.sprites_list_dwarves)):
            arcade.draw_text(Static_Data.get_list_of_people()[x].health,
                             self.sprites_list_dwarves_health[x].center_x + 30,
                             self.sprites_list_dwarves_health[x].center_y - 50,
                             arcade.color.REDWOOD,
                             20)

            arcade.draw_text(Static_Data.get_list_of_people()[x].defend,
                             self.sprites_list_dwarves_defend[x].center_x + 40,
                             self.sprites_list_dwarves_defend[x].center_y,
                             arcade.color.BLACK,
                             20)
            arcade.draw_text(Static_Data.get_list_of_people()[x].amount_energy,
                             self.sprites_list_dwarves_energy[x].center_x - 30,
                             self.sprites_list_dwarves_energy[x].center_y,
                             arcade.color.BLACK,
                             20)

    def draw_enemy_text(self):
        for x in range(len(self.sprites_list_enemies)):
            arcade.draw_text(Static_Data.get_enemies_to_defeat()[x].health,
                             self.sprites_list_enemies[x].center_x + 30,
                             self.sprites_list_enemies[x].center_y - 50,
                             arcade.color.REDWOOD,
                             10)
            arcade.draw_text(Static_Data.get_enemies_to_defeat()[x].value,
                             self.sprites_list_enemies_indicator[x].center_x + 40,
                             self.sprites_list_enemies_indicator[x].center_y,
                             arcade.color.WHITE,
                             10)
            arcade.draw_text(Static_Data.get_enemies_to_defeat()[x].defend,
                             self.sprites_list_enemies_defend[x].center_x + 40,
                             self.sprites_list_enemies_defend[x].center_y,
                             arcade.color.WHITE,
                             10)

    # Gjør så lite som mulig, annet enn å tegne
    def on_update(self, delta_time: float):
        self.combat_class.start_combat(self)
        if len(Static_Data.get_enemies_to_defeat()) < 1:
            Static_Data_Bools.set_combat(False)
            Deck_management.reset_deck()
            map_view = GUI.MapWindowTest()
            self.window.show_view(map_view)
            map_view.setup()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        card = arcade.get_sprites_at_point((x, y), self.sprites_list_cards)

        if len(card) > 0:
            primary_card = card[-1]
            self.held_card = [primary_card]
            self.held_cards_original_position = primary_card.position

            indicator, distance = arcade.get_closest_sprite(self.held_card[0], self.sprites_list_cards_indicator)

            self.held_card_indicator = [indicator]
            self.held_card_indicator_original_position = indicator.position
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

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):

        for card in self.held_card:
            card.center_x += dx
            card.center_y += dy

        for x in range(len(self.held_card_indicator)):
            self.held_card_indicator[x].center_x += dx
            self.held_card_indicator[x].center_y += dy

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        # If we don't have any cards, who cares
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
                                                             self.sprites_list_enemies.index(enemies),
                                                             self.active_dwarf)
            if result:
                self.change_active_dwarf()
                self.update_cards()
                self.update_enemies()
                self.update_dwarves()

        # We are no longer holding cards
        self.held_card = []
        self.held_card_indicator = []

    def make_SpriteList_from_numbers(self, number_inn, x_position_inn, y_position_inn):
        sprite_list_temporary = arcade.SpriteList()
        SIZE_CONSTANT = 0.30
        string_number = str(number_inn)
        for x in range(len(string_number)):
            if string_number[x] == "0":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Zero.value, SIZE_CONSTANT))
            elif string_number[x] == "1":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.One.value, SIZE_CONSTANT))
            elif string_number[x] == "2":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Two.value, SIZE_CONSTANT))
            elif string_number[x] == "3":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Three.value, SIZE_CONSTANT))
            elif string_number[x] == "4":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Four.value, SIZE_CONSTANT))
            elif string_number[x] == "5":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Five.value, SIZE_CONSTANT))
            elif string_number[x] == "6":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Six.value, SIZE_CONSTANT))
            elif string_number[x] == "7":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Seven.value, SIZE_CONSTANT))
            elif string_number[x] == "8":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Eight.value, SIZE_CONSTANT))
            elif string_number[x] == "9":
                sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Nine.value, SIZE_CONSTANT))
        for x in range(len(sprite_list_temporary)):
            sprite_list_temporary[x].center_x = x_position_inn + (x*24)
            sprite_list_temporary[x].center_y = y_position_inn
        return sprite_list_temporary

