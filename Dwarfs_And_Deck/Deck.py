class Deck:
    def __init__(self): #Dette er en  klasse som inneholder informasjonen om korta
        self.content = [] #Innholdet i decket
        self.discard_pile = [] #Kaste-bunken
        self.hand_max_amount = 3 #initial-verdien på maks håndstørrelse
        self.hand = [] #hva som er i hånda
        self.one_time_used_cards = [] #eventuelle engangsbruk kort