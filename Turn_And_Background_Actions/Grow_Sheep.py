import random

import Enumerators
import Sheeps
from Static_Data import Static_Data


def grow_and_handle_sheep():
    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Male_Lamb or \
                Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Female_Lamb:
            Static_Data.get_list_of_sheeps()[x].age += 1
    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Ewe:
            lamb = random.randint(1, 2)
            if lamb == 1:
                Static_Data.get_list_of_sheeps().append(Sheeps.SheepMaleLamb())
            if lamb == 2:
                Static_Data.get_list_of_sheeps().append(Sheeps.SheepFemaleLamb())
    for x in range(len(Static_Data.get_list_of_sheeps())):
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Male_Lamb:
            if Static_Data.get_list_of_sheeps()[x].age >= 1:
                Static_Data.get_list_of_sheeps()[x] = Sheeps.SheepMale()

        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == Enumerators.TypeOfSheep.Female_Lamb:
            if Static_Data.get_list_of_sheeps()[x].age >= 1:
                Static_Data.get_list_of_sheeps()[x] = Sheeps.SheepFemale()
