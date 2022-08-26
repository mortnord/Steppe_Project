import arcade
from pyglet.math import Vec2

import Background_Calculations
import Enumerators
import GUI_Calculations
import Turn_And_Background_Actions.turn_action
from Events import Random_Event
from GUI_Dirc import Combat_View, Deck_GUI, Equipment_View
from Inventory import Inventory
from Static_Data import Static_Data
from Commands_Dirc import Migration, Commands, Harvest_Commands, Inventory_and_herd_management
from Static_Data_Bools import Static_Data_Bools


class Map_View(arcade.View):
    def __init__(self):
        super().__init__()
        self.list_of_sheep_nr = []
        self.list_of_items_UI = []
        self.food_list = arcade.SpriteList()
        self.sheep_list = arcade.SpriteList()
        self.harvest_info = arcade.SpriteList()
        self.harvest_button = arcade.SpriteList()
        self.actions_UI = arcade.SpriteList()
        self.other_UI_UI = arcade.SpriteList()
        self.region_list = None
        self.arrow_list = None

        arcade.set_background_color(arcade.color.AMAZON)
        self.width, self.height = arcade.window_commands.get_display_size()
        self.camera_sprites = arcade.Camera(self.width, self.height)
        self.camera_correction_x = 300
        self.camera_correction_y = 300
        self.scaling_x = 1920 / self.width
        self.scaling_y = 1080 / self.height

    def draw_connections(self):
        for x in range(len(Static_Data.get_map_with_regions())):
            for y in range(len(Static_Data.get_map_with_regions()[x].connections)):
                arcade.draw_line(Static_Data.get_map_with_regions()[x].connections[y].own_x,
                                 Static_Data.get_map_with_regions()[x].connections[y].own_y,
                                 Static_Data.get_map_with_regions()[x].connections[y].target_x,
                                 Static_Data.get_map_with_regions()[x].connections[y].target_y, arcade.color.BLACK, 3)

    def setup(self):
        self.arrow_list = arcade.SpriteList()

        arrow = arcade.Sprite("Assets/red_arrow_down.png", 0.10)
        arrow.center_x = Static_Data.get_current_map().x_position - 10
        arrow.center_y = Static_Data.get_current_map().y_position + 30
        self.arrow_list.append(arrow)
        self.generate_region_map_sprites()
        self.generate_harvest_UI()
        self.generate_inventory_UI()
        self.generate_sheep_UI()
        self.generate_other_UI()
        self.update_number_sprites()
        position = Vec2(-self.camera_correction_x, -self.camera_correction_y)
        self.camera_sprites.move_to(position, 1)

    def on_show_view(self):
        arcade.set_viewport(300, self.window.width, 300, self.window.height)

    def generate_region_map_sprites(self):
        self.region_list = arcade.SpriteList()
        for x in range(len(Static_Data.get_map_with_regions())):
            # Create the coin instance
            size = 0.15
            if Static_Data.get_map_with_regions()[x].landscape.elite_difficulty:
                size = 0.40
            if Static_Data.get_map_with_regions()[x].landscape.type_of_landscape == Enumerators.Landscapes.Steppes:
                coin = arcade.Sprite(Enumerators.Landscapes_sprites.Steppes.value, size)
            elif Static_Data.get_map_with_regions()[x].landscape.type_of_landscape == Enumerators.Landscapes.Wooded:
                coin = arcade.Sprite(Enumerators.Landscapes_sprites.Wooded.value, size)
            elif Static_Data.get_map_with_regions()[x].landscape.type_of_landscape == Enumerators.Landscapes.Hills:
                coin = arcade.Sprite(Enumerators.Landscapes_sprites.Hills.value, size)
            else:
                coin = arcade.Sprite("Assets/coinGold_ul.png",
                                     0.25)
            # Position the coin
            coin.center_x = Static_Data.get_map_with_regions()[x].x_position / self.scaling_x

            coin.center_y = Static_Data.get_map_with_regions()[x].y_position / self.scaling_y

            # Add the coin to the lists
            self.region_list.append(coin)

    def on_draw(self):
        self.clear()

        self.draw_connections()
        self.camera_sprites.use()
        self.region_list.draw()
        self.arrow_list.draw()
        self.harvest_button.draw()
        self.harvest_info.draw()
        self.actions_UI.draw()
        self.food_list.draw()
        self.sheep_list.draw()
        self.other_UI_UI.draw()

        for x in range(len(self.list_of_items_UI)):
            self.list_of_items_UI[x].draw()
        for x in range(len(self.list_of_sheep_nr)):
            self.list_of_sheep_nr[x].draw()

    def on_update(self, delta_time: float):

        self.arrow_list[0].center_x = Static_Data.get_current_map().x_position - 10
        self.arrow_list[0].center_y = Static_Data.get_current_map().y_position + 30

        if Static_Data_Bools.get_combat():
            combat_view = Combat_View.Combat_View()
            combat_view.setup()
            self.window.show_view(combat_view)
        self.update_number_sprites()
        self.update_sheep_nr_slaughter()
        self.scaling_x = 1920 / self.height
        self.scaling_y = 1080 / self.width

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        map_region_selected = arcade.get_sprites_at_point((x - 300, y - 300), self.region_list)
        button_clicked = arcade.get_sprites_at_point((x - 300, y - 300), self.harvest_button)
        milk_clicked = arcade.get_sprites_at_point((x - 300, y - 300), self.food_list)
        sheep_clicked = arcade.get_sprites_at_point((x - 300, y - 300), self.list_of_sheep_nr[1])
        rams_clicked = arcade.get_sprites_at_point((x - 300, y - 300), self.list_of_sheep_nr[0])
        UI_clicked = arcade.get_sprites_at_point((x - 300, y - 300), self.other_UI_UI)
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

        if len(button_clicked):

            if Static_Data.get_Actions_Available() > 0:
                if button_clicked[0] == self.harvest_button[0]:
                    Harvest_Commands.harvest_grass(len(Static_Data.get_list_of_people()))
                elif button_clicked[0] == self.harvest_button[1]:
                    Harvest_Commands.harvest_wood(len(Static_Data.get_list_of_people()))
                elif button_clicked[0] == self.harvest_button[2]:
                    Harvest_Commands.harvest_stone(len(Static_Data.get_list_of_people()))
                elif button_clicked[0] == self.harvest_button[3]:
                    Harvest_Commands.fish_in_river()
                elif button_clicked[0] == self.harvest_button[4]:
                    Turn_And_Background_Actions.turn_action.take_Action()
                Background_Calculations.background_info()
        if len(milk_clicked):
            if Static_Data.get_Actions_Available() > 0:
                if milk_clicked[0] == self.food_list[1]:
                    Inventory_and_herd_management.conserve_food()
        if len(sheep_clicked):
            Inventory_and_herd_management.slaughter_sheep(Enumerators.TypeOfSheep.Ewe, 1)

        if len(rams_clicked):
            Inventory_and_herd_management.slaughter_sheep(Enumerators.TypeOfSheep.Ram, 1)
        if len(UI_clicked):
            if UI_clicked[0] == self.other_UI_UI[0]:
                deck_view = Deck_GUI.Deck_GUI()
                deck_view.setup()
                Static_Data.get_window().show_view(deck_view)
            if UI_clicked[0] == self.other_UI_UI[1]:
                equipment_view = Equipment_View.Equipment_View()
                equipment_view.setup()
                Static_Data.get_window().show_view(equipment_view)

    def generate_harvest_UI(self):
        self.harvest_button.clear()
        self.harvest_info.clear()

        self.harvest_button.append(arcade.Sprite(Enumerators.Button_Sprites.Harvest_Grass.value, 0.50))
        self.harvest_button.append(arcade.Sprite(Enumerators.Button_Sprites.Harvest_Wood.value, 0.50))
        self.harvest_button.append(arcade.Sprite(Enumerators.Button_Sprites.Harvest_Stone.value, 0.50))
        self.harvest_button.append(arcade.Sprite(Enumerators.Button_Sprites.Harvest_Fish.value, 0.50))
        self.harvest_button.append(arcade.Sprite(Enumerators.Button_Sprites.Pass.value, 0.50))
        for x in range(len(self.harvest_button)):
            self.harvest_button[x].center_x = (400 + 55 * x) / self.scaling_x
            self.harvest_button[x].center_y = 600 / self.scaling_y

        self.harvest_info.append(arcade.Sprite(Enumerators.Landscapes_sprites.Steppes.value, 0.15))
        self.harvest_info.append(arcade.Sprite(Enumerators.Landscapes_sprites.Wooded.value, 0.15))
        self.harvest_info.append(arcade.Sprite(Enumerators.Landscapes_sprites.Hills.value, 0.15))
        for x in range(len(self.harvest_info)):
            self.harvest_info[x].center_x = self.harvest_button[x].center_x
            self.harvest_info[x].center_y = self.harvest_button[x].center_y + 50

    def generate_sheep_UI(self):
        self.sheep_list.clear()

        self.sheep_list.append(arcade.Sprite(Enumerators.Sprites.Sheep.value, 0.03))
        self.sheep_list.append(arcade.Sprite(Enumerators.Sprites.Lamb.value, 0.03))
        for x in range(len(self.sheep_list)):
            self.sheep_list[x].center_x = (1000 + x * 50) / self.scaling_x
            self.sheep_list[x].center_y = 600 / self.scaling_y
        self.update_sheep_nr_slaughter()

    def generate_inventory_UI(self):
        self.food_list.clear()

        self.food_list.append(arcade.Sprite(Enumerators.Sprites.Meat.value, 0.20))
        self.food_list.append(arcade.Sprite(Enumerators.Sprites.Milk.value, 0.20))
        for x in range(len(self.food_list)):
            self.food_list[x].center_x = (250 + 55 * x) / self.scaling_x
            self.food_list[x].center_y = 600 / self.scaling_y

    def update_number_sprites(self):
        self.actions_UI = GUI_Calculations.make_SpriteList_from_numbers(int(Static_Data.get_Actions_Available()),
                                                                        self.harvest_button[
                                                                            len(self.harvest_button) - 1].center_x + 50,
                                                                        self.harvest_button[
                                                                            len(self.harvest_button) - 1].center_y)
        self.list_of_items_UI.clear()

        self.list_of_items_UI.append(GUI_Calculations.make_SpriteList_from_numbers(int(Inventory.get_grass_amount()),
                                                                                   self.harvest_info[0].center_x,
                                                                                   self.harvest_info[0].center_y + 50))
        self.list_of_items_UI.append(GUI_Calculations.make_SpriteList_from_numbers(int(Inventory.get_wood_amount()),
                                                                                   self.harvest_info[1].center_x,
                                                                                   self.harvest_info[1].center_y + 50))
        self.list_of_items_UI.append(GUI_Calculations.make_SpriteList_from_numbers(int(Inventory.get_stone_amount()),
                                                                                   self.harvest_info[2].center_x,
                                                                                   self.harvest_info[2].center_y + 50))
        self.list_of_items_UI.append(
            GUI_Calculations.make_SpriteList_from_numbers(int(Inventory.get_temporary_food_amount()),
                                                          self.food_list[1].center_x,
                                                          self.food_list[1].center_y + 50))
        self.list_of_items_UI.append(GUI_Calculations.make_SpriteList_from_numbers(int(Inventory.get_food_amount()),
                                                                                   self.food_list[0].center_x,
                                                                                   self.food_list[0].center_y + 50))

        self.list_of_items_UI.append(
            GUI_Calculations.make_SpriteList_from_numbers(int(Static_Data.get_current_map().landscape.amount_of_grass),
                                                          self.harvest_info[0].center_x,
                                                          self.harvest_info[0].center_y - 100))
        self.list_of_items_UI.append(
            GUI_Calculations.make_SpriteList_from_numbers(int(Static_Data.get_current_map().landscape.amount_of_wood),
                                                          self.harvest_info[1].center_x,
                                                          self.harvest_info[1].center_y - 100))
        self.list_of_items_UI.append(
            GUI_Calculations.make_SpriteList_from_numbers(int(Static_Data.get_current_map().landscape.amount_of_stone),
                                                          self.harvest_info[2].center_x,
                                                          self.harvest_info[2].center_y - 100))

    def update_sheep_nr_slaughter(self):

        self.list_of_sheep_nr.clear()
        type_of_sheeps = Inventory_and_herd_management.look_over_sheeps(
            Static_Data.get_list_of_sheeps())  # male, female, male_lamb, female_lamb
        self.list_of_sheep_nr.append(GUI_Calculations.make_SpriteList_from_numbers(int(type_of_sheeps[0]),
                                                                                   self.sheep_list[0].center_x,
                                                                                   self.sheep_list[0].center_y + 50))
        self.list_of_sheep_nr.append(GUI_Calculations.make_SpriteList_from_numbers(int(type_of_sheeps[1]),
                                                                                   self.sheep_list[0].center_x,
                                                                                   self.sheep_list[0].center_y - 50))
        self.list_of_sheep_nr.append(GUI_Calculations.make_SpriteList_from_numbers(int(type_of_sheeps[2]),
                                                                                   self.sheep_list[1].center_x,
                                                                                   self.sheep_list[1].center_y + 50))
        self.list_of_sheep_nr.append(GUI_Calculations.make_SpriteList_from_numbers(int(type_of_sheeps[3]),
                                                                                   self.sheep_list[1].center_x,
                                                                                   self.sheep_list[1].center_y - 50))
        self.list_of_sheep_nr.append(
            GUI_Calculations.make_SpriteList_from_numbers(int(len(Static_Data.get_list_of_sheeps())),
                                                          self.sheep_list[0].center_x - 50,
                                                          self.sheep_list[0].center_y + 10))
        self.list_of_sheep_nr.append(
            GUI_Calculations.make_SpriteList_from_numbers(Static_Data.get_Amount_of_Grass_eating_per_action(),
                                                          self.sheep_list[0].center_y - 150,
                                                          self.sheep_list[0].center_x + 100))

    def generate_other_UI(self):
        self.other_UI_UI.clear()

        self.other_UI_UI.append(arcade.Sprite(Enumerators.Button_Sprites.Deck_UI.value, 0.40))
        self.other_UI_UI.append(arcade.Sprite(Enumerators.Button_Sprites.Equipment.value, 0.40))
        self.other_UI_UI[0].center_x = -200 / self.scaling_x
        self.other_UI_UI[0].center_y = 700 / self.scaling_y
        self.other_UI_UI[1].center_x = -200 / self.scaling_x
        self.other_UI_UI[1].center_y = 600 / self.scaling_y
