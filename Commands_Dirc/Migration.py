import Generation.Initial_Generation
from Static_Data import Static_Data


def create_next_areas():
    possible_areas = []

    for x in range(len(Static_Data.get_current_map().connections)):
        possible_areas.append(Static_Data.get_map_with_regions()[Static_Data.get_current_map().connections[x].nr_region])
    for x in range(len(Static_Data.get_map_with_regions())):

        for y in range(len(Static_Data.get_map_with_regions()[x].connections)):
            if Static_Data.get_map_with_regions()[x].connections[y].nr_region == Static_Data.get_current_map().landscape.Landscapes_ID:
                possible_areas.append(Static_Data.get_map_with_regions()[Static_Data.get_map_with_regions()[x].connections[y].nr_region])
                print("This area links back to this")
    for x in range(len(possible_areas)):
         if possible_areas[x].landscape.has_river:
             print("You can migrate to a " + possible_areas[x].landscape.type_of_landscape.name + " region with a river")
         else:
             print("You can migrate to a " + possible_areas[x].landscape.type_of_landscape.name + " region")
    print("Write 1 2 or 3 to migrate to that region")
    choice = input()
    if choice == "1":
         return possible_areas[0]
    elif choice == "2":
        return possible_areas[1]
    elif choice == "3":
        return possible_areas[2]