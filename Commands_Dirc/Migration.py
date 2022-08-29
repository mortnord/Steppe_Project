from Static_Data import Static_Data


def create_next_areas():
    possible_areas = []
    for area in Static_Data.get_current_map().connections:
        possible_areas.append(Static_Data.get_map_with_regions()[area.nr_region])
    return possible_areas
