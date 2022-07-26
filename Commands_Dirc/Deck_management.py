import random

from Static_Data import Static_Data


def print_deck():
    print((str(len(Static_Data.get_deck_list().content))) + " cards in deck")

    print("Your hand is")

    for x in range(len(Static_Data.get_deck_list().hand)):
        Static_Data.get_deck_list().hand[x].print_text()


def shuffle_deck():
    random.shuffle(Static_Data.get_deck_list().content)


def draw_cards_until_full():
    while len(Static_Data.get_deck_list().hand) < Static_Data.get_deck_list().hand_max_amount:
        if len(Static_Data.get_deck_list().content) == 0:
            while len(Static_Data.get_deck_list().discard_pile) > 0:
                Static_Data.get_deck_list().content.append(Static_Data.get_deck_list().discard_pile.pop())
            shuffle_deck()
        draw_card()


def draw_card():
    Static_Data.get_deck_list().hand.append(Static_Data.get_deck_list().content.pop(0))
    Static_Data.get_deck_list().hand_amount = len(Static_Data.get_deck_list().content)


def discard_hand():
    while len(Static_Data.get_deck_list().hand) > 0:
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand.pop())
