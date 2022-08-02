import random
import math

from Generation import Initial_Generation
from Map_Dirc import Map_Region, Connection, Landscape
from Static_Data import Static_Data


def find_connections(region):
    connection_1 = 10000
    connection_2 = 10000
    connection_3 = 10000
    target_x_1 = 0
    target_y_1 = 0
    nr_target_1 = 0
    target_x_2 = 0
    target_y_2 = 0
    nr_target_2 = 0
    target_x_3 = 0
    target_y_3 = 0
    nr_target_3 = 0
    for x in range(len(Static_Data.get_map_with_regions())):
        distance = (math.dist([region.x_position, region.y_position], [Static_Data.get_map_with_regions()[x].x_position,
                                                                       Static_Data.get_map_with_regions()[
                                                                           x].y_position]))
        if distance == 0.0:
            pass
        elif distance < connection_1:
            connection_1 = distance
            target_x_1 = Static_Data.get_map_with_regions()[x].x_position
            target_y_1 = Static_Data.get_map_with_regions()[x].y_position
            nr_target_1 = x
        elif distance < connection_2:
            connection_2 = distance
            target_x_2 = Static_Data.get_map_with_regions()[x].x_position
            target_y_2 = Static_Data.get_map_with_regions()[x].y_position
            nr_target_2 = x
        elif distance < connection_3:
            connection_3 = distance
            target_x_3 = Static_Data.get_map_with_regions()[x].x_position
            target_y_3 = Static_Data.get_map_with_regions()[x].y_position
            nr_target_3 = x
    region.connections.append(
        Connection.Map_Connection(region.x_position, region.y_position, target_x_1, target_y_1, connection_1, nr_target_1))

    region.connections.append(
        Connection.Map_Connection(region.x_position, region.y_position, target_x_2, target_y_2, connection_2, nr_target_2))

    region.connections.append(
        Connection.Map_Connection(region.x_position, region.y_position, target_x_3, target_y_3, connection_3, nr_target_3))


def map_generation():
    list_of_regions = []
    list_of_regions.append(Map_Region.Region(-4, 0, Landscape.City()))

    for x in range(-4,4):
        for y in range(-6,6):
            rand_nr = random.randint(1, 5)
            if rand_nr == 1:
                list_of_regions.append(Map_Region.Region(x + 1, y,Initial_Generation.next_map_generation()))

    list_of_regions.append(Map_Region.Region(5, 0,Landscape.City()))

    Static_Data.set_map_with_regions(list_of_regions)
    for x in range(len(Static_Data.get_map_with_regions())):
        find_connections(Static_Data.get_map_with_regions()[x])
