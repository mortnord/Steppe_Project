import arcade

import Setup
from Commands_Dirc import Combat
from Static_Data import Static_Data


# lag dette på nytt, der en kamp situasjon skifter til denne scenen, som lager fiender og alt relatert til kamp blir gjort her.
# lag fiender
# håndter fiender
#

class Combat_View(arcade.View):
    combat_class = Combat.Combat()

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.held_card = []
        self.held_card_original_position = None
        self.held_card_indicator = []
        self.held_card_indicator_original_position = None

    def setup(self):
        self.sprites_list_enemies = arcade.SpriteList()
        self.sprites_list_enemies_indicator = arcade.SpriteList()
        self.sprites_list_cards_indicator = arcade.SpriteList()
        self.sprites_list_cards = arcade.SpriteList()
        self.sprites_list_dwarves = arcade.SpriteList()
        self.mouse_hand = arcade.SpriteList()
        for x in range(len(Static_Data.get_enemies_to_defeat())):
            self.sprites_list_enemies.append(arcade.Sprite(Static_Data.get_enemies_to_defeat()[x].sprite, 0.10))

        for x in range(len(self.sprites_list_enemies)):
            self.sprites_list_enemies[x].center_x = 150 * x + 150
            self.sprites_list_enemies[x].center_y = 400

        for x in range(len(Static_Data.get_deck_list().hand)):
            self.sprites_list_cards.append(arcade.Sprite(Static_Data.get_deck_list().hand[x].sprite, 0.20))

        for x in range(len(self.sprites_list_cards)):
            self.sprites_list_cards[x].center_x = 150 * x + 150
            self.sprites_list_cards[x].center_y = 100

        for x in range(len(Static_Data.get_list_of_people())):
            self.sprites_list_dwarves.append(arcade.Sprite(Static_Data.get_list_of_people()[x].sprite, 0.10))

        for x in range(len(self.sprites_list_dwarves)):
            self.sprites_list_dwarves[x].center_x = 150 * x + 150
            self.sprites_list_dwarves[x].center_y = 200

    def update_cards(self):
        self.sprites_list_cards.clear()
        for x in range(len(Static_Data.get_deck_list().hand)):
            self.sprites_list_cards.append(arcade.Sprite(Static_Data.get_deck_list().hand[x].sprite, 0.20))
            self.sprites_list_cards_indicator.append(arcade.Sprite(Static_Data.get_deck_list().hand[x].indicator_sprite,0.10))
        for x in range(len(self.sprites_list_cards)):
            self.sprites_list_cards[x].center_x = 150 * x + 150
            self.sprites_list_cards[x].center_y = 50
            self.sprites_list_cards_indicator[x].center_x = self.sprites_list_cards[x].center_x
            self.sprites_list_cards_indicator[x].center_y = self.sprites_list_cards[x].center_y

    def update_enemies(self):
        self.sprites_list_enemies.clear()
        for x in range(len(Static_Data.get_enemies_to_defeat())):
            self.sprites_list_enemies.append(arcade.Sprite(Static_Data.get_enemies_to_defeat()[x].sprite, 0.10))
            self.sprites_list_enemies_indicator.append(arcade.Sprite(Static_Data.get_enemies_to_defeat()[x].type_of_planned_attack_sprite,0.10))
        for x in range(len(self.sprites_list_enemies)):
            self.sprites_list_enemies[x].center_x = 150 * x + 150
            self.sprites_list_enemies[x].center_y = 400
            self.sprites_list_enemies_indicator[x].center_x = self.sprites_list_enemies[x].center_x
            self.sprites_list_enemies_indicator[x].center_y = self.sprites_list_enemies[x].center_y + 50

            arcade.draw_text(Static_Data.get_enemies_to_defeat()[x].value,
                             self.sprites_list_enemies_indicator[x].center_x + 40,
                             self.sprites_list_enemies_indicator[x].center_y,
                             arcade.color.WHITE,
                             1)


    def update_indications(self):
        self.sprites_list_enemies_indicator.clear()

    def on_draw(self):
        """ Draw this view """
        self.clear()

        arcade.start_render()
        self.sprites_list_enemies.draw()
        self.sprites_list_cards.draw()
        self.sprites_list_dwarves.draw()
        self.sprites_list_enemies_indicator.draw()
        self.sprites_list_cards_indicator.draw()
        for x in range(len(self.sprites_list_enemies)):
            arcade.draw_text(Static_Data.get_enemies_to_defeat()[x].value,
                             self.sprites_list_enemies_indicator[x].center_x + 30,
                             self.sprites_list_enemies_indicator[x].center_y,
                             arcade.color.WHITE,
                             10)
            arcade.draw_text(Static_Data.get_enemies_to_defeat()[x].health,
                             self.sprites_list_enemies[x].center_x,
                             self.sprites_list_enemies[x].center_y-50,
                             arcade.color.REDWOOD,
                             10)
        for x in range(len(self.sprites_list_cards)):
            arcade.draw_text(Static_Data.get_deck_list().hand[x].value,
                             self.sprites_list_cards[x].center_x,
                             self.sprites_list_cards[x].center_y-30,
                             arcade.color.BLACK,
                             10)
        arcade.finish_render()

    # Gjør så lite som mulig, annet enn å tegne
    def on_update(self, delta_time: float):
        self.combat_class.start_combat(self)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        card = arcade.get_sprites_at_point((x, y), self.sprites_list_cards)

        if len(card) > 0:
            primary_card = card[-1]
            self.held_card = [primary_card]
            self.held_cards_original_position = primary_card.position

        indicator, distance = arcade.get_closest_sprite(self.held_card[0],self.sprites_list_cards_indicator)


        self.held_card_indicator = [indicator]
        self.held_card_indicator_original_position = indicator.position

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
        dwarfs, distance_dwarfs = arcade.get_closest_sprite(self.held_card[0],self.sprites_list_dwarves)

        if(arcade.check_for_collision(self.held_card[0],enemies)):
            print("Using card "+ str((self.sprites_list_cards.index(self.held_card[0]) + 1)) + " on goblin" + str(self.sprites_list_enemies.index(enemies)))
        if(arcade.check_for_collision(self.held_card[0], dwarfs)):
            pass
            #do defense stuff here

        # We are no longer holding cards
        self.held_card = []
        self.held_card_indicator = []