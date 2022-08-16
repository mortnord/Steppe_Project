import Enumerators
from Static_Data import Static_Data
from Equipment import Base_Armor, Base_Weapon, Base_Ring, Base_Cloak


class Dwarf:  # En dverg
    ID = None

    def __init__(self):
        self.eat_amount = float(1)  # Hvor mye mat dvergen trenger
        self.ID = Static_Data.get_ID()  # auto-generert ID
        self.max_health = 10
        self.health = 10  # initial-verdi liv
        self.defend = 0  # mengden armor
        self.sprite = Enumerators.Sprites.Dwarf.value
        self.has_energy = True
        self.amount_energy = 1
        self.max_energy = 1
        self.armor = Base_Armor.Base_Armor()
        self.weapon = Base_Weapon.Base_Weapon()
        self.ring = Base_Ring.Base_Ring()
        self.cloak = Base_Cloak.Base_Cloak()
        self.bonus_defend = 0
        self.bonus_attack = 0

    def take_damage(self, value_damage):  # Denne metoden kalles når vi tar skade
        print(self.defend)
        if self.defend > 0:  # Vis vi har armor, ta først og mist armor.
            self.defend = self.defend - value_damage
            if self.defend < 0:  # Vis vi er på negativ armor (f.eks hadde 3 armor, og tok 4 skade), så mist liv for å komme i null.
                self.health += self.defend
                self.defend = 0
        else:  # Ingen armor, = bare skade
            self.health -= value_damage

    def use_energy(self, value_energy):
        self.amount_energy -= value_energy
        if self.amount_energy == 0:
            return False
        else:
            return True

    def calculate_bonus_damage(self):
        self.bonus_attack = self.ring.bonus_attack + self.armor.bonus_attack + self.weapon.bonus_attack + self.cloak.bonus_attack
        self.bonus_defend = self.ring.bonus_defend + self.armor.bonus_defend + self.weapon.bonus_defend + self.cloak.bonus_defend
