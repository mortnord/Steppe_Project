class Static_Data_Bools:
    Silo = False

    @classmethod
    def set_Silo_bool(cls, input):
        cls.Silo = input

    @classmethod
    def get_Silo_bool(cls):
        return cls.Silo