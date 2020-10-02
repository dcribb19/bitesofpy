import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = '/tmp'


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    date_str = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
    # remove timezone
    date_str = date_str.replace(tzinfo=None)
    return date_str


def get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    format_dates = [date.strftime('%Y-%m') for date in dates]
    return collections.Counter(format_dates).most_common(1)[0][0]
    