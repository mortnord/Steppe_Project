from Equipment.Base_Equipment.Base_Ring import Base_Ring


class Healing_Ring(Base_Ring):
    def usage(self, using_dwarf):
        using_dwarf.health += 1
        if using_dwarf.health > using_dwarf.max_health:
            using_dwarf.health = using_dwarf.max_health
