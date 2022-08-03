class Card:
    def __init__(self): #Base-verdier for alle kort.
        self.value = 0  #Skade/healing/defend whatever
        self.type_of_card = 0
        self.dwarfs_required = 0
        self.one_time = False #Kan brukes som flag senere for å indikere att kortet er one-time-use per kamp

    def print_text(self):
        print("This is an " + self.type_of_card.value + " card with " + str(self.value) + " value, and this costs " + str(self.dwarfs_required) + " dwarfs")
