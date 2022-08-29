import Enumerators
from Equipment.Base_Equipment.Base_Equipment import Base_Equipment


class Base_Cloak(Base_Equipment):
    def __init__(self):
        super().__init__()
        self.sprite = Enumerators.Base_Equipment.Base_Cloak.value
        self.type = Enumerators.Equipment_types.Cloak
        self.text = "Does nothing"
