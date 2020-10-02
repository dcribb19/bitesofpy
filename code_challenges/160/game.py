import csv
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat_mapping = dict()
    with open(BATTLE_DATA) as f:
        reader = csv.reader(f)

        attackers = next(reader)
        defeat_mapping[attackers[0]] = attackers[1:]

        for row in reader:
            defeat_mapping[row[0]] = row[1:]

    return defeat_mapping


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()

    if (player1 not in defeat_mapping.keys() or
       player2 not in defeat_mapping.keys()):
        raise ValueError

    attack = defeat_mapping['Attacker'].index(player1)
    result = defeat_mapping[player2][attack]

    if result == 'win':
        return player2
    elif result == 'lose':
        return player1
    else:
        return 'Tie'
