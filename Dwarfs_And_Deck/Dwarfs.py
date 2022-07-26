from Static_Data import Static_Data


class Dwarf:
    ID = None

    def __init__(self):
        self.eat_amount = float(1)
        self.ID = Static_Data.get_ID()
        self.health = 10
        self.defend = 0

    def take_damage(self, value_damage):
        print(self.defend)
        if self.defend > 0:
            self.defend = self.defend - value_damage
            if self.defend < 0:
                self.health -= self.defend
                self.defend = 0
        else:
            self.health -= value_damage
