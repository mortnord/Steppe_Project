import arcade
from arcade.gui import UIManager

import Enumerators
import GUI_Calculations
from Static_Data import Static_Data
from GUI_Dirc import GUI


class Deck_GUI(arcade.View):
    def __init__(self):
        super().__init__()
        self.list_of_card_sprite_lists = []
        self.list_of_card_text = []
        self.other_UI_UI = arcade.SpriteList()
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
        for sprite_list in self.list_of_card_sprite_lists:
            sprite_list.draw()
        self.other_UI_UI.draw()
        self.text_manager.draw()
        self.manager.draw()

    def update_cards(self):
        self.list_of_card_sprite_lists.clear()
        for card in Static_Data.get_deck_list().content:
            self.list_of_card_sprite_lists.append(GUI_Calculations.make_card_sprite_list_from_backend(card))

        cards_in_a_row = 0
        y_split = 0
        x_split = 0
        for x, sprite_lists in enumerate(self.list_of_card_sprite_lists):
            for sprites_in_list in sprite_lists:
                sprite_lists[0].center_x = 150 + x_split
                sprite_lists[0].center_y = 800 + y_split
                sprite_lists[1].center_x = sprite_lists[0].center_x - 70
                sprite_lists[1].center_y = sprite_lists[0].center_y + 120.5
                sprite_lists[2].center_x = sprite_lists[0].center_x - 23
                sprite_lists[2].center_y = sprite_lists[0].center_y - 12.5
                sprite_lists[3].center_x = sprite_lists[0].center_x + 66
                sprite_lists[3].center_y = sprite_lists[0].center_y - 12.5
            self.list_of_card_text.append((arcade.gui.UILabel(x=sprite_lists[0].center_x - 80,
                                                                 y=sprite_lists[0].center_y - 30,
                                                                 text=str(Static_Data.get_deck_list().content[
                                                                              x].value),
                                                                 width=1, height=1, font_size=24,
                                                                 font_name="Arial",
                                                                 text_color=arcade.color.BLACK)))

            self.list_of_card_text.append(arcade.gui.UILabel(x=sprite_lists[0].center_x - 80,
                                                                y=sprite_lists[0].center_y - 80,
                                                                text=GUI_Calculations.create_card_text_from_backend(
                                                                    Static_Data.get_deck_list().content[x]),
                                                                width=300, height=50, font_size=10,
                                                                font_name="Arial",
                                                                text_color=arcade.color.BLACK))

            x_split += 250
            cards_in_a_row += 1
            if cards_in_a_row > 6:
                cards_in_a_row = 0
                y_split -= 350
                x_split = 0
            for text in self.list_of_card_text:
                text.fit_content()
                self.text_manager.add(text)

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
            sprite_list_nr = 0
            for sprite_list in self.list_of_card_sprite_lists:

                card_clicked = arcade.get_sprites_at_point((x, y), sprite_list)
                if card_clicked:
                    card_object = Static_Data.get_deck_list().content[sprite_list_nr]
                    self.manager.add(GUI_Calculations.make_panel_from_card(x, y, card_object))
                else:
                    sprite_list_nr += 1
