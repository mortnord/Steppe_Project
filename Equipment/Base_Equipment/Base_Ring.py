import Enumerators
from Equipment.Base_Equipment.Base_Equipment import Base_Equipment


class Base_Ring(Base_Equipment):
    def __init__(self):
        super().__init__()
        self.sprite = Enumerators.Base_Equipment.Base_Ring.value
        self.type = Enumerators.Equipment_types.Ring
        self.text = "Does nothing"
