import Enumerators
from Equipment.Base_Equipment.Base_Weapon import Base_Weapon
from Debuffs import Bleed_Debuff
from Static_Data import Static_Data


class Spear(Base_Weapon):
    def __init__(self):
        super().__init__()
        self.sprite = Enumerators.Equipment_Weapon_Sprite.Spear.value
        self.text = "A Basic Spear, bleeds for 1 over 2 turns each hit"

    def usage_card_enemy(self, using_card, using_dwarf, using_enemy):
        Static_Data.get_enemies_to_defeat()[using_enemy].debuff_list.append(Bleed_Debuff.Bleed(1, 2))  # Strength of bleed, rounds
