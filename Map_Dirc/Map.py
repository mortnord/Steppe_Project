import random
import math

import arcade

from Generation import Initial_Generation
from Map_Dirc import Map_Region, Connection, Landscape
from Static_Data import Static_Data


def make_connection(x_position, y_position, target_x, target_y, nr_target, region, distance):
    region.connections.append(
        Connection.Map_Connection(x_position, y_position, target_x, target_y, distance, nr_target))


def find_connections():
    for x in range(len(Static_Data.get_map_with_regions())):
        for y in range(len(Static_Data.get_map_with_regions())):
            distance = arcade.get_distance(Static_Data.get_map_with_regions()[x].x_position,
                                           Static_Data.get_map_with_regions()[x].y_position,
                                           Static_Data.get_map_with_regions()[y].x_position,
                                           Static_Data.get_map_with_regions()[y].y_position)
            make_connection(Static_Data.get_map_with_regions()[x].x_position,
                            Static_Data.get_map_with_regions()[x].y_position,
                            Static_Data.get_map_with_regions()[y].x_position,
                            Static_Data.get_map_with_regions()[y].y_position,
                            Static_Data.get_map_with_regions()[x].landscape.Landscapes_ID,
                            Static_Data.get_map_with_regions()[x],
                            distance)
        Static_Data.get_map_with_regions()[x].connections.sort(key=lambda z : z.distance)
        while len(Static_Data.get_map_with_regions()[x].connections) > 4:
            Static_Data.get_map_with_regions()[x].connections.pop()


def map_generation():
    zoom_multiplier = 40
    list_of_regions = []
    list_of_regions.append(Map_Region.Region(-7 * zoom_multiplier, 0 * zoom_multiplier, Landscape.City()))

    for x in range(-6, 6):
        for y in range(-4, 4):
            rand_nr = random.randint(1, 5)
            if rand_nr == 1:
                list_of_regions.append(Map_Region.Region((x + 1) * zoom_multiplier, y * zoom_multiplier,
                                                         Initial_Generation.next_map_generation()))

    list_of_regions.append(Map_Region.Region(7 * zoom_multiplier, 0 * zoom_multiplier, Landscape.City()))

    Static_Data.set_map_with_regions(list_of_regions)
    find_connections()