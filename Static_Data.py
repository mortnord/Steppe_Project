import Commands_Dirc


class Static_Data():
    ID = 0
    Landscape_ID = 0
    Building_ID = 0
    Actions_Available = 0
    Amount_of_Grass_eating_per_action = 0
    list_of_people = []
    list_of_sheeps = []
    current_map = 0
    next_map = 0
    growing_time = 0
    max_amount_of_buildings = 0
    current_amount_of_buildings = 0
    deck_list = 0
    which_dwarf_to_attack = 0

    map_with_regions = []

    enemies_to_defeat = []

    window = 0

    @classmethod
    def set_window(cls, window_input):
        cls.window = window_input

    @classmethod
    def get_window(cls):
        return cls.window

    @classmethod
    def set_map_with_regions(cls, map_with_regions_input):
        cls.map_with_regions = map_with_regions_input

    @classmethod
    def get_map_with_regions(cls):
        return cls.map_with_regions

    @classmethod
    def reset_which_dwarf_to_attack(cls):
        cls.which_dwarf_to_attack = 0

    @classmethod
    def get_which_dwarf_to_attack(cls):
        return cls.which_dwarf_to_attack

    @classmethod
    def set_which_dwarf_to_attack(cls, input):
        cls.which_dwarf_to_attack += input

    @classmethod
    def get_enemies_to_defeat(cls):
        return cls.enemies_to_defeat

    @classmethod
    def set_enemies_to_defeat(cls, enemies_to_defeat_input):
        cls.enemies_to_defeat = enemies_to_defeat_input
    @classmethod
    def get_deck_list(cls):
        return cls.deck_list

    @classmethod
    def set_deck_list(cls, deck_list_input):
        cls.deck_list = deck_list_input

    @classmethod
    def get_ID(cls):
        cls.ID += 1
        return cls.ID

    @classmethod
    def get_Landscape_ID(cls):
        cls.Landscape_ID += 1
        return cls.Landscape_ID-1

    @classmethod
    def get_Building_ID(cls):
        cls.Building_ID += 1
        return cls.Building_ID

    @classmethod
    def get_Actions_Available(cls):
        return cls.Actions_Available

    @classmethod
    def set_Actions_Available(cls, actions_Available_input):
        cls.Actions_Available = actions_Available_input

    @classmethod
    def use_Actions_available(cls, amount_usage):
        cls.Actions_Available -= amount_usage

    @classmethod
    def set_Amount_of_Grass_eating_per_action(cls, Amount_of_Grass_eating_per_action_input):
        cls.Amount_of_Grass_eating_per_action = Amount_of_Grass_eating_per_action_input

    @classmethod
    def get_Amount_of_Grass_eating_per_action(cls):
        return cls.Amount_of_Grass_eating_per_action

    @classmethod
    def get_list_of_people(cls):
        return cls.list_of_people

    @classmethod
    def set_list_of_people(cls, list_of_people_input):
        cls.list_of_people = list_of_people_input

    @classmethod
    def get_list_of_sheeps(cls):
        return cls.list_of_sheeps

    @classmethod
    def set_list_of_sheeps(cls, list_of_sheeps_input):
        cls.list_of_sheeps = list_of_sheeps_input

    @classmethod
    def set_current_map(cls, current_map_input):
        cls.current_map = current_map_input

    @classmethod
    def get_current_map(cls):
        return cls.current_map

    @classmethod
    def set_next_map(cls, next_map_input):
        cls.next_map = next_map_input

    @classmethod
    def get_next_map(cls):
        return cls.next_map

    @classmethod
    def get_growing_time(cls):
        return cls.growing_time

    @classmethod
    def set_growing_time(cls, growing_time_input):
        cls.growing_time += growing_time_input

    @classmethod
    def set_max_amount_of_buildings(cls, max_amount_of_buildings_input):
        cls.max_amount_of_buildings = max_amount_of_buildings_input

    @classmethod
    def get_max_amount_of_buildings(cls):
        return cls.max_amount_of_buildings

    @classmethod
    def set_current_amount_of_buildings(cls, current_amount_of_buildings_input):
        cls.current_amount_of_buildings += current_amount_of_buildings_input

    @classmethod
    def get_current_amount_of_buildings(cls):
        return cls.current_amount_of_buildings