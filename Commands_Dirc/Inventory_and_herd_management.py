import math

import Background_Calculations
import Buildings
import Enumerators
import Turn_And_Background_Actions.turn_action
from Inventory import Inventory
from Static_Data import Static_Data
from Static_Data_Bools import Static_Data_Bools


def conserve_food(): #Her lager vi ost
    if Static_Data_Bools.get_Cheesery_bool(): #Først sjekker vi om spilleren har bygget ysteriet
        print(
            "Do you want to use an action to conserve temporary food (buckets of milk) into cheese? 3 buckets gives 1 "
            "cheese. Y/N")
        answer = input() #Vil spillere lage ost?
        if answer == "Y":
            Turn_And_Background_Actions.turn_action.take_Action() #Det tar tid å lage ost..
            buckets_conserved = math.floor((int(Inventory.get_temporary_food_amount()) / 3)) #For hver 3 bøtter med melk, så får vi en ost
            Inventory.set_food_amount(buckets_conserved) #Ost er mat vi kan ta med oss rundt, i motsetning til melk
            Inventory.set_temporary_food_amount(-(buckets_conserved * 3)) #Fjern temporary food, det er jo ost nå
        Inventory.print_inventory() #Skriv hva vi har nå
    else:
        print("You have no way to conserve the food") #Må ha ysteri...

def slaughter_sheep(sheep, number): #Her forventer vi inn saue-type, og hvor mange
    temp_list = []
    for x in range(len(Static_Data.get_list_of_sheeps())): #Her går vi igjennom alle sauene,
        if Static_Data.get_list_of_sheeps()[x].type_of_sheep == sheep: #Og velger sauer som matcher typen vi skal slakte
            temp_list.append(Static_Data.get_list_of_sheeps()[x])
            Inventory.set_food_amount(Static_Data.get_list_of_sheeps()[x].meat_amount) #Så får vi maten for slaktinga
            if len(temp_list) == number: #Når vi har slakta nok, så stopper vi
                break
    for x in range(len(temp_list)):
        Static_Data.get_list_of_sheeps().remove(temp_list[x]) #Her fjerner vi sauene fra lista over sauer vi har, de er jo døde


def slaughter_Sheep_choice(): #Her velger vi om vi skal slakte værer eller søyer
    print("Do you want to slaughter rams or ewes?")

    resource_to_gather = input()
    print("How many?")
    number = int(input())
    resource_to_gather = Background_Calculations.handle_input(resource_to_gather) #hvor mange vi skal slakte
    if resource_to_gather == "ram" or resource_to_gather == "rams": #værer
        slaughter_sheep(Enumerators.TypeOfSheep.Ram, number)
    elif resource_to_gather == "ewe" or resource_to_gather == "ewes": #søyer
        slaughter_sheep(Enumerators.TypeOfSheep.Ewe, number)


def look_over_sheeps(list_of_sheeps): #Her ser vi over flokken
    male_sheep = 0 #Først har vi null av alle
    female_sheep = 0
    male_lambs = 0
    female_lambs = 0
    for x in range(len(list_of_sheeps)): #Så teller vi over hele saueflokken
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Ram: #Værer
            male_sheep += 1 #hver vi teller legger vi til en i integeren over hvor mange vi har
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Ewe: #Søyer
            female_sheep += 1
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Male_Lamb: #Værlam
            male_lambs += 1
        if list_of_sheeps[x].type_of_sheep == Enumerators.TypeOfSheep.Female_Lamb: #Søylam
            female_lambs += 1

    print("You have " + str(male_sheep) + " rams") #Så skriver vi ut hvor mange vi har av hver

    print("You have " + str(female_sheep) + " ewes")

    print("You have " + str(male_lambs) + " young rams")

    print("You have " + str(female_lambs) + " young ewes")

    print("You have " + str(len(list_of_sheeps)) + " sheep in total")

    print("Do you want to slaughter some sheep? Y/N") #spørsmål vi vil slakte, vis spiller skriver Y, så slaktes det
    player_command = str(input())
    if player_command == "Y":
        slaughter_Sheep_choice()


def look_over_dwarfs_and_inventory(list_of_people): #Samme som sauetelling, bare over dverger
    for x in range(len(list_of_people)):
        print(str(list_of_people[x].ID) + " is ID ")
    Inventory.print_inventory()


def build_building(type_building): #Her bygger vi bygninger, vi forventer inn hva type bygning det er snakk om
    if Static_Data.get_max_amount_of_buildings() > Static_Data.get_current_amount_of_buildings(): #Først sjekker vi om vi har kapasitet til å bygge
        if Inventory.get_wood_amount() >= type_building.cost_to_build_wood and Inventory.get_stone_amount() >= type_building.cost_to_build_stone: #Så sjekker vi om vi har råd
            print("Built building") #så bygger vi bygning
            Inventory.buildings.append(type_building) #Legger den i lista over bygninger
            Inventory.set_wood_amount(-type_building.cost_to_build_wood) #og betaler for den
            Inventory.set_stone_amount((-type_building.cost_to_build_stone))
        else:
            print("Not enough resources")
    else:
        print("Not enough building slots")


def build_options(): #Her finner vi alternativer for å bygge
    print("What do you want to build? Options are")
    for type_building in Enumerators.TypeOfBuilding: #en litt alternativ for-loop, istedenfor X-, så bruker vi en attribut vi finner i Enumerators.TypeOfBuilding
                                                    #Da gjør vi det like mange ganger som det er oppføringer i den attributten
        print(type_building.value)
    building_choice = input() #her skriver vi ka bygning vi skal ha
    building_choice = Background_Calculations.handle_input(building_choice)
    if building_choice == "silo": #Her bygger vi den type bygninger vi vil ha
        build_building(Buildings.Silo())
    if building_choice == "wagon":
        build_building(Buildings.Wagon())
    if building_choice == "cheesery":
        build_building(Buildings.Cheesery())


def inventory_and_herd_management(): #Rygg-raden i denne sub-commanden. Vi bestemmer hva vi skal gjøre, basert på player input.
    print(
        "Press 1 to check the sheep herd, or 2 to check the inventory, press 3 to conserve food in inventory, press 4 to enter build option")
    player_command = str(input())
    if player_command == "1":
        look_over_sheeps(Static_Data.get_list_of_sheeps())
    elif player_command == "2":
        look_over_dwarfs_and_inventory(Static_Data.get_list_of_people())
    elif player_command == "3":
        conserve_food()
    elif player_command == "4":
        build_options()
