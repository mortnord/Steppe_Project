import Generation.Initial_Generation
from Static_Data import Static_Data


def create_next_areas():


    possible_areas = []
    for x in range(len(Static_Data.get_current_map().connections)):  # Vi legger til alle områdene som vi har en connection til
        possible_areas.append(Static_Data.get_map_with_regions()[Static_Data.get_current_map().connections[x].nr_region])
        print(possible_areas)
    return possible_areas