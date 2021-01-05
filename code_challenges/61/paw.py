from collections import namedtuple
import random
from string import ascii_uppercase
from typing import List

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')


def create_paw_deck(n: int = 8):
    if n > 26:
        raise ValueError('n is out of range')

    # letter range
    letters = ascii_uppercase[:n]
    # build deck
    cards = [letter + str(number) for letter in letters for number in NUMBERS]
    # random sample to assign actions
    rand_act_cards = random.sample(cards, n)
    # remaining cards not in sample
    no_act_cards = set(cards) - set(rand_act_cards)

    deck: List[PawCard] = []

    for card in rand_act_cards:
        # assign random action to sample
        deck.append(PawCard(card, random.choice(ACTIONS)))

    for card in no_act_cards:
        deck.append(PawCard(card, None))

    return deck
