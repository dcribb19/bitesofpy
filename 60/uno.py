from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')
twos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Draw Two', 'Skip', 'Reverse'] 

def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    wilds = [UnoCard(None, 'Wild') for x in range(4)]
    wild_d4s = [UnoCard(None, 'Wild Draw Four') for x in range(4)]
    zeros = [UnoCard(suit=suit, name='0') for suit in SUITS]
    base_deck = [UnoCard(suit=suit, name=card) for suit in SUITS for card in twos] * 2
    deck = base_deck + zeros + wilds + wild_d4s
    return deck
