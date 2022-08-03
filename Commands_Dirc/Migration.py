import Generation.Initial_Generation
from Static_Data import Static_Data


def create_next_areas():
    possible_areas = []  # Mulige områder vi kan migrere til

    for x in range(
            len(Static_Data.get_current_map().connections)):  # Vi legger til alle områdene som vi har en connection til
        possible_areas.append(
            Static_Data.get_map_with_regions()[Static_Data.get_current_map().connections[x].nr_region])

    for x in range(len(possible_areas)): #Her skriver vi ut hva områder vi kan migrere til
        if possible_areas[x].landscape.has_river:
            print("You can migrate to a " + possible_areas[x].landscape.type_of_landscape.name + " region with a river")
        else:
            print("You can migrate to a " + possible_areas[x].landscape.type_of_landscape.name + " region")
    print("Write 1 2 or 3 to migrate to that region")
    choice = input() #Her velger vi, enn så leng kun velge 1 2 eller 3, kanskje finne en alternativ måte å løse det på?
    if choice == "1":
        return possible_areas[0]
    elif choice == "2":
        return possible_areas[1]
    elif choice == "3":
        return possible_areas[2]
