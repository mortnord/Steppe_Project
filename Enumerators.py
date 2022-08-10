from enum import Enum

# Enumeratorer er en egen definert variabel, som man kan bruke for å sammenligne og sjekke ting, f.eks at TypeOfSheep = Ram osv.
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
    Active_Dwarf_Pointer = "Assets/red_arrow_down.png"
    Goblin = "Assets/Goblin.png"
    Slime = "Assets/Slime.png"

    Energy = "Assets/energy.png"
    End_Turn = "Assets/End_Turn.png"


class Monsters(Enum):
    Goblin = "Goblin"
    Slime = "Slime"


class Numbers(Enum):
    Zero = "Assets/Numbers/Number-0-0.png"
    One = "Assets/Numbers/Number-1-0.png"
    Two = "Assets/Numbers/Number-2-0.png"
    Three = "Assets/Numbers/Number-3-0.png"
    Four = "Assets/Numbers/Number-4-0.png"
    Five = "Assets/Numbers/Number-5-0.png"
    Six = "Assets/Numbers/Number-6-0.png"
    Seven = "Assets/Numbers/Number-7-0.png"
    Eight = "Assets/Numbers/Number-8-0.png"
    Nine = "Assets/Numbers/Number-9-0.png"
