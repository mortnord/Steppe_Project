def print_buildings():
    if len(Inventory.get_buildings()) > 0:
        for x in range(len(Inventory.get_buildings())):
            print(Inventory.get_buildings()[x].type_of_building.value)

#Get/Set-metoder for inventory, henter og legger in data.
class Inventory:
    grass_amount = 0
    max_grass_amount = 0
    food_amount = 5
    max_food_amount = 0
    temporary_food_amount = 0
    wood_amount = 0
    max_wood_amount = 0
    stone_amount = 0
    max_stone_amount = 0
    buildings = []

    @classmethod
    def get_grass_amount(cls):
        return cls.grass_amount

    @classmethod
    def set_grass_amount(cls, grass_amount_input):
        cls.grass_amount += grass_amount_input

    @classmethod
    def get_max_grass_amount(cls):
        return cls.max_grass_amount

    @classmethod
    def set_max_grass_amount(cls, max_grass_amount_input):
        cls.max_grass_amount = max_grass_amount_input

    @classmethod
    def get_max_food_amount(cls):
        return cls.max_food_amount

    @classmethod
    def set_max_food_amount(cls, max_food_amount_input):
        cls.max_food_amount = max_food_amount_input

    @classmethod
    def get_max_stone_amount(cls):
        return cls.max_stone_amount

    @classmethod
    def set_max_stone_amount(cls, max_stone_amount_input):
        cls.max_stone_amount = max_stone_amount_input

    @classmethod
    def get_max_wood_amount(cls):
        return cls.max_wood_amount

    @classmethod
    def set_max_wood_amount(cls, max_wood_amount_input):
        cls.max_wood_amount = max_wood_amount_input

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
    def set_buildings(cls, buildings_input):
        cls.buildings.append(buildings_input)

    @classmethod
    def get_buildings(cls):
        return cls.buildings

    @classmethod
    def print_inventory(cls):
        print("You have " + str(cls.grass_amount) + " grass out of " + str(cls.max_grass_amount) + " in storage capacity")
        print("You have " + str(cls.food_amount) + " food out of " + str(cls.max_food_amount) +" in storage capacity")
        print("You have " + str(cls.wood_amount) + " wood out of " + str(cls.max_wood_amount) +" in storage capacity")
        print("You have " + str(cls.stone_amount) + " stone out of " + str(cls.max_stone_amount) +" in storage capacity")
        print("You have " + str(cls.temporary_food_amount) + " buckets of milk")
        print(print_buildings())
