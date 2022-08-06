import arcade

import Setup
from Static_Data import Static_Data
#lag dette på nytt, der en kamp situasjon skifter til denne scenen, som lager fiender og alt relatert til kamp blir gjort her.
#lag fiender
#håndter fiender
#

class Combat_View(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def setup(self):
        self.sprites_list = arcade.SpriteList()
        for x in range(len(Static_Data.get_enemies_to_defeat())):
            self.sprites_list.append(arcade.Sprite(Static_Data.get_enemies_to_defeat()[x].sprite, 0.25))

        for x in range(len(self.sprites_list)):
            self.sprites_list[x].center_x = 150 * x
            self.sprites_list[x].center_y = 300
        print(len(self.sprites_list))

    def on_draw(self):
        """ Draw this view """
        self.clear()

        arcade.start_render()
        self.sprites_list.draw()

        arcade.finish_render()
    #Gjør så lite som mulig, annet enn å tegne
    def on_update(self, delta_time: float):
        Setup.run_Game()
        self.sprites_list.clear()
