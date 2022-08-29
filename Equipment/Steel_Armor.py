import Enumerators
from Equipment.Base_Equipment.Base_Armor import Base_Armor


class Steel_Armor(Base_Armor):
    def __init__(self):
        super().__init__()
        self.bonus_defend = 1
        self.sprite = Enumerators.Equipment_Armor_Sprite.Steel_Armor.value
        self.text = ""
