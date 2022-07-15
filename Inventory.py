class Inventory():
    food_amount = 5
    temporary_food_amount = 0
    wood_amount = 0
    stone_amount = 0
    @classmethod
    def get_food_amount(cls):
        return cls.food_amount

    @classmethod
    def get_temporary_food_amount(cls):
        return cls.temporary_food_amount

    @classmethod
    def set_temporary_food_amount(cls, temporary_food_amount_input):
        cls.temporary_food_amount += temporary_food_amount_input

    @classmethod
    def set_food_amount(cls, food_input):
        cls.food_amount += food_input

    @classmethod
    def set_wood_amount(cls, wood_input):
        cls.wood_amount += wood_input

    @classmethod
    def get_wood_amount(cls):
        return cls.wood_amount

    @classmethod
    def get_stone_amount(cls):
        return cls.stone_amount

    @classmethod
    def set_stone_amount(cls, stone_input):
        cls.stone_amount += stone_input

    @classmethod
    def print_inventory(cls):
        print("You have " + str(cls.food_amount) + " food")
        print("You have " + str(cls.wood_amount) + " wood")