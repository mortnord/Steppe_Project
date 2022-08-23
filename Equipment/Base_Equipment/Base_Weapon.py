import Enumerators
from Equipment.Base_Equipment.Base_Equipment import Base_Equipment


class Base_Weapon(Base_Equipment):
    sprite = Enumerators.Base_Equipment.Base_Weapon.value
    type = Enumerators.Equipment_types.Weapon