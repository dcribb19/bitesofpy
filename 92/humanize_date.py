from collections import namedtuple
from datetime import datetime, time, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError
    delta = NOW - date
    if delta < timedelta(seconds=(TIME_OFFSETS[0].offset)):
        return TIME_OFFSETS[0].date_str
    elif delta < timedelta(seconds=TIME_OFFSETS[1].offset):
        return TIME_OFFSETS[1].date_str.format(delta.seconds)
    elif delta < timedelta(seconds=TIME_OFFSETS[2].offset):
        return TIME_OFFSETS[2].date_str
    elif delta < timedelta(seconds=TIME_OFFSETS[3].offset):
        return TIME_OFFSETS[3].date_str.format(int(delta.seconds/TIME_OFFSETS[3].divider))
    elif delta < timedelta(seconds=TIME_OFFSETS[4].offset):
        return TIME_OFFSETS[4].date_str.format(int(delta.seconds/TIME_OFFSETS[3].divider))
    elif delta < timedelta(seconds=TIME_OFFSETS[5].offset):
        return TIME_OFFSETS[5].date_str.format(int(delta.seconds/TIME_OFFSETS[5].divider))
    elif delta < timedelta(seconds=TIME_OFFSETS[6].offset):
        return TIME_OFFSETS[6].date_str
    else:
        return (NOW - delta).strftime('%m/%d/%y')
