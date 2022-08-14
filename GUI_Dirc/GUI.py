import arcade
from pyglet.math import Vec2

import Background_Calculations
import Enumerators
from Events import Random_Event
from GUI_Dirc import Combat_View
from Inventory import Inventory
from Static_Data import Static_Data
from Commands_Dirc import Migration, Commands, Harvest_Commands
from Static_Data_Bools import Static_Data_Bools


class Map_View(arcade.View):
    def __init__(self):
        super().__init__()
        self.region_list = None
        self.arrow_list = None

        arcade.set_background_color(arcade.color.AMAZON)
        self.camera_sprites = arcade.Camera(600, 600)

    def setup(self):
        self.arrow_list = arcade.SpriteList()

        arrow = arcade.Sprite("Assets/red_arrow_down.png", 0.10)
        arrow.center_x = Static_Data.get_current_map().x_position - 10
        arrow.center_y = Static_Data.get_current_map().y_position + 30
        self.arrow_list.append(arrow)
        self.generate_region_map_sprites()
        self.generate_harvest_UI()

        position = Vec2(-300, -300)
        self.camera_sprites.move_to(position, 1)

    def generate_region_map_sprites(self):
        self.region_list = arcade.SpriteList()
        for x in range(len(Static_Data.get_map_with_regions())):
            # Create the coin instance

            if Static_Data.get_map_with_regions()[x].landscape.type_of_landscape == Enumerators.Landscapes.Steppes:
                coin = arcade.Sprite(Enumerators.Landscapes_sprites.Steppes.value, 0.15)
            elif Static_Data.get_map_with_regions()[x].landscape.type_of_landscape == Enumerators.Landscapes.Wooded:
                coin = arcade.Sprite(Enumerators.Landscapes_sprites.Wooded.value, 0.15)
            elif Static_Data.get_map_with_regions()[x].landscape.type_of_landscape == Enumerators.Landscapes.Hills:
                coin = arcade.Sprite(Enumerators.Landscapes_sprites.Hills.value, 0.15)
            else:
                coin = arcade.Sprite("Assets/coinGold_ul.png",
                                     0.25)
            # Position the coin
            coin.center_x = Static_Data.get_map_with_regions()[x].x_position
            coin.center_y = Static_Data.get_map_with_regions()[x].y_position
            # Add the coin to the lists
            self.region_list.append(coin)

    def draw_connections(self):
        for x in range(len(Static_Data.get_map_with_regions())):
            for y in range(len(Static_Data.get_map_with_regions()[x].connections)):
                arcade.draw_line(Static_Data.get_map_with_regions()[x].connections[y].own_x,
                                 Static_Data.get_map_with_regions()[x].connections[y].own_y,
                                 Static_Data.get_map_with_regions()[x].connections[y].target_x,
                                 Static_Data.get_map_with_regions()[x].connections[y].target_y, arcade.color.BLACK, 3)

    def on_draw(self):
        self.clear()
        self.draw_connections()
        self.camera_sprites.use()
        self.region_list.draw()
        self.arrow_list.draw()
        self.harvest_button.draw()
        self.harvest_info.draw()
        self.actions_UI.draw()
        for x in range(len(self.list_of_items_UI)):
            self.list_of_items_UI[x].draw()

    def on_update(self, delta_time: float):

        self.arrow_list[0].center_x = Static_Data.get_current_map().x_position - 10
        self.arrow_list[0].center_y = Static_Data.get_current_map().y_position + 30

        if Static_Data_Bools.get_combat():
            combat_view = Combat_View.Combat_View()
            combat_view.setup()
            self.window.show_view(combat_view)
        self.update_inventory_sprites()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        map_region_selected = arcade.get_sprites_at_point((x - 300, y - 300), self.region_list)
        if len(map_region_selected) > 0:
            possible_areas = Migration.create_next_areas()
            if Static_Data.get_map_with_regions()[self.region_list.index(map_region_selected[0])] in possible_areas:

                Commands.migrate(
                    Static_Data.get_map_with_regions()[self.region_list.index(map_region_selected[0])])

                Random_Event.handle_event()  # Random event
                if Static_Data_Bools.get_combat():
                    combat_view = Combat_View.Combat_View()
                    combat_view.setup()
                    Static_Data.get_window().show_view(combat_view)
        button_clicked = arcade.get_sprites_at_point((x - 300, y - 300), self.harvest_button)

        if len(button_clicked) > 0:
            zero = 0
            print(Static_Data.get_Actions_Available())
            if Static_Data.get_Actions_Available() > zero:
                if button_clicked[0] == self.harvest_button[0]:
                    Harvest_Commands.harvest_grass(len(Static_Data.get_list_of_people()))
                elif button_clicked[0] == self.harvest_button[1]:
                    Harvest_Commands.harvest_wood(len(Static_Data.get_list_of_people()))
                elif button_clicked[0] == self.harvest_button[2]:
                    Harvest_Commands.harvest_stone(len(Static_Data.get_list_of_people()))
                elif button_clicked[0] == self.harvest_button[3]:
                    Harvest_Commands.fish_in_river()
                Background_Calculations.background_info()

    def generate_harvest_UI(self):

        self.harvest_button = arcade.SpriteList()
        self.harvest_info = arcade.SpriteList()

        self.harvest_button.append(arcade.Sprite(Enumerators.Button_Sprites.Harvest_Grass.value, 0.50))
        self.harvest_button.append(arcade.Sprite(Enumerators.Button_Sprites.Harvest_Wood.value, 0.50))
        self.harvest_button.append(arcade.Sprite(Enumerators.Button_Sprites.Harvest_Stone.value, 0.50))
        self.harvest_button.append(arcade.Sprite(Enumerators.Button_Sprites.Harvest_Fish.value, 0.50))
        for x in range(len(self.harvest_button)):
            self.harvest_button[x].center_x = -150 + 55 * x
            self.harvest_button[x].center_y = 175

        self.harvest_info.append(arcade.Sprite(Enumerators.Landscapes_sprites.Steppes.value, 0.15))
        self.harvest_info.append(arcade.Sprite(Enumerators.Landscapes_sprites.Wooded.value, 0.15))
        self.harvest_info.append(arcade.Sprite(Enumerators.Landscapes_sprites.Hills.value, 0.15))
        for x in range(len(self.harvest_info)):
            self.harvest_info[x].center_x = self.harvest_button[x].center_x
            self.harvest_info[x].center_y = self.harvest_button[x].center_y + 50

        self.update_inventory_sprites()

    def update_inventory_sprites(self):
        self.actions_UI = Combat_View.make_SpriteList_from_numbers(int(Static_Data.get_Actions_Available()),
                                                                   self.harvest_button[0].center_x - 100,
                                                                   self.harvest_button[0].center_y)
        self.list_of_items_UI = []

        self.list_of_items_UI.append(Combat_View.make_SpriteList_from_numbers(int(Inventory.get_grass_amount()),
                                                                              self.harvest_info[0].center_x,
                                                                              self.harvest_info[0].center_y + 50))
        self.list_of_items_UI.append(Combat_View.make_SpriteList_from_numbers(int(Inventory.get_wood_amount()),
                                                                              self.harvest_info[1].center_x,
                                                                              self.harvest_info[1].center_y + 50))
        self.list_of_items_UI.append(Combat_View.make_SpriteList_from_numbers(int(Inventory.get_stone_amount()),
                                                                              self.harvest_info[2].center_x,
                                                                              self.harvest_info[2].center_y + 50))

        self.list_of_items_UI.append(
            Combat_View.make_SpriteList_from_numbers(int(Static_Data.get_current_map().landscape.amount_of_grass),
                                                     self.harvest_info[0].center_x,
                                                     self.harvest_info[0].center_y - 100))
        self.list_of_items_UI.append(
            Combat_View.make_SpriteList_from_numbers(int(Static_Data.get_current_map().landscape.amount_of_wood),
                                                     self.harvest_info[1].center_x,
                                                     self.harvest_info[1].center_y - 100))
        self.list_of_items_UI.append(
            Combat_View.make_SpriteList_from_numbers(int(Static_Data.get_current_map().landscape.amount_of_stone),
                                                     self.harvest_info[2].center_x,
                                                     self.harvest_info[2].center_y - 100))
