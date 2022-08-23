import arcade

import Enumerators
import GUI_Calculations
from Inventory import Inventory
from Static_Data import Static_Data
from GUI_Dirc import GUI


class Equipment_View(arcade.View):
    def __init__(self):
        super().__init__()
        self.other_UI_UI = arcade.SpriteList()
        self.sprite_dwarves = arcade.SpriteList()
        self.sprite_equipment_dwarves_list = []
        self.equipment_sprites = arcade.SpriteList()
        self.width, self.height = arcade.window_commands.get_display_size()
        self.scaling_x = 1920 / self.width
        self.scaling_y = 1080 / self.height
        self.held_item = []

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_OLIVE_GREEN)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def setup(self):
        self.update_other_UI()
        self.update_dwarves()
        self.update_equipment()

    def on_draw(self):
        self.clear()
        self.other_UI_UI.draw()
        self.sprite_dwarves.draw()
        for x in range(len(self.sprite_equipment_dwarves_list)):
            self.sprite_equipment_dwarves_list[x].draw()

        self.equipment_sprites.draw()


    def update_other_UI(self):
        self.other_UI_UI.clear()

        self.other_UI_UI.append(arcade.Sprite(Enumerators.Button_Sprites.Back.value, 0.40))
        self.other_UI_UI[0].center_x = 100 / self.scaling_x
        self.other_UI_UI[0].center_y = 1000 / self.scaling_y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        UI_clicked = arcade.get_sprites_at_point((x, y), self.other_UI_UI)
        if len(UI_clicked):
            map_view = GUI.Map_View()
            map_view.setup()
            Static_Data.get_window().show_view(map_view)
        equipment_clicked = arcade.get_sprites_at_point((x, y), self.equipment_sprites)
        if len(equipment_clicked):
            equip_click = equipment_clicked[-1]
            self.held_item = [equip_click]

    def update_dwarves(self):
        self.sprite_dwarves.clear()
        for x in range(len(Static_Data.get_list_of_people())):
            self.sprite_dwarves.append(arcade.Sprite(Static_Data.get_list_of_people()[x].sprite, 0.10))
        length_divider = self.width / 4
        for x in range(len(self.sprite_dwarves)):
            self.sprite_dwarves[x].center_x = length_divider * (x + 1) / self.scaling_x
            self.sprite_dwarves[x].center_y = 700 / self.scaling_y
        for x in range(len(self.sprite_dwarves)):
            self.sprite_equipment_dwarves_list.append(GUI_Calculations.make_SpriteList_from_equipment_list(Static_Data.get_list_of_people()[x],
                                                                     self.sprite_dwarves[x]))

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):

        for equip_click in self.held_item:
            equip_click.center_x += dx
            equip_click.center_y += dy

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.held_item:
            dwarves, distance_equipment = arcade.get_closest_sprite(self.held_item[0], self.sprite_dwarves)
            if arcade.check_for_collision(self.held_item[0],dwarves):
                nr_item = self.equipment_sprites.index(self.held_item[0])
                if Inventory.equipment[nr_item].type == Enumerators.Equipment_types.Weapon:
                    Inventory.equipment.append(Static_Data.get_list_of_people()[self.sprite_dwarves.index(dwarves)].weapon)
                    Static_Data.get_list_of_people()[self.sprite_dwarves.index(dwarves)].weapon = Inventory.equipment.pop(nr_item)
                elif Inventory.equipment[nr_item].type == Enumerators.Equipment_types.Armor:
                    Inventory.equipment.append(Static_Data.get_list_of_people()[self.sprite_dwarves.index(dwarves)].armor)
                    Static_Data.get_list_of_people()[self.sprite_dwarves.index(dwarves)].armor = Inventory.equipment.pop(nr_item)
                elif Inventory.equipment[nr_item].type == Enumerators.Equipment_types.Ring:
                    Inventory.equipment.append(Static_Data.get_list_of_people()[self.sprite_dwarves.index(dwarves)].ring)
                    Static_Data.get_list_of_people()[self.sprite_dwarves.index(dwarves)].ring = Inventory.equipment.pop(nr_item)
                elif Inventory.equipment[nr_item].type == Enumerators.Equipment_types.Cloak:
                    Inventory.equipment.append(Static_Data.get_list_of_people()[self.sprite_dwarves.index(dwarves)].cloak)
                    Static_Data.get_list_of_people()[self.sprite_dwarves.index(dwarves)].cloak = Inventory.equipment.pop(nr_item)
            self.update_dwarves()
            self.held_item = []
            self.update_equipment()

    def update_equipment(self):
        self.equipment_sprites.clear()
        for x in range(len(Inventory.equipment)):
            self.equipment_sprites.append(arcade.Sprite(Inventory.equipment[x].sprite, 0.20))
        cards_in_a_row = 0
        y_split = 0
        x_split = 0
        for x in range(len(self.equipment_sprites)):
            self.equipment_sprites[x].center_x = 150 + x_split / self.scaling_x
            self.equipment_sprites[x].center_y = 300 + y_split / self.scaling_y
            x_split += 70
            cards_in_a_row += 1
            if cards_in_a_row > 9:
                cards_in_a_row = 0
                y_split -= 100
                x_split = 0
