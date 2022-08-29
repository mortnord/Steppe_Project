class Base_Equipment:
    def __init__(self):
        self.bonus_defend = 0
        self.bonus_attack = 0
        self.text = ""

    def usage(self, using_dwarf):
        pass

    def usage_card(self, using_card, using_dwarf):
        pass

    def usage_card_enemy(self, using_card, using_dwarf, using_enemy):
        pass
