class Card:
    def __init__(self):
        self.value = 0
        self.type_of_card = 0

    def usage(self):
        return self.value, self.type_of_card

    def print_text(self):
        print("This is an " + self.type_of_card.value + " card with " + str(self.value) + " value")