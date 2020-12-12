#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
from operator import itemgetter

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def _similarity(wine: str, cheese: str) -> float:
    '''Return a similarity value for given names of wine and cheese.'''
    w = Counter(wine.lower())
    c = Counter(cheese.lower())
    wc = sum((w & c).values())
    return wc / (1 + pow(len(wine) - len(cheese), 2))


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    if wine_type not in ['all', 'red', 'white', 'sparkling']:
        raise ValueError

    if wine_type == 'all':
        wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
    elif wine_type == 'red':
        wines = RED_WINES
    elif wine_type == 'white':
        wines = WHITE_WINES
    else:  # wine_type = 'sparkling'
        wines = SPARKLING_WINES

    max_score = 0
    pairing = tuple()
    for wine in wines:
        for cheese in CHEESES:
            score = _similarity(wine, cheese)
            if score > max_score:
                pairing = (wine, cheese, score)
                max_score = score

    return pairing


def match_wine_5cheeses():
    """pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically
    ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel',
        ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    pairings = []
    wines = sorted(RED_WINES + WHITE_WINES + SPARKLING_WINES)
    for wine in wines:
        top_5 = []
        for cheese in CHEESES:
            top_5.append((cheese, _similarity(wine, cheese)))
        top_5 = sorted(top_5, key=itemgetter(0))
        top_5 = sorted(top_5, key=itemgetter(1), reverse=True)
        top_5 = [x[0] for x in top_5[:5]]
        pairings.append((wine, top_5))
    return pairings
