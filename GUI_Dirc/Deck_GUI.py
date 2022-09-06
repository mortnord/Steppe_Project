import arcade
from arcade.gui import UIManager

import Enumerators
import GUI_Calculations
from Static_Data import Static_Data
from GUI_Dirc import GUI


class Deck_GUI(arcade.View):
    def __init__(self):
        super().__init__()
        self.other_UI_UI = arcade.SpriteList()
        self.list_of_cards_text = []
        self.sprites_list_cards_indicator = arcade.SpriteList()
        self.sprites_list_cards_energy_indicator = arcade.SpriteList()
        self.sprites_list_cards = arcade.SpriteList()
        self.indicator_text_label = []
        self.info_text_label = []
        self.width, self.height = arcade.window_commands.get_display_size()
        self.scaling_x = 1920 / self.width
        self.scaling_y = 1080 / self.height
        self.manager = UIManager()
        self.manager.enable()
        self.text_manager = UIManager()
        self.text_manager.enable()

    def setup(self):
        self.update_cards()
        self.update_other_UI()

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_GREEN)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):

        self.clear()
        self.other_UI_UI.draw()
        self.sprites_list_cards.draw()
        self.sprites_list_cards_indicator.draw()
        self.sprites_list_cards_energy_indicator.draw()
        for card in self.list_of_cards_text:
            card.draw()
        self.text_manager.draw()

        self.manager.draw()

    def update_cards(self):
        self.sprites_list_cards.clear()
        self.sprites_list_cards_indicator.clear()
        self.list_of_cards_text = []
        for card in Static_Data.get_deck_list().content:
            self.sprites_list_cards.append(arcade.Sprite(card.sprite, 1))
            self.sprites_list_cards_indicator.append(
                arcade.Sprite(card.indicator_sprite, 1))
            if card.energy_required == 1:
                self.sprites_list_cards_energy_indicator.append(arcade.Sprite(Enumerators.Sprites.One_Energy.value))
            elif card.energy_required == 2:
                self.sprites_list_cards_energy_indicator.append(arcade.Sprite(Enumerators.Sprites.One_Energy.value))
            else:
                self.sprites_list_cards_energy_indicator.append(arcade.Sprite(Enumerators.Sprites.Free_Energy.value))

        cards_in_a_row = 0
        y_split = 0
        x_split = 0

        for x in range(len(self.sprites_list_cards)):

            self.sprites_list_cards[x].center_x = 150 + x_split / self.scaling_x
            self.sprites_list_cards[x].center_y = 800 + y_split / self.scaling_y

            self.sprites_list_cards_indicator[x].center_x = self.sprites_list_cards[x].center_x - 23
            self.sprites_list_cards_indicator[x].center_y = self.sprites_list_cards[x].center_y - 12.5

            self.sprites_list_cards_energy_indicator[x].center_x = self.sprites_list_cards[x].center_x - 70
            self.sprites_list_cards_energy_indicator[x].center_y = self.sprites_list_cards[x].center_y + 120.5

            self.indicator_text_label.append(arcade.gui.UITextArea(x=self.sprites_list_cards_indicator[x].center_x - 55,
                                                                   y=self.sprites_list_cards_indicator[x].center_y - 20,
                                                                   text=str(
                                                                       Static_Data.get_deck_list().content[x].value),
                                                                   width=1, height=1, font_size=24,
                                                                   font_name="Arial",
                                                                   text_color=arcade.color.BLACK))

            self.info_text_label.append(arcade.gui.UITextArea(x=self.sprites_list_cards_indicator[x].center_x - 50,
                                                              y=self.sprites_list_cards_indicator[x].center_y - 50,
                                                              text=GUI_Calculations.create_card_text_from_backend(
                                                                  Static_Data.get_deck_list().content[x]),
                                                              width=300, height=50, font_size=10,
                                                              font_name="Arial",
                                                              text_color=arcade.color.BLACK))
            self.indicator_text_label[x].fit_content()
            self.info_text_label[x].fit_content()
            self.text_manager.add(self.indicator_text_label[x])
            self.text_manager.add(self.info_text_label[x])
            x_split += 250
            cards_in_a_row += 1
            if cards_in_a_row > 6:
                cards_in_a_row = 0
                y_split -= 350
                x_split = 0

    def update_other_UI(self):
        self.other_UI_UI.clear()

        self.other_UI_UI.append(arcade.Sprite(Enumerators.Button_Sprites.Back.value, 0.40))
        self.other_UI_UI[0].center_x = 100 / self.scaling_x
        self.other_UI_UI[0].center_y = 1000 / self.scaling_y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.manager.clear()
        if button == arcade.MOUSE_BUTTON_LEFT:

            UI_clicked = arcade.get_sprites_at_point((x, y), self.other_UI_UI)
            if UI_clicked:
                map_view = GUI.Map_View()
                map_view.setup()
                Static_Data.get_window().show_view(map_view)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            card_clicked = arcade.get_sprites_at_point((x, y), self.sprites_list_cards)
            if card_clicked:
                card_object = Static_Data.get_deck_list().content[self.sprites_list_cards.index(card_clicked[0])]
                self.manager.add(GUI_Calculations.make_panel_from_card(x, y, card_object))
