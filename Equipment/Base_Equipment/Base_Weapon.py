import Enumerators
from Equipment.Base_Equipment.Base_Equipment import Base_Equipment


class Base_Weapon(Base_Equipment):
    def __init__(self):
        super().__init__()
        self.sprite = Enumerators.Base_Equipment.Base_Weapon.value
        self.type = Enumerators.Equipment_types.Weapon
        self.text = "Does nothing"
