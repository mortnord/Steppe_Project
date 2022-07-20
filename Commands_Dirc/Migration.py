import Generation.Initial_Generation


def create_next_areas():
    possible_areas = []
    for x in range(3):
        possible_areas.append(Generation.Initial_Generation.next_map_generation())
    for x in range(len(possible_areas)):
        if possible_areas[x].has_river:
            print("You can migrate to a " + possible_areas[x].type_of_landscape.name + " region with a river")
        else:
            print("You can migrate to a " + possible_areas[x].type_of_landscape.name + " region")
    print("Write 1 2 or 3 to migrate to that region")
    choice = input()
    if choice == "1":
        return possible_areas[0]
    elif choice == "2":
        return possible_areas[1]
    elif choice == "3":
        return possible_areas[2]