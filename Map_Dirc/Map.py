import random

import arcade

from Generation import Initial_Generation
from Map_Dirc import Map_Region, Connection, Landscape
from Static_Data import Static_Data


def make_connection(x_position, y_position, target_x, target_y, nr_target, distance):
    return Connection.Map_Connection(x_position, y_position, target_x, target_y, distance, nr_target)


def find_connections():
    for x in range(len(Static_Data.get_map_with_regions())):
        for y in range(len(Static_Data.get_map_with_regions())):
            distance = arcade.get_distance(Static_Data.get_map_with_regions()[x].x_position,
                                           Static_Data.get_map_with_regions()[x].y_position,
                                           Static_Data.get_map_with_regions()[y].x_position,
                                           Static_Data.get_map_with_regions()[y].y_position)
            if distance == 0.0:
                pass
            else:
                Static_Data.get_map_with_regions()[x].connections.append(make_connection(
                                Static_Data.get_map_with_regions()[x].x_position,
                                Static_Data.get_map_with_regions()[x].y_position,
                                Static_Data.get_map_with_regions()[y].x_position,
                                Static_Data.get_map_with_regions()[y].y_position,
                                Static_Data.get_map_with_regions()[y].landscape.Landscapes_ID,
                                distance))

    for x in range(len(Static_Data.get_map_with_regions())):
        Static_Data.get_map_with_regions()[x].connections.sort(key=lambda z: z.distance)


        while (len(Static_Data.get_map_with_regions()[x].connections)) > 3:
            Static_Data.get_map_with_regions()[x].connections.pop()
            print("Vi fjerner stuff")
            print(Static_Data.get_map_with_regions()[x].connections)


def map_generation():
    zoom_multiplier = 70

    list_of_regions = []
    list_of_regions.append(Map_Region.Region(-3 * zoom_multiplier, 0 * zoom_multiplier, Landscape.City()))

    for x in range(-3, 3):
        for y in range(-2, 2):
            chance_to_generate = random.randint(1,20)
            if chance_to_generate == 1:
                pass
            else:
                list_of_regions.append(Map_Region.Region((x + 1) * zoom_multiplier, y * zoom_multiplier,
                                                         Initial_Generation.next_map_generation()))

    list_of_regions.append(Map_Region.Region(4 * zoom_multiplier, 0 * zoom_multiplier, Landscape.City()))

    Static_Data.set_map_with_regions(list_of_regions)
    find_connections()
