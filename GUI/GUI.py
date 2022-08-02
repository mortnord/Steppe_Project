import arcade
from pyglet.math import Vec2

from Static_Data import Static_Data


class MapWindowTest(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Test", resizable=True)
        self.coin_list = None

        arcade.set_background_color(arcade.color.AMAZON)
        self.camera_sprites = arcade.Camera(600, 600)

    def setup(self):
        self.coin_list = arcade.SpriteList()
        # Create the coins
        for i in range(len(Static_Data.get_map_with_regions())):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("Assets/coinGold_ul.png",
                                 0.25)

            # Position the coin
            coin.center_x = Static_Data.get_map_with_regions()[i].x_position
            coin.center_y = Static_Data.get_map_with_regions()[i].y_position
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

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.draw_connections()
        self.camera_sprites.use()
        self.coin_list.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.coin_list.update()
        self.camera_sprites.set_projection()
