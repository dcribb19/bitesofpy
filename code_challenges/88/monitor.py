from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()


def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    start = time()
    dt = get_today()
    timed = time() - start
    try:
        yield timed
    finally:
        if timed >= OPERATION_THRESHOLD_IN_SECONDS:
            violations[dt] += 1
            if violations.most_common(1)[0][1] >= ALERT_THRESHOLD:
                print(ALERT_MSG)
