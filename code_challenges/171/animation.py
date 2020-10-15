from itertools import cycle
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    start = time()
    spin = cycle(SPINNER_STATES)
    while time() - start < seconds:
        print(next(spin), end='\r', flush=True)
        sleep(STATE_TRANSITION_TIME)


if __name__ == '__main__':
    spinner(2)
