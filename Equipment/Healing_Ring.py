import Enumerators
from Equipment.Base_Equipment.Base_Ring import Base_Ring


class Healing_Ring(Base_Ring):
    def __init__(self):
        super().__init__()
        self.text = "Heals 1 health at end of round"
        self.sprite = Enumerators.Equipment_Ring_Sprite.Healing_Ring.value

    def usage(self, using_dwarf):
        using_dwarf.health += 1
        if using_dwarf.health > using_dwarf.max_health:
            using_dwarf.health = using_dwarf.max_health
