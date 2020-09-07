from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    c = Counter()
    with open(commits) as f:
        reader = f.readlines()
        rows = [row for row in reader]
    for row in rows:
        row = row.split(',')
        d = row[0].replace('Date:   ', '').split('|')[0].strip()
        d = parse(d)
        d = d.strftime('%Y-%m')
        try:
            ins_del = (int(row[1].strip().split()[0])
                       + int(row[2].strip().split()[0]))
        except IndexError:
            ins_del = int(row[1].strip().split()[0])
        c[d] += ins_del
    if year:
        c = {k: v for k, v in c.items() if k.startswith(str(year))}
        return (min(c, key=c.get), max(c, key=c.get))
    return (c.most_common()[-1][0], c.most_common(1)[0][0])
