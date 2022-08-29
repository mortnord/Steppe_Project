import random

import arcade

import Enumerators
from Generation import Initial_Generation
from Map_Dirc import Map_Region, Connection, Landscape
from Static_Data import Static_Data


def make_connection(x_position, y_position, target_x, target_y, nr_target,
                    distance):  # Denne lager connectionen mellom regioner
    return Connection.Map_Connection(x_position, y_position, target_x, target_y, distance, nr_target)


def find_connections():  # Komplisert.
    for first_region in Static_Data.get_map_with_regions():  # for alle regioner,
        for second_region in Static_Data.get_map_with_regions():  # til alle andre regioner effektivt
            distance = arcade.get_distance(first_region.x_position,
                                           first_region.y_position,
                                           second_region.x_position,
                                           second_region.y_position)
            if distance == 0.0:  # Den måler mot seg selv, så da skipper vi det
                pass
            else:  # Vi har en annen region i siktet
                first_region.connections.append(make_connection(
                    first_region.x_position,
                    first_region.y_position,
                    second_region.x_position,
                    second_region.y_position,
                    second_region.landscape.Landscapes_ID,
                    distance))  # her lager vi en connection og legger den til i Region sin connection liste.

    for map_region in Static_Data.get_map_with_regions():

        map_region.connections.sort(key=lambda z: z.distance)
        # Vi sorter connection-lista basert på distansen, slik at de 3 nærmeste er på bunnen

        while len(map_region.connections) > 3:  # så, fjerner vi alle untatt de 3 første,
            # dette gjør at kun de 3 nærmeste er igjen
            map_region.connections.pop()


def map_generation():
    zoom_multiplier = 150  # størrelse multiplier
    valid_map_checked = True
    list_of_regions = []
    while valid_map_checked:
        maps_generated = 0
        list_of_regions = [
            Map_Region.Region(0 * zoom_multiplier, 1 * zoom_multiplier, Landscape.City(), zoom_multiplier)]
        for x in range(0, 6):  # Lag en 6x4 område med 95% sjangse på å generate en region
            for y in range(0, 3):
                maps_generated += 1
                list_of_regions.append(Map_Region.Region((x + 1) * zoom_multiplier, y * zoom_multiplier,
                                                         Initial_Generation.next_map_generation(), zoom_multiplier))

        needed_regions = 0
        wood_checked = False
        stone_checked = False
        for map_region in list_of_regions:
            if map_region.landscape.type_of_landscape == Enumerators.Landscapes.Wooded and wood_checked is False:
                needed_regions += 1
                wood_checked = True
            if map_region.landscape.type_of_landscape == Enumerators.Landscapes.Hills and stone_checked is False:
                needed_regions += 1
                stone_checked = True
        if needed_regions == 2:
            valid_map_checked = False
        else:
            print(list_of_regions[0].landscape.Landscapes_ID)
            list_of_regions.clear()

            Static_Data.set_Landscape_ID(maps_generated + 1)

    list_of_regions.append(
        Map_Region.Region(7 * zoom_multiplier, 1 * zoom_multiplier, Landscape.City(), zoom_multiplier))  # slutt-byen.

    modify_map_with_elites_and_others(list_of_regions)
    Static_Data.set_map_with_regions(list_of_regions)
    find_connections()


def modify_map_with_elites_and_others(list_of_regions):
    elite_1 = random.choice(list_of_regions[1:12])
    elite_1.landscape.elite_difficulty = True

    elite_2 = random.choice(list_of_regions[13:25])
    elite_2.landscape.elite_difficulty = True
