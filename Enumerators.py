from enum import Enum

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