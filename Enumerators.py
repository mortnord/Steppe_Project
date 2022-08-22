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


class Landscapes_sprites(Enum):
    Steppes = "Assets/Landscape_Sprites/grass_tile.png"
    Wooded = "Assets/Landscape_Sprites/forest_tile.png"
    Hills = "Assets/Landscape_Sprites/stone.png"


class TypeOfBuilding(Enum):
    Silo = "Silo"
    Wagon = "Wagon"
    Cheesery = "Cheesery"


class TypeOfCard(Enum):
    Attack = "Attack"
    Defend = "Defend"
    Quick_Attack = "Quick Attack"
    Heavy_Attack = "Heavy Attack"
    Healing = "Healing"


class TypeOfPlannedAttack(Enum):
    Attack = "Attack"
    Defend = "Defend"
    Healing = "Healing"


class Sprites_Of_Planned_Attack(Enum):
    Attack = "Assets/sword.png"
    Defend = "Assets/shield.png"
    Healing = "Assets/healing.png"


class Sprites(Enum):
    Card = "Assets/card.png"

    Dwarf = "Assets/Animals_Dwarfs_And_Monsters/dwarf.png"
    Active_Dwarf_Pointer = "Assets/red_arrow_down.png"
    Goblin = "Assets/Animals_Dwarfs_And_Monsters/Goblin.png"
    Slime = "Assets/Animals_Dwarfs_And_Monsters/Slime.png"
    Demon = "Assets/Animals_Dwarfs_And_Monsters/Demon.png"

    Energy = "Assets/energy.png"
    End_Turn = "Assets/End_Turn.png"

    Milk = "Assets/milk.png"
    Meat = "Assets/meat.png"

    Lamb = "Assets/Animals_Dwarfs_And_Monsters/lam.png"
    Sheep = "Assets/Animals_Dwarfs_And_Monsters/Gammalnorskspel.png"

class Monsters(Enum):
    Goblin = "Goblin"
    Slime = "Slime"
    Demon = "Demon"


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

class Button_Sprites(Enum):
    Harvest_Grass = "Assets/UI/Harvest_Buttons/Harvest_Button_Grass.png"
    Harvest_Wood = "Assets/UI/Harvest_Buttons/Harvest_Button_Wood.png"
    Harvest_Stone = "Assets/UI/Harvest_Buttons/Harvest_Button_Stone.png"
    Harvest_Fish = "Assets/UI/Harvest_Buttons/Harvest_Button_Fish.png"
    Pass = "Assets/UI/Harvest_Buttons/pass.png"
    Deck_UI = "Assets/UI/deck.png"
    Back = "Assets/UI/back.png"