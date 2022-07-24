import Enumerators

from Cards.Base_Cards import Card

class Defend(Card):
    def __init__(self):

        super().__init__()
        self.value = 2
        self.type_of_card = Enumerators.TypeOfCard.Defend