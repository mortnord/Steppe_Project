import random

import Enumerators
from Dwarfs_And_Deck import Sheeps
from Static_Data import Static_Data


def grow_and_handle_sheep():  # Komplisert metode som får sau til å formere seg og vokse
    for sheep in Static_Data.get_list_of_sheeps():  # først, alle eksisterende lam blir 1 år gamle.
        if sheep.type_of_sheep == Enumerators.TypeOfSheep.Male_Lamb or \
                sheep.type_of_sheep == Enumerators.TypeOfSheep.Female_Lamb:
            sheep.age += 1
    for sheep in Static_Data.get_list_of_sheeps():  # så, får man enten ett værlam eller ett saulam per søya. Kanskje
        # burde fått mellom 1-3?
        if sheep.type_of_sheep == Enumerators.TypeOfSheep.Ewe:
            lamb = random.randint(1, 2)
            if lamb == 1:
                Static_Data.get_list_of_sheeps().append(Sheeps.SheepMaleLamb())
            if lamb == 2:
                Static_Data.get_list_of_sheeps().append(Sheeps.SheepFemaleLamb())
    for x, sheep in enumerate(Static_Data.get_list_of_sheeps()):  # så, alle lammene som er 1 år eller eldre blir
        # erstattet med en voksen sau
        if sheep.type_of_sheep == Enumerators.TypeOfSheep.Male_Lamb:
            if sheep.age >= 1:
                Static_Data.get_list_of_sheeps()[x] = Sheeps.SheepMale()

        if sheep.type_of_sheep == Enumerators.TypeOfSheep.Female_Lamb:
            if sheep.age >= 1:
                Static_Data.get_list_of_sheeps()[x] = Sheeps.SheepFemale()
