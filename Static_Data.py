import Commands


class Static_Data():
    ID = 0
    Landscape_ID = 0
    Actions_Available = 0
    Amount_of_Grass_eating_per_action = 0
    list_of_people = []
    list_of_sheeps = []
    current_map = 0

    @classmethod
    def get_ID(cls):
        cls.ID += 1
        return cls.ID

    @classmethod
    def get_Landscape_ID(cls):
        cls.Landscape_ID += 1
        return cls.Landscape_ID

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

