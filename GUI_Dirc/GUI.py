import arcade
from pyglet.math import Vec2

import Commands_Dirc.Commands
import Setup
from Events import Random_Event
from GUI_Dirc import Combat_View
from Static_Data import Static_Data
from Commands_Dirc import Migration
from Static_Data_Bools import Static_Data_Bools


class MapWindowTest(arcade.View):
    def __init__(self):
        super().__init__()
        self.region_list = None
        self.arrow_list = None

        arcade.set_background_color(arcade.color.AMAZON)
        self.camera_sprites = arcade.Camera(600, 600)

    def setup(self):
        self.region_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()

        arrow = arcade.Sprite("Assets/red_arrow_down.png", 0.10)
        arrow.center_x = Static_Data.get_current_map().x_position - 10
        arrow.center_y = Static_Data.get_current_map().y_position + 30
        self.arrow_list.append(arrow)
        # Create the coins
        for x in range(len(Static_Data.get_map_with_regions())):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("Assets/coinGold_ul.png",
                                 0.25)

            # Position the coin
            coin.center_x = Static_Data.get_map_with_regions()[x].x_position
            coin.center_y = Static_Data.get_map_with_regions()[x].y_position
            print(coin.center_x)
            print(coin.center_y)
            # Add the coin to the lists
            self.region_list.append(coin)

        position = Vec2(-300, -300)
        self.camera_sprites.move_to(position, 1)

    def draw_connections(self):
        for x in range(len(Static_Data.get_map_with_regions())):
            for y in range(len(Static_Data.get_map_with_regions()[x].connections)):
                arcade.draw_line(Static_Data.get_map_with_regions()[x].connections[y].own_x,
                                 Static_Data.get_map_with_regions()[x].connections[y].own_y,
                                 Static_Data.get_map_with_regions()[x].connections[y].target_x,
                                 Static_Data.get_map_with_regions()[x].connections[y].target_y, arcade.color.BLACK, 3)
            arcade.draw_text(str(Static_Data.get_map_with_regions()[x].nr_region),
                             Static_Data.get_map_with_regions()[x].x_position,
                             Static_Data.get_map_with_regions()[x].y_position,
                             arcade.color.GREEN, 40, 80, 'left')

    def on_draw(self):
        self.clear()
        self.draw_connections()
        self.camera_sprites.use()
        self.region_list.draw()
        self.arrow_list.draw()

    def on_update(self, delta_time: float):

        self.arrow_list[0].center_x = Static_Data.get_current_map().x_position - 10
        self.arrow_list[0].center_y = Static_Data.get_current_map().y_position + 30

        if Static_Data_Bools.get_combat():
            combat_view = Combat_View.Combat_View()
            combat_view.setup()
            self.window.show_view(combat_view)
        Setup.run_Game()
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        map_region_selected = arcade.get_sprites_at_point((x - 300, y - 300), self.region_list)
        if len(map_region_selected) > 0:
            possible_areas = Migration.create_next_areas()
            if Static_Data.get_map_with_regions()[self.region_list.index(map_region_selected[0])] in possible_areas:

                Commands_Dirc.Commands.migrate(
                    Static_Data.get_map_with_regions()[self.region_list.index(map_region_selected[0])])

                Random_Event.handle_event()  # Random event
                if Static_Data_Bools.get_combat():
                    combat_view = Combat_View.Combat_View()
                    combat_view.setup()
                    Static_Data.get_window().show_view(combat_view)


