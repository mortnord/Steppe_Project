import Enumerators
from Equipment.Base_Equipment.Base_Weapon import Base_Weapon


class Steel_Axe(Base_Weapon):
    def __init__(self):
        super().__init__()
        self.bonus_attack = 1
        self.sprite = Enumerators.Equipment_Weapon_Sprite.Steel_Axe.value
        self.text = ""
