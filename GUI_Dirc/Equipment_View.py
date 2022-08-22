import arcade

import Enumerators
from GUI_Calculations import make_SpriteList_from_numbers
from Static_Data import Static_Data
from GUI_Dirc import GUI


class Equipment_View(arcade.View):
    def __init__(self):
        super().__init__()
        self.other_UI_UI = arcade.SpriteList()
        self.width, self.height = arcade.window_commands.get_display_size()
        self.scaling_x = 1920 / self.width
        self.scaling_y = 1080 / self.height

    def setup(self):
        self.update_other_UI()

    def on_draw(self):
        self.clear()
        self.other_UI_UI.draw()

    def update_other_UI(self):
        self.other_UI_UI.clear()

        self.other_UI_UI.append(arcade.Sprite(Enumerators.Button_Sprites.Back.value, 0.40))
        self.other_UI_UI[0].center_x = -200 / self.scaling_x
        self.other_UI_UI[0].center_y = 700 / self.scaling_y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        UI_clicked = arcade.get_sprites_at_point((x - 300, y - 300), self.other_UI_UI)
        if len(UI_clicked):
            map_view = GUI.Map_View()
            map_view.setup()
            Static_Data.get_window().show_view(map_view)
