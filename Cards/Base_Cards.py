import Enumerators


class Card:
    def __init__(self): #Base-verdier for alle kort.
        self.value = 0  #Skade/healing/defend whatever
        self.type_of_card = 0
        self.dwarfs_required = 0
        self.one_time = False #Kan brukes som flag senere for å indikere att kortet er one-time-use per kamp
        self.sprite = Enumerators.Sprites.Card.value
        self.indicator_sprite = None

    def usage_card_equipment(self, using_card, using_dwarf):
        using_dwarf.cloak.usage_card(using_card, using_dwarf)
        using_dwarf.armor.usage_card(using_card, using_dwarf)
        using_dwarf.weapon.usage_card(using_card, using_dwarf)
        using_dwarf.ring.usage_card(using_card, using_dwarf)
