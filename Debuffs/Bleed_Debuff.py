from Debuffs.Base_Debuffs import Base_Debuff


class Bleed(Base_Debuff):
    def __init__(self, strength_of_bleed, rounds_remaining):
        super().__init__()
        self.rounds_remaining = rounds_remaining
        self.strength = strength_of_bleed

    def usage(self, target):
        target.health -= self.strength
        self.rounds_remaining -= 1
        if not self.rounds_remaining:
            self.active = False
        print(self.active)