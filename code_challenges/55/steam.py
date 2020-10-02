from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    games = []
    steam = feedparser.parse(FEED_URL)
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    for i in range(len(steam['entries'])):
        game = Game(steam['entries'][i]['title'], steam['entries'][i]['link'])
        games.append(game)
    return games