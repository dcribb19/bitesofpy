import pandas as pd
from pathlib import Path
from typing import Dict

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
TMP = Path('/tmp')


def get_belts(data: str) -> Dict[str, str]:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """
    data = pd.read_json(data)
    data = data.sort_values(by='date')
    data['total'] = data['score'].cumsum()

    belts = {}
    for row in data.itertuples():
        for score in SCORES:
            if (row.total >= score and
                    BELTS[SCORES.index(score)] not in belts.keys()):
                belts[BELTS[SCORES.index(score)]] = row.date

    for k, v in belts.items():
        belts[k] = v.strftime('%B %d, %Y')

    return belts
