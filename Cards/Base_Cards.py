import Enumerators


class Card:
    def __init__(self):  # Base-verdier for alle kort.
        self.type_of_card = None
        self.energy_required = None
        self.type_of_card_general = None
        self.text = ""
        self.one_time = False  # Kan brukes som flag senere for å indikere att kortet er one-time-use per kamp
        self.sprite = Enumerators.Sprites.Card.value
        self.indicator_sprite = None
        self.indicator_sprite_secondary = None

    def usage_card_equipment(self, using_card, using_dwarf):
        using_dwarf.cloak.usage_card(using_card, using_dwarf)
        using_dwarf.armor.usage_card(using_card, using_dwarf)
        using_dwarf.weapon.usage_card(using_card, using_dwarf)
        using_dwarf.ring.usage_card(using_card, using_dwarf)

    def usage_card_enemy(self, using_card, using_dwarf, using_enemy):
        using_dwarf.cloak.usage_card_enemy(using_card, using_dwarf, using_enemy)
        using_dwarf.armor.usage_card_enemy(using_card, using_dwarf, using_enemy)
        using_dwarf.weapon.usage_card_enemy(using_card, using_dwarf, using_enemy)
        using_dwarf.ring.usage_card_enemy(using_card, using_dwarf, using_enemy)
