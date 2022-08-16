import random

from Static_Data import Static_Data


def shuffle_deck():
    random.shuffle(Static_Data.get_deck_list().content)  # Stokker korta


def draw_cards_until_full(view):  # Her trekker vi kort til vi har fult

    while len(
            Static_Data.get_deck_list().hand) < Static_Data.get_deck_list().hand_max_amount:  # trekk så lenge vi ikke har full hånd
        draw_card()  # Trekk kort, sjekk implementatin for detaljer

    view.update_cards()


def draw_card():  # Trekk-kort-metoden..må kanskje legge til while-loopen fra draw_cards_until_full
    if len(Static_Data.get_deck_list().content) < 1:  # Vis kort-bunka er tom, så flytt alle korta tilbake fra discard-pilen til bunka (stokk kortene inn igjen)
        for x in range(len(Static_Data.get_deck_list().discard_pile)):
            Static_Data.get_deck_list().content.insert(0, Static_Data.get_deck_list().discard_pile.pop(0))
        shuffle_deck()
    Static_Data.get_deck_list().hand.append(
        Static_Data.get_deck_list().content.pop(0))  # Legg til første kort fra decket til hånda
    Static_Data.get_deck_list().hand_amount = len(
        Static_Data.get_deck_list().content)  # Oppdatert mengden kort vi har i hånda


def discard_hand():
    for x in range(len(Static_Data.get_deck_list().hand)):
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().hand[x])

    Static_Data.get_deck_list().hand.clear()

def reset_deck():  # Resetter alt tilbake til normalen
    discard_hand()
    while len(Static_Data.get_deck_list().one_time_used_cards) > 0:  # en gangskort tilbake til bunka
        Static_Data.get_deck_list().discard_pile.append(Static_Data.get_deck_list().one_time_used_cards.pop())
    while len(Static_Data.get_deck_list().discard_pile) > 0:
        Static_Data.get_deck_list().content.append(Static_Data.get_deck_list().discard_pile.pop())
    shuffle_deck()  # Stokk korta etter de er lagt inn
