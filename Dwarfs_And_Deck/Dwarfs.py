import Enumerators
from Static_Data import Static_Data


class Dwarf:  # En dverg
    ID = None

    def __init__(self):
        self.eat_amount = float(1)  # Hvor mye mat dvergen trenger
        self.ID = Static_Data.get_ID()  # auto-generert ID
        self.health = 10  # initial-verdi liv
        self.defend = 0  # mengden armor
        self.sprite = Enumerators.Sprites.Dwarf.value
        self.has_energy = True
        self.amount_energy = 1
        self.max_energy = 1

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
