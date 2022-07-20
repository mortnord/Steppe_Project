class Static_Data_Bools:
    Silo = False
    Wagon = False
    Cheesery = False
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