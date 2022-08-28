import math

import Background_Calculations
import Enumerators
import Turn_And_Background_Actions.turn_action
from Inventory import Inventory
from Static_Data import Static_Data


def conserve_food():  # Her lager vi ost

    buckets_conserved = math.floor(
        (int(Inventory.get_temporary_food_amount()) / 3))  # For hver 3 bøtter med melk, så får vi en ost
    if buckets_conserved > 0:
        Inventory.set_food_amount(buckets_conserved)  # Ost er mat vi kan ta med oss rundt, i motsetning til melk
        Inventory.set_temporary_food_amount(-(buckets_conserved * 3))  # Fjern temporary food, det er jo ost nå
        Turn_And_Background_Actions.turn_action.take_Action()  # Det tar tid å lage ost..


# TODO Re-implementer cheesey for å lage ost

def slaughter_sheep(sheep, number):  # Her forventer vi inn saue-type, og hvor mange
    temp_list = []
    for x in range(len(Static_Data.get_list_of_sheeps())):  # Her går vi igjennom alle sauene,
        if Static_Data.get_list_of_sheeps()[
            x].type_of_sheep == sheep:  # Og velger sauer som matcher typen vi skal slakte
            temp_list.append(Static_Data.get_list_of_sheeps()[x])
            Inventory.set_food_amount(Static_Data.get_list_of_sheeps()[x].meat_amount)  # Så får vi maten for slaktinga
            if len(temp_list) == number:  # Når vi har slakta nok, så stopper vi
                break
    for x in range(len(temp_list)):
        Static_Data.get_list_of_sheeps().remove(
            temp_list[x])  # Her fjerner vi sauene fra lista over sauer vi har, de er jo døde
    Background_Calculations.background_info()


def look_over_sheeps(list_of_sheeps):  # Her ser vi over flokken
    male_sheep = 0  # Først har vi null av alle
    female_sheep = 0
    male_lambs = 0
    female_lambs = 0
    for x in range(len(list_of_sheeps)):  # Så teller vi over hele saueflokken
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Ram:  # Værer
            male_sheep += 1  # hver vi teller legger vi til en i integeren over hvor mange vi har
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Ewe:  # Søyer
            female_sheep += 1
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Male_Lamb:  # Værlam
            male_lambs += 1
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Female_Lamb:  # Søylam
            female_lambs += 1
    type_of_sheeps = [male_sheep, female_sheep, male_lambs, female_lambs]
    return type_of_sheeps


