from audioop import avg
from collections import namedtuple
import csv
import os
from pathlib import Path
import sqlite3
import random
import string

import requests

DATA_URL = 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
TMP = Path(os.getenv("TMP", "/tmp"))

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = TMP / f'nba_{salt}.db'

Player = namedtuple('Player', ('name year first_year team college active '
                               'games avg_min avg_points'))

conn = sqlite3.connect(DB)
cur = conn.cursor()


def import_data():
    with requests.Session() as session:
        content = session.get(DATA_URL).content.decode('utf-8')

    reader = csv.DictReader(content.splitlines(), delimiter=',')

    players = []
    for row in reader:
        players.append(Player(name=row['Player'],
                              year=row['Draft_Yr'],
                              first_year=row['first_year'],
                              team=row['Team'],
                              college=row['College'],
                              active=row['Yrs'],
                              games=row['Games'],
                              avg_min=row['Minutes.per.Game'],
                              avg_points=row['Points.per.Game']))

    cur.execute('''CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)''')
    cur.executemany('INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)', players)
    conn.commit()


if DB.stat().st_size == 0:
    print('loading data')
    import_data()


# you code:

def player_with_max_points_per_game():
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    # SELECT
    avg_points = cur.execute('SELECT name, avg_points FROM players')
    # Cast avg_points to float
    avg_points = [(player[0], float(player[1])) for player in avg_points]
    # Sort avg_points descending
    avg_points = sorted(avg_points, key=lambda x: x[1], reverse=True)
    # Return name
    return avg_points[0][0]


def number_of_players_from_duke():
    """Return the number of players with college == Duke University"""
    college = ('Duke University',)
    cur.execute('SELECT college FROM players WHERE college=?', college)
    return len(cur.fetchall())


def avg_years_active_players_stanford():
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    college = ('Stanford University',)
    years = cur.execute('SELECT active FROM players WHERE college=?', college)
    players = 0
    total_years = 0
    for row in years:
        players += 1
        total_years += int(row[0])
    return round(total_years / players, 2)


def year_with_most_drafts():
    """Return the year with the most drafts, in SQL you can use GROUP BY"""
    cur.execute('SELECT year, COUNT(year) FROM players GROUP BY year')
    return int(sorted(cur.fetchall(), key=lambda x: x[1], reverse=True)[0][0])
