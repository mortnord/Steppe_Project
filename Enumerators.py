from enum import Enum

#Enumeratorer er en egen definert variabel, som man kan bruke for å sammenligne og sjekke ting, f.eks at TypeOfSheep = Ram osv.
import Enemies.Goblins


class TypeOfSheep(Enum):
    Ram = "Ram"
    Ewe = "Ewe"
    Male_Lamb = "Male lamb"
    Female_Lamb = "Female Lamb"

class Landscapes(Enum):
    Steppes = "Steppes"
    Wooded = "Wooded"
    Hills = "Hills"
    Rocky = "Rocky"
    City = "City"

class TypeOfBuilding(Enum):
    Silo = "Silo"
    Wagon = "Wagon"
    Cheesery = "Cheesery"

class TypeOfCard(Enum):
    Attack = "Attack"
    Defend = "Defend"
    Attack_and_defend = "Attack and defend"
    Quick_Attack = "Quick Attack"
    Heavy_Attack = "Heavy Attack"
    Healing = "Healing"

class TypeOfPlannedAttack(Enum):
    Attack = "Attack"
    Defend = "Defend"
    Healing = "Healing"

class Sprites_of_planned_attack(Enum):
    Attack = "Assets/sword.png"
    Defend = "Assets/shield.png"
    Healing = "Assets/healing.png"

class Sprites(Enum):
    Card = "Assets/card.png"

    Dwarf = "Assets/dwarf.png"

    Goblin = "Assets/Goblin.png"
    Slime = "Assets/Slime.png"

    Energy = "Assets/energy.png"

class Monsters(Enum):
    Goblin = "Goblin"
    Slime = "Slime"