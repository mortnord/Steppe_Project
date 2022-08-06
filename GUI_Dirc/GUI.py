import arcade
from pyglet.math import Vec2

import Setup
from Static_Data import Static_Data


class MapWindowTest(arcade.View):
    def __init__(self):
        super().__init__()
        self.coin_list = None
        self.arrow_list = None

        arcade.set_background_color(arcade.color.AMAZON)
        self.camera_sprites = arcade.Camera(600, 600)

    def setup(self):
        self.coin_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()

        arrow = arcade.Sprite("Assets/red_arrow_down.png",0.10)
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
            # Add the coin to the lists
            self.coin_list.append(coin)


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
        arcade.start_render()
        self.draw_connections()
        self.camera_sprites.use()
        self.coin_list.draw()
        self.arrow_list.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):

        self.arrow_list[0].center_x = Static_Data.get_current_map().x_position - 10
        self.arrow_list[0].center_y = Static_Data.get_current_map().y_position + 30
        self.camera_sprites.set_projection()
        Setup.run_Game()

