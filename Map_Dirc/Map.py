import arcade

import Enumerators
from Generation import Initial_Generation
from Map_Dirc import Map_Region, Connection, Landscape
from Static_Data import Static_Data


def make_connection(x_position, y_position, target_x, target_y, nr_target,
                    distance):  # Denne lager connectionen mellom regioner
    return Connection.Map_Connection(x_position, y_position, target_x, target_y, distance, nr_target)


def find_connections():  # Komplisert.
    for x in range(len(Static_Data.get_map_with_regions())):  # for alle regioner,
        for y in range(len(Static_Data.get_map_with_regions())):  # til alle andre regioner effektivt
            distance = arcade.get_distance(Static_Data.get_map_with_regions()[x].x_position,
                                           Static_Data.get_map_with_regions()[x].y_position,
                                           Static_Data.get_map_with_regions()[y].x_position,
                                           Static_Data.get_map_with_regions()[
                                               y].y_position)  # mål distansen mellom de 2 regionene
            if distance == 0.0:  # Den måler mot seg selv, så da skipper vi det
                pass
            else:  # Vi har en annen region i siktet
                Static_Data.get_map_with_regions()[x].connections.append(make_connection(
                    Static_Data.get_map_with_regions()[x].x_position,
                    Static_Data.get_map_with_regions()[x].y_position,
                    Static_Data.get_map_with_regions()[y].x_position,
                    Static_Data.get_map_with_regions()[y].y_position,
                    Static_Data.get_map_with_regions()[y].landscape.Landscapes_ID,
                    distance))  # her lager vi en connection og legger den til i Region sin connection liste.

    for x in range(len(Static_Data.get_map_with_regions())):

        Static_Data.get_map_with_regions()[x].connections.sort(key=lambda
            z: z.distance)  # Vi sorter connection-lista basert på distansen, slik at de 3 nærmeste er på bunnen

        while (len(Static_Data.get_map_with_regions()[x].connections)) > 3:  # så, fjerner vi alle untatt de 3 første,
            # dette gjør at kun de 3 nærmeste er igjen
            Static_Data.get_map_with_regions()[x].connections.pop()


def map_generation():
    zoom_multiplier = 70  # størrelse multiplier
    valid_map_checked = True
    list_of_regions = []
    list_of_regions.append(Map_Region.Region(-3 * zoom_multiplier, 0 * zoom_multiplier, Landscape.City()))  # start-byen
    while valid_map_checked:
        for x in range(-3, 3):  # Lag en 6x4 område med 95% sjangse på å generate en region
            for y in range(-2, 2):
                list_of_regions.append(Map_Region.Region((x + 1) * zoom_multiplier, y * zoom_multiplier,
                                                         Initial_Generation.next_map_generation()))
        needed_regions = 0
        wood_checked = False
        stone_checked = False
        for x in range(len(list_of_regions)):
            if list_of_regions[x].landscape.type_of_landscape == Enumerators.Landscapes.Wooded and wood_checked is False:
                needed_regions += 1
                wood_checked = True
            if list_of_regions[x].landscape.type_of_landscape == Enumerators.Landscapes.Hills and stone_checked is False:
                needed_regions += 1
                stone_checked = True
        if needed_regions == 2:
            valid_map_checked = False
        else:
            list_of_regions = []
    list_of_regions.append(Map_Region.Region(4 * zoom_multiplier, 0 * zoom_multiplier, Landscape.City()))  # slutt-byen.

    Static_Data.set_map_with_regions(list_of_regions)
    find_connections()
