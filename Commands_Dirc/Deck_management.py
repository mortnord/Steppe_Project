import random

from Static_Data import Static_Data


def print_deck():
    shuffle_deck()
    for x in range(Static_Data.get_deck_list().deck_amount):
        Static_Data.get_deck_list().content[x].print_text()

def shuffle_deck():
    random.shuffle(Static_Data.get_deck_list().content)