from collections import namedtuple
from pathlib import Path
from typing import List
from urllib.request import urlretrieve

tmp = Path('/tmp')
timings_log = tmp / 'pytest_timings.out'
if not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )

Bite = namedtuple('Bite', 'number, num_tests, seconds')


def _filter_data(timings: List[str]) -> List[Bite]:
    '''Convert list of strings to list of Bite namedtuples'''
    bites = []
    for line in timings:
        if 'error' in line or 'no tests' in line:
            continue
        elif 'warning' in line:
            bite, _, num_passed, _, _, _, _, seconds, _, _ = line.split()
        else:  # only tests that have passed
            bite, _, num_passed, _, _, seconds, _, _ = line.split()
        bites.append(Bite(number=bite,
                          num_tests=int(num_passed),
                          seconds=float(seconds)
                          )
                     )
    return bites


def get_bite_with_fastest_avg_test(timings: List[str]) -> str:
    """Return the bite which has the fastest average time per test"""
    bites = _filter_data(timings)
    speeds = []
    for bite in bites:
        speed = bite.seconds / bite.num_tests
        speeds.append([speed, bite])
    return sorted(speeds)[0][1].number


if __name__ == '__main__':
    with open(timings_log) as f:
        bites = f.readlines()
    print(get_bite_with_fastest_avg_test(bites))
