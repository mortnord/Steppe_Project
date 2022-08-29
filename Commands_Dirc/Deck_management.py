import random

from Static_Data import Static_Data


def shuffle_deck():
    random.shuffle(Static_Data.get_deck_list().content)  # Stokker korta


def draw_cards_until_full(view):  # Her trekker vi kort til vi har fult

    while len(
            Static_Data.get_deck_list().hand) < Static_Data.get_deck_list().hand_max_amount:  # trekk så lenge vi
        # ikke har full hånd
        draw_card()  # Trekk kort, sjekk implementatin for detaljer

    view.update_cards()


def draw_card():  # Trekk-kort-metoden..må kanskje legge til while-loopen fra draw_cards_until_full
    if not Static_Data.get_deck_list().content:  # Vis kort-bunka er tom, så flytt alle korta tilbake fra
        # discard-pilen til bunka (stokk kortene inn igjen)

        for card in Static_Data.get_deck_list().discard_pile:
            Static_Data.get_deck_list().content.insert(0, card)
        Static_Data.get_deck_list().discard_pile.clear()
        shuffle_deck()
    Static_Data.get_deck_list().hand.append(
        Static_Data.get_deck_list().content.pop(0))  # Legg til første kort fra decket til hånda


def discard_hand():
    for card in Static_Data.get_deck_list().hand:
        Static_Data.get_deck_list().discard_pile.append(card)
    Static_Data.get_deck_list().hand.clear()


def reset_deck():  # Resetter alt tilbake til normalen
    discard_hand()
    while Static_Data.get_deck_list().one_time_used_cards:  # en gangskort tilbake til bunka
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().one_time_used_cards.pop())
    while Static_Data.get_deck_list().discard_pile:
        Static_Data.get_deck_list().content.append(Static_Data.get_deck_list().discard_pile.pop())
    shuffle_deck()  # Stokk korta etter de er lagt inn
