import arcade

import Background_Calculations
import Generation.Initial_Generation
from GUI_Dirc import GUI
from Static_Data import Static_Data

def setup():
    Generation.Initial_Generation.start_initial_creation()
    Background_Calculations.background_info()  # Background info som actions osv
    window = arcade.Window(600, 600, "TEST")
    Static_Data.set_window(window)
    map_view = GUI.Map_View()
    Static_Data.get_window().show_view(map_view)
    map_view.setup()
    arcade.run()