from collections import namedtuple, Counter
from datetime import datetime, timedelta
import feedparser
from math import floor
import re
from statistics import mean
from typing import NamedTuple

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


class PythonBytes:
    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(url).entries

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        return [ep.itunes_episode
                for ep in self.entries
                if domain.lower() in ep.summary.lower()]

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        rex = re.compile(r'https?://[^/]+')
        c = Counter()

        for entry in self.entries:
            domains = set(re.findall(rex, entry.summary))
            for domain in domains:
                if domain not in IGNORE_DOMAINS:
                    c[domain] += 1

        return c.most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        return len([ep for ep in self.entries if SPECIAL_GUEST in ep.summary])

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        times = [ep.itunes_duration for ep in self.entries]
        format_times = []

        for time in times:
            if not time.startswith('00'):
                time = '0' + time
            format_times.append(time)

        dts = [datetime.strptime(x, '%H:%M:%S') for x in format_times]
        secs = [timedelta(
            hours=x.hour,
            minutes=x.minute,
            seconds=x.second
            ).seconds for x in dts]

        return Duration(
            floor(mean(secs)),
            max(format_times),
            min(format_times)
        )
