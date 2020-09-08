import csv
import os
from pathlib import Path
from urllib.request import urlretrieve
import re

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        # get rid of headers
        _ = next(reader)
        rows = [row for row in reader]
        rows = [[re.search(r'\d+', row[0]).group(0), float(row[1])]
                for row in rows if row[1] != 'None'
                ]
        rows = sorted(rows, key=lambda x: x[1], reverse=True)
    return [row[0] for row in rows][:N]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
