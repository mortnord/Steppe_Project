class Static_Data_Bools:
    Took_reward = False
    Silo = False
    Wagon = False
    Cheesery = False
    Reward = False
    Combat = False

    @classmethod
    def set_combat(cls, input):
        cls.Combat = input

    @classmethod
    def get_combat(cls):
        return cls.Combat

    @classmethod
    def set_Silo_bool(cls, input):
        cls.Silo = input

    @classmethod
    def get_Silo_bool(cls):
        return cls.Silo

    @classmethod
    def set_Wagon_bool(cls, input):
        cls.Wagon = input

    @classmethod
    def get_Wagon_bool(cls):
        return cls.Wagon


    @classmethod
    def set_Cheesery_bool(cls, input):
        cls.Cheesery = input

    @classmethod
    def get_Cheesery_bool(cls):
        return cls.Cheesery

    @classmethod
    def set_reward(cls, input):
        cls.Reward = input

    @classmethod
    def get_reward(cls):
        return cls.Reward

    @classmethod
    def get_took_reward(cls):
        return cls.Took_reward

    @classmethod
    def set_took_reward(cls, input):
        cls.Took_reward = input