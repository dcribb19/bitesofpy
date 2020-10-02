from collections import Counter, defaultdict
import csv

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """
    Receives loaded csv content (str) and returns a dict of
    keys=characters and values=Counter object,
    which is a mapping of episode=>words spoken
    """
    csv_reader = csv.reader(content.split('\n'), delimiter=',')
    headers = next(csv_reader)
    num_words = defaultdict(Counter)
    for row in csv_reader:
        if not row:
            continue
        episode = row[1]
        character = row[2]
        words = len(row[3].split())
        num_words[character].update(Counter({episode: words}))
    return num_words
